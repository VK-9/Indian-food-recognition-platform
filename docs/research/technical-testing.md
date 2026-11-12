
# Gemini API Key – Indian Food Recognition Testing


## 1. Technology Used

- **Programming Language:** Python
- **Development Environment:** Visual Studio Code
- **AI Model:** Gemini 3.5 Flash
- **AI Platform:** Google AI Studio
- **Backend:** Python with Flask
- **API Integration:** Google Gemini API

## 2. Working Approach

1. The user uploads a food image.
2. The Python Flask backend receives the image.
3. The image is sent to the Gemini API.
4. Gemini analyzes the food image.
5. The API returns the food name, other visible items, category, cooking method, ingredients, portion size and confidence level.

## 3. Practical Testing

We tested the API using five Indian food images.

### Test 1: Masala Dosa

![Masala Dosa API Result](../../evidence/masala-dosa-result.jpg)

- **Food:** Masala Dosa
- **Other Items:** Sambar, coconut chutney, red chutney
- **Category:** South Indian Food
- **Cooking:** Pan-fried
- **Ingredients:** Rice batter, potato filling, curry leaves
- **Portion:** Large
- **Confidence:** High
- **Observation:** The model correctly identified the main food and visible side items.

### Test 2: South Indian Thali

![South Indian Thali API Result](../../evidence/south-indian-thali-result.jpg)

- **Food:** South Indian Thali
- **Other Items:** Rice, sambar, rasam, vegetable curries, curd, puri, papadum
- **Category:** Indian Cuisine
- **Cooking:** Steamed, boiled, deep-fried
- **Ingredients:** White rice, lentils, drumsticks, green vegetables, curd, wheat flour
- **Portion:** Large
- **Confidence:** High
- **Observation:** Multiple food items were identified. Exact regional names of some small side curries may vary.

### Test 3: Poori

![Poori API Result](../../evidence/poori-result.jpg)

- **Food:** Poori
- **Other Items:** None
- **Category:** Fried Bread
- **Cooking:** Deep-fried
- **Ingredients:** Wheat flour dough
- **Portion:** Medium
- **Confidence:** High
- **Observation:** The food was correctly identified. Exact dough type cannot be determined from the image.

### Test 4: Poha

![Poha API Result](../../evidence/poha-result.jpg)

- **Food:** Poha
- **Other Items:** Cilantro garnish, green chilies
- **Category:** Indian Breakfast
- **Cooking:** Stir-fried
- **Ingredients:** Flattened rice, potatoes, peanuts, cilantro, green chilies, mustard seeds
- **Portion:** Medium
- **Confidence:** High
- **Observation:** The model identified Poha and its visible ingredients.

### Test 5: Samosa

![Samosa API Result](../../evidence/samosa-result.jpg)

- **Food:** Samosa
- **Other Items:** None
- **Category:** Snack
- **Cooking:** Deep-fried
- **Ingredients:** Fried pastry shell
- **Portion:** Small
- **Confidence:** High
- **Observation:** The main food was correctly identified. Internal filling was not clearly visible.

## 4. Testing Summary

- Total images tested: 5
- All five main food items were identified correctly.
- The API also identified visible side dishes and ingredients.
- Some hidden ingredients and exact regional food details could not be confirmed from images.


## 5. Technical Feasibility

The approach was successfully tested using Python, Flask and the Gemini API.

**Requirements:**
- Python environment
- Flask
- Google GenAI Python SDK
- Gemini API key
- Internet connection

**Cost:** API usage may incur charges depending on the Google AI Studio model, free-tier limits and current pricing.

**Limitations:**
- Hidden ingredients cannot always be identified.
- Portion size is approximate.
- Similar-looking food items may be confused.
- Results depend on image quality and visibility.
- API availability and usage limits depend on Google.


## 6. References and Sources

1. **Google AI Studio:** Model selection and API experimentation  
   https://aistudio.google.com/

2. **Gemini API Documentation:** API integration and Python implementation  
   https://ai.google.dev/gemini-api/docs

3. **Google GenAI Python SDK:**  
   https://github.com/googleapis/python-genai

4. **Model Picker Screenshot:**  
   ![Gemini Model Picker](../../evidence/model-picker.jpg)

