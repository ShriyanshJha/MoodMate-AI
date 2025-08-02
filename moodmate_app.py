
import streamlit as st
from emotion_detector import detect_emotion_from_face
import pandas as pd
import datetime
import os
import webbrowser

st.set_page_config(page_title="MoodMate AI", layout="centered")
st.title("😊 MoodMate AI")
st.markdown("Your Emotion-Aware Home Assistant")

# Ensure mood history file exists
history_file = "mood_history.csv"
if not os.path.exists(history_file):
    df = pd.DataFrame(columns=["Date", "Detected Emotion"])
    df.to_csv(history_file, index=False)

# Auto face detection and response
st.header("📷 Detect Emotion from Face and Respond")

if st.button("Start Emotion Scan"):
    emotion = detect_emotion_from_face()
    if emotion:
        st.success(f"Detected Emotion: {emotion}")

        # Save to history
        df = pd.read_csv(history_file)
        df = df.append({"Date": datetime.datetime.now(), "Detected Emotion": emotion}, ignore_index=True)
        df.to_csv(history_file, index=False)

        # Music map
        music_links = {
            "Happy": "",  # Optional
            "Sad": "https://www.youtube.com/watch?v=1ZYbU82GVz4",
            "Tired": "https://www.youtube.com/watch?v=DWcJFNfaw9c",
            "Angry": "https://www.youtube.com/watch?v=lFcSrYw-ARY",
            "Stressed": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
            "Neutral": ""
        }

        if emotion in ["Neutral", "Happy"]:
            st.info("Music is optional for Neutral and Happy moods.")
        elif emotion in music_links:
            st.write("Playing recommended music based on your mood...")
            webbrowser.open(music_links[emotion])
    else:
        st.error("No face detected.")

# Mood History
st.header("📊 Mood History Tracker")
df = pd.read_csv(history_file)
st.line_chart(df["Detected Emotion"].value_counts())
st.dataframe(df.tail(10))
