import streamlit as st

def eda_customer_behaviour():
    st.warning("* Please run EDA notebook in case you want to go thru the code and calculation")
    st.info("""
        * **30.7k customers** (21.9% of 140.7k) are recurrent
        * Top 3 Recurrency times 
            * 78.1% buy once
            * 17.8% re-buy twice
            * 3.4% re-buy 3 times
    """)

    st.info("""
        Product Recurrency 
        *  A recurrent customer is typically purchasing around **Audio and Cable/Accessories**
            * Batteries + Charging Cable  
            * Charging Cable
            * Wired/Apple Headphones + Charging Cable
            * Batteries
            * Apple/Bose/wired Headphones + Batteries
            * Wired Headphones
    """)

    st.info("""
        These products are good in terms of  
        * percentual margin: batteries, charging cable, cable, headphone (wired, bosed, apple)
        * absolute margin: apple headphone
    """)

    st.info("""
        * Customers from **San Francisco, Los Angeles, New York and Boston** tend to be more recurrent and to have better margin
    """)

    st.info("""
        * 90% of customers bring an individual **annual margin up to 400**

    """)

def eda_product_basket_analysis():
    st.warning("* Please run EDA notebook in case you want to go thru the code and calculation")
    st.info("""
        **23.3k orders** (13.1% of 178.4k) with more than 1 product
        * Typically these orders have 2 products
        * 2.0M$ of margin, or 10.4% of all margin result
        """)
    
    st.info("""
        **362 combinations** of orders with multiple products 
        * Note there are multiple units from same product
        * The first 2 combinations happened +5k times, the next 5 between 800 and 1.7k, and the remaining less than 370
    """)

    # st.image("inputs/images/eda_product_basket.png", use_column_width='always',
    #             caption='Product Basket - Common products bought together in the same order')

    st.info("""
        Note the Products lines are around **Mobile, Cable/Access., Audio**:
        * Multiple Batteries packs
        * Multiple Charging Cables
        * Multiple wired headphones 
        * Mobile + Charging cable
        * Mobile + Headphone
    """)

    st.info("""
        The following products have a good profile in terms of 
        * percentual margin: batteries, lightning cable, usb-c cable, headphone (wired, bose, apple)
        * absolute margin: iPhone, apple headphone
 
    """)


def eda_product_region_performance():
    st.warning("""* Please check "Tracker Over Time" tab at Tableau App to check/validate the numbers """)
    st.success("""
        * Here we are interested in identifying “tiered” behaviour (Highest, High, Medium, Low), 
            based on Margin and Quantity across months, slicing by Product and Region.
            * **Household product line captures attention**, since it has low for margin and quantity
        """)

    st.info("""
        Region
        * It repeats the pattern at Overall Results:
            * San Francisco, Los Angeles, and New York are Highest group.
            * Portland, ME has far low performance and seasonality compared to others. Why? 
                Roadmap: conduct additional investigations
        """)

    st.info("""
        Product
        * Margin: 
            * Highest: Macbook
            * Low: Vareebadd phone, 20in Monitor, Lightning Cable, USB-C Cable, **LG Washing Machine**, Wired Headphones, **LG Dryer**, AA Batteries, AAA Batteries

        * Quantity: 
            * Highest: AAA Batteries, AA Batteries, USB-C cable, Lightning Cable, Wired Headphones
            * Low: Vareebadd phone, **LG dryer, LG washing**
        """)

    # st.image("inputs/images/eda_performance_over_time.png", use_column_width='always',
    #             caption='Product Quantity performance over time')


def eda_patterns_over_time():
    st.info("""
        * Bar plot shows **Margin** Levels across months (taken from Tableau App)
        * The pattern repeats for other levels **(Revenue, Costs, # Order, # Product, # Customer)**.

        """)
    # st.image("inputs/images/eda_patterns_over_time.png", use_column_width='always', caption='Margin levels per month')

    st.info("""
        * Levels are higher in **Q4 and Q2: Dec, Oct, April**
            * Mainly due to Macbook, iPhone and Thinkpad
            * Why? Likely hypothesis is due to date seasonality

        * Changing X axis
            * Levels are similar around days of the month and weekdays. 
            * Levels are higher from 11h to 13h and from 19h to 21h
                * **action**: promote specific ads on these time frames (online or in-store)
        """)


def eda_overall_results(): 
    st.success("""
        In 2019
        * 34.3M$ Product **Revenue**
        * 14.3M$ Product **Cost**
        * 20.0M$ Product **Margin**
            * 140.7k customers
            * 178.4k orders
            * 208.7k products sold
            * 86% of orders have 1 product
        """)

    st.info("""
        Product and Region Analysis
        * There is not product or product line with **margin loss**
        * For product line and product, **quantity of orders and margin are not correlated**  
        * CA (Los Angeles and San Francisco) and TX (Austin and Dallas) have customer from 2 cities. Remaining states from 1 city.
        * There is not state or city with **margin loss**
        * For state and city, **quantity of orders and margin are correlated**
        """)

    st.info("""
        * 7 Product Lines
            * Top 3 Qty ordered (85%)
                * Cables and Acces. 50% (105k) 
                * Audio 24% (49k)
                * PC/Video Games 12% (24k)

            * Top 3 Margin (78%)
                * Computer/Laptop 41% (8.3M)
                * Mobile 20% (4.1M)
                * PC/Video Game 17% (3.4M)
        """)

    st.info("""
        * 19 Products
            * Top 3 Qty ordered (39%)
                * AAA Batteries 15% (31k)
                * AA Batteries 13% (27k)
                * USB-C Cable 11% (24k)

            * Top 3 Margin (54%)
                * Macbook 28% (5.6M)
                * iPhone 13% (2.7M)
                * ThinkPad 13% (2.6M) 
        """)

    st.info("""
        * 8 States
            * Top 3 # Orders (66%)
                * CA 40% (71.3k) 
                * NY 13% (23.8k) 
                * TX 13% (23.7k)

            * Top 3 Margin (66.5%)
                * CA 40% (7.9M)
                * NY 13.5% (2.7M)
                * TX 13% (2.6M)
        """)

    st.info("""
        * 10 Cities
            * Top 3 # Orders (53%)
                * CA, San Francisco 24% (42k) 
                * CA, Los Angeles 16% (28k) 
                * NY, New York 13% (23k)

            * Top 3 Margin (53%)
                * CA, San Francisco 24% (4.8M)
                * CA, Los Angeles 15% (3.1M)
                * NY, New York 13% (2.7M)    
        """)
