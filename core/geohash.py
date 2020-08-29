import pygeohash

class GeoHash:
    def generate_geohash(localization):
        loc = localization.split(',')
        return pygeohash.encode(float(loc[0]), float(loc[1]))
