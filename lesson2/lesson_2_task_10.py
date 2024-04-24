def bank(X, Y):
    year_sum = 0.10  
    start_sum = X 
    for _ in range(Y):
        start_sum += start_sum * year_sum  

    return start_sum


print(bank(1000, 1))
