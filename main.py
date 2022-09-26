import phonenumbers
import opencage
import folium
from CheckNumber import number

from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
# enter ur api key value here
api_key = "Enter_your_apikeyValue"

pnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pnumber, "en")
service_provider = carrier.name_for_number(pnumber, "en")
print(location, service_provider)

geocoder = OpenCageGeocode(api_key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

Map = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(Map)

Map.save("FinalMap.html")
