"""
Probability Density Function Assignment
Roll Number: 102313066

Transformation:
z = x + 0.15 sin(0.6x)

PDF:
p(z) = c * exp(-λ (z - μ)^2)

Parameters estimated using Maximum Likelihood Estimation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import os


ROLL_NUMBER = 102313066

a_r = 0.05 * (ROLL_NUMBER % 7)
b_r = 0.3 * ((ROLL_NUMBER % 5) + 1)

print("Roll Number:", ROLL_NUMBER)
print("a_r =", a_r)
print("b_r =", b_r)
print("Transformation: z = x + 0.15 sin(0.6x)\n")



data_path = "../data/data.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError("Place dataset as data/data.csv")

try:
    df = pd.read_csv(data_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(data_path, encoding="latin-1")


if "no2" in df.columns:
    x = df["no2"].dropna().values
elif "NO2" in df.columns:
    x = df["NO2"].dropna().values
else:
    raise ValueError("NO2 column not found in dataset")

print("Total NO2 samples:", len(x))
print("Original Mean:", np.mean(x))
print("Original Std:", np.std(x), "\n")



z = x + a_r * np.sin(b_r * x)

print("Transformation applied.")
print("Transformed Mean:", np.mean(z))
print("Transformed Std:", np.std(z), "\n")


def negative_log_likelihood(params, data):
    mu, lam = params

    if lam <= 0:
        return np.inf

    c = np.sqrt(lam / np.pi)
    log_likelihood = np.sum(np.log(c) - lam * (data - mu) ** 2)

    return -log_likelihood


initial_mu = np.mean(z)
initial_lambda = 1 / (2 * np.var(z))

result = minimize(
    negative_log_likelihood,
    x0=[initial_mu, initial_lambda],
    args=(z,),
    method="L-BFGS-B",
    bounds=[(None, None), (1e-8, None)]
)

mu = result.x[0]
lam = result.x[1]
c = np.sqrt(lam / np.pi)

print("Estimated Parameters:")
print("μ =", mu)
print("λ =", lam)
print("c =", c, "\n")



z_range = np.linspace(min(z), max(z), 500)
pdf = c * np.exp(-lam * (z_range - mu) ** 2)



import seaborn as sns
sns.set_style("whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Original NO2 Distribution
axes[0, 0].hist(x, bins=50, density=True, alpha=0.7, color="#4C72B0")
axes[0, 0].set_title("Original NO2 Distribution")
axes[0, 0].set_xlabel("NO2")
axes[0, 0].set_ylabel("Density")

# Transformation Function
x_sample = np.linspace(min(x), max(x), 500)
z_sample = x_sample + a_r * np.sin(b_r * x_sample)

axes[0, 1].plot(x_sample, z_sample, color="#DD8452", linewidth=2)
axes[0, 1].plot(x_sample, x_sample, linestyle="--", color="gray")
axes[0, 1].set_title("Transformation: z = x + a sin(bx)")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("z")

# Transformed Data Distribution
axes[1, 0].hist(z, bins=50, density=True, alpha=0.7, color="#55A868")
axes[1, 0].set_title("Distribution of Transformed Variable (z)")
axes[1, 0].set_xlabel("z")
axes[1, 0].set_ylabel("Density")

# Fitted PDF vs Empirical
z_range = np.linspace(min(z), max(z), 500)
pdf = c * np.exp(-lam * (z_range - mu) ** 2)

axes[1, 1].hist(z, bins=50, density=True, alpha=0.5, label="Empirical")
axes[1, 1].plot(z_range, pdf, color="red", linewidth=2, label="Estimated PDF")
axes[1, 1].set_title("Estimated Gaussian PDF Fit")
axes[1, 1].set_xlabel("z")
axes[1, 1].set_ylabel("Density")
axes[1, 1].legend()

plt.suptitle(
    f"Probability Density Function Learning\nRoll No: {ROLL_NUMBER}",
    fontsize=16
)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("assignment_presentation.png", dpi=300)
plt.show()

print("Presentation plot saved as assignment_presentation.png")
