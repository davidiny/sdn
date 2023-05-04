from scapy.all import *
import sys

dst_ip    = sys.argv[1]
count     = int(sys.argv[2])
data_rate = int(sys.argv[3])

src_mac = RandMAC()
ip_src = RandIP()
sendp(Ether(src=src_mac)/IP(src=ip_src,dst=dst_ip), count=count, inter=(data_rate * (10**-6)))
