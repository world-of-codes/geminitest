from google.genai import types

from config import supply_key

from google import genai

from test2 import prompt

key= supply_key()

client = genai.Client(api_key=key)

prompt='Give me a name for a programming course'

for temp in [0.0,1.0]:
    print("\nTemperature:",temp)
    response=client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        temperature=temp
    )
)

print(response.text)




