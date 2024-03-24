# function
#lan = input('請輸入想要的國籍語言(英語或中文): ')
def say_hi(lan): # define 一個say_hi的function按鈕； language= 想像成投幣孔
	if lan == '英語':
		print('hi')
	elif lan =='國語':
		print('你好')
	else:
		print('我不知道你在說甚麼!?')	
say_hi('國語')	#完成上述自定義function按鈕時，投入國語的硬幣於lan投幣孔中
say_hi('英語')
say_hi('q')
print('say_hi-----------------------')

def add(x, y): #也可以於增加不同投幣孔類，達到多parameters。
	print(x + y)
	print(x, y)
add(5, 6)
print('add-----------------------')

def add1 (x=4, y=2): #parameter可以預設defaut值 x=1, y=5 (defaut不需要"空格")
	print(x + y)
add1(6, 8) #投幣孔x: 4->6；投幣孔y: 2->8
add1() #defaut 4+2=6
add1(y=5) #投幣孔y: 2->5；4+5=9
print('add1-----------------------')

def average(numbers):
	return sum(numbers) / len(numbers)

result = average([50, 52, 120])
print(result)
print(average([50, 52, 120]))
print('average-----------------------')


