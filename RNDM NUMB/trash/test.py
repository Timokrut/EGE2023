for a in range(1, 100):
    t = 1
    for x in range(1, 100):
        t *= (x & 33 == 0) <= ((x & 45 != 0) <= (x & a != 0))
    if t == 1:
        print(a)
        break    