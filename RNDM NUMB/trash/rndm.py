for A in range(1, 100):
    t = 1
    for x in range(1, 100):
        for y in range(1, 100):
            t *= (2 * x + 3 * y < 30) or ( x + y >= A)
    if t == 1:
        print(A)            