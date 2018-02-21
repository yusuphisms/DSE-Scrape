#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 01:58:50 2018

@author: yo-my-bard
"""

import pandas as pd
from sqlalchemy import create_engine

def addToDaily():
    """
    Add the daily DSE Market data to the SQLite database.
    """
    tables = pd.read_html("http://www.dse.co.tz/dse/market-report")
    daily = tables[0]
    engine = create_engine("sqlite:////Users/Muse/Documents/GitHub/DSEScrape/DSE-Scrape/DSEScrape.db")
    daily.drop(["Prev Closing Price", "Price Change (%)"], axis=1, inplace=True)
    daily.rename(columns = {"Closing Price": "ClosingPrice"}, inplace=True)
    daily.to_sql("DSEDaily", engine, if_exists='append', index = False)
    

def addToSummary():
    """
    Add the market summary data to the SQLite database.
    
    """
    