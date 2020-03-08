import os
import time
import ScannCreds
scannIP = str(input("NetIP/Subnet :")).lower()

if scannIP == "y" or scannIP == "5":
    print(ScannCreds.creds())
else:
    devname = str(input("DevName :"))
    str(os.system('nmap -sn -v ' + scannIP + ' > NetList.txt'))
    with open('NetList.txt') as f:#open text file
        lines = [line.rstrip() for line in f]
    for item in lines:#find my desired device
        if item.find(devname) != -1:
            print(item)
    
    IP = str(input("IP :"))
    User = str(input("UserName :"))
    print(os.system('ssh '+ User + '@' + IP))
