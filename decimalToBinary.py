def decToBin(n):
    assert int(n)==n,'Number should be integer'
    if n==0:
        return 0   
    return n%2 + 10* decToBin(int(n/2))

print(decToBin(10))