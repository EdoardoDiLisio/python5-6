from scapy.all import *
from urllib3 import HTTPResponse
from scapy.layers.http import HTTPRequest
from scapy.layers.http import HTTPResponse

iPkt = 0

def process_pkt(pkt):
    global iPkt
    iPkt += 1
    print("Ho letto un pkt sulla tua macchina" + str(iPkt))

    if not pkt.haslayer(IP): # type: ignore
        return
    
    ip_layer = "IP_SRC:" + pkt[IP].src + "IP_DST:" + pkt[IP].dst + " " + str(pkt[IP].proto) + " " + str(pkt[IP].len); # type: ignore
    print(ip_layer)
    
    if pkt[IP].proto == 6: # type: ignore
        print("Ho riconosciuto un pacchetto TCP: TCP_SRC " + str(pkt[TCP].sport) + " TCP_DST: " + str(pkt[TCP].dport)) # type: ignore

    # if pkt[TCP].sport == 443 or pkt[TCP].dport == 443:  type: ignore
    #     print("Ho riconosciuto un pacchetto HTTPS: ") 
    if pkt[TCP].sport == 80: # type: ignore
        print("HTTP response")
        if pkt.haslayer(HTTPResponse):
            print(pkt[HTTPResponse].show())
    elif pkt[TCP].dport == 80: # type: ignore
        print("HTTP request")
        if pkt.haslayer(HTTPRequest):
            print(pkt[HTTPRequest].show())






sniff(iface="eth0",filter="tcp", prn=process_pkt)