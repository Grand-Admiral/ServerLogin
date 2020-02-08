import os
def creds():
    scannIP = str("Your LAN IP/Subnet you wish to use '/24' is standard")
    print(os.system('nmap -sn -v ' + scannIP))
    IP = str(input("IP :"))
    User = str("your username")
    print(os.system('ssh '+ User + '@' + IP))
    
