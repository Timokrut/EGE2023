def is_prime(n):
    if n <= 1:
        return False
    for j in range (2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True    


k = 0

for x in range(2422000, 2422081):
    if is_prime(x) == 1:
        k += 1
        print(k, x)




