from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_driver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--hideless')

    chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome, options=chrome_options)
    
    return driver
