

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

from browser_use import Agent

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
	raise ValueError('GEMINI_API_KEY is not set')

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(api_key))
agent = Agent(
	task='Go to amazon.com, search for laptop, sort by best rating, and give me the price of the first result',
	llm=llm,
)

async def main():
	await agent.run(max_steps=10)
	input('Press Enter to continue...')


asyncio.run(main())