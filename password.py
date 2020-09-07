import time
x = 0
while True:
	password = input('請輸入密碼')
	if password == 'a123456':
		print('成功登入')
		break
	else:
		print('密碼錯誤')
		x = x + 1
		print('你錯了',x,'次?')
		if x >= 3:
			print('請於10秒後輸入')
			time.sleep(10)
			