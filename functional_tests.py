from selenium import webdriver
from selenium.webdriver.chrome.service import Service

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(service=Service('./chromedriver'), options=options)
    browser.get('http://localhost:8000')

    assert 'Django' in browser.title