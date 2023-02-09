from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(executable_path=r'C:\Users\jakeo\Desktop\coding\Projects\TDD\geckodriver.exe', options=options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title