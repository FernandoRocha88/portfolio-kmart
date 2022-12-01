import streamlit as st
from src.insights_content import insights_pricing, insights_product, insights_customer_behaviour

st.set_page_config(page_title="Insights and Recommendations", page_icon="📌")


st.write("#### 📌 Insights and Recommendations \n ---")

insights_topics = [
            "Pricing",
            "Product",
            "Customer Behaviour"
            ]
tab1, tab2, tab3 = st.tabs(insights_topics)

with tab1: insights_pricing()
with tab2: insights_product()
with tab3: insights_customer_behaviour()
