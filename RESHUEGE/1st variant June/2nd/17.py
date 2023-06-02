f = open('17 (10).txt')
a = [int(x) for x in f]

k = m = 0

div = []
for j in range (len(a)):
    if a[j] % 2 == 0:
        div.append(a[j])
srednee = sum(div)//len(div)

for i in range(len(a)- 1):
    if a[i] % 3 == 0 or a[i+1] % 3 == 0:
        if a[i] < srednee or a[i+1] < srednee:
            k += 1
            m = max(m, a[i] + a[i+1])

print(k, m)