#!/usr/bin/env python3

from bottle import route, run, static_file, response
from json import dumps
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

@route('/GetAirTemp/<date>/<lon:float>/<lat:float>')
def getAirTemp(date, lon, lat):
	return data[date][lon][lat]

@route('/GetSolarInsolation/<date>/<lon:float>/<lat:float>')
def getSolarInsolation(date, lon, lat):
	return get_solar_insolation(date,lat,lon)

@route('/GetUV/<date>/<lon:float>/<lat:float>')
def getUV(date, lon, lat):
	return data[date][lon][lat]

@route('/GetTide/<date>/<lon:float>/<lat:float>')
def getTide(date, lon, lat):
	response.content_type = "application/json"
	return dumps({"tide": {"hour": [0, 1], "height": [5, 6, 5, 6, 7, 6, 5, 4]}}) #data[date][lon][lat]

@route('/GetWind/<date>/<lon:float>/<lat:float>')
def getWind(date, lon, lat):
	response.content_type = "application/json"
	return dumps({"wind": {"hour": [0, 1, 2, 3, 4, 5, 6, 7], "direction": ["WS", "W"], "strength": [1, 2]}}) #data[date][lon][lat]

@route('/GetEscherichiacoli/<date>/<lon:float>/<lat:float>')
def getEscherichiacoli(date, lon, lat):
	return data[date][lon][lat]

@route('/GetUnderSeaVisibility/<date>/<lon:float>/<lat:float>')
def getUnderSeaVisibility(date, lon, lat):
	return data[date][lon][lat]


if __name__ == "__main__":
	# Build data sets
	print("Building Chlorophyll data sets ...")
	BuildChlorophyllDataSets()

	# Run the web server
	run(host='0.0.0.0', port=8080, debug=True)
