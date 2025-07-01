import pandas as pd

# Load fixed phenotype file
df = pd.read_csv("phenotype_data_fixed.txt", sep="\t")

# Recode: 0 ➝ 1 (control), 1 ➝ 2 (case)
df["Cardiovascular_Risk"] = df["Cardiovascular_Risk"].replace({0: 1, 1: 2})

# Save new PLINK-ready phenotype file
df.to_csv("phenotype_data_plink.txt", sep="\t", index=False)
print("✅ Saved recoded phenotype file as: phenotype_data_plink.txt")
