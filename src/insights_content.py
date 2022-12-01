import streamlit as st

def insights_pricing():
    st.success("1: **Under which circumstances could we adjust (increase/decrease) the price?**")
    st.info("""
        Increase price when demand is higher: **Apr, Oct and Dec**
        * Additional investigation to be done with marketing to understand effects on customer willingness vs price increase.
            * Macbook: from 1700 to, 1800 (5% increase) (additional revenue 162k*)
            * Apple headphone: from 150 to 170 (13% increase) (additional revenue 105k*)
            * Bose headphone from 100 to 120 (20% increase) (additional revenue 91k*)
        * **Assume volume in Apr, Oct, Dec doesn't change for respective products*
    """)
    st.info("""
        Decrease price when demand is lower: **Aug and Jan**, for products with high percentage margin (around 60%)
        * Additional investigation to be done with marketing to understand demand increase vs price decrease
            * Macbook - from 1700 to 1500 (12% discount, cost is 500)
            * Apple Headphone- from 150 to 130 (13% discount, cost is 45)
    """)

    st.write("---")
    st.success("2: **Are the prices in-line with the market reality?**")
    st.info("""
        * If there is no existing internal competitor pricing comparison, or easy-access external report, 
            **develop a quick price ecommerce web scraper**, to compare if our prices are in line with the market reality.
    """)


def insights_product():
    st.success("1: **Can we do: up-selling, cross-selling?**")
    st.info("""
        **Up-selling: Engage with customer for a product update**
        * Product (with good margin and value-added product)
            * From Thinkpad (1000) to Macbook (1700)
            * Google (600) to iPhone (700)
            * 20in monitor (110) to 27in FHD (150)
            * Bose headphones (100) to Apple Airpods (150)	

        * Channel Mechanism
            * Online (passive): customer adds item to basket, and is about to close the deal. An upsell offer appears.
            * In-store (active): sales consultant will place the order, but before closing the deal, 
                engages to convince customer to up-sell. Sales consultant will get a % commission of difference 
                between the expensive and cheaper.
    """)
    st.info("""
        **Cross-selling** - based on product basket analysis and product recurrency, and products with percentual margin to squeeze
        * iPhone (700) + Apple Airpod Headphone (150), where headphone is 33% off (from 150 to 100). 
            * Mobile + Headphone is a common product set.
            * Revenue 800 (700 + 100), cost 345 (45+300), margin 455 (56% margin)

        * Batteries + Batteries
            * Buy 3 packs (of the same product) and get 1 free
            * AA Batteries: revenue 11.52 (3 x 3.84), cost 4.8 (4 x 1.2), margin 6.72 (58% margin)
            * AAA Batteries: revenue 9 (3 x 3), cost 4.4 (4 x 1.1), margin 4.6 (51% margin)

        * USB-C Charging Cable + Batteries
            * Buy 1 USB-C Cable and 2 packs of battery, get a 1 pack of battery free
            * USB-C + AA: revenue 19.63 (11.95+ 2x3.84), cost 7.4 (3.8 + 3x1.2), margin 12.23 (62% margin)
            * USB-C + AAA: revenue 17.93 (11.95+ 2x2.99), cost 7.1 (3.8 + 3x1.1), margin 10.83 (60% margin)
    """)

    st.write("---")
    st.success("2: **Which products captured our attention and why?**")
    st.info("""
        **Washing Machine and Dryer Machine**
        * Reflect on how are they adding value to the customers  
        * They have lower volume, lower margin and lower percentage margin. But still, leave a positive margin.
        * Reflect on what is the effort/cost to maintain the supply chain, marketing and sales activities for these products 

        **AA/AAA Batteries**
        * Together they have 131k margin (0.6%) , 59k volume (28%), 40k customers, 161 packs sold daily
        * Batteries are bought recurrently
        * Why are people buying so much with us? 
            * Due to price? Due to demand? 
                * People are using batteries with  products that we don’t sell
                * Is battery a bait that bring people to us?
                * How is our pricing compared to the competition?
    """)

    st.write("---")
    st.success("3: **What are the product portfolio risks?**")
    st.info("""
        **Supplier/Brand diversification**
        * 50% of margin (10M) comes from Apple (Macbook, iPhone and Airpod headphones). 
            * It is important to identify and take care of “super products”. 
            * At the same time, it is a wise and healthy strategy to **not depend a lot exclusively on 1 product/brand/product line**.
                * **Reflect**: what are the similar or complementary products  from other premium brands, that make sense to our customer base?
    """)


def insights_customer_behaviour():
    st.success("1: **What is the product recurrency profile?**")
    st.info("""
        A recurrent customer is typically purchasing around **Audio and Cable/Accessories**: 
        * Batteries + Charging Cable; 
        * Charging Cable; 
        * Wired/Apple Headphones + Charging Cable; 
        * Batteries; 
        * Apple/Bose/wired Headphones + Batteries; 
        * Wired Headphones

    """)

    st.write("---")
    st.success("2: **How do I find more people that buy recurrently?**")
    st.info("""
        Cities like **San Francisco, Los Angeles, New York, and Boston** have more customers that buy more recurrently.
        * Limitation: Additional information on customer profile (demographics and behavioural data) would help to provide deeper insights.

    """)

    st.write("---")
    st.success("3: **Where do I find more customers that have higher margin (regardless if it is recurrent)?**")
    st.info("Same as above")