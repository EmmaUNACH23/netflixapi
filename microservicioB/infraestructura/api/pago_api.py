from fastapi import APIRouter
from domain.pago import Pago
from application.services.pago_service import PagoService

router = APIRouter()
service = PagoService()

@router.post("/pagos")
def crear(pago: Pago):
    return service.crear(pago)

@router.get("/pagos")
def listar():
    return service.listar()

@router.get("/pagos/{id}")
def obtener(id: int):
    return service.obtener(id)

@router.put("/pagos/{id}")
def actualizar(id: int, pago: Pago):
    return service.actualizar(id, pago)

@router.delete("/pagos/{id}")
def eliminar(id: int):
    return service.eliminar(id)
