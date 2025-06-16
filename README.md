# graspp-25S-Wealth-Consumption

## List of Mumbers
・Haichuan Zhang

・Peilin Wang

・Zhenyang Cui

## Main Individual Contributions
- Haichuan Zhang
  - Collected and analyzed macroeconomic data for the EU.
  - Researched and organized related prior studies and literature.

- Peilin Wang
  - Organized and prepared presentation materials.

- Zhenyang Cui
  - Managed the GitHub repository and project structure.
  - Developed and maintained the Jupyter Notebook.

Collected and analyzed macroeconomic data for Japan

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

- `data/`: Raw and processed datasets  
  - `raw_data/`: Raw macro data from EU and Japan  
  - `processing_data/`: Intermediate processed data  
  - `clean/`: Final dataset used for regression  

- `docs/`: Project Documentation (Reports, Presentations)

- `notebooks/`: Jupyter notebooks  
  - `milestone_1_update.ipynb`: Main notebook for figures and modeling

- `report/`: Output (Visualizations, Models, Summaries)  
  *(We won't use this file this time.)*

- `src/`: Python scripts  
  - `data_function/`: Scripts for data extraction and downloading

- `requirements.txt` / `environment.yml`: Dependency files

- `README.md`: Project overview


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

- Data Pipeline:
  - Raw → processed via custom extract scripts (`src/data_function/`)
  - Cleaned merged datasets used throughout analysis
  
- Contents:
  - visualization:
    - Line plots, bar charts, histograms
    - QQ plots, residual vs fitted, ACF plots
    - Radar chart comparison (2014 vs 2023)
    - Pairwise scatterplots with regression lines
  - regression analysis
    - OLS, robust OLS, GLS, and GLM models
    - Growth rate and log-differenced specifications
    - Residual diagnostics and normality tests
    - Shapiro-Wilk test results
  - Interactive Tool:
    - dashboard to explore Japanese macroeconomic indicators

## Milestone 3 （Until 2025/06/23）

- The goal for milestone 3 is to have your analysis presented in a white-paper, slides or a dashboard.
  - It is required to record a video (10-15 minutes).
    - (1) high level overview of your github repository.
    - (2) a quick overview of your slides/whitepaper.

- Contents:
  - 1. Data description (including links), research question, link to your project github
  - 2. Descriptive statistics (country count, time period), min, max, mean of your variables (not all have to be included)
  - 3. Scatter plots to compare your main relationships of interest (you don't have to include all controls)
  - 4. Additional plots (time series, histograms)
  - 5. Regression/Statistical Model
  - 6. Optional: Text Analysis
  - 7. Optional: Case studies

## Key Findings:
    - EU:
      - Household consumption exhibits a steady upward trend over time, closely tracking the rise in employment income and housing wealth.
      - A sharp decline in 2020, followed by a swift rebound, reflects the consumption shock caused by the COVID-19 pandemic and subsequent recovery.
      - In the long-run model:
        - employment income, housing wealth, and financial assets—are positively and significantly associated with household consumption.
        - Among these, income has the largest and most statistically robust effect, suggesting a strong income-consumption linkage over time.
      - In the short-run model:
        - Only housing wealth growth is significantly correlated with changes in consumption.
        - Changes in income and financial wealth do not exhibit significant short-term impacts on consumption growth.
    - Japan:  
      - In the short-run model, stock market wealth (financial assets) has a statistically significant positive effect on household consumption, indicating that capital gains may directly influence consumer behavior in Japan.
      - Although housing wealth has a relatively larger coefficient, it is not statistically significant, implying that short-run consumption is less responsive to changes in real estate values.
      - Employment income shows no significant short-run effect, possibly reflecting Japan's stable and slow-changing wage system.

## Summary of Our Work:
### EU: 
 - To Research Question: Does household consumption increase with household wealth?
   - Yes – Strong Long-Run Relationship
   - Conclusion: In the EU, household consumption increases with household wealth in the long run, especially with stable income and rising real estate and financial asset values.
### Japan: 
 - To Research Question: Does household consumption increase with household wealth?
   - Partially – Short-Run Sensitivity to Financial Wealth
   - Conclusion: In Japan, short-term consumption responds mainly to financial wealth, not housing or income.
