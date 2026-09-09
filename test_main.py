import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    html = response.text
    assert "Autonomous AI SDLC Studio &amp; Multi-Agent Test Harness" in html or "Autonomous AI SDLC Studio & Multi-Agent Test Harness" in html
    assert "featured-project" in html
    assert "hello@nathanscottlester.com" in html
    assert "4+" in html


def test_projects_page():
    response = client.get("/projects")
    assert response.status_code == 200
    html = response.text
    assert "featured-project" in html
    assert "/projects/ai-sdlc-studio" in html
    assert "/projects/ai-engineer-blueprint" in html
    assert "newsgenie" in html
    assert "azure-governance-dashboard" in html
    assert "intelligent-knowledge-hub" in html


def test_ai_sdlc_studio_case_study_route():
    response = client.get("/projects/ai-sdlc-studio")
    assert response.status_code == 200
    html = response.text
    assert "Autonomous AI SDLC Studio & Multi-Agent Test Harness" in html
    assert "9 Stages" in html
    assert "Architecture & The 9-Stage Agentic Loop" in html
    assert "RegPulse" in html
    assert "Deterministic Cost Governance" in html
    assert "Persistent Hybrid Vector Memory Bank" in html
    assert "hello@nathanscottlester.com" in html


def test_ai_engineer_blueprint_route():
    response = client.get("/projects/ai-engineer-blueprint")
    assert response.status_code == 200
    html = response.text
    assert "The AI Engineer Blueprint: Architecture &amp; Deployment Decision Engine" in html or "The AI Engineer Blueprint: Architecture & Deployment Decision Engine" in html
    assert "What AI Architecture Do I Need?" in html
    assert "Where Should I Run It?" in html
    assert "Traditional ML / Rules" in html
    assert "Direct Prompting" in html
    assert "RAG (Retrieval-Augmented)" in html
    assert "Single Agent (with Tools)" in html
    assert "Multi-Agent / Swarm" in html
    assert "Local Machine / Edge" in html
    assert "Self-Hosted VPS (Hostinger)" in html or "Self-Hosted VPS" in html
    assert "Cloud Hyperscaler (Azure/AWS/GCP)" in html or "Cloud Hyperscaler" in html
    assert "The AI Engineer: System Instructions" in html
    assert "ai_engineer_system_prompt.md" in html
    assert "Start with Single Agents" in html
    assert "Modular Decoupled Design" in html
    assert "Acknowledge the ACI" in html
    assert "hello@nathanscottlester.com" in html


def test_existing_projects():
    for slug in ["newsgenie", "azure-governance-dashboard", "intelligent-knowledge-hub"]:
        response = client.get(f"/projects/{slug}")
        assert response.status_code == 200


def test_about_page():
    response = client.get("/about")
    assert response.status_code == 200
    assert "hello@nathanscottlester.com" in response.text


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_not_found_project():
    response = client.get("/projects/unknown-slug")
    assert response.status_code == 200
    assert "Project not found" in response.text
