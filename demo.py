import streamlit as st
import pickle
import numpy as np

pip = pickle.load(open("model1.pkl","rb"))
df = pickle.load(open("df.pkl","rb"))

st.title("WEATHER FORECAST")
st.image("download.png",width=500)

precipitation = st.slider("Precipitation", min_value=0, max_value=56, value=15, step=1)
temp_max = st.slider("Maximum Temperature", min_value=0, max_value=50, value=15, step=1)
temp_min = st.slider("Minimum Temperature", min_value=-10, max_value=20, value=15, step=1)
wind = st.number_input("Wind Speed")

if st.button("Predict"):
    query = np.array([precipitation, temp_max, temp_min, wind])
    query = query.reshape(1, 4)
    prediction = pip.predict(query)
    st.title("Weather forecast for the selected data")
    # st.markdown(prediction)
    if prediction == 2:
        st.subheader("Rain")
    elif prediction == 4:
        st.subheader("Sun")
    elif prediction == 1:
        st.subheader("FOG")
    elif prediction == 0 :
        st.subheader("Drizzling")
    else: 
        st.write("SNOW")
        
