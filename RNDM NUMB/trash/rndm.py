# n = int(input())
# ans = []
# for i in range(0, n):
#     a = int(input())
#     if a % 3 == 0:
#         ans.append(a)

# print(sum(ans))        


# a = 1
# k = 0
# ans = []
# while a != 0:
#     a = int(input())
#     if a == 0:
#         break
#     k += 1
#     if a % 3 == 0:
#         ans.append(a)

# print(k, sum(ans))        


a = 1
k = 0
ans = []
ans1 = []
while a != 0:
    a = int(input())
    ans.append(a)
    
    if a == 0:
        break
    
    if a % 2 == 0 and a % 5 == 0:
        ans1.append(a)

print(sum(ans), len(ans1))   