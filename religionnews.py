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
    url = 'https://religionnews.com/category/world/page/'+str(i)
    page = driver.get(url)
    time.sleep(10)

    div = driver.find_elements(By.CSS_SELECTOR, '.other-category-posts .category-post')
    
    for i in div:
        data = {}
        data["headline"] = i.find_element(By.CSS_SELECTOR, '.other-category-posts .entry-title').text
        data["topic"] = topic
        source=i.find_element(By.XPATH, 'a')
        data["source"] = source.get_attribute("href")
        times = i.find_element(By.CSS_SELECTOR, '.other-category-posts .the-author')
        data["date"] = times.text[14:]
        img = i.find_element(By.CSS_SELECTOR,".other-category-posts .category-post-thumbnail")
        data["thumbnail_url"]=img.get_attribute("src")

        new = requests.get(data["source"])
        soup = BeautifulSoup(new.content, "html.parser")
        desc=""
        a=soup.select("html>body>div>div>div>div>div>div>div")
        for q in a:
            desc += q.text
        data["description"] = desc
        data_list.append(data)
print(data_list)
print(len(data_list))
driver.quit()