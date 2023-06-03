f = open('24 (6).txt').readline()

k = m = 1

for i in range(len(f)-1):
    if f[i] + f[i+1] != 'ad' and f[i] + f[i+1] != 'da' :
        k += 1
        m = max(k, m)    
    else:
        k = 1

print(m)        