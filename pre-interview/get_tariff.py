# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 22:50:55 2016

@author: Chris Bird
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time, os, logging

def get_o2_landline_rate(country, browser):
    """ Get rate for calling landlines from O2.
    browser     -- selenium browser object
    country     -- country name
    """
    url = 'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'
    browser.get(url)
    time.sleep(0.2)
    assert "International" in browser.title

    logging.info("find #countryName")
    elem = browser.find_element_by_xpath('//*[@id="countryName"]')
    elem.send_keys(country)
    elem.send_keys(Keys.RETURN)
    time.sleep(0.2)

    logging.info("find #paymonthly")
    elem = browser.find_element_by_xpath('//*[@id="paymonthly"]')
    elem.click()
    time.sleep(0.2)

    logging.info("find rate in #standardRatesTable")
    landline = browser.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')

    return landline.text


def get_rate(browser, network_name, call_type, contract_type, country):
    """ Scrape a tariff
    browser         -- selenium browser object
    network_name    -- name of providers
    call_type       -- "landline"|"mobile"|"text"
    contract_type   -- "monthly"|"payAsYouGo"
    country         -- country name
    """
    if network_name == 'O2':
        pass
    else:
        raise Exception('Network "' + network_name + " not currently handled")
    # ... etc

    result = get_o2_landline_rate(country, browser)
    return result

def get_tariffs():
    """ scrape network providers' websites for rates """
    browser = webdriver.Firefox() # for the purposes of this task; a reallife version would cater for many different browsers
    time.sleep(0.5) # wait for browser to initialise

    countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

    for country in countries:
        print "Getting landline rate for " + country
        try:
            print "O2's landline rate for " + country + " is: " + get_rate(browser, "O2", "landline", "monthly", country)
        except NoSuchElementException as ex:
            # e.g. Message: Unable to locate element: {"method":"name","selector":"countryName"}
            print "NoSuchElementException: " + ex.message #str(ex.args)
        except Exception as ex:
            print "An error occurred whilst trying to retrieve a rate for " + country
            print "Message: " + ex.message

    browser.close()

if __name__ == "__main__":
    if os.getenv('DEBUGGING'):
        logging.basicConfig(level=logging.INFO) # logging.DEBUG
    get_tariffs()
