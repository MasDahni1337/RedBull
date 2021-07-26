import sys
import time
import random
class werno:
    biasa = "\033[1;37m"
    abang = "\033[1;31m"
    ijo = "\033[1;32m"
    kuning = "\033[0;33m"
    biru = "\033[1;34m"
    hasil = "\033[1;37;42m"
    merah_putih = "\033[1;37;41m"
    njambon = "\033[1;33m"
    normal = "\033[0;37;40m"

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