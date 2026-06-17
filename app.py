import streamlit as st

st.set_page_config(page_title="Clickstream Analysis", layout="wide")

st.title("🛍️ E-commerce Clickstream Analysis Dashboard")
st.markdown("**Clothing Store User Behavior (2008) | End-to-End Project**")

st.success("✅ Dashboard Loaded Successfully!")

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Clicks", "165,000+")
col2.metric("Total Sessions", "~45,000")
col3.metric("Avg Clicks/Session", "3.6")

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Key Visualizations", "🔍 Insights", "📋 About Project"])

with tab1:
    st.subheader("Most Popular Categories")
    st.image("visualizations/category_distribution.png")

    st.subheader("Clicks per Session Distribution")
    st.image("visualizations/clicks_per_session.png")

    st.subheader("Activity by Day of Week")
    st.image("visualizations/activity_by_day.png")

with tab2:
    st.subheader("Main Findings")
    st.markdown("""
    - **Trousers** is the most popular category (~49,000 clicks)
    - Highest activity on **Tuesday & Wednesday**
    - Most sessions are very short (High Bounce Rate)
    - Country 29 dominates the traffic
    - Trousers have the highest price range
    """)

    st.subheader("Business Recommendations")
    st.markdown("""
    - Make **Trousers** the flagship category
    - Improve UX to reduce bounce rate
    - Run weekend promotions
    - Focus marketing on top country
    """)

with tab3:
    st.subheader("Project Details")
    st.write("This is a complete Clickstream Analysis project built as a portfolio piece.")
    st.write("**Tech Stack**: Python, Pandas, Seaborn, Matplotlib, Streamlit")
    
    st.markdown("### Links")
    st.markdown("- [View Notebooks](notebooks)")
    st.markdown("- [GitHub Repository](https://github.com/geethalakshmi579/ecommerce-clickstream-analysis)")

st.caption("Built by Geethalakshmi | Clickstream Analysis Project")
