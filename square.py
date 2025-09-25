
def pythagorean_triplets(limit):

    x = 0
    y = 0

    results = []

    for z in range(1, limit + 1):

        for x in range(1, limit + 1):
            for y in range(1, limit +1):
                if x**2 + y**2 == z**2:
                    results.append([x, y, z])

    return results

"""

Future topics
1. Tuples vs List

Input -> Nothing

1. initialize
2. Loops
3. Loops
4. Loops
5. Checks
6. Prints
"""

def main():
    limit = 20
    triplets = pythagorean_triplets(limit)

    print(triplets)



if __name__ == "__main__":
    main()
