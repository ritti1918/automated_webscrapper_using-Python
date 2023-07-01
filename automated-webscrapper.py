
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook


path="C:/Users/ritti/OneDrive/Documents/progs/chromedriver_win32/chromedriver.exe"
options = Options()
options.add_experimental_option('detach', True)
chrome_driver = webdriver.Chrome()
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(2)

search_button = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]").click()
input_search=driver.find_element("id","APjFqb")
input_search.send_keys("flipkart online shopping")
input_search.send_keys(Keys.ENTER)
time.sleep(3)

driver.get("https://www.flipkart.com/")

driver.find_element("xpath","/html/body/div[2]/div/div/button").click()
searchBar=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
searchBar.send_keys("iphone under 50000")
searchbutton=driver.find_element("xpath","/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
searchbutton.click()
time.sleep(5)


Product_names = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    website_url = "https://www.flipkart.com/search?q=iphone+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_14_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_14_na_na_na&as-pos=3&as-type=RECENT&suggestionId=iphone+under+50000&requestId=6dd5e5cc-c881-4b09-8f18-a403541ae1b8&as-searchtext=iphones+under+&page=1"+ str(i)
    response = requests.get(website_url)
    print(response)

    soup = BeautifulSoup(response.text, "lxml")

    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    names = box.find_all("div", class_ = "_4rR01T")

    for i in names:
        name = i.text
        Product_names.append(name)
    
    # #    print(Product_names)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")

    for i in prices:
        name = i.text
        Prices.append(name)
    
    # #    print(Prices)

    desc = box.find_all("ul", class_ = "_1xgFaf")

    for i in desc:
        name= i.text
        Description.append(name)
    # #    print(Description)

    review = box.find_all("div", class_ = "_3LWZlK")
    
    for i in review:
        name = i.text
        Reviews.append(name)
    
    #    print(Reviews)




    df=pd.DataFrame({'Product_name':(Product_names),
                    'Price'     :(Prices),
                    'Description':(Description ),
                    'Reviews'    :(Reviews)
                    })
    #  print(df)

    df.to_csv('iphonedataextract.csv',index=False)