This is just the place where the python code will write json objects which ```results.html``` will read for display purposes.
Can change the location by going to  ```../python/rss.py``` and changing the variable ```python data_dir.```

Directory currently has example files written from the program by inputting the rss feed:
```
http://rss.cnn.com/rss/edition_africa.rss
```
To display these results, simply load the webpage
```
/results.html?q=2015-11-17-14-44-43-313703,2015-11-17-14-44-44-016557,2015-11-17-14-44-47-688744,2015-11-17-14-44-48-014740,2015-11-17-14-44-48-524645,2015-11-17-14-44-48-944103,2015-11-17-14-44-50-001793,2015-11-17-14-44-51-335048,2015-11-17-14-44-51-605629,2015-11-17-14-44-52-763135,2015-11-17-14-44-54-835016,2015-11-17-14-44-56-715825,2015-11-17-14-44-58-461193,2015-11-17-14-45-01-130706,2015-11-17-14-45-02-827914,2015-11-17-14-45-08-716547,2015-11-17-14-45-10-438353,2015-11-17-14-45-11-230708,2015-11-17-14-45-14-007197,2015-11-17-14-45-14-501234,2015-11-17-14-45-15-144761,2015-11-17-14-45-15-682618,2015-11-17-14-45-16-135140,2015-11-17-14-45-19-463208,2015-11-17-14-45-20-058702
```
