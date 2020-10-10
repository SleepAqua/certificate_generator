'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 15:00:28
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:53:26
'''
import re

from .txx_consts import TODAY

"""
() are important for "|" logic!
"""

# Finance
ASHARE_STK_REGEX = '^60.*SH|^00.*SZ|^30.*SZ'
ASHARE_IDX_REGEX = '^000.*SH|^399.*SZ'
ASHARE_INFUND_REGEX = '^5.*SH|^17.*SZ|^18.*SZ|^15.*SZ|^16.*SZ|^5.*SZ'

# Date
DATENUM_21_CENTURY_REGEX = "(20[0-9][0-9])([0][1-9]|[1][0-2])([0][1-9]|[1-2][0-9]|[3][0-1])"
MONTH_REGEX = "([0][1-9]|[1][0-2])"
DAY_REGEX = "([0][1-9]|[1-2][0-9]|[3][0-1])"

# Time
TIME_24_REGEX = "([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])"
HOUR_24_REGEX = "([0-1][0-9]|[2][0-3])"

TIME_12_REGEX = "([0][0-9]|[1][0-1]):([0-5][0-9]):([0-5][0-9])"
HOUR_12_REGEX = "([0][0-9]|[1][0-1])"

MIN_SEC_REGEX = "([0-5][0-9])"

# Datetime
DATE_21_CENTURY_TIME_24_REGEX = DATENUM_21_CENTURY_REGEX + " " + TIME_24_REGEX
DATE_21_CENTURY_TIME_12_REGEX = DATENUM_21_CENTURY_REGEX + " " + TIME_12_REGEX
