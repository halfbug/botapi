from fastapi import FastAPI
from app.api.routes import api_router_v1
from app.core.config import config
# Create a FastAPI instance with a route prefix
app = FastAPI()
# print(config.API_V1_ROUTE) 

# Add Routers
app.include_router(api_router_v1, prefix=config.API_V1_ROUTE)
# settings.API_V1_STR