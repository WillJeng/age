driving = input("你是否有開過車車? 請輸入是或否:") 
if driving != "是" and driving != "否":
	print("請輸入正確格式")
	raise SystemExit
	
age = input("請問你的年齡是:")
age = int(age)
if driving == "是":
	if age >= 18:
		print("您符合資格")
	else:
		print("您條件不符合")
elif driving == "否":
	if age >= 18:
		print("您怎麼還不去考駕照!")
	else:
		print("小鬼 毛長齊了再來吧!")