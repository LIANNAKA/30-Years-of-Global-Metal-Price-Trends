# 📊 Global Metal Price Forecasting & Predictive Analytics (1992–2021)

---
<img width="2409" height="1463" alt="Screenshot 2026-05-23 230221" src="https://github.com/user-attachments/assets/4b5c9c19-242c-4d45-98a0-f78c2a8308f5" />
<img width="893" height="597" alt="Screenshot 2026-05-14 151310" src="https://github.com/user-attachments/assets/24c120dc-2cf3-4d45-a429-6629ece9b245" />

# 🧾 Project Overview

This project analyzes and forecasts 30 years of historical global metal price data using Exploratory Data Analysis (EDA), Feature Engineering, and Machine Learning techniques.

The project initially focused on identifying long-term market trends, inflation impact, and commodity volatility through EDA and was later extended into predictive analytics using regression models and time-series feature engineering.

The analysis covers five major metals:

* Aluminium
* Gold
* Nickel
* Silver
* Uranium

The primary goal is to transform raw financial and commodity market data into actionable business insights and predictive forecasting intelligence that can support industrial planning, investment analysis, and risk management.

---

# 🎯 Objectives

* Analyze long-term commodity price trends across major metals
* Understand volatility behavior and market fluctuations
* Study inflation-adjusted vs actual pricing trends
* Build predictive machine learning models for commodity forecasting
* Compare regression model performance across different metals
* Generate business-oriented insights for financial and industrial decision-making

---

# 📁 Dataset Information

### Source

Kaggle – Metal Price Changes (Last 30 Years)

### Time Period

1992 – 2021

### Dataset Size

361 rows × 13 columns

### Key Features

* Monthly metal prices
* Inflation rate
* Inflation-adjusted metal prices

### Metals Included

* Gold
* Silver
* Aluminium
* Nickel
* Uranium

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Time-Series Analysis
* Jupyter Notebook

---

# 🧹 Data Preprocessing

To ensure clean and reliable analysis, the following preprocessing steps were performed:

* Handled missing values 
* Created a unified `Date` column for time-series analysis
* Converted data into chronological order
* Verified dataset consistency and structure
* Selected relevant columns for focused analysis
* Exported cleaned datasets for machine learning workflows

---

# ⚙️ Feature Engineering

Time-series feature engineering was implemented to transform historical pricing data into predictive learning signals.

### Engineered Features

#### 📌 Lag Features

Created:

* 1-month lag
* 2-month lag
* 3-month lag

to capture historical dependencies and sequential market behavior.

#### 📌 Rolling Mean Features

Generated moving averages to smooth short-term fluctuations and identify broader market trends.

#### 📌 Temporal Features

Extracted:

* Year
* Month
* Quarter

to capture seasonal and cyclical patterns.

#### 📌 Volatility Indicators

Calculated percentage returns to measure market volatility and pricing behavior.
<img width="1120" height="1201" alt="Screenshot 2026-05-14 151144" src="https://github.com/user-attachments/assets/5f3af397-b960-4b6d-a7d4-cc6411b8bc27" />

---

# 🤖 Machine Learning Models

The project was extended into predictive analytics using regression-based machine learning models.

## 📈 Linear Regression

Implemented as a baseline regression model to understand linear market behavior and long-term pricing trends.

### Key Observation

* Performed exceptionally well on stable trend patterns
* Achieved near-perfect fitting on engineered historical data

---

## 🌲 Random Forest Regressor

Implemented to capture nonlinear relationships and volatility-driven market movements.

### Performance Highlights

| Metal     | R² Score |
| --------- | -------- |
| Gold      | 0.89     |
| Silver    | 0.92     |
| Aluminium | 0.95     |
| Nickel    | 0.96     |
| Uranium   | 0.45     |

### Key Observation

Random Forest performed significantly better on nonlinear and industrial-demand-driven commodities while struggling with extreme volatility spikes in Uranium prices.

---

# 📊 Exploratory Data Analysis (EDA)

## 📈 Trend Analysis

* Studied long-term market movement across all metals
* Compared growth behavior and commodity cycles

## 📉 Volatility Analysis

* Identified highly volatile commodities
* Detected periods of economic instability and market shocks

## 💰 Inflation Impact Analysis

* Compared actual vs inflation-adjusted prices
* Evaluated purchasing power changes over time

# 🔍 Key Insights

* Gold demonstrated strong long-term growth and acted as a reliable inflation hedge
* Silver showed significantly higher volatility compared to Gold
* Uranium experienced extreme market spikes, especially around 2007–2008
* Aluminium and Nickel reflected industrial demand cycles and economic activity
* Random Forest captured nonlinear pricing behavior more effectively than baseline regression
* Traditional regression models struggled during highly volatile market shocks

---

# 📈 Business & Industrial Impact

This project demonstrates practical applications of predictive analytics in:

### 📦 Manufacturing Industry

* Raw material cost forecasting
* Procurement planning

### 💹 Investment & Finance

* Commodity trend analysis
* Inflation hedge evaluation

### ⚙️ Supply Chain & Risk Management

* Pricing strategy optimization
* Volatility monitoring

### 🌍 Economic Research

* Long-term market cycle analysis
* Inflation-adjusted commodity evaluation

---

# 📊 Model Evaluation Metrics

The models were evaluated using:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

These metrics helped compare:

* forecasting stability
* prediction accuracy
* volatility handling capability

---

# ⚠️ Challenges Faced

* Handling missing and inconsistent time-series data
* Aligning inflation-adjusted vs actual prices
* Managing volatility-driven market spikes
* Preserving time-series order during model training
* Forecasting highly unstable commodity behavior

---

# 🚀 Future Scope

* ARIMA-based time-series forecasting
* LSTM deep learning models
* Real-time commodity price tracking system
* Interactive Power BI / Tableau dashboards
* Streamlit deployment for live forecasting
* Advanced financial forecasting pipelines

---

# 📌 Conclusion

This project demonstrates how Exploratory Data Analysis, Feature Engineering, and Machine Learning can transform raw historical commodity data into meaningful forecasting intelligence and business insights.

By combining statistical analysis, regression modeling, and predictive analytics, the project highlights how data-driven approaches can support smarter decision-making in finance, manufacturing, procurement, and economic forecasting.

The project evolved from descriptive analytics into a scalable predictive analytics pipeline, reflecting a practical industry-oriented approach to commodity market forecasting.
