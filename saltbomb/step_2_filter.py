import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("ingredients_repository_full.csv")

# Step 2: Apply filtering criteria
filtered = df[
    (df["Toxic"] == "N") &
    (df["SkinSafe"] == "Y") &
    (df["EcoFriendly"] == "Y") &
    (df["Cost_Rs_per_kg"] <= 100) &
    (df["Chelation_Strength"] >= 3) &
    (df["Availability"].isin(["High", "Very High"])) &
    (df["pH"].between(5, 7))
]

# Step 3: Sort by highest SofteningScore, then Cost_performance
filtered = filtered.sort_values(
    by=["SofteningScore", "Cost_performance"],
    ascending=[False, False]
)

# Step 4: Save filtered results
filtered.to_csv("filtered_ingredients.csv", index=False)
print(
    f"Filtered ingredients saved to filtered_ingredients.csv "
    f"({len(filtered)} results)"
)
