"""Custom topology example

Two hosts directly connected by a switch
"""
import sys

#num = len(sys.argv)
#print("Arguments:", end = " ")
#for i in range(1, num):
#    print(sys.argv[i], i, end = " ")

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller, OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI

rate = 1

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        switch1 = self.addSwitch( 's1', switch=OVSSwitch )
        

        # Add links
        self.addLink( leftHost, switch1, cls=TCLink, bw=rate)
        self.addLink( rightHost, switch1, cls=TCLink, bw=rate)

def create():
        topo = MyTopo()
        #c1 = Controller('c1', port=6633, cls=TCLink, bw=rate)
        net = Mininet(topo=topo, link=TCLink)
        net.start()
        CLI( net )
        net.stop()

if __name__ == '__main__':
        create()

topos = { 'mytopo': ( lambda: MyTopo() ) }
