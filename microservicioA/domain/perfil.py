from pydantic import BaseModel

class Perfil(BaseModel):
    id: int
    nombre: str
    idioma: str
    calidad: str
