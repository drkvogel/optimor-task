# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:50:55 2016

@author: Chris Bird
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import logging

def get_o2_landline_tariff(country, browser_name):

    url = 'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'

    if browser_name == 'Firefox':
        browser = webdriver.Firefox()
    else:
        raise Exception('Browser "' + browser_name + " not currently handled")

    # load intial page
    browser.get(url)

    # select country #countryName //*[@id="countryName"]
    logging.info("find #countryName")
    elem = browser.find_element_by_xpath('//*[@id="countryNa me"]')
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.2)

    # select Pay Monthly #paymonthly //*[@id="paymonthly"]
    logging.info("find #paymonthly")
    elem = browser.find_element_by_xpath('//*[@id="paymonthly"]')
    elem.click()
    time.sleep(0.2)

    # find tariff in #standardRatesTable //*[@id="standardRatesTable"]/tbody/tr[1]/td[2]
    logging.info("find tariff in #standardRatesTable")
    landline = browser.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')

    browser.close()
    return landline.text


#countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]
countries = ["Canada", "Germany"]

for country in countries:
    print "Getting landline tariff for " + country
    try:
        print "O2's landline tariff for " + country + " is: " + get_o2_landline_tariff(country, 'Firefox')
    except NoSuchElementException as ex:
        # e.g. NoSuchElementException: Message: Unable to locate element: {"method":"name","selector":"countryName"}
        print "NoSuchElementException: " + ex.message #str(ex.args)
    except Exception as ex:
        print "An error occurred whilst trying to retrieve a tariff for " + country
        print "Message: " + str(ex.args)
