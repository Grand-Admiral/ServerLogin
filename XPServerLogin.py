import os
import time
import ScannCreds
scannIP = str(input("NetIP/Subnet :")).lower()
if scannIP == "y":
    print(ScannCreds.creds())
else:
    print(os.system('nmap -sn -v ' + scannIP))
    IP = str(input("IP :"))
    User = str(input("UserName :"))
    print(os.system('ssh '+ User + '@' + IP))
