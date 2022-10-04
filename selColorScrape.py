from selenium import webdriver

url = "https://www.computerhope.com/htmcolor.htm"

driver = webdriver.Chrome()
driver.get(url)


rows = driver.find_element_by_class_name("tcw")
num = 0
for color in rows:
    name = color.find_element_by_xpath("//*[@id="main-content"]/article/table[2]/tbody/tr[i]/td[2]" % num).text
    id = color.find_element_by_xpath("//*[@id="main-content"]/article/table[2]/tbody/tr[i]/td[1]/a" % num).text