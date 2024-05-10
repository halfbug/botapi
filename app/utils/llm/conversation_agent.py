from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.utils.llm.sysprompt.conversational_agent import CONVERSATIONAL_AGENT_PROMPT



class ConversationAgent:
    def __init__(self, openai_model, tools):
        self.openai_model = openai_model
        self.memory = ConversationBufferMemory(
            return_messages=True, memory_key="chat_history"
        )
        self.prompt = self.create_prompt()
        self.chain = self.openai_model.create_functional_chain(self.prompt)
        self.qa = AgentExecutor(
            agent=self.chain, tools=tools, verbose=True, memory=self.memory
        )

    def create_prompt(self):
        return ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    CONVERSATIONAL_AGENT_PROMPT,
                ),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )

    def convchain(self, query):
        if not query:
            return
        result = self.qa.invoke({"input": query})
        return result["output"]
