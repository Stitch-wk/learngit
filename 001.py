# -*- coding: utf-8 -*-
#sorted函数排序方法
list1 = []
for i in range(5):
    num1 = int (input('请输入整数:'))
    list1.append(num1)
list2=sorted(list1)
print(list1)
print(list2)
input('press any key to...')

#增加了冒泡排序法
list3 = []
print ('请输入十个整数：')
for i in range(10):
    print ('输入第%d个整数：'%i)
    num2 = int input()
    list3.append(num2)
print (list3)
 
for i in range(9):
    for j in range(9 - i):
        if list3[j] > list3[j+1]:
	        list3[j], list3[j + 1] = list3[j + 1], list3[j]
print (list3)
input ('press any key to...')

    
