P = range(10, 41)
Q = range(5, 16)
R = range(35, 51)
for x in [7, 12, 20, 37, 45]:
    for ans in [True, False]:
        if ((ans) or (x in P)) or ((x in Q) <= (x in R)):
            print(x, ans)