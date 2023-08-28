# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:03:02 2023

@author: Rohan_Sarpal
"""

import pandas as pd
from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BingImageCrawler
from pathlib import Path
#Change 'BingImageCrawler' to 'GoogleImageCrawler' for google search at line 25

mitFilter=True  #change to False to remove Filters
#Set the filter to creative vommons license and set if th eimage is either
#photo, face, clipart, linedrawing, or animated
filters = dict(type='photo',license='commercial,modify')
howmany= 100
names=pd.read_csv('path of csv file')
l1=list(names.n)
print(l1)
subset=names.n
print(subset)

for keyword in subset:
     crawler = BingImageCrawler(
         parser_threads=5,
         downloader_threads=5,
         storage={'root_dir': 'path of directory/{}'.format(keyword)}
     )    
     if mitFilter==True:
         crawler.crawl(keyword=keyword, filters=filters, max_num=howmany, min_size=(500, 500))
     else:
         crawler.crawl(keyword=keyword, max_num=howmany, min_size=(500, 500))