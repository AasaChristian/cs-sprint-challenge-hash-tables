def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash = {}
    result = []
    for num in a:
        if num > 0:
            if num in hash and num not in result:
                result.append(num)
            else:
                hash[num] = -num

        else:
            num = -num
            if num in hash and num not in result:
                result.append(num)
            else:
                hash[num] = -num


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
