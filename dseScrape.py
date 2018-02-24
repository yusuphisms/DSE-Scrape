#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 01:58:50 2018

@author: yo-my-bard

Scraping the Dar Es Salaam Stock Exchange and saving it to a database.
Exploring means to automate the process, build graphs of companies over time,
and make data readily accessible.
"""

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///DSEScrape.db")

def addToDaily():
    """
    Add the daily DSE Market data to the SQLite database.
    
    Currently requires user input of the date as a string in the format "2018-02-21"
    
    """
    date = input("Enter the date (format '2018-02-21') for this Daily DSE data: ")
    tables = pd.read_html("http://www.dse.co.tz/dse/market-report")
    daily = tables[0]
    daily.drop(["Prev Closing Price", "Price Change (%)"], axis=1, inplace=True)
    daily.rename(columns = {"Closing Price": "ClosingPrice"}, inplace=True)
    daily["ClosingDate"] = date
    daily.to_sql("DSEDaily", engine, if_exists='append', index = False)
    

def addToSummary():
    """
    Add the market summary data to the SQLite database.
    
    Currently requires user input of the date as a string in the format "2018-02-21"
    
    """
    date = input("Enter the date (format '2018-02-21') for this Market Summary data: ")
    tables = pd.read_html("http://www.dse.co.tz/dse/market-report")
    summary = tables[2]
    summary.rename(columns={1: "ClosingPrice", 0:"Indices"}, inplace=True)
    summary.dropna(axis=1, how='any', inplace=True )
    summary.drop([0], axis=0, inplace=True)
    summary["ClosingDate"] = date
    summary.to_sql("MarketSummary", engine, if_exists='append', index=False)   

addToDaily() #Input the date format when prompted to add data to Daily DSE
addToSummary() #Input the date format when prompted to add data to Market Summary
