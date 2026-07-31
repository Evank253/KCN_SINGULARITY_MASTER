"""
KCN Master Registry Loader

Loads ecosystem knowledge:
- capabilities
- agents
- tools
- skills
- versions
- tests
- benchmarks
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class RegistryLoader:
    """Load and expose KCN master registries from JSON files."""

    def __init__(self, base: str | Path | None = None) -> None:
        if base is None:
            candidates = [
                Path("registries"),
                Path(__file__).resolve().parents[2] / "registries",
                Path(__file__).resolve().parents[1] / "registries",
            ]
            self.base = next((p for p in candidates if p.exists()), Path("registries"))
        else:
            self.base = Path(base)

        self.capabilities = self._load("capabilities.json")
        self.agents = self._load("agents.json")
        self.tools = self._load("tools.json")
        self.skills = self._load("skills.json")
        self.versions = self._load("versions.json")
        self.tests = self._load("tests.json")
        self.benchmarks = self._load("benchmarks.json")

    def _load(self, filename: str) -> dict[str, Any]:
        path = self.base / filename
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def list_capabilities(self) -> list[dict[str, Any]]:
        return self.capabilities.get("capabilities", [])

    def list_agents(self, department: str | None = None) -> list[dict[str, Any]]:
        agents = self.agents.get("agents", [])
        if department:
            return [a for a in agents if a.get("department") == department]
        return agents

    def list_tools(self, department: str | None = None) -> list[dict[str, Any]]:
        tools = self.tools.get("tools", [])
        if department:
            return [t for t in tools if department in t.get("departments", [])]
        return tools

    def get_capability(self, capability_id: str) -> dict[str, Any] | None:
        for cap in self.list_capabilities():
            if cap.get("id") == capability_id:
                return cap
        return None

    def get_agent(self, agent_id: str) -> dict[str, Any] | None:
        for agent in self.list_agents():
            if agent.get("id") == agent_id:
                return agent
        return None
