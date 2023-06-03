f = open('24222.txt').readline()
k = m = 0
for i in range(len(f)):
    if f[i] == 'R':
        k += 1
        m = max(k, m)
    else:
        k = 0

print(m)  
