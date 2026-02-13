from fastapi import FastAPI
from infraestructura.api.pago_api import router

app = FastAPI()

app.include_router(router)

