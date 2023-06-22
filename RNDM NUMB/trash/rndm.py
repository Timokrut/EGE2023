def tr(x):
    s = ''

    while x != 0:
        s = str(x%3) + s
        x//=3

    return int(s) 

print(tr(3))       