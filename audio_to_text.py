import whisper

def audio_to_text(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

audio_path = "data/query_audio.wav"
query_text = audio_to_text(audio_path)
print("Recognized Query:", query_text)