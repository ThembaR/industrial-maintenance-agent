from pathlib import Path

import httpx


EQUIPMENT_API = "http://127.0.0.1:8000"


def get_equipment_status(equipment_id: str) -> dict:
    """
    Retrieve current equipment status from the equipment API.
    """

    url = f"{EQUIPMENT_API}/equipment/{equipment_id}/status"

    response = httpx.get(url, timeout=3.0)

    response.raise_for_status()

    return response.json()


def search_maintenance_manual(query: str) -> str:
    """
    Simple keyword-based retrieval for the first version.
    I will replace this with semantic retrieval later.
    """

    manual_path = (
        Path(__file__).parent.parent
        / "knowledge"
        / "maintenance_manual.md"
    )

    manual = manual_path.read_text()

    query_words = query.lower().split()

    matching_lines = []

    for line in manual.splitlines():
        if any(word in line.lower() for word in query_words):
            matching_lines.append(line)

    if not matching_lines:
        return "No relevant maintenance information was found."

    return "\n".join(matching_lines)