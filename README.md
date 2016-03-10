## Optimor Python Developer Interview Task

I had done this sort of thing before with `BeautifulSoup`, but `Selenium` and `xpath` was new to me.

I have mainly been doing C++ and JavaScript at work recently, so my Python is a bit rusty! And so it took me a bit longer than 1.5hrs.

I found Chrome Dev Tools' "copy Xpath" feature very useful!

I tried to make the functions modular and parameterised, as though it were a library in real life that, with some more development, could handle different browsers, contract types, networks, etc. Though starting a new browser and then closing it for each scrape seemed inefficient so I just used Firefox and passed it between the functions.

I used `pylint` at the end to see if I'd made any style errors - two "Pythonic" style recommendations I'm not sure I agree with are the limit on line length, and a minimum variable name length - hence, I set `disable=line-too-long, invalid-name` in `~/.pylintrc`! However that is just my personal view at the moment and I haven't yet had to share Python code with other people...

I'm afraid I don't know much about Unit Testing so there is none.