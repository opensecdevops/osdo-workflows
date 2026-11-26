#!/usr/bin/env python3
"""Validate every `uses:` reference in .github/workflows/*.yml.

For each remote reference owner/repo[/path]@ref this checks that:
  - ref is a full 40-hex commit SHA (no tags, branches or short SHAs);
  - the action (action.yml/action.yaml) or reusable workflow (.yml) exists
    at that SHA, fetched from raw.githubusercontent.com (HTTP 200);
  - every `with:` key the caller passes exists in the callee's inputs;
  - every required callee input without a default is passed.
For local references (./...) it checks the file exists and, for reusable
workflows, validates `with:` against `on.workflow_call.inputs`.

Exit status is 1 if any check fails. Requires PyYAML.
"""
import glob
import re
import sys
import urllib.error
import urllib.request

import yaml

WORKFLOWS_GLOB = ".github/workflows/*.yml"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_cache = {}


def fetch(url):
    if url not in _cache:
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                _cache[url] = resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            _cache[url] = exc.code
        except urllib.error.URLError as exc:
            _cache[url] = f"error: {exc.reason}"
    return _cache[url]


def load_callee_inputs(text, is_workflow):
    doc = yaml.safe_load(text)
    if is_workflow:
        on = doc.get(True, doc.get("on")) or {}
        spec = (on.get("workflow_call") or {}).get("inputs") or {}
    else:
        spec = doc.get("inputs") or {}
    return spec


def check_with(label, with_keys, spec, errors):
    for key in with_keys:
        if key not in spec:
            errors.append(f"{label}: input '{key}' does not exist in callee")
    for name, meta in spec.items():
        meta = meta or {}
        if meta.get("required") and "default" not in meta and name not in with_keys:
            errors.append(f"{label}: required input '{name}' not passed")


def check_remote(label, ref_str, with_keys, errors):
    target, _, ref = ref_str.rpartition("@")
    parts = target.split("/")
    owner, repo = parts[0], parts[1]
    subpath = "/".join(parts[2:])
    if not SHA_RE.match(ref):
        errors.append(f"{label}: '{ref_str}' is not pinned by full SHA")
        return
    base = f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}"
    if subpath.endswith(".yml") or subpath.endswith(".yaml"):
        candidates = [(f"{base}/{subpath}", True)]
    else:
        prefix = f"/{subpath}" if subpath else ""
        candidates = [(f"{base}{prefix}/action.yml", False),
                      (f"{base}{prefix}/action.yaml", False)]
    for url, is_wf in candidates:
        body = fetch(url)
        if isinstance(body, str) and not body.startswith("error"):
            spec = load_callee_inputs(body, is_wf)
            check_with(label, with_keys, spec, errors)
            return
    errors.append(f"{label}: '{ref_str}' not found at SHA (HTTP {fetch(candidates[0][0])})")


def main():
    errors = []
    checked = 0
    for path in sorted(glob.glob(WORKFLOWS_GLOB)):
        doc = yaml.safe_load(open(path, encoding="utf-8"))
        on = doc.get(True, doc.get("on")) or {}
        local_spec = None
        if isinstance(on, dict) and "workflow_call" in on:
            local_spec = (on["workflow_call"] or {}).get("inputs") or {}
        for job_name, job in (doc.get("jobs") or {}).items():
            refs = []
            if "uses" in job:
                refs.append((f"{path}:{job_name}", job["uses"], list((job.get("with") or {}).keys()), True))
            for idx, step in enumerate(job.get("steps") or []):
                if "uses" in step:
                    label = f"{path}:{job_name}:step{idx}"
                    refs.append((label, step["uses"], list((step.get("with") or {}).keys()), False))
            for label, uses, with_keys, is_job in refs:
                checked += 1
                if uses.startswith("./"):
                    if not __import__("os").path.exists(uses[2:]):
                        errors.append(f"{label}: local path '{uses}' does not exist")
                    elif is_job:
                        callee = yaml.safe_load(open(uses[2:], encoding="utf-8"))
                        con = callee.get(True, callee.get("on")) or {}
                        check_with(label, with_keys, (con.get("workflow_call") or {}).get("inputs") or {}, errors)
                    continue
                check_remote(label, uses, with_keys, errors)
    print(f"checked {checked} uses: references in {len(glob.glob(WORKFLOWS_GLOB))} workflow files")
    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for e in errors:
            print("  -", e)
        return 1
    print("OK: all references resolve and all with-inputs exist")
    return 0


if __name__ == "__main__":
    sys.exit(main())
