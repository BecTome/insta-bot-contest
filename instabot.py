# %% Load Libraries
from time import sleep
from selenium import webdriver

# # %% Open the browser and enter instagram
# Open browser
browser = webdriver.Firefox(executable_path='./venv/bin/geckodriver')
# Get HTTP request
browser.get('https://www.instagram.com/')
# Wait 5 seconds
sleep(5)
# Close it
browser.close()