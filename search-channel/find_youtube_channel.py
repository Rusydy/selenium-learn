# Import the necessary modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the YouTube home page
driver.get("https://www.youtube.com/")

# Find the element using xpath '//*[@id="search"]'
search_bar = driver.find_element(By.XPATH, "//input[@id='search']")

# Enter something to search for
search_bar.send_keys("《想我就打给我》-Bell玲惠")

# Now submit the form. WebDriver will find the form for us from the element
search_bar.submit()