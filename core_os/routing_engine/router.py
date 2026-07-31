"""
KCN Core Routing Engine

Routes user objectives to the correct KCN department,
capabilities, tools, and agents.
"""

from __future__ import annotations

from typing import Any

from .registry_loader import RegistryLoader


# Order matters: more specific intent domains first (dict preserves insertion order)
DEPARTMENT_KEYWORDS: dict[str, list[str]] = {
    "learning_academy": [
        "learn", "course", "skill", "train", "certify", "practice", "assess",
        "tutor", "education",
    ],
    "financial_intelligence": [
        "money", "budget", "finance", "financial", "business plan", "scenario",
        "cost estimate", "investment",
    ],
    "web_development": [
        "website", "application", "software", "code", "app", "api",
        "frontend", "backend", "deploy", "marketplace",
    ],
    "reality_design": [
        "house", "building", "construction", "landscape",
        "home", "blueprint", "floor plan", "digital twin", "structure",
        "architectural design", "3d model", "sofa", "furniture",
        "interior", "simulate", "simulation", "cad", "bim",
        "object edit", "living room",
    ],
    "human_ai": [
        "personal", "goal", "memory", "growth", "decision support", "self",
        "organize my",
    ],
}


class KCNRouter:
    """Analyze a user request and produce a routing plan."""

    def __init__(self, registry: RegistryLoader | None = None) -> None:
        self.registry = registry or RegistryLoader()

    def analyze_request(self, request: str) -> dict[str, Any]:
        request_lower = request.lower()
        department = "human_ai"

        for dept, keywords in DEPARTMENT_KEYWORDS.items():
            if any(word in request_lower for word in keywords):
                department = dept
                break

        capabilities = [
            c for c in self.registry.list_capabilities()
            if c.get("department") == department
        ]
        agents = self.registry.list_agents(department=department)
        tools = self.registry.list_tools(department=department)

        return {
            "request": request,
            "department": department,
            "capabilities": [c.get("id") for c in capabilities],
            "capability_details": capabilities,
            "agents": [a.get("id") for a in agents],
            "agent_details": agents,
            "tools": [t.get("id") for t in tools],
            "status": "routed",
        }
