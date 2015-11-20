## What it Does

Analysts were spending too much time monitoring RSS feeds of news articles. Nounalizer helps distill this information faster than reading and presents the data in a visually pleasing manner. The underlying idea that provides the theory for why this works is that important things are nouns and will be mentioned more (in aggregate) than things that are not important. Let's then show noun frequency for individual RSS feeds.


![Demo](https://github.com/ngageoint/Nounalizer/blob/master/images/demo_comp.gif)

###Architecture


This tool is designed to sit on a web server with php. Users will come to the website, enter in text for an rss feed link, referenced as ```javascript $('#rss').val()``` in ```index.html``` and ```rss``` in ```python/rss.py```. An ajax call is then made to ```python.php``` which executes the python script. The script executes by writing temporary files to ```python tmp_dir``` and ```python data_dir``` as declared in ```python/rss.py```. After reading stdout, waiting for python to write the name of the files it wrote to the ```data/``` directory, ```python.php``` returns the string of comma-separated file names to ```index.html``` which redirects to ```results.html```.

###Directory Structure


* `css/`  --  contains css files for `index.html`, `results.html`, and `rats.html`
* `data/`  --  empty folder to which `python.php` writes files
* `js/`  --  contains javascript files
* `python/`  --  contains python file that `python.php` calls
* `README.md`  --  development documentation
* `index.html`  --  main welcome page for Nounalizer
* `python.php`  --  file that is called by `index.html` to execute `python/rss.py`
* `rats.html`  --  the best error page ever made
* `results.html`  --  displays aggregate results of comma-separated files names in `data/` which are referenced following `q=` tag in the url of the file
* `seal.png`  --  NGA seal referenced in `index.html` for introduction page

###Dependencies

Python:
* [spaCy](http://www.spacy.io)  --  MIT
* [python-goose](https://github.com/grangier/python-goose)  --  Apache 2.0
* [Feedparser](https://github.com/kurtmckee/feedparser)  --  [Copyright](https://github.com/kurtmckee/feedparser/blob/develop/LICENSE) (c) 2010-2015, Kurt McKee

javascript:
* [GreenSock](http://greensock.com/)  --  [Copyright](https://greensock.com/standard-license) (c) 2008-2015, GreenSock
* [d3js](https://github.com/mbostock/d3)  --  [Copyright](https://github.com/mbostock/d3/blob/master/LICENSE) (c) 2010-2015, Michael Bostock
* [ScrollMagic](http://scrollmagic.io/)  --  MIT
* [jquery](https://jquery.com/)  --  [Copyright](https://github.com/jquery/jquery/blob/master/LICENSE.txt) jQuery Foundation and other contributors

##Contributing
Nounalizer was developed at the National Geospatial-Intelligence Agency (NGA). The government has "unlimited rights" and is releasing this software to increase the impact of government instruments by providing developers with the opportunity to take things in new directions. The software use, modification, and distribution rights are stipulated within the Apache 2.0 License. See also NOTICE file for additional information regarding dependency attribution. 

Software source code previously released under an open source license and then modified by NGA staff is considered a "joint work" (see 17 USC 101); it is partially copyrighted, partially public domain, and as a whole is protected by the copyrights of the non-government authors and must be released according to the terms of the original open source license.

