from app.tools import (
    get_equipment_status,
    search_maintenance_manual,
)


def investigate_equipment(
    equipment_id: str,
    fault_code: str | None = None,
) -> dict:
    """
    Perform a basic equipment investigation.

    This is intentionally rule-based.
    I will replace the decision-making layer
    with an LLM in the next phase.
    """

    equipment = get_equipment_status(equipment_id)

    query = fault_code or equipment.get("fault_code") or ""

    manual_information = search_maintenance_manual(query)

    return {
        "equipment": equipment,
        "maintenance_information": manual_information,
    }