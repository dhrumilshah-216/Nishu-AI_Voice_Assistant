import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Function to fetch news using the NewsData.io API
def get_news():
    # Example: Use NEWS_API_KEY here to make a request
    pass

# Function to send a prompt to the OpenRouter AI model
def ask_ai(prompt):
    # Example: Use OPENROUTER_API_KEY here to generate a response
    pass
