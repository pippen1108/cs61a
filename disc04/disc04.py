def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 1 or n == 0:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    #use slicing to get the non-consecutive elements of the list
    #just caculate the product of the all elements from the index of 0 or 1, because
    #it will get the most element from the possible combanaiton of the sliced list
    step = 2
    max_product = 1
    for head in [0,1]:
        while step < len(s) - 1 - head:
            product = 1
            for x in s[head::step]:
                product *= x
            step += 1
            if product > max_product:
                max_product = product
    return max_product
