import requests
import streamlit as st 
from city import top_city
API_KEY = ("hirtjhjtrhiojrthijoijoij")

BASE_URL = ("http://api.openweathermap.org/data/2.5/weather")

city = st.selectbox('choose your city',sorted(top_city))
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

button = st.button("Show")

if button:
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 2)
        st.subheader("Weather")
        st.caption(weather)
        st.subheader("Temperature")

        st.caption(temperature)
        print("weather: ", weather)
        print("temperature: ", temperature)

    else:
        print("an error occurred")