## importing socket module
import socket

#To get the physical address of the device we use getmac module of Python.
from getmac import get_mac_address as Mac_Address

#We import sys to terminate the terminal in case something goes wrong
import sys

#To get external IP address we use requests module 
from requests import get as Pawan_Get_Request

Website__Address = 'https://api.ipify.org'

def Pawan__Get__Network__Detaiils():
	## getting the hostname by socket.gethostname() method
	My_Hostname = str(socket.gethostname())

	## getting the IP address using socket.gethostbyname_ex() method
	My_IP_Address = socket.gethostbyname_ex(My_Hostname)[-1]
	My_IP_Address = My_IP_Address[1]
	My_IP_Address = str(My_IP_Address)

	#Here we capture the system mac address
	My_Mac_Address = str(Mac_Address())

	#Here we use the website ipfy.og to get our external ip addres
	Public_IP_Address = str(Pawan_Get_Request(Website__Address).text)

	#Here we get the location details using the extrernal (Public) IP address
	Location_Website_Address = 'http://ip-api.com/json/' + Public_IP_Address
	My_Location_Details = Pawan_Get_Request(Location_Website_Address).json()
	My_Country = str(My_Location_Details['country'])
	My_Region = str(My_Location_Details['region'])
	My_City = str(My_Location_Details['city'])
	My_ISP = str(My_Location_Details['isp'])
	My_Coordinates = str((My_Location_Details['lat'],My_Location_Details['lon']))
	
	return {"Hostname is   ":My_Hostname,"My Internal (Private) IP Address is   ":My_IP_Address,"My MAC Address is   ":My_Mac_Address, "My Public (External) IP Address is  " :Public_IP_Address, 'My Country is   ':My_Country,'My region is   ':My_Region, 'My city is   ':My_City, 'My internet service provider is   ':My_ISP, 'My Coordinates are   ':My_Coordinates }

def Pawan_Port_Scanner():

	remoteServer = "127.0.0.1"
	remoteServerIP = socket.gethostbyname(remoteServer)

	Port_Ka_List =[]


	try:
		for port in range(1,1025):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((remoteServerIP,port))
			if result == 0:
				Port_Ka_List.append(port)
			sock.close()
		return Port_Ka_List

	except socket.gaierror:
		print("Nirmohi ne socket hi nahi diya")
		sys.exit()

	except socket.error:
		print("Zulmi ne koi socket choone na dia ..... hai daiyya")
		sys.exit()

if __name__ == "__main__":
	Dictionary_Function_Output = Pawan__Get__Network__Detaiils()
	for Network_Information_Component in Dictionary_Function_Output:
		Combined_Text = Network_Information_Component + "  ::  " + Dictionary_Function_Output[Network_Information_Component]
		print(Combined_Text)

	Port_Hain_Na = Pawan_Port_Scanner()
	for Port in Port_Hain_Na:
		print(f"The port # {Port} is open")
