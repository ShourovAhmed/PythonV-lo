import json


def printProperty(propName):
    for ft in data['features']:
        print(ft['properties'][propName])

##
with open('velo.geojson') as f:
    data = json.load(f)

features = data['features'][0]

printProperty('Objecttype')


