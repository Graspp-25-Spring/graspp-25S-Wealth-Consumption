# graspp-25S-Wealth-Consumption

## Mumbers
・Haichuan Zhang

・Peilin Wang

・Zhenyang Cui

## Description of Class
Data Science for Public Policy (2025S1S2) of Utokyo

## Research Question
Does household consume more when its wealth increases? 

We are interested in the relationship between household wealth and private consumption. Using data for EU zone 20 countries and Japan, we expect to identify a positive relationship between consumption and wealth. Our methodology is OLS regression, and we aim to compute Marginal Propensity to consume(MPC) and elasticity to represent the effect.

## Launch Notebook with Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JaredChoi-git/graspp-25S-Wealth-Consumption/main)

## Description of this Repository

### Propose of this Repository
This repository is for group work assignments.

### Folder Structure
- `data/`: Raw and processed datasets
- `docs/`: Project Documentation (Reports, Presentations)
- `notebooks/`: Jupyter notebooks
- `report/`: Output (Visualizations, Models, Summaries)
- `src/`: Python scripts

## Milestone 1 （Until 2025/4/28）

We aim to select and clean data and generate descriptive statistics.

### Data Description

#### EU
- **Description**: Quarterly private consumption data  
- **Source**: European Central Bank (ECB)  
- **Countries/Entities**: 20 EU zone countries  
- **API Documentation Link**: [`ecbdata`](https://pypi.org/project/ecbdata/)  
- **Notes**:  
  - The dataset ranges from April 1995 to December 2024  
  - The `ecbdata` library is installed via pip  
  - We've modified the Python script (`download_data.py`) to include the proper data import line, and tested that it works

#### Japan
- **Description**: Quarterly macroeconomic data for Japan (consumption, income, and wealth)
- **Source**: Cabinet Office Japan (内閣府) and Family Income and Expenditure Survey (e-Stat)
- **Countries/Entities**: Japan
- **Variables**:
  - Household consumption (家計最終消費支出)
  - Fixed asset value (住宅資産)
  - Stock market financial assets (株式保有資産)
  - Employee compensation (雇用者報酬)
- **Download Method**: requests.get() from official Cabinet Office URLs
- **Dataset Range**: 1994–2023 (Annual, some quarterly if available)
- **Notes**:
  - Data is downloaded from Cabinet Office open data page (ESRI)
  - File paths are structured to be relative, compatible with GitHub repositories
  - The script has been updated to dynamically locate project root and save the data using os.path.join(...)

## Milestone 2 （Until 2025/05/12）

Data Visualization and Interpretation
