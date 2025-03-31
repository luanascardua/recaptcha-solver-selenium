from selenium.webdriver.common.by import By


class Selectors:
    btn_audio_challenge = By.ID, "recaptcha-audio-button"
    audio_source = By.ID, "audio-source"
    input_audio_response = By.ID, "audio-response"
    checkbox = By.ID, "recaptcha-anchor"
    recaptcha_iframe = (By.XPATH, "//iframe[contains(@src, 'recaptcha/api2/anchor')]")
    iframe_challenge_recaptcha = By.XPATH, "//iframe[starts-with(@src, 'https://www.google.com/recaptcha/api2/bframe?')]"
    
    #//*[@id="recaptcha-audio-button"]
    # By.XPATH, '/html/body/div[2]/div[4]/iframe'
    # recaptcha_iframe = (By.XPATH, '/*[@id="recaptcha-audio-button"]')