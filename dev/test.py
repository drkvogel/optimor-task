# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:45:08 2016

@author: Chris Bird
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]
url = 'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'

# #countryName
# #paymonthly
# #standardRatesTable

def get_landline_tariff(country):
    driver = webdriver.Firefox()
    driver.get(url)
    #assert "Python" in driver.title

    # select country
    elem = driver.find_element_by_name("countryName")
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    # assert that there is now li.btn_arrow_tab a#paymonthly
    # <li class="btn_arrow_tab left active  ui-state-default ui-corner-top">
    #     <a href="#paymonthlyTariffPlan" id="paymonthly" class="doubleText">Pay Monthly<small>View standard rates and Bolt Ons</small></a>
    # </li>

    # select Pay Monthly
    elem = driver.find_element_by_name("paymonthly")
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)

    # find tariff
    elem = driver.find_element_by_name("standardRatesTable")
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)


    #assert "No results found." not in driver.page_source
    driver.close()
    return 



for country in range(countries):
    print "landline tariff for" + country + " is: " + get_landline_tariff(country)



# example from http://selenium-python.readthedocs.org/getting-started.html
#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
