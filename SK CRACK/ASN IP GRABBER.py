import os, json

try:
    import requests
except:
    os.system('pip install requests --user')
try:
    import ipranges
except:
    os.system('pip install ipranges --user')

ASN = input('ASN >> : ')
r = requests.get(f'https://api.bgpview.io/asn/{ASN}/prefixes').json()
rather = r['data']['ipv4_prefixes']
for Yh in range(0, int(len(rather)) - 1):
    IPM = r['data']['ipv4_prefixes'][Yh]
    Jahl = IPM['ip'] + '/' + str(IPM['cidr'])
    IPL = ipranges.IP4Net(Jahl)
    for IP in IPL:
        print(IP)
        open(f'{ASN}_IPS.txt', 'a', errors='ignore', encoding='utf-8').write(f'{IP}\n')

