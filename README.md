English | [Español](README.es.md)

# 🔒 OSDO Workflows — Reusable Security Workflows for GitHub Actions

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/opensecdevops/osdo-workflows/badge)](https://securityscorecards.dev/viewer/?uri=github.com/opensecdevops/osdo-workflows)

> **10 composable, reusable GitHub Actions workflows** covering the full application security spectrum — from SAST and SCA to container scanning, IaC analysis, DAST, API security, mobile security, cloud security, license compliance, and continuous monitoring.

## What Is This?

`osdo-workflows` is a library of reusable [GitHub Actions reusable workflows](https://docs.github.com/en/actions/sharing-automations/reusing-workflows) maintained by the [OpenSecDevOps](https://github.com/opensecdevops) community. Each workflow targets a specific security domain and is designed to be called from any repository with a single `uses:` reference — no copy-paste, no drift.

Compose them individually or combine multiple workflows into a comprehensive security pipeline tailored to your stack.

## Workflow Catalog

| # | Workflow File | Purpose |
|---|---------------|---------|
| 1 | `osdo-framework.yml` | **Complete CI/CD security pipeline** — tests, SAST, SCA, SBOM generation, and compliance reporting in a single call |
| 2 | `osdo-container-security.yml` | **Container image scanning** — Trivy, Grype, Dockerfile linting, SBOM (SPDX/CycloneDX), and Cosign image signing |
| 3 | `osdo-iac-security.yml` | **Infrastructure-as-Code security** — Checkov, KICS, tfsec, Terrascan; covers Terraform, Kubernetes, CloudFormation, Helm, and Ansible |
| 4 | `osdo-supply-chain.yml` | **Supply chain security** — SBOM generation & validation, SLSA provenance (Levels 1–4), malware detection, and typosquatting checks |
| 5 | `osdo-continuous-monitoring.yml` | **Scheduled security monitoring** — recurring vulnerability re-scans, trend analysis, multi-channel alerts, and automatic GitHub Issues |
| 6 | `osdo-dast.yml` | **Dynamic Application Security Testing** — OWASP ZAP scans (baseline/full/API), SSL/TLS checks, and security header validation |
| 7 | `osdo-api-security.yml` | **API security testing** — OpenAPI/Swagger spec validation, OWASP API Top 10, auth testing, rate-limit verification, and API fuzzing |
| 8 | `osdo-mobile-security.yml` | **Mobile application security** — OWASP MASVS (L1/L2) for Android, iOS, React Native, and Flutter; SSL pinning and obfuscation checks |
| 9 | `osdo-cloud-security.yml` | **Multi-cloud security posture** — AWS, Azure, and GCP resource scanning; IAM analysis, CIS Benchmarks, and public-exposure detection |
| 10 | `osdo-license-compliance.yml` | **License compliance enforcement** — policy allow/deny lists, copyleft detection, compatibility checks, and NOTICE file generation |

## Quick Start

Reference any workflow with `uses:` in your own repository's workflow file.

**Simplest setup — full security pipeline in one call:**

```yaml
# .github/workflows/security.yml
name: Security Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    secrets: inherit
```

**Composing individual security domains:**

```yaml
# .github/workflows/security.yml
name: Security Pipeline

on: [push, pull_request]

jobs:
  container-scan:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      image-name: my-app
      image-tag: ${{ github.sha }}
      enable-sbom: true
      enable-signing: true
      critical-threshold: "0"

  iac-scan:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      iac-type: terraform
      iac-directory: ./infra
      compliance-frameworks: "cis,nist"

  supply-chain:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      package-manager: npm
      slsa-level: "2"
      enable-sbom-generation: true
```

> **Tip — pin by full commit SHA in production:** see [Pin Versions](#3-pin-versions). `@v2` is a mutable ref, and `@v2.0.0` references composite actions that do not exist (HOL-265).

## Full Documentation

📖 [OSDO Documentation Hub](https://github.com/opensecdevops/osdo) — complete configuration reference, integration patterns, and best practices.

---

## Table of Contents

- [Overview](#overview)
- [Available Workflows](#available-workflows)
- [Workflow Reference](#workflow-reference)
- [Integration Patterns](#integration-patterns)
- [Configuration Guide](#configuration-guide)
- [Best Practices](#best-practices)

---

## Overview

OSDO Workflows provides a comprehensive suite of **10 specialized security workflows** designed to be reusable through `workflow_call`. Each workflow focuses on a specific security domain, which lets you:

- ✅ **Pick what you need** — use only what you require
- ✅ **Combine workflows** — build complete security pipelines
- ✅ **Customize** — extensive input parameters for flexibility
- ✅ **Scale** — from individual projects to enterprise deployments

---

## Available Workflows

| Workflow | Purpose | Key Features |
|----------|---------|--------------|
| **[osdo-framework.yml](#1-osdo-framework)** | Complete CI/CD pipeline | Tests, security, compliance, reporting |
| **[osdo-container-security.yml](#2-container-security)** | Container security | Trivy, Grype, SBOM, signing |
| **[osdo-iac-security.yml](#3-infrastructure-as-code-security)** | IaC security | Terraform, K8s, CloudFormation, drift detection |
| **[osdo-supply-chain.yml](#4-supply-chain-security)** | Supply chain security | SBOM, provenance, SLSA, malware detection |
| **[osdo-continuous-monitoring.yml](#5-continuous-monitoring)** | Security monitoring | Trend analysis, alerts, auto-remediation |
| **[osdo-dast.yml](#6-dast)** | Dynamic application testing | OWASP ZAP, SSL/TLS, security headers |
| **[osdo-api-security.yml](#7-api-security)** | API security | OWASP API Top 10, schema validation |
| **[osdo-mobile-security.yml](#8-mobile-security)** | Mobile application security | MASVS compliance, iOS/Android |
| **[osdo-cloud-security.yml](#9-cloud-security)** | Cloud security | AWS/Azure/GCP, IAM, compliance |
| **[osdo-license-compliance.yml](#10-license-compliance)** | License management | Policy enforcement, compatibility checks |

---

## Workflow Reference

### 1. OSDO Framework

**Complete, all-in-one security and compliance pipeline.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  node-version: '22'
  run-tests: true
  run-security-scan: true
  test-coverage-threshold: '80'
  critical-threshold: '0'
  high-threshold: '5'
```

**Key Features:**
- Complete CI/CD pipeline
- Tests, quality gates and security analysis
- SBOM generation
- Compliance reporting

---

### 2. Container Security

**Thorough security analysis and hardening of container images.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  image-name: my-app
  image-tag: v1.0.0
  scanners: "trivy,grype"
  enable-sbom: true
  enable-signing: true
  critical-threshold: "0"
```

**Key Features:**
- Multi-scanner support (Trivy, Grype, Snyk)
- Static analysis of Dockerfiles
- SBOM generation (SPDX/CycloneDX)
- Image signing with Cosign
- Secret detection in images
- CIS compliance checks

**Outputs:**
- `vulnerabilities-found` — Total vulnerabilities
- `critical-count` — Critical vulnerabilities
- `image-signed` — Signing status
- `security-score` — Overall score (0-100)

---

### 3. Infrastructure-as-Code Security

**Security analysis for Terraform, Kubernetes, CloudFormation and more.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  iac-type: terraform
  iac-directory: "./terraform"
  scanners: "all"
  compliance-frameworks: "cis,nist,pci-dss"
  enable-drift-detection: true
```

**Key Features:**
- Multi-tool analysis (Checkov, KICS, tfsec, Terrascan)
- Kubernetes manifest validation
- Policy as Code enforcement
- Infrastructure drift detection
- Multi-cloud support
- Remediation guidance

**Outputs:**
- `violations-found` — Total violations
- `compliance-score` — Compliance percentage
- `drift-detected` — Drift status

---

### 4. Supply Chain Security

**Complete software supply chain security and SBOM management.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  package-manager: npm
  enable-sbom-generation: true
  provenance-verification: true
  slsa-level: "2"
  malware-scan: true
  typosquatting-detection: true
```

**Key Features:**
- SBOM generation and validation
- Provenance verification
- SLSA compliance (Levels 1–4)
- Malware and typosquatting detection
- License compliance checks
- Build attestation
- Reachability analysis

**Outputs:**
- `sbom-valid` — SBOM validation status
- `slsa-level-achieved` — SLSA level achieved
- `malicious-packages` — Count of malicious packages
- `security-score` — Supply chain score

---

### 5. Continuous Monitoring

**Scheduled security monitoring with trend analysis and alerting.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-continuous-monitoring.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  monitoring-scope: all
  alert-channels: "github,slack"
  trending-period: "30d"
  auto-create-issues: true
```

**Key Features:**
- Scheduled vulnerability re-scanning
- Trend analysis and security posture tracking
- Multi-channel alerts
- Automatic issue creation
- Remediation tracking
- Comparison with previous scans

**Outputs:**
- `new-vulnerabilities` — New vulnerabilities since the last scan
- `security-score` — Current score
- `trend-direction` — improving/degrading/stable

---

### 6. DAST

**Dynamic application security testing for running applications.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-dast.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  target-url: https://app.example.com
  scan-type: full
  owasp-top-10: true
  check-ssl-tls: true
  api-spec: "./openapi.yaml"
```

**Key Features:**
- OWASP ZAP scanning
- OWASP Top 10 detection
- SSL/TLS configuration testing
- Security header validation
- Content Security Policy checks
- API-specific tests

**Outputs:**
- `vulnerabilities-found` — Total vulnerabilities
- `owasp-violations` — OWASP Top 10 issues
- `risk-score` — Application risk score

---

### 7. API Security

**Specialized security testing for REST, GraphQL and gRPC APIs.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-api-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  api-spec-path: "./openapi.yaml"
  api-type: REST
  base-url: https://api.example.com
  owasp-api-top-10: true
  rate-limiting-test: true
  api-fuzzing: true
```

**Key Features:**
- OpenAPI/Swagger specification validation
- OWASP API Security Top 10
- Authentication and authorization testing
- Rate-limit verification
- Schema validation
- GraphQL-specific tests
- API fuzzing

**Outputs:**
- `security-score` — API security score
- `owasp-violations` — API Top 10 violations
- `auth-issues` — Authentication issues

---

### 8. Mobile Security

**Security analysis for Android, iOS, React Native and Flutter applications.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-mobile-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  platform: android
  binary-path: ./app-release.apk
  masvs-level: L2
  check-ssl-pinning: true
  check-obfuscation: true
```

**Key Features:**
- OWASP MASVS compliance (L1/L2)
- Static and binary analysis
- SSL pinning verification
- Code obfuscation checks
- Root/jailbreak detection
- Permission analysis
- Embedded secret detection

**Outputs:**
- `security-score` — Mobile security score
- `masvs-compliance` — MASVS compliance status
- `critical-issues` — Critical security issues

---

### 9. Cloud Security

**Multi-cloud security analysis for AWS, Azure and GCP.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  cloud-provider: aws
  regions: "us-east-1,us-west-2"
  iam-analysis: true
  compliance-frameworks: "cis,nist"
  public-exposure-check: true
```

**Key Features:**
- Multi-cloud support (AWS/Azure/GCP)
- IAM policy analysis
- Network security assessment
- Encryption verification
- Public exposure detection
- CIS Benchmarks compliance
- Cost-security analysis

**Outputs:**
- `misconfigurations-found` — Total misconfigurations
- `compliance-score` — Compliance percentage
- `iam-issues` — IAM security issues
- `cost-impact` — Estimated remediation cost

---

### 10. License Compliance

**Software license management and compliance enforcement.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-license-compliance.yml@<FULL-COMMIT-SHA> # vX.Y.Z
with:
  package-manager: npm
  allowed-licenses: "MIT,Apache-2.0,BSD-3-Clause"
  denied-licenses: "GPL-3.0,AGPL-3.0"
  generate-notice-file: true
  compatibility-check: true
```

**Key Features:**
- Multi-language support
- License policy enforcement
- Copyleft license detection
- Compatibility verification
- NOTICE file generation
- SBOM with license information
- Automated compliance reports

**Outputs:**
- `total-licenses` — Unique licenses found
- `denied-licenses-found` — Policy violations
- `compliance-status` — Overall status

---

## Integration Patterns

### Pattern 1: Full-Stack Security

```yaml
name: Full Stack Security

on: [push, pull_request]

jobs:
  # Code & Dependencies
  supply-chain:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      package-manager: all
      slsa-level: "2"

  # Containers
  containers:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      image-name: ${{ github.repository }}
      enable-signing: true

  # Infrastructure
  infrastructure:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      iac-type: all

  # Cloud Resources
  cloud:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      cloud-provider: aws
      compliance-frameworks: "cis,pci-dss"

  # Licenses
  licenses:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-license-compliance.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      fail-on-denied: true
```

### Pattern 2: Scheduled Monitoring

```yaml
name: Security Monitoring

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  monitor:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-continuous-monitoring.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      monitoring-scope: all
      alert-channels: "github,slack"
      auto-create-issues: true
```

### Pattern 3: Pre-Production Validation

```yaml
name: Pre-Production Security

on:
  pull_request:
    branches: [main]

jobs:
  api-security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-api-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      base-url: https://staging.api.example.com
      owasp-api-top-10: true

  dast:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-dast.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    with:
      target-url: https://staging.example.com
      scan-type: full
```

---

## Configuration Guide

### Workflow Selection Matrix

| Need | Recommended Workflow(s) |
|------|------------------------|
| **General CI/CD** | osdo-framework |
| **Docker/Kubernetes** | osdo-container-security |
| **Terraform/IaC** | osdo-iac-security |
| **Dependencies** | osdo-supply-chain |
| **Running application** | osdo-dast |
| **REST/GraphQL API** | osdo-api-security |
| **Mobile application** | osdo-mobile-security |
| **AWS/Azure/GCP** | osdo-cloud-security |
| **Open-source licenses** | osdo-license-compliance |
| **Continuous monitoring** | osdo-continuous-monitoring |

### Common Configuration Profiles

#### High-Security Project
```yaml
with:
  critical-threshold: "0"
  high-threshold: "0"
  fail-on-high: true
  fail-on-critical: true
  slsa-level: "3"
```

#### Balanced Approach
```yaml
with:
  critical-threshold: "0"
  high-threshold: "10"
  fail-on-high: false
  slsa-level: "2"
```

#### Permissive (Development)
```yaml
with:
  critical-threshold: "5"
  high-threshold: "20"
  fail-on-high: false
  slsa-level: "1"
```

---

## Best Practices

### 1. Start Simple, Scale Gradually

Start with the **osdo-framework** workflow, then add specialized workflows as needed.

### 2. Use Secrets Correctly

Always use GitHub Secrets for sensitive data:

```yaml
jobs:
  cloud-security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@<FULL-COMMIT-SHA> # vX.Y.Z
    secrets: inherit
```

### 3. Pin Versions

Pin each reusable workflow to a **full 40-character commit SHA** and keep the release tag in a comment. Branch-style refs such as `@v2` are mutable. The `v2.0.0` tag calls composite actions that do not exist (HOL-265), so use the first release published after that fix. Resolve the SHA of a tag with:

```bash
git ls-remote https://github.com/opensecdevops/osdo-workflows "refs/tags/vX.Y.Z^{}"
```

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@<FULL-COMMIT-SHA> # vX.Y.Z
```

The workflows here call `opensecdevops/osdo-actions` pinned to its `v2.0.0` commit `cb95b82420cf2982af9669720ce4a4a06bf88090`. Replace `vX.Y.Z` and `<FULL-COMMIT-SHA>` with the release that contains the HOL-265 fix.

### 4. Combine With Judgment

Don't run every workflow on every event:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * 1'  # Weekly monitoring
```

### 5. Track Trends

Use `osdo-continuous-monitoring` for long-term tracking of your security posture.

---

## Workflow Comparison

| Feature | Framework | Container | IaC | Supply Chain | Mobile | Cloud |
|---------|-----------|-----------|-----|--------------|--------|-------|
| **Scope** | Complete | Containers | Infrastructure | Dependencies | Applications | Cloud resources |
| **Complexity** | High | Medium | Medium | High | Medium | High |
| **Setup Time** | 5 min | 2 min | 3 min | 5 min | 10 min | 15 min |
| **Languages** | All | N/A | Multiple | All | iOS/Android | N/A |
| **SBOM** | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Compliance** | ✅ | ✅ | ✅ | ✅ | ✅ (MASVS) | ✅ (CIS) |

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](https://github.com/opensecdevops/.github/blob/main/CONTRIBUTING.md) for details.

---

## 📄 License

Apache License 2.0 — see [LICENSE](LICENSE) for details.

---

## 🔗 Related Projects

- **[osdo-actions](https://github.com/opensecdevops/osdo-actions)** - Granular GitHub Actions
- **osdo-workflow-template** - Framework with predefined conventions
- **[OSDO Documentation](https://github.com/opensecdevops/osdo)** - Complete documentation hub

---

**Made with ❤️ by the OpenSecDevOps Community**

*Last updated: December 2025*
