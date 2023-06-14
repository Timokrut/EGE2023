f = open('./27A_2720.txt')
n = int(f.readline())
a = [int(x) for x in f.readlines()]
forall = []
ans = []
k = 0
has7 = 0

for i in a:
    if i % 7 == 0:
        forall.append(i)
        k += len(forall)
        has7 += 1
    else:
        k += has7
        forall.append(i)    

print(k)        