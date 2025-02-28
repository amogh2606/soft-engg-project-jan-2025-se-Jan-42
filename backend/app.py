from app import create_app
from backend.app import db

app = create_app()

 # Ensure tables are created

if __name__ == "__main__":
    app.run(debug=True)
