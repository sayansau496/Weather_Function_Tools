import os
#from dotenv import load_dotenv
from google import genai

#load_dotenv()

#client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
client = genai.Client()

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents="Say hello to my students in one short sentence.",
)
print(response.text)
