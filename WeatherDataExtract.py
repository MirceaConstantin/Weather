# folosim urllib pentru a lua codul html de pe pagina cu datele xml
# folosim xml.etree.ElementTree pentru a interoga fisierul xml si a extrage datele
from urllib.request import urlopen
import xml.etree.ElementTree as ET

#URL-ul paginii xml
xml_url = "http://meteo.arso.gov.si/uploads/probase/www/fproduct/text/en/forecast_BUCUR-BAN_latest.xml"

# creeare si scrierea in fisier a datelor
file_out = open("weather_Sunrise_Sunset.txt", 'w+')

# luam codul html din pagina si il stocam in memorie ca string (linia 14)
# din string, convertam in fisier xml                          (linia 15)
url = urlopen(xml_url).read()
xml = ET.fromstring(url)

# pentru fiecare camp <metData> gasit, cauta <sunrise> si <sunset> si printeaza valorile 
# in fisierul "weather_Sunrise_Sunset.txt"
for Nodes in xml.findall('metData'):
    for sunrise in Nodes.findall('sunrise'):
        file_out.write(sunrise.text + '\n')
    for sunset in Nodes.findall('sunset'):
        file_out.write(sunset.text + '\n')
    file_out.write("\n")










