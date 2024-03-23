import ipinfo
import socket
import sys
 
#Define input variable
if len(sys.argv) != 2:
    print("Usage: iplocation <IP ADDRESS> or <WEBSITE NAME>")
    sys.exit(1)

try: 
    givenip = sys.argv[1]
 
    #Variable definitions that get the ipinfo package to work
    handler = ipinfo.getHandler()
    details = handler.getDetails(socket.gethostbyname(givenip)) #the socket.gethostbyname converts a DNS line into an IP
 
    #Print statements with normal programs
    print(f"IP entered: {givenip}.")
    print(f"ISP: {details.org}.")
    print(f"Location: {details.city}, {details.region}, {details.country}")
    print(f"Coordinates {details.loc}")
    print(f"IP Hostname: {details.hostname}.")
except:
    print("Invalid input. Try again (EX: 8.8.8.8 or www.google.com)")
    