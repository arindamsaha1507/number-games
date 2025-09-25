import time

def pythagorean_triplets_brute_force(limit: int) -> list[list[int]]:

    if not isinstance(limit, int):
        raise TypeError("Limit is of the wrong type")
    
    x = 0
    y = 0
    results = []

    for z in range(1, limit + 1):

        for x in range(1, limit + 1):
            for y in range(1, limit +1):
                if x**2 + y**2 == z**2:
                    results.append([x, y, z])

    return results


def square_list(int_list: list[int]) -> list[int]:
    return [x**2 for x in int_list]

def add_list(list1: list[int], list2: list[int]) -> dict[tuple, int]:
    # return [x1 +x2 for x1, x2 in zip(list1, list2)]

    dictionary = {}
    for x1 in list1:
        for x2 in list2:
            dictionary[(x1, x2)] = x1 + x2

    return dictionary


def pythagorean_triplets_smart(limit: int) -> list[list[int]]:

    results = []

    nums = list(range(1, limit + 1))
    squares = square_list(nums)
    added_squares = add_list(squares, squares)

    for key, value in added_squares.items():
        if value in squares:
            results.append([int(key[0] ** 0.5), int(key[1] ** 0.5), int(value ** 0.5)])

    return results


def main():

    limit = 100
    
    start_time = time.time()
    pythagorean_triplets_smart(limit)
    end_time = time.time()
    print(f"Execution took {end_time - start_time} seconds")


    start_time = time.time()
    pythagorean_triplets_brute_force(limit)
    end_time = time.time()
    print(f"Execution took {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
