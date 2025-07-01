# GWAS-Pipeline-Cardiovascular-risk
# GWAS Pipeline for Cardiovascular Risk

This project demonstrates a complete Genome-Wide Association Study (GWAS) pipeline using synthetic genotype and phenotype data to identify SNPs associated with cardiovascular risk.

## 🧪 Project Goals
- Simulate genotype and phenotype data for 50 individuals
- Perform GWAS using PLINK
- Generate Manhattan and QQ plots
- Interpret top SNP associations

## 🛠️ Tools Used
- Python (pandas, matplotlib, seaborn)
- PLINK 1.9
- Gitpod (for cloud-based development)

## 📁 Key Files
- `synthetic_genotype_50samples.csv`
- `synthetic_phenotype_50samples.csv`
- `plot_gwas_results.py` – generates Manhattan and QQ plots
- `fix_phenotype_ids.py`, `fix_pheno_recoding.py` – formats phenotype files
- `results/` – contains GWAS output and plots

## 📊 Example Output
- `results/manhattan_plot.png`
- `results/qq_plot.png`

## 🚀 Run the Pipeline
```bash
# Convert files and run PLINK
python3 convertfile.py
plink --file Genotype_data --make-bed --out output_data
python3 fix_phenotype_ids.py
python3 fix_pheno_recoding.py
plink --bfile output_data --pheno phenotype_data_plink.txt --make-bed --out data/final_ready
plink --bfile data/final_ready --logistic --out results/gwas_results

# Generate plots
python3 plot_gwas_results.py
