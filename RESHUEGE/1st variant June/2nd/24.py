f = open('24 (8).txt').readline()
k = m = 3
for i in range(len(f)-3):
    if f[i] + f[i+1] + f[i+2] + f[i+3] != 'XZZY':
        k += 1
        m = max(k, m)
    else:
        k = 3

print(m)            