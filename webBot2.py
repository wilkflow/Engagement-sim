
import os,time
from selenium import webdriver # Import the Selenium Webdriver
from selenium.webdriver.common.by import By
import requests
import random
import json
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
global proxy_list
global proxy
global ltextlist 
ltextlist = ['instert partial link text in this list']
proxy_list = []
with open('http.txt', 'r') as p_ch:
    for line in p_ch:
        proxy_list.append('http://'+line.strip().replace('\n', ''))
    #print(proxy_list)

def test_proxy(proxy_url):
    """
    Tests if a given proxy URL is working by making a request through it.
    """
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    test_url = "https://httpbin.io/ip"  # A simple service to show your IP

    try:
        response = requests.get(test_url, proxies=proxies, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # If the request is successful, check the IP address returned
        # This helps verify if the request actually went through the proxy
        data = response.json()
        origin_ip = data.get("origin")

        print(f"Proxy {proxy_url} is active.")
        print(f"Originating IP through proxy: {origin_ip}")
        return True

    except requests.exceptions.RequestException as e:
        #print(f"Proxy {proxy_url} failed")
        return False


 
urlToVisit = input("What website URL would you like to visit? : ") # Capture Website url to visit
noOfVisitsToBeDone = random.randint(2,5)
noOfVisitsCompleted = 0 # The initial value of noOfVisitsCompleted, with global scope






def visit_web():
    global proxy
    global proxy_list
    global ltextlist
    elemToClick = random.choice(ltextlist)
    nprox = False
    
    while not nprox:
        t_prox = random.choice(proxy_list)
        ip = t_prox.replace('http://', '').split(':')[0]
        format = f'https://api.findip.net/{ip}/?token=3bf0a2b162fa4877be7e58125d3cc771'
        #print(format)
        response = requests.get(format)
        #print(response)
        json_response = response.json()
        #print(json_response)
        if json_response['country']['iso_code'] == 'US' or json_response['country']['iso_code'] == 'CA':
            print(f'testing {t_prox}')
            if test_proxy(t_prox):
                proxy = t_prox
                nprox = True
            else:
                proxy_list.remove(t_prox)
        else:
            proxy_list.remove(t_prox)
    
    options = Options()
    #options.add_argument("--headless=new")
    options.add_argument(f"--proxy-server={proxy}")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
    options=options) 
    global noOfVisitsCompleted # Using global keyword to signify that assignment is done at a global scope
    try:
        print("Browser Launched...") # Log message on browser opened
        time.sleep(random.randint(1,3))
        browser.get(urlToVisit)
        print("URL Loaded...") # Log message on URL opened
        time.sleep(random.randint(20, 60))
        try:
            submit_button = browser.find_element(By.CSS_SELECTOR, "input[value='Close and accept']") #Close and accept   #I Agree!
            browser.execute_script("arguments[0].click();", submit_button)
        except:
            submit_button = browser.find_element(By.CSS_SELECTOR, "button[value='I Agree!']")
            browser.execute_script("arguments[0].click();", submit_button)
        time.sleep(random.randint(5, 10))
        try:
            elem = browser.find_element(By.PARTIAL_LINK_TEXT, elemToClick) # Locate element on Website using class name      Rapala Original Floating Minnow
            browser.execute_script("arguments[0].click();", elem)
        except:
            print('LINK CLICK FAILED')
            elem = browser.find_element(LINK_TEXT, elemToClick) # Locate element on Website using class name      Rapala Original Floating Minnow
            browser.execute_script("arguments[0].click();", elem)
        print("Element Clicked...") # Log message on element clicked
        time.sleep(random.randint(10, 20))
        browser.quit()
        print("Browser Closed...") # Log message on browser closed
        
        print("Visit No. %d Completed "% int(noOfVisitsCompleted)) # Log message on visit stop
        print(proxy)
    except:
        browser.quit()
	
def repeat_visit_web():
	for i in range(int(noOfVisitsToBeDone)): # Number of times to revisit web
		global noOfVisitsCompleted # Using global keyword to signify that assignment is done at a global scope
		noOfVisitsCompleted = i+1 # xrange returns 0 index based numbers so to make them realistic for humans we add 1
		print("Visit No. %d Started "% int(noOfVisitsCompleted)) # Log message on visit start
		visit_web() # Call the visit_web function to visit specified website



repeat_visit_web() # The initial call that starts the program
print(proxy)
os.remove('http.txt')

