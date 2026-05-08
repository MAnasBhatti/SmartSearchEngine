<<<<<<< HEAD
# SearchEngine

A simple Flask-based TF-IDF search engine web app that ranks documents by cosine similarity. This project includes a Python web app and Docker support for local development.

## Project Structure

- `app.py` — Flask application and TF-IDF search engine implementation
- `requirements.txt` — Python dependency list
- `Dockerfile` — Docker image build instructions
- `docker-compose.yml` — Docker Compose service definition
- `templates/index.html` — HTML template used by Flask

## Features

- Custom TF-IDF vector calculation for a small document corpus
- Cosine similarity search to rank relevant documents
- Web UI for submitting search queries and viewing results
- Docker and Docker Compose support for containerized deployment

## Local Setup

1. Open the project folder in VS Code.
2. Create a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Run the app:
   ```powershell
   python app.py
   ```
5. Open your browser and go to:
   ```text
   http://127.0.0.1:5000
   ```

## Docker Setup

1. Build and start the service:
   ```powershell
   docker compose up --build
   ```
2. Open your browser at:
   ```text
   http://127.0.0.1:5000
   ```
3. Stop the service:
   ```powershell
   docker compose down
   ```

## Notes

- Flask loads templates from the `templates/` directory. The app expects `templates/index.html`.
- If the app throws `jinja2.exceptions.TemplateNotFound: index.html`, move `index.html` into `templates/`.

## License

This project is provided as-is for learning and demonstration purposes.
=======
# SmartSearchEngine
An intelligent search engine using TF-IDF to deliver accurate and relevant search results.
>>>>>>> c6fd8f1cd053dddddebd56aa78e068db670a2c1c
