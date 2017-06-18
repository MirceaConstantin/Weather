from urllib.request import urlopen
import xml.etree.ElementTree as ET

xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"
url = urlopen(xml_url).read()
xml = ET.fromstring(url)

file_out = open("weather_Sunrise_Sunset.txt", 'w+')

for Nodes in xml.findall('metData'):
    for sunrise in Nodes.findall('sunrise'):
        file_out.write(sunrise.text + '\n')
    for sunset in Nodes.findall('sunset'):
        file_out.write(sunset.text + '\n')
    file_out.write("\n")










