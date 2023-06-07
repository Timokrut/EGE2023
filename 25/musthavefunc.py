def count_div(n): #подсчет делителей
    k = 0
    for  j in range(1, int(n**0.5) + 1):
        if n % j == 0:
            k += 1
            if j != n // j:
                k += 1
    return k

# print(count_div(100)) 
# 9               


def find_div(n): #найти делители
    a = []
    for j in range(1, int(n**0.5) + 1):
        if n % j == 0:
            a.append(j)
            if j != n // j:
                a.append(n//j)
    a.sort()
    return a   

# print(find_div(100))
# [1, 2, 4, 5, 10, 20, 25, 50, 100]


def is_prime(n): #простое или нет
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True        

# print(is_prime(3))
# True