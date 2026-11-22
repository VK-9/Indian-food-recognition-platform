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

### 2.4 Additional Nutrition Sources

The dataset also uses additional nutrition sources for selected food records where a suitable matching entry was available.

| Source | Food IDs | Usage and limitations |
|---|---|---|
| Healthify Nutrifacts | F033, F038, F042 | Per-100-g and per-serving nutrition information for selected foods and beverages. |
| RealCalorieTracker | F020, F022 | INDB-based recipe entries and close matching prepared dishes. |
| SVAS | F027 | Ingredient-based nutrition estimates informed by IFCT-2017. |
| Khaana | F029 | Recipe-based nutrition estimates for a 580 g serving of Litti Chokha. |
| IIIT Delhi RecipeDB | F036 | Recipe-level nutrition information; serving size was not specified. |
| Barbeque Nation | F032 | Branded restaurant nutrition information; per-100 g values only. |
| TUMUL / Nandini | F049 | Branded product nutrition information; nutrition basis requires clarification. |
| NutriLifeCalc | F006 | Secondary nutrition information for Dal Tadka; per-serving values were unavailable. |

**Important:** These sources differ in methodology and reliability. Recipe-based estimates, branded product values and database entries should be identified according to their actual source type. A close recipe match should not be described as an exact match.

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

## 4. Reference Quantity and Serving Assumptions

For consistency, nutrition values are stored on a per-100-g basis when the source provides that reference.

- `reference_quantity` represents the quantity used as the basis for the nutrition values (100 in the current dataset).
- `reference_unit` represents the unit of that reference quantity (g in the current dataset).
- The reference quantity does not necessarily represent one actual serving.
- `serving_description` records a human-readable portion description, such as 1 bowl, 1 piece or 1 serving.
- A serving description does not guarantee a standardized serving weight.
- Serving weight should only be recorded when a reliable source provides it.
- Volume and weight should not be treated as interchangeable without a supported conversion.

### 4.1 Per-Serving Nutrition Values

The CSV has six per-serving fields, which correspond to the same six nutrient types recorded per 100 g:

- `energy_kcal_per_serving` — Energy (kcal)
- `energy_kj_per_serving` — Energy (kJ)
- `carbohydrates_g_per_serving` — Carbohydrates (g)
- `protein_g_per_serving` — Protein (g)
- `fat_g_per_serving` — Fat (g)
- `fibre_g_per_serving` — Fibre (g)

Per-serving values are transcribed only when the selected source provides the relevant serving-level information. Secondary sources and recipe-based estimates are identified separately from Anuvaad INDB values. The serving description is a text label and does not, by itself, establish a serving weight in grams.

If a source provides only per-100-g values, the serving size is unclear, or the source does not provide a particular nutrient for the serving, the unsupported per-serving field or fields remain blank. Values are not calculated from an assumed serving weight, and missing nutrients are not inferred from the other nutrient fields. This rule applies independently to all six per-serving fields.

### 4.2 Calculation from a Known Food Weight

For a source that provides nutrition per 100 g, the approximate nutrient amount for a known food weight can be calculated as:

**Nutrient amount = (Nutrient value per 100 g × Food weight in g) / 100**

This calculation is valid only when the food and preparation basis match the source record and the actual food weight is known.

## 5. Dataset Source Mapping (F001–F050)

The table below is aligned to the current `foods.csv` records. Source labels and URLs are reproduced from the CSV so that each food ID can be traced consistently. A blank source URL means that no verified source was recorded for that combined dish; it is not an invitation to infer or substitute a source.

| Food ID | Food Name | `nutrition_source` (CSV label) | `nutrition_source_url` |
|---|---|---|---|
| F001 | Poha | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/poha/ |
| F002 | Idli | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/idli/ |
| F003 | Roti/Chapati | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/chapati-roti/ |
| F004 | Moong Dal | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/dal-moong/ |
| F005 | Rajma Curry | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/kidney-bean-curry-rajmah-curry/ |
| F006 | Dal Tadka | NutriLifeCalc | https://www.nutrilifecalc.com/foods/dal-tadka |
| F007 | Chole | Anuvaad INDB | https://www.anuvaad.org.in/nutrition-fact/chickpeas-curry-safed-channa-curry/ |
| F008 | Aloo Paratha | Anuvaad INDB | https://www.anuvaad.org.in/nutrition-fact/potato-parantha-paratha-aloo-ka-parantha-paratha/ |
| F009 | Mixed Vegetable Pulao | Anuvaad INDB | https://www.anuvaad.org.in/nutrition-fact/mixed-vegetable-pulao/ |
| F010 | Plain Dosa | Anuvaad INDB | https://www.anuvaad.org.in/nutrition-fact/plain-dosa/ |
| F011 | Samosa | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/potato-samosa-aloo-ka-samosa/ |
| F012 | Vegetable Pakora | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/mixed-vegetable-pakora-pakoda/ |
| F013 | Upma | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/semolina-upma-suji-rava-upma/ |
| F014 | Khichdi | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/rice-dal-porridge-chawal-dal-ki-khichdi-khichri/ |
| F015 | Lemon Rice | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/lemon-rice-pulihora-elumichai-sadam-chitranna/ |
| F016 | Jeera Rice | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/cumin-pulao-jeera-zeera-pulao/ |
| F017 | Puri | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/poori/ |
| F018 | Bhatura | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/bhatura/ |
| F019 | Palak Paneer | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/spinach-paneer-palak-paneer/ |
| F020 | Paneer Butter Masala | Real Calorie Tracker (INDB-matched standard recipe) | https://realcalorietracker.com/foods/paneer-in-butter-sauce |
| F021 | Masala Dosa | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/masala-dosa/ |
| F022 | Uttapam | Real Calorie Tracker (INDB-matched standard recipe) | https://realcalorietracker.com/foods/uttapam |
| F023 | Medu Vada | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/plain-urad-dal-vada-uzunne-vada-minapa-garelu-ulundu-vadai-medu-vada/ |
| F024 | Dhokla | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/khaman-dhokla/ |
| F025 | Kachori | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/khasta-kachori/ |
| F026 | Pav Bhaji | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/pav-bhaji/ |
| F027 | Misal Pav | Svas (IFCT-2017 ingredient-based calculation) | https://www.svas.life/nutrition/misal-pav/ |
| F028 | Thepla | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/methi-thepla/ |
| F029 | Litti Chokha | Khaana (recipe-based nutrition estimate) | https://khaana.com/recipes/litti-chokha.html |
| F030 | Baingan Bharta | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/brinjal-bhartha-baingan-ka-bhartha/ |
| F031 | Vegetable Biryani | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/vegetable-biryani-biriyani/ |
| F032 | Chicken Biryani | Barbeque Nation nutrition information | https://bn.barbequenation.com/sites/default/files/2024-12/BNHL%20NV%20New%20%281%29.pdf |
| F033 | Masala Chai | Healthify Nutrifacts | https://www.healthifyme.com/web/nutrifacts/masala-chai-0cdff33d93 |
| F034 | Curd Rice | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/curd-rice-dahi-bhaat-dahi-chawal-perugu-annam-daddojanam-thayir-saadam/ |
| F035 | Vegetable Sandwich | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/vegetable-and-mayonnaise-sandwich/ |
| F036 | Paneer Tikka | IIIT Delhi RecipeDB | https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/67098 |
| F037 | Gulab Jamun | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/gulab-jamun-with-khoya/ |
| F038 | Jalebi | Healthify Nutrifacts | https://www.healthifyme.com/web/nutrifacts/jalebi-fe489fd719 |
| F039 | Kheer | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/rice-kheer-chawal-ki-kheer/ |
| F040 | Poha Jalebi | Not identified / blank in CSV | Not available |
| F041 | Dal Baati Churma | Not identified / blank in CSV | Not available |
| F042 | Vada Pav | Healthify Nutrifacts | https://www.healthifyme.com/web/nutrifacts/vada-pav-284e957a95 |
| F043 | Rava Dosa | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/semolina-dosa-suji-rava-dosa/ |
| F044 | Appam | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/appam/ |
| F045 | Sambar | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/sambar/ |
| F046 | Rasam | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/rasam-with-tamarind-puli-rasam-chintapandu-rasam-charu-saaru/ |
| F047 | Aloo Gobi | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/potato-cauliflower-aloo-gobhi/ |
| F048 | Chana Dal | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/split-bengal-gram-dal-channa-dal/ |
| F049 | Mysore Pak | TUMUL (Nandini) | https://www.tumul.coop/mysore-pak |
| F050 | Shrikhand | Anuvaad Indian Nutrient Databank (INDB) | https://www.anuvaad.org.in/nutrition-fact/sweetened-yogurt-shrikhand/ |

**Source consistency notes:**
- Anuvaad appears under two CSV labels: `Anuvaad Indian Nutrient Databank (INDB)` and `Anuvaad INDB`. Both refer to the same named source family; the CSV labels have deliberately not been changed.
- F020 and F022 use `Real Calorie Tracker (INDB-matched standard recipe)`; this is a secondary, recipe-matched source, not a direct Anuvaad record URL.
- F027, F029, F032, F033, F036, F038, F042 and F049 use secondary sources listed in Section 2.4 and in References.
- F040 and F041 have no source label or URL in the CSV because no verified source for the exact combined dish was identified. Their nutrition values remain unavailable.
- The CSV remains the data file of record. This document records source provenance and methodology; it does not create or estimate missing nutrition values.

## 6. Foods with High Recipe Variation

Indian dishes can vary significantly across regions, households, ingredients and preparation methods. These differences can affect their nutritional composition.

Examples from this dataset include:

- **Dal Tadka and Chana Dal:** Lentil type, water content, oil or ghee quantity and tempering ingredients can vary.
- **Poha:** Peanuts, potatoes, onions and oil quantities may differ.
- **Idli and Dosa varieties:** Batter composition, fermentation and preparation methods can affect nutritional values.
- **Parathas and Thepla:** Stuffing, flour composition and cooking fat can vary.
- **Puri, Bhatura, Samosa and Kachori:** Dough composition, filling and frying oil absorption can affect energy and fat values.
- **Chole and Rajma Curry:** Legume quantity, gravy thickness and oil content can differ.
- **Paneer Butter Masala and Palak Paneer:** Paneer quantity, cream, butter and gravy ingredients may vary.
- **Biryani varieties:** Rice-to-ingredient ratio, cooking fat and preparation style can differ.
- **Regional dishes such as Misal Pav and Litti Chokha:** Regional recipes and serving combinations may vary.
- **Sweets such as Gulab Jamun, Jalebi, Kheer, Mysore Pak and Shrikhand:** Ingredients, sugar content and preparation methods can differ.

A single generic nutrition value may not represent every version of these dishes. The selected source recipe, food variant and preparation basis should therefore be documented. Where a close match or recipe-based estimate is used, it should not be presented as an exact standardized value.

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
7. Per-serving nutrition values must be recorded only when supported by a reliable source with a clearly documented serving basis.
8. All six per-serving nutrient fields (energy in kcal, energy in kJ, carbohydrates, protein, fat and fibre) should be populated wherever reliable source values are available.
9. If per-serving information is unavailable, inconsistent or ambiguous, the corresponding fields must remain blank and the reason should be documented.

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
   
5. NutriLifeCalc – Dal Tadka
   https://www.nutrilifecalc.com/foods/dal-tadka

6. Healthify. Nutrifacts database. Used for selected food records, including Masala Chai, Jalebi and Vada Pav.
   https://www.healthifyme.com/web/nutrifacts/vada-pav-284e957a95
   Masala Chai: https://www.healthifyme.com/web/nutrifacts/masala-chai-0cdff33d93
   Jalebi: https://www.healthifyme.com/web/nutrifacts/jalebi-fe489fd719

7. RealCalorieTracker. Nutrition information for Paneer in Butter Sauce and Uttapam.
   https://realcalorietracker.com/foods/paneer-in-butter-sauce
   https://realcalorietracker.com/foods/uttapam

8. SVAS. Misal Pav nutrition information.
   https://www.svas.life/nutrition/misal-pav/

9. Khaana. Litti Chokha recipe.
   https://khaana.com/recipes/litti-chokha.html

10. IIIT Delhi. RecipeDB. Paneer Tikka recipe information.
    https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/67098

11. Barbeque Nation – Official Chicken Biryani Nutrition Information
    https://bn.barbequenation.com/sites/default/files/2024-12/BNHL%20NV%20New%20%281%29.pdf
    
12. TUMUL (Nandini) – Mysore Pak
    https://www.tumul.coop/mysore-pak
