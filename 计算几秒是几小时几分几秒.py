time = int(input("请输入秒："))
print(f"{time}秒=" + str(int(time / 3600)) + "小时" + str(int(time / 60 % 60)) + "分" + str(int(time % 60))+"秒")
