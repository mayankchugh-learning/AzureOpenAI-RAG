#importing important utilities and libraries
import json
import requests
import openai
from openai import AzureOpenAI
import os
from dotenv import load_dotenv


#setting openai configuration details
load_dotenv()
deployment_name = (os.getenv("OPENAI_EMBED_MODEL") or "").strip()
endpoint = (os.getenv("OPENAI_API_EMBED_BASE") or "").strip().rstrip("/")
subscription_key = (os.getenv("OPENAI_API_EMBED_KEY") or "").strip()
api_version = (os.getenv("OPENAI_API_EMBED_VERSION") or "").strip()

if not endpoint or not subscription_key:
    raise SystemExit(
        "Missing OPENAI_API_EMBED_BASE or OPENAI_API_EMBED_KEY. "
        "Use the Endpoint and Key from Azure Portal for the resource that hosts your embedding deployment."
    )

#creating an Azure OpenAI client
client = AzureOpenAI(
  api_key = subscription_key,  
  api_version = api_version,
  azure_endpoint =endpoint 
)

data="What is the capital of France?"

response = client.embeddings.create(
    input = data,
    model= deployment_name
)

print(response.model_dump_json(indent=2))



