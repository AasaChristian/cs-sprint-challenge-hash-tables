def intersection(arrays):
    """
    YOUR CODE HERE
    """
    hash = {}
    len = 0
    result = []
    for lists in arrays:
        len += 1
        for numb in lists:
            if numb not in hash:
                hash[numb] = 1
            else:
                hash[numb] += 1
                if hash[numb] == len and numb not in result:
                    result.append(numb)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
