
def readFile():
    f = open( "european_cities.csv", "r" )
    line = f.readline()
    cities = line.strip().split( ";" )

    distance = []
    for line in f:
        distance.append( line.strip().split( ";" ) )

    return cities, distance

readFile()

