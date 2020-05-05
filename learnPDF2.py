"""
 在python中有一个基本的 数据结构 叫做 序列
 本章重点讨论两种：列表和元组
 列表和元组的主要不同在于：列表是可以修改的，而元组不可以
 列表适用于需要中途添加元素的情形，元组适用于出于某种考虑禁止进行修改的情形
"""
# 在数据库中，你可以使用序列来表示人，第一个元素为姓名，第二个元素为年龄
# 如果使用列表来表示（所有元素用方括号括起来，用逗号隔开）类似于下面这样：
edward = ['Edward Gummy', 42]
print(edward)
# 序列中还可以包含其他序列，由此可以构建一个数据库包含各种成员列表：
edward = ['Edward Gummy', 42]
john = ['John Smith', 50]
database = [edward, john]
print(database)
"""
python支持一种数据结构的基本概念，成为容器（container）,
容器基本上是一种可以包含其他对象的对象
两种主要的容器是序列（列表和元组）和映射（如字典）。
在序列中，每个元素都有编号，在映射中，每个元素都有名称，称作“ 键 ”
有一种既不是序列也不是映射的容器叫做集合（set）
"""
# 通用的序列操作

# 1.索引
# 序列中可以使用编号来访问各个元素
greeting = 'Hello'
print(greeting[0])              # python没有专门表示字符的类型，一个字符就是包含一个元素的字符串
# 这成为索引，你可以通过索引来获取序列元素，当你使用负数来索引时，python将从右开始（最后一个元素）往左数：
print(greeting[-1])
# 对于字符字面量（或者其他字面量），可以直接进行索引操作而不用把它赋给变量：
print('hello'[1])
# 当函数返回的是一个序列，可以直接进行索引操作：
# forth = input('year =')[3]
# print(forth)
# 以下程序示例要求你输入年，月（数1--12），日（数1--31），并输出相应的月份名：
"""
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
ending = ['st', 'nd', 'rd'] + 17*['th']\
    + ['st', 'nd', 'rd'] + 7*['th']\
    + ['st']

year = input('Year = ')
month = input('Month(1--12) =')
day = input('Day(1--31) =')

month_number = int(month)
day_number = int(day)

month_name = months[month_number-1]
ordinal = day + ending[day_number-1]

print(month_name + ' ' + ordinal + ',' + year)
"""
# 除了使用索引来访问特定的元素外，还可以使用 切片 来访问特定范围内的元素，为此我们需要两个索引，并用冒号分隔
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
print(tag[32:-4])
# 切片用于提取序列的的一部分，但是需要注意的是：第一个索引是包含第一个元素的编号，第二个元素是切片后剩余的的第一个元素的编号
# 如下所示：
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[3:6])          # 这行输出的是[4, 5, 6]
print(number[0:1])          # 这行输出的是[1]
# 简而言之，你提供的切片的边界，其中一个第一个索引指向的元素是包含在切片里的，第二个索引指定的元素不包含在切片里
"""
几个要点：
1.索引是负数表示从后往前数，表示倒数第几个元素；
2.在执行切片操作时，如果第一个索引指向的元素在第二个索引指向的元素后面(比如倒数第三个元素在第一个元素后面)，
切片就会返回空序列，比如：number[-3,0],结果会返回空序列；
>>[]
3.如果切片结束于序列的末尾，则可以省略第二个索引
number[-3:]
>>[8, 9, 10]
4.如果切片位于序列的开头，则可以省略第一个索引
number[:3]
>>[1, 2, 3]
5.如果要复制整个序列，则可以将两个索引都省略：
number[:]
>>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

# 步长操作
# 切片操作示例：用户输入一个URL，python从中提取域名：
# 从类似www.python.org中提取域名
"""
url = input('please input the URL:')
domain = url[11:-4]
print("Domain name:" + domain)

"""
# 切片操作实际上还有一个参数：步长，步长为1，意味着从一个元素到下一个元素：
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[0:10:1])
# >>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 步长为2，从起点到终点，每隔一个元素提取一个元素：
print(number[0:10:2])
# >>[1, 3, 5, 7, 9]
# 每隔三个元素提取一个元素，直接将步长为4即可：
print(number[::4])
# 步长不能为0 否则无法提取元素；步长可以为负数，python将可以从右往左读：
print(number[8:3:-1])
# >>[9, 8, 7, 6, 5]
print(number[10:0:-2])
# >>[10, 8, 6, 4, 2]
print(number[0:10:-2])
# >>[]
print(number[::-2])
# >>[10, 8, 6, 4, 2]
print(number[5::-2])
# >>[6, 4, 2]
print(number[:8:-2])
# >>[10. 8]

# 序列相加
# 可以使用加法运算符来拼接序列：
print([1, 2, 3] + [4, 5, 6])
# >>[1, 2, 3, 4, 5, 6]
print('Hello' + 'world!')
# >>Hello world!
# 不能拼接字符串和数字，python不支持不同类型的序列拼接
# 序列与数x相乘时，生成重复序列X次的新序列：
print('python'*5)
# >>pythonpythonpythonpythonpython
print([42]*10)
# >>[42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

# None,空列表和初始化
# 空列表一般指不包含任何内容的两个方括号[]表示，如果要表示有着10个元素的列表但没有任何有用的内容可以使用[0]*10
# 有些情况下，需要表示“什么都没有”的值，表示里面没有任何内容，可以使用None。
# 因此，将有着10个元素的列表初始化为0,可以这样表示：
Sequence = [None]*10
# >>[None, None, None, None, None, None, None, None, None, None]

# 序列（字符串）乘法运算示例：
# 在位于屏幕中央且宽度合适的方框内打印句子
'''
sentence = input('Sentence:')
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2

print()
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '| ' +       sentence     + ' |')
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()
'''
# 成员资格
# 要检查特定的值是否包含在序列中，使用运算符in,in检查是否满足指定条件，并返回相应的值：满足时返回True,不满足返回False
# 这样的运算符成为布尔运算符，其前述真值称为布尔值
# 下面是in运算符的使用示例：
permission = 'rw'
print('w' in permission)        # 返回值为True
print('rw'not in permission)    # 返回值为False
print('x' in permission)        # 返回值为False
# user = ['mlh', 'foo', 'bar']
# print(input('Input your user name:') in user)     # 判断输入的名字是否在user列表中，在程序需要进行安全策略时很有用
subject = '$$$ Get Rich Now! $$$'
print('$' in subject)           # 返回值为True，可以用于垃圾邮件过滤器

# 程序示例：从用户那里获取一个用户名和一个PIN码，检查他们组成的列表是否存在与数据库中
'''database = [
    ['albert', '1234'],
    ['dilbert', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
user = input('User name:')
pin = input('PIN code:')
if [user, pin] in database: print('Access granted')
'''

# 长度，最小值和最大值
# 函数len返回序列中的元素个数，min,max分别返回序列中的最小元素和最大元素
number = [100, 34, 678]
print(len(number))
print(min(number))
print(max(number))
print(min(2, 3))
print(max(9, 3, 2, 5))

# 列表不同于元组和字符串的地方在于：列表是可变的，即可以修改其内容，列表还有很多特别的用法
# 函数list:鉴于不能像修改列表一样修改字符串
print(list('hello'))
# 我们可以将任何序列（包括字符串）作为list函数的参数

# 基本列表操作
# 1.修改列表：给列表元素赋值    使用索引法给特定位置的元素赋值x[1] = 2
x = [1, 1, 1]
x[1] = 2
print(x)
# >>[1, 2, 1]
# 不能给超出列表范围的元素赋值
# 2.修改列表：删除列表元素     使用del语句删除列表中的特定元素
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)
# >>['Alice', 'Beth', 'Dee-Dee', 'Earl']
# 3.给切片赋值：
name = list('Perl')
print(name)
# >>['P', 'e', 'r', 'l']
name[2:] = list('ar')
print(name)
# >>['P', 'e', 'a', 'r']
# 通过切片赋值，可以将切片替换为长度与其不同的序列
name = list('Perl')
name[1:] = list('ython')
print(name)
# >>['P', 'y', 't', 'h', 'o', 'n']
# 使用切片赋值还可以在不改变原有元素的情况下插入新的元素
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]        # 替换一个空切片，相当于插入一个序列
print(numbers)
# >>[1, 2, 3, 4, 5]
# 同时还可以用相反的方法删除切片
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []               # 这段代码与del number[1:4]等效
print(numbers)
# >>[1, 5]


# 列表方法
# 方法是与对象（列表，数，字符串）联系紧密的函数。通常像下面这样调用：
# object.method(arguments)
# 方法调用和函数调用很像，只是方法名之前加了对象和句点。列表包含多个可以查看和修改其内容的方法

# 1.append
# append用于将对象附加到列表的末尾
lst = [1, 2, 3]
lst.append(4)
print(lst)
# >>[1, 2, 3, 4]
# append用于就地修改列表，也就是它并不会返回修改后的新列表，而是直接修改新列表

# 2.clear
# 方法clear就地清空列表中的内容
lst = [1, 2, 3]
lst.clear()                 # 类似于切片赋值语句lst[:] = []
print(lst)
# >>[]

# 3.copy
# 方法copy复制列表。常规复制只是将另一个名称关联到列表:
a = [1, 2, 3]
b = a
b[1] = 4
print(a)
# >>[1, 4, 3]
# 要让a,b指向不同的列表，就需要将b关联到a的副本
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)
# >>[1, 2, 3]               # 使用a[:]或list(a)，它们也都复制a
print(b)
# >>[1, 4, 3]

# 4.count
# 方法count计算指定元素在列表中出现多少次
print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
# >>2
x = [[1, 2], 1, 1, [1, [1, 2]]]
print(x.count(1))
# >>2
print(x.count([1, 2]))
# >>1

# 5.extend
# 方法extend让你能够同时将多个值附加到列表末尾，为此可将这些值组成的序列作为参数提供给方法extend
# 也就是说，你可以用一个列表来拓展另一个列表
a = [1, 2, 3]
b = [1, 5, 6]
a.extend(b)
print(a)
# >>[1, 2, 3, 4, 5, 6]
# 这和两个列表的拼接相似，但是列表的拼接并不会改变原有的列表
a = [1, 2, 3]
b = [1, 5, 6]
print(a + b)
# >>[1, 2, 3, 4, 5, 6]
print(a)
# >>[1, 2, 3]
# 拼接出来的列表与前一个示例扩展得到的列表完全相同，但在这里a并没有被修改。鉴于常规拼接必须使用a和b的副本创建一个新列表，
# 因此如果你要获得类似于下面的效果，拼接的效率将比extend低：
a = a + b               # 效率低
# 拼接操作并非就地执行的，即它不会修改原来的列表。要获得与extend相同的效果，可将列表赋给切片，如下所示：
a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b          # 可读性不高
print(a)
# >>[1, 2, 3, 4, 5, 6]

# 6.index
# 方法index用于返回列表中指定值第一次出现时的索引
knight = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knight.index('who'))
# >>4

# 7.insert
# 方法insert用于将对象插入到一个列表中
numbers = [1, 2, 3, 5, 6]
numbers.insert(3, 'four')
print(numbers)
# >>[1, 2, 3, 'four', 5, 6]
# 与extend一样，也可使用切片赋值来获得与insert一样的效果。
numbers = [1, 2, 3, 5, 6, 7]
numbers[3:3] = ['four']
numbers
# >>[1, 2, 3, 'four', 5, 6, 7]
# 这虽巧妙，但可读性根本无法与使用insert媲美

# 8.pop
# 方法pop用于从列表中删除一个元素（末尾为最后一个元素），并返回这个元素
x = [1, 2, 3]
print(x.pop())
# >>3
print(x)
# >>[1, 2]
print(x.pop(0))
# >>1
print(x)
# >>[2]
# pop是唯一一个修改列表并且返回值为非None值得方法
# pop可以实现一种常见的数据结构——栈（stack）,即后进的先出(LIFO)
# push和pop是大家普遍接受的两种栈操作（加入和取走）的名称。Python没有提供push，但可
# 使用append来替代。方法pop和append的效果相反，因此将刚弹出的值压入（或附加）后，得到的栈将与原来相同
x = [1, 2, 3]
x.append(x.pop())
print(x)
# >>[1, 2, 3]
# 要创建先进先出（FIFO）的队列，可使用insert(0, ...)代替append。另外，也可继续使
# 用append，但用pop(0)替代pop()。一种更佳的解决方案是，使用模块collections中的deque

# 9.remove
# 方法remove用于删除第一个为指定值的的元素
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)
# >>['to', 'or', 'not', 'to', 'be']
# remove是就地修改且不返回值的方法之一

# 10.reverse
# 方法reverse用于按照相反的顺序排列列表中的元素
x = [1, 2, 3]
x.reverse()
print(x)
# >>[3, 2, 1]
# reverse修改列表，但不返回任何值（remove和sort一样）
# 如果要按照相反的顺序迭代序列，就需要使用迭代函数reversed,这个函数不返回列表而是返回迭代器
# 你可以使用list将返回的对象转换为列表
x = [1, 2, 3]
print(list(reversed(x)))
# >>[3, 2, 1]

# 11.sort
# 方法sort用于对列表的就地排序，就地排序意味着对原来的列表进行修改，使其元素按顺序排列，而不返回排序后列表的副本
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
# >>[1, 2, 4, 6, 7, 9]
# 这里需要注意的是，方法sort并没有返回值，一下这种做法（误以为sort有返回值）是错误的：
x = [4, 6, 2, 1, 7, 9]
# y = x.sort()  # Don't do this !
# print(y)      # None
# 由于sort只是对x进行排序而不返回任何值最终结果就是x是排过序的，而y是None
# 所以如果需要排序后的列表副本并保留原始副本不变，需要将y关联到x的副本，在对y进行排序：
x = [4, 6, 2, 1, 7, 9]
y = x.copy()
y.sort()
print(y)
# >>y = [1, 2, 4, 6, 7, 9]
# 只是将x赋给y是不可以的，x和y会指向同一个副本，为获取排列后列表的副本，另一种方式是使用函数sorted:
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print(x)
# >>[4, 6, 2, 1, 7, 9]
print(y)
# >>[1, 2, 4, 6, 7, 9]
# 实际上这个函数可以用于任何的序列，但总是返回一个列表
print(sorted('python'))
# >>['h', 'n', 'o', 'p', 't', 'y']

# 12.高级排序
# 方法sort接收两个可使用的参数：key和reverse,这两个参数成为关键字参数
# key类似于参数cmp:你将其设置为一个用于比较的函数，然而并不会直接的进行列表中元素的大小比较
# 它是为每一个元素创造一个键，再根据这些键来对元素进行排序
# 假如要按照元素长度对元素进行排序，可以将key设置为len
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)
# >>['add', 'acme', 'aerate', 'abalone', 'aardvark']
# 对于另一个参数reverse,只需要指定一个真值（True or False）,以指出是否要按照相反的顺序对元素进行排序
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)
# >>[9, 7, 6, 4, 2, 1]

# 元组：不可修改的序列
# 与列表一样，元组也是序列，唯一的差别在于元组是不可修改的（字符串也是不能修改的）
# 元组语法很简单，只要将一些值用逗号分隔，就可以自动创建一个元组
# 1, 2, 3
print(1, 2, 3)
# >>1 2 3
# 如你所见，元组还可以用圆括号括起来（常见）
# (1, 2, 3)
print((1, 2, 3))
# >>(1, 2, 3)
# 空元组用两个什么都不包含的空括号表示
# ()
print(())
# 如果只表示元组中只有一个元素也要加逗号
print(42,)
# >>42
print(42)
# >>42
print((42,))
# (42)和42等效，但加上括号会完全不同
print(3*(40 + 2))
# >>126
print(3*(40 + 2,))
# >>(42, 42, 42)            # 根据结果来看似乎逗号,优先级比加号+要低？
# tuple的工作原理和list类似：它将一个序列作为参数，并将其转变为一个元组，如果参数本身就是一个元组，就原封不动的返回它
print(tuple([1, 2, 3]))
# >>(1, 2, 3)
print(tuple('abc'))
# >>('a', 'b', 'c')
# print(tuple(1, 2, 3))     # Unexpected argument?
# >>(1, 2, 3)
# 元组并不复杂，除了创建和访问元素外，可执行的操作并不多
# 元组创建及其访问元素的方式和其他序列相同
x = 1, 2, 3
print(x[1])
# >>2
print(x[0:2])
# >>(1, 2)
# 熟悉元组的原因：
# 1.元组用作映射中的键（集合的成员），列表不行
# 2.有些内置函数和方法返回的是元组

# 小结：

# 序列：序列是一种数据结构，其中的元素带编号（编号从0开始）。列表、字符串和元组
# 都属于序列，其中列表是可变的（你可修改其内容），而元组和字符串是不可变的（一旦
# 创建，内容就是固定的）。要访问序列的一部分，可使用切片操作：提供两个指定切片起始和结束位置的索引
# 要修改列表，可给其元素赋值，也可使用赋值语句给切片赋值

# 成员资格：要确定特定的值是否包含在序列（或其他容器）中，可使用运算符in将运算符in用于字符串时情况比较特殊——这样可查找子串

# 方法：一些内置类型（如列表和字符串，但不包括元组）提供了很多有用的方法
# 有点像函数，只是与特定的值相关联
# 方法是面向对象编程的一个重要方面

# 本章介绍的新函数：
'''
1.len(seq)                          返回序列的长度
2.list(seq)                         将序列转换为列表
3.max(args)                         返回序列或一组参数中的最大值
4.min(args)                         返回序列或一组参数中的最小值
5.reverse(seq)                      让你能反向迭代序列
6.sorted(seq)                       返回一个有序列表，其中包含了指定序列的所有元素
7.tuple(seq)                        将序列转换为元组

'''









