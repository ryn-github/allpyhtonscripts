from selenium import webdriver
import bs4
import logging 

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

driver = webdriver.Firefox()
driver.get('https://thepiratebayproxylist.se/')
list_link = driver.find_elements_by_partial_link_text('pirate')
logging.debug(list_link)
n = 0
	
for i in range(len(list_link)):
	try:
		list_link[i].click()
		break
	except:
		n = i+1
		if n == i:
			break
		else:
			list_link[n].click()
			break