# step_3_generate_combos.py

import pandas as pd
import itertools

# Load full ingredient dataset (previously filtered if needed)
df = pd.read_csv("ingredients_repository_full.csv")

# Define known literature combos (we'll mark these as 'Exists')
KNOWN_COMBOS = [
    "EDTA + Sodium Bicarbonate",
    "Sodium Carbonate + Tartaric Acid"
]


# Function to calculate formulation score
def calculate_score(ingredients):
    total_cost = sum(i['Cost_Rs_per_kg'] for i in ingredients)
    avg_pH = sum(i['pH'] for i in ingredients) / len(ingredients)
    total_softening = sum(i['Chelation_Strength'] * 20 for i in ingredients)
    avg_safety = sum(i['SafetyScore'] for i in ingredients) / len(ingredients)
    avg_eco = sum(i['EcoScore'] for i in ingredients) / len(ingredients)
    is_toxic = any(i['Toxic'] == 'Y' for i in ingredients)

    penalty = 0
    if avg_pH < 5 or avg_pH > 7:
        penalty += 20
    if is_toxic:
        penalty += 50

    final_score = (
        0.4 * total_softening
        + 0.3 * avg_safety
        - 0.2 * total_cost
        + 0.1 * avg_eco
        - penalty
    )

    return {
        'TotalCost': total_cost,
        'Avg_pH': round(avg_pH, 2),
        'Total_SofteningScore': total_softening,
        'Avg_SafetyScore': round(avg_safety, 2),
        'Avg_EcoScore': round(avg_eco, 2),
        'Toxicity_Flag': 'Y' if is_toxic else 'N',
        'FormulationScore': round(final_score, 2)
    }


# Store results
results = []

# Generate 2- and 3-ingredient combinations
for r in [2, 3]:
    for combo in itertools.combinations(df.to_dict('records'), r):
        names = [i['Ingredient'] for i in combo]
        combo_name = " + ".join(names)
        metrics = calculate_score(combo)
        metrics['ComboName'] = combo_name
        metrics['Contains_Citric_and_MgSO4'] = (
            'Y'
            if set(['Citric Acid', 'Magnesium Sulfate']).issubset(
                set(names)
            )
            else 'N'
        )
        metrics['Exists_in_Literature'] = (
            'Y' if combo_name in KNOWN_COMBOS else 'N'
        )
        results.append(metrics)

# Save to CSV
pd.DataFrame(results) \
    .sort_values(by='FormulationScore', ascending=False) \
    .to_csv("step_3_ranked_formulations.csv", index=False)

print(
    "Combinations generated and ranked. Output saved to "
    "step_3_ranked_formulations.csv"
)
