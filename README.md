# topic-question-generator

A Python Flask app that accepts a topic and generates 5 relevant questions using Google's Generative AI (Gemini).

## Features
- Accepts any topic from the user
- Produces 5 thoughtful questions
- Works with a built-in fallback if no API key is configured
- Ready for local run and cloud deployment

## Environment setup

### 1) Create a virtual environment

On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment variables
Create a `.env` file in the project root:
```bash
copy .env.example .env
```

Then add your Google API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
PORT=5000
FLASK_DEBUG=False
```

If you do not have a Google API key yet:
- Go to Google AI Studio
- Create a project
- Generate an API key
- Add it to `.env`

## Run the app
```bash
python app.py
```

Open:
```text
http://localhost:5000
```

## Deployment
This app can be deployed on platforms like Render, Railway, or Heroku.

Example startup command:
```bash
gunicorn app:app
```

## Example input
```text
Artificial Intelligence
```

## Example output
- What is the main idea behind Artificial Intelligence?
- How does Artificial Intelligence impact everyday life?
- What are the biggest challenges in AI today?
- In what real-world industries is AI useful?
- What would you like to explore next about AI?
