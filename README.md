# graspp-25S-Wealth-Consumption

## List of Mumbers
・Haichuan Zhang

・Peilin Wang

・Zhenyang Cui

## Launch Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JaredChoi-git/graspp-25S-Wealth-Consumption/main)

## Research Question
**Does household consumption increase with household wealth?**

We explore the relationship between household wealth and private consumption using data from:
- 20 EU zone countries
- Japan

We aim to test this using regression analysis (OLS, GLS, GLM) and quantify:
- Elasticity of consumption to different types of wealth
- Marginal Propensity to Consume (MPC)

## Description of this Repository

### Propose of this Repository
This repository is for group work assignments.

### Folder Structure (Simple Version)
graspp-25S-Wealth-Consumption/
│
├── data/
│    ├── raw data                       # Raw macro data from EU and Japan 
│    ├── processing_data                # Intermediate processed data
│    └── clean                          # Final dataset used for regression
│
├── docs/                               # Project Documentation (Presentations)
│
├── notebooks/
│    ├── milestone_1_update.ipynb       # Main notebook for figures and modeling
│    
├── src/
│    └── data_function/                 # Scripts for data extraction and data downloading
│
├── requirements.txt / environment.yml  # Dependencies
└── README.md

## Milestone 1 （Until 2025/4/28）

- We aim to select and clean data and generate descriptive statistics.
  - Main analysis notebook: `notebooks/milestone_1_update.ipynb`

### Data Description

#### EU
- **Source**: European Central Bank (ECB)
- **Description**: Quarterly private consumption data
- **Countries/Entities**: 20 EU zone countries
- **API Documentation Link**: [`ecbdata`](https://pypi.org/project/ecbdata/)
- **File Path after Downloading**: `data/raw data/EU`
- **Notes**:  
  - The dataset ranges from April 1995 to December 2024  
  - The `ecbdata` library is installed via pip  
  - We've modified the Python script (`download_data.py`) to include the proper data import line, and tested that it works

#### Japan
- **Source**: Cabinet Office Japan (内閣府) and Family Income and Expenditure Survey (e-Stat)
- **Description**: Quarterly macroeconomic data for Japan ([Household Consumption (2023)](https://www.esri.cao.go.jp/jp/sna/data/data_list/kakuhou/files/2023/tables/2023ffm1n_jp.xlsx), [Fixed Assets (2023)](https://www.esri.cao.go.jp/jp/sna/data/data_list/kakuhou/files/2023/tables/2023si4_jp.xlsx), [Employment Income (2023)](https://www.esri.cao.go.jp/jp/sna/data/data_list/kakuhou/files/2023/tables/2023ffm2_jp.xlsx))
- **Countries/Entities**: Japan
- **Variables**:
  - Household consumption (家計最終消費支出)
  - Fixed asset value (住宅資産)
  - Stock market financial assets (株式保有資産)
  - Employee compensation (雇用者報酬)
- **Download Method**: requests.get() from official Cabinet Office URLs
- **File Location**:
  - Raw Excel: `data/raw data/japan/{file_name}.xlsx`
  - Processed CSV: `data/processing_data/japan/{file_name}.csv`
  - Final merged: `data/clean/japan/merged_macro_data.csv`
- **Dataset Range**: 1994–2023 (Annual, some quarterly if available)
- **Notes**:
  - Data is downloaded from Cabinet Office open data page (ESRI)
  - File paths are structured to be relative, compatible with GitHub repositories
  - The script has been updated to dynamically locate project root and save the data using os.path.join(...)

## Milestone 2 （Until 2025/05/26）

- We aim to visualize macroeconomic trends and conduct regression analysis.
  - Main analysis notebook: `notebooks/milestone_1_update.ipynb`

- Includes:
  - visualization:
    - Line plot
    - Bar chart
    - Histogram
    - QQ plot
    - Residuals vs Fitted
    - ACF plot
    - Radar chart
  - regression analysis
    - Growth rate calculations
    - Log-difference models
    - Residual diagnostics
    - AR(1) regressions
