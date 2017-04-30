import pygrib

def save_to_csv(grb, csv_file_name):
    maxt = grb.values
    lats = list(grb.distinctLatitudes)
    # print lats
    lons = [lon-360 if lon>180 else lon for lon in grb.distinctLongitudes]
    lons = ['lat/lon']+lons[181:]+lons[:181]
    # print lons
    with open(csv_file_name,'w') as _csv:
        _csv.write(','.join([str(lon) for lon in lons]))
        _csv.write('\n')
        for i in range(len(lats)):
            vals = [str(_) for _ in maxt[i]]
            _csv.write(','.join([str(lats[i])]+vals[181:]+vals[:181]))
            _csv.write('\n')


if __name__ == '__main__':
    grbs = pygrib.open('gfs.t06z.pgrb2.1p00.f000')
    # for grb in grbs:
    #    print grb
    # grb = grbs.select(name='U component of wind')[5]
    #grb = grbs.select(name='Temperature',typeOfLevel='surface',level=0)[0]
    index = 4
    grbs.seek(index-1)
    grb=grbs.readline()
    print grb
    # maxt = grb.values
    # print maxt.shape, maxt.min()-273.15, maxt.max()-273.15
    # lats, lons = grb.latlons()
    # print lats.shape, lats.min(), lats.max(), lons.shape, lons.min(), lons.max()
    # print maxt[90-22][123]-273.15, maxt.min()-273.15, maxt.max()-273.15
    #for grb in grbs.select(name='Temperature')[-20:]:
    #    maxt = grb.values
    #    print grb
    #    print maxt[90-22][123]-273, maxt.min()-273.15, maxt.max()-273.15
    # print grb.distinctLatitudes
    # print grb.distinctLongitudes
    save_to_csv(grb, 'test.csv')
