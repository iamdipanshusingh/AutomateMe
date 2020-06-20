#!/usr/bin/env python3
import os
import glob
import platform
import contextlib
from pydub import AudioSegment
from pydub.playback import play

try:
    input = raw_input
except:
    pass

try:
    app_name = input("What do you want to call your app ? ")
    pubspec_path = input("Enter app's root folder location with respect to current folder: ")

    for apk in glob.glob("*.apk"):
        if apk:
            os.remove(apk)
    for aab in glob.glob("*.aab"):
        if aab:
            os.remove(aab)

    path = pubspec_path + "build/app/outputs/apk/release/app-release.apk"

    os.system("flutter clean; flutter pub get;")
    os.system("echo [+] Cleaned cache and ran 'flutter pub get'")
    os.system("echo [+] Creating apk")
    os.system("flutter build apk")
    os.system("cp " + path + " ./" + app_name + '.apk')
    os.system("echo [+] Apk created")

    sound = AudioSegment.from_mp3('accomplished.mp3')
    play(sound)
    
    os.system("nautilus .")

except KeyboardInterrupt:
    os.system("echo '\n[.] Terminating the process'")
