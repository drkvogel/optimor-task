# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:50:55 2016

@author: Chris Bird
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def get_o2_landline_tariff(country, browser_name):
    url = 'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'
    if browser_name == 'Firefox':
        browser = webdriver.Firefox()
    else:
        raise Exception('Browser "' + browser_name + " not currently handled")

    # load intial page
    browser.get(url)
    #assert "O2" in browser.title

    # select country #countryName //*[@id="countryName"]
    elem = browser.find_element_by_xpath('//*[@id="countryName"]')
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

    elem = browser.find_element_by_xpath('//*[@id="paymonthly"]')
    #elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.2)
    # raise Exception("paymonthly")

    # find tariff in #standardRatesTable //*[@id="standardRatesTable"]/tbody/tr[1]/td[2]
    landline = browser.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')
    raise Exception("standardRatesTable")

    #assert "No results found." not in browser.page_source
    # browser.close()
    return landline


countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

for country in range(countries):
    try:
        print "O2's landline tariff for" + country + " is: " + get_o2_landline_tariff(country, 'Firefox')
    except NoSuchElementException:
        # e.g. NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"countryName"}
        
    except Exception as ex:
        print "An error occurred whilst trying to retrieve a tariff for " + country
        print "Message: "+ex.args
