def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    loop thrue weights and add weight a
    """
    hash = {}
    count = 0

    for item in weights:
        needed = limit - item
        if item in hash:
            if count> hash[item]:
                return count, hash[item]
            else:
                return hash[item], count
        else:
            hash[needed] = (count)

        count += 1
            
    return None
w = [ 4, 6, 10, 15, 16 ] 

print(get_indices_of_item_weights(w, 5, 21 ))
