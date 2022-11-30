# h = input('Please enter your highest: ')
# w = input('Please enter your weight: ')
# enter = '\n'
# print(f'highest:{h} cm {enter}weight:{w} kg')

# if rain == '有'：
# 	print('ok')


password = 'a123456'
i = 3
while i > 0:

	pwd = input('Please enter the password: ')

	if pwd == 'a123456':
		print('登錄成功！')
		break
	# elif i == 0:

	else:
		i -= 1
		if i == 0:
			break

		print(f'密碼錯誤！ 還有{i}次機會')
