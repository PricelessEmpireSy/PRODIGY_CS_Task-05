from scapy.all import sniff
from scapy.all import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"Packet captured:\nSource IP: {ip_layer.src}\nDestination IP: {ip_layer.dst}\nProtocol: {packet.proto}\nPayload: {packet.payload}\n")

def main():
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
