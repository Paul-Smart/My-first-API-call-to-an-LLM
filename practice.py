import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from IPython.display import Markdown, display 
from openai import OpenAI


#loading the dote_nv
load_dotenv(override= True)
api_key = os.getenv('OPENAI_API_KEY')

#check the key

if not api_key:
    print("No API was found")
elif not api_key.startswith("sk-"):
    print("An API key was found")
elif api_key.strip() != api_key:
    print("An API key was found but it might have space or tab characters")
else:
    print("API key found and looks good so far")

#Calling OPENAI with some message
message = "Hello, GPT! This is my first ever message to you! Hi!"

messages =  [{"role" : "user", "content" : message
}]

messages

openai = OpenAI()

response = openai.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
response.choices[0].message.content