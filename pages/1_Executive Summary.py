import streamlit as st

st.set_page_config(page_title="Executive Summary", page_icon="📑")
st.write("#### 📑 Executive Summary \n ---")

exec_summary_text = """
    * In 2019 
        * Product Margin of **58% (20M$)**, 
        * 140k customers, 178k orders, **208k products** sold
        * 90% of time, a customer brings a margin up to $400
        * Result is driven by products (**laptop and mobile**) that are not bought recurrently 

    * **13% of customer base** buys orders with more than 1 product
        * Typically include product lines from mobile, Cable/Access and Audio

    * **22% of customer base** is recurrent
        * A recurrent customer is typically buying across Audio and Cable/Access

    * There are **multiple business opportunities** around pricing (based on demand) and product (up-sell, cross-sell) and **1 risk** around product portfolio dependency

    """
st.warning("Visit Insights and Recommendations page for additional details and explanations")
st.info(exec_summary_text)
