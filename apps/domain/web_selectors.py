from selenium.webdriver.common.by import By


class Selectors:
    btn_audio_challenge = By.ID, "recaptcha-audio-button"
    audio_source = By.ID, "audio-source"
    input_audio_response = By.ID, "audio-response"
    checkbox = By.ID, "recaptcha-anchor"
    recaptcha_iframe = (By.XPATH, "//iframe[contains(@src, 'recaptcha/api2/anchor')]")