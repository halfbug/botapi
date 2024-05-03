import os
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.retrievers.web_research import WebResearchRetriever
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from app.core.config import config

os.environ["GOOGLE_API_KEY"] = config.GOOGLE_API_KEY
os.environ["GOOGLE_CSE_ID"] = config.GOOGLE_CSE_ID


@tool
def search_web(query):
    """
    Performs search on Google Shopping.
    Args:
        - query (str): search queries with specifications such as exact-match phrases ("nikola tesla"), logical OR operators (tesla OR edison), exclusion criteria (tesla -motors), wildcard usage (tesla "rock * roll"), range matching (tesla announcement 2015..2017), price searches (tesla deposit $1000), unit conversions (250 kph in mph), searches within page titles (intitle:"tesla vs edison"), URL searches (tesla announcements inurl:2016), text searches within document bodies (intext:"orbi vs google wifi"), filetype specific searches ("tesla announcements" filetype:pdf), related site searches (related:nytimes.com), proximity searches (tesla AROUND(3) edison), and chained operator combinations ("nikola tesla" intitle:"top 5..10 facts" -site:youtube.com inurl:2015).

         Returns:
        - search results: string return.
    """
    vectorstore = Chroma(
        embedding_function=OpenAIEmbeddings(), persist_directory="./chroma_db_oai"
    )

    # LLM
    llm = ChatOpenAI(temperature=0)

    # Search
    search = GoogleSearchAPIWrapper()

    # Initialize
    web_research_retriever = WebResearchRetriever.from_llm(
        vectorstore=vectorstore, llm=llm, search=search
    )

    qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm, retriever=web_research_retriever
    )

    result = qa_chain({"question": query})
    return result
