from google.genai import types

from config import supply_key

from google import genai



key= supply_key()

client = genai.Client(api_key=key)

prompt='''
Explain OOPS in python.
Include classes , objects , inheritance and polymorhism.
'''


response=client.models.count_tokens(
    model='gemini-3.5-flash',
    contents=prompt
)

print(f" Input tokens: {response.total_tokens}")



'''
config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        ))
'''