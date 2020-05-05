# 设置字符串的格式：完整版
# 本内容的基本思想是对字符串调用方法format,并提供要设置其格式的值
# 字符串包含有关如何设置格式的信息，这些信息是使用一种微型格式指定的语言的(mini-language)指定的
# 要在最终结果中包含花括号，可在格式字符串中使用两个花括号{{和}}指定
# '{{ceci n'est pas une replacement field}}}'.format()
# >>'ceci n'est pas une replacement field}'

# 在格式字符串中最重要的一部分就是替换字段，替换字段有如下部分组成

"""
字段名：
索引或标识符，指出要设置哪个值的格式并使用结果来替换该字段。除指定值
外，还可指定值的特定部分，如列表的元素。
转换标志：
跟在叹号后面的单个字符。当前支持的字符包括r（表示repr）、s（表示str）
和a（表示ascii）。如果你指定了转换标志，将不使用对象本身的格式设置机制，而是使
用指定的函数将对象转换为字符串，再做进一步的格式设置。
格式说明符：
跟在冒号后面的表达式（这种表达式是使用微型格式指定语言表示的）。格
式说明符让我们能够详细地指定最终的格式，包括格式类型（如字符串、浮点数或十六
进制数），字段宽度和数的精度，如何显示符号和千位分隔符，以及各种对齐和填充方式。
下面详细介绍其中的一些要素。
"""

# 替换字段名
# 两种方法：
# 1.只需向format提供要设置其格式的为命名参数，并在格式字符串中使用未命名字段，此时将按顺序将字段和参数匹配
# 2.给参数指定名称，这种参数将被用于相应的替换字段中，你可以混合使用两种方法：
print("{foo} {} {bar} {}".format(1, 2, bar=4, foo=3))
# >>3 1 4 2
# 还可以使用索引来指定使用相应的未命名的参数，这样可以不按顺序使用相应未命名的参数
print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))
# >>3 2 4 1
# 然而不能同时使用手工编号和自动编号，这样会混乱不堪
# 你不仅可以使用提供的值本身，还可以访问它的组成部分（就像在常规代码python中一样）：
fullname = ['Alfred','Smoketoomuch']
print("Mr {name[1]}".format(name = fullname))
# >>Mr Smoketoomuch
import math
tmpl = "The {mod.__name__}module defines the value {mod.pi} for π"
# 注意此处的下划线是两个_组成的__name__而不是一个_name_
print(tmpl.format(mod = math))
# >>'The math module defines the value 3.141592653589793 for π'
# 可使用索引，还可使用句点表示法来访问导入的模块中的方法、属性、变量和函数（看起来很怪异的变量__name__包含指定模块的名称）

# 基本转换
# 指定要在字段中包含的值后，就可以添加有关设置其指格式的指令了
# 首先提供一个转换标志
print("{pi!s}{pi!r}{pi!a}".format(pi = "π"))
# 上述三个标志（s,r和a）指定分别使用str,repr和ascii进行格式转换
# 函数str通常创建普通外观的字符串版本（不对输入的字符串做任何处理）
# 函数repr尝试创建给定值的python表示（一个字符串字面量）
# 函数ascii只创建用于ASCII字符的表示
# 可以指定要转换的值是哪种类型：格式说明
print("The number is {num}".format(num = 42))
# >>The number is 42
print("The number is {num:f}".format(num = 42))     # {num:f}指定输入的值按浮点型输出
# >>The number is 42.000000
print("The number is {num:b}".format(num = 42))     # {num:b}指定输入的值按二进制形式输出
# >>The number is 101010
'''
字符串格式设置中的各种类型说明符：
1.b                 将整数表示为二进制数
2.c                 将整数解读为Unicode码点
3.d                 将整数视为十进制数进行处理，这是整数默认使用的说明符
4.e                 用科学表示法表示小数（用e表示整数）
5.E                 与e相同，但使用E来表示指数
6.f                 将小数表示为浮点数
7.F                 与f相同，但遇到特殊值（nan或者inf），使用大写表示
8.g                 自动在定点表示法和科学表示法之间选择。默认的用于小数的说明符，默认情况下至少有一位小数
9.G                 与g相同，只是使用大写表示指数和特殊值
10.n                与g相同，但插入随区域而异的数字分隔符
11.o                将整数表示为八进制数
12.s                保持字符串的格式不变，默认用于字符串的说明符
13.x                将整数表示为十六进制数并用小写字母
14.X                与x相同但使用大写
15.%                将数表示为百分比值（乘以100.在说明符后面加上f格式，再在后面加上%）
'''

# 宽度，精度和千位分隔符
# 浮点数默认显示小数点后6位，除非需要在格式说明中指定宽度和精度
# 宽度是由整数指定的：
print("{num:10}".format(num = 3))
# >>'         3'
print("{name:10}".format(name = "Bob"))
# >>'Bob       '
# 如上所示，数和字符串的对齐方式也不同
# 精度也是用整数表示的，但是需要在前面加上表示小数的句点：
import math
print("Pi day is {pi:.2f}".format(pi = math.pi))
# >>Pi day is 3.14
# 可以同时指定宽度和精度：
print("{pi:10.2f}".format(pi = math.pi))
# >>'      3.14'
# 实际上，对于其他类型也可以指定精度，但是并不常见：
print('The father of python is {:.5}'.format("Guido van Rossum"))
# >>The father of python is Guido
# 可以使用逗号表示你要使用千位分隔符：
print("The googol is {:,}".format(10*100))
# >>The googol is 1,000

# 符号，对齐和0填充
# 字符串和数字的默认对齐方式不同，如果一栏中同时包含字符串和数字，需要修改默认对齐方式
# 在指定宽度和精度的数前面，可添加一个标志。这个标志可以是零、加号、减号或空格，其中零表示使用0来填充数字:
import math
print("{:010.2f}".format(math.pi))              # 宽度和精度前加0表示用0填充
# >>0000003.14
# 要指定左对齐、右对齐和居中，可分别使用<、>和^：
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(math.pi))
# >>3.14
#    3.14
#       3.14
# 可以使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充:
print("{:$^15}".format("WIN BIG"))
# >>$$$$WIN BIG$$$$
# 还有更具体的说明符=，它指定将填充字符放在符号和数字之间：
print("{0:10.2f}\n{1:10.2f}".format(math.pi,-math.pi))     # 这里的{0:}和{1:}表示位置
#       3.14
#      -3.14
print("{0:10.2f}\n{1:=10.2f}".format(math.pi,-math.pi))
# >>      3.14
# >>-     3.14
# 如果要给正数加上符号，可使用说明符+（将其放在对齐说明符后面），而不是默认的-.如果将符号说明符指定为空格，
# 会在正数前面加上空格而不是+
print("{0:-.2}\n{1:-.2}".format(math.pi,-math.pi))          # 默认设置
# >>3.1                     # {}里面的正负号属于格式化的负号:如果是+就正号加正,负号加负;如果是–就是正号不变,符号加负
# >>-3.1
print("{0:-.2f}".format(math.pi))
# >>3.14
print("{0:.2f}".format(math.pi))
# >>3.14
print("{0:.2f}".format(-math.pi))
# >>-3.14
print("{0:+.2}\n{1:-.2}".format(math.pi,-math.pi))
# >>+3.1
# -3.1
print("{0:.2}\n{1:.2}".format(+math.pi,-math.pi))
# >>3.1
# -3.1
print("{0:+.2}\n{1:+.2}".format(math.pi,-math.pi))
# >>+3.1
# -3.1
print("{0: .2}\n{0:.2}".format(math.pi,-math.pi))
# >> 3.1
# 3.1
# '#'号选项：
# 可将其放在符号说明符和宽度之间（如果指定了这两种设置）这个选项将触发另一种转换方式，转换细节随类型而异。例如，对于二进制、
# 八进制和十六进制转换，将加上一个前缀
print("{:b}".format(42))
# >>101010
print("{:#b}".format(42))
# >>0b101010
# 对于各种十进制数，它要求必须保留小数点(对于类型g,它保留小数点后面的零)
print("{:g}".format(42))
# >>42
print("{:#g}".format(42))
# >>42.0000
# 字符串格式设置示例：
# 根据指定的宽度打印格式良好的价格列表：
'''
width = int(input('Please input the width: '))

price_width = 20
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width,price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width,price_width)

print('='*width)
print(header_fmt.format('Item','Price'))
print('-'*width)

print(fmt.format('iphone 11 pro',9999))
print(fmt.format('Huawei p40',6999))
print(fmt.format('mi 10(4G + 168G)',3999))
print(fmt.format('Google G13',4999))

print('='*width)
'''

# 字符串方法：
# 字符串方法比列表要多得多，因为很多方法都是从string那里继承过来的。
# 字符串的方法太多，这里只介绍比较重要的，完整的参考附录B
# 虽然字符串方法比sting的方法流行的多，但是string包含字符串方法里没有的一些函数
# 下面就是几个模块string里很有用的几个常量:
'''
1.string.digits:包含数字0--9的字符串
2.string.ascii_letters:包含所有ACSCII字母（大写和小写）的字符串
3.string.ascii_lowercase:包含所有ACSCII小写字母的字符串
4.string.printable:包含所有可打印的ASCII字符的字符串
5.string.punctuation:包含所有ASCII标点字符的字符串
6.string.ascii_uppercase:包含所有ASCII大写字母的字符串
'''
# 1.center
# 方法center实现在字符串两边填充字符（默认为空格），使字符串居中：
print("Hello world!".center(39))
# >>              Hello world!
print("Hello world!".center(39,'*'))
# >>**************Hello world!*************

# 2.find
# 方法find查找字符串中的指定的子串，如果找到返回子串的首字母的索引；如果没找到返回-1
print('With a moo-moo here, and a moo-moo there'.find('moo'))
# >>7
title = "Monty Python's Flying Circus"
print(title.find('Monty'))
# >>0
print(title.find('Python'))
# >>-1
# 在第二章的检查成员资格中，我们介绍了垃圾邮件过滤器检查邮件是否包含字符串"$$$"
# 这种检查也可以使用find来执行（in只能用于检查单个字母是否存在与字符串中）
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$'))
# >>0
# 字符串方法find返回的并不是布尔值，而是查找到的子串的首字母的索引，如果find返回0则说明它在字符串
# 的开头找到了子串
# 你还可以指定搜索的起点和终点：
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$',1))                    # 指定搜索的起点
# >>20
print(subject.find('!!!',0,6))                  # 指定起点和终点
# >>-1
# 需要注意的是：起点和终点的搜索范围包括起点，但不包含终点

# 3.join
# join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素
'''
错误用法：
seq = [1, 2, 3, 4, 5]
sep = '+'
seq.join(sep)       # 尝试合并一个数字列表
AttributeError: 'list' object has no attribute 'join'
'''
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))
# >>1+2+3+4+5
dirs = '','user','bin','env'
print('/'.join(dirs))
# >>/user/bin/env
print('C:' + '\\'.join(dirs))
# >>C:\user\bin\env
# 所有合并的元素都必须是字符串

# 4.lower
# 方法lower返回字符串的小写版本
print("JETBRAINS".lower())
# >>jetbrains
# 检查列表中的元素大写和小写是区分的：
if 'Gumby' in ['gumby', 'smith', 'jones']:
    print("Found it!")
else:
    print("It is not here!")
# >>It is not here!
# 如果要实现用户输入不区分大小写，lower就很有用：
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower() in names:
    print("Find it!")
else:
    print("It is not here!")
# >>Find it!
'''
与字符串的lower功能相关的是title,它将字符串转换为首字符大写，也就是所有单词的首字母大写
其他字母都小写：
"that is all, forks".title()
>>"That Is All, Forks"
另一种方法是使用模块string中的capwords
import string
string.capwords("That is all, forks")
>>"THAT Is ALL, FORKs"
'''
# 5.replace
# 方法replace用于将字符串中的子串替换为另一个子串并返回替换后的结果：
print('This is my program'.replace('my','your'))
# >>This is your program

# 6.slipt
# slipt是一个非常重要的字符串方法，其作用与join相反，用于将字符串拆分为序列
print('1+2+3+4+5'.split('+'))
# >>['1', '2', '3', '4', '5']
print('This is my program'.split())
# >>['This', 'is', 'my', 'program']

# 7.strip
# 方法strip用于将字符串的开头和结尾的空白删除，不包括字符串之间的空白：
print(' internal whitespace is kept '.strip())
# >>internal whitespace is kept

# 8.translate
# translate与replace一样用于替换字符串的特定部分，不同的是它只进行单字符替换，
# 这种方法的优势在于可以同时替换多个字符
# 在使用translate之前必须创建一个转换表，这个转换表指出不同的Unicode码之间的关系转换
# 要创建转换表，可对字符串类型str调用方法maketrans,这种方法接收两个参数：两个长度相同的字符串
# 它们指定将第一个字符串中的每个字符都替换为第二个字符串中的字符，代码类似这样：
table = str.maketrans('cs','kz')
# 如果需要查看转换表中的内容，你看到的只是Unicode码之间的映射：
print(table)
# >>{99: 107, 115: 122}
# 创建转换表后，可以将其用作方法translate的参数：
print('This is a copy test'.translate(table))
# >>Thiz iz a kopy tezt
# 在调用maketrans是还可以定义第三个参数，由于删除某个特定的字符，例如我要将所有空格删除：
table = str.maketrans('cs','kz',' ')
print('This is a copy test'.translate(table))
# >>Thizizakopytezt

'''
小结：
本章介绍了字符串的两个重要方面：
1.字符串的格式设置：
求模运算符（%）用于将值合并为包含转换标志（如%s）的字符串，这让你能够用很多方式来设置值得格式
如左对齐和右对齐，指定字段得宽度和精度，添加符号以及在左边填充0等等
2.字符串方法：字符串有很多的方法，有些经常用到（如split和join），有些很少用到(如istitle和capitalize)

本章介绍得新函数：
string.capwords([s,sep])                使用split根据sep进行拆分s,将每一项得首字母大写，并且用空格分隔符进行分隔
ascii(obj)                              将对象用ASCII表示
'''




























