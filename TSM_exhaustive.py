import TSM_main as tsm

def main():
    cities, distance = tsm.read_file()
    permutations = tsm.get_permutations( cities[:10] )

    best = -1
    for p in permutations:
        dist = tsm.distance_permutation( p, cities, distance )
        best = dist if best == -1 else best
        best = dist if dist < best else best
    print best
        
if __name__ == "__main__":
    main()
