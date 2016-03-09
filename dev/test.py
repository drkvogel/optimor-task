# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:45:08 2016

@author: Chris Bird
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


def get_o2_landline_tariff(country):
    url = 'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'
    browser = webdriver.Firefox()
    browser.get(url)
    #assert "Python" in browser.title

    # select country #countryName //*[@id="countryName"]
    elem = browser.find_element_by_name("countryName")
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    # assert that there is now li.btn_arrow_tab a#paymonthly
    # <li class="btn_arrow_tab left active  ui-state-default ui-corner-top">
    #     <a href="#paymonthlyTariffPlan" id="paymonthly" class="doubleText">Pay Monthly<small>View standard rates and Bolt Ons</small></a>
    # </li>
    time.sleep(0.2)
    raise Exception("countryName")

    # select Pay Monthly #paymonthly //*[@id="paymonthly"]
    #elem = browser.find_element_by_name("paymonthly") # no, that's the id, not the name - name is the element type, e.g. p or a or li
    #browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")

    browser.find_element_by_xpath('//*[@id="paymonthly"]')
    #elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.2)
    raise Exception("paymonthly")

    # find tariff in #standardRatesTable
    elem = browser.find_element_by_name("standardRatesTable")
    #elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.2)
    raise Exception("standardRatesTable")


    #assert "No results found." not in browser.page_source
    browser.close()
    return 

# selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"countryName"}

countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

for country in range(countries):
    try:
        print "O2's landline tariff for" + country + " is: " + get_o2_landline_tariff(country)
    except NoSuchElementException:
        #

    except Exception as ex:
        print "An error occurred whilst trying to retrieve a tariff for " + country
        print "Message: "+ex.args




# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import time

# browser = webdriver.Firefox() # Get local session of firefox
# browser.get("http://www.yahoo.com") # Load page
# assert "Yahoo!" in browser.title
# elem = browser.find_element_by_name("p") # Find the query box
# elem.send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(0.2) # Let the page load, will be added to the API
# try:
#     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
# except NoSuchElementException:
#     assert 0, "can't find seleniumhq"
# browser.close()


# example from http://selenium-python.readthedocs.org/getting-started.html
#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
