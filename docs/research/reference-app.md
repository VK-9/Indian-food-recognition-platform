# SVL-01 – Reference App Investigation and User Journey

**Reference Application:** Cal AI  
**Investigation Type:** Reference App Study and User Journey  
**Status:** Partially Completed

---

## 1. Objective

The main aim of this task is to understand how the Cal AI application works from a user's point of view.

This study focuses on the app's onboarding process, user details, fitness goals, account creation, subscription screen, and food-scanning process.

The purpose is to learn from the reference app and find ways to make our Indian Food Recognition & Nutrition App more useful and easy to use.

## 2. Reference Application

**Application Name:** Cal AI

**Application Website:** https://www.calai.app/

Cal AI is an application that helps users track their food, calories, and daily nutrition.

It helps users understand how much food they eat and keep track of their nutrition.

We studied the features that were available to us in the app and also used other available reference material for screens that we could not access directly.

No private data, restricted features, or app code was accessed.

## 3. Investigation Method

The following steps were followed during the investigation:

1. Opened the Cal AI application.
2. Started the onboarding process.
3. Checked the questions asked during setup.
4. Noted the personal details and fitness goals requested by the app.
5. Checked the daily calorie and nutrition targets.
6. Continued to the account creation screen.
7. Reached the subscription screen.
8. Stopped the direct testing without purchasing a subscription.
9. Used other available reference material to understand the food-scanning and nutrition-result screens.

**Note:** We personally tested the app only up to the subscription screen. The remaining food-scanning and nutrition screens were not tested directly. Information about those screens was collected from other reference sources.

## 4. Observed User Journey

The following steps explain the user journey of Cal AI. Each step shows whether we tested it ourselves or referred to other sources.

### Step 1: Welcome Screen

- The app shows a welcome screen.
- Users can select the Get Started option to begin.
- The app then starts asking questions about the user.

**Status:** Observed – Personally Tested

**Screenshot:**

[Welcome Screen](./evidence/01-Welcome-screen.jpg)

*Figure 1: Welcome screen of Cal AI.*

### Step 2: User Information Collection

During onboarding, the app asks users for details such as:

- Gender
- Weekly workout frequency
- Height
- Weight
- Date of birth (DOB)
- Previous use of calorie-tracking apps
- How the user found the application

**Status:** Observed – Personally Tested

**Screenshot:**

[ User Information ](./evidence/02-user-information.jpg)

*Figure 2: User information questions shown during onboarding.*

### Step 3: Fitness Goal Selection

- The app asks users about their fitness goals.
- Users can answer questions about what they want to achieve.
- A tap-and-hold action is also shown during the setup process.

**Status:** Observed – Personally Tested

**Screenshot:**

[Cal AI Fitness Goals](./evidence/03-Fitness-goal-selection.jpg)

*Figure 3: Fitness goal selection screen.*

### Step 4: Daily Nutrition Targets

- The app shows the progress of the onboarding process.
- After collecting user details, it displays daily nutrition targets.
- The information includes:
  - Daily calorie target
  - Protein target
  - Carbohydrate target
  - Fat target

**Status:** Observed – Personally Tested

**Screenshot:**

[Cal AI Nutrition Targets](./evidence/04-nutrition-targets.jpg)

*Figure 4: Daily calorie and nutrition targets.*

### Step 5: Account Creation

The app provides options to create an account.

The available options we observed were:

- Continue with Google
- Continue with Email

**Status:** Observed – Personally Tested

**Screenshot:**

[Cal AI Account Creation](./evidence/05-account-creation.jpg)

*Figure 5: Account creation options.*

### Step 6: Subscription Screen

- After the onboarding and account creation steps, the app shows a subscription screen.
- Users are shown subscription options.
- We did not purchase any subscription.

**Status:** Observed – Personally Tested

**Screenshot:**

[Cal AI Subscription Screen](./evidence/06-subscription-screen.jpg)

*Figure 6: Subscription screen where our direct testing stopped.*

### Step 7: Food Scanning and Nutrition Analysis

We could not directly test the food-scanning process because our investigation stopped at the subscription screen.

However, we found reference images of the following screens from other sources:

- Food scanning screen
- Food image upload or camera screen
- AI food analysis screen
- Food recognition result
- Nutrition information screen

**Status:** Not Tested – External Reference

**Screenshots:**

![Cal AI Food Scanning Screen](../../images/cal-ai-food-scanning.png)

*Figure 7: Food scanning screen from an external reference.*

![Cal AI Food Result Screen](../../images/cal-ai-food-result.png)

*Figure 8: Food recognition and nutrition result from an external reference.*

## 5. Information Shown to Users

The following table shows the features we observed and the features we could not test directly.

| Feature | Information / Function | Status |
|---|---|---|
| Welcome Screen | Get Started option | Observed |
| User Profile | Gender, height, weight, DOB | Observed |
| Activity Information | Weekly workout frequency | Observed |
| Previous App Usage | Previous calorie-app usage | Observed |
| Fitness Goals | Questions about fitness goals | Observed |
| Daily Nutrition | Calories, protein, carbohydrates, fats | Observed |
| Account Creation | Google and Email options | Observed |
| Subscription | Subscription screen | Observed |
| Food Scanning | Food image scanning screen | Not Tested – External Reference |
| Food Recognition | Food identification screen | Not Tested – External Reference |
| AI Analysis | Food image analysis screen | Not Tested – External Reference |
| Nutrition Results | Calories and nutrition details | Not Tested – External Reference |
| Food Editing | Changing detected food or quantity | Not Tested |

## 6. Food Scanning and Analysis – Features Not Tested

We could not test the following features directly in the Cal AI application.

Some screen images were found through other reference sources, but their actual working process could not be checked.

| Feature | What We Need to Check | Status |
|---|---|---|
| Food Image Input | Can users take a photo or upload an image? | Not Tested – External Reference |
| Food Recognition | Can the app identify food correctly? | Not Tested – External Reference |
| Mixed Meals | Can it identify different foods on one plate? | Not Tested |
| Unclear Images | How does it handle blurry or unclear food images? | Not Tested |
| Wrong Predictions | Can users correct the wrong food name? | Not Tested |
| Portion Size | Can users change the food quantity? | Not Tested |
| Nutrition Results | Does it show calories, protein, carbs, and fats? | Not Tested – External Reference |
| Food Tracking | Can users save scanned food in a daily food diary? | Not Tested |

These are questions for further investigation. They are not confirmed problems or limitations of Cal AI.

## 7. Product Observations and Improvement Ideas

The following points are based on our observations and ideas for improving our Indian Food Recognition & Nutrition App.

| No. | Observation / Opportunity | Improvement Idea |
|---|---|---|
| 1 | The app asks users for personal details during onboarding. | Keep the setup simple and ask only important questions. |
| 2 | The app asks about fitness goals and activity levels. | Provide clear options for different fitness goals. |
| 3 | The app shows daily calorie and nutrition targets. | Show calories, protein, carbohydrates, and fats clearly on the dashboard. |
| 4 | The onboarding process has multiple steps. | Make the setup process short and easy to complete. |
| 5 | Daily nutrition targets help users track their food intake. | Include nutrition details for common Indian meals. |
| 6 | Indian meals often contain multiple food items on one plate. | Recognize meals such as Roti, Dal, Rice, and Sabzi separately. |
| 7 | India has many regional food items. | Support foods such as Poha, Dosa, Idli, Samosa, and Paratha. |
| 8 | Food recognition may sometimes give incorrect results. | Allow users to check and correct detected food items. |
| 9 | Food quantity affects calorie and nutrition values. | Allow users to change the food quantity or serving size. |

**Note:** Points 1–5 are based on the onboarding screens we personally observed. Points 6–9 are our own ideas for improving our application. They are not confirmed problems with Cal AI.

## 8. Useful Features Identified

The following features can be useful while developing our application:

1. **Simple Welcome Screen:** A clear starting screen helps users begin easily.
2. **User Information:** Details such as height, weight, age, and activity level can help set nutrition targets.
3. **Fitness Goals:** Users should be able to select their fitness goals.
4. **Daily Nutrition Targets:** Showing calories, protein, carbohydrates, and fats helps users track their daily nutrition.
5. **Account Creation:** Google and Email options give users different ways to create an account.
6. **Food Scanning Screen:** External reference images can help us understand how a food-scanning screen may look. We did not test its working process.
7. **Nutrition Result Screen:** External reference images can help us plan how to display food and nutrition details. We did not test this feature directly.
   
## 9. Questions for Further Investigation

The following questions are still unanswered because we could not directly test the food-scanning process:

1. Can users scan food using the camera or upload an image from the gallery?
2. How accurately does the app recognize Indian food?
3. Can it identify different food items from one Indian Thali image?
4. What happens when a food image is blurry or unclear?
5. Can users correct a wrong food prediction?
6. How are calories, protein, carbohydrates, and fats calculated?
7. What happens if the app cannot recognize a food item?

These questions can be checked later if we get authorized access to these features.

## 10. Investigation Limitations

- We studied only the features available to us.
- We personally tested the onboarding process up to the subscription screen.
- We did not purchase a subscription.
- Food scanning and nutrition analysis were not tested directly.
- External screenshots and information were used to understand the remaining screens.
- We have kept personally tested features separate from externally collected references.
- No private data, restricted features, or app code was accessed.

## 11. Conclusion

This investigation helped us understand the basic user journey of Cal AI.

We personally observed the welcome screen, user information questions, fitness goal selection, daily nutrition targets, account creation, and subscription screen.

We also collected reference images of the food-scanning and nutrition-result screens from other sources. However, we did not test these features directly.

**Final Status:** Partially Completed – Onboarding personally tested up to the subscription screen. Remaining food-scanning and nutrition screens reviewed through external references but not tested directly.
