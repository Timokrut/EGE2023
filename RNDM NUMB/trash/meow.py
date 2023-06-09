def second_symbol(s, symbol):
    k = 0
    for i in range(len(s)):
        if s[i] == symbol:
            k += 1
            if k == 2:
                return i
    return -1
print(second_symbol('qq', 'q'))            