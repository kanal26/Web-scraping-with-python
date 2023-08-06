# Web-scraping-with-python
Scrape details of all companies listed for different “Status” types, like Active, striked-off, under process of strike off from the zaubacorp.com website  and store them in a MongoDB collection.

# Requirements:
python
requests
from lxml import html
from pymongo import MongoClient
sys
from multiprocessing import Pool

# How to run this code
there are two source code files, one is zaubacorpcom_url_assignment.py and another is zaubacorpcom_data_assignment.py
first of all run url script zaubacorpcom_url_assignment.py to scrape urls from the website command is == >> python zaubacorpcom_url_assignment.py
after url script run data zaubacorpcom_data_assignment.py script for scrape the details from the website command is == >>python zaubacorpcom_data_assignment.py 1 1 1
first argument for total number of instance 
second  argument for current number of instance 
third argument for total number of requests
