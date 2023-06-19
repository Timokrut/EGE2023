s = 'ДЕКОР'
k = 0
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                res = a1+a2+a3+a4
                k += 1
                if res[0] == 'К':
                    print(k)