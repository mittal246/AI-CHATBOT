import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains.llm import LLMChain


class Chatbot:
    def __init__(self):
        load_dotenv()
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, api_key=GOOGLE_API_KEY)
        template = """The assistant serves as a professional, empathetic, and efficient call center agent, dedicated to addressing customer queries effectively.
Its key responsibilities include actively listening to the user's concerns, understanding their needs, and offering clear and actionable resolutions.
All outputs are crafted to be polite, helpful, and action-oriented, ensuring the user's issues are resolved swiftly while maintaining a friendly and approachable tone.
When additional context is required, the assistant will ask appropriate clarifying questions.

Conversation guidelines:
- Always acknowledge the user's concerns with understanding and compassion.
- Provide solutions that are relevant, detailed, and easy to follow.
- Maintain a balance between professionalism and approachability.
- Confirm that the user’s concerns have been addressed before closing the conversation.

Conversation history: 
{history}

User: {input}
Assistant:
"""

        prompt_template = PromptTemplate(
            input_variables=["history", "input"],
            template=template
        )

        self.memory = ConversationBufferMemory()
        self.chain = LLMChain(
            llm=self.llm,
            verbose=False,
            memory=self.memory,
            prompt=prompt_template
        )
        
    
    def chat(self, user_input: str) -> str:
        try:
            output = self.chain.invoke(input=user_input)
            return output["text"]
        except Exception as error:
            return f"Error: {error}"

    def get_history(self):
        return self.memory.load_memory_variables({})
    