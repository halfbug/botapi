from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.tools.render import format_tool_to_openai_function
from app.core.config import config


class OpenAIModel:
    def __init__(self, tools):
       
        self.functions = [format_tool_to_openai_function(f) for f in tools]
        self.chat_model = ChatOpenAI(openai_api_key=config.OPENAI_API_KEY,temperature=0).bind(functions=self.functions)

    def create_functional_chain(self, prompt):
        return (
            RunnablePassthrough.assign(
                agent_scratchpad=lambda x: format_to_openai_functions(
                    x["intermediate_steps"]
                )
            )
            | prompt
            | self.chat_model
            | OpenAIFunctionsAgentOutputParser()
        )
