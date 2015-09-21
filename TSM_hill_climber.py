import TSM_main as tsm
import random

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

def swap( i1, i2, cities ):
    temp = cities[i2]
    cities[i2] = cities[i1]
    cities[i1] = temp
    
def generate_neighbours( permutation ):
    neighbours = []
    for i in range( len( permutation ) - 1 ):
        new = list(permutation)
        swap( i, i+1, new )        
        neighbours.append( new )
    return neighbours

def check_neighbours( cities, distance, best_distance, permutation ):

    neighbours = generate_neighbours( permutation )
    for n in neighbours:
        d = tsm.distance_permutation( n, cities, distance)
        if d < best_distance:
            return d, n
    return None, None
    
def main():
    cities, distance = tsm.read_file()
    random_cities = random_permutation( cities[:10] )
    best_cities = random_cities
    best_distance = tsm.distance_permutation( random_cities, cities, distance )
    
    not_optimum = True
    while not_optimum:
        temp_distance, temp_cities = check_neighbours( cities, distance, best_distance, best_cities )
        if temp_distance == None:
            not_optimum = False
        else:
            best_distance, best_cities = temp_distance, temp_cities
            
    print best_distance , best_cities
    
        
if __name__ == "__main__":
    main()
