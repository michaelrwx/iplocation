#This program was made to teach me how to use packages from pip. I wanted to make something like nslookup or traceroute except it gives out the IP right away!
import ipinfo

#Define input variable
print(f"Enter an IP address: ")
givenip = input()

#Variable definitions that get the ipinfo package to work
handler = ipinfo.getHandler()
details = handler.getDetails(givenip)

#Print statements with normal programs
print(f"You entered {givenip}.")
print(f"Your ISP is {details.org}.")
print(f"In fact your city is {details.city}, {details.region}. Located in the beautiful land of {details.country_name}") 
print(f"Your coordinates are {details.loc}, latitude-longitude order of course.")
print(f"I believe your hostname is {details.hostname}.")

print(f"Would you like a detailed view? [y/n]")
decision = input()

if decision == "y" or decision == "Y":
    print(details.all) #Maybe make this look cleaner
else:
    print("Peace") 

#To Do: 
    #Give option to parse results to a file
    #Create DNS compatibility








