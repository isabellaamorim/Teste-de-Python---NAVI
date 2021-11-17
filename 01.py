def one_to_fivemillion(): 
    n_sum  = 0
    for i in range(1, 5000001):
        if (i % 2 == 0) and (i % 49 == 0) and (i % 37 == 0): 
            n_sum += 1
    return n_sum

print(one_to_fivemillion())
