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
    parser.add_argument("-n", "--name", dest="name", help="App name")
    parser.add_argument("-p", "--path", dest="path", default='../../', nargs='?',
                        const='../../', help="Path of your app's root folder")
    parser.add_argument("-t", "--type", dest="type", default='apk', const='apk', nargs='?',
                        choices=['apk', 'aab'], help="Kind of applicaion you want to create")
    options = parser.parse_args()

    if not options.name:
        app_name = input("What do you want to call your app ? ")
    else:
        app_name = options.name

    if not options.path:
        pubspec_path = input(
            "Enter app's root folder location with respect to current folder: ")
    else:
        pubspec_path = options.path

    if not options.type:
        app_type = 'apk'
    else:
        app_type = options.type

    for apk in glob.glob("*.apk"):
        if apk:
            os.remove(apk)
    for aab in glob.glob("*.aab"):
        if aab:
            os.remove(aab)

    common_path = pubspec_path + "build/app/outputs/"
    if app_type == 'apk':
        path = common_path + "apk/release/app-release.apk"
    else:
        path = common_path + "bundle/release/app-release.aab"

    os.system("flutter clean; flutter pub get;")
    os.system("echo [+] Cleaned cache and ran 'flutter pub get'")
    os.system("echo [+] Creating apk")

    if app_type == 'apk':
        os.system("flutter build apk")
    else:
        os.system("flutter build appbundle")

    if app_type == 'apk':
        os.system("cp " + path + " ./" + app_name + '.apk')
    else:
        os.system("cp " + path + " ./" + app_name + '.aab')

    os.system("echo [+] " + app_type + " created")

    os.system("nautilus .")

except KeyboardInterrupt:
    os.system("echo '\n[.] Terminating the process'")
