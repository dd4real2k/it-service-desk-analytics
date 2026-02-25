import streamlit as st
import pandas as pd
import joblib

st.title("IT Service Desk Analytics")

vol_model = joblib.load("ticket_volume_model.joblib")
sla_model = joblib.load("sla_model.joblib")

st.header("Ticket Volume Prediction")
dow = st.selectbox("Day of Week (0=Mon)", list(range(7)))
month = st.selectbox("Month", list(range(1,13)))

input_vol = pd.DataFrame([{
    "day_of_week": dow,
    "month": month
}])

pred_vol = vol_model.predict(input_vol)[0]
st.metric("Predicted Tickets", f"{pred_vol:.0f}")

st.header("SLA Breach Risk Prediction")

hour = st.slider("Hour of Day", 0, 23)

input_sla = pd.DataFrame([{
    "hour": hour,
    "day_of_week": dow
}])

risk = sla_model.predict_proba(input_sla)[0,1]
st.metric("Breach Risk", f"{risk*100:.1f}%")