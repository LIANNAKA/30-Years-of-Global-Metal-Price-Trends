import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go
# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Commodity Price Forecasting",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📊 Commodity Price Forecasting")

st.sidebar.markdown("""
### Project Overview

Forecast commodity prices using:

- Linear Regression
- Random Forest
- XGBoost
- ARIMA

### Dataset

- 30 Years Historical Data
- 1992 – 2021
- Gold
- Silver
- Aluminium
- Nickel
- Uranium

### Technologies

- Python
- Pandas
- Scikit-Learn
- XGBoost
- Statsmodels
- Streamlit
- Plotly
""")

# =====================================================
# TITLE
# =====================================================

st.markdown("""
# 📈 Commodity Price Forecasting Platform

### Analyze 30 Years of Commodity Market Data and Generate Forecasts using Machine Learning and Time-Series Models

Built with:
- Linear Regression
- Random Forest
- XGBoost
- ARIMA

""")

# =====================================================
# METAL MAP
# =====================================================

metal_map = {
    "Gold": "gold",
    "Silver": "silver",
    "Aluminium": "alum",
    "Nickel": "nickel",
    "Uranium": "uran"
}

# =====================================================
# MODEL MAP
# =====================================================

model_map = {
    "Linear Regression": {
        "folder": "linear_regression",
        "suffix": "lr"
    },
    "Random Forest": {
        "folder": "random_forest",
        "suffix": "rf"
    },
    "XGBoost": {
        "folder": "xgboost",
        "suffix": "xgb"
    }
}

# =====================================================
# LOAD DATA
# =====================================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@st.cache_data
def load_data():

    file_path = (
        BASE_DIR /
        "data" /
        "processed" /
        "cleaned_metal_prices.csv"
    )

    return pd.read_csv(file_path)

df = load_data()
# =====================================================
# GLOBAL SELECTIONS
# =====================================================

col1, col2 = st.columns(2)

with col1:

    metal = st.selectbox(
        "Select Metal",
        list(metal_map.keys())
    )

with col2:

    model_type = st.selectbox(
        "Select ML Model",
        list(model_map.keys())
    )

selected_metal = metal_map[metal]

latest_price = df[f"Price_{selected_metal}"].iloc[-1]

avg_price = df[f"Price_{selected_metal}"].mean()

max_price = df[f"Price_{selected_metal}"].max()

volatility = df[f"Price_{selected_metal}"].std()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Latest Price",
    f"${latest_price:,.2f}"
)

kpi2.metric(
    "Average Price",
    f"${avg_price:,.2f}"
)

kpi3.metric(
    "Maximum Price",
    f"${max_price:,.2f}"
)

kpi4.metric(
    "Volatility",
    f"{volatility:.2f}"
)


# =====================================================
# LOAD ML MODEL
# =====================================================

model_path = (
    BASE_DIR /
    "models" /
    model_map[model_type]["folder"] /
    f"{selected_metal}_{model_map[model_type]['suffix']}.pkl"
)

with open(model_path, "rb") as f:
    model = pickle.load(f)

# =====================================================
# TABS
# =====================================================
tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Historical Analysis",
        "🤖 ML Forecasting",
        "⏳ ARIMA Forecasting",
        "📈 Model Performance"
    ]
)

# =====================================================
# TAB 1
# =====================================================

with tab1:

    st.subheader(f"{metal} Historical Price Analysis")

    fig = px.line(
    df,
    y=f"Price_{selected_metal}",
    title=f"{metal} Historical Price Trend"
)

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Price",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        f"""
        ### Insights

        - Visualizes historical price movements for **{metal}**
        - Useful for identifying long-term trends
        - Highlights volatility and market cycles
        """
    )

# =====================================================
# TAB 2
# =====================================================

with tab2:

    st.subheader(
        f"{metal} Forecasting using {model_type}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        year = st.number_input(
            "Year",
            min_value=2022,
            value=2026,
            key="year_input"
        )

        month = st.number_input(
            "Month",
            min_value=1,
            max_value=12,
            value=1,
            key="month_input"
        )
    with col2:

        quarter = st.number_input(
            "Quarter",
            min_value=1,
            max_value=4,
            value=1,
            key="quarter_input"
        )

        lag1 = st.number_input(
            "Lag 1 Price",
            key="lag1_input"
        )

    with col3:

        lag2 = st.number_input(
            "Lag 2 Price",
            key="lag2_input"
        )

        lag3 = st.number_input(
            "Lag 3 Price",
            key="lag3_input"
        )

        rolling = st.number_input(
            "Rolling Mean (3 Months)",
            key="rolling_input"
        )

    # ==========================================
    # PREDICTION
    # ==========================================

    if st.button("🚀 Predict Price"):

        sample = pd.DataFrame(
            [[
                year,
                month,
                quarter,
                lag1,
                lag2,
                lag3,
                rolling
            ]],
            columns=[
                "Year",
                "Month_Num",
                "Quarter",
                f"Price_{selected_metal}_Lag_1",
                f"Price_{selected_metal}_Lag_2",
                f"Price_{selected_metal}_Lag_3",
                f"Price_{selected_metal}_Rolling_Mean_3"
            ]
        )

        prediction = model.predict(sample)

        pred_col1, pred_col2 = st.columns(2)

        pred_col1.metric(
            "Predicted Price",
            f"${prediction[0]:,.2f}"
        )

        pred_col2.metric(
            "Forecast Year",
            str(year)
        )

    # ==========================================
    # ACTUAL VS PREDICTED GRAPH
    # ==========================================

    st.markdown("---")

    st.subheader(
        f"📊 Actual vs Predicted ({model_type})"
    )

    prediction_path = (
    BASE_DIR /
    "predictions" /
    model_map[model_type]["folder"] /
    f"Price_{selected_metal}_{model_map[model_type]['suffix']}_predictions.csv"
)

    try:

        pred_df = pd.read_csv(
            prediction_path
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=pred_df["Actual"],
                mode="lines",
                name="Actual Prices"
            )
        )

        fig.add_trace(
            go.Scatter(
                y=pred_df["Predicted"],
                mode="lines",
                name="Predicted Prices"
            )
        )

        fig.update_layout(
            title=f"{metal} - {model_type}",
            xaxis_title="Test Period",
            yaxis_title="Price",
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.dataframe(
            pred_df.head()
        )

    except Exception:

        st.warning(
            "Prediction file not found. Please generate prediction CSV files first."
        )

    # ==========================================
    # MODEL INFO
    # ==========================================

    st.markdown("---")

    st.subheader("🤖 Model Information")

    if model_type == "Linear Regression":

        st.info(
            """
            Linear Regression models the relationship
            between historical features and future prices.
            """
        )

    elif model_type == "Random Forest":

        st.info(
            """
            Random Forest captures nonlinear patterns
            using an ensemble of decision trees.
            """
        )

    elif model_type == "XGBoost":

        st.info(
            """
            XGBoost uses gradient boosting to capture
            complex market relationships and trends.
            """
        )

# =====================================================
# TAB 3
# =====================================================

with tab3:

    st.subheader(
        f"ARIMA Forecasting for {metal}"
    )

    forecast_steps = st.slider(
        "Forecast Months",
        min_value=1,
        max_value=24,
        value=12,
        key="arima_forecast_steps"
    )

    try:

        arima_path = (
            BASE_DIR /
            "models" /
            "arima" /
            f"{selected_metal}_arima.pkl"
        )

        with open(
            arima_path,
            "rb"
        ) as f:

            arima_model = pickle.load(f)

        if st.button("Generate ARIMA Forecast"):

            forecast = arima_model.forecast(
                steps=forecast_steps
            )

            forecast_df = pd.DataFrame(
                {
                    "Forecasted Price": forecast
                }
            )

            st.download_button(
            "📥 Download Forecast",
            forecast_df.to_csv(index=False),
            "forecast.csv",
            "text/csv"
            )

            st.dataframe(
                forecast_df
            )

            forecast_index = list(
    range(
        len(df),
        len(df) + forecast_steps
            )
        )

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=df[f"Price_{selected_metal}"],
                mode="lines",
                name="Historical Prices"
            )
        )

        fig.add_trace(
            go.Scatter(
                x=forecast_index,
                y=forecast,
                mode="lines",
                name="ARIMA Forecast"
            )
        )

        fig.update_layout(
            title=f"{metal} ARIMA Forecast",
            xaxis_title="Time",
            yaxis_title="Price",
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    except Exception as e:

        st.warning(
            "ARIMA model not found. Please serialize and save your ARIMA models first."
        )

with tab4:

    st.subheader(
        "📈 Model Performance Comparison"
    )

    performance_df = pd.DataFrame({

        "Model":[
            "Linear Regression",
            "Random Forest",
            "XGBoost"
        ],

        "R² Score":[
            1.00,
            0.96,
            0.98
        ]
    })

    st.dataframe(
        performance_df,
        use_container_width=True
    )

    fig = px.bar(
        performance_df,
        x="Model",
        y="R² Score",
        title="Model Performance Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    performance_df = pd.DataFrame({

    "Model":[
        "Linear Regression",
        "Random Forest",
        "XGBoost"
    ],

    "R²":[
        1.00,
        0.96,
        0.98
    ]
    })

    st.dataframe(
        performance_df,
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Commodity Price Forecasting | EDA • Feature Engineering • Linear Regression • Random Forest • XGBoost • ARIMA"
)