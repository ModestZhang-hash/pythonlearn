# 本章将介绍可通过名称来访问其各个值得数据数据结构
# 这种数据结构成为映射，字典是python中唯一内置的映射数据类型
# 其中的值不按顺序排列，而是储存在键下。键可能是数，字符串和元组中

# 字典的用途
# 字典旨在能够让你轻松的通过特定的单词（键），来找到其定义（值）
# 有时候使用字典比使用列表更合适，以下是字典在python中的一些用途：
"""
1.表示棋盘的状态，其中每一个键都是由坐标组成的元组
2.储存文件修改时间，其中键为文件名；
3.数字电话/地址本
"""
# 假设有如下名单：
name = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
# 如果要创建一个小型数据库，用于存放这些用户得电话号码，该如何办呢
# 一种方法是另外创建一个列表，用于存放四位号码：
numbers = ['2341', '9102', '3158', '0142', '5551']
# 创建完这些列表之后，我们将可以像下面这样查找Cecil的电话号码：
print(numbers[name.index('Cecil')])
# >>3158
# 这样可行，但并不实用，实际上你希望像下面这样做：
# phonebook['Cecil']
# >>3158
# 实现这样需要我们构建一个phonebook字典

# 创建和使用字典
# 字典以类似下面这样的方式表示:
phonebook = {'Alice':'2341', 'Beth':'9102', 'Cecil':'3158', 'Dee-Dee':'0142', 'Earl':'5551'}
# 字典有键和其对应的值组成，这种键值对称为项（item），在上面的示例中，键为用户名字，值为号码
# 每一个键与值之间用:号隔开，项之间用逗号隔开，整个字典放在花括号里，空字典用两个花括号表示：{}
# 在字典（或其他映射数据类型）中，键必须是独一无二的，而值并非必须如此
# 1，函数dict
# 可以使用函数dict从其他映射类型（如其他字典）或键值对序列创建字典：
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
# >>{'name': 'Gumby', 'age': 42}
print(d['name'])
# >>Gumby
# 还可以使用关键字实参来调用这个函数，如下所示：
d = dict(name = 'Gumby', age = 42)
print(d)
# >>{'name': 'Gumby', 'age': 42}
# 基本的字典操作：
'''
1.len(d)返回字典d包含的项（键-值对）数
2.d[k]返回与键k相关联的值
3.d[k] = v将值v关联到键k
4.del d[k]删除键为k的项
5.k in d检查字典d是否包含键为k的项
'''
# 虽然字典与列表有很多相似之处，但它们也有一些不同点：
'''
1.键的类型：字典中的键可以是整数，但并非必须是整数。可以是任意不变的类型，如浮点数（实数），字符串或元组
2.自动添加：即便是字典原本没有的键，也可以给它赋值，这将在字典中创建新的项。
            然而如果不使用append给列表添加新的项，就不能给列表中没有的元素赋值
3.成员资格：表达式k in d(其中d是一个字典)查找的是键而不是值，
            而表达式v in l(其中l是一个列表)查找的是值而不是索引
'''
# 相比于检查列表是否包含指定值，检查字典是否包含指定键的效率更高，数据结构越大，差距就越大
# 前述的第一点是字典的主要优点，第二点也很重要，有示例说明：
# x = []
# x[42] = 'Foobar'          将Foobar赋给一个空列表中索引为42的元素，显然不可能，因为并没有这样的元素
x = {}
x[42] = 'Foobar'            # 将Foobar赋给一个空字典的键是可行的，字典中有了新的项
print(x[42])
# >>Foobar
print(x)
# >>{42: 'Foobar'}

# 字典示例：
'''
# 一个简单的数据库
# 将人名用作字典的键，键中分别包含'phone'和'addr',它们分别于电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
# 电话号码和地址的描述性标签，供打印时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')

# 要查找电话号码还是地址
request = input('Phone number(p) or address(a)?')

# 使用正确的键
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

# 仅当名字是字典包含的键时才打印信息
if name in people:
    print("{}'s {} is {}".format(name, labels[key],people[name][key]))
# 运行结果类似下面这样：
# Name: Beth 
# Phone number (p) or address (a)? p 
# Beth's phone number is 9102.
'''
# 将字符串格式设置功能用于字典
# 有些情况下，通过在字典中储存一系列命名的值，可让格式设置更容易些
# 可在字典中包含各种信息，这样只需要在格式字符串中提取所需要的信息即可
# 为此必须使用format_map来指出你将通过一个映射来提供所需信息
print(phonebook)
# >>{'Alice': '2341', 'Beth': '9102', 'Cecil': '3158', 'Dee-Dee': '0142', 'Earl': '5551'}
print('The phone of Cecil is {Cecil}'.format_map(phonebook))
# >>The phone of Cecil is 3158
# 像这样使用字典，可以指定任意数量的转换说明符，条件是所有的字段名都是包含在字典中的键，
# 在模板系统中，这种字符串设置方式很常见

# 字典方法
# 1.clear
# 方法clear用于删除所有的字典项，因为操作是就地执行的，所以没有返回值(或者说返回值为None)
d = {}
d['name'] = ['Gumby']
d['age'] = [42]
print(d)
# >>{'name': ['Gumby'], 'age': [42]}
print(d.clear())
# >>None
print(d)
# >>{}
# 有以下两个例子来进行比较：
'''
1.通过将空字典赋值给x，对y并没有影响，它依然指向原来的字典
x = {}
y = x
x['key'] = 'value'

print(y)
>>{'key': 'value'}

x = {}
print(x)
>>{}

x = {}
print(y)
>>{'key': 'value'}

2.要删除原来字典中的所有元素就必须使用clear,这样y也是空字典
x = {}
y = x
x['key'] = 'value'

print(y)
>>{'key': 'value'}

x.clear()
print(y)
>>{}
'''
# 2.copy
# 方法copy返回一个新字典，其中包含的键值对与原来的字典相同
# （这种方法执行的是浅复制，因为值本身是原件，而非副本）
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
# >>{'username': 'mlh', 'machines': ['foo', 'baz']}
print(x)
# >>{'username': 'admin', 'machines': ['foo', 'baz']}
# 当替换副本中的值时，原件不受影响，但是当修改附件的值时，原件的值会跟着一起被修改
# 因为原件指向的也是被修改的值
# 为了避免这种问题，可以使用深复制，同时复制值及其包含的所有值
# 为此，可以使用模块copy中的deepcopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
# >>{'names': ['Alfred', 'Bertrand', 'Clive']}
print(dc)
# >>{'names': ['Alfred', 'Bertrand']}
# 3.fromkeys
# 方法fromkeys创建一个新字典，其中包含指定的键，且每一个键都对应的值都是None
print({}.fromkeys(['name', 'age']))
# >>{'name': None, 'age': None}
# 如果你不想使用默认值None，可以使用特定值
print(dict.fromkeys(['name', 'age'],'Unknown'))
# >>{'name': 'Unknown', 'age': 'Unknown'}

# 4.get
# 方法get为访问字典中的项提供了比较宽松的环境，通常如果你访问字典中没有的项会报错：
'''
d = {}
print(d['name'])

>>Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
KeyError: 'name' 
'''
# 而使用get不会这样：
d = {}
print(d.get('name'))
# >>None
# 用get访问字典中不存在的项时不会报错，而是会返回None。你还可以指定默认值，使其返回的不是None而是别的值
print(d.get('name', 'N/A'))
# >>N/A
# 如果字典中包含指定的键，get作用和普通查找相同
d['name'] = {'Eric'}
print(d.get('name'))
# >>{'Eric'}

# 字典方法示例：
'''
一个使用get的简单数据库
在这里插入上一个示例的数据库（people）
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
# 电话号码和地址的描述性标签，供打印时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name: ')

# 要查找电话号码还是地址
request = input('Phone number(p) or address(a)?')

# 使用正确的键
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

# 使用get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key,'Not available') 

print("{}'s {} is {}".format(name, label, result))

下面是这个程序的运行情况，注意到get提高了灵活性，让程序在用户输入的值出乎意料时
也能妥善处理。
>>Name: Gumby 
Phone number (p) or address (a)? batting average 
Gumby's batting average is not available. 
'''

# 5.items
# items返回一个包含所有字典项的列表，其中每一个元素都为(key,value)的形式，字典的项在列表中的排列顺序不确定
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
d.items()
print(d.items())
# >>dict_items([('title', 'Python Web Site'), ('url', 'http://www.python.org'), ('spam', 0)])
# 返回值为一种名为字典视图的特殊类型，字典视图可用于迭代，你还可以确定其长度以及对其进行成员资格检查
it = d.items()
print(len(it))
# >>3
print(('spam', 0) in it)
# >>True
# 视图的一个优点是不复制，它们始终是底层字典的反映，即使你修改了底层字典也是如此
d['spam'] = 1
print(('spam', 0) in it)
# >>False
d['spam'] = 0
print(('spam', 0) in it)
# >>True
# 然而，如果你要将字典项复制到列表中，可自己动手做
print(list(d.items()))
# >>[('title', 'Python Web Site'), ('url', 'http://www.python.org'), ('spam', 0)]

# 6.keys
# 方法keys返回一个字典视图，其中包含指定字典的键

# 7.pop
# 方法pop可用于获取与指定键相关联的值，并将该键值对从字典中删除
d = {'x':1, 'y':2}
d.pop('x')
print(d)
# >>{'y': 2}

# 8.popitem
# 方法popitem类似于list.pop,但list.pop弹出列表中的最后一个元素，而popitem随机弹出一个字典项
# 因为字典项的顺序是不固定的，没有最后一个元素的概念
# 因此你可以用这个方法高效的删除或处理字典中的项
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
# >>('title', 'Python Web Site')
print(d)
# >>{'url': 'http://www.python.org', 'spam': 0}
# 虽然popitem类似于列表中的pop，但是字典中并没有于之append相对应的方法，这本身对字典来说是没有意义的

# 9.setdefault
# 方法setdefault类似于get,因为他也获取于指定键相关的值，但除此之外，setdefault允许在字典不包含指定项时
# 在字典中添加键值对
d = {}
d.setdefault('name','N/A')
print(d)
# >>{'name': 'N/A'}
d['name'] = 'Gumby'
print(d)
# >>{'name': 'Gumby'}
# 如你所见，当字典中不存在指定键时，字典返回指定值并更新字典；如果指定的键存在，就保持字典不变
# 如果没有指定，就返回None
d = {}
d.setdefault('name')
print(d)
# >>{'name': None}

# 10.update
# 方法update使用一个字典的项来更新另一个字典
d = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'changed': 'Mar 14 22:09:15 MET 2016'
    }
x = {'title': 'Python Language Website'}
d.update(x)
print(d)
# >>{'title': 'Python Language Website', 'url': 'http://www.python.org', 'changed': 'Mar 14 22:09:15 MET 2016'}
# 对于通过参数提供的字典，将其项添加到当前字典中，如果当前字典项包含相同的键，就替换它
# 可像调用本章前面讨论的函数dict（类型构造函数）那样调用方法update。这意味着调用
# update时，可向它提供一个映射、一个由键值对组成的序列（或其他可迭代对象）或关键字参数

# 11.value
# 方法value返回一个由字典值组成的字典视图，不同于方法key，方法value返回的视图可能包含重复的值
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print(d.values())
# >>dict_values([1, 2, 3, 1])

'''
本章小结：
本章主要介绍了如下内容：
1.映射：映射让你能够使用任何不可变的对象（最常用的就是字符串和元组）来标识其元素。
        python只有一种内置的映射类型，就是字典
2.将字符串功能格式用于字典：要对字典执行字符串格式操作，不能使用format格式和命名参数，而必须使用format_map
3.字典方法：字典有很多方法，这些方法的调用方式和列表与字符串的调用方式相同

本章介绍的新函数：
dict(seq)               从键值对，映射或关键字参数创建字典
'''













