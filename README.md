# 🔒 OSDO Workflows - Flujos de Trabajo de Seguridad Reutilizables

Colección integral de flujos de trabajo especializados y reutilizables de GitHub Actions para seguridad, cumplimiento normativo y garantía de calidad en diversas tecnologías.

---

## 📚 Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Flujos de Trabajo Disponibles](#flujos-de-trabajo-disponibles)
- [Inicio Rápido](#inicio-rápido)
- [Catálogo de Flujos de Trabajo](#catálogo-de-flujos-de-trabajo)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Patrones de Integración](#patrones-de-integración)
- [Guía de Configuración](#guía-de-configuración)
- [Mejores Prácticas](#mejores-prácticas)

---

## 🎯 Descripción General

OSDO Workflows proporciona una suite integral de **10 flujos de trabajo de seguridad especializados** diseñados para ser reutilizables mediante `workflow_call`. Cada flujo de trabajo se enfoca en un dominio de seguridad específico, lo que permite:

- ✅ **Seleccionar lo que necesitas** - Usa únicamente lo que requieras
- ✅ **Combinar flujos de trabajo** - Construye pipelines de seguridad completos
- ✅ **Personalizar** - Parámetros de entrada extensos para mayor flexibilidad
- ✅ **Escalar** - Desde proyectos individuales hasta despliegues a escala empresarial

---

## 📦 Flujos de Trabajo Disponibles

| Flujo de Trabajo | Propósito | Características Principales |
|----------|---------|--------------|
| **[osdo-framework.yml](#1-osdo-framework)** | Pipeline CI/CD completo | Pruebas, seguridad, cumplimiento, informes |
| **[osdo-container-security.yml](#2-seguridad-de-contenedores)** | Seguridad de contenedores | Trivy, Grype, SBOM, firma |
| **[osdo-iac-security.yml](#3-seguridad-de-infraestructura-como-código)** | Seguridad de IaC | Terraform, K8s, CloudFormation, detección de desvíos |
| **[osdo-supply-chain.yml](#4-seguridad-de-la-cadena-de-suministro)** | Seguridad de la cadena de suministro | SBOM, procedencia, SLSA, detección de malware |
| **[osdo-continuous-monitoring.yml](#5-monitoreo-continuo)** | Monitoreo de seguridad | Análisis de tendencias, alertas, auto-remediación |
| **[osdo-dast.yml](#6-dast)** | Pruebas dinámicas de aplicaciones | OWASP ZAP, SSL/TLS, cabeceras de seguridad |
| **[osdo-api-security.yml](#7-seguridad-de-api)** | Seguridad de API | OWASP API Top 10, validación de esquemas |
| **[osdo-mobile-security.yml](#8-seguridad-móvil)** | Seguridad de aplicaciones móviles | Cumplimiento MASVS, iOS/Android |
| **[osdo-cloud-security.yml](#9-seguridad-en-la-nube)** | Seguridad en la nube | AWS/Azure/GCP, IAM, cumplimiento |
| **[osdo-license-compliance.yml](#10-cumplimiento-de-licencias)** | Gestión de licencias | Aplicación de políticas, verificación de compatibilidad |

---

## 🚀 Inicio Rápido

### Uso Básico

```yaml
# .github/workflows/security.yml
name: Security Pipeline

on: [push, pull_request]

jobs:
  security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@v2
    secrets: inherit
```

### Enfoque Multi-Flujo

```yaml
# .github/workflows/comprehensive-security.yml
name: Comprehensive Security

on: [push, pull_request]

jobs:
  # Container Security
  containers:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@v2
    with:
      image-name: my-app
      image-tag: latest

  # Supply Chain
  supply-chain:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@v2
    with:
      package-manager: npm
      slsa-level: "2"

  # IaC Security
  infrastructure:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@v2
    with:
      iac-type: terraform
      compliance-frameworks: "cis,nist"
```

---

## 📖 Catálogo de Flujos de Trabajo

### 1. OSDO Framework

**Pipeline completo de seguridad y cumplimiento normativo con todo incluido.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@v2
with:
  node-version: '22'
  run-tests: true
  run-security-scan: true
  test-coverage-threshold: '80'
  critical-threshold: '0'
  high-threshold: '5'
```

**Características Principales:**
- Pipeline CI/CD completo
- Pruebas, controles de calidad y análisis de seguridad
- Generación de SBOM
- Informes de cumplimiento normativo

---

### 2. Seguridad de Contenedores

**Análisis exhaustivo de seguridad y refuerzo de imágenes de contenedores.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@v2
with:
  image-name: my-app
  image-tag: v1.0.0
  scanners: "trivy,grype"
  enable-sbom: true
  enable-signing: true
  critical-threshold: "0"
```

**Características Principales:**
- Soporte multi-escáner (Trivy, Grype, Snyk)
- Análisis estático de Dockerfile
- Generación de SBOM (SPDX/CycloneDX)
- Firma de imágenes con Cosign
- Detección de secretos en imágenes
- Verificaciones de cumplimiento CIS

**Salidas:**
- `vulnerabilities-found` - Total de vulnerabilidades
- `critical-count` - Vulnerabilidades críticas
- `image-signed` - Estado de la firma
- `security-score` - Puntuación general (0-100)

---

### 3. Seguridad de Infraestructura como Código

**Análisis de seguridad para Terraform, Kubernetes, CloudFormation y más.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@v2
with:
  iac-type: terraform
  iac-directory: "./terraform"
  scanners: "all"
  compliance-frameworks: "cis,nist,pci-dss"
  enable-drift-detection: true
```

**Características Principales:**
- Análisis con múltiples herramientas (Checkov, KICS, tfsec, Terrascan)
- Validación de manifiestos de Kubernetes
- Aplicación de Política como Código
- Detección de desvíos de infraestructura
- Soporte multi-nube
- Guía de remediación

**Salidas:**
- `violations-found` - Total de violaciones
- `compliance-score` - Porcentaje de cumplimiento
- `drift-detected` - Estado de desvío

---

### 4. Seguridad de la Cadena de Suministro

**Seguridad completa de la cadena de suministro de software y gestión de SBOM.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@v2
with:
  package-manager: npm
  enable-sbom-generation: true
  provenance-verification: true
  slsa-level: "2"
  malware-scan: true
  typosquatting-detection: true
```

**Características Principales:**
- Generación y validación de SBOM
- Verificación de procedencia
- Cumplimiento SLSA (Niveles 1-4)
- Detección de malware y typosquatting
- Verificaciones de cumplimiento de licencias
- Atestación de compilación
- Análisis de alcanzabilidad

**Salidas:**
- `sbom-valid` - Estado de validación del SBOM
- `slsa-level-achieved` - Nivel SLSA alcanzado
- `malicious-packages` - Recuento de paquetes maliciosos
- `security-score` - Puntuación de la cadena de suministro

---

### 5. Monitoreo Continuo

**Monitoreo de seguridad programado con análisis de tendencias y alertas.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-continuous-monitoring.yml@v2
with:
  monitoring-scope: all
  alert-channels: "github,slack"
  trending-period: "30d"
  auto-create-issues: true
```

**Características Principales:**
- Reescaneo programado de vulnerabilidades
- Análisis de tendencias y seguimiento de la postura de seguridad
- Alertas en múltiples canales
- Creación automática de incidencias
- Seguimiento de remediación
- Comparación con análisis anteriores

**Salidas:**
- `new-vulnerabilities` - Nuevas vulnerabilidades desde el último análisis
- `security-score` - Puntuación actual
- `trend-direction` - improving/degrading/stable

---

### 6. DAST

**Pruebas de seguridad de aplicaciones dinámicas para aplicaciones en ejecución.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-dast.yml@v2
with:
  target-url: https://app.example.com
  scan-type: full
  owasp-top-10: true
  check-ssl-tls: true
  api-spec: "./openapi.yaml"
```

**Características Principales:**
- Análisis con OWASP ZAP
- Detección de OWASP Top 10
- Pruebas de configuración SSL/TLS
- Validación de cabeceras de seguridad
- Verificaciones de Política de Seguridad de Contenido
- Pruebas específicas de API

**Salidas:**
- `vulnerabilities-found` - Total de vulnerabilidades
- `owasp-violations` - Problemas del OWASP Top 10
- `risk-score` - Puntuación de riesgo de la aplicación

---

### 7. Seguridad de API

**Pruebas de seguridad especializadas para APIs REST, GraphQL y gRPC.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-api-security.yml@v2
with:
  api-spec-path: "./openapi.yaml"
  api-type: REST
  base-url: https://api.example.com
  owasp-api-top-10: true
  rate-limiting-test: true
  api-fuzzing: true
```

**Características Principales:**
- Validación de especificaciones OpenAPI/Swagger
- OWASP API Security Top 10
- Pruebas de autenticación y autorización
- Verificación de limitación de velocidad
- Validación de esquemas
- Pruebas específicas de GraphQL
- Fuzzing de API

**Salidas:**
- `security-score` - Puntuación de seguridad de la API
- `owasp-violations` - Violaciones del API Top 10
- `auth-issues` - Problemas de autenticación

---

### 8. Seguridad Móvil

**Análisis de seguridad para aplicaciones Android, iOS, React Native y Flutter.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-mobile-security.yml@v2
with:
  platform: android
  binary-path: ./app-release.apk
  masvs-level: L2
  check-ssl-pinning: true
  check-obfuscation: true
```

**Características Principales:**
- Cumplimiento OWASP MASVS (L1/L2)
- Análisis estático y binario
- Verificación de SSL pinning
- Verificaciones de ofuscación de código
- Detección de root/jailbreak
- Análisis de permisos
- Detección de secretos embebidos

**Salidas:**
- `security-score` - Puntuación de seguridad móvil
- `masvs-compliance` - Estado de cumplimiento MASVS
- `critical-issues` - Problemas de seguridad críticos

---

### 9. Seguridad en la Nube

**Análisis de seguridad multi-nube para AWS, Azure y GCP.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@v2
with:
  cloud-provider: aws
  regions: "us-east-1,us-west-2"
  iam-analysis: true
  compliance-frameworks: "cis,nist"
  public-exposure-check: true
```

**Características Principales:**
- Soporte multi-nube (AWS/Azure/GCP)
- Análisis de políticas IAM
- Evaluación de seguridad de red
- Verificación de cifrado
- Detección de exposición pública
- Cumplimiento de CIS Benchmarks
- Análisis de coste-seguridad

**Salidas:**
- `misconfigurations-found` - Total de configuraciones incorrectas
- `compliance-score` - Porcentaje de cumplimiento
- `iam-issues` - Problemas de seguridad IAM
- `cost-impact` - Estimación del coste de remediación

---

### 10. Cumplimiento de Licencias

**Gestión de licencias de software y aplicación de cumplimiento normativo.**

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-license-compliance.yml@v2
with:
  package-manager: npm
  allowed-licenses: "MIT,Apache-2.0,BSD-3-Clause"
  denied-licenses: "GPL-3.0,AGPL-3.0"
  generate-notice-file: true
  compatibility-check: true
```

**Características Principales:**
- Soporte multi-lenguaje
- Aplicación de políticas de licencias
- Detección de licencias copyleft
- Verificación de compatibilidad
- Generación de archivos NOTICE
- SBOM con información de licencias
- Informes de cumplimiento automatizados

**Salidas:**
- `total-licenses` - Licencias únicas encontradas
- `denied-licenses-found` - Violaciones de política
- `compliance-status` - Estado general

---

## 🎨 Patrones de Integración

### Patrón 1: Seguridad Full Stack

```yaml
name: Full Stack Security

on: [push, pull_request]

jobs:
  # Code & Dependencies
  supply-chain:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-supply-chain.yml@v2
    with:
      package-manager: all
      slsa-level: "2"

  # Containers
  containers:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-container-security.yml@v2
    with:
      image-name: ${{ github.repository }}
      enable-signing: true

  # Infrastructure
  infrastructure:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-iac-security.yml@v2
    with:
      iac-type: all

  # Cloud Resources
  cloud:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@v2
    with:
      cloud-provider: aws
      compliance-frameworks: "cis,pci-dss"

  # Licenses
  licenses:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-license-compliance.yml@v2
    with:
      fail-on-denied: true
```

### Patrón 2: Monitoreo Programado

```yaml
name: Security Monitoring

on:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  monitor:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-continuous-monitoring.yml@v2
    with:
      monitoring-scope: all
      alert-channels: "github,slack"
      auto-create-issues: true
```

### Patrón 3: Validación Pre-Producción

```yaml
name: Pre-Production Security

on:
  pull_request:
    branches: [main]

jobs:
  api-security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-api-security.yml@v2
    with:
      base-url: https://staging.api.example.com
      owasp-api-top-10: true

  dast:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-dast.yml@v2
    with:
      target-url: https://staging.example.com
      scan-type: full
```

---

## ⚙️ Guía de Configuración

### Matriz de Selección de Flujos de Trabajo

| Necesidad | Flujo(s) de Trabajo Recomendado(s) |
|------|------------------------|
| **CI/CD General** | osdo-framework |
| **Docker/Kubernetes** | osdo-container-security |
| **Terraform/IaC** | osdo-iac-security |
| **Dependencias** | osdo-supply-chain |
| **Aplicación en Ejecución** | osdo-dast |
| **API REST/GraphQL** | osdo-api-security |
| **Aplicación Móvil** | osdo-mobile-security |
| **AWS/Azure/GCP** | osdo-cloud-security |
| **Licencias de Código Abierto** | osdo-license-compliance |
| **Monitoreo Continuo** | osdo-continuous-monitoring |

### Patrones de Configuración Comunes

#### Proyecto de Alta Seguridad
```yaml
with:
  critical-threshold: "0"
  high-threshold: "0"
  fail-on-high: true
  fail-on-critical: true
  slsa-level: "3"
```

#### Enfoque Equilibrado
```yaml
with:
  critical-threshold: "0"
  high-threshold: "10"
  fail-on-high: false
  slsa-level: "2"
```

#### Permisivo (Desarrollo)
```yaml
with:
  critical-threshold: "5"
  high-threshold: "20"
  fail-on-high: false
  slsa-level: "1"
```

---

## 🎯 Mejores Prácticas

### 1. Comienza Simple, Escala Gradualmente

Comienza con el flujo de trabajo **osdo-framework** y luego añade flujos especializados según sea necesario.

### 2. Utiliza Secretos Correctamente

Usa siempre los Secretos de GitHub para datos sensibles:

```yaml
jobs:
  cloud-security:
    uses: opensecdevops/osdo-workflows/.github/workflows/osdo-cloud-security.yml@v2
    secrets: inherit
```

### 3. Fija las Versiones

Usa versiones o etiquetas específicas en producción:

```yaml
uses: opensecdevops/osdo-workflows/.github/workflows/osdo-framework.yml@v2.2.0
```

### 4. Combina con Criterio

No ejecutes todos los flujos de trabajo en cada evento:

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * 1'  # Weekly monitoring
```

### 5. Monitorea Tendencias

Usa `osdo-continuous-monitoring` para el seguimiento a largo plazo de la postura de seguridad.

---

## 📊 Comparación de Flujos de Trabajo

| Característica | Framework | Contenedor | IaC | Cadena de Suministro | Móvil | Nube |
|---------|-----------|-----------|-----|--------------|--------|-------|
| **Alcance** | Completo | Contenedores | Infraestructura | Dependencias | Aplicaciones | Recursos en la Nube |
| **Complejidad** | Alta | Media | Media | Alta | Media | Alta |
| **Tiempo de Configuración** | 5 min | 2 min | 3 min | 5 min | 10 min | 15 min |
| **Lenguajes** | Todos | N/A | Múltiples | Todos | iOS/Android | N/A |
| **SBOM** | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ |
| **Cumplimiento** | ✅ | ✅ | ✅ | ✅ | ✅ (MASVS) | ✅ (CIS) |

---

## 🤝 Contribuciones

¡Damos la bienvenida a las contribuciones! Consulta [CONTRIBUTING.md](../CONTRIBUTING.md) para más detalles.

---

## 📄 Licencia

Licencia MIT - consulta [LICENSE](../LICENSE) para más detalles.

---

## 🔗 Proyectos Relacionados

- **[osdo-actions](../osdo-actions/README.md)** - GitHub Actions granulares
- **[osdo-workflow-template](../osdo-workflow-template/README.md)** - Marco de trabajo con convenciones predefinidas
- **[Documentación OSDO](../README.md)** - Centro de documentación completo

---

**Hecho con ❤️ por la Comunidad OpenSecDevOps**

*Última actualización: diciembre de 2025*
