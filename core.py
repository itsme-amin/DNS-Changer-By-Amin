import os

def shecan_dns():
    os.system('cmd /c "netsh interface ipv4 set dnsservers "Wi-Fi" static "178.22.122.100"')
    os.system('cmd /c "netsh interface ipv4 add dnsservers "Wi-Fi" "185.51.200.2" index=2"')

def begzar_dns():
    os.system('cmd /c "netsh interface ipv4 set dnsservers "Wi-Fi" static "185.55.226.26"')
    os.system('cmd /c "netsh interface ipv4 add dnsservers "Wi-Fi" "185.55.225.25" index=2"')

def riotplus_dns():
    os.system('cmd /c "netsh interface ipv4 set dnsservers "Wi-Fi" static "185.229.29.224"') 

def default_dns():
    os.system('cmd /c "netsh interface ipv4 set dns "Wi-Fi" dhcp"')

default_dns()