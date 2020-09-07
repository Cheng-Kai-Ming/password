import time
password = 'a123456'
x = 3
print('您有三次機會!!')
while x < 4 and x > 0:
	pas = input('請輸入密碼')
	if pas == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		x = x - 1
		if x > 0:
			print('尚有', x ,'次')
		else:
			print('輸入太多次而中斷連線')
			print('請等待10秒後再輸入')
			time.sleep(10)
			break


			