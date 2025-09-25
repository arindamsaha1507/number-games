
original_number = 2


def square(number):

    return number**2

def pythagorean_triplets(limit):

    x = 0
    y = 0

    for z in range(1, limit + 1):

        for x in range(1, limit + 1):
            for y in range(1, limit +1):
                if x**2 + y**2 == z**2:
                    print(x, y, z)

def main():
    limit = 20
    pythagorean_triplets(limit)


if __name__ == "__main__":
    main()
