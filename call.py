#importing importing libraries
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

#creating an azure openAi client
load_dotenv()

from openai import AzureOpenAI

endpoint = os.getenv("OPENAI_API_BASE")
model_name = "gpt-4o"
deployment = "gpt-4o"

subscription_key =os.getenv("OPENAI_API_KEY")
api_version = os.getenv("OPENAI_API_VERSION")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {"role": "user", "content": "list out all the players in the indian national cricket team?"}
        
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)