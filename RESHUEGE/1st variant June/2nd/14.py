x = 4 ** 2020 + 2 ** 2017 - 15
s = []

while x != 0:
    s = [x%2] + s
    x //= 2

print(s.count(1))    