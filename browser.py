from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Browser:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://demo.redmine.org')
