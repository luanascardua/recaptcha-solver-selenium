import speech_recognition as sr
from pydub import AudioSegment

import io
import requests


class SpeechRecognitionAdapter:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def load_mp3_from_url(url):
        """Download MP3 file by an URL and return as BytesIO """
        response = requests.get(url)
        if response.status_code == 200:
            return io.BytesIO(response.content)
        else:
            print(f"[ERROR] Download audio | Status code: {response.status_code}")
            return None

    def convert_mp3_bytes_to_wav_bytes(mp3_bytes: io.BytesIO):
        """ Convert MP3 (BytesIO) to WAV (BytesIO) """
        audio = AudioSegment.from_file(mp3_bytes, format="mp3")
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        return wav_io
    
    def recognize_speech_from_bytes(audio_bytes):
        """ Recognize the audio directly of a BytesIO object"""
        recognizer = sr.Recognizer()
        
        with sr.AudioFile(audio_bytes) as source:
            audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data, language="pt-BR")
            print("text recognized:", text)
            return text
        except sr.UnknownValueError:
            print("Could not recognize audio")
        except sr.RequestError as e:
            print(f"Error connecting to recognition service: {e}")