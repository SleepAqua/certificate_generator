'''
@version: Python 3.7.3
@Author: Louis
@Date: 2020-06-15 13:41:58
@LastEditors: Louis
@LastEditTime: 2020-06-15 17:40:27
'''
import os


def make_parent_dir(path_):
    """ Create the parent directory of given directory or file if not exist. """
    parent_dir = os.path.dirname(path_)
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)

def make_dir(path_):
    """ Create the given directory if not exist. """
    if not os.path.isdir(path_):
        os.makedirs(path_)

def count_files(dir_):
    """ Counter the file numbers of given directory. If the directory does not exist, return None. """
    if not os.path.isdir(dir_):
        return None
    return len(os.listdir(dir_))
