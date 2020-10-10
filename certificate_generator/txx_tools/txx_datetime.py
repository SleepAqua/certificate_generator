'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:41:58
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:03:48
'''
import os
from datetime import datetime, timedelta


def parse_date_in_str(_str, datenum):
    """ Parse the formatters like %Y%m%d in str into the given date. """
    dn = datetime.strptime(str(datenum), "%Y%m%d")
    return dn.strftime(_str)

def datenum_to_season(path, datenum):
    """ Transform %Y%m%d into %Y%SEASON, e.g. 20180506 --> 2018S2 """
    month_season_table = {"01":"S1", "02":"S1", "03":"S1",
                          "04":"S2", "05":"S2", "06":"S2",
                          "07":"S3", "08":"S3", "09":"S3",
                          "10":"S4", "11":"S4", "12":"S4"}
    if not isinstance(datenum, str):
        datenum = str(datenum)
    year = datenum[:4]
    month = datenum[4:6]
    return year + month_season_table[month]

def is_datenum(datenum):
    """ Return True if given str is a date in format %Y%m%d """
    try:
        datetime.strptime(datenum, "%Y%m%d")
        return True
    except (ValueError, TypeError):
        return False

def start_of_time(t):
    """ Return the start of the passed time. e.g, 18:25:36 --> 18:00:00 """
    return t - timedelta(minutes=t.minute) - timedelta(seconds=t.second)

def end_of_time(t):
    """ Return the next hour of the passed time. e.g, 18:25:36 --> 19:00:00 """
    return t + timedelta(minutes=60) - timedelta(minutes=t.minute) - timedelta(seconds=t.second)
