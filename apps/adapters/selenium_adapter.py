from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from apps.domain.web_selectors import Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class SeleniumAdapter:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        pass

    def _wait_for_element(self, web_element: tuple[str], timeout: int = 15) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(web_element))
    
    def _js_click(self, web_element: tuple[str]) -> None:
        self._driver.execute_script("arguments[0].click();", web_element)

    def _get_url(self, url: str) -> None:
        self._driver.get(url)

    def click_checkbox_im_not_robot(self, recaptcha_iframe: tuple) -> str:
        if isinstance(recaptcha_iframe, tuple):
            recaptcha_iframe = self._wait_for_element(recaptcha_iframe)

        self._driver.switch_to.frame(recaptcha_iframe)
        checkbox_im_not_robot = self._wait_for_element(Selectors.checkbox)
        self._js_click(checkbox_im_not_robot)

        self._driver.switch_to.default_content()
        

    def _get_audio_source(self) -> str:
        frame = self._wait_for_element(Selectors.iframe_challenge_recaptcha)
        self._driver.switch_to.frame(frame)

        btn_audio_challenge = self._wait_for_element(Selectors.btn_audio_challenge)
        self._js_click(btn_audio_challenge)

        try:
            src_audio_link = self._driver.find_element(By.ID, "audio-source")#self._wait_for_element(Selectors.audio_source)
            src_audio_link = src_audio_link.get_attribute("src")
        except TimeoutException:
            print('Google has detected automated queries. Try again later.')
            
        return src_audio_link
