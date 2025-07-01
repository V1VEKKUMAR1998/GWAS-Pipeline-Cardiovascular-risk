import pandas as pd

# Load .fam file to get sample IDs used by PLINK
fam = pd.read_csv("output_data.fam", delim_whitespace=True, header=None)
fam.columns = ["FID", "IID", "PID", "MID", "Sex", "Phenotype"]
fam_ids = fam[["FID", "IID"]]

# Load your existing phenotype file
phenotype = pd.read_csv("phenotype_data.txt", sep="\t")

# Merge phenotype with fam to keep only matching IDs
merged = fam_ids.merge(phenotype, on=["FID", "IID"], how="left")

# Report summary
matched = merged["Cardiovascular_Risk"].notnull().sum()
missing = merged["Cardiovascular_Risk"].isnull().sum()
print(f"✅ Matched phenotypes: {matched}")
print(f"❌ Missing phenotypes: {missing}")

# Fill missing phenotypes with -9 (PLINK's missing code)
merged["Cardiovascular_Risk"] = merged["Cardiovascular_Risk"].fillna(-9)

# Save cleaned phenotype file
merged[["FID", "IID", "Cardiovascular_Risk"]].to_csv("phenotype_data_fixed.txt", sep="\t", index=False)
print("📄 Cleaned phenotype file saved as: phenotype_data_fixed.txt")
