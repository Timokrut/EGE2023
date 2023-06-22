a = tuple(map(int, open('решения_sufgan/data/test_27.txt').readlines()[1:]))
b = a[0] + 1
m = 0
for i in range(1, len(a)):
    m = max(m, b + a[i])
    b = max(b, a[i])
    b += 1
print(m)