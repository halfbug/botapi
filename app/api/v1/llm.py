import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class PromptRequest(BaseModel):
    message: str
    wrID: str


class PromptResponse(BaseModel):
    message: str
    wrID: str
    content: dict  # Change content type to dictionary


@router.post("/prompt", response_model=PromptResponse)
async def prompt(request_data: PromptRequest):
    try:
        reply_message = f"You said: {request_data.message}"
        # Example of creating a pandas DataFrame (replace this with your actual data)
        data = {"column1": [1, 2, 3], "column2": [4, 5, 6]}
        df = pd.DataFrame(data)
        # Convert DataFrame to dictionary
        df_dict = df.to_dict()
        return PromptResponse(
            message=reply_message, wrID=request_data.wrID, content=df_dict
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
