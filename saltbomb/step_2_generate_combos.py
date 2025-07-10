# step_2_generate_combos.py

import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (previously filtered or complete)
df = pd.read_csv("ingredients_repository_full.csv")

# Known literature combos (for flagging)
KNOWN_COMBOS = [
    "EDTA + Sodium Bicarbonate",
    "Sodium Carbonate + Tartaric Acid"
]

# Calculate a formulation score and relevant indicators


def calculate_score(ingredients):
    cost = sum(i['Cost_Rs_per_kg'] for i in ingredients)
    avg_pH = sum(i['pH'] for i in ingredients) / len(ingredients)
    softening = sum(i['Chelation_Strength'] * 20 for i in ingredients)
    safety = sum(i['SafetyScore'] for i in ingredients) / len(ingredients)
    eco = sum(i['EcoScore'] for i in ingredients) / len(ingredients)
    toxic = any(i['Toxic'] == 'Y' for i in ingredients)

    penalty = 0
    if avg_pH < 5 or avg_pH > 7:
        penalty += 20
    if toxic:
        penalty += 50

    score = (
        0.4 * softening + 0.3 * safety - 0.2 * cost +
        0.1 * eco - penalty
    )

    return {
        'TotalCost': round(cost, 2),
        'Avg_pH': round(avg_pH, 2),
        'Total_SofteningScore': softening,
        'Avg_SafetyScore': round(safety, 2),
        'Avg_EcoScore': round(eco, 2),
        'Toxicity_Flag': 'Y' if toxic else 'N',
        'FormulationScore': round(score, 2)
    }


# Store results
results = []

# Generate all 2- and 3-ingredient combos
for r in [2, 3]:
    for combo in itertools.combinations(df.to_dict('records'), r):
        names = [i['Ingredient'] for i in combo]
        name = " + ".join(names)
        metrics = calculate_score(combo)
        metrics['ComboName'] = name
        flag_combo = set(['Citric Acid', 'Magnesium Sulfate'])
        metrics['Contains_Citric_and_MgSO4'] = (
            'Y' if flag_combo.issubset(set(names)) else 'N'
        )
        metrics['Exists_in_Literature'] = (
            'Y' if name in KNOWN_COMBOS else 'N'
        )
        results.append(metrics)

# Convert to DataFrame and sort by score
ranked = pd.DataFrame(results).sort_values(
    by='FormulationScore', ascending=False
)

# Save results
ranked.to_csv("step_3_ranked_formulations.csv", index=False)
print("\u2705 Ranked combinations saved to step_3_ranked_formulations.csv")

# Barplot: Top 10 formulations
top10 = ranked.head(10)
plt.figure(figsize=(10, 6))
sns.barplot(
    y="ComboName", x="FormulationScore",
    data=top10, palette="viridis"
)
plt.title("Top 10 Water Softening Formulations")
plt.xlabel("Formulation Score")
plt.ylabel("Combination")
plt.tight_layout()
plt.savefig("formulation_top10_barplot.png")
print("\u2705 Graph saved: formulation_top10_barplot.png")

# Highlight your combo if in top 10
highlighted = top10[
    top10['Contains_Citric_and_MgSO4'] == 'Y'
]
if not highlighted.empty:
    print("\n\U0001F7E2 Your combo ranks in Top 10:")
    print(highlighted[['ComboName', 'FormulationScore']])

# --- Requirements ---
# To run this script, ensure the following libraries are installed:
# pip install pandas matplotlib seaborn
