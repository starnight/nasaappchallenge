#!/usr/bin/env python3

import csv
from axeschange import lon2col, lat2row

filenames = ["data/MY1DMW_CHLORA_2017-02-02_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-02-10_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-02-18_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-02-26_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-03-06_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-03-14_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-03-22_rgb_3600x1800.CSV",
			 "data/MY1DMW_CHLORA_2017-03-30_rgb_3600x1800.CSV"]

data = []

def build1DataSet(filename):
	datafile = open(filename, "r")
	datareader = csv.reader(datafile, delimiter=',')

	d = []
	for row in datareader:
		d.append(row)

	data.append(d)

def BuildChlorophyllDataSets():
	for filename in filenames:
		build1DataSet(filename)

def date2set(date):
	if   date < "20170210": i = 0
	elif date < "20170218": i = 1
	elif date < "20170226": i = 2
	elif date < "20170306": i = 3
	elif date < "20170314": i = 4
	elif date < "20170322": i = 5
	elif date < "20170330": i = 6
	else: 					i = 7

	return i

def GetChlorophyll(date, lon, lat):
	col = lon2col(lon)
	row = lat2row(lat)
	idx = date2set(date)
	return data[idx][row][col]

if __name__ == "__main__":
	BuildChlorophyllDataSets()

	print(len(data))
	for d in data:
		print(len(d))
	
	print(data[7][1799][3599])
