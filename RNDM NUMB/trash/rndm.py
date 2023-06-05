a = [int(x) for x in open('17 (12).txt')]
b = [int(x) for x in open('17 (12).txt') if int(x) % 2 == 1]
avg = sum(b)//len(b)

k = m = 0

for i in range(len(a) - 1):
    if a[i] % 5 == 0 or a[i+1] % 5 == 0:
        if a[i] < avg or a[i+1] < avg:
            k += 1
            m = max(m, a[i] + a[i+1])


print(k, m)            
