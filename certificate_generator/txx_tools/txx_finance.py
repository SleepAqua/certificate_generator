'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:41:58
LastEditors: Louis
LastEditTime: 2020-08-19 11:55:41
'''
import sys
import pandas as pd
from functools import partial
from datetime import date, time, datetime, timedelta

from .txx_consts import EQUITY_TRADE_DAYS_PATH, FUTURE_TRADE_DAYS_PATH
from .txx_log import single_lvl_logger


LOGGER = single_lvl_logger()

def is_trade_day(datenum, date_file=EQUITY_TRADE_DAYS_PATH):
    """
    Is the given datenum a trade day or not.
    @date_file: a csv file containing only dates series
    """
    trade_days = pd.Series(pd.read_csv(date_file, header=None, dtype={0:str})[0])
    return datenum in set(trade_days.loc[(trade_days >= datenum)])

def get_file_days_between(start_date, end_date, date_file=EQUITY_TRADE_DAYS_PATH):
    """ 
    Return a Series containing the dates betweeen start_date and end_date in the date_file.
    @date_file: a csv file containing only dates series
    """
    trade_days = pd.Series(pd.read_csv(date_file, header=None, dtype={0:str})[0])
    return trade_days.loc[(trade_days >= start_date) & (trade_days <= end_date)]

get_equity_days_between = partial(get_file_days_between, date_file=EQUITY_TRADE_DAYS_PATH)
get_future_days_between = partial(get_file_days_between, date_file=FUTURE_TRADE_DAYS_PATH)

def get_last_n_tradeday(cur_date, n, date_file=EQUITY_TRADE_DAYS_PATH):
    """ 
    Return a Series of 'n' number of dates before 'cur_date' in the 'date_file'.
    """
    if not n:
        if is_trade_day(cur_date, date_file):
            return cur_date
        else:
            LOGGER.warning(f"{cur_date} is not a trade day")
            return cur_date
    trade_days = pd.Series(pd.read_csv(date_file, header=None, dtype={0:str})[0])
    return trade_days.loc[(trade_days < cur_date)].tail(n).iloc[0]

def format_secode(x):
    """
    Add market suffix SH or SZ for stock code.
    """
    if not isinstance(x, str):
        x = str(x.zfill(9))
    if x[0] == "6" or x[0] == "9":
        return f"{x}.SH"
    elif x[0] == "0" or x[0] == "2" or x[0] == "3":
        return f"{x}.SZ"
    else:
        LOGGER.warning("This is not a SecuCode for stocks.")
        return None

def argv_to_trade_days(argv, tradeday_type="equity", history_start= "20000104"):
    """
    Parse arguments from user command:
    1. xx.py %Y%m%d %Y%m%d --> make data from left date to right date
    2. xx.py yesterday --> make data of last trade day
    3. xx.py tomorrow/tmr --> make data of next trade day
    4. xx.py today --> make data of today
    5. xx.py history --> make data of history (default history start date is 2000-01-04)
    6. xx.py --> make data of today

    tradeday_type: which trade day file to read: equity/future (default trade day type is equity)
    """
    if len(argv) == 3:
        first_datenum = argv[1]
        last_datenum = argv[2]
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'yesterday' or sys.argv[1] == 'last':
            first_datenum = datetime.strftime(datetime.now()-timedelta(1), "%Y%m%d")
            last_datenum = datetime.strftime(datetime.now()-timedelta(1), "%Y%m%d")
        elif sys.argv[1] == 'tomorrow' or sys.argv[1] == "tmr":
            first_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
            last_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
        elif sys.argv[1] == 'today':
            first_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
            last_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
        elif sys.argv[1] == 'history':
            first_datenum = history_start
            last_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
        else:
            raise NotImplementedError('mode: last/today/history')
    elif len(sys.argv) == 1:
        first_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
        last_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
    else:
        raise NotImplementedError('input error')
    if tradeday_type == "equity":
        trade_days= get_equity_days_between(first_datenum, last_datenum)
    elif tradeday_type == "future":
        trade_days= get_future_days_between(first_datenum, last_datenum)
    else:
        raise NotImplementedError('tradeday_type: equity/future')
    return trade_days


def simple_argv_days(argv, tradeday_type="equity"):
    """
    Parse arguments from user command (simple version):
    1. xx.py %Y%m%d %Y%m%d --> make data from left date to right date
    2. xx.py --> make data of today

    tradeday_type: which trade day file to read: equity/future (default trade day type is equity)
    """
    if len(argv) == 3:
        first_datenum = argv[1]
        last_datenum = argv[2]
    elif len(sys.argv) == 1:
        first_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
        last_datenum = datetime.strftime(datetime.now(), "%Y%m%d")
    else:
        raise NotImplementedError('input error')
    if tradeday_type == "equity":
        trade_days= get_equity_days_between(first_datenum, last_datenum)
    elif tradeday_type == "future":
        trade_days= get_future_days_between(first_datenum, last_datenum)
    else:
        raise NotImplementedError('tradeday_type: equity/future')
    return trade_days