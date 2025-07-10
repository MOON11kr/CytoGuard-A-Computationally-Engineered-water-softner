import pandas as pd
import matplotlib.pyplot as plt

# Your top 5 combos from the dataset
data = {
    'ComboName': [
        'Citric Acid + Magnesium Sulfate',
        'EDTA + Sodium Bicarbonate',
        'Sodium Carbonate + Tartaric Acid',
        'Citric + MgSO₄ + Na Bicarbonate',
        'Citric + MgSO₄ + Hexametaphosphate'
    ],
    'FormulationScore': [39.65, 37.90, 36.50, 38.03, 39.65]
}

df = pd.DataFrame(data)

# Bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(
    df['ComboName'],
    df['FormulationScore'],
    color='mediumseagreen'
)
plt.xlabel("Formulation Score")
plt.title("Top 5 Water Softening Formulations (Based on the Data)")

for bar, label in zip(bars, df['ComboName']):
    if label.startswith("Citric Acid + Magnesium Sulfate"):
        bar.set_color('darkorange')

plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top5_formulation_scores.png", dpi=300)
plt.show()
