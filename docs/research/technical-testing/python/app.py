import os
from flask import Flask, request, render_template_string
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

# Upload size limit: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# HTML Page
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Food Recognition</title>
</head>
<body>
    <h1>Food Recognition Test</h1>

    <form action="/analyze" method="POST" enctype="multipart/form-data">
        <p>Select Food Image:</p>
        <input type="file" name="image" accept="image/*" required>
        <button type="submit">Analyze Food</button>
    </form>

    {% if result %}
        <h2>Food Analysis Result:</h2>
        <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

# Home Page
@app.route("/")
def home():
    return render_template_string(HTML)


# Food Image Analysis
@app.route("/analyze", methods=["POST"])
def analyze():

    image = request.files.get("image")

    if not image or not image.filename:
        return "Please select a food image."

    mime_type = image.mimetype

    if mime_type not in ["image/jpeg", "image/png", "image/webp"]:
        return "Only JPG, PNG and WEBP images are supported."

    image_data = image.read()

    if len(image_data) > 5 * 1024 * 1024:
        return "Image must be smaller than 5 MB."

    try:

        prompt = """
        Identify the food in this image.

        Give the result in EXACTLY 8 short lines:

        Food: Main food name
        Other items: Visible food items
        Category: Food category
        Cooking: Cooking method
        Ingredients: Clearly visible ingredients
        Portion: Small, medium or large
        Confidence: High, medium or low
        Note: Any uncertainty or confusion

        Rules:
        - Keep every line short and simple.
        - Do not write introductions or explanations.
        - Do not use paragraphs or markdown.
        - Do not guess or invent food items.
        - Do not estimate calories or exact grams.
        - If no food is visible, write "No food detected".
        - If unsure, clearly mention the uncertainty.
        """

        image_part = types.Part.from_bytes(
            data=image_data,
            mime_type=mime_type
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=[prompt, image_part]
        )

        result = (response.text or "No response received.").strip()
        result = result.replace("**", "").replace("__", "")

        return render_template_string(
            HTML,
            result=result
        )

    except Exception as e:
        return f"Gemini API Error: {str(e)}", 502


if __name__ == "__main__":
    app.run(debug=True)
