# AFOLU Sector Agricultural GHG Emissions Analysis — India
# Data Source: FAOSTAT (FAO, United Nations)
# Author: Vanshita Sharma | M.Sc. Agronomy | ISO 14064 Lead Verifier

import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATA
df = pd.read_csv("data/india_afolu_emissions.csv", encoding="latin1", sep="\t")

# 2. CLEAN AND FILTER
df = df[df["Area"] == "India"]
df = df[["Item", "Element", "Year", "Value", "Unit"]]
df = df.dropna(subset=["Value"])
df = df[df["Element"].str.contains("CO2eq", case=False, na=False)]

print("Dataset loaded. Shape:", df.shape)
print("\nTop emission sources found:")
print(df["Item"].value_counts().head(10))

# 3. TOTAL EMISSIONS TREND
total_by_year = df.groupby("Year")["Value"].sum().reset_index()
total_by_year.columns = ["Year", "Total_Emissions_kt_CO2eq"]

plt.figure(figsize=(12, 6))
plt.plot(total_by_year["Year"], total_by_year["Total_Emissions_kt_CO2eq"],
         color="#1F5C8B", linewidth=2.5, marker="o", markersize=4)
plt.fill_between(total_by_year["Year"], total_by_year["Total_Emissions_kt_CO2eq"],
                 alpha=0.1, color="#1F5C8B")
plt.title("India — Total Agricultural GHG Emissions Trend\n(FAOSTAT, kt CO2eq)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=11)
plt.ylabel("Emissions (kt CO2eq)", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("chart1_total_emissions_trend.png", dpi=150)
plt.close()
print("Chart 1 saved.")

# 4. TOP EMISSION SOURCES
recent = df[df["Year"] >= df["Year"].max() - 10]
by_source = recent.groupby("Item")["Value"].mean().sort_values(ascending=False).head(8)

plt.figure(figsize=(12, 6))
plt.barh(by_source.index[::-1], by_source.values[::-1], color="#1F5C8B")
plt.title("India — Top Agricultural GHG Emission Sources\n(Average last 10 years, kt CO2eq)", fontsize=14, fontweight="bold")
plt.xlabel("Average Emissions (kt CO2eq)", fontsize=11)
plt.grid(axis="x", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("chart2_top_sources.png", dpi=150)
plt.close()
print("Chart 2 saved.")

# 5. KEY SOURCES COMPARISON
sources_of_interest = ["Enteric Fermentation", "Rice Cultivation",
                        "Synthetic Fertilizers", "Manure Management"]
filtered = df[df["Item"].isin(sources_of_interest)]
pivot = filtered.groupby(["Year", "Item"])["Value"].sum().unstack(fill_value=0)

colors = ["#1F5C8B", "#2E9E6B", "#E07B39", "#8B1F5C"]
plt.figure(figsize=(13, 6))
for i, col in enumerate(pivot.columns):
    plt.plot(pivot.index, pivot[col], label=col, linewidth=2, color=colors[i % len(colors)])
plt.title("India — Key Agricultural GHG Sources Comparison\n(FAOSTAT, kt CO2eq)", fontsize=14, fontweight="bold")
plt.xlabel("Year", fontsize=11)
plt.ylabel("Emissions (kt CO2eq)", fontsize=11)
plt.legend(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("chart3_key_sources_comparison.png", dpi=150)
plt.close()
print("Chart 3 saved.")

# 6. EXPORT SUMMARY
summary = df.groupby(["Item", "Year"])["Value"].sum().reset_index()
summary.to_csv("india_afolu_summary.csv", index=False)
print("Summary CSV exported.")
print("\nAnalysis complete!")