from fastapi import FastAPI
from app.api.routes import api_router_v1
# Create a FastAPI instance with a route prefix
app = FastAPI()


# Add Routers
app.include_router(api_router_v1, prefix="/api/v1")
# settings.API_V1_STR