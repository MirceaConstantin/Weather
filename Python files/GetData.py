import xml.etree.ElementTree as ET

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"
url     = urlopen(xml_url).read()
xml     = ET.fromstring(url)
Iter    =  xml.findall('metData')
Search  =  xml.find('metData')

# Weather Data lists
Date = []
Hours = []
weatherType = []
MinMaxTemperature = []
WindDirection = []
WindSpeed = []

# XML file iteration
for Data in Iter:
	Date.append((Data.find('valid').text.split(' ')[0], Data.find('valid_day').text.split(' ')[0]))
	Hours.append((Data.find('sunrise').text.split(' ')[1], Data.find('sunset').text.split(' ')[1]))
	weatherType.append(Data.find('nn_shortText').text)
	MinMaxTemperature.append((Data.find('txsyn').text, Data.find('tnsyn').text))
	WindDirection.append(Data.find('dd_shortText').text)
	WindSpeed.append(int(Data.find('ff_value').text) * 3.6)

# Temperature exctracion (found only in the first <metData>)
Temperature = Search.find('t').text

# Humidity exctration (from another XML file)
xml_url_Humidity = "http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_BUCUR-BAN_latest.xml"
url_Humidity = urlopen(xml_url_Humidity).read()
xml_Humidity = ET.fromstring(url_Humidity)
Humidity_Search = xml_Humidity.find('metData')
Humidity = Humidity_Search.find("rh").text


with open("Get_Data_For_App.txt", 'w') as file_out:
	for i in range(0, 5):
		file_out.write(str(Date[i][0])+'\n')
		file_out.write(str(Date[i][1])+'\n')
		file_out.write(str(Hours[i][0])+'\n')
		file_out.write(str(Hours[i][1])+'\n')
		file_out.write(str(weatherType[i])+'\n')
		file_out.write(Temperature+'\n')
		file_out.write(str(MinMaxTemperature[i][0])+'\n')
		file_out.write(str(MinMaxTemperature[i][1])+'\n')
		file_out.write(Humidity+'\n')
		file_out.write(str(WindDirection[i])+'\n')
		file_out.write(str(WindSpeed[i])+'\n')
