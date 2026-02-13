from fastapi import APIRouter
from domain.perfil import Perfil
from application.services.perfil_service import PerfilService

router = APIRouter()
service = PerfilService()

@router.post("/perfiles")
def crear(perfil: Perfil):
    return service.crear(perfil)

@router.get("/perfiles")
def listar():
    return service.listar()

@router.get("/perfiles/{id}")
def obtener(id: int):
    return service.obtener(id)

@router.put("/perfiles/{id}")
def actualizar(id: int, perfil: Perfil):
    return service.actualizar(id, perfil)

@router.delete("/perfiles/{id}")
def eliminar(id: int):
    return service.eliminar(id)
