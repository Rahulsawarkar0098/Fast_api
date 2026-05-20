import base64
from openai import AsyncOpenAI
from config import OPENAI_API_KEY

client =AsyncOpenAI(api_key=OPENAI_API_KEY)


async def genearate_thumbnail(prompt:str,style_prompt:str,headshot_url:str)->bytes:
    """
    Use the responses API with GPT IMAGE 2
    pass the headshot url directly as an input image
    returns raw png bytes
    """
full_prompt=(
        f"{style_prompt}\n\n"
        "IMPORTANT : the generated thumbnail MUST promenently feature the person"
        "shown in the provided reference headshot photo keep there likeness accurate."
    )
 

response =client.responses.create(
    model="gpt-4o",
    input=[
        {
            "role":"user",
            "content":full_prompt
        }
    ]
)
    
