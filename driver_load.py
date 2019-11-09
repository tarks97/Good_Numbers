from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from pyvirtualdisplay import Display
#display = Display(visible=0,size=(1920, 1080))


def driver_load():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    #  chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("nogui=False")
    #     driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options, executable_path=r'/home/tarik/Desktop/tarikTask-master/venv/bin/chromedriver')
    return driver