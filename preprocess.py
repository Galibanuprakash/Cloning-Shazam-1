import re
import pandas as pd

def clean_text(text):
    text = re.sub(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text)  # Remove timestamps
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    return text.strip()

def preprocess_subtitles():
    df = pd.read_csv("data/subtitle_data.csv")
    df["Content"] = df["Content"].apply(clean_text)
    df.to_csv("data/cleaned_subtitles.csv", index=False)
    print("Preprocessing complete!")

preprocess_subtitles()