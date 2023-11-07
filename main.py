import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Next days")
place = st.text_input("Place")
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")


def get_data(place, days, option):



d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "date", "y": "Temperature(C)"})

st.plotly_chart(figure)
