# print(input("the meaning of life:"))

# x = input("x =")
# y = input("y =")
# print(int(x)*int(y))

'''
if 1 == 2:
     print("one equals two")
 if 1 == 1:
        print("one equals one")
'''



# print(2**3)
# print(pow(2, 3))

print(abs(-10))     # abs实现取绝对值
print(round(2/3))   # round实现将浮点型数取其最接近的整数

# 整数总是向下圆整，round实现取其最接近的整数，如果计算出一个人的年龄位32.9，他未满33岁，这时候就需要用floor函数
# 但你并不能直接调用floor函数，因为它包含在模块math中
import math
print(math.floor(32.9)) # floor函数实现浮点数向下圆整，类似于将浮点数进行int强制类型转换
print(int(32.9))
# 还有一些类似的函数str和float能够实现转换数据类型；实际上它们并不是函数而是类
print(math.ceil(32.3)) # 和floor函数相反，ceil函数实现浮点数向上取整

# 有如下import函数的变种：
from math import sqrt
print(sqrt(9))          # 使用from...import...的格式可以在调用函数时不指定函数所在的模块
# 同时python支持通过变量来调用函数，比如执行赋值语句foot = math.import后，就可以使用foot来求一个数的平方根了foot(4)=2.0

# 向求平方根函数sqrt赋值一个负数：
# print(sqrt(-9))         # 编译器会报错
# 负数的平方根是个虚数，python提供了一个求解虚数（复数）的模块
import cmath
print(cmath.sqrt(-1))     # 输出结果为1j
# 这里需要注意的是：这里并没有使用from..import..命令格式，因为一旦使用的话会无法正常使用sqrt函数
# 所以除非万不得已使用这种命令格式，一般只是用import math命令格式
# python并没有专门表示虚数的类型，虚数一般看作实部为零的复数类型

# name = input("what is your name?")
# print("Hello," + name + "!")

# 字符串
print('hello world')
print("hello world")
print('"hello world" she said')
print("let\'s go!")
print("\"hello world\" she said")
print("let's say: " '"hello world"')        # 合并字符串输出

# 拼接字符串
print('hello,' + 'world')
x = 'hello,'
y = 'world'
print(x + y)
# str使得字符串里的特殊字符尽可能地以合适的编码操作输出;repr按照原本的格式原模原样的输出
print(str("hello,\nworld"))
print(repr("hello,\nworld"))
# 在python3中，所有的字符串都是Unicode编码型字符串

# 长字符串：在表示很长的字符串时，需要我们使用三引号
print('''This is very long string .It continues here.
and it's not over yet."Hello World!"
Still here.''')     # 使用三引号的长字符串本身可以包含单引号和双引号，所以无需使用\进行转义

# 原始字符串：保证我们不以特殊的方式处理反斜杠，不适用原始字符串的话，我们会需要多个\进行字符串转义：
print("path = 'C:\nwhere'")
path = 'C:\nwhere'
print(path)         # 不使用原始字符串
# 对于很长的路径就需要大量的\
path = 'C:\\Program Files\\fnord\\foo\\bar\\baz\\frozz\\bozz'
print(path)
# 这时候如果使用原始字符串就不会对\做特殊处理，原模原样的输出：
print(r'C:\nwhere')
print(r'C:\Program Files\fnord\foo\bar\baz\frozz\bozz')
# 正如所见，原始字符串用r前缀来表示；它几乎可以保留所有的字符
# 原始字符串不会对\进行转义：
print(r"let\'s go")

# Unicode编码（字符串前\u或\U前缀）
print("\u00c6")
print("\U0001F60A")
print("This is a cat:\N{Cat}")

'''
本章介绍的新函数：
1. abs(number)                      返回指定数的绝对值
2.bytes(string,encoding[,error])    对指定的字符串进行编码，并以指定的方式处理错误
3.cmath.sqrt(number)                返回平方根，可用于负数
4.float(object)                     将字符串或者数字转换为浮点型数
5.help([object])                    提供交互式帮助
6.input(prompt)                     以字符串的方式获取用户输入
7.int(object)                       将字符型或浮点型数转换成整数
8.math.ceil(number)                 以浮点数的方式返回向上圆整的结果
9.math.floor(number)                以浮点数的方式返回向下圆整的结果
10.math.sqrt(number)                返回平方根，不能用于负数
11.pow(x,y[,z])                     返回x的y次方对z求模的结构
12.print(object, ...)               将提供的实参打印出来，用空格分隔
13.repr(object)                     返回指定的字符串表示
14.round(number,[n.digits])         四舍五入为指定的精度，正好为5时舍入到偶数
15.str(object)                      将指定的值转换为字符串，用于转换bytes时，可以指定编码和错误处理方式
'''





