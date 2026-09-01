import streamlit as st
import pandas as pd
import joblib

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="🏢",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "data/processed/business_intelligence_data.csv"
)

model = joblib.load(
    "models/churn_prediction_model.pkl"
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("🏢 AI Business Intelligence")
st.sidebar.caption("Decision Support Platform")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Dashboard",
        "Customer Intelligence",
        "Risk Intelligence",
        "Revenue Intelligence",
        "Churn Analytics",
        "AI Decision Support"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "AI-powered analytics platform for customer intelligence, "
    "churn prediction and business decision support."
)

# ==================================================
# HEADER
# ==================================================

st.title(
    "AI-Powered Business Intelligence & Decision Support Platform"
)

st.caption(
    "Customer Analytics | Churn Prediction | "
    "Risk Intelligence | Decision Support"
)

st.divider()


# ==================================================
# EXECUTIVE DASHBOARD
# ==================================================

if page == "Executive Dashboard":

    st.header("🏠 Executive Dashboard")

    total_customers = df["customerID"].nunique()
    churned_customers = (df["Churn"] == "Yes").sum()
    churn_rate = df["Churn_Encoded"].mean() * 100
    avg_monthly_charges = df["MonthlyCharges"].mean()
    total_revenue = df["TotalCharges"].sum()
    high_risk_customers = (
        df["Risk_Level"] == "High"
    ).sum()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "Churned Customers",
        f"{churned_customers:,}"
    )

    col3.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Average Monthly Charges",
        f"${avg_monthly_charges:.2f}"
    )

    col5.metric(
        "Total Revenue",
        f"${total_revenue:,.0f}"
    )

    col6.metric(
        "High Risk Customers",
        f"{high_risk_customers:,}"
    )

    st.divider()

    st.subheader("📊 Churn Analytics")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### Churn Rate by Contract")

        contract_churn = (
            df.groupby("Contract")["Churn_Encoded"]
            .mean()
            .mul(100)
            .round(2)
        )

        st.bar_chart(contract_churn)

    with col2:

        st.write("### Churn Rate by Internet Service")

        internet_churn = (
            df.groupby("InternetService")["Churn_Encoded"]
            .mean()
            .mul(100)
            .round(2)
        )

        st.bar_chart(internet_churn)

    st.divider()

    st.subheader("⚠️ Customer Risk Distribution")

    risk_distribution = (
        df["Risk_Level"]
        .value_counts()
        .reindex(["High", "Medium", "Low"])
        .fillna(0)
    )

    st.bar_chart(risk_distribution)


# ==================================================
# CUSTOMER INTELLIGENCE
# ==================================================

elif page == "Customer Intelligence":

    st.header("👥 Customer Intelligence")

    customer_ids = (
        df["customerID"]
        .astype(str)
        .tolist()
    )

    selected_customer = st.selectbox(
        "🔎 Select Customer ID",
        customer_ids
    )

    customer = df[
        df["customerID"].astype(str)
        == selected_customer
    ].iloc[0]

    st.divider()

    st.subheader("👤 Customer Profile")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Customer ID",
        customer["customerID"]
    )

    col2.metric(
        "Tenure",
        f"{int(customer['tenure'])} months"
    )

    col3.metric(
        "Monthly Charges",
        f"${customer['MonthlyCharges']:.2f}"
    )

    col4.metric(
        "Contract",
        customer["Contract"]
    )

    st.divider()

    st.subheader("📋 Customer Services")

    col1, col2, col3 = st.columns(3)

    col1.write(
        f"**Internet Service:** "
        f"{customer['InternetService']}"
    )

    col2.write(
        f"**Phone Service:** "
        f"{customer['PhoneService']}"
    )

    col3.write(
        f"**Payment Method:** "
        f"{customer['PaymentMethod']}"
    )

    st.divider()

    st.subheader("🤖 AI Churn Intelligence")

    churn_probability = float(
        customer.get("Churn_Probability", 0)
    )

    risk_level = customer.get(
        "Risk_Level",
        "Unknown"
    )

    actual_churn = customer.get(
        "Churn",
        "Unknown"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Churn Probability",
        f"{churn_probability * 100:.2f}%"
    )

    col2.metric(
        "Risk Level",
        risk_level
    )

    col3.metric(
        "Actual Churn",
        actual_churn
    )

    st.divider()

    st.subheader("💡 Recommended Action")

    if risk_level == "High":

        st.error(
            "🔴 High Risk: Prioritize this customer for "
            "proactive retention and targeted incentives."
        )

    elif risk_level == "Medium":

        st.warning(
            "🟡 Medium Risk: Monitor customer behavior and "
            "consider personalized engagement."
        )

    else:

        st.success(
            "🟢 Low Risk: Continue normal customer engagement."
        )


# ==================================================
# RISK INTELLIGENCE
# ==================================================

elif page == "Risk Intelligence":

    st.header("⚠️ Risk Intelligence")

    st.write(
        "AI-powered customer risk monitoring and prioritization."
    )

    high_risk = (
        df["Risk_Level"] == "High"
    ).sum()

    medium_risk = (
        df["Risk_Level"] == "Medium"
    ).sum()

    low_risk = (
        df["Risk_Level"] == "Low"
    ).sum()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🔴 High Risk",
        f"{high_risk:,}"
    )

    col2.metric(
        "🟡 Medium Risk",
        f"{medium_risk:,}"
    )

    col3.metric(
        "🟢 Low Risk",
        f"{low_risk:,}"
    )

    st.divider()

    st.subheader("📊 Risk Distribution")

    risk_data = pd.DataFrame(
        {
            "Customers": [
                high_risk,
                medium_risk,
                low_risk
            ]
        },
        index=[
            "High",
            "Medium",
            "Low"
        ]
    )

    st.bar_chart(risk_data)

    st.divider()

    st.subheader("🔴 High-Risk Customers")

    high_risk_df = df[
        df["Risk_Level"] == "High"
    ].copy()

    columns = [
        "customerID",
        "Contract",
        "InternetService",
        "tenure",
        "MonthlyCharges",
        "Churn_Probability",
        "Risk_Level"
    ]

    st.dataframe(
        high_risk_df[columns].head(100),
        width="stretch",
        hide_index=True
    )

    csv_data = high_risk_df[
        columns
    ].to_csv(index=False)

    st.download_button(
        "📥 Download High-Risk Customer Report",
        csv_data,
        "high_risk_customers.csv",
        "text/csv"
    )


# ==================================================
# REVENUE INTELLIGENCE
# ==================================================

elif page == "Revenue Intelligence":

    st.header("💰 Revenue Intelligence")

    st.write(
        "Revenue performance analysis across contracts, "
        "internet services and customer segments."
    )

    total_revenue = df["TotalCharges"].sum()

    average_customer_value = (
        df["TotalCharges"].mean()
    )

    average_monthly_charges = (
        df["MonthlyCharges"].mean()
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.0f}"
    )

    col2.metric(
        "💵 Average Customer Value",
        f"${average_customer_value:,.2f}"
    )

    col3.metric(
        "📅 Average Monthly Charges",
        f"${average_monthly_charges:,.2f}"
    )

    st.divider()

    st.subheader("📄 Revenue by Contract")

    revenue_contract = (
        df.groupby("Contract")["TotalCharges"]
        .sum()
        .sort_values(ascending=False)
        .round(2)
    )

    st.bar_chart(revenue_contract)

    contract_table = (
        df.groupby("Contract")
        .agg(
            Customers=("customerID", "count"),
            Total_Revenue=("TotalCharges", "sum"),
            Average_Revenue=("TotalCharges", "mean"),
            Churn_Rate=("Churn_Encoded", "mean")
        )
        .reset_index()
    )

    contract_table["Churn_Rate"] = (
        contract_table["Churn_Rate"] * 100
    ).round(2)

    contract_table["Total_Revenue"] = (
        contract_table["Total_Revenue"]
        .round(2)
    )

    contract_table["Average_Revenue"] = (
        contract_table["Average_Revenue"]
        .round(2)
    )

    st.dataframe(
        contract_table,
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.subheader("🌐 Revenue by Internet Service")

    revenue_internet = (
        df.groupby("InternetService")["TotalCharges"]
        .sum()
        .sort_values(ascending=False)
        .round(2)
    )

    st.bar_chart(revenue_internet)

    internet_table = (
        df.groupby("InternetService")
        .agg(
            Customers=("customerID", "count"),
            Total_Revenue=("TotalCharges", "sum"),
            Average_Monthly_Charges=("MonthlyCharges", "mean"),
            Churn_Rate=("Churn_Encoded", "mean")
        )
        .reset_index()
    )

    internet_table["Churn_Rate"] = (
        internet_table["Churn_Rate"] * 100
    ).round(2)

    internet_table["Total_Revenue"] = (
        internet_table["Total_Revenue"]
        .round(2)
    )

    internet_table["Average_Monthly_Charges"] = (
        internet_table["Average_Monthly_Charges"]
        .round(2)
    )

    st.dataframe(
        internet_table,
        width="stretch",
        hide_index=True
    )

    st.divider()

    st.subheader("💡 Revenue Business Insights")

    highest_revenue_contract = (
        revenue_contract.idxmax()
    )

    highest_revenue_internet = (
        revenue_internet.idxmax()
    )

    st.info(
        f"📄 **{highest_revenue_contract}** contract "
        "generates the highest total revenue."
    )

    st.info(
        f"🌐 **{highest_revenue_internet}** internet service "
        "generates the highest total revenue."
    )

    st.warning(
        "⚠️ Revenue should be evaluated together with churn. "
        "High-revenue segments with high churn can represent "
        "major retention opportunities."
    )


# ==================================================
# CHURN ANALYTICS
# ==================================================

elif page == "Churn Analytics":

    st.header("📊 Churn Analytics")

    st.subheader("Churn Rate by Contract")

    contract_churn = (
        df.groupby("Contract")["Churn_Encoded"]
        .mean()
        .mul(100)
        .round(2)
    )

    st.bar_chart(contract_churn)

    st.subheader("Churn Rate by Internet Service")

    internet_churn = (
        df.groupby("InternetService")["Churn_Encoded"]
        .mean()
        .mul(100)
        .round(2)
    )

    st.bar_chart(internet_churn)


# ==================================================
# AI DECISION SUPPORT
# ==================================================

elif page == "AI Decision Support":

    st.header("🤖 AI Decision Support")

    st.write(
        "Machine learning powered business recommendations "
        "for customer retention and revenue protection."
    )

    st.divider()

    # ==========================================
    # BUSINESS METRICS
    # ==========================================

    total_customers = len(df)

    high_risk = (
        df["Risk_Level"] == "High"
    ).sum()

    medium_risk = (
        df["Risk_Level"] == "Medium"
    ).sum()

    churned = (
        df["Churn_Encoded"] == 1
    ).sum()

    total_revenue = df["TotalCharges"].sum()

    # ==========================================
    # TOP DECISION KPIs
    # ==========================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

    col2.metric(
        "🔴 High Risk",
        f"{high_risk:,}"
    )

    col3.metric(
        "⚠️ Churned Customers",
        f"{churned:,}"
    )

    col4.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.0f}"
    )

    st.divider()

    # ==========================================
    # PRIORITY ACTIONS
    # ==========================================

    st.subheader("🎯 Priority Business Actions")

    st.error(
        f"🔴 **Priority 1 — High-Risk Customers:** "
        f"{high_risk:,} customers should be prioritized "
        "for proactive retention campaigns."
    )

    st.warning(
        "📄 **Priority 2 — Contract Strategy:** "
        "Month-to-month customers show substantially higher "
        "churn. Encourage migration to one-year or two-year "
        "contracts using targeted offers."
    )

    st.warning(
        "🌐 **Priority 3 — Fiber Optic Segment:** "
        "Fiber optic customers have elevated churn. "
        "Investigate pricing, service quality and support "
        "experience."
    )

    st.info(
        "💰 **Priority 4 — Revenue Protection:** "
        "Focus retention resources on high-risk customers "
        "with meaningful customer value."
    )

    st.divider()

    # ==========================================
    # CONTRACT DECISION
    # ==========================================

    st.subheader("📄 Contract Strategy")

    contract_analysis = (
        df.groupby("Contract")
        .agg(
            Customers=("customerID", "count"),
            Churn_Rate=("Churn_Encoded", "mean"),
            Revenue=("TotalCharges", "sum")
        )
        .reset_index()
    )

    contract_analysis["Churn_Rate"] = (
        contract_analysis["Churn_Rate"] * 100
    ).round(2)

    contract_analysis["Revenue"] = (
        contract_analysis["Revenue"]
        .round(2)
    )

    st.dataframe(
        contract_analysis,
        width="stretch",
        hide_index=True
    )

    highest_churn_contract = (
        contract_analysis
        .sort_values("Churn_Rate", ascending=False)
        .iloc[0]["Contract"]
    )

    highest_churn_rate = (
        contract_analysis
        .sort_values("Churn_Rate", ascending=False)
        .iloc[0]["Churn_Rate"]
    )

    st.info(
        f"💡 **AI Recommendation:** "
        f"Prioritize retention campaigns for "
        f"**{highest_churn_contract}** customers, "
        f"where churn is approximately "
        f"**{highest_churn_rate:.2f}%**."
    )

    st.divider()

    # ==========================================
    # INTERNET SERVICE DECISION
    # ==========================================

    st.subheader("🌐 Internet Service Strategy")

    internet_analysis = (
        df.groupby("InternetService")
        .agg(
            Customers=("customerID", "count"),
            Churn_Rate=("Churn_Encoded", "mean"),
            Revenue=("TotalCharges", "sum")
        )
        .reset_index()
    )

    internet_analysis["Churn_Rate"] = (
        internet_analysis["Churn_Rate"] * 100
    ).round(2)

    internet_analysis["Revenue"] = (
        internet_analysis["Revenue"]
        .round(2)
    )

    st.dataframe(
        internet_analysis,
        width="stretch",
        hide_index=True
    )

    highest_internet_churn = (
        internet_analysis
        .sort_values("Churn_Rate", ascending=False)
        .iloc[0]
    )

    st.info(
        f"💡 **AI Recommendation:** "
        f"The **{highest_internet_churn['InternetService']}** "
        f"segment has the highest churn rate "
        f"({highest_internet_churn['Churn_Rate']:.2f}%). "
        "Review pricing, service quality and customer support "
        "for this segment."
    )

    st.divider()

    # ==========================================
    # HIGH VALUE RISK CUSTOMERS
    # ==========================================

    st.subheader("💎 High-Value Customers at Risk")

    if "Customer_Value" in df.columns:

        high_value_risk = df[
            (df["Risk_Level"] == "High")
        ].sort_values(
            "Customer_Value",
            ascending=False
        )

        columns = [
            "customerID",
            "Contract",
            "InternetService",
            "tenure",
            "MonthlyCharges",
            "Customer_Value",
            "Churn_Probability",
            "Risk_Level"
        ]

        available_columns = [
            col for col in columns
            if col in high_value_risk.columns
        ]

        st.dataframe(
            high_value_risk[
                available_columns
            ].head(20),
            width="stretch",
            hide_index=True
        )

        st.success(
            "🎯 Recommended Strategy: "
            "Prioritize high-risk customers with high "
            "customer value for personalized retention."
        )

    else:

        st.info(
            "Customer Value information is not available "
            "in the current processed dataset."
        )

    st.divider()

    # ==========================================
    # FINAL EXECUTIVE RECOMMENDATION
    # ==========================================

    st.subheader("🧠 Executive AI Recommendation")

    st.success(
        "The recommended strategy is to combine ML-based "
        "customer risk scoring with business segmentation. "
        "Prioritize high-risk customers, encourage long-term "
        "contracts, investigate high-churn service segments, "
        "and protect high-value customers through targeted "
        "retention campaigns."
    )

    st.caption(
        "Decision Support System • Machine Learning Powered"
    )