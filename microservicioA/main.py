from fastapi import FastAPI
from infraestructura.api.perfil_api import router

app = FastAPI()
app.include_router(router)
