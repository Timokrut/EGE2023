def descending_order(num):
    a=[]
    s = str(num)
    for i in s:
        a.append(i)

    a.sort(reverse=True)

    res = ''

    for i in a:
        res += str(i)

    
    return int(res)


print(descending_order(15))    