from langchain.chains.llm_math.base import LLMMathChain
from langchain_openai import ChatOpenAI
gpt = ChatOpenAI(model="gpt-3.5-turbo-1106")
llm_chain = LLMMathChain.from_llm(llm=gpt)

def follow_chat(user_input: str):
    return llm_chain.invoke(input={
        "template": "Eres un asistente con capacidades matemáticas a través de Python. Transforma las preguntas del usuario en problemas matemáticos calculables con Python. Siempre calcula lo necesario, con las constantes siempre representadas con su valor numérico, sin utilizar variables con nombre.",
        "question": user_input}
    )["answer"]
