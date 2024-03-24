def sum_of_list(a):
	return sum(a)
print(sum_of_list([1, 2, 3]))

# for loop來處理清單
def sum_of_list1(b):
	sum_num = 0
	for num in b:
		sum_num += num # sum_num = b清單中每一筆相加
	return sum_num
print(sum_of_list1([1, 2, 3]))