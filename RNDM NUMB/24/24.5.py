f = open('24 (7).txt').readline()
s = f.replace('A', '*').replace('O', '*').replace('C', '+').replace('D', '+').replace('F', '+')

print(s.count('**+**+**+**+'))