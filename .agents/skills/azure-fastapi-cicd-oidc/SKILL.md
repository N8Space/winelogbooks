---
name: azure-fastapi-cicd-oidc
description: Interactive agent skill to scaffold and automate zero-secret CI/CD pipelines for Python FastAPI apps deployed to Azure App Service using GitHub Actions and OIDC Workload Identity Federation.
version: 2.0.0
---

# Azure App Service FastAPI CI/CD with GitHub Actions (OIDC)

Use this skill to guide the user through setting up a zero-secret, enterprise-grade deployment pipeline between GitHub Actions and Azure App Service (Linux) for Python FastAPI workloads.

---

## 1. Agent Interaction Protocol (Execution Instructions)

When this skill is invoked, the AI Agent **must** follow this conversational execution loop:

### Step 1: Collect Configuration Parameters
Before outputting setup code or scripts, prompt the user for the following required parameters (or infer them from the current workspace/context if already explicitly established):

1. **Azure Web App Name** (`APP_NAME`): The target Azure App Service name.
2. **Azure Resource Group** (`RESOURCE_GROUP`): Resource group containing the App Service.
3. **GitHub Handle / Organization** (`GITHUB_USER`): Owner of the GitHub repository.
4. **GitHub Repository Name** (`GITHUB_REPO`): Target repository name.
5. **Target Deployment Branch** (`GITHUB_BRANCH`): Default: `main`.
6. **Python Runtime Version** (`PYTHON_VER`): Default: `3.13`.

### Step 2: Render Tailored Provisioning Artifacts
Once values are confirmed, dynamically inject the variables into:
- The **Azure CLI Provisioning Script** (executed in Azure Cloud Shell or local CLI).
- The **`.github/workflows/deploy.yml`** workflow file.
- The **GitHub Secrets checklist**.

---

## 2. Interactive Azure Infrastructure Provisioning Script

This template accepts user-provided arguments, environment variables, or falls back to interactive terminal prompts if run directly in Bash.

```bash
#!/usr/bin/env bash
set -euo pipefail

# --- Configuration Prompts (Interactive Fallback) ---
read -rp "Enter Azure Web App Name (e.g., my-fastapi-app): " APP_NAME
read -rp "Enter Azure Resource Group: " RESOURCE_GROUP
read -rp "Enter GitHub Username/Org (e.g., octocat): " GITHUB_USER
read -rp "Enter GitHub Repository Name (e.g., my-repo): " GITHUB_REPO
read -rp "Enter Deployment Branch [default: main]: " GITHUB_BRANCH
GITHUB_BRANCH=${GITHUB_BRANCH:-main}

IDENTITY_NAME="id-github-${GITHUB_REPO}"

echo ""
echo "==> Gathering active Azure Subscription and Tenant information..."
SUBSCRIPTION_ID=$(az account show --query id -o tsv)
TENANT_ID=$(az account show --query tenantId -o tsv)

echo "==> Creating User-Assigned Managed Identity: ${IDENTITY_NAME}..."
az identity create \
  --name "${IDENTITY_NAME}" \
  --resource-group "${RESOURCE_GROUP}" \
  --output none

IDENTITY_CLIENT_ID=$(az identity show --name "${IDENTITY_NAME}" --resource-group "${RESOURCE_GROUP}" --query clientId -o tsv)
IDENTITY_PRINCIPAL_ID=$(az identity show --name "${IDENTITY_NAME}" --resource-group "${RESOURCE_GROUP}" --query principalId -o tsv)

echo "==> Assigning 'Website Contributor' RBAC Role to Identity..."
az role assignment create \
  --assignee-object-id "${IDENTITY_PRINCIPAL_ID}" \
  --assignee-principal-type "ServicePrincipal" \
  --role "Website Contributor" \
  --scope "/subscriptions/${SUBSCRIPTION_ID}/resourceGroups/${RESOURCE_GROUP}" \
  --output none

echo "==> Configuring Federated Identity Credentials for OIDC..."
# 1. Branch-scoped credential
az identity federated-credential create \
  --name "github-${GITHUB_BRANCH}-branch" \
  --identity-name "${IDENTITY_NAME}" \
  --resource-group "${RESOURCE_GROUP}" \
  --issuer "[https://token.actions.githubusercontent.com](https://token.actions.githubusercontent.com)" \
  --subject "repo:${GITHUB_USER}/${GITHUB_REPO}:ref:refs/heads/${GITHUB_BRANCH}" \
  --audiences "api://AzureADTokenExchange" \
  --output none

# 2. Environment-scoped credential (production)
az identity federated-credential create \
  --name "github-environment-production" \
  --identity-name "${IDENTITY_NAME}" \
  --resource-group "${RESOURCE_GROUP}" \
  --issuer "[https://token.actions.githubusercontent.com](https://token.actions.githubusercontent.com)" \
  --subject "repo:${GITHUB_USER}/${GITHUB_REPO}:environment:production" \
  --audiences "api://AzureADTokenExchange" \
  --output none

echo "==> Setting Gunicorn/Uvicorn ASGI Startup Command..."
az webapp config set \
  --resource-group "${RESOURCE_GROUP}" \
  --name "${APP_NAME}" \
  --startup-file "gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 main:app" \
  --output none

echo "==> Disabling Legacy SCM Basic Auth (Hardening)..."
az resource update \
  --resource-group "${RESOURCE_GROUP}" \
  --name ftp \
  --namespace Microsoft.Web \
  --resource-type basicPublishingCredentialsPolicies \
  --parent "sites/${APP_NAME}" \
  --set properties.allow=false \
  --output none 2>/dev/null || true

az resource update \
  --resource-group "${RESOURCE_GROUP}" \
  --name scm \
  --namespace Microsoft.Web \
  --resource-type basicPublishingCredentialsPolicies \
  --parent "sites/${APP_NAME}" \
  --set properties.allow=false \
  --output none 2>/dev/null || true

echo ""
echo "=========================================================================="
echo " ACTION REQUIRED: Add these secrets to GitHub (Settings > Secrets > Actions)"
echo "=========================================================================="
echo "AZURE_CLIENT_ID:       ${IDENTITY_CLIENT_ID}"
echo "AZURE_TENANT_ID:       ${TENANT_ID}"
echo "AZURE_SUBSCRIPTION_ID: ${SUBSCRIPTION_ID}"
echo "=========================================================================="

```

---

## 3. Dynamic GitHub Actions Workflow Template

Place at `.github/workflows/deploy.yml` with injected variables:

```yaml
name: Build and Deploy FastAPI to Azure Web App

on:
  push:
    branches:
      - {{GITHUB_BRANCH}}
  workflow_dispatch:

permissions:
  id-token: write
  contents: read

jobs:
  build:
    name: Build & Package Artifact
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python {{PYTHON_VER}}
        uses: actions/setup-python@v5
        with:
          python-version: '{{PYTHON_VER}}'

      - name: Install dependencies
        run: |
          python -m venv .venv
          source .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Create clean deployment package
        run: |
          zip -r release.zip . -x ".venv/*" "__pycache__/*" ".git/*" ".github/*"

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: python-fastapi-package
          path: release.zip
          retention-days: 1

  deploy:
    name: Deploy to Azure App Service
    runs-on: ubuntu-latest
    needs: build
    environment:
      name: 'production'
      url: ${{ steps.deploy-to-webapp.outputs.webapp-url }}

    steps:
      - name: Download artifact from build job
        uses: actions/download-artifact@v4
        with:
          name: python-fastapi-package

      - name: Authenticate to Azure using OIDC
        uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

      - name: Deploy artifact to Web App
        id: deploy-to-webapp
        uses: azure/webapps-deploy@v3
        with:
          app-name: '{{APP_NAME}}'
          package: release.zip

```

---

## 4. Local Project Scaffolding Standards

Ensure local repository root contains the following baseline files:

### `requirements.txt`

```text
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
gunicorn>=22.0.0
pydantic>=2.8.0

```

### `.gitignore`

```text
.venv/
__pycache__/
*.pyc
.env
.DS_Store
release.zip
.vscode/

```

---

## 5. Troubleshooting Matrix

| Issue | Root Cause | Resolution |
| --- | --- | --- |
| `AADSTS700213: No matching federated identity` | Subject claim mismatch (often due to GitHub numeric IDs in token claims). | Copy the exact subject claim from GitHub Actions error log and recreate the federated credential with that literal string. |
| `Error: No subscriptions found` | Managed Identity lacks RBAC access on the target scope. | Run `az role assignment create` to grant `Website Contributor` on the resource group. |
| Deprecation warnings on Node 20 | GitHub runners transitioning default runner nodes. | Non-fatal; can set `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION: 'true'` in workflow env if needed. |
| Browser shows old/parked landing page | Local DNS or browser cache hit. | Flush DNS (`ipconfig /flushdns`) and test in Incognito or via `curl -I https://<custom-domain>`. |

```

```