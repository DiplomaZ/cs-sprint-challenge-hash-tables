def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    tup = None
    
    def calculate(s,l):
        pass
        temp_tup = ()
        if s >= l:
            temp_tup = (s,l)
        else:
            temp_tup = (l,s)

        if sum(tup) == length:

            tup = temp_tup
            return True
        else:
            return False

    weights_hash = {}

    for i, weight in enumerate(weights):
        weights_hash[weight] = i

    for weight in weights:
        if weight == None:
            continue
        other_val = limit - weight
        if other_val in weights_hash:
            if weight == other_val:
                weights[weights_hash[weight]]=limit+100

                tup = (weights_hash[weight], weights.index(other_val))
                
            elif weights_hash[weight] > weights_hash[other_val]:
                tup = (weights_hash[weight], weights_hash[other_val])
            


            else:
                tup = (weights_hash[other_val], weights_hash[weight])
    return tup
# weights_1 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)


print(answer_2)