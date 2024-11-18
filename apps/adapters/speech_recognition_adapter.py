import speech_recognition as sr


class SpeechRecognitionAdapter:
    def transcribe_audio(self, file_path):
        recognizer = sr.Recognizer()
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
        return recognizer.recognize_google(audio_data)
