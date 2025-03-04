## Backend Server Instructions

- Go to the `backend` folder
- Create a virtual environment with the command `python -m venv .venv`
- Activate the virtual environment
    - On Linux: `source .venv/bin/activate`
    - On Windows: `.venv\Scripts\activate`
- Install required dependencies with `pip install -r requirements.txt`
- Set the `GOOGLE_API_KEY` environment variable
    - API key can be generated [HERE](https://ai.google.dev/gemini-api/docs).
- Use `flask run` command to run the app
