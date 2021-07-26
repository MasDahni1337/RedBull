import os
from android import *
from windows import *
from posix import PRIO_PGRP

def awal():
    os.system('neofetch --ascii /home/dahni/ascii/bull1.txt')
    print("W3lcome to RedBull RAT Tools")
    print("[1] Build virus server")
    print("[2] Bind server to apk/exe")
    print("[3] Exploit victim")

def banner():
    print("Chose your exploit method!")
    print("[1] Android")
    print("[2] Windows")
    print("[3] Linux")
    print("[4] iOS")
    print("[5] MacOS")
    print("")

def bind():
    print("Chose your bind object!")
    print("[1] Original Apk")
    print("[2] Exe Windows")

def eksekusi():
    awal()
    x = input("chose : ")
    load()
    if x == "1":
        banner()
        pilih = input("chose : ")
        load()
        if pilih == "1":
            ban_andro()
            return eksekusi()
        elif pilih == "2":
            win_vir()
            return eksekusi()
    elif x == "2":
        bind()
        pilih = input("chose : ")
        if pilih == "1":
            bind_apk()
            return eksekusi()
    elif x == "3":
        print("this for exploit function")
    else:
        print("masukan input yg bener")

eksekusi()