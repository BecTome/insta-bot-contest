# %% Load Libraries
from time import sleep
from selenium import webdriver

# # %% Open the browser and enter instagram
# Open browser
browser = webdriver.Firefox(executable_path='./venv/bin/geckodriver')

# If Selenium can’t find an element, then it waits for five seconds to allow 
# everything to load and tries again. 
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/') # Get HTTP request

# finds the element <a> whose text is equal to Log in. It does this using XPath,
# but there are a few other methods you could use.
login_link = browser.find_element_by_xpath("//a[text()='Log in']")

login_link.click() # clicks on the found element <a> for the login link.

sleep(5) # Wait 5 seconds

browser.close() # Close it