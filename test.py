from google.genai import types

from config import supply_key

from google import genai



key= supply_key()

client = genai.Client(api_key=key)

response=client.models.generate_content(
    model='gemini-3.5-flash',
    contents='explain LLM in 2 lines for a student',
    config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )))

print(response.text)