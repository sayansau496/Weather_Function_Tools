import os
from google import genai
from google.genai import types
from dbtools import talk_db,insert_db
from weather import get_weather

# Initialize the client (ensure GEMINI_API_KEY is set in your environment)
client = genai.Client()


# Create a chat session to enable the automatic function-calling loop
chat = client.chats.create(
    model="gemini-3.5-flash",
    config=types.GenerateContentConfig(
        tools=[talk_db,insert_db,get_weather],
        temperature=0
    )
)

# Provide the prompt containing the data and the question
prompt = """
I have 2 tools by the name talk_db and inser_db 
which will fetch data from mysql and insert records in table respectively.
Execute both the tools first talk_db then run insert_db
"""


prompt_weather='''
I have added the tool get_weather which takes Bangalore as city name 
for which call the tool and extract the current live weather.
'''

prompt_parameter=f"""
    Get current weather information for a city.

    Args:

        city: Name of the city, given from {input('enter city')}.
    """



print("Sending request to Gemini...\n")
response = chat.send_message(prompt_parameter)

# The SDK will automatically detect the tool request, run the Python function locally, 
# and return the result to the model to generate this final text response.
print("Response:")
print(response.text)