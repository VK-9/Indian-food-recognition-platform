# TASKS.md - Indian Food Recognition & Nutrition App

## 1. Purpose

This file is the source of truth for current project tasks, owners, priorities, deliverables, and completion status.

The objective is to investigate, build, and test an early prototype of an Indian food recognition and nutrition app, with an optional traditional food *tasir* (garam/thanda) feature.

This is an exploratory project. The first milestone is a working, testable prototype-not a production-ready application.

## 2. Working Rules

1. Read `README.md` and your individual PDF task brief before starting.
2. Work on your assigned tasks and keep progress updated in this file.
3. Use a separate Git branch for each feature or task.
4. Submit code changes through pull requests. Do not commit directly to `main`.
5. Document evidence, sources, assumptions, failures, and unresolved questions.
6. Do not claim that something works unless you have tested it.
7. Do not add API keys, passwords, private credentials, or personal data to the repository.
8. Raise blockers early, with details of what you tried and what happened.
9. Ask for clarification when requirements or acceptance criteria are unclear.

## 3. Status Definitions

Use these status values:

- `NOT STARTED` - Work has not begun.
- `IN PROGRESS` - Work is underway.
- `BLOCKED` - Progress depends on an unresolved issue.
- `IN REVIEW` - Submitted for review.
- `DONE` - Acceptance criteria have been met and the work has been reviewed.

A task is not `DONE` simply because its report or code has been submitted.

## 4. Priority Definitions

- `P0` - Essential for the first prototype.
- `P1` - Important, but can follow the initial working flow.
- `P2` - Optional improvement or future investigation.

## 5. Task Board

| ID | Task | Owner | Priority | Status |
|---|---|---|---|---|
| SVL-01 | Investigate reference app and map user journey | Student A - Shyam | P0 | NOT STARTED |
| SVL-02 | Investigate development approach and technical feasibility | Student A - Shyam | P0 | NOT STARTED |
| SVL-03 | Build initial food-image input and result flow | Student A - Shyam | P0 | NOT STARTED |
| SVL-04 | Create initial Indian food dataset | Student B - Khushi | P0 | NOT STARTED |
| SVL-05 | Research nutrition sources and serving assumptions | Student B - Khushi | P0 | NOT STARTED |
| SVL-06 | Research Tasir classifications for a small food set | Student B - Khushi | P1 | NOT STARTED |
| SVL-07 | Design food correction and optional Tasir feedback flow | Shared - A leads implementation; B leads data requirements | P1 | NOT STARTED |
| SVL-08 | Integrate prototype with initial food data | Shared | P0 | NOT STARTED |
| SVL-09 | Test prototype and document findings | Shared | P0 | NOT STARTED |
| SVL-10 | Review contributions and present final demonstration | Shared | P0 | NOT STARTED |

The owner assignments are initial working assignments. They may be adjusted based on progress, dependencies, and demonstrated strengths.

---

## 6. Detailed Tasks

### SVL-01 - Investigate the Reference App and Map Its User Journey

**Owner:** Student A - Shyam  
**Priority:** P0

#### Objective

Understand how the reference food-scanning app works from a user's perspective.

#### Actions

- Install or access the reference app where possible.
- Observe the onboarding and food-scanning journey.
- Record the steps from opening the app to viewing the food analysis.
- Identify the information shown to users and any available editing options.
- Observe how the app handles ambiguous images, mixed meals, and incorrect predictions where testable.
- Identify useful features and opportunities to improve the experience for Indian users.

#### Deliverables

- `docs/research/reference-app.md`
- A user-journey diagram or clearly numbered workflow.
- Screenshots or notes from authorized observations, where appropriate.
- A list of useful features, gaps, and unanswered questions.

#### Acceptance criteria

- The user journey is documented from input to result.
- Direct observations are separated from assumptions.
- At least five specific product observations or improvement opportunities are documented.
- Any untested behaviour is explicitly marked as untested.

**Important:** Do not bypass access controls or attempt to obtain proprietary code or private data. Use authorized, observable functionality and permitted investigation methods.

### SVL-02 - Investigate the Technical Approach

**Owner:** Student A - Shyam  
**Priority:** P0

#### Objective

Determine a realistic way to implement the first prototype with the tools and resources available.

#### Actions

- Investigate suitable approaches for food-image input and recognition.
- Evaluate available APIs, models, or other feasible approaches.
- Determine what can be implemented without paid services, where practical.
- Document setup requirements, limitations, and possible costs.
- Investigate REA only where it is relevant and technically supported.
- Recommend a simple architecture for the first prototype.

#### Deliverables

- `docs/research/technical-feasibility.md`
- A short architecture diagram or component list.
- A recommendation with alternatives and trade-offs.
- Setup instructions and a list of blockers or external dependencies.

#### Acceptance criteria

- The recommendation is supported by evidence or a reproducible test.
- The report distinguishes tested approaches from documentation-based research.
- Limitations, expected costs, and dependencies are disclosed.
- The proposed approach is small enough for an initial prototype.

### SVL-03 - Build the Initial Food-Image Input and Result Flow

**Owner:** Student A - Shyam  
**Priority:** P0

#### Objective

Build the first usable application flow that accepts a food image and presents a result.

#### Initial scope

- Allow image upload or camera input where supported.
- Submit the image to the selected recognition approach.
- Display the predicted food or dish.
- Display an uncertainty message or fallback when a reliable prediction is unavailable.
- Show nutrition estimates when supported by available data.
- Provide a basic loading state and error handling.

If live recognition is not feasible with available resources, first build the interface using clearly labelled sample results and document what is required to connect a real recognition service.

#### Deliverables

- Working prototype code.
- `docs/product/scan-flow.md`
- Instructions for running the feature.
- Test notes, screenshots, and known issues.

#### Acceptance criteria

- Another contributor can run the prototype using the documented steps.
- A user can submit an image and see the expected result or a clear error.
- Sample results are clearly distinguished from real predictions.
- The interface does not present unverified nutrition estimates as exact facts.
- Credentials are not committed to GitHub.

### SVL-04 - Create the Initial Indian Food Dataset

**Owner:** Student B - Khushi  
**Priority:** P0

#### Objective

Create a small, structured dataset of Indian foods that can be used by the prototype.

#### Actions

- Begin with 30-50 common Indian foods or dishes.
- Include a useful mix of everyday meals, snacks, breads, rice dishes, lentil dishes, and regional foods.
- Include alternate or regional names when available.
- Record important ingredient or preparation differences.
- Identify dishes that may be visually similar.
- Record the source and confidence of each entry.

#### Deliverables

- `data/food/foods.csv` or an agreed equivalent structured format.
- `docs/research/food-dataset-notes.md`
- A data dictionary explaining each field.

#### Suggested fields

- `food_id`
- `food_name`
- `regional_names`
- `food_category`
- `common_ingredients`
- `preparation_notes`
- `serving_size`
- `serving_unit`
- `nutrition_source`
- `confidence_or_notes`

Nutrition fields may be added when values and sources are available. Do not invent values to fill empty cells.

#### Acceptance criteria

- At least 30 entries are documented.
- The dataset has a consistent structure.
- Duplicate entries and obvious naming inconsistencies are checked.
- Important recipe variations are noted.
- Sources and uncertainty are recorded where relevant.

### SVL-05 - Research Nutrition Sources and Serving Assumptions

**Owner:** Student B - Khushi  
**Priority:** P0

#### Objective

Determine how the prototype can present nutrition information responsibly for Indian foods.

#### Actions

- Investigate credible Indian food-composition sources, including ICMR-National Institute of Nutrition resources where relevant.
- Identify which foods can be matched to reliable nutrition records.
- Distinguish values for raw ingredients, cooked ingredients, and prepared dishes.
- Document serving-size assumptions and unit conversions.
- Investigate the limitations of estimating portion size from an image.
- Identify where recipes vary too much for one generic nutrition estimate.

#### Deliverables

- `docs/research/nutrition-sources.md`
- Source references for the initial dataset.
- A recommendation for how nutrition values and estimates should be displayed.

#### Acceptance criteria

- Sources are traceable.
- Raw and cooked values are not mixed without explanation.
- Serving sizes and units are documented.
- Unknown values are left unknown rather than fabricated.
- Limitations of image-based estimation are clearly stated.

### SVL-06 - Research Tasir Classifications

**Owner:** Student B - Khushi  
**Priority:** P1

#### Objective

Investigate how a small set of foods are traditionally classified as *garam* or *thanda*, while documenting differences between sources and traditions.

#### Actions

- Select 10-15 foods from the initial food dataset.
- Look for traceable traditional references where available.
- Record differences in classification across sources or contexts.
- Note where classifications depend on preparation, ingredients, or tradition.
- Separate source-based findings from personal or crowd-reported beliefs.
- Propose how the app should communicate uncertainty.

#### Deliverables

- `data/tasir/tasir.csv` or an agreed equivalent.
- `docs/research/tasir-research.md`
- A short recommendation for how the quiz should ask and display responses.

#### Suggested fields

- `food_id`
- `reported_classification`
- `tradition_or_region`
- `source_name`
- `source_reference`
- `preparation_context`
- `confidence_or_notes`
- `review_status`

#### Acceptance criteria

- At least 10 foods have been investigated.
- Sources and context are recorded wherever available.
- Disagreements are documented instead of forced into one universal answer.
- Unverified crowd responses are labelled as user-reported.
- The feature does not make unsupported medical or disease-treatment claims.

### SVL-07 - Design Food Correction and Tasir Feedback

**Lead:** Student A - Shyam, for implementation  
**Lead:** Student B - Khushi, for data requirements  
**Priority:** P1

#### Objective

Design a feedback flow that helps improve the product without treating every user response as verified data.

#### Proposed flow

1. The app predicts a food or reports that it cannot identify the image confidently.
2. The user can correct the food name or provide additional details.
3. The app optionally asks the user to answer a short Tasir question.
4. Responses are stored for review under an appropriate consent and data-retention process.
5. Reviewed submissions may be incorporated into curated datasets.

#### Actions

- Define the correction fields and optional quiz questions.
- Decide what happens when the user skips the quiz.
- Design basic validation and error handling.
- Define how submissions are marked as pending, reviewed, or rejected.
- Document privacy, consent, duplicate-submission, and abuse considerations.

#### Deliverables

- `docs/product/feedback-flow.md`
- A basic UI flow or prototype.
- An agreed data structure for submissions.

#### Acceptance criteria

- Food correction and Tasir feedback are distinguishable.
- Users can skip optional questions.
- The flow does not claim that every response trains the AI immediately.
- Unreviewed submissions can be distinguished from reviewed records.
- Data collection and retention are documented before retaining user-submitted images or identifiable information.

### SVL-08 - Integrate the Prototype and Initial Dataset

**Owner:** Shared  
**Priority:** P0

#### Objective

Connect the application flow to the initial food dataset and provide a coherent demonstration.

#### Actions

- Agree on the data format and integration interface.
- Connect the result flow to available food records.
- Show nutrition information only when an appropriate record is available.
- Provide a clear fallback for unmatched or ambiguous foods.
- Resolve integration issues through reviewed pull requests.

#### Deliverables

- An integrated prototype.
- Updated setup instructions.
- A short record of integration decisions and remaining limitations.

#### Acceptance criteria

- The application and dataset work together in the agreed demo flow.
- Missing data does not cause misleading output.
- Another contributor can run the integrated prototype.
- The team documents known integration issues.

### SVL-09 - Test the Prototype

**Owner:** Shared  
**Priority:** P0

#### Objective

Determine what works, what fails, and what should be improved next.

#### Actions

Test a small, agreed set of cases, including:

- Clear images of common dishes.
- Mixed Indian meals.
- Visually similar foods.
- Poor-quality or ambiguous images.
- Unknown foods.
- Incorrect user corrections.
- Foods with missing nutrition data.
- Different preparations of the same dish.
- Skipped Tasir questions.
- Error or unavailable-service scenarios.

#### Deliverables

- `tests/test-cases.md`
- `docs/research/prototype-test-results.md`
- A prioritized list of bugs and improvements.

#### Acceptance criteria

- Each test has an input, expected behaviour, observed result, and status.
- Failed tests are documented honestly.
- The team identifies the most important issues rather than only reporting successful cases.
- Any claimed accuracy metric includes its test method and sample size.

### SVL-10 - Demonstrate and Review the Work

**Owner:** Shared  
**Priority:** P0

#### Objective

Present the investigation, implementation, and learning from the initial milestone.

#### Each student should be able to explain

- What they investigated and why.
- What they personally implemented or contributed.
- Which sources and tools they used.
- What they tested and what happened.
- What failed or remains uncertain.
- What they would change next and why.

#### Deliverables

- A short working demonstration.
- A summary of individual contributions.
- Updated documentation.
- A list of next steps and unresolved questions.

#### Acceptance criteria

- The demonstration matches the actual state of the project.
- Each contributor can explain their own work and important decisions.
- Known limitations are disclosed.
- The next development priorities are supported by findings from the milestone.

---

## 7. Initial Milestone Plan

Use this as a suggested sequence, not a substitute for the deadlines agreed in each student's task brief.

| Stage | Focus | Expected outcome |
|---|---|---|
| Stage 1 | Investigation and setup | Reference-app notes, feasibility findings, initial dataset plan |
| Stage 2 | Independent work | Initial scan flow and structured food dataset |
| Stage 3 | Integration | Prototype connected to available food records |
| Stage 4 | Validation | Test results, issues, and recommended next steps |
| Stage 5 | Review | Demonstration and individual contribution review |

Tasks may overlap when dependencies allow. The project owner will confirm the actual checkpoints.

## 8. Definition of Done

A task is ready for review when:

- The requested deliverable exists.
- Acceptance criteria have been checked.
- Research sources and assumptions are documented.
- Code runs or setup limitations are clearly explained.
- Relevant tests have been performed.
- Known issues are disclosed.
- Changes are committed to the appropriate branch.
- A pull request is ready where code or shared files have changed.

The project owner marks the task `DONE` after reviewing the submission.

## 9. Progress Updates

Each student should update their task status and communicate progress at agreed checkpoints.

Use this format for a concise update:

- **Completed:** What has been done?
- **Evidence:** What can be reviewed or demonstrated?
- **Blocked by:** What is preventing progress, if anything?
- **Next:** What will be done next?
- **Help needed:** What decision or assistance is required?

Progress should be judged by evidence, reasoning, quality, and learning-not by the length of a report or the amount of code written.

## 10. Future Backlog

These items are intentionally outside the initial milestone unless the project owner approves them:

- Improved mixed-meal detection and portion estimation.
- More extensive regional-food coverage.
- A reviewed food-image dataset.
- Better recognition confidence and correction handling.
- Duplicate detection and abuse prevention for feedback submissions.
- A curated Tasir knowledge base with source and tradition metadata.
- User accounts and cloud data storage.
- Automated model training or fine-tuning.
- Production deployment, analytics, and scaling.

Do not begin these items until the initial prototype's core flow has been tested and reviewed.

---

**Project principle:** Build the smallest useful version, test it with real examples, document the evidence, and improve it based on what we learn.
