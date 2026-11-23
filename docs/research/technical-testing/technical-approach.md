# SVL-02 – Investigate the Technical Approach

## 1. Technology Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code
- **AI Model:** Gemini 3.5 Flash (as recorded in testing evidence)
- **Platform:** Google AI Studio
- **Backend:** Flask
- **API:** Google Gemini API
- **Python SDK:** Google GenAI SDK

## 2. Python Dependencies

| Package | Purpose |
|---|---|
| Flask | Web application and backend handling |
| google-genai | Gemini API integration |
| python-dotenv | API key configuration |

### requirements.txt

```text
Flask==3.1.3
google-genai==2.33.0
pillow==13.0.0
python-dotenv==1.2.4
```

## 3. Component List

| Component | Responsibility |
|---|---|
| User Interface | Uploads food images |
| Flask Backend | Handles application requests |
| Image Upload | Receives uploaded images |
| Image Validation | Checks image format and size |
| Google GenAI SDK | Connects Python with Gemini |
| Gemini API | Analyzes food images |
| Result Display | Displays analysis to the user |
| Environment Configuration | Loads API credentials |

## 4. Prerequisites

- Python 3.9 or later
- pip package installer
- Git
- Google Gemini API key
- Internet connection

## 5. Python Environment Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/VK-9/Indian-food-recognition-platform.git
cd Indian-food-recognition-platform
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure API Key

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### Step 6: Run Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## 6. API Integration

The application uses Google's Gemini API through the Google GenAI Python SDK.

- API key is loaded from the `.env` file.
- User uploads a food image through the Flask application.
- The application checks the image format and size.
- Image data and the analysis prompt are sent to Gemini.
- Gemini analyzes the food image and generates a response.
- The result is displayed on the webpage.

**Model ID in app.py:** `gemini-3.5-flash`

## 7. Image Upload Configuration

- **Supported Formats:** JPG, PNG, WEBP
- **Maximum Upload Size:** 5 MB
- **HTTP Method:** POST
- **API Endpoint:** `/analyze`

## 8. Practical Testing

The application was tested using six different food images, including Indian food images and one blurry food image.

| Test Case | Food | Observation |
|---|---|---|
| 1 | Masala Dosa | Identified the food and accompanying items |
| 2 | South Indian Thali | Identified multiple food items in the plate |
| 3 | Poori | Identified fried bread |
| 4 | Poha | Identified food and visible ingredients |
| 5 | Samosa | Identified the snack but could not confirm its internal filling |
| 6 | Blurry Food Image | Identified it as a dinner feast spread but could not confirm the exact food items |

The generated response includes:

- Food Name
- Other Items
- Category
- Cooking Method
- Ingredients
- Portion Size
- Confidence
- Note

### Confidence Results

- The first five recorded food tests returned High confidence.
- The sixth test (blurry food image) returned 20% (Low confidence).
- The model mentioned that the image was extremely out of focus, making precise identification difficult.

These results show that image quality can affect food recognition and confidence levels.

Detailed test images and results are documented separately in `technical-testing.md`.


### Observed Limitations

- Exact regional names of small side dishes may not be identified.
- Ingredients inside food cannot always be confirmed.
- Similar-looking food items may be confused.
- AI-generated confidence does not guarantee correct identification.
- API response format is not independently validated.
- API retry and request throttling are not implemented.

## 9. Gemini API Quotas and Cost

Gemini API usage depends on the selected model, account tier, and project limits.

- **RPM:** Requests Per Minute
- **TPM:** Tokens Per Minute
- **RPD:** Requests Per Day

The free tier has usage restrictions. Paid usage depends on model-specific input and output token pricing.

Exact quotas and costs should be checked using the current model and Google AI Studio account.

### Official References

- Pricing: https://ai.google.dev/gemini-api/docs/pricing
- Rate Limits: https://ai.google.dev/gemini-api/docs/rate-limits
- AI Studio: https://aistudio.google.com/ 

## 10. Security and Reproducibility

- Store API credentials in `.env`.
- Never upload `.env` or `.venv` to GitHub.
- Do not hardcode API keys in source code.
- Install dependencies using `requirements.txt`.


## 11. Technical Feasibility

The practical testing demonstrates that Python, Flask, and the Gemini API can be integrated for food image recognition.

The application was tested on six different Indian food images and generated food descriptions including food names, visible ingredients, cooking methods, and portion details.

## 14. References

- Google AI Studio: https://aistudio.google.com/
- Gemini API Documentation: https://ai.google.dev/gemini-api/docs
- Google GenAI Python SDK: https://github.com/googleapis/python-genai
