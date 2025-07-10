import pandas as pd
import matplotlib.pyplot as plt
from math import pi

# Data with scores for radar chart
data = {
    "Parameter": [
        "pH",
        "Cost",
        "Skin Safety",
        "Toxicity",
        "Env. Safety",
        "Chelation"
    ],
    "Citric Acid": [2.2, 82.5, 5, 4, 5, 3],
    "MgSO4": [6.75, 45, 5, 4, 5, 1]
}
df = pd.DataFrame(data)

# Normalize data for radar chart
labels = df["Parameter"].tolist()
citric = df["Citric Acid"].tolist()
mgso4 = df["MgSO4"].tolist()

# Number of variables
n = len(labels)
if n == 0:
    raise ValueError("No parameters to plot")

# Angles for each axis
angles = [i / n * 2 * pi for i in range(n + 1)]

# Initialize radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot Citric Acid
citric += citric[:1]
ax.fill(angles, citric, color='red', alpha=0.25, label='Citric Acid')
ax.plot(angles, citric, color='red', linewidth=2)

# Plot MgSO4
mgso4 += mgso4[:1]
ax.fill(angles, mgso4, color='blue', alpha=0.25, label='MgSO4')
ax.plot(angles, mgso4, color='blue', linewidth=2)

# Add labels and title
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, size=10)
ax.set_title("Citric Acid vs MgSO4 Comparison", size=12, pad=20)

# Add legend
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Save as high-res PNG
plt.savefig("radar_comparison.png", dpi=300, bbox_inches='tight')
plt.close()
