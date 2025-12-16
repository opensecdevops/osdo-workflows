# 🔒 OSDO Workflows - Reusable Security Workflows

Comprehensive collection of specialized, reusable GitHub Actions workflows for security, compliance, and quality assurance across diverse technology stacks.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Available Workflows](#available-workflows)
- [Quick Start](#quick-start)
- [Workflow Catalog](#workflow-catalog)
- [Usage Examples](#usage-examples)
- [Integration Patterns](#integration-patterns)
- [Configuration Guide](#configuration-guide)
- [Best Practices](#best-practices)

---

## 🎯 Overview

OSDO Workflows provides a comprehensive suite of **10 specialized security workflows** designed to be reusable via `workflow_call`. Each workflow focuses on a specific security domain, allowing you to:

- ✅ **Pick and Choose** - Use only what you need
- ✅ **Combine Workflows** - Build comprehensive security pipelines
- ✅ **Customize** - Extensive input parameters for flexibility
- ✅ **Scale** - From single projects to enterprise-wide deployments

---

## 📦 Available Workflows

| Workflow | Purpose | Key Features |
|----------|---------|--------------|
| **[osdo-framework.yml](#1-osdo-framework)** | Complete CI/CD pipeline | Tests, security, compliance, reporting |
| **[osdo-container-security.yml](#2-container-security)** | Container security | Trivy, Grype, SBOM, signing |
| **[osdo-iac-security.yml](#3-infrastructure-as-code-security)** | IaC security | Terraform, K8s, CloudFormation, drift detection |
| **[osdo-supply-chain.yml](#4-supply-chain-security)** | Supply chain security | SBOM, provenance, SLSA, malware detection |
| **[osdo-continuous-monitoring.yml](#5-continuous-monitoring)** | Security monitoring | Trend analysis, alerting, auto-remediation |
| **[osdo-dast.yml](#6-dast)** | Dynamic app testing | OWASP ZAP, SSL/TLS, security headers |
| **[osdo-api-security.yml](#7-api-security)** | API security | OWASP API Top 10, schema validation |
| **[osdo-mobile-security.yml](#8-mobile-security)** | Mobile app security | MASVS compliance, iOS/Android |
| **[osdo-cloud-security.yml](#9-cloud-security)** | Cloud security | AWS/Azure/GCP, IAM, compliance |
| **[osdo-license-compliance.yml](#10-license-compliance)** | License management | Policy enforcement, compatibility check |

---

## 🚀 Quick Start

### Basic Usage

```yaml
# .github/workflows/security.yml
name: Security Pipeline

on: [push, pull_request]

jobs:
  security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@v1
    secrets: inherit
```

### Multi-Workflow Approach

```yaml
# .github/workflows/comprehensive-security.yml
name: Comprehensive Security

on: [push, pull_request]

jobs:
  # Container Security
  containers:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@v1
    with:
      image-name: my-app
      image-tag: latest

  # Supply Chain
  supply-chain:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@v1
    with:
      package-manager: npm
      slsa-level: "2"

  # IaC Security
  infrastructure:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@v1
    with:
      iac-type: terraform
      compliance-frameworks: "cis,nist"
```

---

## 📖 Workflow Catalog

### 1. OSDO Framework

**Complete security and compliance pipeline with everything included.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@v1
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
- Tests, quality gates, security scans
- SBOM generation
- Compliance reporting

---

### 2. Container Security

**Comprehensive container image security scanning and hardening.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@v1
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
- Dockerfile linting
- SBOM generation (SPDX/CycloneDX)
- Image signing with Cosign
- Secrets detection in images
- CIS compliance checks

**Outputs:**
- `vulnerabilities-found` - Total vulnerabilities
- `critical-count` - Critical vulnerabilities
- `image-signed` - Signing status
- `security-score` - Overall score (0-100)

---

### 3. Infrastructure as Code Security

**Security analysis for Terraform, Kubernetes, CloudFormation, and more.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@v1
with:
  iac-type: terraform
  iac-directory: "./terraform"
  scanners: "all"
  compliance-frameworks: "cis,nist,pci-dss"
  enable-drift-detection: true
```

**Key Features:**
- Multi-tool scanning (Checkov, KICS, tfsec, Terrascan)
- Kubernetes manifest validation
- Policy as Code enforcement
- Infrastructure drift detection
- Multi-cloud support
- Remediation guidance

**Outputs:**
- `violations-found` - Total violations
- `compliance-score` - Compliance percentage
- `drift-detected` - Drift status

---

### 4. Supply Chain Security

**Complete software supply chain security and SBOM management.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@v1
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
- SLSA compliance (Levels 1-4)
- Malware and typosquatting detection
- License compliance checks
- Build attestation
- Reachability analysis

**Outputs:**
- `sbom-valid` - SBOM validation status
- `slsa-level-achieved` - SLSA level
- `malicious-packages` - Malware count
- `security-score` - Supply chain score

---

### 5. Continuous Monitoring

**Scheduled security monitoring with trend analysis and alerting.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-continuous-monitoring.yml@v1
with:
  monitoring-scope: all
  alert-channels: "github,slack"
  trending-period: "30d"
  auto-create-issues: true
```

**Key Features:**
- Scheduled vulnerability rescanning
- Trend analysis and security posture tracking
- Multi-channel alerting
- Automated issue creation
- Remediation tracking
- Comparison with previous scans

**Outputs:**
- `new-vulnerabilities` - New vulns since last scan
- `security-score` - Current score
- `trend-direction` - improving/degrading/stable

---

### 6. DAST

**Dynamic Application Security Testing for running applications.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-dast.yml@v1
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
- Security headers validation
- Content Security Policy checks
- API-specific testing

**Outputs:**
- `vulnerabilities-found` - Total vulnerabilities
- `owasp-violations` - OWASP Top 10 issues
- `risk-score` - Application risk score

---

### 7. API Security

**Specialized security testing for REST, GraphQL, and gRPC APIs.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-api-security.yml@v1
with:
  api-spec-path: "./openapi.yaml"
  api-type: REST
  base-url: https://api.example.com
  owasp-api-top-10: true
  rate-limiting-test: true
  api-fuzzing: true
```

**Key Features:**
- OpenAPI/Swagger spec validation
- OWASP API Security Top 10
- Authentication/Authorization testing
- Rate limiting verification
- Schema validation
- GraphQL-specific tests
- API fuzzing

**Outputs:**
- `security-score` - API security score
- `owasp-violations` - API Top 10 violations
- `auth-issues` - Authentication problems

---

### 8. Mobile Security

**Security analysis for Android, iOS, React Native, and Flutter apps.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-mobile-security.yml@v1
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
- Permissions analysis
- Hardcoded secrets detection

**Outputs:**
- `security-score` - Mobile security score
- `masvs-compliance` - MASVS compliance status
- `critical-issues` - Critical security issues

---

### 9. Cloud Security

**Multi-cloud security scanning for AWS, Azure, and GCP.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@v1
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
- `misconfigurations-found` - Total misconfigurations
- `compliance-score` - Compliance percentage
- `iam-issues` - IAM security issues
- `cost-impact` - Remediation cost estimate

---

### 10. License Compliance

**Software license management and compliance enforcement.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-license-compliance.yml@v1
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
- Compatibility checking
- NOTICE file generation
- SBOM with license info
- Automated compliance reporting

**Outputs:**
- `total-licenses` - Unique licenses found
- `denied-licenses-found` - Policy violations
- `compliance-status` - Overall status

---

## 🎨 Integration Patterns

### Pattern 1: Full Stack Security

```yaml
name: Full Stack Security

on: [push, pull_request]

jobs:
  # Code & Dependencies
  supply-chain:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@v1
    with:
      package-manager: all
      slsa-level: "2"

  # Containers
  containers:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@v1
    with:
      image-name: ${{ github.repository }}
      enable-signing: true

  # Infrastructure
  infrastructure:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@v1
    with:
      iac-type: all

  # Cloud Resources
  cloud:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@v1
    with:
      cloud-provider: aws
      compliance-frameworks: "cis,pci-dss"

  # Licenses
  licenses:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-license-compliance.yml@v1
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
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-continuous-monitoring.yml@v1
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
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-api-security.yml@v1
    with:
      base-url: https://staging.api.example.com
      owasp-api-top-10: true

  dast:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-dast.yml@v1
    with:
      target-url: https://staging.example.com
      scan-type: full
```

---

## ⚙️ Configuration Guide

### Workflow Selection Matrix

| Need | Recommended Workflow(s) |
|------|------------------------|
| **General CI/CD** | osdo-framework |
| **Docker/Kubernetes** | osdo-container-security |
| **Terraform/IaC** | osdo-iac-security |
| **Dependencies** | osdo-supply-chain |
| **Running App** | osdo-dast |
| **REST/GraphQL API** | osdo-api-security |
| **Mobile App** | osdo-mobile-security |
| **AWS/Azure/GCP** | osdo-cloud-security |
| **Open Source Licenses** | osdo-license-compliance |
| **Continuous Monitoring** | osdo-continuous-monitoring |

### Common Configuration Patterns

#### High Security Project
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

## 🎯 Best Practices

### 1. Start Simple, Scale Up

Begin with the **osdo-framework** workflow, then add specialized workflows as needed.

### 2. Use Secrets Properly

Always use GitHub Secrets for sensitive data:

```yaml
jobs:
  cloud-security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@v1
    secrets: inherit
```

### 3. Pin Versions

Use specific versions or tags for production:

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@v1.2.0
```

### 4. Combine Wisely

Don't run every workflow on every Event:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * 1'  # Weekly monitoring
```

### 5. Monitor Trends

Use continuous-monitoring for long-term security posture tracking.

---

## 📊 Workflow Comparison

| Feature | Framework | Container | IaC | Supply Chain | Mobile | Cloud |
|---------|-----------|-----------|-----|--------------|--------|-------|
| **Scope** | Complete | Containers | Infrastructure | Dependencies | Apps | Cloud Resources |
| **Complexity** | High | Medium | Medium | High | Medium | High |
| **Setup Time** | 5 min | 2 min | 3 min | 5 min | 10 min | 15 min |
| **Languages** | All | N/A | Multiple | All | iOS/Android | N/A |
| **SBOM** | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Compliance** | ✅ | ✅ | ✅ | ✅ | ✅ (MASVS) | ✅ (CIS) |

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

---

## 📄 License

MIT License - see [LICENSE](../LICENSE) for details.

---

## 🔗 Related Projects

- **[osdo-actions](../osdo-actions/README.md)** - Granular GitHub Actions
- **[osdo-workflow-template](../osdo-workflow-template/README.md)** - Opinionated framework
- **[OSDO Documentation](../README.md)** - Complete documentation hub

---

**Made with ❤️ by the OpenSecDevOps Community**

*Last Updated: December 2025*
