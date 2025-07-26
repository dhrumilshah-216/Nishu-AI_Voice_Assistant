import os
from dotenv import load_dotenv

load_dotenv()

# Get both API keys
news_api_key = os.getenv("NEWS_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

print("OpenAI Key:", openai_api_key)
print("News API Key:", news_api_key)
