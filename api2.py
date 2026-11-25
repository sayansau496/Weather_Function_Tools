import os
from google import genai
from google.genai import types

# Initialize the client (ensure GEMINI_API_KEY is set in your environment)
client = genai.Client()

def check(name:str):
    """find the length of the given string.
            
            Args:
                name: the given name.
                
                
            Returns:
                the length of the given name in the function argument by the variable name
            """
    print('called..................',name.upper())
    return len(name.swapcase().strip())
        

def sum_no(a:int,b:int):
    """find the sum of 2 numbers.
        
        Args:
            a: The first number.
            b: The second number.
            
        Returns:
            the sum is {a+b} in ANUDIP
        """
    return f"the sum of {a} and {b} in ANUDIP is {a+b}"

def check_name_in_list(name: str, name_list: list[str]) -> bool:
    """Checks if a specific name is present in a given list of names.
    
    Args:
        name: The name to search for.
        name_list: A list of names to search through.
        
    Returns:
        True if the name is in the list, False otherwise.
    """
    return name in name_list

# Create a chat session to enable the automatic function-calling loop
chat = client.chats.create(
    model="gemini-flash-lite-latest",
    config=types.GenerateContentConfig(
        tools=[check],
        temperature=0
    )
)

# Provide the prompt containing the data and the question
prompt1 = """
I have a list of approved guests: Alice, Bob, Charlie, Diana, Soumya. 
Can you check if 'Soumya' is on the list?
"""
prompt2 = """
find sum of 111 and 345.
Use the tool sum_no
"""

prompt3='''
find the length of                            aMiTaVa                             
call the tool check
'''

print("Sending request to Gemini...\n")
response = chat.send_message(prompt3)

# The SDK will automatically detect the tool request, run the Python function locally, 
# and return the result to the model to generate this final text response.
print("Response:")
print(response.text)