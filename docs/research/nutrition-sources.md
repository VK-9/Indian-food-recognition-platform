# Nutrition Sources and Serving Assumptions

## 1. Purpose

This document records the nutrition sources reviewed for the Indian Food Recognition Platform. It explains how nutrition values should be selected, how serving sizes should be interpreted, and the limitations of estimating nutrition from food images.

The objective is to keep nutrition information traceable and avoid presenting uncertain estimates as exact values.

## 2. Nutrition Data Sources

### 2.1 ICMR–National Institute of Nutrition (NIN)

**Source:** Indian Food Composition Tables (IFCT), 2017  
**URL:** https://www.nin.res.in/ebooks/IFCT2017.pdf

- IFCT 2017 provides nutrient-composition information for commonly consumed Indian food items.
- It is a primary reference for the nutritional composition of raw food ingredients.
- It can be used to identify nutrient values for ingredients such as cereals, pulses, vegetables and other food components.
- Ingredient values should not automatically be treated as the nutrition values of a fully prepared dish.

### 2.2 Indian Nutrient Databank (INDB) – Anuvaad

**Source:** Indian Nutrient Databank  
**URL:** https://www.anuvaad.org.in/indian-nutrient-databank/

INDB provides nutritional information for common Indian recipes, including values per 100 g and per serving.

Its methodology explains that the database uses food-composition references such as IFCT 2017, IFCT 2004, UK food-composition data and USDA data. It also includes recipes collected from cookbooks and other sources.

**Methodology:** https://www.anuvaad.org.in/methodology/

This is a useful source for prepared Indian dishes because it includes recipe-level information rather than only individual raw ingredients.

### 2.3 ICMR–NIN Dietary Guidelines

**Source:** Dietary Guidelines for Indians, 2024  
**URL:** https://www.nin.res.in/dietaryguidelines/pdfjs/locale/DGI24thJune2024fin.pdf

These guidelines provide general dietary and food-group guidance. They may help provide context for food portions, but they should not be treated as the source of exact nutrition values for an individual prepared dish.

## 3. Raw Ingredients vs Cooked Foods vs Prepared Dishes

Nutrition values depend on the state and preparation of the food.

| Food data type | Meaning | Example |
|---|---|---|
| Raw ingredient | Nutrient values before cooking | Raw rice, raw lentils |
| Cooked ingredient | Nutrient values after cooking | Cooked rice, boiled lentils |
| Prepared dish | A complete recipe containing multiple ingredients | Dal tadka, chole, vegetable pulao |

**Important rules:**

1. Raw ingredient values must not be directly presented as cooked-dish values.
2. Cooking can change food weight because of water absorption or loss.
3. Oil, ghee, salt, spices and other ingredients can change the nutritional composition of a recipe.
4. A prepared-dish value should be used only when the source describes a sufficiently matching recipe.
5. If the preparation basis is unclear, the uncertainty must be documented.

## 4. Serving Size and Unit Assumptions

For consistency, nutrition values may be stored per 100 g when the source provides that basis.

- `100 g` is a reference quantity for comparing nutrition values.
- It does not necessarily represent one actual serving.
- Serving size should be recorded separately when a reliable source provides it.
- Units must be clearly mentioned, such as grams (g) or millilitres (ml).
- Volume and weight should not be treated as interchangeable without a supported conversion.

For a source that provides nutrition per 100 g, the approximate nutrient amount for a known food weight can be calculated as:

**Nutrient amount = (Nutrient value per 100 g × Food weight in g) / 100**

This calculation is valid only when the food and preparation basis match the source record.

## 5. Initial Dataset Source Mapping

The initial dataset contains the following food entries:

| Food ID | Food name | Nutrition source / status |
|---|---|---|
| F001 | Poha | Anuvaad INDB |
| F002 | Idli | Anuvaad INDB |
| F003 | Roti / Chapati | Anuvaad INDB |
| F004 | Moong Dal | Anuvaad INDB |
| F005 | Rajma Curry | Anuvaad INDB |
| F006 | Dal Tadka | Nutrition source not yet verified; values left blank |
| F007 | Chole | Anuvaad recipe record; preparation basis should be checked |
| F008 | Aloo Paratha | Anuvaad recipe record; preparation basis should be checked |
| F009 | Mixed Vegetable Pulao | Anuvaad recipe record; preparation basis should be checked |
| F010 | Plain Dosa | Anuvaad recipe record; preparation basis should be checked |

The corresponding source URLs are recorded in `data/food/foods.csv` and `docs/research/food-dataset-notes.md`.

Nutrition values should remain blank when a reliable matching source has not been confirmed. Existing values should not be changed without checking the source record and its preparation basis.

## 6. Foods with High Recipe Variation

Some Indian dishes have substantial differences between household and regional recipes.

Examples include:

- **Dal Tadka:** Different lentils, quantities of oil or ghee, and tempering ingredients may be used.
- **Chole:** Chickpea quantity, gravy thickness and oil content can vary.
- **Aloo Paratha:** Stuffing quantity and cooking fat can vary.
- **Mixed Vegetable Pulao:** Rice-to-vegetable ratio and oil quantity can differ.
- **Poha:** Added peanuts, potatoes and oil can change its nutritional composition.
- **Rajma Curry:** Bean quantity and gravy ingredients can vary.

A single generic nutrition value may not represent every version of these dishes. The selected source recipe and its limitations should therefore be documented.

## 7. Limitations of Image-Based Portion Estimation

A food image can help identify a dish, but it cannot reliably reveal its complete nutritional composition.

Important limitations include:

1. **Portion size:** A photograph does not always provide the actual weight of the food.
2. **Depth and scale:** Camera angle and the absence of a known reference object make size estimation difficult.
3. **Hidden ingredients:** Oil, ghee, sugar, salt and other ingredients may not be visible.
4. **Recipe variation:** Similar-looking dishes may have different ingredients and preparation methods.
5. **Mixed dishes:** Rice dishes, curries and other mixed foods may contain ingredients in different proportions.
6. **Cooking method:** Fried, roasted, steamed and boiled versions may look similar but have different nutritional compositions.

Therefore, image-based nutrition output should be treated as an estimate rather than an exact measurement.

## 8. Recommendations for Nutrition Display

The platform should follow these recommendations:

- Display the identified food name and the estimated portion separately.
- Show the nutrition reference basis, such as per 100 g or per serving.
- Display calories, carbohydrates, protein, fat and fibre only when supported by a source.
- Mention the nutrition source wherever possible.
- Clearly label image-based portion and nutrition results as estimates.
- Show a confidence indication for food identification separately from nutrition accuracy.
- Avoid displaying exact-looking values when the recipe or portion size is uncertain.
- Keep unknown nutrition values blank instead of inventing values.

## 9. Data Quality and Verification Rules

1. Every nutrition value must have a traceable source.
2. The source URL should be stored in the dataset.
3. Raw, cooked and prepared-dish values must be distinguished.
4. The reference quantity and serving size must not be confused.
5. Recipe variations and uncertainty should be recorded in the notes.
6. Unverified values must remain blank until a suitable source is found.

## 10. Conclusion

ICMR–NIN IFCT 2017 is an important reference for Indian food ingredients, while the Anuvaad Indian Nutrient Databank provides useful nutrition information for prepared Indian recipes.

For this project, nutrition values should be source-based, clearly labelled and separated from image-based portion estimates. This approach will make the platform's nutrition output more transparent and reliable.

## References

1. ICMR–National Institute of Nutrition. *Indian Food Composition Tables 2017.*  
   https://www.nin.res.in/ebooks/IFCT2017.pdf

2. Anuvaad. *Indian Nutrient Databank.*  
   https://www.anuvaad.org.in/indian-nutrient-databank/

3. Anuvaad. *Research Methodology.*  
   https://www.anuvaad.org.in/methodology/

4. ICMR–National Institute of Nutrition. *Dietary Guidelines for Indians, 2024.*  
   https://www.nin.res.in/dietaryguidelines/pdfjs/locale/DGI24thJune2024fin.pdf
