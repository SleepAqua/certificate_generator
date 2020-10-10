'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 17:06:58
@LastEditors: Louis
@LastEditTime: 2020-07-27 18:20:49
'''
from .txx_log import single_lvl_logger

LOGGER = single_lvl_logger()

try:
    import keyring
except ModuleNotFoundError:
    LOGGER.warning("keyring module not import, try pip install keyring or ignore this")


def register(subject, username, password):
    """
    Save your password inside your computer permenately.
    """
    keyring.set_password(subject, username, password)

def peek_password(subject, username):
    """
    Access your password inside your computer.
    """
    return keyring.get_password(subject, username)