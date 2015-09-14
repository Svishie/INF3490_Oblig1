from city import City

def readFile():
    f = open( "european_cities.csv", "r" )
    line = f.readline()
    temp = line.split( ";" )
    cities = []
    for city in temp:
        cities.append( City( city ) )
        print city

readFile()

