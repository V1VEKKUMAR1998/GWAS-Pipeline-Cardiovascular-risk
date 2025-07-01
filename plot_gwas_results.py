import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load GWAS result file
df = pd.read_csv("results/gwas_results.assoc.logistic", delim_whitespace=True)

# Filter for additive model and drop NA p-values
df = df[df["TEST"] == "ADD"].dropna(subset=["P"])

# Manhattan Plot
df["-log10(P)"] = -np.log10(df["P"])
df["ind"] = range(len(df))
df_grouped = df.groupby("CHR")

plt.figure(figsize=(14, 6))
colors = ["#1f77b4", "#ff7f0e"]
x_labels, x_labels_pos = [], []

for i, (name, group) in enumerate(df_grouped):
    group.plot(kind="scatter", x="ind", y="-log10(P)", color=colors[i % 2], ax=plt.gca(), s=10)
    x_labels.append(name)
    x_labels_pos.append((group["ind"].iloc[-1] + group["ind"].iloc[0]) / 2)

plt.axhline(-np.log10(5e-8), color='red', linestyle='--')  # genome-wide significance line
plt.xticks(x_labels_pos, x_labels)
plt.xlabel("Chromosome")
plt.ylabel("-log10(P)")
plt.title("Manhattan Plot")
plt.tight_layout()
plt.savefig("results/manhattan_plot.png")
plt.close()

# QQ Plot
observed_p = np.sort(df["P"])
expected_p = -np.log10(np.linspace(1/len(observed_p), 1, len(observed_p)))
observed_logp = -np.log10(observed_p)

plt.figure(figsize=(6, 6))
plt.scatter(expected_p, observed_logp, s=10)
plt.plot([0, max(expected_p)], [0, max(expected_p)], color='red', linestyle='--')
plt.xlabel("Expected -log10(P)")
plt.ylabel("Observed -log10(P)")
plt.title("QQ Plot")
plt.tight_layout()
plt.savefig("results/qq_plot.png")
plt.close()

print("✅ Manhattan plot saved as: results/manhattan_plot.png")
print("✅ QQ plot saved as: results/qq_plot.png")
