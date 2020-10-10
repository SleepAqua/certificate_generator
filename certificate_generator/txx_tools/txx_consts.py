'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:27:40
LastEditors: Louis
LastEditTime: 2020-08-19 15:06:25
'''
import os
import sys
from enum import Enum
from datetime import datetime


TODAY = datetime.now().strftime("%Y%m%d")
TODAY_ = datetime.now().strftime("%Y-%m-%d")
TIME = datetime.now().strftime("%H:%M:%S")
NOW = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

TODAY_OBJ = datetime.now().date()
TIME_OBJ = datetime.now().time()
NOW_OBJ = datetime.now()

SEP_MAP = {"xls": "\t", "XLS": "\t", "CSV": ",", "csv": ",", "xlsx": "\t", "XLSX": "\t"}

EQUITY_TRADE_DAYS_PATH = "/dat/all/Equity/Wind/Daily/list/tradedays.csv"
FUTURE_TRADE_DAYS_PATH = "/dat/all/Future/WIND/list/tradedays.csv"

MARKET_MAP = {"SZSE": "SZ", "SSE": "SH", "SZE": "SZ"}
