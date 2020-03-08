import os
def creds():
    scannIP = str("Your LAN IP/Subnet you wish to use '/24' is standard")
    print(os.system('nmap -sn -v ' + scannIP + ' > NetList.txt'))
    
    with open('NetList.txt') as f:#open text file
        lines = [line.rstrip() for line in f]
    for item in lines:#find my desired device
        if item.find('Device to search') != -1:
            print(item)
            
    IP = str(input("IP :"))
    User = str("your username")
    print(os.system('ssh '+ User + '@' + IP))
    
