from fastapi import FastAPI
from fpapi.router import router
from fpapi.openapi import OpenApiSchema

app = FastAPI()
app.include_router(router)
app.openapi = OpenApiSchema(app.routes).get_openapi
