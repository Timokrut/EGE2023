k = 0 
s = '13579'
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                res = a1+a2+a3+a4
                s12 = int(res[0]) + int(res[1])
                s34 = int(res[2]) + int(res[3])
                mx = max(s12, s34)
                mn = min(s12, s34)
                rs = str(mn) + str(mx) 
                if rs == '414':
                    k += 1

print(k)                    