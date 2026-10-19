# Student Venture Lab — Indian Food Recognition & Nutrition App

## 1. Project Overview

This project is part of **Student Venture Lab (SVL)**, an initiative by **Nine Myths Pvt. Ltd.** to give students practical experience investigating problems, building solutions, testing ideas, and learning through real product development.

We are exploring an app that helps users identify food from images and understand its nutritional information, with a particular focus on Indian foods and eating habits.

The project will use an existing food-scanning app, such as CAL AI, as a reference for understanding the user experience and product workflow. The goal is **not to copy its proprietary code, assets, or protected design**, but to learn from publicly observable functionality and independently build a useful solution for Indian users.

## 2. Problem We Want to Solve

Food recognition and nutrition tracking can be challenging when users eat Indian meals, including:

- Regional dishes with different local names.
- Mixed meals containing multiple food items.
- Foods that look similar but have different ingredients or preparation methods.
- Homemade dishes with variable portions, recipes, and cooking methods.
- Foods for which users also want to understand traditional *tasir* (garam/thanda) classifications.

Our initial goal is to investigate these problems and build a working prototype that addresses a small, clearly defined part of them.

## 3. Initial Product Scope

The initial prototype may include the following features.

### A. Food Image Recognition

- Allow a user to upload or capture a food image.
- Predict the likely food or dish.
- Show an indication of uncertainty when the prediction is unreliable.
- Allow users to correct the predicted dish.
- Support regional names and alternative spellings where practical.

### B. Nutrition Information

Where reliable data is available, display estimated nutritional information such as:

- Calories.
- Protein.
- Carbohydrates.
- Fat.
- Estimated serving size or portion.

Nutrition estimates must clearly communicate their assumptions and limitations. An image alone may not reveal the exact ingredients, oil quantity, recipe, or portion weight.

### C. Food Correction and Learning

When the app cannot identify a dish confidently or gives an incorrect result, users may be asked to provide additional information, such as:

- Correct food or dish name.
- Regional or alternative name.
- Ingredients, where known.
- Preparation method, where relevant.
- Optional portion or serving details.

These submissions can help us identify recognition gaps and build a better-reviewed dataset.

**Important:** User submissions are feedback, not automatically verified ground truth. They must not be treated as reliable training data without appropriate review and validation.

### D. Food Tasir Quiz

We will explore a short, optional, engaging quiz that asks users how they traditionally classify a food or dish.

For example:

**How is this food traditionally classified in your understanding?**
- Garam
- Thanda
- Depends on preparation or ingredients
- Not sure

Where useful, the app may also ask what the response is based on, such as family or regional tradition, a traditional reference, or personal understanding.

Tasir information must be presented carefully. Traditional classifications can vary across regions, families, and traditions. They must not be presented as proven medical facts or as a substitute for medical advice.

## 4. Project Principles

All contributors are expected to follow these principles:

1. **Investigate before building.** Understand the problem and existing solutions before choosing an implementation.
2. **Show evidence.** Distinguish what was directly observed or tested from what was inferred or remains unknown.
3. **Prefer working prototypes.** A small, testable feature is more useful than a large feature that exists only in a document.
4. **Be honest about uncertainty.** Do not invent results, sources, test outcomes, or technical capabilities.
5. **Validate information.** Nutrition data and traditional food information should have traceable sources and clearly stated limitations.
6. **Design for Indian users.** Consider regional dishes, names, ingredients, recipes, and practical usage conditions.
7. **Respect privacy.** Collect only necessary user data. Images and feedback should be retained only under an appropriate, clearly communicated data policy and consent process.
8. **Build responsibly.** Use authorized resources, respect intellectual property, and check the licences of code, models, datasets, and dependencies.
9. **Communicate clearly.** Document decisions, blockers, failed experiments, and next steps.
10. **Learn through iteration.** Testing and correcting a failed approach is part of the work.

## 5. Development Workflow

We intend to use the following tools where suitable:

- **GitHub:** Shared repository, version control, task tracking, and code review.
- **Antigravity:** Primary development environment, subject to tool availability.
- **OpenCode:** Additional coding and review assistance where suitable.
- **Claude:** Assistance with reasoning, research synthesis, and reviewing approaches where available.
- **Reverse Engineer Anything (REA):** Investigation of supported software or artefacts where lawful, technically feasible, and authorized.

Tool availability, free-tier limits, supported models, and capabilities may change. Contributors must verify what is available and document any limitations encountered.

AI tools can make mistakes. Generated code, research, nutrition estimates, and conclusions must be checked rather than accepted automatically.

## 6. Repository Structure

The repository may evolve as the project develops. The initial structure is expected to follow this pattern:

```text
/
├── README.md
├── TASKS.md
├── docs/
│   ├── research/
│   ├── product/
│   └── decisions/
├── data/
│   ├── food/
│   └── tasir/
├── src/
├── tests/
└── .gitignore
```

Not every folder needs to be created immediately. Add folders when they become useful.

- `README.md`: Project purpose, principles, and shared workflow.
- `TASKS.md`: Current tasks, owners, priorities, acceptance criteria, and status.
- `docs/research/`: Research notes, observations, sources, and investigation results.
- `docs/product/`: User journeys, feature definitions, and product decisions.
- `docs/decisions/`: Important technical or product decisions and their reasoning.
- `data/food/`: Food information and nutrition datasets, with source details.
- `data/tasir/`: Tasir classifications and their sources, context, and uncertainty.
- `src/`: Application code.
- `tests/`: Test cases, results, and relevant test data.

The repository structure is a starting point, not a requirement to create empty folders before work begins.

## 7. GitHub Contribution Rules

Each student should use their own GitHub account.

- Create a separate branch for each assigned feature or task.
- Avoid making changes directly to the `main` branch.
- Submit a pull request when work is ready for review.
- Explain what changed, why it changed, and how it was tested.
- Include screenshots or short demonstrations when they help verify a feature.
- Address review feedback and fix issues before merging.
- Keep commits focused and descriptive.
- Update relevant documentation when implementation or assumptions change.

The project owner will review and approve changes before they are merged into the main branch.

Never commit API keys, passwords, access tokens, private credentials, personal information, or unapproved user images. Use environment variables and an appropriate local configuration file excluded by `.gitignore`.

## 8. Research and Evidence Standards

Research should be reproducible and useful to someone who was not present during the investigation.

When investigating a feature or tool, document:

- The question being investigated.
- The source or method used.
- What was directly observed.
- What was tested and the steps followed.
- The results, including failures.
- What is inferred rather than confirmed.
- Limitations and unanswered questions.
- The next recommended action.

Where external information is used, record the source URL, relevant date where applicable, and any important limitations.

Do not describe a feature as tested unless you actually tested it. If testing was not possible, explain why and distinguish documentation-based understanding from hands-on findings.

## 9. Food Data and Tasir Data Standards

### Food and Nutrition Data

Where possible, each food record should include:

- Food or dish name.
- Regional or alternative names.
- Ingredients or recipe context, if known.
- Preparation method, if relevant.
- Serving-size assumptions.
- Nutritional values and units.
- Data source and reference details.
- Confidence, limitations, or missing information.

Do not assume every dish has one fixed nutritional profile. Recipes and preparation methods can substantially affect the result.

### Tasir Data

Where possible, each record should include:

- Food or dish name.
- The reported classification.
- Region or tradition, when voluntarily provided and relevant.
- Source or basis for the classification.
- Preparation or ingredient context, if relevant.
- Conflicting classifications or uncertainty.
- Review status.

Keep user-reported beliefs distinct from classifications supported by a named traditional reference. Neither should automatically be treated as clinical evidence.

## 10. Testing Expectations

Every implemented feature should have a clear way to verify whether it works.

Testing may include:

- Normal use cases.
- Incorrect or ambiguous inputs.
- Indian regional foods and mixed meals.
- Poor lighting, unusual angles, or low-quality images.
- Incorrect food predictions and user corrections.
- Missing nutrition data.
- Different preparation methods or serving assumptions.
- Error handling and loading states.
- Privacy and data-retention behaviour, where implemented.

Record important test results and known issues. Do not hide failed tests or claim accuracy without a defined test method and supporting results.

## 11. Communication and Ownership of Tasks

The `TASKS.md` file is the current source of truth for assigned work.

Each task should have:

- A clear objective.
- An owner.
- A priority.
- A deadline or agreed checkpoint, where applicable.
- Expected deliverables.
- Acceptance criteria.
- Dependencies or known blockers.
- A current status.

If a task is blocked, communicate the issue early. Explain what was attempted, what failed, and what help or decision is needed.

Contributors should work independently where possible, while reviewing one another's work and collaborating on integration and testing.

The detailed individual assignments and instructions provided separately take precedence for each student's assigned deliverables.

## 12. What Success Looks Like

At this stage, success is not defined by launching a complete commercial app.

Useful progress includes:

- A clear understanding of the problem and target users.
- Research supported by observable evidence and credible sources.
- A documented, realistic product scope.
- A working prototype of one or more important flows.
- A structured and traceable initial food dataset.
- A thoughtful approach to food corrections and Tasir feedback.
- Tests that reveal strengths, weaknesses, and failure cases.
- Code that another contributor can understand and run.
- Clear communication, responsible collaboration, and demonstrable learning.

Commercial success is not guaranteed. The purpose of this stage is to investigate, build, test, and learn.

## 13. Intellectual Property and Confidentiality

All contributions must follow the applicable joining letter and any additional written agreement provided by Nine Myths Pvt. Ltd.

Do not publish confidential project information, private datasets, credentials, unreleased features, or other restricted material without permission.

Check the licence and permitted use of all third-party code, datasets, models, tools, and assets before incorporating them into the project.

## 14. Getting Started

Before beginning a task:

1. Read this `README.md`.
2. Read `TASKS.md`.
3. Review your separate task brief and instructions.
4. Confirm that you can access the repository and create a branch.
5. Set up the required tools and document any installation problems.
6. Ask questions when requirements or acceptance criteria are unclear.
7. Keep your research, code, tests, and progress documented.
8. Submit your work for review through a pull request.

**Our working principle: Investigate carefully. Build something testable. Validate the result. Document what you learn.**
