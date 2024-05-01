from fastapi import APIRouter

from app.api.v1 import file, llm

api_router_v1 = APIRouter()

api_router_v1.include_router(file.router, prefix="/file", tags=["file"])
api_router_v1.include_router(llm.router, prefix="/llm", tags=["llm"])

# api_router.include_router(role.router, prefix="/role", tags=["role"])
