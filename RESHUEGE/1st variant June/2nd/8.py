k = 0
s = 'МАТВЕЙ'
for a1 in 'МАТВЕ':
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        res = a1 +a2 +a3+a4+a5+a6 
                        if res.count('М') == 1 and res.count('АЕ') == 0 and res.count('А') == 1 and res.count('Т') == 1 and res.count('В') == 1 and res.count('Е') == 1 and res.count('Й') == 1:
                            k += 1 
print(k)                            