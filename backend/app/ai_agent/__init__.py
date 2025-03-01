import os
from getpass import getpass

# check if LLM API key is set
if 'GOOGLE_API_KEY' not in os.environ:
    print("Environment variable GOOGLE_API_KEY not set")
    os.environ['GOOGLE_API_KEY'] = getpass("Enter the Google API key: ")

