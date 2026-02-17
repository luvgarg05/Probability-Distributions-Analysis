# Probability Density Function Analysis

<div align="center">

**Lavanya Garg**  
Roll Number: `102313066`

</div>

---

## 🎯 Results - Estimated Parameters

The probability density function:

```
p(z) = c × exp(-λ(z-μ)²)
```

<br>

### **Final Parameter Values**

| Parameter | Value |
|:---------:|:------|
| **λ (lambda)** | `0.0014605774066158705` |
| **μ (mu)** | `25.81266175860678` |
| **c** | `0.021561916150066855` |

<br>

## 📈 Visualizations

<div align="center">

![Results](assignment1_results.png)

*Figure: (Top-left) Original NO2 distribution, (Top-right) Transformation function, (Bottom-left) Fitted PDF vs empirical distribution, (Bottom-right) Q-Q plot*

</div>

<br>

---

## 📌 Problem Statement

Given NO2 air quality data, apply a non-linear transformation and estimate the parameters of a probability density function.

<br>

## 🔧 Transformation

Based on roll number calculations:

```
ar = 0.05 × (102303451 mod 7) = 0.25
br = 0.3 × (102303451 mod 5 + 1) = 0.6
```

**Transformation Function:**

```python
z = x + 0.25 × sin(0.6x)
```

<br>

## 📊 Dataset

- **Source:** India Air Quality Data
- **Feature:** NO2 levels
- **Data Points:** 419,509 (after removing null values)

<br>

## 🔬 Method

Used **Maximum Likelihood Estimation (MLE)** to find the parameters.

The normalization constraint `c = √(λ/π)` was applied to ensure the PDF integrates to 1.

<br>

## 📁 Repository Structure

```
.
├── README.md                   # This file
├── assignment1_solution.py     # Python implementation
├── assignment1_results.png     # Visualization outputs
└── .gitignore                  # Git ignore file
```

<br>

## 🚀 Running the Code

Make sure you have the dataset file (`data.csv` or `data-2.csv`) in the same directory.

```bash
python assignment1_solution.py
```

<br>

## 📦 Dependencies

```
pandas
numpy
matplotlib
scipy
```

<br>

---


