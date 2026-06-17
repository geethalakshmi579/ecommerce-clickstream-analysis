# Clickstream Analysis - E-commerce User Behavior (2008 Dataset)

## 📋 Project Overview
End-to-end clickstream analysis on an online clothing store dataset to understand user journeys, identify popular paths, drop-off points, and derive actionable business insights.

### 🎯 Objectives
- Exploratory Data Analysis (EDA) on clickstream data
- Sessionization and user path analysis
- Understand user behavior and category performance
- Provide data-driven business recommendations

### 🛠 Tech Stack
- **Python**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Tools**: Jupyter Notebooks

### 📊 Dataset
- **Source**: E-shop clothing 2008 dataset
- **Size**: ~165,000 click events
- **Time Period**: April to August 2008
- **Key Columns**: Session ID, Page Category, Price, Country, Order (sequence)

### 📈 Key Visualizations

![Most Popular Categories](visualizations/category_distribution.png)
![Distribution of Clicks per Session](visualizations/clicks_per_session.png)
![User Activity by Day of Week](visualizations/activity_by_day.png)
![Category Popularity by Day](visualizations/category_by_day.png)
![Price Distribution by Category](visualizations/price_by_category.png)
![Top 10 Countries](visualizations/top_countries.png)

---

### 🔍 Main Findings

1. **Category Performance**
   - **Trousers** is the most popular category with ~49,000 clicks.
   - Sale, Blouses, and Skirts have similar engagement (~38,000 clicks each).

2. **User Engagement**
   - Most sessions are very short — majority of users make only 1 to 10 clicks.
   - High bounce rate observed (many users leave after very few interactions).

3. **Temporal Patterns**
   - Highest activity on **Tuesday** and **Wednesday**.
   - Lowest activity on **Saturday** and **Sunday**.
   - Trousers remain the dominant category every day.

4. **Pricing Insights**
   - Trousers have the highest median price and widest price range.
   - Sale category has the lowest prices.

5. **Geographical Insights**
   - **Country 29** dominates with over 80% of total traffic (~135,000 clicks).
   - Very limited activity from other countries.

6. **User Behavior**
   - Users mostly browse within one category per session.
   - Limited cross-category exploration.

---

### 💡 Business Recommendations

- **Focus on Trousers**: Make trousers the flagship category on homepage, run targeted ads, and maintain strong inventory.
- **Reduce Bounce Rate**: Improve website UX with better product recommendations, faster navigation, and clearer CTAs.
- **Weekend Campaigns**: Launch special discounts or promotions on weekends to boost low traffic.
- **Market Focus**: Concentrate efforts on Country 29 while testing expansion strategies for other regions.
- **Pricing Strategy**: Position trousers as premium products and use aggressive discounts in the Sale category to drive volume.

---

## How to Run the Project

1. Clone the repository
2. Place the original dataset in the `data/` folder
3. Install dependencies:
   ```bash
   pip install -r requirements.txt


clickstream-analysis/
├── data/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_cleaning_and_features.ipynb
│   ├── 03_session_path_analysis.ipynb
│   └── 04_visualizations_insights.ipynb
├── visualizations/
├── README.md
└── requirements.txt

## Author
Venkata Geetha lakshmi Gunda — Aspiring Data Analyst