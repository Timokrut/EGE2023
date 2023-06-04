def f(s, c, m):
    if s >= 68: return c%2 == m%2
    if c == m: return 0

    h = [f(s+1, c+1, m), f(s+4, c+1, m), f(s*5, c+1, m)]
    return any(h) if (c+1)% 2 == m% 2 else any(h)
#если ход неудачный - any(h)-----------------↑ 


for s in range(1, 67):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            if m == 2:
                print(s, m)
            break   