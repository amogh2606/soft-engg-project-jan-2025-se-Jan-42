import os, warnings
from getpass import getpass
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

# check if LLM API key is set
if 'GOOGLE_API_KEY' not in os.environ:
    print("Environment variable GOOGLE_API_KEY not set")
    os.environ['GOOGLE_API_KEY'] = getpass("Enter the Google API key: ")

# set LLM cache
set_llm_cache(InMemoryCache(maxsize=100))

# ignore user warnings
warnings.filterwarnings('ignore', category=UserWarning)
