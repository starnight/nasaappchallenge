import bisect
import os

def _get_data_file(date,category):
	dataset = {
		'ocean_surface_temp': 'MYD28W_2017-03-22_rgb_3600x1800.SS.CSV',
		'solar_insolation':'CERES_INSOL_D_2017-04-19_rgb_1440x720.SS.CSV',
	}
	return os.path.join('data',dataset[category])


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
	data_file = _get_data_file(date,category)
	# result[lat][lon]
	result = []
	with open(data_file,'r') as data:
		for row in data.readlines():
			result.append(row.split(','))
	# print([float(_) for _ in [_[0] for _ in result][1:]])
	x, y = _map_to_cord(result,lat,lon)
	return result[x][y]

def get_ocean_surface_temp(date,lat,lon):
	# degree C
	return _get_value(date,'ocean_surface_temp',lat,lon)

# CERES_INSOL_M_2017-03-01_rgb_1440x720.SS.CSV

def get_solar_insolation(date,lat,lon):
	#0 ~ 550
	return _get_value(date,'solar_insolation',lat,lon)


if __name__ == '__main__':
	args = ('20170301',21.943973, 120.795837)
	print(get_ocean_surface_temp(*args))
	print(get_solar_insolation(*args))