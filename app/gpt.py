import os
from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('OPENAI_TOKEN')

client = AsyncOpenAI(
    base_url="https://api.proxyapi.ru/openai/v1",
    api_key=token,
)


async def gpt_text(request, model):
    completion = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Ты - персональный помощник ТОП-менеджера"
            },
            {
                "role": "user",
                "content": request
            }
        ],
        model=model
    )
    return completion.choices[0].message.content
