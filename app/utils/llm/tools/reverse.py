from langchain.tools import tool


@tool
def create_your_own(query: str) -> str:
    """This function can do whatever you would like once you fill it in"""
    print(type(query))
    return query[::-1]
