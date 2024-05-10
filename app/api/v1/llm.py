import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.utils.llm.conversation_agent import ConversationAgent
from app.utils.llm.openai_model import OpenAIModel
from app.utils.llm.tools.reverse import create_your_own
from app.utils.llm.tools.web_search import search_web

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

        tools = [create_your_own]  # Define your tools
        workroom_modal = OpenAIModel(tools=tools)  # Initialize the OpenAI model
        conversation_agent = ConversationAgent(openai_model=workroom_modal, tools=tools)

        reply_message = conversation_agent.convchain(request_data.message)
        print(reply_message)

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
