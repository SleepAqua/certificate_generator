'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:27:40
LastEditors: Louis
LastEditTime: 2020-08-24 15:00:39
'''
import os
import logging

from .txx_os import make_parent_dir
from .txx_consts import TODAY


def single_lvl_logger(log_file=None, global_level=logging.INFO, handler_level=logging.INFO):
    """
    Awalys with a StreamHandler, if log_file is not None, a FileHandler will also be added.
    @log_file: the path of log file, default is None (StreamHandler).
    @global_level: the level for the global, default is INFO.
    @handler_level: the level for the handler, default is INFO.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    while logger.handlers:
        logger.handlers.pop()

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s -- %(module)s %(lineno)s: %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    if log_file:
        make_parent_dir(log_file)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(handler_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(handler_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def multi_lvl_logger(log_dir="$program_dir/log/%Y%m%d/"):
    """
    Seperately store the 3 level logs: INFO, WARNING, ERROR. With StreamHandler for sure.
    @log_dir: the directory for saving the three logs. Log files named by data and level.
    """
    lvl_dict = {"info": logging.INFO, "warning": logging.WARNING, "error": logging.ERROR}

    logger = logging.getLogger()
    while logger.handlers:
        logger.handlers.pop()

    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    logger.addHandler(console)

    for lvl in ["info", "warning", "error"]:
        log_path = os.path.join(log_dir, "{}_{}.log".format(TODAY, lvl))
        make_parent_dir(log_path)
        handler = logging.FileHandler(log_path, "a")
        handler.setLevel(lvl_dict[lvl])
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s -- %(module)s %(lineno)s: %(message)s'))
        logger.addHandler(handler)

    return logger
