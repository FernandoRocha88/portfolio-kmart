import streamlit as st 
import pandas as pd
from src.home_page_content import home_page_text
from src.data_management import load_kmart_dataset
from config.hide_default_button_icon import hide_default_format
st.set_page_config(page_title="Customer Insights and Sales Strategy Recommendation", page_icon="🛒")#,layout="wide")
st.markdown(hide_default_format, unsafe_allow_html=True)

# load data and utils to be shared across application
st.session_state['data_frame'] = load_kmart_dataset()

def run():
    home_page_text()


if __name__ == "__main__":
    run()