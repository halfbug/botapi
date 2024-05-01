from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd

router = APIRouter()

class PromptRequest(BaseModel):
    message: str
    wrID: str

class PromptResponse(BaseModel):
    message: str
    wrID: str
    content: str # pd.DataFrame

@router.post("/prompt", response_model=PromptResponse)
async def prompt(request_data: PromptRequest):
    try:
        # Here you can process the request data, generate a reply, and create a pandas DataFrame
        reply_message = f"You said: {request_data.message}"
        # Example of creating a pandas DataFrame (replace this with your actual data)
        data = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
        df = pd.DataFrame(data)
        return PromptResponse(message=reply_message, wrID=request_data.wrID, content="df")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
