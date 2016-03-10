Optimor Python Developer Interview Task   

Background: A common task we perform is updating our knowledge­base of networks’ international calling costs (the cost per minute of calling a foreign country from the UK). These costs are typically based on country zones, although a list of zones and constituent countries is not always directly  available, so we may have to query the network’s website directly to obtain these results.  

Task: Install and use Selenium(1) (or another web crawling library for Python, if you feel another is more suitable) to scrape the following URL(2)for the price of calling a landline in the countries listed in(3) from an O2 Pay Monthly contract. Print the answers. 

We’re looking for good, readable Pythonic code, not just a hacked ­together script.    

1. http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html#   
2. http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk
3. Canada, Germany, Iceland, Pakistan, Singapore, South Africa  

Tips: 
We don’t expect you to have experience with Selenium or other web crawlers beforehand. working at Optimor involves being able to rapidly pick up tools/libraries without formal training. This task is designed to test that.
We expect you to make full use of the internet and available documentation. 
We don’t recommend researching the minutiae of XPath beforehand: you should be able  to consult http://www.w3schools.com/xpath/ during the project itself.  
We think the task should take 1­-1.5 hours, including installing and learning Selenium. 
The countries are actually stored in a JSON file loading and parsing this would be a better real­life solution, but in the context of this task, imagine this doesn’t exist ;)  

If you enjoyed the task, you may be interested in brownie points for:  
    good use of version control (git)
    solid resilience and reporting for errors  
    unit testing  
    
Questions 
If you have questions about the specification above, please email  sam.whitehall@optimorlabs.com    
Submission Please email code (GitHub/BitBucket repository, preferably) to hrteam@optimorlabs.com. 
You may wish to include a comment about how you found the task. 

http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html#  
http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk
Canada, Germany, Iceland, Pakistan, Singapore, South Africa
http://www.w3schools.com/xsl/xpath_intro.asp