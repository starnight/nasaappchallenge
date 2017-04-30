#!/usr/bin/env python3

lon_domain = []
lat_domain = []

def haveLonDoamin():
	for i in range(-1800, 1800):
		lon_domain.append(i)

def haveLatDomain():
	for i in range(-899, 901):
		lat_domain.append(-i)

haveLonDoamin()
haveLatDomain()

def lon2col(lon):
	return lon_domain.index(round(lon*10))

def lat2row(lat):
	return lat_domain.index(round(lat*10))

def lonlat2arridx(lon, lat):
	return lon2col(lon), lat2row(lat)
