from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini" ,
                 openai_api_key=api_key)

prompt1=PromptTemplate(
    template="generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template="create a 5 points summary of the {text}",
    input_variables=['text']
)

parser=StrOutputParser()

chain = prompt1|model|parser|prompt2|model|parser

result=chain.invoke({
    'topic':'Black Hole'
})

print(result)

chain.get_graph().print_ascii()



