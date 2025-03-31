from apps.adapters.speech_recognition_adapter import SpeechRecognitionAdapter


class TranscribeAudio:
    def __init__(self, speech_recognition_adapter: SpeechRecognitionAdapter):
        self.speech_recognition_adapter = speech_recognition_adapter

    def transcribe(self, audio_url: str):
        audio_mp3_bytes = self.speech_recognition_adapter.load_mp3_from_url(audio_url)
        if audio_mp3_bytes:
            audio_wav_bytes = self.speech_recognition_adapter.convert_mp3_bytes_to_wav_bytes(audio_mp3_bytes)
            self.speech_recognition_adapter.recognize_speech_from_bytes(audio_wav_bytes)