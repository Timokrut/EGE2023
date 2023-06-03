k = 1
m = 0
f = open('2111.txt').readline()
for i in range(len(f)-1):
    if f[i] != f[i+1]:
        k += 1
        m = max(k, m)
    else:
        k = 1
 
print(m)            