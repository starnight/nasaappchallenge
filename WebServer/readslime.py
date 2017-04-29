#!/usr/bin/env python3

import csv
from axeschange import lon2col, lat2row

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from math import floor, ceil

# These data come from NASA Earth Observations (NEO)
# https://neo.sci.gsfc.nasa.gov/view.php?datasetId=MY1DMW_CHLORA&date=2017-03-01
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
		c = []
		for col in row:
			c.append(float(col))
		d.append(c)

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
	return "%.5f" % data[idx][row][col]

def getZ(i, x, y):
	ix = int(round(x*10)) + 1800
	iy = -(int(round(y*10)) - 900)
	z = data[i][iy][ix]
	if z == 99999.0:
		z = 0.0
	#print("x: {0}, y:{1}, z:{2}".format(ix, iy, z))
	return z

def plotRegion(i, x, y):
	lon = np.arange(floor(x[0]), ceil(x[1]), 0.1)
	lat = np.arange(ceil(y[1]), floor(y[0]), -0.1)
	X, Y = np.meshgrid(lon, lat)

	z = np.array([getZ(i, x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
	Z = z.reshape(X.shape)
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	surf = ax.plot_surface(X, Y, Z)

	plt.xlabel("Longitude")
	plt.ylabel("Latitude")
	plt.title("Chlorophyll Concentration (mg/m^3)")
	plt.show()
	plt.close()
	
if __name__ == "__main__":
	BuildChlorophyllDataSets()

	print(len(data))
	for d in data:
		print(len(d))
	
	print(data[7][1799][3599])
	
	
	#for i in range(len(data)):
	#	print(i)
	plotRegion(1, [31.31, 104.57], [-23.43, 44.04])
