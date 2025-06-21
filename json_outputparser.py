from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini" ,
                 openai_api_key=api_key)

parser=JsonOutputParser()

prompt= PromptTemplate(
    template="write a short introduction of the {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain=prompt|model|parser

result=chain.invoke({
    'topic':'Cricket'
})

print(result)