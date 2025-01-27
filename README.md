# UBC Lost and Found System Analysis and Forecasting

<img src="./img/access.jpg" alt="drawing" style="width:100%;"/>
Access Services. Retrieved from <a href = "https://parking.ubc.ca/">UBC Parking</a> 

## Overview
This project explores the UBC Lost and Found system using a data-driven approach to uncover trends, improve operational efficiency, and provide actionable insights. By analyzing categorical distribution and temporal patterns of lost items, and building predictive time series forecasting models, this project aims to provide recommendations to optimize storage allocation, improve item recovery, and enhance communication channels.

The findings highlight how forecasting models and exploratory data analysis (EDA) can help design smarter, more proactive lost and found systems while also showcasing the broader applications of data science to operational challenges.

## Dataset
The [UBC Lost and Found database](https://lostandfound.ubc.ca/all-items) is a publicly accessible dataset containing information about items reported lost within the University of British Columbia campus. The dataset spans from May 2024 to the current day, with over 160 entries. Each entry includes details such as the item type, description, date lost, and location. The dataset retrieved as of January 2025 is used for the project.

## Key Features
### 1. Exploratory Data Analysis (EDA)
- **Commonly Lost Items**: Identified frequent categories, such as electronics and keys, highlighting the need for targeted solutions.
- **Temporal Patterns**: Discovered peak loss periods by analyzing weekday and monthly trends.
- **Location Trends**: Identified high-traffic areas, such as libraries, as hotspots for lost items.
- **NLP on Item Descriptions**: Used natural language processing to classify item descriptions into meaningful subcategories like wallets, accessories, and tech items.

### 2. Predictive Modeling
- **ARIMA Model**: Focused on linear trends and long-term forecasting, useful for aggregate resource planning.
- **LSTM Model**: Captured nonlinear patterns and short-term dependencies, useful for dynamic daily forecasts.
- **Model Comparison**: Highlighted trade-offs between simplicity (ARIMA) and flexibility (LSTM) for different forecasting needs.

### 3. Actionable Recommendations
- **Targeted Awareness Campaigns**: Suggested communication strategies to reduce losses during high-risk periods.
- **Optimized Storage Solutions**: Recommended resource allocation based on predicted item trends.
- **Enhanced Communication Platforms**: Proposed centralized reporting systems for better lost and found operations.

## Technical Details
- **Libraries**: pandas, matplotlib, numpy, seaborn, scikit-learn, statsmodels, NLTK, mglearn, spaCy, PyTorch
- **Model Building**: Time series forecasting with ARIMA and minimal-layer LSTM models