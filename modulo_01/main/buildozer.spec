[app]
title = JogoDaForca
package.name = jogodaforca
source.dir = .
requirements = kivy

[buildozer]
# Android settings (descubra como preencher corretamente em https://buildozer.readthedocs.io/en/latest/)

android.arch = armeabi-v7a
android.ndk_path = /path/to/your/android-ndk-r20b
android.sdk_path = /path/to/your/android-sdk
android.api = 28

# Ensure build the app with Python 3.8.6
# (you can also use python3 or python2, but 3.8.6 is recommended)
# p4a.branch = master
# p4a.source_dir = /path/to/python-for-android

