# SVL-02 – System Architecture

## 1. Overview

The application uses Python and Flask to handle food image uploads. The uploaded image is sent to the Gemini API for analysis, and the generated food details are displayed on the webpage.


## 2. Main Components

| Component | Description |
|---|---|
| Web Interface | Allows users to upload food images |
| Flask Application | Handles requests and application flow |
| Image Upload | Receives the selected image |
| Image Validation | Checks image format and file size |
| Google GenAI SDK | Sends image data to Gemini |
| Gemini API | Analyzes the uploaded food image |
| Generated Response | Contains food-related analysis |
| Result Display | Shows the generated result on the webpage |

## 3. Application Flow

1. User opens the application.
2. Selects and uploads a food image.
3. Flask receives the image.
4. Image format and size are checked.
5. The image is sent to Gemini through the Google GenAI SDK.
6. Gemini generates the food analysis.
7. The response is returned to the Flask application.
8. The result is displayed on the webpage.

## 4. API Communication

- **API Provider:** Google Gemini
- **SDK:** Google GenAI Python SDK
- **Model:** Gemini 3.5 Flash (as recorded in testing evidence)
- **Endpoint:** `/analyze`
- **Request Method:** POST
- **Input:** Food image and analysis prompt
- **Output:** Food recognition details

## 5. Image Validation

The application checks the uploaded image before sending it to the API.

- Supported formats: JPG, PNG, WEBP
- Maximum file size: 5 MB

Unsupported images or images exceeding the size limit are rejected.

## 6. Output

The API-generated response includes:

- Food Name
- Other Items
- Category
- Cooking Method
- Ingredients
- Portion Size
- Confidence
- Note

The result is displayed on the webpage after image analysis.
