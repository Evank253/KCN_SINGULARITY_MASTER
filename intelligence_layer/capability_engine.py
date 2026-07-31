"""
Capability Matching Engine

Finds required capabilities, agents, and tools for a goal.
"""

from __future__ import annotations

from typing import Any


class CapabilityEngine:
    """Match a goal string against capability registry entries."""

    def match(
        self,
        goal: str,
        capabilities: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        goal_lower = goal.lower()
        results: list[dict[str, Any]] = []

        for cap in capabilities:
            name = (cap.get("name") or "").lower()
            description = (cap.get("description") or "").lower()
            department = (cap.get("department") or "").lower()

            if (
                name in goal_lower
                or any(token in goal_lower for token in name.split())
                or department.replace("_", " ") in goal_lower
            ):
                results.append(cap)
            elif any(word in description for word in goal_lower.split() if len(word) > 4):
                if cap not in results:
                    results.append(cap)

        return results

    def match_by_department(
        self,
        department: str,
        capabilities: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        return [c for c in capabilities if c.get("department") == department]
