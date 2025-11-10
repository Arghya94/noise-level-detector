import streamlit as st
import sounddevice as sd
import numpy as np
import geocoder
import folium
from streamlit_folium import st_folium

st.title("🌍 Real-Time Noise Level Detector")

st.write("This app records ambient sound, estimates the noise level, and shows your location on a map.")

duration = st.slider("Recording duration (seconds)", 2, 10, 3)

if st.button("🎤 Record Now"):
    st.info("Recording ambient sound...")
    fs = 44100
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    volume_norm = np.linalg.norm(recording) * 10
    noise_level = 20 * np.log10(volume_norm + 1e-6)
    noise_level = round(noise_level, 2)

    g = geocoder.ip('me')
    loc = g.latlng if g.latlng else [0, 0]

    st.success(f"Noise Level: **{noise_level} dB**")

    # Display map
    m = folium.Map(location=loc, zoom_start=12)
    color = "green" if noise_level < 50 else "orange" if noise_level < 70 else "red"
    folium.Marker(loc, popup=f"{noise_level} dB", icon=folium.Icon(color=color)).add_to(m)
    st_folium(m, width=700, height=450)
