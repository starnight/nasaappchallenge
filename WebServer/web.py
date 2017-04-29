#!/usr/bin/env python3

from bottle import route, run, static_file

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

@route('/GetChlorophyll/<date:float>/<lon:float>/<lat:float>')
def getChlorophyll(date, lon, lat):
	return data[date][lon][lat]

@route('/GetOceanSurfaceTemp/<date:float>/<lon:float>/<lat:float>')
def getOceanSurfaceTemp(date, lon, lat):
	return data[date][lon][lat]

@route('/GetUV/<date:float>/<lon:float>/<lat:float>')
def getUV(date, lon, lat):
	return data[date][lon][lat]

if __name__ == "__main__":
	run(host='0.0.0.0', port=8080, debug=True)
