from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROMEDRIVER_PATH = "./chromedriver"

options = Options()
options.headless = True
driver = webdriver.Chrome(CHROMEDRIVER_PATH,options=options)

driver.get("https://serpmaster.com/")
elem = driver.find_element_by_css_selector("form input")
elem.clear()
elem.send_keys("What is the new Budget 2020?")
elem.send_keys(Keys.RETURN)
l=1
while l==1:
    op = driver.find_element_by_css_selector("code")
    l = len(op.find_elements_by_css_selector("*"))


from json import loads

x = loads(op.text)
rq = x["demoResponse"]["results"][0]["content"]["results"]["related_questions"]

for r in rq:
    print(r["search"]["title"])

driver.close()