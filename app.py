import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Clickstream Dashboard", layout="wide")
st.title("🛍️ E-commerce Clickstream Analysis")
st.markdown("**Clothing Store User Behavior Analysis (2008)**")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/e-shop_cleaned_final.csv')

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")
selected_categories = st.sidebar.multiselect("Categories", df['main_category_name'].unique(), default=df['main_category_name'].unique())
df_filtered = df[df['main_category_name'].isin(selected_categories)]

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Clicks", f"{len(df):,}")
col2.metric("Total Sessions", f"{df['session_id'].nunique():,}")
col3.metric("Avg Clicks/Session", f"{len(df)/df['session_id'].nunique():.2f}")
col4.metric("Bounce Rate (approx)", "High")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📅 Time Analysis", "💰 Pricing"])

with tab1:
    st.subheader("Category Distribution")
    fig1 = plt.figure(figsize=(10,5))
    df_filtered['main_category_name'].value_counts().plot(kind='bar', color='coral')
    plt.xticks(rotation=45)
    st.pyplot(fig1)

with tab2:
    st.subheader("Activity by Day of Week")
    fig2 = plt.figure(figsize=(10,5))
    sns.countplot(data=df_filtered, x='day_of_week', 
                  order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    plt.xticks(rotation=45)
    st.pyplot(fig2)

with tab3:
    st.subheader("Price Distribution by Category")
    fig3 = plt.figure(figsize=(10,6))
    sns.boxplot(data=df_filtered, x='main_category_name', y='price')
    plt.xticks(rotation=45)
    st.pyplot(fig3)

st.caption("Clickstream Analysis Project • Built with Streamlit")