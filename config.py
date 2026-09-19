from dotenv import load_dotenv,find_dotenv
import os

def supply_key():
    load_dotenv(find_dotenv(), override=True)
    return os.getenv("GEMINI_API_KEY")



