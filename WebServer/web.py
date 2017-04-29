#!/usr/bin/env python3

from bottle import route, run, static_file
from readslime import BuildChlorophyllDataSets, GetChlorophyll
from yli88 import get_ocean_surface_temp,get_solar_insolation

@route('/')
@route('/hello')
def hello():
	return "Hello World"

@route('/key/<key>/value/<val:int>')
def keyin(key, val):
	return "You typed key:{0} value:{1}".format(key, val)

@route('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root='static')

@route('/GetChlorophyll/<date>/<lon:float>/<lat:float>')
def getChlorophyll(date, lon, lat):
	return GetChlorophyll(date, lon, lat)

@route('/GetOceanSurfaceTemp/<date>/<lon:float>/<lat:float>')
def getOceanSurfaceTemp(date, lon, lat):
	return get_ocean_surface_temp(date,lat,lon)

@route('/GetSolarInsolation/<date>/<lon:float>/<lat:float>')
def getSolarInsolation(date, lon, lat):
	return get_solar_insolation(date,lat,lon)

@route('/GetUV/<date>/<lon:float>/<lat:float>')
def getUV(date, lon, lat):
	return data[date][lon][lat]

if __name__ == "__main__":
	# Build data sets
	print("Building Chlorophyll data sets ...")
	BuildChlorophyllDataSets()

	# Run the web server
	run(host='0.0.0.0', port=8080, debug=True)
