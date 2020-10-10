'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 15:39:07
@LastEditors: Louis
@LastEditTime: 2020-06-15 15:53:33
'''
import re
import pandas as pd


def add_number_to_cols(df):
    """ Add number ahead of column names, e.g. [col1, col2] --> [[1]col1, [2]col2] """
    df.columns = [f"[{n}]{col}" for n, col in enumerate(df.columns)]
    return df

def remove_number_from_cols(df):
    """ Remove number ahead of column names, e.g. [[1]col1, [2]col2] --> [col1, col2] """
    df = df.rename(columns={col:re.sub("\[\d+\]", "", col) for col in df.columns})
    return df
