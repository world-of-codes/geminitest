from google.genai import types

from config import supply_key

from google import genai



key= supply_key()

client = genai.Client(api_key=key)

response=client.models.generate_content(
    model='gemini-3.5-flash',
    contents='Give me a creative name for a coffee shop.',
    config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
        temperature=1.0
    )
)

print(response.text)




