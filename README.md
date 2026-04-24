# IT Service Desk Analytics System

## 🚀 Project Summary
Built a data-driven analytics system to forecast IT support demand and predict SLA breaches using machine learning, enabling proactive incident management and improved service desk efficiency.

---

## 📌 Problem
IT service desks handle high volumes of support tickets daily, making it difficult to:
- Predict workload demand
- Maintain SLA compliance
- Allocate resources efficiently

Poor visibility into ticket patterns can lead to delays, SLA breaches, and reduced user satisfaction.

---

## 🎯 Objective
To build a system that:
- Forecasts ticket volume for workforce planning
- Predicts SLA breach risk for proactive escalation
- Identifies key drivers of service desk demand

---

## 📊 Dataset
Historical IT service desk ticket data including:
- Ticket creation time
- Category / issue type
- Priority level
- Resolution time
- SLA status (met / breached)

---

## 🔍 Approach

### 1) Exploratory Data Analysis (EDA)
- Identified peak ticket periods (hourly and daily trends)
- Analysed ticket distribution by category and priority
- Evaluated SLA performance across time and issue types

### 2) Ticket Volume Prediction (Regression)
- Model: Random Forest Regressor
- Reason: Handles non-linear patterns and feature interactions effectively
- Output: Predicted daily ticket volume

### 3) SLA Breach Prediction (Classification)
- Model: Logistic Regression / XGBoost
- Reason: Strong performance on classification tasks with imbalanced data
- Output: Probability of SLA breach

---

## 📈 Results

- SLA breach prediction accuracy: ~80–85%
- Identified key SLA risk drivers:
  - High priority tickets
  - Specific issue categories
  - Peak workload periods

- Improved ability to detect high-risk tickets early
- Enabled better workload forecasting for staffing decisions

---

## 🛠 Tech Stack
- **Python** (Pandas, NumPy, Scikit-learn)
- **SQL** (data extraction & querying)
- **Power BI / Streamlit** (dashboard & visualisation)
- **Matplotlib / Seaborn** (EDA)

---

## 📸 Demo

![Dashboard](images/app_home.png)
![Prediction Example](images/app_example.png)

---

## 💼 Business Impact
This system helps IT teams to:

- 📉 Reduce SLA breaches through early risk detection
- 👥 Optimise staffing using demand forecasting
- ⚡ Improve response times during peak periods
- 🔍 Identify recurring incident patterns for process improvement

---

## 🧠 Domain Insight
This project is inspired by real-world IT support experience, where understanding ticket patterns and SLA risks is critical for maintaining service quality and meeting operational targets.

---

## 🚀 Future Improvements
- Real-time ticket streaming integration
- Deployment as a REST API using FastAPI
- Advanced models (XGBoost / LSTM)
- Integration with ITSM platforms (e.g. ServiceNow)

---

## 👨‍💻 Author
Daniel Diala
GitHub: https://github.com/dd4real2k
