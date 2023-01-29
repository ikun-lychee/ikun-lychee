time = list(map(int, input().split(" ")))
a = time[0]
b = time[1]
c = time[2]
d = time[3]
print(int(((c * 60 + d) - (a * 60 + b)) / 60), ((c * 60 + d) - (a * 60 + b)) % 60)
