#!/usr/bin/env python

import json
# http://code.google.com/p/pyshp/
import shapefile
import sys

def geojson(shape):
    """Converts a shapefile shape into a string that is a GeoJSON thing.
    Hint: use shapefile.Reader(filename)[7].shape to get a shape.
    """
    return json.dumps(dict(type='Polygon',
                           coordinates=[[[x,y] for x,y in shape.points]]))

lsoa_file = 'LSOA_FEB_2004_EW_BGC_Shapefile/LSOA_FEB_2004_EW_BGC.shp'

def main():
    sf = shapefile.Reader(lsoa_file)
    try:
        for i in range(1000000):
            sr = sf.shapeRecord(i)
            name = sr.record[0] + '.json'
            with open(name, 'w') as f:
                f.write(geojson(sr.shape))
            sys.stdout.write('\r%s' % name)
            sys.stdout.flush()
    except IndexError:
        print "\nWrote %d files" % i

if __name__ == '__main__':
    main()
