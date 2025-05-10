# graspp-25S-Wealth-Consumption
## Numbers
・Haichuan Zhang

・Peilin Wang

・Xulong Gao

・Zhenyang Cui

## Dscription of class
Data Science for Public Policy (2025S1S2) of Utokyo


## Research Question
Does household consume more when their wealth increases? We are interested in the relationship between household wealth and private consumption. We expect to identify a positive relationship between consumption and wealth, using data for EU zone 20 countries, and Japan. Our methodology is OLS regression, and we aim to compute Marginal Propensity to consume(MPC) and elasticity to represent the effect.
## Launch Notebook with Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JaredChoi-git/graspp-25S-Wealth-Consumption/main)

# Dscription of this repository
## Why are you here
This repository is for group work assignment.

## Folder structure
- `data/`: Raw and processed datasets
- `docs/`: Project Documentation (Reports, Presentations)
- `notebooks/`: Jupyter notebooks
- `report/`: Output (Visualizations, Models, Summaries)
- `src/`: Python scripts

# Milestone 1 - Data Science for Public Policy
Milestone 1.  （Until 2025/4/28）

We aim to select and clean data, generate descriptive statistics.

- **Description**: Quarterly private consumption data  
- **Source**: European Central Bank (ECB)  
- **Countries/Entities**: 20 EU zone countries  
- **API Documentation Link**: [`ecbdata`](https://pypi.org/project/ecbdata/)  
- **Notes**:  
  - The dataset ranges from April 1995 to December 2024  
  - The `ecbdata` library is installed via pip  
  - We've modified the Python script (`download_data.py`) to include the proper data import line, and tested that it works
