# LSOA #

to begin, you'll need to activate the virtualenv:

    . bin/activate

The code generates GeoJSON files from a big shapefile.  Generally this only
needs to be done once, and it's already been done.  But to run it again:

    (cd http; ../code/thingy.py)
    # Takes about 5 to 10 minutes

To fetch a GeoJSON file over http:

    curl http://ip-address/lsoa/http/E*.json

To see what IP address you need to curl to to get the JSON files:

    curl http://httpbin.org/ip
    # from within the box
