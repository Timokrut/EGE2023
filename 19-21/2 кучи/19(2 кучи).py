def f(a, b, c ,m):
    if a + b >= 78: return c % 2 == m % 2
    if c == m: return 0

    h = [f(a+3, b, c+1, m), f(a, b + 3, c+1, m), f(a*2, b, c+1, m), f(a, b*2, c+1, m)]

    return any(h) if (c+1)%2 == m%2 else any(h)
#если ход неудачный - any(h)--------------↑ 
for b in range(1, 70):
    for m in range(1, 5):
        if f(7, b, 0, m) == 1:
            if m == 2: 
                print(b,m)
            break   


# 19)18
# 20)17
# 21)28 30  