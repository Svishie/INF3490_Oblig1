import itertools
import random

"""
Module that contains functions for reading and processing the data in the TSM-problem for assignment 1 in INF3490.
"""
def read_file():
    f = open( "european_cities.csv", "r" )
    line = f.readline()
    cities = line.strip().split( ";" )

    distance = []
    for line in f:
        distance.append( line.strip().split( ";" ) )

    return cities, distance

def get_city_index( cities, city ):
    return cities.index( city )

def get_distance( cities, distance, c1, c2 ):
    i1 = get_city_index( cities, c1 )
    i2 = get_city_index( cities, c2 )
    return distance[i1][i2]

def get_permutations( cities ):
    return itertools.permutations( cities )

def distance_permutation( permutation, cities, distance ):
    dist = 0.0
    prev = None
    for c in permutation:
        if prev != None:
            dist = dist + float( get_distance( cities, distance, prev, c ) )
        prev = c
    dist = dist + float( get_distance( cities, distance, permutation[-1], permutation[0] ) )
    return dist


def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))
        
def main():
    cities, distance = read_file()
    permutations = get_permutations( cities[:6] )
    for c in permutations:
        print c
    print "\n\n\n{0}".format( random_permutation( cities ) )

if __name__ == "__main__":
    main()
    
