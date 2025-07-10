import pandas as pd
from tabulate import tabulate

# Data for table with verified sources
data = {
    "Parameter": [
        "Chemical Formula",
        "Role in Formulation",
        "Skin Safety",
        "Toxicity",
        "Environmental Safety",
        "Cost Range (India)",
        "pH (1% solution)",
        "Chelation Strength"
    ],
    "Citric Acid": [
        "C₆H₈O₇",
        "Chelator (binds Ca²⁺/Mg²⁺), pH adjuster",
        "GRAS; used in skincare",
        "Non-toxic at low conc.; mild irritation",
        "Biodegradable, low impact",
        "₹75–90/kg",
        "~2.2",
        "Moderate (3 COOH groups)"
    ],
    "MgSO₄·7H₂O": [
        "MgSO₄·7H₂O",
        "Ion stabilizer, pH balance, relaxant",
        "GRAS; safe for topical use",
        "Non-toxic; laxative if ingested",
        "Safe, water-soluble",
        "₹30–60/kg",
        "~6.5–7.0",
        "Weak (not a chelator)"
    ],
    "Source": [
        "<a href='https://pubchem.ncbi.nlm.nih.gov/compound/Citric-Acid'>"
        "PubChem</a>, <a href='https://en.wikipedia.org/wiki/Citric_acid'>"
        "Wikipedia</a>",
        "<a href='https://pubchem.ncbi.nlm.nih.gov/compound/Citric-Acid'>"
        "PubChem</a>, Martell & Smith (1974)",
        "<a href='https://www.fda.gov/food/food-ingredients-packaging/"
        "generally-recognized-safe-gras'>FDA</a>, CIR",
        "<a href='https://pubchem.ncbi.nlm.nih.gov/compound/Citric-Acid"
        "#section=Toxicity'>PubChem</a>, NIH",
        "<a href='https://echa.europa.eu/substance-information/-/"
        "substanceinfo/100.000.071'>ECHA</a>",
        "<a href='https://www.tradeindia.com'>TradeIndia</a>, GeM",
        "<a href='https://pubchem.ncbi.nlm.nih.gov/compound/Citric-Acid"
        "#section=pH'>PubChem</a>, Merck",
        "Martell & Smith (1974)"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Generate table
table = tabulate(df, headers="keys", tablefmt="grid", stralign="left",
                 numalign="center")

# Print table
print(table)

# Save to file
with open("citric_acid_magnesium_sulfate_table.txt", "w") as f:
    f.write(table)
