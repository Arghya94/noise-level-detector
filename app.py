import streamlit as st
import numpy as np
import geocoder
import folium
from streamlit_folium import st_folium
import random

st.set_page_config(page_title="Noise Level Mapper", layout="wide")

st.title("🌍 Real-Time Noise Level Mapper")
st.write("This demo simulates noise levels and shows them on a map based on your location.")

# Get user location
g = geocoder.ip('me')
lat, lon = g.latlng if g.latlng else (22.5726, 88.3639)

# Initialize session state to remember data between reruns
if "readings" not in st.session_state:
    st.session_state["readings"] = []

# Simulate noise level
if st.button("🎤 Measure Noise"):
    noise_level = random.uniform(30, 90)
    st.session_state["readings"].append({"lat": lat, "lon": lon, "noise": noise_level})

# Display readings
if st.session_state["readings"]:
    st.subheader("📊 Recorded Noise Levels")
    for i, r in enumerate(st.session_state["readings"], 1):
        st.write(f"{i}. Location: ({r['lat']:.4f}, {r['lon']:.4f}) → **{r['noise']:.2f} dB**")

    # Create map
    m = folium.Map(location=[lat, lon], zoom_start=14)
    for r in st.session_state["readings"]:
        folium.Marker(
            [r["lat"], r["lon"]],
            popup=f"Noise: {r['noise']:.2f} dB",
            icon=folium.Icon(color="red" if r["noise"] > 70 else "green"),
        ).add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.info("Click the button above to start measuring noise levels.")
