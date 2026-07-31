"""
KCN Universal Tracking Engine

Tracks versions, actions, agents, tests, and evidence.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


class KCNTracker:
    """In-memory tracker for foundation scaffolding. Replace with DB later."""

    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def record(
        self,
        event_type: str,
        component: str,
        details: Any = None,
        actor: str | None = None,
    ) -> dict[str, Any]:
        event = {
            "id": str(uuid4()),
            "type": event_type,
            "component": component,
            "details": details,
            "actor": actor,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        self.events.append(event)
        return event

    def history(
        self,
        component: str | None = None,
        event_type: str | None = None,
    ) -> list[dict[str, Any]]:
        results = self.events
        if component:
            results = [e for e in results if e.get("component") == component]
        if event_type:
            results = [e for e in results if e.get("type") == event_type]
        return results

    def clear(self) -> None:
        self.events.clear()
