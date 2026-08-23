from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Industrial Equipment API",
    version="0.1.0",
)


EQUIPMENT = {
    "P01": {
        "equipment_id": "P01",
        "name": "Hydraulic Pump P01",
        "status": "WARNING",
        "pressure_bar": 142,
        "temperature_c": 63,
        "fault_code": "E17",
    },
    "P02": {
        "equipment_id": "P02",
        "name": "Hydraulic Pump P02",
        "status": "OK",
        "pressure_bar": 185,
        "temperature_c": 51,
        "fault_code": None,
    },
}


@app.get("/equipment/{equipment_id}/status")
def get_equipment_status(equipment_id: str):
    equipment_id = equipment_id.upper()

    equipment = EQUIPMENT.get(equipment_id)

    if equipment is None:
        raise HTTPException(
            status_code=404,
            detail=f"Equipment {equipment_id} not found",
        )

    return equipment