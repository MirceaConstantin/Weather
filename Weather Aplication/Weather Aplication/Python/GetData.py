import xml.etree.ElementTree as ET
import XML_Links
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

from threading import Thread

def get_cities_mt():
	threads = []
	i = 0
	for c in XML_Links.Cities:
		thread = Thread(target=get_city, args=(c,i,))
		threads.append(thread)
		thread.start()
		i += 1
	
	for t in threads:
		t.join()
  
def get_city(city, i):
	(forecast_link, observation_link) = XML_Links.Data[i]

	xml_url = forecast_link
	url     = urlopen(xml_url).read()
	xml     = ET.fromstring(url)
	Iter    =  xml.findall('metData')
	Search  =  xml.find('metData')

	# Temperature exctracion (found only in the first <metData>)
	Temperature = Search.find('t').text

	# Humidity exctration (from another XML file)
	xml_url_Humidity = observation_link
	url_Humidity = urlopen(xml_url_Humidity).read()
	xml_Humidity = ET.fromstring(url_Humidity)
	Humidity_Search = xml_Humidity.find('metData')
	Humidity = Humidity_Search.find("rh").text


	# Writing data to the file
	with open("Get_Data_For_App_" + city + ".txt", 'w') as file_out:
		# Temperature
		file_out.write(Temperature+'\n')
		# Humidity
		file_out.write(Humidity+'\n')
		# XML file iteration
		for Data in Iter:
			file_out.write(Data.find('valid').text.split(' ')[0]+'\n')			# Date
			file_out.write(Data.find('valid_day').text.split(' ')[0]+'\n')		# Week Date
			file_out.write(Data.find('sunrise').text.split(' ')[1]+'\n')		# Sunrise 
			file_out.write(Data.find('sunset').text.split(' ')[1]+'\n')			# Sunset
			file_out.write(Data.find('nn_shortText').text+'\n')					# Weather type
			file_out.write(Data.find('txsyn').text+'\n')						# Max temperature
			file_out.write(Data.find('tnsyn').text+'\n')						# Min Temperature
			file_out.write(str(Data.find('dd_shortText').text)+'\n')			# Wind direction
			file_out.write(str(float(Data.find('ff_value').text) * 3.6)+'\n')	# Wind speed
		file_out.write(city)   
get_cities_mt()