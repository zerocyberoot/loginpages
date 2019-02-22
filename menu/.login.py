import os, sys
print ("0={===>asw<===}=0")
username = 'asw'
password = 'asw'

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
        restart()