week=["周日","周一","周二","周三","周四","周五","周六"]
Y=int(input())
M=int(input())
D=int(input())
f=int((14-M)/12)
y=Y-f
m=M+12*f-2
week=week[(D+y+int(31*m/12)+int(y/4)-int(y/100)+int(y/400))%7]
print(week)
