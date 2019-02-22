#!/usr/bin/python
#Luu ubah,ngk akan jadiin luu mastah
#Luu recoder,ngk akan jadiin luu master
#Luu reedit,malah jadiin luu hacker tersakit
#3D0_CHU11/+62895627525979
print "Login creating by 3D0_CHU11"
newjudul = raw_input("Judulnya (baru): ")
newuser = raw_input("username (baru): ")
newpass = raw_input("password (baru): ")

fo = open(".login.py","w")

loginscript1 = """import os, sys
"""

loginscript2 = """print ("0={===>"""

loginscript3 = newjudul

loginscript4 = """<===}=0")
"""

loginscript5 = """username = '"""

loginscript6 = newuser

loginscript7 = """'
""" 

loginscript8 = """password = '"""

loginscript9 = newpass

loginscript10 = """'

def restart():
        cobalagi = sys.executable
        os.execl(cobalagi, cobalagi, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username: 
                pwd = raw_input("password : ")

                if pwd == password: 
                        sys.exit()

                else:
                        print "Password salah"
                        print "Silahkan Login Kembali"
                        restart()

        else:
                print "Username salah"
                print "Silahkan Login Kembali"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()"""


fo.write(loginscript1)
fo.write(loginscript2)
fo.write(loginscript3)
fo.write(loginscript4)
fo.write(loginscript5)
fo.write(loginscript6)
fo.write(loginscript7)
fo.write(loginscript8)
fo.write(loginscript9)
fo.write(loginscript10)

print "Halaman Login telah dibuat (:SS jika perlu:)"
print "untuk cara pengguanaan silahkan buka halaman awal lalu pilih cara pakai pada nomer 2"
print "toologin by 3D0_CHU11"

fo.close()
#walaikumsallam WR.WB
