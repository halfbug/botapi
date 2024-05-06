from fastapi import FastAPI, HTTPException

from app.api.routes import api_router_v1
from app.core.config import config

# Create a FastAPI instance with a route prefix
app = FastAPI()
# print(config.API_V1_ROUTE)


@app.get("/")
async def health_check():
    """
    Endpoint to check the health status of the application.
    """
    # Perform any necessary health checks here
    # For example, check if the database is reachable, external services are accessible, etc.
    # You can customize the checks based on your application's requirements.

    # Example health check:
    database_status = check_database()

    if database_status:
        return {"status": "OK"}
    else:
        # If any of the checks fail, return a 503 Service Unavailable status
        raise HTTPException(status_code=503, detail="Database unavailable")


def check_database():
    """
    Example function to check the status of the database.
    Replace this function with your actual database health check logic.
    """
    # Replace this with actual database connectivity check
    # For demonstration purposes, returning a hardcoded value
    return True


# Add Routers
app.include_router(api_router_v1, prefix=config.API_V1_ROUTE)
# settings.API_V1_STR

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
