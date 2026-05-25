# India AFOLU Sector - Agricultural GHG Emissions Analysis

**Author:** Vanshita Sharma | M.Sc. Agronomy | ISO 14064 GHG Lead Verifier (TÜV SÜD)  
**Data Source:** FAOSTAT (Food and Agriculture Organization, United Nations)  
**Language:** Python (pandas, matplotlib)

---

## Overview

This project analyses India's agricultural greenhouse gas (GHG) emissions across key AFOLU 
(Agriculture, Forestry and Other Land Use) sources using FAOSTAT data. It produces 
trend visualisations and a policy-relevant summary covering India's Updated NDC (2022) 
commitments to reduce emissions intensity by 45% by 2030.

The analysis was motivated by a gap in accessible, source-disaggregated visualisations 
of India's agricultural emissions - most policy documents cite aggregate figures without 
breaking down the relative contribution and trajectory of individual emission sources.

---

## Research Questions

1. How have India's total agricultural GHG emissions trended over time?
2. Which emission sources dominate India's agricultural GHG profile?
3. How do the four key sources - enteric fermentation, rice cultivation, synthetic 
   fertilisers, and manure management - compare in magnitude and trajectory?

---

## Methodology

- Data filtered for India across all available years from FAOSTAT emissions database
- Emissions standardised to kt CO2 equivalent using IPCC GWP values
- Three analyses conducted:
  - Total emissions trend over time
  - Top emission sources by average over last 10 years
  - Year-by-year comparison of four key policy-relevant sources

---

## Key Findings

- **Enteric fermentation** is India's single largest agricultural emission source — 
  consistent with India having the world's largest livestock population (~536 million animals)
- **Rice cultivation** is the second largest source, reflecting India's status as 
  the world's second largest rice producer (~44 million hectares under cultivation)
- **Synthetic fertiliser** emissions show an upward trend linked to intensification 
  of Indian agriculture post-Green Revolution
- Total agricultural emissions show a steady upward trend, underscoring the urgency 
  of AFOLU-sector interventions in India's NDC pathway

---

## Files

| File | Description |
|------|-------------|
| `analysis.py` | Main Python script — data loading, cleaning, analysis, visualisation |
| `india_afolu_summary.csv` | Exported summary of emissions by source and year |
| `chart1_total_emissions_trend.png` | India total agricultural GHG emissions trend |
| `chart2_top_sources.png` | Top 8 agricultural emission sources (last 10-year average) |
| `chart3_key_sources_comparison.png` | Key sources comparison — enteric fermentation, rice, fertilisers, manure |

---

## Policy Context

India's Updated NDC (2022) commits to:
- Reducing GDP emissions intensity by **45% by 2030** from 2005 levels
- Creating an additional **2.5-3 billion tonne carbon sink** through forests by 2030

The AFOLU sector is critical to both targets. This analysis provides a baseline 
understanding of where agricultural emissions are concentrated - essential for 
designing targeted, evidence-based mitigation strategies.

---

## Tools & Libraries

- Python 3.x
- pandas - data loading, filtering, grouping
- matplotlib - visualisation

---

## Related Work

This project is part of a broader research effort on India's AFOLU emissions and 
carbon market potential. See also:  
**The Unrealised Carbon Economy** - quantifying carbon credit income potential for 
India's 128.9 million smallholder farmers under the CCTS framework using NASA FIRMS 
satellite fire data and FAOSTAT emissions data.
