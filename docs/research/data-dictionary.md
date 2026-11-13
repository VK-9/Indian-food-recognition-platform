# Data Dictionary - Indian Food Dataset

## 1. Purpose

This document explains the fields used in `data/food/foods.csv`. It defines the meaning, expected format, and purpose of each column to ensure the dataset remains consistent and understandable.

## 2. Dataset File

- **File:** `data/food/foods.csv`
- **Format:** CSV (Comma-Separated Values)
- **Measurement basis:** Nutrition values are recorded per 100 grams wherever reliable source data is available.
- **Missing values:** Fields may remain empty when verified information is unavailable. Missing values must not be replaced with invented data.

## 3. Field Definitions

| No. | Field Name | Description |
|---|---|---|
| 1 | `food_id` | Unique identifier assigned to each food record, such as F001 or F050. |
| 2 | `food_name` | Main or standard name of the food or dish. |
| 3 | `regional_names` | Alternate, regional, or commonly used names of the food, where available. |
| 4 | `food_category` | Category used to group the food, such as snack, bread, rice dish, or lentil dish. |
| 5 | `common_ingredients` | Main ingredients commonly used to prepare the food. |
| 6 | `preparation_notes` | Important preparation details, recipe variations, or differences that may affect identification or nutrition. |
| 7 | `serving_size` | Serving quantity recorded for the food, where available. |
| 8 | `serving_unit` | Unit used for the serving size, such as grams (g). |
| 9 | `nutrition_source` | Name of the source used to obtain or estimate the nutrition information. |
| 10 | `nutrition_source_url` | Direct web reference or URL for the nutrition source, where available. |
| 11 | `energy_kcal_per_100g` | Energy value in kilocalories (kcal) per 100 grams. |
| 12 | `energy_kj_per_100g` | Energy value in kilojoules (kJ) per 100 grams. |
| 13 | `carbohydrates_g_per_100g` | Carbohydrate content in grams per 100 grams. |
| 14 | `protein_g_per_100g` | Protein content in grams per 100 grams. |
| 15 | `fat_g_per_100g` | Fat content in grams per 100 grams. |
| 16 | `fibre_g_per_100g` | Dietary fibre content in grams per 100 grams. |
| 17 | `confidence_or_notes` | Confidence information, source limitations, assumptions, unusual values, or other relevant data-quality notes. |

## 4. Data Consistency Rules

1. Each food record must have a unique `food_id`.
2. Field names and column order must remain consistent across the CSV file.
3. Nutrition values must be linked to their sources wherever available.
4. Nutrition values must be identified as per 100 grams and must not be confused with serving-based values.
5. Raw, cooked, and prepared-food values must not be mixed without an explanation.
6. Recipe variations and close food matches must be documented in the relevant notes.
7. Unknown or unverified nutrition values must remain blank rather than being fabricated.
8. Any unusual values, conversions, or source limitations must be mentioned in `confidence_or_notes`.

## 5. Relationship with Research Documentation

This data dictionary should be read together with:

- `data/food/foods.csv` - Structured Indian food records.
- `docs/research/food-dataset-notes.md` - Food-specific research notes, sources, and limitations.
- `docs/research/nutrition-sources.md` - Nutrition references, serving assumptions, and source methodology.

## 6. Conclusion

The data dictionary provides a common understanding of all 17 fields in the Indian food dataset. It helps maintain consistent records, supports future integration with the food-recognition prototype, and makes the dataset easier to review and maintain.
