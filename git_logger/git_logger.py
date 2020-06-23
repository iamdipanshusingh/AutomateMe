#!/usr/bin/env python3
import os
import glob
import platform
import contextlib
import argparse

try:
    input = raw_input
except:
    pass

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--from", dest="fromHash",
                        help="Commit hash from which you want to get the log, excluding this commit")
    parser.add_argument("-t", "--to", dest="toHash",
                        help="Commit hash up to which you want to get the log")
    parser.add_argument("-p", "--path", dest="path",
                        help="Path, where the log will be saved, Desktop is default")
    parser.add_argument("-n", "--name", dest="name", help="Name of log file")
    options = parser.parse_args()

    if not options.fromHash:
        _from = input('Enter commit hash from when you want to get the commit details, this is exclusive: ')
    
    if not options.toHash:
        _to = input('Enter commit hash up to when you want to get the commit details, this is inclusive: ')

    if not options.path:
        _path = input('Where do you want to save your git-log? [Press enter for Desktop]')
        if not _path:
            _path = '~/Desktop/'

    if not options.name:
        _name = input('What do you want to name your git-log? ')

    os.system("git log --oneline " + _from + "..." + _to + " > " + _path + _name)

    os.system("nautilus " + _path)

except KeyboardInterrupt:
    os.system("echo '\n[.] Terminating the process'")
