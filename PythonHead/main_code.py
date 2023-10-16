import unittest

import side_code
#------------------------------------------------------------------------------
#------------------------Python基础--------------------------------------------
# 这是一个注释
# ctrl + / 注释所有
#------------------------------------------------------------------------------
# string类型
# string1 = "the String"
# string2 = "the Second String"
# print(string1 + string2) # 字符串的拼接
# print(string1[0]) # 打印字符串某一位置
# print(string1[0:4]) # 打印字符串0到4的字符
#------------------------------------------------------------------------------
# define a fuction
# 函数用def 并且后面加冒号
# 代码行不需要;
# def get__sum(sum1,sum2):
# 	result = sum1 + sum2
# 	return result

# 	print(get__sum(1,2))
#------------------------------------------------------------------------------
#                                           类
# class Persion:
# 	def __init__(self,name,height,weight):
# 		self.name = name
# 		self.height = height
# 		self.weight = weight

# 	def say_name(self):
# 		print("我的名字叫" + self.name)

# persion1 = Persion("lao",170,180)

# persion1.say_name()

# print(persion1.height)
#------------------------------------------------------------------------------
# 数字类型可以细分
# 1.int(integer)
# 2.float
# 3.complex(复数)
# python可以自动识别类型,可以进行强制转换（类似与C）

# 数字类型中的函数
# 1.abs（绝对值）
# 2.round（四舍五入）
# 3.pow（对数字取幂）
# 4.ceil(大于目前这个值的最小整数，需要import导包math AS：import math）
# 5.floor(小于目前这个值的最小整数，需要import导包math AS：import math)
#------------------------------------------------------------------------------
# 对string的函数API
# string = "hello wolrd!"
# 1. len print(len(string)) 取出长度
# 2. capitalize 对字符串第一个字母大写
# 3. upper 对字符串所有字母大写
# 4. lower 对字符串所有字母小写
# 5. replace 进行字符串中的某一段修改 形如：print(string.replace("wolrd","world"))
# 6. find print(string.find("hello")) 输出0
# 		print(string.find("llo")) 输出2
# 7. print(string.split('o',1)) 有o的地方就进行切割，1代表最多只能切一次，若不加，则见o就切
#------------------------------------------------------------------------------
# 以下是布尔类型的函数API
# 7. boolean (True和False)
# 8. isupper 判断字符是否都是大写
# 可以去官方文档去找更多的API
#------------------------------------------------------------------------------
#
# def get_sum(sum1,sum2=4): # 有默认值的参数一定是放在没有默认值的后面
# 	return sum1 + sum2
# print(get_sum(1,6))
#------------------------------------------------------------------------------
# 定义一个列表
# list1 = ["nihao",7,2,3,4,5] # 不限定数据类型
# print(list1[0]) # 可以查找
#
# list1[1] = 9 #直接更改某一个元素的值
#
# list1.append(6) # 在列表中添加一项
#
# list1.pop(0) # 在列表中删除一项
#
# list1.insert(0,0) # 在零的位置插入一个零
#
# list1.sort() # 进行列表的排列 从小到大
# print(list1) # 打印全部
#
# list1.reverse() # 进行从大到小的排列
# print(list1) # 打印全部
#
# list1.remove(3) # 直接移除列表的一个元素 这个元素必须存在于列表中
# print(list1) # 打印全部
#------------------------------------------------------------------------------
# 关于元组，可以把他定义为不能修改的列表
# tuple1 = (1,2,3)
# tuple1[1] = 9 # 如果修改就会报错
#------------------------------------------------------------------------------
# 元组和列表之间是可以转换的
# print(list(tuple1))
#------------------------------------------------------------------------------
# dictionary 字典是一个数据类型也是一个容器
# 辨析，列表是中括号，元组是小括号，字典是大括号
# name height weight就是一个键
# dict1 = {"name":"laozhang","height":170,"weight":100}
# dict1["gender"] = '男' # 可以直接添加一个键
# print(dict1["height"]) # 字典是通过键来查找字典中的值
# print(dict1) # 输出字典以及他的值
# print(len(dict1)) # len也可以用在字典里
# print(dict1.keys()) # keys这个方法是得到所有的键
# print(dict1.values()) # values这个方法是得到所有的值
#------------------------------------------------------------------------------
# set集合，实际上也是一个容器，和列表不同的是，它没有顺序的概念，不能有重复的元素
# set1 = {1,2,3,2}
# print(set1) # 可以看到输出的值是123没有多余的2
# 集合也可以来定义元组（元组是小括号） 定义如下:
# set1 = {1,2,3,2,500}
# set2 = set((2,3,1,9,8,5))
# print(set2)
# 可以看到输出结果如下，集合会自动排序好元素{1, 2, 3, 5, 8, 9}
# print(set2[0]) 若进行此类操作，在集合里用下标查找元素，则会报错
# 有关集合的函数
# set2.add(10) # 添加某一元素
# set2.discard(5)# 删除某一元素
# print(set2)
# print(set1.intersection(set2)) # 算交集
# print(set1.difference(set2)) # 非共有的元素 前面有但是后面没有的元素
# print(set1.issubset(set2)) # 判断前面是不是后面的子集，返回Boolean类型
# 相比于其他的容器，它更加趋向于一个整体，可以进行两个容器的交并补
#------------------------------------------------------------------------------
# 值类型：数字，布尔
# 引用类型：列表，元组，字典，集合，字符串
#------------------------------------------------------------------------------
# 条件控制模拟
# if else语句 elif = else if
# homework_finished = True
#
# if (homework_finished) :
#     print("you can do it")
# else :
#     print("get out to learning")
#
# prize = 1000
# expensive = (prize > 800)
# print(expensive)
#------------------------------------------------------------------------------
# 循环
# while循环
# a = 100
# while (a>50):
#     print(a)
#     a = a - 1
#     print("over")
# for循环
# 可以对序列循环 序列：元组，列表，字符串
# string1 = "wadawdadfafa"
# list1 = ["nihao",7,2,3,4,5]
# # 类似于foreach
# for char in string1:
#     print(char)
# for nono in list1:
#     print(nono)
# # 也可以利用range去实现逐个打印
# for i in range(len(list1)):
#     print(list1[i])
# for j in range(10):
#     print(j)
#     if(j == 5): # 可以用if和break关键字跳出循环
#         break
# print("over")
# patients = [False,True,False,True,True]
#
# for i in patients:
#     if(i):
#         continue
#
#     print("继续治疗")
#------------------------------------------------------------------------------
# 模块
# import 模块（就可以使用该模块里的代码）
# from 模块 import getsum （直接调用这个模块里的一个函数）
# from 模块 import *（导入该模块里的全部内容）
# import 模块 as 更名 （可以更改调用这个模块的名字）
#
# print(side_code.get_sum(2,2))
#------------------------------------------------------------------------------
# 面向对象编程
# 就要用到之前学习的类 不多赘述和java差不多
# 创建对象时，要传入创建类的参数
# class ATM:
#     def __init__(self, id, add, branch): # 每一个类中都有__init__这个函数并且（self，，，）第一个变量是self
#         self.id = id
#         self.add = add
#         self.branch = branch
# 当然在方法里也要有self
#     def ATM_queryID(self, add, id):
#          print(ATM)
# atm1 = ATM("0", "工行", "临汾工行")
# atm2 = ATM("1", "农行", "临汾农行")
# print(atm1.id)
# print(atm1.add)
# print(atm1.branch)
# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.grades = {"语文": 0, "数学": 0, "英语": 0}
#
#     def set_grades(self, couse, grades):
#         if couse in self.grades:
#             self.grades[couse] = grades
#
#     def print_grades(self):
#         print(f"学生{self.name} (学号:{self.student_id}) 的成绩为:")
#         for couse in self.grades:
#             print(f"{couse}: {self.grades[couse]}分")
#
# chen = Student("zhang", "10086")
# zhang = Student("chen", "10094")
#
# zhang.set_grades("语文", 99)
# print(zhang.grades)
# zhang.print_grades()
#------------------------------------------------------------------------------
# 继承（创建有层次的类）
# 这里以不同员工工资计算举例
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def print_info(self):
#         print(f"姓名：{self.name} 工号: {self.id}")
#
# class FullTimeEmployee(Employee):
#     def __init__(self, name, id,monthly_salary):
#         super().__init__(name, id)
#         self.monthly_salary = monthly_salary
#
#     def calculate_monthly_pay(self):
#         return self.monthly_salary
#
# class PartTimeEmployee(Employee):
#     def __init__(self, name, id, daily_salary, work_days):
#         super().__init__(name,id)
#         self.daily_salary = daily_salary
#         self.work_days = work_days
#
#     def calculate_monthly_pay(self):
#         return self.daily_salary * self.work_days
#
# zhang = FullTimeEmployee("zhang", "2003", 5000)
# li = PartTimeEmployee("li","2018",50,20)
# zhang.print_info()
# li.print_info()
# print(f"工资：{zhang.calculate_monthly_pay()}")
# print(li.calculate_monthly_pay())
#------------------------------------------------------------------------------
# 读取文件的格式
# f = open("./data.txt", "r", encoding="utf-8")
# with open("./text", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)
# # 这里建议用with as 因为你比较健忘，怕你忘记写file
# # 如果用with as 一定要记得缩进
# with open("./text", "r", encoding="utf-8") as f1:
#     print(f1.readline())
#     print(f1.readline())
# # 换两行的原因是readline会自动读取文字末尾的换行，而print自带换行，所以会换两行
# with open("./text", "r", encoding="utf-8") as f2:
# # print(f2.readlines())
# # 这样写不好会返回一个列表（有中括号）
# # 这里可以利用for循环
#     lines = f2.readlines()
#     for i in lines:
#         print(i)
#------------------------------------------------------------------------------
# 文件调用会自动将文件设置为r（只读）模式
# 这里展示如何写文件 w（写入）和 a(附加)模式
# 并且有关文件的读取模式下的方法也不能够使用，如：read（）
# with open("./text", "w", encoding="utf-8") as f:
#     f.write("刚才写的被替换成了现在这个\n")
#     f.write("hello,world\n")
# with open("./text", "a", encoding="utf-8") as f:
#     f.write("这是附加文本")
#------------------------------------------------------------------------------
# 在程序的运行中经常会出现各种各样的错误，比如字符串运算错误，文件找不到错误等
# 于是可以添加try except方法

# try:
#     weight = float(input("请输入你的体重："))
# except:
#     print("发生了未知错误")
# else:
# print(f"您的体重是" + weight)
# finally:
# print("结束程序")

# 可以看到，如果用户输入了不是float的参数，系统不会飘红，而是显示出错误原因
# 如果输入了正确的信息，那么else语句将会被执行
# 无论错误与否，finally的语句都将被执行
#------------------------------------------------------------------------------
# import unitteat # 专门用来测试代码的库
# 举例
# class TestMyAdder(unittest.TestCase):
#     def test_positive_with_positive(self):
#         self.assertEquals(my_adder(5,3),8)
#
#     def test_negative_with_positive(self):
#         self.assertEquals(my_adder(-5,3),-2)

# 操作台上会告诉你测试了几个函数，通过了几个函数，如果错了，将会提供错误的原因

#------------------------------------------------------------------------------
#---------------------好了完结撒花一下午学完python的基础知识----------------------
# 现在是20231016 21.53
