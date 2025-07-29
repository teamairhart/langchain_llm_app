from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os   
from dotenv import load_dotenv

load_dotenv()

def generate_pimp_name(first_name, last_name):
    # Use ChatOpenAI for chat models like gpt-3.5-turbo
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.9,
        max_tokens=100,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    prompt_template_name = PromptTemplate(
        input_variables=["first_name", "last_name"],
        template="Generate 3 unique pimp names using either or both {first_name} and {last_name}. Be extremely creative and show your gangsta side."
    )
    
    # Modern LangChain approach using the pipe operator
    chain = prompt_template_name | llm | StrOutputParser()
    
    response = chain.invoke({"first_name": first_name, "last_name": last_name})
    
    return response

if __name__ == "__main__":
    pimp_name = generate_pimp_name("Matt", "Pettoni")
    print(f"Your New Handle: \n{pimp_name}")