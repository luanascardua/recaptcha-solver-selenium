from apps.adapters.selenium_adapter import SeleniumAdapter
from apps.adapters.speech_recognition_adapter import SpeechRecognitionAdapter


class SolverCaptcha:
    def __init__(self, selenium_adapter: SeleniumAdapter, audio_transcription_adapter: SpeechRecognitionAdapter):#, audio_download_port, audio_transcription_port):
        self.selenium_adapter = selenium_adapter
        self.audio_transcription_adapter = audio_transcription_adapter
        '''self.audio_download_port = audio_download_port
        self.audio_transcription_port = audio_transcription_port'''

    def solve(self, recaptcha_iframe: tuple) -> str:
        self.selenium_adapter.click_checkbox_im_not_robot(recaptcha_iframe)
        audio_link = self.selenium_adapter._get_audio_source()

        if audio_link:
            transcription = self.audio_transcription_adapter.transcribe_audio(audio_link)
