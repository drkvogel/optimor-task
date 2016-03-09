# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:45:08 2016

@author: Chris Bird
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_o2_landline_tariff(country):
    url = 'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'
    driver = webdriver.Firefox()
    driver.get(url)
    #assert "Python" in driver.title

    # select country #countryName
    elem = driver.find_element_by_name("countryName")
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    # assert that there is now li.btn_arrow_tab a#paymonthly
    # <li class="btn_arrow_tab left active  ui-state-default ui-corner-top">
    #     <a href="#paymonthlyTariffPlan" id="paymonthly" class="doubleText">Pay Monthly<small>View standard rates and Bolt Ons</small></a>
    # </li>
    raise Exception("countryName")

    # select Pay Monthly #paymonthly
    elem = driver.find_element_by_name("paymonthly")
    #elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    raise Exception("paymonthly")

    # find tariff in #standardRatesTable
    elem = driver.find_element_by_name("standardRatesTable")
    #elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    raise Exception("standardRatesTable")


    #assert "No results found." not in driver.page_source
    driver.close()
    return 

countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]
for country in range(countries):
    try:
        print "O2's landline tariff for" + country + " is: " + get_o2_landline_tariff(country)
    except Exception as ex:
        print "An error occurred whilst trying to retrieve a tariff for " + country
        print "Could not find "+ex.args


# example from http://selenium-python.readthedocs.org/getting-started.html
#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
