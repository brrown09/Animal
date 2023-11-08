import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Next days")

# Get the place from the user
place = st.text_input("Place")

# Get the number of days for the forecast
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

# Get the data to view (temperature or sky)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

# Print a subheader
st.subheader(f"{option} for the next {days} days in {place}")



# If the place is not empty
if place:
    # Filter the data based on the user's input
    filtered_data = get_data(place, days)

    # If the user wants to see the temperature
    if option == "Temperature":

        # Create a list of temperatures
        temperatures = [dict["main"]["temp"] for dict in filtered_data]

        # Create a list of dates
        dates = [dict["dt_txt"] for dict in filtered_data]

        # Create a line plot of the temperature
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})

        # Display the plot on Streamlit
        st.plotly_chart(figure)

    # If the user wants to see the sky
    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        # Filter the data to only include the sky condition
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)

        # Display an image of the sky conditions
        st.image(image_paths, width=115)

