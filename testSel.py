# use selenium
"""
import time

from selenium import webdriver

# driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

"""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
from selenium import webdriver

url = "https://www.youtube.com/c/Sidemen/videos"

driver = webdriver.Chrome()
driver.get(url)

videos = driver.find_element_by_class_name("style-scope ytd-grid-video-renderer")
for video in videos:
    title = video.find_element_by_xpath('//*[@id="video-title"]').text
    views = video.find_element_by_xpath('//*[@id="metadata-line"]/span[1]').text
    when = video.find_element_by_xpath('//*[@id="metadata-line"]/span[2]').text
    print(title, views, when)
