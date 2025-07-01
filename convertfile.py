import pandas as pd

# Load genotype data (updated filename)
geno = pd.read_csv("Genotype_data.csv")
samples = geno["SampleID"]
snp_cols = geno.columns[1:]

# Create .ped file
ped_rows = []
for i, row in geno.iterrows():
    fid = row["SampleID"]
    iid = row["SampleID"]
    pid = "0"
    mid = "0"
    sex = "1"
    pheno = "-9"
    
    snp_data = []
    for val in row[snp_cols]:
        if val == 0:
            snp_data += ["A", "A"]
        elif val == 1:
            snp_data += ["A", "G"]
        elif val == 2:
            snp_data += ["G", "G"]
        else:
            snp_data += ["0", "0"]
    
    ped_rows.append([fid, iid, pid, mid, sex, pheno] + snp_data)

# Save .ped file (no space in filename)
with open("Genotype_data.ped", "w") as f:
    for line in ped_rows:
        f.write(" ".join(map(str, line)) + "\n")

# Create and save .map file
map_rows = []
for idx, snp in enumerate(snp_cols):
    chr_num = "1"
    pos = str(10000 + idx)
    map_rows.append([chr_num, snp, "0", pos])

pd.DataFrame(map_rows).to_csv("Genotype_data.map", sep="\t", header=False, index=False)

print("✅ Converted to .ped and .map successfully!")

