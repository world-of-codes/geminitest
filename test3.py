from config import supply_key
from google import genai

key= supply_key()

client = genai.Client(api_key=key)

prompts=[
    "Hello",
    "Explain python",
    "Explain OOPS in python.",
    '''
    Include classes , objects , inheritance and polymorhism.
    Also explain constructor in python.
    explain abstrcat class in python.
    explain garbage collection in python.    
    '''
    ]

for prompt in prompts:
    result=client.models.count_tokens(
        model='gemini-3.5-flash',
        contents=prompt
    )
    print('-'*50)
    print(prompt[:50])
    print("Tokens: ",result.total_tokens)

















'''
config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        ))
'''