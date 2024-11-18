from abc import ABC, abstractmethod

class BrowserOutputPort(ABC):
    @abstractmethod
    def open_url(self, url):
        pass

    @abstractmethod
    def switch_to_recaptcha_frame(self):
        pass

    @abstractmethod
    def get_audio_challenge_link(self):
        pass

    @abstractmethod
    def download_audio(self, audio_url):
        pass

    @abstractmethod
    def submit_audio_response(self, response_text):
        pass


class SpeechRecognitionOutputPort(ABC):
    @abstractmethod
    def transcribe_audio(self, file_path):
        pass
