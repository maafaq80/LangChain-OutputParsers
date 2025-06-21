from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
# from langchain_core.pydantic_v1 import BaseModel
from pydantic import BaseModel,Field

load_dotenv()
api_key=os.getenv("OPEN_AI_API_KEY")

model=ChatOpenAI(model="gpt-4o-mini" ,
                 openai_api_key=api_key)

class Person(BaseModel):
    name:str = Field(description="Name of the person")
    age:int = Field(gt=18, description="Age of a person must be greater than or equal to 18")
    city:str= Field(description="THe city of the person ")
    

    

parser=PydanticOutputParser(pydantic_object=Person)

prompt=PromptTemplate(
    template="add the details of a fictional person from the {area} \n {format_instructions}",
    input_variables=['area'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain=prompt|model|parser

result=chain.invoke({
    'area':'Pakistan'
})

print(result)