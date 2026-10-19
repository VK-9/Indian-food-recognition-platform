# PRODUCT_BRIEF.md
# Indian Food Recognition & Nutrition App

**Project:** Student Venture Lab  
**Organization:** Nine Myths Pvt. Ltd.  
**Version:** 1.0  
**Status:** Initial product definition

---

## 1. Product Vision

Build a food-scanning app that helps Indian users identify what is on their plate, understand its estimated nutritional value, and explore traditional food *tasir* (garam/thanda) classifications.

The app should be particularly useful for Indian foods, including regional dishes, homemade meals, and foods that may be difficult for generic food-recognition systems to identify correctly.

The first objective is to build and test a small working prototype. We are not attempting to build a complete commercial product at this stage.

## 2. The Problem

People who want to understand their food intake face several challenges:

- Food-scanning applications may not recognize Indian regional dishes reliably.
- Similar-looking dishes may have different ingredients and nutritional profiles.
- Homemade meals vary in recipes, cooking methods, and portion sizes.
- A photograph cannot always reveal the exact ingredients or quantity of oil used.
- Users may want to understand traditional food classifications, but these can vary across regions, families, and sources.
- When an app identifies a dish incorrectly, users need a simple way to correct it.

We want to explore whether a product designed around these realities can provide a better experience for Indian users.

## 3. Target User

Our initial target user is an Indian person who wants to understand the food they eat without manually entering every ingredient.

Example users include:

- Someone tracking daily calories and macronutrients.
- Someone eating homemade Indian meals.
- Someone who eats regional dishes that may be unfamiliar to generic food databases.
- Someone curious about traditional food *tasir* classifications.

These are initial hypotheses about users, not validated market research. The team should identify which user needs are most important during testing.

## 4. Core Product Principles

The prototype should follow these principles:

1. **Simple first experience:** A user should be able to start a food scan without navigating a complicated interface.
2. **Honest predictions:** The app must not pretend to recognize food when it is uncertain.
3. **User correction:** Users should be able to correct an incorrect or incomplete food identification.
4. **Useful nutrition information:** Show sourced nutritional values or clearly labelled estimates with appropriate assumptions.
5. **Indian food context:** Support regional names, ingredient variations, and preparation differences where feasible.
6. **Optional Tasir participation:** Users may share their understanding of a dish's traditional classification without being forced to answer.
7. **Responsible data collection:** Feedback must be collected and retained under an appropriate privacy and consent process.
8. **Continuous improvement:** User feedback should help us identify gaps and build better-reviewed datasets.

## 5. Primary User Journey

The following is the expected product flow. Students may propose improvements, but significant changes should be documented and discussed before implementation.

### Step 1 — Open the app

The user sees a simple home screen with a clear option to scan food.

**Expected behaviour:** The user understands what the app does and how to start.

### Step 2 — Capture or upload a food image

The user takes a photograph or selects an existing image.

**Expected behaviour:**
- The app accepts a supported image format.
- The user can see which image they selected.
- The app handles invalid or unsupported images gracefully.

For the first prototype, one image representing one meal is sufficient.

### Step 3 — Identify the food

The app attempts to identify the food or dish.

**Expected behaviour:**
- Display the predicted dish or dishes.
- Show an uncertainty message when the prediction is unreliable.
- Provide a way to correct the result.
- Avoid displaying a confident but unsupported identification.

The technical approach used to recognize the food is an implementation decision for the students.

### Step 4 — Confirm the dish and portion

The user can confirm the prediction or correct the food name.

Where practical, the app should also let the user clarify the serving size or portion.

For a mixed meal, the app may identify multiple items if the selected approach supports it. If reliable identification is not possible, it should clearly communicate the limitation.

**Expected behaviour:** The user can correct an incorrect result rather than being forced to accept it.

### Step 5 — View food and nutrition information

The app displays available information for the identified food.

The initial result may include:

- Food or dish name.
- Estimated calories.
- Protein.
- Carbohydrates.
- Fat.
- Serving size and assumptions.
- Relevant notes about preparation or data limitations.

**Expected behaviour:**
- Nutrition values are linked to appropriate food records or sources.
- Estimated values are labelled as estimates.
- The app does not invent values when reliable information is unavailable.
- The interface makes it clear that a photograph alone cannot determine exact ingredients or nutritional content.

A complete nutrition profile is not mandatory for every food in the initial prototype.

### Step 6 — Offer an optional Tasir quiz

After the food result, the app may invite the user to answer a short question.

Example:

**How is this food traditionally classified in your understanding?**

- Garam
- Thanda
- Depends on preparation or ingredients
- Not sure

Depending on the product design, the app may ask what the response is based on, such as family or regional tradition, a traditional reference, or personal understanding.

**Expected behaviour:**
- The quiz is optional.
- The user can skip it without losing the food result.
- The app records the response separately from food-recognition feedback.
- The interface does not imply that a crowd-reported classification is scientifically established or medically proven.

### Step 7 — Save feedback for review

If a user corrects a dish or submits a Tasir response, the system may retain that feedback only under an appropriate data-collection and consent process.

**Expected behaviour:**
- Food corrections and Tasir responses remain distinguishable.
- Submissions can be marked as pending review, accepted, or rejected.
- Unreviewed submissions are not automatically treated as verified ground truth.
- Retention of images and other user-submitted information is documented.

Automated model training is outside the initial prototype's requirements.

---

## 6. Important Alternative Flow: Food Not Recognized

Failure handling is a core part of the product, not an afterthought.

When the app cannot confidently identify a dish:

1. Tell the user that the prediction is uncertain or unavailable.
2. Ask the user to enter or select the food name, if they know it.
3. Allow a regional or alternative name where practical.
4. Optionally collect ingredients or preparation details.
5. Let the user continue with the information available.
6. Record the correction for review, where consent and retention requirements are satisfied.

The app should not block the user from continuing simply because recognition failed.

For the first prototype, a basic manual correction field is sufficient. Advanced suggestions, automated verification, and model retraining can be considered later.

## 7. Minimum Viable Prototype (MVP)

The MVP is the smallest version that can demonstrate the product's core value.

### Must have

- A basic interface for uploading a food image.
- A defined food-recognition step, using a feasible recognition service or a clearly labelled demonstration substitute.
- A screen showing the prediction or an appropriate failure state.
- A way for the user to correct the food name.
- A connection to a small structured Indian food dataset.
- Display of available nutrition information, with appropriate assumptions and limitations.
- Basic loading and error handling.
- Setup instructions and reproducible test cases.

### Should have, if feasible

- Portion or serving-size selection.
- Regional and alternative food names.
- Recognition of multiple foods in one image.
- An optional Tasir quiz.
- A basic mechanism for storing feedback for review.

### Not required in the first milestone

- A production-ready mobile app.
- User accounts or subscription payments.
- A complete Indian food database.
- Guaranteed calorie accuracy from photographs.
- Automatic model training from user feedback.
- Medical or personalized dietary recommendations.
- A comprehensive, universally agreed Tasir database.
- Production deployment or large-scale infrastructure.

The project owner may approve additional scope after the MVP is demonstrated and tested.

## 8. Data Requirements

The application will depend on structured food information.

At a minimum, the initial food dataset should identify:

- A unique food identifier.
- Food or dish name.
- Alternative or regional names, where available.
- Relevant ingredients or preparation notes.
- Serving-size assumptions, where applicable.
- Available nutrition values.
- Source references and limitations.

Tasir information should be maintained separately or in a clearly distinct data structure. Where possible, it should include the classification, source or basis, relevant tradition or region, preparation context, and review status.

Do not force uncertain information into a definitive answer merely to complete a dataset.

## 9. Safety, Accuracy, and Trust

The product must distinguish between three different kinds of information.

### A. Nutritional information

Nutrition values should be sourced or clearly identified as estimates. Serving sizes, recipe variation, and uncertainty must be acknowledged.

### B. Traditional Tasir classifications

Tasir is a traditional classification that may vary by tradition, source, region, preparation, and context.

The app may document these classifications, but must not present them as established clinical facts or claim that a food will treat, prevent, or cause a disease based solely on its classification.

### C. User-reported feedback

A user's correction or quiz response represents their contribution or understanding. It is not automatically proof that the food identification or classification is correct.

Images and feedback must be handled responsibly. Collect only what is necessary, explain the intended use, and apply an appropriate consent and retention process.

## 10. How We Will Evaluate the MVP

The prototype should be tested against a small, documented set of real examples.

Test cases should include:

- Clear images of common Indian dishes.
- Mixed meals, where supported.
- Visually similar dishes.
- Regional dishes or alternative food names.
- Ambiguous or low-quality images.
- Incorrect food predictions.
- Foods with incomplete nutrition data.
- Failed recognition requests.
- Skipped Tasir questions, if the quiz is implemented.

For each test, record the input, expected behaviour, observed result, and any limitation.

We should evaluate whether the app handles failures honestly—not just how many images it recognizes successfully.

## 11. Definition of Success

The first milestone will be considered successful when:

1. A contributor can run the prototype using the documented setup instructions.
2. A user can submit a food image and receive a prediction or a clear fallback.
3. The user can correct an incorrect food identification.
4. The app can display appropriate information from the initial structured dataset.
5. Nutrition values and assumptions are communicated responsibly.
6. The team can demonstrate the user journey and explain known limitations.
7. Tests and research findings are documented.
8. The students can explain their individual contributions and the decisions they made.

The Tasir quiz is a useful exploratory feature, but it is not a prerequisite for demonstrating the core food-scanning workflow.

## 12. Product Decisions vs. Student Decisions

The project owner defines the target problem, expected user journey, initial scope, privacy principles, and acceptance criteria.

Students are expected to investigate and recommend:

- The technical architecture.
- The recognition model or API.
- The implementation approach.
- The data format and integration method.
- The handling of uncertainty.
- The test strategy.
- Potential product improvements.
- The best next steps based on evidence.

Students should not wait for detailed instructions on every technical decision. They should document their reasoning, discuss important trade-offs, and demonstrate what they have learned.

## 13. Questions for Both Students

Before or during implementation, each student should independently answer:

1. What is the biggest weakness in this proposed user journey?
2. Which assumption in this product brief should we test first?
3. What is the most difficult technical or data problem in this MVP?
4. What would you simplify to deliver a useful prototype sooner?
5. How would you determine whether the product is actually helping its target user?

These questions are intended to encourage independent thinking. Different answers are welcome when supported by evidence and reasoning.

## 14. Relationship to Other Project Documents

- `README.md` explains the project background, working principles, and repository workflow.
- `PRODUCT_BRIEF.md` defines the product vision, user journey, scope, and success criteria.
- `TASKS.md` defines the current task owners, priorities, status, and acceptance criteria.
- Individual PDF briefs specify each student's assigned responsibilities and deliverables.

If a technical implementation decision needs to change the expected product behaviour, document the proposed change and discuss it with the project owner before proceeding.

---

**Our guiding principle: Build a useful, testable experience for Indian users. Be honest about uncertainty. Learn from evidence, not assumptions.**
