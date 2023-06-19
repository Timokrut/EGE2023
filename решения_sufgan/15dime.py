res = ''
p = range(10, 36) 
q = range(17, 49)
for a in range(0, 100): # примерные промежутки для A
    res += '0' if all(((x == a) <= (not (x in p))) <= ((x == a) <= (x in q)) for x in range(100)) else ' ' # наше выражение
print(res) # убедиться, что все ок
print(len(max(res.split(), key=len)) - 1)