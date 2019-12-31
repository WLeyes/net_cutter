#!/usr/bin/env python
import netfilterqueue
import subprocess


def process_packet(packet):
    print(packet)
    packet.drop()


try:
    subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C \n")
    subprocess.call(["iptables", "--flush"])
