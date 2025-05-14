import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set up Streamlit page
st.set_page_config(page_title="Macroeconomic Dashboard", layout="centered")
st.title("Macroeconomic Variable Correlation Dashboard (Japan)")

# Load macroeconomic data
@st.cache_data
def load_data():
    df = pd.read_csv("data/clean/japan/merged_macro_data.csv")
    return df

df_raw = load_data()

# Define target variables and display names
value_columns = ['household_consumption', 'fixed_asset', 'stock_asset', 'employment_income']
col_map = {
    'household_consumption': 'Household Consumption',
    'fixed_asset': 'Housing Wealth',
    'stock_asset': 'Stock Asset',
    'employment_income': 'Employment Income'
}

# Select data transformation method
data_type = st.radio("Select Data Type", ["Raw", "Log", "Diff", "Log-Diff"], horizontal=True)

# Copy raw data for transformation
df = df_raw.copy()

# Apply transformation based on selection
if data_type == "Log":
    for col in value_columns:
        df[col] = np.log(df[col])
elif data_type == "Diff":
    for col in value_columns:
        df[col] = df[col].diff()
    df = df.dropna().reset_index(drop=True)
elif data_type == "Log-Diff":
    for col in value_columns:
        df[col] = np.log(df[col]).diff()
    df = df.dropna().reset_index(drop=True)

# Year range filter
years = df['year'].unique()
selected_years = st.slider(
    "Select Year Range",
    int(years.min()),
    int(years.max()),
    (int(years.min()), int(years.max()))
)
df_filtered = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

# Variable selectors
var_x = st.selectbox("Select X-axis variable", value_columns, format_func=lambda x: col_map[x])
var_y = st.selectbox("Select Y-axis variable", value_columns, index=1, format_func=lambda x: col_map[x])

# Plot scatter plot with regression line
if var_x and var_y:
    st.subheader(f"{col_map[var_x]} vs {col_map[var_y]} ({data_type})")
    fig, ax = plt.subplots()
    sns.regplot(data=df_filtered, x=var_x, y=var_y, ax=ax, line_kws={"color": "red"})
    ax.set_xlabel(col_map[var_x])
    ax.set_ylabel(col_map[var_y])
    st.pyplot(fig)

    # Display Pearson correlation coefficient
    corr_val = df_filtered[[var_x, var_y]].corr().iloc[0, 1]
    st.markdown(f"Pearson Correlation Coefficient: `{corr_val:.3f}`")
