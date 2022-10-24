# Import libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import time
from time import sleep

# Configure selenium options
options = Options()
options.headless = False
options.add_argument("--window-size=500,1200")
options.add_argument(".incognito")

# Set Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Start driver
driver.get('URL')

"""




ADD SOME COOKING HERE



"""

# Driver quit
driver.quit()