#!usr/bin/python2.7
# -*- coding: utf-8 -*-
#
#Miguel Angel Martinez 121119
#This tool allows to find all open ports with NMAP, you can
#scan IP Segments, IP Range or a Single IP
#

import argparse
import nmap

nm = nmap.PortScanner()


print (" ____  ____  ____  _      _            ____ ___  _")
print ("/ ___\/   _\/  _ \/ \  /|/ \  /|      /  __\\  \//")
print ("|    \|  /  | / \|| |\ ||| |\ ||_____ |  \/| \  / ")
print ("\___ ||  \_ | |-||| | \||| | \||\____\|  __/ / /  ")
print ("\____/\____/\_/ \|\_/  \|\_/  \|      \_/   /_/   ")
print ("                                                  ")
print ("____ ___  _   _      _  _  _______               ")
print ("/  __\\  \//  / \__/|/ \/ |/ /\__  \              ")
print ("| | // \  /   | |\/||| ||   /   /  |              ")
print ("| |_\\ / /    | |  ||| ||   \  _\  |              ")
print ("\____//_/     \_/  \|\_/\_|\_\/____/              ")

parser = argparse.ArgumentParser(description="NMAP to find open ports by file o single")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-ip",help="Single IP - 192.168.1.2, Segments 192.168.0/24")
group.add_argument('-file', help="Text File with Single IP or Segments")
group.add_argument("-version", action="version", version="Escanner NMAP Services 1.2")
args = parser.parse_args()

ip = args.ip
filename = args.file

#Escaneo de puertos
def scann(segIP, ipName):
    #print segIP
    #print a
	nm.scan(hosts=segIP, arguments='-sC -sV -p- -min-rate 1000 -max-retries 5')
	rpt = open(ipName + ".txt","w")
	rpt.write(nm.csv())
	rpt.close
	print "================= End Scan ====================="


#Abrimos archivo
def abreF(NomFile):    
    fic = open(NomFile,'r')    
    for linea in fic.readlines():
        print (linea)
        ipTx = linea.find("/")
        ipFil = linea[0:ipTx]
        #print (ipFil)
        scann(linea,ipFil)
    fic.close()  



#print (ip)
#print (filename)
#Extrae la IP para nombrar el archivo
if ip:
    ipTex = ip.find("/")
    if ipTex <> -1:
        ipFile = ip[0:ipTex]
        #print (ipFile)
        scann(ip, ipFile)
    else:
        scann(ip,ip)

if filename:
    abreF(filename)




