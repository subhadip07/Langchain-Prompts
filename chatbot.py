from langchain_groq import ChatGroq
from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatGroq(model='llama-3.1-8b-instant')

while True:
    user_input=input('You: ')
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    print('AI: ', result.content)
