import pandas as pd

# ✅ Step 1: Define the ingredient data
ingredients = [
    {
        "Ingredient": "Citric Acid",
        "Type": "Chelator",
        "Cost_Rs_per_kg": 80,
        "BulkPrice_USD_per_ton": 1000,
        "pH": 2.2,
        "pKa_values": "[3.13, 4.76, 6.39]",
        "Chelation_Strength": 4,
        "Toxic": "N",
        "Availability": "Very High",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 9,
        "SupplierCountry": "Global",
        "SourceLink": "https://pubchem.ncbi.nlm.nih.gov/compound/Citric-acid"
    },
    {
        "Ingredient": "Magnesium Sulfate",
        "Type": "Ion Source",
        "Cost_Rs_per_kg": 60,
        "BulkPrice_USD_per_ton": 430,
        "pH": 7.0,
        "pKa_values": "",
        "Chelation_Strength": 1,
        "Toxic": "N",
        "Availability": "Very High",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 8,
        "SupplierCountry": "India",
        "SourceLink": "https://mkp.gem.gov.in"
    },
    {
        "Ingredient": "EDTA",
        "Type": "Chelator",
        "Cost_Rs_per_kg": 400,
        "BulkPrice_USD_per_ton": 2500,
        "pH": 4.3,
        "pKa_values": "[0, 1.5, 2, 6, 10.3]",
        "Chelation_Strength": 5,
        "Toxic": "Y",
        "Availability": "Medium",
        "SkinSafe": "N",
        "EcoFriendly": "N",
        "EcoScore": 2,
        "SupplierCountry": "Global",
        "SourceLink": "https://pubchem.ncbi.nlm.nih.gov/compound/EDTA"
    },
    {
        "Ingredient": "Sodium Carbonate",
        "Type": "Base",
        "Cost_Rs_per_kg": 30,
        "BulkPrice_USD_per_ton": 200,
        "pH": 11.6,
        "pKa_values": "[10.3]",
        "Chelation_Strength": 1,
        "Toxic": "N",
        "Availability": "Very High",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 7,
        "SupplierCountry": "India",
        "SourceLink": (
            "https://pubchem.ncbi.nlm.nih.gov/compound/"
            "Sodium-carbonate"
        )
    },
    {
        "Ingredient": "Sodium Bicarbonate",
        "Type": "Buffer/Base",
        "Cost_Rs_per_kg": 25,
        "BulkPrice_USD_per_ton": 180,
        "pH": 8.3,
        "pKa_values": "[6.3]",
        "Chelation_Strength": 1,
        "Toxic": "N",
        "Availability": "Very High",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 8,
        "SupplierCountry": "Global",
        "SourceLink": (
            "https://pubchem.ncbi.nlm.nih.gov/compound/"
            "Sodium-bicarbonate"
        )
    },
    {
        "Ingredient": "Sodium Hexametaphosphate",
        "Type": "Chelator",
        "Cost_Rs_per_kg": 100,
        "BulkPrice_USD_per_ton": 900,
        "pH": 7.0,
        "pKa_values": "",
        "Chelation_Strength": 3,
        "Toxic": "N",
        "Availability": "High",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 7,
        "SupplierCountry": "Global",
        "SourceLink": "https://en.wikipedia.org/wiki/Sodium_hexametaphosphate"
    },
    {
        "Ingredient": "Phytic Acid",
        "Type": "Chelator",
        "Cost_Rs_per_kg": 150,
        "BulkPrice_USD_per_ton": 1200,
        "pH": 1.9,
        "pKa_values": "[1.9, 2.5, 3.0, 5.5, 6.6, 7.4]",
        "Chelation_Strength": 4,
        "Toxic": "N",
        "Availability": "Medium",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 8,
        "SupplierCountry": "Global",
        "SourceLink": "https://pubchem.ncbi.nlm.nih.gov/compound/Phytic-acid"
    },
    {
        "Ingredient": "Tartaric Acid",
        "Type": "Chelator",
        "Cost_Rs_per_kg": 120,
        "BulkPrice_USD_per_ton": 950,
        "pH": 3.0,
        "pKa_values": "[2.98, 4.34]",
        "Chelation_Strength": 3,
        "Toxic": "N",
        "Availability": "Medium",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 7,
        "SupplierCountry": "India",
        "SourceLink": "https://pubchem.ncbi.nlm.nih.gov/compound/Tartaric-acid"
    },
    {
        "Ingredient": "Gluconic Acid",
        "Type": "Chelator",
        "Cost_Rs_per_kg": 140,
        "BulkPrice_USD_per_ton": 1050,
        "pH": 3.5,
        "pKa_values": "[3.6]",
        "Chelation_Strength": 3,
        "Toxic": "N",
        "Availability": "Medium",
        "SkinSafe": "Y",
        "EcoFriendly": "Y",
        "EcoScore": 7,
        "SupplierCountry": "Global",
        "SourceLink": "https://pubchem.ncbi.nlm.nih.gov/compound/Gluconic-acid"
    }
]

# ✅ Step 2: Create the DataFrame
df = pd.DataFrame(ingredients)

# ✅ Step 3: Compute derived scores
df["SofteningScore"] = df["Chelation_Strength"] * 20
df["SafetyScore"] = df.apply(
    lambda r: (
        (1 if r["Toxic"] == "N" else 0) * 50
        + max(0, (7 - abs(r["pH"] - 6.5))) * 5
    ),
    axis=1
)
df["Cost_performance"] = df["SofteningScore"] / df["Cost_Rs_per_kg"]
df["BlendCompatibility"] = ""

# ✅ Step 4: Export to CSV
df.to_csv("ingredients_repository_full.csv", index=False)
print(
    "✅ File created: ingredients_repository_full.csv with",
    len(df),
    "ingredients."
)
