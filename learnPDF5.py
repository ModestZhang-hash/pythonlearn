# 本章将深入探讨条件语句和循环语句
# 之后我们将探讨列表推导，它们虽然是表达式，但是工作原理几乎与条件和循环相同
# 最后我们将介绍pass,del和exec

# 再谈print和import
# 接下来看看print和import得几个隐藏特性

# 1.打印多个参数
# 显而易见，参数之间加入空格符，用于合并文本和变量值
name = 'Gumby'
salutation = 'Mr.'
greeting = 'Hello'
print(greeting, salutation, name)
# >>Hello Mr. Gumby
# 如果字符串变量greeting不包含逗号，你不能这么做：
print(greeting, ',',salutation,name)
# >>Hello , Mr. Gumby               这将在逗号之前多个空格
# 下面是一种可行的解决方案：
print(greeting + ',', salutation, name)
# >>Hello, Mr. Gumby                它将逗号与变量greeting相加
# 如果需要，还可以自定义分隔符：
print('I', 'wish', 'to', 'register', 'a', 'complaint',sep='_')
# >>I_wish_to_register_a_complaint
# 你还可以自定义结束字符串，用于代替默认的换行符
# 例如如果将结束符定义为空字符，以后就可以继续打印到当前行：
print('Hello,',end='')
print('world')
# >>Hello,world

# 2.导入时重命名
# 从模块导入时，通常使用：
# import somemodule
# 或者使用：
# from somemodule import somefunction
# 或者这样：
# from somemodule import somefunction , anotherfunction, yetanotherfunction
# 或者：
# from somemodule import *
# 仅当你确定要导入模块里的一切时，使用最后一种格式。
# 但如果有两个模块，它们都包含函数open,该如何办呢？
# 你可以使用第一种方式导入模块，就像下面这样：
# module1.open(...)
# module2.open(...)
# 还有一种办法：在语句末尾添加as子语句并指定别名，下面是一个导入整个模块并给它指定别名的例子：
import math as foobar
print(foobar.sqrt(4))
# >>2.0
# 对于前面的函数open，可以这样导入它们：
# from module import open as open1
# from module import open as open2

# 3.序列解包
# 我们可以同时（并行）给多个变量赋值：
x, y, z = 1, 2, 3
print(x,  y, z)
# >>1 2 3
# 觉得用处不大？这种方式可以交换多个变量的值：
x, y = y, x
print(x, y, z)
# >>2 1 3
# 实际上，这里执行的操作为：序列解包（或可迭代对象解包）：
# 即将一个序列（或任意可迭代对象）解包，并将得到的值储存在一系列的变量当中，用下面的例子解释：
values = 1, 2, 3
print(values)
# >>(1, 2, 3)
x, y, z = values
print(x)
# >>1
# 这在使用返回元组（或其他序列或可迭代对象）的函数或方法时很有用
# 假设要从字典中随机获取一个键值对，可使用方法popitem.它随机获取一个键值对并以元组的形式返回
# 接下来可以直接将返回的元组解包到两个变量中：
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, values = scoundrel.popitem()
print(key)
# >>girlfriend
print(values)
# >>Marion
# 这让函数能够返回被元组打包的多个值，然后通过一条赋值语句能够轻松的访问这些值。
# 要解包的序列包含的元素个数必须与你在等号左边列出的目标个数相同。否则python将报错
# x, y, z = 1, 2
# x, y, z = 1, 2, 3, 4              这两种情况都会报错
# 可以使用星号（*）运算符来收集多余的值，这样无需确保值和变量的个数相同，示例如下：
a, b, *rest = [1, 2, 3, 4]
print(rest)
# >>[3, 4]
# 还可以将带星号的变量放到其他位置：
name = "Albus Percival Wulfric Brian Dumbledore"
first, *middle, last = name.split()
print(middle)
# >>['Percival', 'Wulfric', 'Brian']
# 在赋值语句的右边可以是任意类型的序列，但带星号的变量最终包含的总是一个列表，
# 在变量和值的个数相同的时候也是如此
a, *b, c = 'abc'
print(a, b, c)
# >>a ['b'] c
# 这样的收集方式也可以用于函数的参数列表中

# 2.链式赋值
# 链式赋值是一种快捷方式，用于将多个变量关联到同一个值，
# 这有点像前面介绍的并行赋值，但是只涉及一个值：
# x = y = somefunction()
# 上述的代码与下面的代码等价：
'''
y = somefunction()
x = y
'''
# 需要注意的是，这两条语句可能与下面的语句不等价：
'''
x = somefunction()
y = somefunction()
'''

# 3。增强赋值
# 可以不用写代码x = x + 1,简化写法
# x += 1                        这称为增强赋值，适用于所有的标准运算符
x = 2
x += 1
x *= 2
print(x)
# >>6
# 增强赋值也适用于其他数据类型：
fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)
# >>foobarfoobar
# 通过增强赋值让代码更紧凑，更简洁，提高可读性

# 3.缩进的乐趣
# 代码块并不是一种语句，但必须熟悉它
# 代码块是一组语句，可在满足条件时执行（if语句），或者循环执行（for语句），代码块是通过缩进代码来实现的
# 同一代码块中各行代码的缩进量必须相同，下面的伪代码演示如何缩进：
'''
this is a line
this is another line:
    this is another block
    continuing the same block
    the last line of this block
phew,there we escaped the inner block

在很多语言中，都是用特殊的单词或字符（如begin或{）来标识代码块的起始位置
并使用另一个特殊的单词或字符（如end或}）来表示结束位置，在python中使用冒号：来指出
接下来的部分是一个代码块，并将该代码块的每行缩进相同的长度，发现缩进量与之前相同时
你就知道当前代码块结束了
'''

# 条件和条件语句
# 用作布尔表达式时，下面的值都将被解释器视为假：
# >>False None 0 "" () [] {}
# 除了这些，python中的任何值都可以被解释为真。但标准的真值为True和False
# 其实True和False不过是0和1的别名，虽然看起来不同，但作用是相同的
print(True)
# >>True
print(False)
# >>False
print(True == 1)
# >>True
print(False == 0)
# >>True
print(True + False + 42)
# >>43
# 布尔值True和False属于bool类型的，而bool类似list,str,tuple,可以用来转换其他值
print(bool('I think therefore I am'))
# >>True
print(bool(42))
# >>True
print(bool(''))
# >>False
print(bool(0))
# >>False

# 有条件执行和if语句
# 真值可以合并，先来看看真值可以用来做什么：
'''
name = input('What is your name?')
if name.endswith('Gumby'):
    print('Hello, Mr.Gumby!')
# if语句让你有条件的执行代码

# else子语句
name = input('What is your name?')
if name.endswith('Gumby'):
    print('Hello, Mr.Gumby!')
else:
    print('Hello stranger.')
'''
# 还有和if语句很像的条件表达式：C语言中三目运算符的python版本
'''
name = input('What is your name?')
status = 'friend' if name.endswith('Gumby') else 'stranger'
print(status)
# >>What is your name?zhang Gumby
# friend
'''

'''
# elif语句
# 相当于包含条件的else语句
num = int(input('Enter a number:'))
if num > 0:
    print('The number is positive.')
elif num < 0:
    print('The number is nagetive.')
elif num == 0:
    print('The number is zero.')
'''

# 代码块嵌套
# if语句里可以再放if语句：
'''
name = input('What is your name?')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello Mr.Gumby')
    elif name.startswith('Mrs.'):
        print('Hello Mrs.Gumby')
    else:
        print('Hello Gumby')
else:
    print('Hello stranger')
'''
# 更复杂的条件
'''
1.比较运算符
在条件表达式中，最基本的运算符可能就是比较运算符：
x == y                  x等于y
x < y                   x小于y
x > y                   x大于y
x >= y                  x大于等于y
x <= y                  x小于等于y
x != y                  x不等于y
x is y                  x和y是同一个对象
x is not y              x和y是不同的对象
x in y                  x是容器（如序列）y的成员
x not in y              x不是容器(如序列)y的成员
'''
'''
从理论上说，可使用<和<=等运算符比较任意两个对象x和y的相对大小，并获得一个真
值，但这种比较仅在x和y的类型相同或相近时（如两个整数或一个整数和一个浮点数）才有
意义
将整数与字符串相加毫无意义，检查一个整数是否小于一个字符串也是一样。奇怪的
是，在Python 3之前，竟然可以这样做。不过即便你使用的是较旧的Python版本，也应对这类
比较敬而远之，因为结果是不确定的，每次执行程序时都可能不同。在Python 3中，已经不允
许这样比较不兼容的类型了
'''
# 同赋值一样，python也支持链式比较，可以同时使用多个运算比较符，如0 < age < 100
#  ==相等运算符：
print('foo' == 'foo')
# >>True
print('foo' == 'bar')
# >>False
# 一个等号是赋值运算符，用于修改值，

# is：相同运算符
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x is z)
# >>False
print(x == z)
# >>True
# is只是用于判断两个变量是否相同（指向同一个对象），并不能判断是否相等
# 两个列表虽然相等，但并不相同
# 用下面的例子来说明：
x = [1, 2, 3]
y = [2, 4]
del x[2]
y[1] = 1
y.reverse()
print(x == y)
# >>True
print(x is y)
# >>False

# in成员资格运算符
'''
name = input('What is your name?')
if 's' in name:
    print("Your name contains the letter 's'")
else:
    print("Your name doesn't contain the letter 's'")
'''
# 字符串和序列的比较
# 字符串是根据字母的排列顺序来进行比较的：
print('alpha' < 'beta')
# >>True
# 字符都是按顺序值进行排列的，要获取字符的顺序值，使用函数ord
print(ord('a'))
# >>97
print(ord('b'))
# >>98
print(ord('A'))
# >>65
print(ord('B'))
# >>66
print('a' < 'B')
# >>False
# 忽略大小写，可以使用字符串方法lower
print('a'.lower() < 'B'.lower())
# >>True
print('JetBrain'.lower() == 'jetbrain'.lower())
# >>True
print([1, 2] < [2, 1])
# >>True
print([1, [2, 4]] < [1, [2, 5]])
# >>True

# 布尔运算符
# 举例说明：
'''
number = int(input('Please enter a number between 1 and 10:'))
if number > 1:
    if number < 10:
        print('It is correct.')
    else:
        print('It is wrong.')
else:
    print('It is wrong.')
# 这样虽然可行。但是输出了两次'It is wrong'
# 可以使用如下方法：
number = int(input('Please enter a number between 1 and 10:'))
if number > 1 and number < 10:
    print('It is correct.')
else:
    print('It is wrong.')
'''
# 短路逻辑和条件表达式
'''
布尔运算符有个有趣的特征：只做必要的计算。例如，仅当x和y都为真时，表达式x and 
y才为真。因此如果x为假，这个表达式将立即返回假，而不关心y。实际上，如果x为假，这
个表达式将返回x，否则返回y。（这将提供预期的结果，你明白了其中的原理吗？）这种行为
称为短路逻辑（或者延迟求值）：布尔运算符常被称为逻辑运算符，如你所见，在有些情况下
将“绕过”第二个值。对于运算符or，情况亦如此。在表达式x or y中，如果x为真，就返回
x，否则返回y。（你明白这样做合理的原因吗？）请注意，这意味着位于布尔运算符后面的代
码（如函数调用）可能根本不会执行。像下面这样的代码就利用了这种行为：
name = input('Please enter your name: ') or '<unknown>' 
如果没有输入名字，上述or表达式的结果将为'<unknown>'。在很多情况下，你都宁愿使
用条件表达式，而不耍这样的短路花样。不过前面这样的语句确实有其用武之地
'''
# 断言
# if语句有个很有用的‘亲戚’，功能实现类似下面的伪代码：
'''
if not condition:
    crash program
为什么要编写这样的代码呢？因为在错误条件发生时立即崩溃胜过以后让它让崩溃
基本上你可以要求某些条件得到满足，为此可在语句中使用关键字assert
age = 10
assert 0 < age < 10
age = -1
assert 0 < age < 10
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
AssertionError
如果知道程序满足特定条件才会正确执行，可以加入assert语句作为检查点
还可以在条件后面加一个字符串，用于对断言做出说明：
age = 1
assert 0 < age < 100, 'The age must be realistic' 
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
AssertionError: The age must be realistic 
'''

# 循环
# 循环的伪代码：
'''
while we aren't stopped:
    send mail
    waite one month
'''
# while循环
# 为了避免繁琐的代码，需要像下面这样：
x = 1
while x < 100:
    print(x)
    x += 1
# 你还可以使用循环确保用户输入的是名字：
'''
name = ''
while not name:
    name = input('Please enter your name:')
    print('Your name is {}'.format(name))
请尝试运行这些代码，并在要求你输入名字时直接按回车键。你会看到提示信息再次出现，
因为name还是为空字符串，这相当于假
如果你只是输入一个空格字符（将其作为你的名字），结果将如何呢？试试看。程序将
接受这个名字，因为包含一个空格字符的字符串不是空的，因此不会将name视为假。这
无疑是这个小程序的一个瑕疵，但很容易修复：只需将while not name改为while not name 
or name.isspace()或while not name.strip()即可
'''
# for循环
# while语句非常灵活，可用于在条件为真时反复执行代码块。
# 在这种情况下通常很好，但是有时候你可能需要自己定制：
# 这种需求一般是针对序列（或其他可迭代对象）中每个元素执行代码块
# 可迭代对象一般是指可以使用for循环进行遍历的对象
# 为此，可以使用for语句：
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
 print(word)

# 或者这样：
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
 print(number)
# python提供了一个可以创建范围的内置函数：
print(list(range(0, 10)))
# >>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 范围类似切片，显示起始位置0，但不显示结束位置10，下面的程序打印数1-100：
for number in range(1, 101):
    print(number)
# 相比之前的while代码，这段代码显得紧凑的多
# 只要能够使用for循环就不要使用while循环

# 迭代字典
# 要遍历字典的所有关键字，可以像遍历序列那样使用for语句
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'correspond to', d[key])
# 也可以使用keys来返回字典中的所有键，如果只对值感兴趣可以使用d.value
# 你可能还记得d.item以元组的形式返回字典的键值对，for循环的一个优点是，可在其中使用序列解包
for key, values in d.items():
    print(key, 'correspond to', values)
'''
字典元素的排列顺序是不确定的。换而言之，迭代字典的键或值时，一定会处理所有的
键或值，但不知道处理的顺序。如果顺序很重要，可将键或值存储在一个列表中并对列
表排序，再进行迭代。要让映射记住其项的插入顺序，可使用模块collections中的
OrderedDict类
'''

# python迭代工具
# python提供了一些可以帮助迭代序列（或其他可迭代对象），有些内置函数使用起来很方便
# 1.并行迭代
# 有时候你想要同时迭代两个序列，假设有下面两个列表：
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# 如果要打印名字以及对应年龄，可以这样：
for i in range(len(names)):
 print(names[i], 'is', ages[i], 'years old')
# i是作为循环索引变量的标准名称，有一个很有用的并行迭代工具函数zip，它将两个并行序列‘缝合’起来
# 返回一个由元组组成的序列，返回值是一个适合迭代的对象，要查看其内容，可以使用list将其转换为列表
print(list(zip(name, ages)))
# >>[('A', 12), ('l', 45), ('b', 32), ('u', 102)]
# 函数zip可用于缝合任意数量的序列，需要指出的是，当序列的长度不同时，zip将在最短长度的序列用完后结束缝合

# 2.迭代时获取索引
'''
在有些情况下，你需要在迭代对象序列的同时获取当前对象的索引。例如，你可能想替换一
个字符串列表中所有包含子串'xxx'的字符串。当然，完成这种任务的方法有很多，但这里假设
你要像下面这样做：
for string in strings: 
 if 'xxx' in string: 
 index = strings.index(string) # 在字符串列表中查找字符串
 strings[index] = '[censored]'
这可行，但替换前的搜索好像没有必要。另外，如果没有替换，搜索返回的索引可能不对（即
返回的是该字符串首次出现处的索引）。下面是一种更佳的解决方案：
index = 0 
for string in strings: 
 if 'xxx' in string: 
 strings[index] = '[censored]' 
 index += 1 
这个解决方案虽然可以接受，但看起来也有点笨拙。另一种解决方案是使用内置函数
enumerate。
for index, string in enumerate(strings): 
 if 'xxx' in string: 
 strings[index] = '[censored]'
这个函数让你能够迭代索引键值对，其中的索引是自动提供的
'''

# 3.反向迭代和排序后迭代
'''
来看另外两个很有用的函数：reversed和sorted。它们类似于列表方法reverse和sort（sorted
接受的参数也与sort类似），但可用于任何序列或可迭代的对象，且不就地修改对象，而是返回
反转和排序后的版本。
>>> sorted([4, 3, 6, 8, 3]) 
[3, 3, 4, 6, 8] 
>>> sorted('Hello, world!') 
[' ', '!', ',', 'H', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r', 'w'] 
>>> list(reversed('Hello, world!')) 
['!', 'd', 'l', 'r', 'o', 'w', ' ', ',', 'o', 'l', 'l', 'e', 'H'] 
>>> ''.join(reversed('Hello, world!')) 
'!dlrow ,olleH' 
请注意，sorted返回一个列表，而reversed像zip那样返回一个更神秘的可迭代对象。你无需
关心这到底意味着什么，只管在for循环或join等方法中使用它，不会有任何问题。只是你不能
对它执行索引或切片操作，也不能直接对它调用列表的方法。要执行这些操作，可先使用list对
返回的对象进行转换。
'''

# 跳出循环
# 有些情况下，你可能会想要终止循环，并进行新一轮迭代或者直接结束循环
'''
1.break
要结束循环或者跳出循环，可以使用break.假设你要找出小于100的最大平方值（整数与自己相乘的结果），
可以从100向下迭代，找到一个平方值后直接终止迭代，无需继续迭代，直接跳出循环
from math import sqrt
for n in rang(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
如果你输出这个程序，将到81程序结束，注意到我向range传递了第三个参数——步长，
即序列中相邻数的差通过将步长设置为负数，可让range向下迭代，如上面的示例所示；还可
让它跳过一些数：
range(0, 10, 2) 
[0, 2, 4, 6, 8] 


2.continue
语句continue没有break用得多。它结束当前迭代，并跳到下一次迭代开头。这基本上意味
着跳过循环体中余下的语句，但不结束循环。这在循环体庞大而复杂，且存在多个要跳过它的原
因时很有用。在这种情况下，可使用continue，如下所示：
for x in seq: 
 if condition1: continue 
 if condition2: continue 
 if condition3: continue 
 do_something() 
 do_something_else() 
 do_another_thing() 
 etc() 
然而，在很多情况下，使用一条if语句就足够了
for x in seq: 
 if not (condition1 or condition2 or condition3): 
 do_something() 
 do_something_else() 
 do_another_thing() 
 etc() 
'''
'''
3. while True/break成例
在Python中，for和while循环非常灵活，但偶尔遇到的一些问题可能让你禁不住想：如果这
些循环的功能更强些就好了。例如，假设你要在用户根据提示输入单词时执行某种操作，并在用
户没有提供单词时结束循环。为此，一种办法如下：
word = 'zhangxiaoqian'
while word:
 word = input('Please enter a word: ')
 # 使用这个单词做些事情：
 print('The word was', word)        # 需要空字符结束循环
 
 这与你希望的一致，但你可能想使用单词做些比打印它更有用的事情。然而，如你所见，这
些代码有点难看。为进入循环，你需要将一个哑值（未用的值）赋给word。像这样的哑值通常昭
示着你的做法不太对。下面来尝试消除这个哑值
word = input('Please enter a word:')
while word:
    print('The word is :', word)
    word = input('Please input a word:')
    # 哑值消除了，但包含重复的代码（这样也不好）：需要在两个地方使用相同的赋值语句并调
# 用input。如何避免这样的重复呢？可使用成例while True/break
while True:
    word = input('Please enter a word: ')
    if not word:
        break
    print('The word was ', word)
while True导致循环永不结束，但你将条件放在了循环体内的一条if语句中，而这条if语句
将在条件满足时调用break。这说明并非只能像常规while循环那样在循环开头结束循环，而是可
在循环体的任何地方结束循环。if/break行将整个循环分成两部分：第一部分负责设置（如果使
用常规while循环，将重复这部分），第二部分在循环条件为真时使用第一部分初始化的数据。
虽然应避免在代码中过多使用break（因为这可能导致循环难以理解，在一个循环中包含多
个break时尤其如此），但这里介绍的技巧很常见，因此大多数Python程序员（包括你自己）都能
够明白你的意图
'''

'''
4.循环中的else语句
通常，在循环中使用break是因为你“发现”了什么或“出现”了什么情况。要在循环提前
结束时采取某种措施很容易，但有时候你可能想在循环正常结束时才采取某种措施。如何判断循
环是提前结束还是正常结束的呢？可在循环开始前定义一个布尔变量并将其设置为False，再在跳
出循环时将其设置为True。这样就可在循环后面使用一条if语句来判断循环是否是提前结束的
broke_out = False 
for x in seq: 
 do_something(x) 
 if condition(x): 
 broke_out = True 
 break 
 do_something_else(x) 
if not broke_out: 
 print("I didn't break out!") 
一种更简单的办法是在循环中添加一条else子句，它仅在没有调用break时才执行。继续前
面讨论break时的示例
from math import sqrt
'''
'''
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        print("Didn't find it!")
'''

# 简单推导
# 列表推导是一种简单推导形式，类似于数学中的集合推导
# 列表推导的工作原理很简单，类似于for循环
print([x * x for x in range(10)])
# >>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 如果只想打印能被3整除的平方数，可以使用以下方法：
print([x * x for x in range(10) if x % 3 == 0])
# >>[0, 9, 36, 81]
# 我们还可以添加更多的for部分：
print([(x, y) for x in range(3) for y in range(3)])
# >>[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 作为对比，下面两个循环生成同样的列表：
result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)
# >>[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 使用圆括号代替方括号并不能实现元组推导，而是将创建生成器，详细信息请参阅第9章的
# 旁注“简单生成器”。然而，可使用花括号来执行字典推导
squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[8])
# >>8 squared is 64

# 大致介绍一下另外三条语句：pass、del和exec。
# 有时候什么都不用做。这种情况不多，但一旦遇到，知道可使用pass语句大有裨益
# pass                  什么都没发生
# 那么为何需要一条什么都不做的语句呢？在你编写代码时，可将其用作占位符。例如，你可
# 能编写了一条if语句并想尝试运行它，但其中缺少一个代码块
# 这些代码不能运行，因为在Python中代码块不能为空。要修复这个问题，只需在中间的代码
# 块中添加一条pass语句即可
name = 'Bill Gates'
if name == 'Ralph Auldus Melish':
 print('Welcome!')
elif name == 'Enid':
 # 还未完成……
 pass
elif name == 'Bill Gates':
 print('Access Denied')
# >>Access Denied

# 使用del删除
# 对于你不再使用的对象，Python通常会将其删除（因为没有任何变量或数据结构成员指向它）
x = ['i', 'python']
y = x
del x[1]
print(x)            # >>['i']
print(y)            # >>['i']

a = ['i', 'python']
b = a
del a               # the variable 'a' is not defined
print(b)           # <<['i', 'python']

# 使用exec和eval来处理字符串以及计算结果
# 函数exec将字符串作为代码执行：
exec("print('Hello World')")
# >>Hello World
# 调用exec函数时只传递一个参数绝非好事
# 因为函数执行实际上需要分配一个命名空间：用于放置变量的地方
# 否则代码将污染你的命名空间，也就是修改你的变量：
'''
比如像这样：
from math import sqrt
exec("sqrt = 1")
sqrt(4)
运行会报错：
Traceback (most recent call last): 
 File "<pyshell#18>", line 1, in ? 
 sqrt(4) 
TypeError: object is not callable: 1 
'''
# 函数exec主要用于动态地创建代码字符串。如
# 果这种字符串来自其他地方（可能是用户），就几乎无法确定它将包含什么内容。因此为了安全起见，要提供一个字典以充当命名空间
'''
命名空间（作用域）是个重要的概念，将在下一章深入讨论，但就目前而言，你可将命
名空间视为放置变量的地方，类似于一个看不见的字典。因此，当你执行赋值语句x = 1
时，将在当前命名空间存储键x和值1。当前命名空间通常是全局命名空间（到目前为止，
我们使用的大都是全局命名空间），但并非必然如此
'''
# 为此你可以添加第二个参数字典，用作代码字符串的命名空间：
from math import sqrt
scope = {}
exec('sqrt = 1', scope)
print(sqrt(4))              # 2.0
print(scope['sqrt'])        # 1
# 请注意，如果你尝试将scope打印出来，将发现它包含很多内容，这是因为自动在其中添加
# 了包含所有内置函数和值的字典__builtins__
len(scope)          # 2
scope.keys()        # ['sqrt', '__builtins__']

# eval
# eval类似于exec的内置函数，exec执行一系列的python语句，而eval计算字符串中表达式的值
# 并返回结果，而exec并不返回，因为它本身是一条语句，比如你可以使用如下代码来创建一个简单计算器

# eval(input("Enter an arithmetic expression: "))

# 与exec一样，也可向eval提供一个命名空间，虽然表达式通常不会像语句那样给变量重新赋值
# 虽然表达式通常不会给变量重新赋值，但绝对能够这样做，如调用给全局变量重新赋值
# 的函数。因此，将eval用于不可信任的代码并不比使用exec安全。当前，在Python中执行
# 不可信任的代码时，没有安全的办法。一种替代解决方案是使用Jython（参见第17章）等
# Python实现，以使用Java沙箱等原生机制

'''
小结：
本章介绍了多种语句：

1.打印语句：
你可使用print语句来打印多个用逗号分隔的值。如果print语句以逗号结尾，
后续print语句将在当前行接着打印

2.导入语句：
有时候，你不喜欢要导入的函数的名称——可能是因为你已将这个名称用作
他用。在这种情况下，可使用import ... as ...语句在本地重命名函数

3.赋值语句：
通过使用奇妙的序列解包和链式赋值，可同时给多个变量赋值；而通过使用
增强赋值，可就地修改变量

4.代码块：
代码块用于通过缩进将语句编组。代码块可用于条件语句和循环中，还可用于
函数和类定义中（这将在本书后面介绍）

5.条件语句：
条件语句根据条件（布尔表达式）决定是否执行后续代码块。通过使用if/elif/
else，可将多个条件语句组合起来。条件语句的一个变种是条件表达式，如a if b else c

6.断言：
断言断定某件事（一个布尔表达式）为真，可包含说明为何必须如此的字符串。
如果指定的表达式为假，断言将导致程序停止执行（或引发第8章将介绍的异常）。最好
尽早将错误揪出来，免得它潜藏在程序中，直到带来麻烦

7.循环：
你可针对序列中的每个元素（如特定范围内的每个数）执行代码块，也可在条件
为真时反复执行代码块。要跳过代码块中余下的代码，直接进入下一次迭代，可使用
continue语句；要跳出循环，可使用break语句。另外，你还可在循环末尾添加一个else
子句，它将在没有执行循环中的任何break语句时执行

8.推导：
推导并不是语句，而是表达式。它们看起来很像循环，因此我将它们放在循环中
讨论。通过列表推导，可从既有列表创建出新列表，这是通过对列表元素调用函数、剔
除不想要的函数等实现的。推导功能强大，但在很多情况下，使用普通循环和条件语句
也可完成任务，且代码的可读性可能更高。使用类似于列表推导的表达式可创建出字典

9.pass、del、exec和eval：
pass语句什么都不做，但适合用作占位符。del语句用于删除变
量或数据结构的成员，但不能用于删除值。函数exec用于将字符串作为Python程序执行。
函数eval计算用字符串表示的表达式并返回结果
'''
'''
本章介绍的新函数：
1.chr(n)                                返回一个字符串，其中只包含一个字符，这个字符对应于传入的顺序值n（0 ≤
                                        n < 256）
2.eval(source[,globals[,locals]])       计算并返回字符串表示的表达式的结果
3.exec(source[, globals[, locals]])     将字符串作为语句执行
4.enumerate(seq)                        生成可迭代的索引键值对
5.ord(c)                                接收一个只包含一个字符的字符串，并返回这个字符的顺序值
6.range([start,] stop[, step])          创建一个由整数组成的列表
7.reversed(c)                           按照相反的顺序返回seq中的值，以便用于迭代
8.sorted(seq[,cmp][,key][,reverse])     返回一个列表，其中包含seq中的所有值且这些值是经过排序的
9.xrange([start,] stop[, step])         创建一个用于迭代的xrange对象
10.zip(seq1, seq2,...)                  创建一个适合用于并行迭代的新序列
'''
























