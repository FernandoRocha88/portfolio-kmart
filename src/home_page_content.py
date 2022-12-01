import streamlit as st

def home_page_text():

    st.write("#### 🛒 Customer Insights and Sales Strategy Recommendation \n ---")

    st.info(
        """
        Welcome to **Customer Insights and Sales Strategy Recommendation** App using Kmart dataset!
        * The analysis combines Python and Tableau. 
        * You may click [here to access the repo](https://github.com/FernandoRocha88/portfolio-kmart) 
            with the notebooks to collect and explore the data 
            and [here to access the Tableau App](https://public.tableau.com/app/profile/fernando.doreto/viz/kmart/UseCases?publish=yes). 
            These are used to evaluate the dataset and derive insights.
        """)

    with st.expander("Kmart Dataset"):
        st.info(dataset_text)
        df = st.session_state['data_frame']
        st.write("Find below a data snapshot")
        st.write(df.head(7))

    with st.expander("Business Requirements"):
        st.success(biz_requirements_text)

    with st.expander("Roadmap"):
        st.warning(roadmap_text)


dataset_text = """
    * [Kmart](https://en.wikipedia.org/wiki/Kmart) is an online and in-store retailer in the US. 
        * The raw data is provided by this [GitHub repo](https://github.com/jsc1535/K-Mart-Data-Analysis). 
            Once data is collected and processed, it contains **185k rows** showing sales levels in 2019
    * Each row is product quantity bought in an order. A customer order is made by a set of products. The sum of orders represents the total sales
    * The data is broke down by:
        * product name, product line, product quantity
        * order date, order id
        * product unitary price/cost
        * product revenue/cost/margin
        * customer address
    """


biz_requirements_text = """
    * We are interested in analyzing Kmart results, so the business can:
        * 1 - Understand **Overall Results and Patterns**, in terms of Margin, Revenue, # Orders, # Customers, over time or across different products/regions. 
        * 2 - Discuss **business strategies and recommendations**, based on previous agreed questions around **product, pricing and customer behaviour**.


    """

roadmap_text = """
    * 1 - Develop a **Monitoring Panel**  at Tableau
        * Upper section: a date range slider - comparing actual data to target data for yearly target for Sales, Margin, Cost
        * Lower section: Map (show states and cities colored to give notion of coverage), click in given state to show total sales, total order, total shipping, total costs, total margin, total customers, for a given date range

    * 2 - Develop an internal application to simulate/predict **customer willingness/demand based on price adjust** (increase/decrease) 

    * 3 - **ML use cases**
        * Customer segmentation analysis
        * Predict product demand, using regression and/or time series forecast
        * Use a association rules, to get detailed understanding on common groups of products sold together (as “iPhone + Headphone” is handled different than “Headphone + iPhone” as it is now)

    * 4 - Do **more analysis** in terms of 
        * promotion (how are our initiatives in terms of ads, either online or in-store? Which products could we advertise?) 
        * place (what is our territory and coverage performance? Should we invest in new places or improve existing?)
        * Understand why price was fixed over the year (this is a toy dataset, but this question would make sense in a real business context)

    * 5 - Get **customer base profile data** to 
        * understand customer behaviour
        * improve process around: customer acquisition (awareness, consideration, signup), retention and advocacy

    * 6 - Understand why are we **not selling more products**? 
        * It is a theoretical question for this project, but useful in a real project

    * 7 - Get more **data from other channels and platforms**
        * Collect data for more years: 2016, 2017, 2018, 2020, 2021
        * Break down between online and in-store purchase (we know sales out of working hours are online, but in working hours we don't know the mix)
        * Feature engineering: combine other datasets
            * Suppply Chain data: delivery time such products, stock levels, freight
            * Taxes, Profit, Cashflow 
            * Customer Survey - for given purchase and for how customer perceives Kmart

    """