def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    storage = dict.fromkeys(a, None)
    result = []
    for val in a:
        if -val in storage and val > 0:
            result.append(val)
    return result


if __name__ == "__main__":
    print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))
