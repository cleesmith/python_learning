# import time

import pygeoip
from pygeoip import MEMORY_CACHE, MMAP_CACHE, STANDARD

output = {}
try:
  geoip = pygeoip.GeoIP('/Users/auser/Sites/idstools_snort/GeoLiteCity.dat', MEMORY_CACHE)
except IOError:
  print('IOError: can not find GeoLiteCity.dat')

output["src_geoip"] = geoip.record_by_addr('74.125.228.199')
# output["src_geoip"] = geoip.record_by_addr('192.168.0.2')
print('\ntype(output[src_geoip])=%s' % type(output["src_geoip"]))
print('output[src_geoip]=%s' % output["src_geoip"])

if output["src_geoip"] == None:
	print('no geo data for IP address!')
else:
	latitude = None
	longitude = None

	# test no value:
	output["src_geoip"]["longitude"] = None
	# test missing field:
	# del output["src_geoip"]["longitude"]

	# min/max: latitude: -90 to 90 longitude: -180 to 180
	# latitude=37.41919999999999 longitude=-122.0574
	if ("latitude" in output["src_geoip"]) and (output["src_geoip"]["latitude"] != None):
		latitude = output["src_geoip"]['latitude']
		print('\ntype(latitude)=%s' % type(latitude))
		print('\nlatitude=%3.14f' % latitude)
	else:
		print('no latitude!')

	if ("longitude" in output["src_geoip"]) and (output["src_geoip"]["longitude"] != None):
		longitude = output["src_geoip"]['longitude']
		print('\ntype(longitude)=%s' % type(longitude))
		print('\nlongitude=%3.14f' % longitude)
	else:
		print('no longitude!')

	if (longitude == None) or (latitude == None):
		# *****
		# FIXME create or don't create the "location" field ???
		# *****
		output["src_geoip"]["location"] = None
	else:
		# "location" is a geojson array used by "bettermap" in kibana:
		output["src_geoip"]["location"] = [longitude, latitude]

	print('location=%s' % output["src_geoip"]["location"])

print('\ntype(output[src_geoip])=%s' % type(output["src_geoip"]))
print('output[src_geoip]=%s' % output["src_geoip"])

# time.sleep(60)

