#!/usr/bin/env python3
from instabot import Bot
import os
import argparse

try:
    input = raw_input
except:
    pass

def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", dest="username", help="Instagram username")
    parser.add_argument("-p", "--password", dest="password", help="Account's password")
    parser.add_argument("-i", "--image", dest="image", help="Image path")
    parser.add_argument("-c", "--caption", dest="caption", help="Caption of the post")
    return parser.parse_args()

def upload_pic(options):
    if not options.username:
        username = input("Enter your instagram's username: ")
    else:
        username = options.username
    
    if not options.password:
        password = input("Enter password: ")
    else:
        password = options.password
    
    if not options.image:
        image = input("Enter image path along with the name: ")
    else:
        image = options.image
    
    if not options.caption:
        caption = input("Enter caption [Default: blank]: ")
    else:
        caption = options.caption

    instaBot = Bot()
    instaBot.login(username=username, password=password)
    instaBot.upload_photo(image, caption=caption)

    

try:
    options = set_args()
    upload_pic(options)


except KeyboardInterrupt:
    os.system("echo '\n[.] Terminating the process'")