import os
from dotenv import load_dotenv

# Check current directory
print(f"Current working directory: {os.getcwd()}")

# Load the .env file
load_dotenv()

# Get the API key
API_KEY = os.getenv('NASDAQ_API_KEY')
print(f'API_KEY: {API_KEY}')
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the API key
API_KEY = os.getenv('NASDAQ_API_KEY')
print(f'API_KEY: {API_KEY}')

