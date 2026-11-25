import os
from google import genai
client=genai.Client()

all=client.models.list()

for _ in all:
    #if 'generatedcontent' in _:
    print(_.name)