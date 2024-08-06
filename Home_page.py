import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import xgboost as xgb
import seaborn as sns
import sklearn

page = st.sidebar.selectbox("Explore Or Prediction", ("Prediction", "Explore"))

if page == "Prediction":

    st.title ("Car Price Preiction App")

    model = xgb.XGBRegressor()
    model.load_model('xgb_model.json')

    st.write('')
    st.write('')

    st.image("2013-dodge-charger-r-t-muscle-car-lxygkenro11k1iro.jpg")
    
    st.write('')
    st.write('')

    st.markdown("##### Are you planning to sell your car!?\n##### So let's try evaluating the price")
    
    p1 = st.number_input("What is the current ex-showroom price of the car(In lakhs)",2.5,100.0,step=1.0)
    p2 = st.number_input("What is distance completed by the car in kilometers?",100,5000000,step=100)

    s1 = st.selectbox("What is the fual type of the car?",('Petrol','Diesel','CNG'))
    if s1 == "Petrol":
        p3=0
    elif s1 =="Diesel":
        p3=1
    elif s1 =="CNG":
        p3=2        

    s2 = st.selectbox("Are you a Dealer or Individual?",('Dealer','Individual'))
    if s2 == "Dealer":
        p4=0
    elif s2 =="Individual":
        p4=1
    
    s3 = st.selectbox("What is the transmission type?",('Manual','Automatic'))
    if s3 == "Manual":
        p5=0
    elif s3 =="Automatic":
        p5=1

    p6 = st.slider("Number of owners the car previously had?",0,4)    

    date_time=datetime.datetime.now()
    years = st.number_input("In which year car was purchased?",1990,date_time.year)
    p7 = date_time.year - years

    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    try: 
       if st.button('Predict'):
           pred = model.predict(data_new)
           if pred>0:
               st.balloons()
               st.success("You can sell your car for {:.2f} Lakhs".format(pred[0]))
           else:
               st.Warning("You can't able to sell this car")    
    except:
        st.warning("Something went wrong please try again")            
elif page == "Explore":
    st.title ("Car Price Preiction App")

    st.write('')
    st.write('')

    st.image("1969-Ringbrothers-Dodge-Charger-Tusk-001.jpg")

    st.write('')
    st.write('')

    df= pd.DataFrame(    
        np.random.randn(10, 2),    
        columns=['x', 'y'])
    st.bar_chart(df)

    st.write('')
    st.write('')

    df= pd.DataFrame(    
        np.random.randn(10, 2),    
        columns=['x', 'y'])
    st.line_chart(df)

    rand=np.random.normal(1, 2, size=20)
    fig, ax = plt.subplots()
    ax.hist(rand, bins=15)
    st.pyplot(fig)
