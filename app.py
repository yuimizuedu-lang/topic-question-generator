import os
from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

MODEL = genai.GenerativeModel("gemini-1.5-flash")


def generate_questions(topic: str):
    if not topic or not topic.strip():
        raise ValueError("Please provide a topic.")

    if not API_KEY:
        return [
            f"What is the main idea behind {topic}?",
            f"How does {topic} impact everyday life or society?",
            f"What are the most important challenges related to {topic}?",
            f"How is {topic} used in real-world applications?",
            f"What would you like to learn next about {topic}?",
        ]

    prompt = (
        f"Generate exactly 5 thoughtful, engaging questions about the topic: '{topic}'. "
        "The questions should be clear, diverse, and suitable for learning or discussion. "
        "Return only the 5 questions, one per line, with no numbering, no bullets, and no extra text."
    )

    try:
        response = MODEL.generate_content(prompt)
        text = response.text.strip()
        questions = [line.strip() for line in text.splitlines() if line.strip()]
        if len(questions) >= 5:
            return questions[:5]
    except Exception:
        pass

    return [
        f"What is the main idea behind {topic}?",
        f"How does {topic} impact everyday life or society?",
        f"What are the biggest challenges or limitations of {topic}?",
        f"In what real-world situations is {topic} useful?",
        f"What would you like to explore next about {topic}?",
    ]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        if not topic:
            return render_template("index.html", error="Please enter a topic.")

        try:
            questions = generate_questions(topic)
            return render_template("index.html", topic=topic, questions=questions)
        except ValueError as exc:
            return render_template("index.html", error=str(exc))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_DEBUG", "False").lower() == "true")
