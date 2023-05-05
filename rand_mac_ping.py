from scapy.all import *
import sys

dst_ip    = sys.argv[1]
count     = int(sys.argv[2])
data_rate = int(sys.argv[3])
padding      = int(sys.argv[4])

src_mac = RandMAC()
ip_src = RandIP()
sendp(Ether(src=src_mac)/IP(src=ip_src,dst=dst_ip)/ICMP()/Raw(RandString(size=padding)), count=count, inter=(data_rate * (10**-6)))
