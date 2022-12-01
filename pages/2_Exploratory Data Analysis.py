import streamlit as st
st.set_page_config(page_title="Exploratory Data Analysis", page_icon="🔎")
from src.eda_page_content import (
                                    eda_overall_results,
                                    eda_patterns_over_time, 
                                    eda_product_region_performance,
                                    eda_product_basket_analysis,
                                    eda_customer_behaviour
                                    )


st.write("#### 🔎 Exploratory Data Analysis \n ---")
st.write(
        """
        * Note: Please visit [Tableau App](https://public.tableau.com/app/profile/fernando.doreto/viz/kmart/UseCases?publish=yes) 
            and [repo notebooks](https://github.com/FernandoRocha88/portfolio-kmart) 
            to investigate the data and better understand how the information below was derived.
        """)


eda_topics = [
            "Overall Results",
            "Patterns over time",
            "Product/Region Performance",
            "Product Basket Analysis",
            "Customer Behaviour"
            ]
tab1, tab2, tab3, tab4, tab5 = st.tabs(eda_topics)

with tab1: eda_overall_results()
with tab2: eda_patterns_over_time()
with tab3: eda_product_region_performance()
with tab4: eda_product_basket_analysis()
with tab5: eda_customer_behaviour()