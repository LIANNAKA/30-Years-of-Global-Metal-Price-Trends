# 📊 Global Metal Price Forecasting & Predictive Analytics (1992–2021)
---
## 🌐 Live Demo

🔗 **Try the application here:** https://comoditypricechangetrends30yr.streamlit.app/

---

## 🎥 Demo Video

🎬 **Watch the complete walkthrough:**  

https://github.com/user-attachments/assets/c8743478-a17d-4d75-ab75-849d3ec2d04a

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
## 🚀 XGBoost Regressor

To further improve forecasting performance and capture complex market behavior, XGBoost Regressor was implemented as an advanced gradient boosting ensemble model.

### Why XGBoost?

Commodity prices are influenced by multiple nonlinear factors such as inflation, industrial demand, market sentiment, and economic cycles. Traditional regression models often struggle to capture these interactions effectively.

XGBoost was selected because it:

* Handles nonlinear relationships efficiently
* Reduces overfitting through regularization
* Learns complex feature interactions
* Delivers strong performance on structured/tabular datasets
* Is widely adopted in financial and business analytics applications

### Features Used

The model was trained using engineered time-series features including:

* Year
* Month
* Quarter
* 1-Month Lag
* 2-Month Lag
* 3-Month Lag
* 3-Month Rolling Average

### Key Observations

* Successfully captured nonlinear price movement patterns across multiple commodities.
* Demonstrated strong predictive performance on trend-driven metals such as Gold, Silver, Aluminium, and Nickel.
* Feature importance analysis revealed that lag variables and rolling averages contributed significantly to prediction accuracy.
* Performed better at modeling market complexity than traditional Linear Regression while providing greater interpretability than deep learning approaches.

### Business Relevance

XGBoost can support:

* Commodity demand forecasting
* Procurement cost optimization
* Investment trend analysis
* Market risk assessment
* Financial planning and budgeting

This addition extended the project from traditional regression analysis toward advanced predictive analytics and ensemble learning.
<img width="2431" height="1424" alt="image" src="https://github.com/user-attachments/assets/494ada6b-b625-46ae-bc29-f3fb45822392" />

---
---

# ⏳ ARIMA Time-Series Forecasting

To complement machine learning-based forecasting approaches, **ARIMA (AutoRegressive Integrated Moving Average)** was implemented as a dedicated time-series forecasting model.

Unlike regression and ensemble learning models that rely on engineered features, ARIMA leverages historical sequential patterns directly from the time series to forecast future commodity prices.

## 🎯 Why ARIMA?

Commodity prices exhibit temporal dependencies where historical values influence future market behavior. ARIMA was introduced to:

- Capture trend-based price movements
- Forecast future commodity prices using historical patterns
- Compare traditional time-series forecasting against machine learning approaches
- Evaluate forecasting performance across different metal categories

---

## ⚙️ Forecasting Process

### 📊 Data Preparation

- Converted commodity prices into time-series format
- Maintained chronological order of observations
- Performed train-test split without shuffling to preserve temporal integrity

### 🤖 Model Development

- Trained ARIMA models on historical commodity price data
- Generated future monthly price forecasts
- Evaluated forecasting performance using error metrics

---

## 🏭 Metals Forecasted

- Gold
- Silver
- Aluminium
- Nickel
- Uranium

---

## 🔍 Key Observations

- ARIMA successfully captured long-term price trends for relatively stable commodities.
- Gold and Silver exhibited more predictable forecasting behavior.
- Uranium remained challenging due to sudden market shocks and extreme volatility.
- Forecast accuracy varied based on market stability and commodity-specific characteristics.

---

## 📈 Business Applications

### 📦 Procurement Planning
- Forecast raw material costs and purchasing requirements.

### 💰 Commodity Budgeting
- Support budgeting and financial planning based on projected commodity prices.

### 🌍 Market Intelligence
- Identify long-term trends and anticipate market movements.

### 📊 Financial Forecasting
- Assist investors and analysts in evaluating future commodity price scenarios.

### ⚠️ Risk Management
- Monitor commodity volatility and support risk mitigation strategies.

---

## 🚀 Business Value

The addition of ARIMA expanded the project beyond machine learning-based prediction into dedicated time-series forecasting, enabling future price projections based on historical market behavior.

This provides a more comprehensive forecasting framework by combining:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Regression Modeling
- Ensemble Learning (Random Forest & XGBoost)
- Time-Series Forecasting (ARIMA)

---
# 🌐 Streamlit Deployment

To make the forecasting pipeline interactive and accessible, the project was deployed using **Streamlit**. The application enables users to analyze historical commodity price trends, generate machine learning forecasts, and perform ARIMA-based time-series forecasting through a user-friendly web interface.

---

## 🚀 Features

### 📊 Historical Analysis Dashboard

Users can:

- Visualize **30 years of historical metal price trends**
- Explore long-term market cycles
- Analyze commodity-specific volatility

#### Supported Metals

- Gold
- Silver
- Aluminium
- Nickel
- Uranium

---

### 🤖 Machine Learning Forecasting

The dashboard integrates multiple trained machine learning models:

- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

#### User Inputs

Users can provide:

- Year
- Month
- Quarter
- Lag Features
- Rolling Mean Features

The application generates **real-time commodity price predictions** using pre-trained serialized models.

---

### ⏳ ARIMA Forecasting

Traditional time-series forecasting is implemented using ARIMA.

#### Capabilities

- Future price forecasting
- Adjustable forecast horizon
- Interactive forecast visualization
- Forecast export functionality

---

### 📈 Interactive Visualizations

The dashboard leverages **Plotly** for interactive data exploration.

#### Visualizations Included

- Historical Trend Analysis
- Actual vs Predicted Comparisons
- ARIMA Forecast Visualization
- Model Performance Comparison

#### Benefits

- Interactive Zooming
- Hover Tooltips
- Dynamic Exploration
- Responsive Design

---

### 📦 Model Serialization

All trained forecasting models are serialized using **Pickle**, enabling fast deployment without retraining.

#### Serialized Models

- Linear Regression Models
- Random Forest Models
- XGBoost Models
- ARIMA Models

---

## ⚡ Dashboard Highlights

- ✅ Interactive Forecasting
- ✅ Real-Time Predictions
- ✅ Multiple Forecasting Approaches
- ✅ Model Comparison
- ✅ Downloadable Forecasts
- ✅ Business-Friendly Visualizations

---

## 💼 Business Applications

- 📦 Procurement Planning
- 💹 Investment Analysis
- ⚙️ Supply Chain Forecasting
- 📈 Commodity Market Intelligence
- 🌍 Economic Research
- 📊 Financial Risk Assessment

---

## 🎯 Deployment Outcome

The Streamlit application transforms complex forecasting workflows into an intuitive analytical platform, enabling users to explore historical trends, compare forecasting models, and generate future commodity price predictions without requiring technical expertise.
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
# 🚀 Model Serialization & Deployment Readiness

To make the forecasting system production-ready, the project was enhanced with **model serialization**, enabling trained machine learning models to be saved and reused without retraining.

This enhancement bridges the gap between model development and real-world deployment by converting forecasting models into reusable assets that can be integrated into applications, dashboards, and automated prediction systems.

---

## 📌 Why Model Serialization?

Machine learning models trained in notebooks are not directly suitable for deployment. By serializing models using **Pickle (.pkl)**, trained models can be stored and loaded whenever predictions are required.

### Benefits
- ⚡ Faster inference and prediction generation
- 💾 Reduced computational overhead
- 🔄 Consistent and reproducible predictions
- 🚀 Easy integration into web applications and dashboards
- 📈 Deployment-ready forecasting pipeline

---

## 🤖 Serialized Forecasting Models

### Linear Regression Models
- Gold Price Forecasting
- Silver Price Forecasting
- Aluminium Price Forecasting
- Nickel Price Forecasting
- Uranium Price Forecasting

### Random Forest Regressor Models
- Gold Price Forecasting
- Silver Price Forecasting
- Aluminium Price Forecasting
- Nickel Price Forecasting
- Uranium Price Forecasting

### XGBoost Regressor Models
- Gold Price Forecasting
- Silver Price Forecasting
- Aluminium Price Forecasting
- Nickel Price Forecasting
- Uranium Price Forecasting

### ARIMA Forecasting Models
- Gold Price Forecasting
- Silver Price Forecasting
- Aluminium Price Forecasting
- Nickel Price Forecasting
- Uranium Price Forecasting

---

## 🏗️ Project Architecture

```text
Historical Commodity Data
            ↓
     Data Preprocessing
            ↓
    Feature Engineering
            ↓
      Model Training
            ↓
      Model Evaluation
            ↓
 Model Serialization (.pkl)
            ↓
     Deployment Ready
            ↓
    Streamlit Application
```
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
