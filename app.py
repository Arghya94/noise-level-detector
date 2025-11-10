import streamlit as st
import numpy as np
import geocoder
import folium
from streamlit_folium import st_folium
import random

st.title("🌍 Real-Time Noise Level Mapper")
st.write("This demo simulates noise levels and shows them on a map based on your location.")

# Step 1: Get location
st.subheader("📍 Your Current Location")
g = geocoder.ip('me')
lat, lon = g.latlng if g.latlng else (22.5726, 88.3639)
st.write(f"Latitude: {lat}, Longitude: {lon}")

# Step 2: Simulate noise data
st.subheader("🎤 Simulated Noise Measurement")
if st.button("Measure Noise"):
    noise_level = random.uniform(30, 90)  # Simulate dB value
    st.success(f"Noise Level: {noise_level:.2f} dB")

    # Step 3: Display map
    m = folium.Map(location=[lat, lon], zoom_start=14)
    folium.Marker(
        [lat, lon],
        popup=f"Noise: {noise_level:.2f} dB",
        tooltip="Noise Location",
        icon=folium.Icon(color="red" if noise_level > 70 else "green"),
    ).add_to(m)
    st_data = st_folium(m, width=700, height=500)
else:
    st.info("Click the button above to simulate a noise measurement.")

