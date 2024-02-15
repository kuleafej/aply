import os
from backend.schemas import TextCompletion
from openai import OpenAI
from dotenv import load_dotenv
# Load .env file
load_dotenv()

OPEN_API_KEY = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=OPEN_API_KEY)



# print(completion.choices[0].message)

def get_completion(input: TextCompletion):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": input.system},
            {"role": "user", "content": input.user_message}
        ]
        )
    
    return completion