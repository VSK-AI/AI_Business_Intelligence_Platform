# 🤖 AI-Powered Business Intelligence & Decision Support Platform

An end-to-end **AI-powered Business Intelligence platform** for customer analytics, churn prediction, customer risk intelligence, revenue analysis, and data-driven business decision support.

## 📌 Project Overview

This project analyzes customer behavior and business performance using **Machine Learning and Business Intelligence techniques**.

The platform helps businesses:

* Identify customers likely to churn
* Classify customers into High, Medium, and Low risk
* Analyze churn across different customer segments
* Understand revenue performance
* Identify high-value customers at risk
* Generate actionable retention recommendations
* Monitor business KPIs through an interactive Streamlit dashboard

## 🎯 Key Features

### 👥 Customer Analytics

* Customer-level profiling
* Tenure and monthly charge analysis
* Contract and internet service segmentation
* Customer behavior analysis

### 📉 Churn Prediction

* Machine Learning based churn prediction
* Customer churn probability scoring
* Churn risk classification
* Model-driven customer prioritization

### ⚠️ Risk Intelligence

Customers are categorized into:

* 🔴 High Risk
* 🟡 Medium Risk
* 🟢 Low Risk

High-risk customers are prioritized for proactive retention strategies.

### 💰 Revenue Intelligence

The platform analyzes:

* Total revenue
* Average customer value
* Average monthly charges
* Revenue by contract
* Revenue by internet service
* Revenue vs. churn patterns

### 🤖 AI Decision Support

The system converts analytical results into business recommendations such as:

* Prioritizing high-risk customers
* Encouraging long-term contracts
* Investigating high-churn service segments
* Protecting high-value customers
* Designing targeted retention campaigns

### 📊 Interactive Dashboard

The application is built using **Streamlit** and provides an interactive business intelligence dashboard containing:

* Executive Dashboard
* Churn Analytics
* Customer Profile
* Risk Intelligence
* Revenue Intelligence
* AI Decision Support

## 📊 Business Results

Current analysis contains **7,043 customers**.

| Metric                  |       Value |
| ----------------------- | ----------: |
| Total Customers         |       7,043 |
| Churned Customers       |       1,869 |
| Churn Rate              |      26.54% |
| Average Monthly Charges |      $64.76 |
| Total Revenue           | $16,056,169 |
| High-Risk Customers     |         949 |

### Key Business Insights

* **Month-to-month customers** have the highest churn rate at approximately **42.71%**.
* **Fiber optic customers** have the highest churn rate at approximately **41.89%**.
* Long-term contracts show substantially lower churn.
* High-risk customers should receive proactive retention strategies.
* High-value customers with elevated churn probability represent important revenue-protection opportunities.

## 🧠 Machine Learning Workflow

```text
Raw Customer Data
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Data Preprocessing
       ↓
Machine Learning Model
       ↓
Churn Probability
       ↓
Risk Classification
       ↓
Business Intelligence
       ↓
AI Decision Support
       ↓
Streamlit Dashboard
```

## 🛠️ Technology Stack

### Programming

* Python
* SQL

### Data Science

* Pandas
* NumPy
* Scikit-learn
* Matplotlib

### Machine Learning

* Classification
* Churn Prediction
* Risk Scoring
* Feature Engineering

### Business Intelligence

* Customer Segmentation
* Revenue Analytics
* KPI Analysis
* Business Decision Support

### Deployment / Dashboard

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

## 📁 Project Structure

```text
AI_Business_Intelligence_Platform/
│
├── app.py
├── 01_customer_churn_analysis.ipynb
├── requirements.txt
├── README.md
│
├── data/
│   ├── Telco-Customer-Churn.csv
│   └── processed/
│       ├── business_intelligence_data.csv
│       └── high_risk_customers.csv
│
└── models/
    └── churn_prediction_model.pkl
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/VSK-AI/AI_Business_Intelligence_Platform.git
```

Navigate to the project:

```bash
cd AI_Business_Intelligence_Platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 📓 Jupyter Notebook

The notebook:

```text
01_customer_churn_analysis.ipynb
```

contains the analytical and Machine Learning workflow used to develop the project, including data analysis, preprocessing, feature engineering, model development, evaluation, and customer risk analysis.

## 💼 Business Value

This platform demonstrates how **Machine Learning can be converted into actionable business intelligence**.

Instead of only predicting which customers may churn, the system helps answer:

> **Who is at risk, why they may be at risk, and what business action should be taken?**

This enables businesses to focus retention efforts on the customers and segments that matter most.

## 🚀 Future Improvements

* Real-time customer risk monitoring
* Advanced explainable AI using SHAP
* Automated retention campaign generation
* LLM-powered business analyst assistant
* RAG-based business knowledge assistant
* Agentic AI for automated decision workflows
* Cloud deployment using AWS/Azure
* Real-time data pipeline integration

## 👨‍💻 Author

**Vishal Kashyap**

AI / Machine Learning / Data Science

---

⭐ If you find this project useful, consider giving the repository a star.
