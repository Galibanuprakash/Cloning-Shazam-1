from search import search_subtitles
from audio_to_text import audio_to_text

def main():
    audio_path = "data/query_audio.wav"
    query_text = audio_to_text(audio_path)
    results = search_subtitles(query_text)
    print("Relevant Subtitles:", results)

if __name__ == "__main__":
    main()