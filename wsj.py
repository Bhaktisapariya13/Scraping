from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ECG


chromePath = "D:\selenium\chromedriver_win32 (1)\chromedriver.exe" 
driver = webdriver.Chrome(chromePath)
topic= []
data_list = []
for i in range(1,10):
    url = 'https://www.wsj.com/news/types/india-news?page='+str(i)
    page = driver.get(url)
    time.sleep(10)

    div = driver.find_elements(By.CSS_SELECTOR, '.WSJTheme--design-refresh--2eDQsiEp')
    
    for i in div:
        data = {}
        data["headline"] = i.find_element(By.CSS_SELECTOR, '.WSJTheme--headlineText--He1ANr9C').text
        data["topic"] = topic
        source=i.find_element(By.CSS_SELECTOR, 'a')
        data["source"] = source.get_attribute("href")
        times = i.find_element(By.CSS_SELECTOR, '.WSJTheme--timestamp--22sfkNDv')
        data["date"] = times.text
        img = i.find_element(By.CSS_SELECTOR,'#latest-stories .WSJTheme--image--At42misj')
        data["thumbnail_url"]=img.get_attribute("src")

        new = requests.get(data["source"])
        soup = BeautifulSoup(new.content, "html.parser")
        desc=""
        a=soup.select("p")
        for q in a:
            desc += q.text
        data["description"] = desc
        data_list.append(data)
print(data_list)
print(len(data_list))
driver.quit()