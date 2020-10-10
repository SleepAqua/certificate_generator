'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 15:19:25
LastEditors: Louis
LastEditTime: 2020-08-18 14:59:49
'''
import os
from time import perf_counter
from functools import wraps

from .txx_log import single_lvl_logger
from .txx_consts import TODAY
from .txx_os import make_parent_dir
from .txx_df import add_number_to_cols


LOGGER = single_lvl_logger()

def timer(func):
    """ Print the time cost by the decorated function. """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        LOGGER.info(f"Time used: {func.__name__, round(perf_counter()-start_time, 2)}s")
        return result
    return wrapper

def dump_without_overwrite(*args_pd, **kwargs_pd):
    """ Dump the file. If the file already exist, rename the old file and then dump. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            file_content, file_path = func(*args, **kwargs)
            if os.path.isfile(file_path):
                backup_path = file_path.replace(".csv", f"_before_{TODAY}.csv")
                os.rename(file_path, backup_path)
                LOGGER.warning(f"{file_path} exists, renamed old file to {backup_path}")
            make_parent_dir(file_path)
            file_content = add_number_to_cols(file_content)
            file_content.to_csv(file_path, *args_pd, **kwargs_pd)
            LOGGER.info(f"File saved to: {file_path}")
            return file_content, file_path
        return wrapper
    return decorator

def dump_with_overwrite(*args_pd, **kwargs_pd):
    """ Dump the file. If the file already exist, report and overwrite. """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            file_content, file_path = func(*args, **kwargs)
            if os.path.isfile(file_path):
                LOGGER.warning(f"{file_path} exists, overwrited")
            make_parent_dir(file_path)
            file_content = add_number_to_cols(file_content)
            file_content.to_csv(file_path, *args_pd, **kwargs_pd)
            LOGGER.info(f"File saved to: {file_path}")
            return file_content, file_path
        return wrapper
    return decorator