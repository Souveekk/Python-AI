import streamlit as st
import requests

st.title("Weather App")
st.write("Enter a city name to get the current weather.")

API_KEY = "d5413fe29c3ac2da5c1b9ff07308b4f1"  # Get free key at openweathermap.org

city = st.text_input("Enter City Name", placeholder="e.g. London")

if st.button("Get Weather"):
    if city == "":
        st.warning("Please enter a city name.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")

            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", f"{data['main']['temp']} C")
            col2.metric("Humidity",    f"{data['main']['humidity']} %")
            col3.metric("Wind Speed",  f"{data['wind']['speed']} m/s")

            st.info(f"Condition:  {data['weather'][0]['description'].title()}")
            st.info(f"Feels Like: {data['main']['feels_like']} C")
            st.info(f"Min / Max:  {data['main']['temp_min']} C  /  {data['main']['temp_max']} C")

        elif response.status_code == 404:
            st.error("City not found. Please check the spelling.")
        else:
            st.error("Something went wrong. Please try again.")