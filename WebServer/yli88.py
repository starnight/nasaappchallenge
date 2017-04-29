import bisect
import os

from math import atan2
from math import pi

yli88_data = {}

def build_data_file():
	global yli88_data
	dataset = {
		'ocean_surface_temp': 'MYD28W_2017-03-22_rgb_3600x1800.SS.CSV',
		'solar_insolation':'CERES_INSOL_D_2017-04-19_rgb_1440x720.SS.CSV',
		'gfs_temp':'gfs_temp.csv',
		'gfs_wind_speed':'gfs_wind_speed.csv',
		'gfs_wind_u':'gfs_wind_u.csv',
		'gfs_wind_v':'gfs_wind_v.csv',
	}
	for key in dataset.keys():
		result = []
		with open(os.path.join('data',dataset[key])) as data:
			for row in data.readlines():
				result.append(row.split(','))
		yli88_data[key] = result

def _map_to_cord(data_src,lat,lon):
	lat_min = -90.
	lat_max = 90.
	lon_min = -180.
	lon_max = 180.
	if lat_min > lat or lat_max < lat:
		raise Exception('shit, lat is {0}, where are you??'.format(lat))
	if lon_min > lon or lon_max < lon:
		raise Exception('shit, lon is {0}, where are you??'.format(lon))
	cord_lon = [float(_) for _ in data_src[0][1:]]
	# print('lon', len(cord_lon), max(cord_lon), min(cord_lon))
	y = bisect.bisect(cord_lon, lon)+1
	# print(y)
	cord_lat = list(reversed([float(_) for _ in [_[0] for _ in data_src][1:]]))
	# print('lat', len(cord_lat), max(cord_lat), min(cord_lat))
	x = bisect.bisect(cord_lat, lat)
	# print(x)
	return -x, y

def _get_value(date,category,lat,lon):
	global yli88_data
	# result[lat][lon]
	result = yli88_data[category]
	# print([float(_) for _ in [_[0] for _ in result][1:]])
	x, y = _map_to_cord(result,lat,lon)
	return result[x][y]

def get_ocean_surface_temp(date,lat,lon):
	# degree C
	return _get_value(date,'ocean_surface_temp',lat,lon)

# CERES_INSOL_M_2017-03-01_rgb_1440x720.SS.CSV

def get_gfs_temp(date,lat,lon):
	k = _get_value(date,'gfs_temp',lat,lon)
	c = float(k) - 273.15
	return c

def get_gfs_wind_speed(date,lat,lon):
	return _get_value(date,'gfs_wind_speed',lat,lon)

def get_gfs_wind_direction(date,lat,lon):
	u = _get_value(date,'gfs_wind_u',lat,lon)
	v = _get_value(date,'gfs_wind_v',lat,lon)
	rad = atan2(float(v),float(u))
	degree = rad*180/pi
	degree = (degree+360)%360
	return map_to_direction(degree)

def map_to_direction(degree):
	# degree: 0 ~ 360

	# direction_interval = [22.5, 45, 67.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5]
	direction_interval = [11.25,33.75,56.25,78.75,101.25,123.75,146.25,168.75,191.25,213.75,236.25,258.75,281.25,303.75,326.25,348.75]
	direction = ['w', 'sww', 'sw', 'ssw', 's', 'sse', 'se', 'see', 'e', 'nee', 'ne', 'nne', 'n', 'nnw', 'nw', 'nww', 'w']
	return direction[bisect.bisect(direction_interval, degree)].upper()





if __name__ == '__main__':
	build_data_file()
	args = ('20170301',21.943973, 120.795837)
	# print(get_ocean_surface_temp(*args))
	# print(get_solar_insolation(*args))
	# print(map_to_direction(235))
	print(get_gfs_wind_direction(*args))
	print(get_gfs_wind_speed(*args))
	print(get_gfs_temp(*args))