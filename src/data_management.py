import pandas as pd
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_kmart_dataset():
    return pd.read_csv("inputs/dataset/kmart_processed_data.csv")