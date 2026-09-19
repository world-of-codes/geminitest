from google.genai import types

from config import supply_key

from google import genai



key= supply_key()

client = genai.Client(api_key=key)

response=client.models.generate_content(
    model='gemini-3.5-flash',
    contents='Explain dbms normalization to a student',
    config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )))

print(response.text)
print("metadata :- ",response.usage_metadata)
usage=response.usage_metadata
print("prompt tokens" ,usage.prompt_token_count)
print("prompt tokens details " ,usage.prompt_tokens_details)

print("prompt tokens details " ,usage.candidates_token_count)

print("prompt tokens details " ,usage.candidates_tokens_details)




