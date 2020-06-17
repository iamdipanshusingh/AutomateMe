#!/usr/bin/env python3
import os

try:
    input = raw_input
except:
    pass

try:
    app_name = input("Enter app's name: ")
    app_version = input("Enter app's version: ")
    pubspec_path = input("Enter app's root folder location with respect to current folder: ")

    path = pubspec_path + "build/app/outputs/apk/release/app-release.apk"

    apk_name = app_name + '-v' + app_version

    os.system("flutter clean; flutter pub get;")
    os.system("echo [+] Cleaned cache and ran 'flutter pub get'")
    os.system("echo [+] Creating apk")
    os.system("flutter build apk")
    os.system("cp " + path + " ./" + app_name + '.apk')
    os.system("echo [+] Apk created")
    os.system("nautilus .")
except KeyboardInterrupt:
    os.system("echo '\n[.] Terminating the process'")
