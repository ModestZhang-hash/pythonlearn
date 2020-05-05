# structure
# a simple code block to calculate the fibonacci

fibonacci = [0, 1]
for i in range(8):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print(fibonacci)

# >>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''# you also can improve the code like this:
fibonacci = [0, 1]
num = int(input("Please input the range of the fibonacci you want to show: "))
for i in range(num - 2):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])
print(fibonacci)
# you know, we can't call this code block frequently,coder don't like writing the same codes
# in a program, so it is a easy way to use self-defining functions to package this code block
# to make our code readable and elegant
'''


# Now let's try to write a simple code: a 'hello, ' program with self-defining function

def hello(name):
    print(f"Hello, {name}!")


print("Start: ")
hello("John Smith")
print("another person: ")
hello("Sam Wen")
'''
When you run this code block, you will get output like this:
Start:
John Smith
another person:
Sam Wen
'''

# just want to know whether an object can be called, you can use a function named callable


import math
y = math.sqrt
print(callable(y))
# the output is True

# Now let's try to write a function to package the code block of fibonacci


def fibon():
    fibonacci = [0, 1]
    for i in range(8):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    print(fibonacci)
    return

fibon()
# we used def function() to package the code block of fibonacci and output the result
# after defining the fibon() what we should do is just call it


# We know that we can use # to note our code to make it more readable,here we can use a
# note to specify the functions
# it's named "docstring",a string after the 'def function()' to specify the function
# like this:

def square(x):
    """a function to calculate the square of number x"""    # the docstring of function square()
    return x * x

# now you can access the docstring like this:

print(square.__doc__)

# and this is the output: a function to calculate the square of number x

# Most languages'the functions have their return value, if a function has no return value, they won't call
# it a real function.But in Python, you can get a function without return value.Strictly speaking,
# it return None.in this function, return may have a effect to pause the function to go on:


def greet():
    print("Hello, I'm John Smith.")
    return
    print("Hello John, I'm Sam.")       # actually the Pycharm will give you a tip 'This code is unreachable'

greet()


# Let's run it and see what will output:
# 'Hello, I'm John Smith.' this is the output.Why can be this?
# Because when we add 'return' after print("Hello, I'm John Smith.") in function greet()
# Python won't run the part after the 'return'
# it seems like return pauses the function without any return value
# Actually, if we just write like this:

print(greet())

# you will see this output:
# Hello, I'm John Smith.
# None
# Where is the 'None' from? In fact the None is the return value of function greet()
# if we don't want to return anything in a function, we can just write 'return' and
# when we run it, it will run without return value(properly return None) and will pause when
# python see the 'return'


# This section we will discuss about the scope of a function variable
# Here we give a simple example to specify:

def name_change(n):
    n = "John Wike"
    return


name = "John Smith"
name_change(name)
print(name)             # What will be the output of this line?

# You may won't figure out that the output is: John Smith
# Why can be that? You may gass that it will be "John Wike" rather than "John Simth"
# it is bacause the  variable in function definition() is just formal argument
# and the n in funtion can only effect in the scope of name_change()
# and won't make sense with out of the function
# In fact the code block runs like this :
'''
name = "John Smith"
n = name
output name
n = "John Wike"
>>"John Smith"
'''
# This is because you assignment a variable in function defining won't have any effect on the variable out of
# the function


# As we all know, the value of the string, numbers and tuple is immutable
# this means that you can't change the value of them when them are formal arguments in functions
# But if we use a changeable structure such as list as formal arguments in function
# what can we do?
# Here is a example:

def name_change2(n):
    n[0] = "John Wike"
    return


name = ["John Smith", "Sam Wen"]
name_change2(name)
print(name)

# So what would be the output if I run this code block?
# In fact, the result is '['John Wike', 'Sam Wen']'
# in this function, Python changed the argument of the function
# but this example is very different from the prior example
# in the prior example, we made assignment with the local variable in function name_change()
# but in this example, we made assignment with the external variable related a list
# Is it strange? In fact it is not. May be you can rewrite the example without function:

name = ["John Smith", "Sam Wen"]
n = name
n[0] = "John Wike"
print(name)         # In fact the output is '['John Wike', 'Sam Wen']'

# Do you understand? When a list is assigned to two variables, they will
# point to the same list
# if you want to void this, you have to make a copy of the list
# when using the section operation to a list, we also return the copy of the list
# so if you want the section of whole list, what you get is just the copy of the list:

name = ["John Smith", "Sam Wen"]
n = name[:]
print(n == name)        # True
print(n is name)        # False

# as you can see, n equals to name but is not name.
# now if we change the value of n, it won't change the value of name:

n[0] = "John Wike"
print(n)                # ["John Wike", "Sam Wen"]
print(name)             # ["John Smith", "Sam Wen"]

# now let's combine the two method to make the code elegant:

name_change2(name[:])
print(name)             # '['John Smith', 'Sam Wen']'actually it doesn't matter

# You should know that the variable n is assigned with the copy of the list
# so what we do to the variable n is not matter with the original list

# You may doubt about whether the local variable in functions would effect the
# external variable out of the function.The answer is : No.
# in fact the scope of the local variable in functions is confined into the functions
# it won't make any difference out of the functions


# To improve the readability of our codes, we always would change the formal of the data structure
# such as dictionary and list. Here is a simple example to explain this :

find_person = {
    'first_name': {},
    'middle_name': {},
    'last_name': {}
}

'''
As you can see, I just creat a dictionary named 'find_person', in fact there are many mathod to 
creat a dictionary like this :

find_person = {}
find_person['first_name'] = {}
find_person['middle_name'] = {}
find_person['last_name'] = {}

it also works
'''
# Actually the 'find_person' is not simple dictionary you know, in the dictionary 'find_person'
# we creat three dictionary name'first', 'middle' and 'last', they are the dictionaries of a dictionary
# now if we want to put the name of the author into the dictionary named 'find_person'
# we can just do like this:

me = 'Magnus Lie Hetland'
find_person['first_name']['Magnus'] = [me]
find_person['middle_name']['Lie'] = [me]
find_person['last_name']['Hetland'] = [me]

'''
in fact It doesn't only put the first name, it puts the whole name me as the single entry of a list 
in fact you can use this formal to assign the dictionary:

me = 'Magnus Lie Hetland'
tree_num = me.split()
find_person['first_name'] = tree_num[0]
find_person['middle_name'] = tree_num[1]
find_person['last_name'] = tree_num[2]
print(find_person['middle_name'])
'''

# in this way you can't use 'print(find_person['middle_name']['Lie'])' to find person with
# middle name 'Lie'.

# now if you want the person whose middle name is 'Lie', you can do this :

print(find_person['middle_name']['Lie'])

# Now if we need to append our sister's name into the dictionary, what we should do is

my_sister = 'Anne Lie Hetland'
find_person['first_name'].setdefault('Anne', []).append(my_sister)
find_person['middle_name'].setdefault('Lie', []).append(my_sister)
find_person['last_name'].setdefault('Hetland', []).append(my_sister)

# Now if we want to find the person with first_name 'Anne', we can do this :

print(find_person['first_name']['Anne'])
# ['Anne Lie Hetland']

# if we want to find the person with middle_name 'Lie', we can do this :

print(find_person['middle_name']['Lie'])
# ['Magnus Lie Hetland', 'Anne Lie Hetland']

# As you can see, it is too hulk to read, what we want to do is to make the codes elegant and readable

# so we can use a function, now we creat a init_data structure function:


def init_data(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

# this way just package the init_data code block into a function, you can use this function like this:


find_person2 = {}
init_data(find_person2)
print(find_person2)

# the output is {'first': {}, 'middle': {}, 'last': {}}
# in this way we make the code elegant and readable

# Now if we want to package a function to receive person_name and a function to save person_name


def look_up(data, label, name):
    return data[label].get(name)

# this function receive a label(like 'middle') and name(like 'Lie'),then it can return a list of
# a person_name within label_name
# in other words, if you have saved the person_name, you can do like this:


print(look_up(find_person,'first_name', 'Anne'))            # ['Anne Lie Hetland']

# Now let's creat a function to save the person_name:


def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = look_up(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

# the function store make these steps to store the person_name:
# 1.put the arguments data and full_name into the function as the external values
# 2.Use split() to split the full_name to the list named 'names'
# 3.if the 'names' only has two strings, make the middle to the ''
# 4.store the 'first', 'middle', 'last' into the tuple 'labels'(also can list, in this case is just
#   omit the square markets)
# 5.use function zip to merge the label and name so as to do this next:
#   get the list of the label and name
#   append the full_name into the end of the list or insert it into the list

# now let's try to run this :


myname = {}
init_data(myname)
store(myname, 'Magnus Lie Hetland')
print(look_up(myname, 'middle', 'Lie'))

# ['Magnus Lie Hetland']

# now we can try many method:

store(myname, 'John Smith')
print(look_up(myname, 'first', 'John'))
store(myname, 'James Wen')
print(look_up(myname, 'last', 'Wen'))

# ['John Smith']
# ['James Wen']

# In some languages, we often have to assign the value of arguments and make effects out of the functions
# in Python you can't do this directly, only can change the value itself.
# But if the argument is immutable what should we do?
# In this case, you should return the values you need.(if not one, return as tuple formal)
# For example, you can define this function to make number plus-one:


def plus_one(x):
    return x + 1


x = 10
x = plus_one(x)
print(x)                # 11

# The arguments we mention above is all location arguments, in fact the location of the arguments is more
# important than the arguments. This section we will explore the omit-location arguments
# first of all, let's see these two function-definitions:


def hello_1(greeting, name):
    print(f"{greeting}, {name}!")


def hello_2(name, greeting):
    print(f"{name}, {greeting}!")


hello_1("Hello", "John Smith")                  # Hello, John Smith!
hello_2("Hello", "John Smith")                  # Hello, John Smith!

# In many times, we can't remember the order of the arguments,to simplify the work
# we can appoint the name of the arguments:

hello_1(greeting="Hello", name="John Smith")            # Hello, John Smith!

# Here the order of the arguments is not important:

hello_1(name="John Smith", greeting="Hello")            # Hello, John Smith!

# But the names of the arguments are more important:

hello_2(greeting="Hello", name="John Smith")            # John Smith, Hello!

# like this, using name specially appoints the argument, we call the arguments 'key-word argument'
# the key-word argument is benefit to understanding the effect of the argument
# what the biggest benefit of the key-word arguments is you can appoint the defaults of the arguments:


def hello_3(greeting="Hello", name="John Smith"):
    print(f"{greeting}, {name}!")


# if you appoint the defaults of the arguments like this, you won't need to assign the argus when u call it:

hello_3()                                                  # Hello, John Smith!
hello_3("Greetings")                                       # Greetings, John Smith!
hello_3("Greetings", "Universe")                           # Greetings, Universe!

# As you can see, when you want to call it, just use location arguments
# but when you want to assign the 'name'. u should assign the argument 'greeting' first.
# if u want to assign the argument 'name' and the assign argument 'greeting' a default value
# you would do like this:

hello_3(name="Universe")                                # Hello, Universe!

# Wonderful, isn't it?
# In fact you even can combine the location and key-word arguments (although we don't suggest that)
# On condition that you have to appoint the location arguments first, or the interpreter
# can't understand which argument should be assigned with value.
# For example, when you call function hello_4 you must assign the value to the argument 'name'
# but the argus 'greeting' and 'punctuation' is alternative:


def hello_4(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

# There are many ways to call the functions, such as:


hello_4("John Smith")                       # Hello, John Smith!
hello_4("John Smith", "Howdy")              # Howdy, John Smith!
hello_4("John Smith", "Howdy", "...")       # Howdy, John Smith...
hello_4("John Smith", punctuation = ".")    # Hello, John Smith.

# sometimes is very useful to provide arguments more than one.
# In this case we don't want to provide only one argument in one time
# what we want seems like this:
'''
store(data, name1, name2, name3)
'''
# therefore, we should allow user to provide more than one argus to the function
# before do this, let's see a function:


def print_params(*params):
    print(params)

# now let's try to call the function using argument:


print_params("Testing")                                 # ('Testing',)

# noticed that the output is a tuple because of the comma(,)
# now let's try to call it like this:


print_params(1, 2, 3)                                   # (1, 2, 3)

# the star market(*) means to collect the rest of arguments into a tuple
# now let's try to define this function:


def print_params_2(title, *params):
    print(title)
    print(*params)

# now let's try to call it:


print_params_2("Params:", 1, 2, 3)

# and this is the output:
# Params:
# 1 2 3
# so the star market(*) means to collect the rest of the arguments
# if there is no argument for it to collect, it will return an empty tuple:


print_params_2("Nothing:")                  # Nothing to output

# Just like assignment, we can put the star market(*) in other location(of cause not the last)
# but what you have to do is appointing the argus after the *argument
# for example like this :


def in_the_middle(x, *y, z):
    print(x, *y, z)

# now let's try to call it:


in_the_middle(1, 2, 3, 4, 5, z=7)                 # 1 2 3 4 5 7
#             ^ (           )^
#             x,      *y,    z
# of cause the output means: 1 (2 3 4 5) 7
'''
But if you don't appoint the arguments after the *argument, the interpreter will report error:

in_the_middle(1, 2, 3, 4, 5, 7)

Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
TypeError: in_the_middle() missing 1 required keyword-only argument: 'z' 

the other notice is: the *argus can't collect the key-word arguments:
 
print_params_2("Params", something=42)

Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
TypeError: print_params_2() got an unexpected keyword argument 'something' 
'''
# if you want to collect the key-word arguments, you can try this:


def print_params_3(**params):
    print(params)


print_params_3(x=1, y=2, z=3)                       # {'x': 1, 'y': 2, 'z': 3}

# as you can see, when you use the **argus to collect the key-word argus
# it will return a dictionary rather than a tuple
# You can also combine these two method in one function:


def print_param_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)

# the effect of calling it is like this:


print_param_4(1, 2, 3, 4, 5, 6, 7, foo=1, bar=2)
#             ^  ^  ^ (          ){   : ,    : }
#             x  y  z     *pospar   **keypar
# as you can see the output is :
# 1 2 3
# (4, 5, 6, 7)
# {'foo': 1, 'bar': 2}

# Now back to the question of find_person with name
# a solution is like this:


def store_2(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = "first", "middle", "last"
        for label, name in zip(labels, names):
            people = look_up(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

# now you can call this function like this:


d = {}
init_data(d)
store_2(d, "John Smith", "Ben Wek")
print(look_up(d, "last", "Smith"))                      # ['John Smith']


# We talk about the * and ** to collect the argus into the tuple and dictionary,
# in fact we can use the two star markets to do the reverse operations
# now let's see this function:


def add(x, y):
    return x + y

# at the same you have a tuple of the numbers which will be added together:


params = (1, 2)

# this operation seems like contrary to collecting the argus
# it seems like allot the argus, by using * when call this function:


print(add(*params))                 # 3

# this method can make to the section of argus, also is the end of the argus list,
# by using the **, you can allot the values of the dictionary to the key-word arguments
# if you have created the function hello_3, now you can do this:


params = {'name': "John Smith", 'greeting': "Hello"}
hello_3(**params)                   # Hello, John Smith!

# if you use the * or ** both when you define functions and call functions,
# the interpreter will only transmit the tuple or dictionary
# so it's too bother to do that(just like this):


def with_star(**inf):
    print(f"{inf['name']} is {inf['age']} years old.")


def without_star(inf):
    print(f"{inf['name']} is {inf['age']} years old.")


information = {'name': "John Smith", 'age': "20"}
with_star(**information)
# John Smith is 20 years old.
without_star(information)
# John Smith is 20 years old.

# As you can see, the function with ** and function without star have the same effect in this code
# so only using the *(or **) when you define the functions or call the functions can have effect of star markets

'''
Using split operator to transmit the argus is useful, because using this you wouldn't worry about the
number of the argus which would cause the problem.just like this:

def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)
    
def call_foo(*args, **keywords):
    print("Calling foo!")
    foo(*args,, **keywords)
    
this is useful in calling super-class structure function
'''


# After learning many methods for functions arguments, let's see this example of combining the
# methods in functions:


def story(**keywords):
    return "Once upon a time, there was a {job} called {name}".format_map(keywords)

def power(x, y, *others):
    if others:
        print("Received redundant parameter:",others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    "Imitate range() for step >0"
    if stop is None:                                # if not appoint the value of stop
        start, stop = 0, start                      # adjust the value of start and stop
    result = []

    i = start                       # upper cont the start
    while i < stop:                 # cont to the stop
        result.append(i)            # append the current number to the end of the result
        i += step
    return result

# now let's try to call these functions:


print(story(job = 'King', name = 'Gumby'))            # Once upon a time, there was a King called Gumby
print(story(name = 'Sir Robin', job = 'brave knight'))# Once upon a time, there was a brave knight called Sir Robin
params = {'job': 'language', 'name': 'Python'}
print(story(**params)) # Once upon a time, there was a language called Python
del params['job']
print(story(job = 'stroke of genius', **params))# Once upon a time, there was a stroke of genius called Python
print(power(2, 3))                  # 8
print(power(3, 2))                  # 9
print(power(y = 3, x = 2))          # 8

params = (5,) * 2                   # 3125
print(power(*params))
print(power(3, 3, "Hello world"))   # Received redundant parameter: ('Hello world',)

print(interval(10))                 # 27
print(interval(1, 5))               # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(interval(3, 12, 4))           # [1, 2, 3, 4]

print(power(*interval(3, 7)))
# [3, 7, 11]
# Received redundant parameter: (5, 6)
# 81









































