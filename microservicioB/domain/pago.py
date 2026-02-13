from pydantic import BaseModel
from datetime import date
from typing import List

class Pago(BaseModel):
    id: int
    metodoPagoPredeterminado: str
    historialFacturas: List[str]
    fechaProximoPago: date
