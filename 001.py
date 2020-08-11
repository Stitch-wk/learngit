# -*- coding: utf-8 -*-
list = []
for i in range(5):
    a = int(input('请输入整数:'))
    list.append(a)
y=sorted(list)
print(list)
print(y)
input('press any key to...')

#尝试修改第一次

#增加了冒泡排序
list = []
print ('请输入十个整数：')
for i in range(10):
    print ('输入第%d个整数：'%i)
    a = input()
    list.append(a)
print (list)
 
for i in range(9):
    for j in range(9 - i):
        if list[j] > list[j+1]:
	        list[j], list[j + 1] = list[j + 1], list[j]
    print (list)

#以下为第三种方法，选择排序

list = []
print ('请输入5个整数：')
for i in range(5):
    print ('输入第%d个整数：'%i)
    a = input()
    list.append(a)
print (list)
 
for i in range(5):
    min_index = i
    for j in range(i + 1, 5):
        if list[j] < list[min_index]:
            min_index = j //找出最小元素下标
    if min_index != i:       
	    list[min_index], list[i] = list[i], list[min_index]
    print (list)
