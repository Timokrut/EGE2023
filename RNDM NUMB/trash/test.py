def f(a, b, c, m):
    if a + b <= 40:
        return c % 2 == m % 2
    if c == m:
        return 0
    
    h = [f(a-1, b, c+1, m), f(a, b-1, c+1, m), f((a+1)//2, b, c+1, m), f(a, (b+1)//2, c+1, m)]
    return any(h) if (c+1)%2 == m%2 else any(h)

for b in range(20, 200):
    for m in range(1, 5):
        if f(20, b, 0, m):
            if m == 2:
                print(b, m)
            break    