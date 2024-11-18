from apps.adapters.selenium_adapter import SeleniumAdapter


class SolverCaptcha:
    def __init__(self, driver_adapter: SeleniumAdapter, audio_download_port, audio_transcription_port):
        self.driver_adapter = driver_adapter
        self.audio_download_port = audio_download_port
        self.audio_transcription_port = audio_transcription_port

    def solve(self, recaptcha_iframe) -> str:
        self.driver_adapter.click_checkbox_im_not_robot(recaptcha_iframe)
        audio_link = self.driver_adapter._get_audio_source()

        if audio_link:
            transcription = self.audio_transcription_port.transcribe_audio(audio_link)
