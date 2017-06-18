from urllib2 import urlopen
import xml.etree.ElementTree as ET

xml_url = "http://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_BUCUR-BAN_latest.xml"
file_out = open("weather_Humidity.txt", 'w')

url = urlopen(xml_url).read()
xml = ET.fromstring(url)
Node = xml.find('metData')
Humidity = Node.find("rh")

file_out.write(Humidity.text)


