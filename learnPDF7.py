# Talk about the struct again
# In above chapters, we learned main internal data structures
# (number, string, list, sequence and dictionary)
# have a rough idea of the internal functions and standard library(stdlib)
# and creat many self-defining functions. But there is a last point is
# creating self-defining object which we would talk about in this chapter.

print("Talk about the struct again.")

'''
You may ask about that how useful the self-defining object would be?
It seems cool, but what can we do with it?
you can use the number, string, list, sequence and dictionary
Can't we use them to creat functions to satisfy the need ? Of cause you can.
But it is core concept to creat self-defining object(specially object-type and class) in Python.
In fact it is so important that the languages like Python, Smalltalk, C++ and Java are 
regarded as ' Object-oriented languages '.
In this chapter, you will learn how to creat object, Polymorphism(多态), encapsulation(封装),
methods(方法), property(属性), inherit(继承).

Now let's begin.  
'''

# If you are similar to the 'object-oriented languages',
# you may know about the 'struct function', but we don't want to talk about it in this chapter

'''
Object-Magic

in object-oriented languages, the term 'object' means that the a series of data(property)
and a series of methods to access and operate these data.
There are many reasons to use object rather than function nor global variable.
now let's list the advantage to use object:

1.polymorphism: you can use do the same operate on different object. and the objects can 
                run normally
2.encapsulation: hide details about the process of object to the external
3.inherit: creat dedicated class according to the general class

for example, we can creat a e-pay system for a commodities-price web.
the program receive the shopping cart from a system, settle the account 
and finally deduct the cost from the account's credit card.  
'''

" 1.polymorphism: "
# it may means that even though you don't know what kind of object the variable points to,
# you still can operate it, and different operations with different kind object.

# Now let's see an example, if u want to create a commodities-price system.
# u may think you can use tuple to combine the commodities and their price like this:

'''
tuple = ('commodity', price)

such as: ('cookie', 2.50)
'''

# if you just want to enter the name of the commodity and its price, of cause you can
# do like this. But if you want to change the price of the commodity, it's not a good idea.
# think that a web add an auction service, which is low the price until a customer can buy it.
# In fact we want the customer can do like this:
# customer put the commodity into the shopping cart and into the settle web page
# wait for the price low to a proper position, then he can click the "pay it" button.

# However, using a simple tuple can't solve the problem. to do it,
# the object to show commodity must provide the current price in web when you ask to get the
# price of it. In other words , you can't change the price of the commodity if you use the
# tuple to do this. To solve it you can use a function:

"don't do like this: "
'''
def get_price(object):
    if isinstance(object, tuple):
        return object[1]
    else:
        return magic_network_method(object)
'''
# the code block used function isinstance(object, tuple) to check if object is tuple
# if true, run to the next object[1]; if false, call the magic_network_method(object)

# you may think to use the dictionary to do this, but it is too tedious to use it

# In fact if you think more, it is nothing but let the object to do with itself.
# We hope every new object can access or calculate its own price and return the value.
# and what you should do is just to ask them to get the value.
# this is what the polymorphism(actually also encapsulation) does matter.

"polymorphism and methods"
# you get a object, and you don't know how it can be created---in fact is one of
# many forms. What you have to do only is just ask its price and it is enough
# as for method to ask the price, you may know well.
'''
object.get_price()
>>2.5
'''
# like this, the function which is associate to the property of object is called 'method'
# you have met many function like this: many method of string, dictionary and list
'''
'abc'.count('a')
>>1
[1, 2, 'a'].count('a')
>>1
'''
print('abc'.count('a'))                 # 1
print([1, 2, 'a'].count('a'))           # 1


# if you have a variable and you can get to use its method 'count' without knowing
# what type it is: what you have to do is just to provide a character as a argument
# to a method, and then it can run.

# Now let's try to do this:
# the stdlib module 'random' includes a function 'choice', it can get a element from a
# sequence. now let's to use this function to provide a value to a variable:

from random import choice
x = choice(['Hello world', [1, 2, 'e', 'e', 4]])

# using this code, the variable x may includes the string 'Hello world' or
# list[1, 2, 'e', 'e', 4]. specifically which one, we don't know and don't care.
# what you should care is only how many 'e' in variable x, no matter what it is
# string or a list you can find the answer. To do it, you can call 'count':

print(x.count('e'))         # 2

# from the answer you can see the x includes a list.
# but the key is you won't have to check it, only the x have a method named 'count'
# ,and it can use a character as a parameter and return a number.
# if someone can creat an object including this method. you can use the object the same
# as the sequence and list.

"There are many forms in polymorphism"
# every time you can operate an object which you don't know its type,
# the polymorphism does work. it not only suit to method, but also
# many internal operator and function. look at this :

print(1 + 2)                        # 3
print('airplane' + 'license')           # airplanelicense

# this code block just say: the operator(+) and use in numbers or strings
# if you want to creat a 'add' function. you can define it like this :

def add(x, y):
    return x + y

# after this you can use function add() to combine different type variable:

print(add(1, 2))
print(add('airplane','license'))

# it seems simple, but it supports all the object which can add together.
# if we want to creat a function which can print a information to point out
# its length. you can do like this(only want length, we can use function 'len'):

def length(x):
     print(f"the length of {repr(x)} is {len(x)}")

# as you can see, the definition uses a function named 'repr'
# the 'repr' is the collection of the polymorphism, can be used on all objects
# look at this:


length('Fnord')                # the length of 'Fnord' is 6
length([1, 2, 3])               # the length of [1, 2, 3] is 3

# in fact many functions and methods are polymorphism, of cause
# many functions you define yourself even though you are not deliberately.

"2.encapsulation"
# the encapsulation means that hide many not necessary details to external.
# it seems like polymorphism(we needn't to know the details internal)
# they are similar as both of them are roles of structure.
# but the encapsulation are different from the polymorphism
# the polymorphism allows us to call object without knowing what type of the object is
# but the encapsulation allow us to call object without knowing what construction it is

# now let's see an example using polymorphism without encapsulation
# assume that you have a class named 'OpenObject'(we will talk about how to creat class):
'''
class OpenObject():             # this is how to creat class "OpenObject"
    pass


o = OpenObject()                # this is how to creat object
o.set_name("Sir Lancelot")
o.get_name()

>>Sir Lancelot
'''

# You (call the class like call the function) creat an object, and
# associate to the variable named o
# then you can use the methods named 'set_name' and 'get_name'
# all seems like wonderful. However, what will happen if o puts the name
# into the global variable named "global_name"?

'''
global_name

>>"Sir Lancelot"
'''
# this means that when you use the example of class OpenObject,
# you have to think about the content of the "global_name"
# in fact, you should make sure no one can change it
'''
global_name = "Sir Gumby"
o.get_name
>>Sir Gumby
'''
# if you try to creat more than one OpenObject objects
# it may cause the problem
# because they use the same variable:
'''
o1 = OpenObject()
02 = OpenObject()
o1.set_name("Robin hood")
o2.get_name()

>>"Robin hood" 
'''
# as you can see, when you set the name of the o1, you get the name of the o2 at the same time
# this is not the result you want
# how can we encapsulation the name into the object?
# we can regard the name as a property
# property is like a variable belongs to the object. Just like method
# in fact, the method is like the property associate to the function
# if you write the class using property rather than global variable
# and rename it with 'ClosedObject', you can use it like it:

'''
c = ClosedObject()
c.set_name('Sir Lancelot')
c.get_name()

>>'Sit Lancelot'
'''
# it goes well. but it can't prove that name is not storage in the global variable
# now let's creat a object:
'''
r = ClosedObject()
r.set_name('Sir Robin')
r.get_name()

>>'Sir Robin'
'''
# we created a new name of the object, now let's see the name of the previous object
'''
c.get_name()

>>'Sir Lancelot'
'''
# the name is still here! Because the object has its own state.
# the state of object is described by property
# the method of the object may change the property of it.
# and assign some authority of accessing the variable(property)

"3.inherit"
# the inherit is other method. the programmer always avoid to write the same codes.
# we told about to creat function to solve this. But now we have to think another
# question. when we creat a class, and you want to creat another similar class
# (maybe just add some new method), how can we do this ?
# when you creat the new class, you don't want to copy the old code
# and paste it in the new class

"4.class"

"what hell is the class"
# this is the definition of the class --- an object
# any object belongs to a class, and call them "living example"
# if an object of one class is the subset of the object of another class
# the pre class is the subclass of the after class
# so the skylark is the subclass of the birds, the birds is the superclass of the skylark

# through this, you can understand the subclass and the superclass
# in the Object Oriented Programming, the relationship of them have many to say
# as the class is defined by the methods it supports
# all the 'living example'(object) of the class have all the methods of this class
# so all the 'living example'(object) of the subclass have all the methods of the superclass
# so if you want to define a subclass(after you created a superclass)
# you just have to define the extra methods(also you can rewrite the methods you have defined)

# for example, the class of the 'Bird' can provide method 'fly'
# and the 'Penguin'(one subclass of the 'Bird') may creat a new method 'eat_fish'
# when you define the subclass 'Penguin', you may want to
# rewrite the methods of the superclass('fly')
# because the penguin can't fly, the method 'fly' of the 'Penguin'
# should do nothing or crash

"creat self-defining class"

# now let's see an example:


class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(f"Hello World! I'm {self.name}")

# this example has three definition of methods, they looks like
# the definition of the functions, but in the code block of class
# the "Person" is the name of the class
# the class has its own definition space to define its own function in it
# all looks well, you may want to know what hell is the argument 'self'
# it points to the object, then which object?
# now use some example to prove it:

foo = Person()
bar = Person()
foo.set_name("Luker skywalker")
bar.set_name("Anake skywalker")
foo.greet()                                     # Hello World! I'm Luker skywalker
bar.greet()                                     # Hello World! I'm Anake skywalker

# this example may looks simple, but it can prove what is the 'self'
# when 'foo'(class) calls the set_name(method) and greet(method),
# 'foo' will be transmitted to them(method) as the argument
# we named the argument 'self'
# in fact, we can name the argument randomly
# as it always points to the object itself, we called it 'self'

# obviously, the 'self' is useful, if we don't have it,
# all the methods can't access to the object itself ---- the object
# which all the properties belong to
# as usual, you can also access these properties externally

print(foo.name)                 # Luker skywalker
print(bar.name)                 # Anake skywalker
bar.name = "Yoda"
bar.greet()                     # Hello World! I'm Yoda


'''
if the 'foo' is a living example of the 'Person',
you can regard the foo.greet() as the shorthand(缩写) of the Person.greet(foo)
but the after formal has lower polymorphism
'''

"Property, function and method"

# in fact, the difference between method and function is in the argument 'self'
# method(actually the method associated) associate its first argument to the
# living example(object). and you won't have to provide the argument again
# out doubt you can associate the property to the function
# but there won't be an argument 'self'

class Class:
    def method(self):
        print('I have a self!')


def function():
        print("I don't ....")


instance = Class()
instance.method()                       # I have a self!
instance.method = function
instance.method()                       # I don't ....

# you should notice that whether there is argument 'self' not depend on
# the whether using the way (such as instance.method) to call method
# in fact, you can let another variable points to the same method:

class Bird:
    song = "Sqk"
    def sing(self):
        print(self.song)


bird = Bird()
bird.sing()                             # Sqk
bird_song = bird.sing
bird_song()                             # Sqk

# although the last method calling like the function calling
# but the variable 'bird_song' points to the associated method 'bird.sing'
# this means that it can access the argument 'self'
# (it is associated to the living example(object))

"talk about the hide again"

# in the default, you can access the property of the object externally
# now let's see the example of encapsulation again:
'''
c.name
>>'Sir Lancelot'
c.name = 'Sir Gumby'
c.get_name()
>>'Sir Gumby'
'''
# some programmer think this is no problem
# but other programmer don't think so and think this method may
# violate the principle of encapsulation
# you may think why we should hide the property of the object
# after all, if you can strictly access the property of the
# 'ClosedObject'(the class belongs to the property) 'name'
# we don't need to creat the method set_name and get_name

# the point is programmer can't know the situation of the internal of the object
# for example, the ClosedObject can send message to the manager when
# object change it own name. this function include in the method set_name
# but if you strictly set the c.name, what will happen? nothing will happen
# it won't send message
# to avoid this problem, we can make the property private
# we can't access the private attribute(property) external
# only use accessor to do it(like get_name and set_name)
# we will talk about the property(特性), it is a good alternative of the accessor
# Python don't have the strict support to the private property
# it only let the programmer to know when they can change the property from external
# after all, only you can use it when you know how to use object
# however we can use some trick to attain the affect of the private property

# to make the method or property private(can't access externally),
# we can let their names begin with "__":

class Secretive:

    def __inaccessible(self):
        print("Bet you can't see me...")


    def accessible(self):
        print("The secret message is: ")
        self.__inaccessible()


# now you can't access the __inaccessible external
# but you still can access it from class ( "accessible" )
'''
s = Secretive()
s.__inaccessible()

you will get error like this:
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
AttributeError: Secretive instance has no attribute '__inaccessible' 
'''
s = Secretive()
s.accessible()

# The secret message is:
# Bet you can't see me...

# it may looks strange, but this method looks like the method in other languages
# however the method backstage not looks standard:
# in the definition of the class, convert all the name begin with __
# that is begin with _and name of class
'''
Secretive._Secretive__inaccessible()
'''
# if you know the backstage method, you can access the private property from external
# but we don't advice you to do this:

s._Secretive__inaccessible()
# Bet you can't see me...

# all in all, you can't stop other person to access the private property from external
# but this change of name will make strong signal to warning them don't do this


# if you don't want the name to be changed, and want
# signal that "don't change the private property or method from external"
# you can use a _ begin with, although it is an appoint, but have effect


"The scope of the class"
# these two statements below seems equal:
'''
def foo(x): return x * x
foo = lambda x: x * x
'''
# they both creat a function which returns square of a number x
# and associate the function to the variable foo
# you can define 'foo' in the global scope, also you can define in the function or method
# the definition of the class is similar too:
# the definition of class is in the special definition-scope(class definition-scope)
# and all the members of class can access the scope
# the definition of class is a code block which would be run
# not all Python programmers know about this
# but knowing this is helpful
# in the definition of class, not only include def statement:
'''
class C:
    print("Class C being defined...")
 .
 .
 .
class C
'''
# it seems not smart, let's see this code block:

class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)            # 1

m2 = MemberCounter()
m2.init()
print(MemberCounter.members)            # 2

# code block above defined a variable in the class scope
# all the living example(object) can access it
# in this it is used to count the number of members
# every object can access the variable in this class scope like method

print(m1.members)                       # 2
print(m2.members)                       # 2

# if you use an object to assign value to the property 'memeber'
# what will happen?

m1.members = "Two"
print(m1.members)                       # Two
print(m2.members)                       # 2

# the new value is assigned in the porperty of m1
# this property covered the variable of class
# it seems like the relationship between global variable and local variable


"specified superclass"
# we have told about the subclass and superclass
# to specified superclass,
# you can add the ( superclass name ) after class-name in class statement


class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):      # the SPAMFilter is the subclass of the Filter
    def init(self):            # rewrite the method 'init' in the superclass 'Filter'
        self.blocked = ['SPAM']

# the Filter is a filtration sequence of general class
# in fact the Filter filters nothing

f = Filter()
f.init()
print(f.filter([1, 2, 3]))              # [1, 2, 3]

# the usage of class 'Filter' is to be a base-class(superclass) of other classes

s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
# ['eggs', 'bacon']

# Please notice the two points in the definition of the class SPAMFilter:
# 1. rewrite the definition of method 'init' in Filter by providing a new definition
# 2. strictly inherit definition of method 'filter' from class 'Filter', so
#    we needn't rewrite the definition of it

# the second point specified the reason why the inherit is useful:
# we can creat many filter class
# they are all derived from the class 'Filter', and they can all use the method 'filter'


"In-depth exploration of inherit"
# to judge whether a class is the subclass of another class,
# we can use the method 'issubclass':

print(issubclass(SPAMFilter, Filter))       # True
print(issubclass(Filter, SPAMFilter))       # False

# if you have a class, and you want its base-class,
# you can access the property '__bases__':

print(SPAMFilter.__bases__)                  # (<class '__main__.Filter'>,)
print(Filter.__bases__)                      # (<class 'object'>,)

# if you want to know whether an object is the living example of a special class
# you can use the 'isinstance':

s = SPAMFilter()
print(isinstance(s, SPAMFilter))            # True
print(isinstance(s, Filter))                # True
print(isinstance(s, str))                   # False

# using 'isinstance' is not a good method, belongs to the Polymorphism
# as you can see, the s is a (strict)living example of the SPAMFilter class
# but it also is the indirect living example of the Filter
# as the SPMFilter is the subclass of the Filter
# in other word, all the objects of the SPMAFilter are the objects of the Filter
# we can figure it by the example we told ago,
# 'isinstance' can be used in the class, such as str

# if you want to figure out which class an object belongs to, you can use
# property named '__class__':

print(s.__class__)                  # <class '__main__.SPAMFilter'>

'''
we should notice that:
for living example of the new class(no matter created by using '__metaclass__ = type'
or inherited by object), you can also use the 'type(s)' to figure out class it 
belongs to, for all the living example of old class, 'type' returns 'instance' 
'''

"more superclass"
# in chapter ago, you may notice that the plural form '__bases__'
# we have told about that we can use it to figure out base-class of class
# but the base-class may not only one.
# to figure out how to inherit more than one class
# now let's creat more than one class:


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print("Hi, my value is ", self.value)


class TalkingCalculator(Calculator, Talker):
    pass

# subclass'TalkingCalculator' does nothing, all it does is inherited from the
# superclass. it inherit 'calculate' from 'Calculator', inherit 'talk' from 'Talker'
# it became a calculator which can talk


tc = TalkingCalculator()
print(tc.calculate('1 + 2 * 3'))
print(tc.talk())
# >>Hi, my value is  7
# >>None

# like this we name it 'multiple inheritance'.
# it is a useful tool. However, unless you have to do like this,
# avoid using multiple inheritance as sometimes it may cause problems

# we should notice a point when we use multiple inheritance:
# if more than one superclass achieve
# one usage in different ways(more than one same-name method)
# we should be careful when we sort these superclasses in class statement
# because the method of the before class may cover the method of the after class
# so in the example of talking-calculator, if we include method 'talk'
# then the method 'talk' may cover the mehtod 'talk' in class 'Taker'(cause it can't be accessed)
# if you revers the sort of superclass:


class TalkingCalculator(Talker, Calculator):
    pass

# this causes the 'talk' in 'Talk' also can be accessed
# when superclasses of many superclasses are the same
# the sort of accessing superclass when you search for specified method or property
# we called "MRO", it is completed


"interface(接口) and introspection(内省)"
# interface is associated to the polymorphism.
# when you deal with objects, you only care the interface(TCP/Protocols):
# method and property(attribute) external
# in Python, not point external object which including specified methods
# can be used as argument

# as usual, you may ask objects follow specified interface(specified method)
# but if you need, you can ask request:
# not strictly call the methods and hope everything goes well
# check whether the method is existed.


print(hasattr(tc, "talk"))                  # True
print(hasattr(tc, "fnord"))                 # False

# in the code before, you can see the tc(the attribute class"TalkerCalculator")
# includes the property "talk"(points to the same method)
# but no method "fnord"
# if you want, you can check whether you can call the porperty "talk"


print(callable(getattr(tc, "talk", None)))           # True
print(callable(getattr(tc, "fnord", None)))          # False

# we should notice that: we don't access the property using
# "hasattr" in if statement
# it uses the "getattr"(it can allow me to use the default "None")
# then call the "callable"
'''
"setattr" is opposite to the "getattr", can be used to set the property of it:
setattr(tc, "name", "Mr. Gumby")
print(tc.name)
>>Mr. Gumby
'''
# to access the value storage in the object
# you can access the property "__dict__"
# if you want to make sure how the constitute of the object
# you should study module "inspect"
# this module is for senior user to creat the object IE
# (let the user to browse the program the Python-object in graph)
# and other program which may use the module


"Abstract base class"
# however, there is a way better than the check every methods
# Python almost belongs to the duke type
# that is means assume all the objects can finish the work
# at the same time, use "hasattr" to check whether the method is existed
# many languages(such as Java or Go) can explicit appoint the interface
# so the Python introduce the "abc" module to provide the solution
# the module "abc" support the abstract base class
# in fact, the abstract base class the don't support the instantiation class
# here is an example:


from abc import ABC, abstractmethod


class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


# formal like "@this" we call it decorator(装饰器)
# the point in this example is that you use the "@abstractmethod"
# to make the method abstract --- method should be made sure in subclass


# the important point of abstract class is it can't instantiation(实例化):

'''
Talker() 

Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
TypeError: Can't instantiate abstract class Talker with abstract methods talk
'''

# assume that a subclass is derived from the it:


class Knigget(Talker):
    pass

# as we don't rewrite the method "talk", so the object is abstract
# but we can't make it instantiation
# if you want to do this, it may get error.
# but you can rewrite the class to make it can assign the method:


class Knigget(Talker):
    def talk(self):
        print("Ni")

# now we can instantiation it, it is the main usage of the abs-class
# we can use it like this:


k = Knigget()
print(isinstance(k, Talker))                # True
k.talk()                                    # Ni

# we don't care what the object is,
# we only care what can this object do(method of the object)
# so we only have to do with the method "talk", even though
# it is not the subclass of the "Talker", it still can pass the type check
# now let's creat another class


class Herring:
    def talk(self):
        print("Blub.")

# the attribute of the class can pass the check whether it is the class
# of the object "Talker". but it is not the object of the "Talker":


her = Herring()
print(isinstance(her, Talker))          # False

# Of cause you can derive the "Herring" from the "Talker"
# but the "Herring" may come from other people's modules
# in this case, we can't do this
# you can register "Herring" as the "Talker"(not derive subclass from Talker or Herring)
# but if we do this all the objects of the "Herring" will be regarded as the objects
# of the "Talker":


print(Talker.register(Herring))         # <class '__main__.Herring'>
print(isinstance(her, Talker))          # True
print(isinstance(Herring, Talker))     # False


# however, there is an disadvantage of it, The security provided by
# deriving directly from an abstract class is gone.


class Clam:
    pass


print(Talker.register(Clam))            # <class '__main__.Clam'>
print(issubclass(Clam, Talker))         # True
c = Clam()
print(isinstance(c, Talker))            # True

'''
c.talk()
>>Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
AttributeError: 'Clam' object has no attribute 'talk'
'''
# in other word, we should regard 'isinstance' as an expression of intention(意图)
# in here, the 'c' is an intention of becoming 'Talker'
# we trust it can replace the due of the "Talker"
# but it failed

'''
something about the object-oriented:

1.put something associated together. if a function operate a global variable
  it is better to put them in a class as property(attribute) or a method
2.don't let the objects too intimate. the method only care the property 
  belongs to its attribute.for statement of other attributes, 
  let them deal it alone.
3.be careful when use inherit. specially multiple inheritance. sometimes the 
  inheritance is useful, but sometime it may cause the problem complex
  it is too difficult to use multiple inheritance and debug
4.keep concise. to make the method short, we should make all codes can be
  finished reading in 30 seconds. 
  
To figure out what classes should we have, and what methods should the classes
include, we should do like this:
(1) record the description of some problems(what should the problem do),
    and mark all the n., v., adj.
(2) find class from the n.
(3) find method from the v.
(4) find property from the adj.
(5) allocate methods or properties to the classes

after doing these, we should consider the relationship between the classes and objects 
(such as inherit and cooperation)and their duty. we can do like this: 
(1) record a sort of use cases. that is the environment for program.
    try to make the use cases cover all the usage.
(2) deeply understand every case, make the model includes all these
    if omit thing, add it; if thing wrong, change it. untill it is perfect
'''

'''
Summary

1. object: 
            the object is consisted of property and method. the property is the
            variable of the object, and method is function of the object. consider the 
            functions, the (associated)method has a different point,
            it always make object it belongs to as the first argument of itself.
            this argument we always call it "self".
            
2. class: 
          the class is a sort of objects. and these objects belong to the special class.
          the main task of class is defining methods its attribute.
          
3. Polymorphism: 
                 the Polymorphism means that which can deal with different type and
                 object of class. that means we don't have to know which class the object
                 belongs to and we can use its method.
                 
4. encapsulation: 
                 the object may hide its statement. in some languages, we only can access 
                 statement(property) of object by its methods. in Python, all the properties
                 are public. but we should be careful when we strictly access the statement
                 of object as we may cause the statement different.
                 
5. inherit: 
            a class can be as a subclass of another one or more classes. in this case,
            subclass will inherit all the methods of the superclasses. you can appoint 
            more than one super classes. so a usual usage is using one super class or 
            more mixed super classes.
            
6. Interfaces and introspection: 
                                usually, you don't have to insert search the objects,
                                only depend on the polymorphism calling the methods we need
                                if we want to make sure the object include what method and 
                                property, some function can help you done this.

7. abstract subclass:
                    we can creat abstract subclass by module "abc". the abstract subclass 
                    may appoint what features the subclasses should include, but not make true
                    them.
    
8. object-oriented design:
                          about how to make object-oriented design and whether we have to 
                          make object-oriented design. there are different points.
                          all we should do is deeply understanding the mean of it.
'''

'''
new functions in this chapter:

1.callable(object)                          判断对象是否可调用（如是否是函数或方法）
2.getattr(object,name[,default])            获取属性的值，还可提供默认值
3.hasattr(object, name)                     确定对象是否有指定的属性
4.isinstance(object, class)                 确定对象是否是指定类的实例
5.issubclass(A, B)                          确定A是否是B的子类
6.random.choice(sequence)                   从一个非空序列中随机地选择一个元素
7.setattr(object, name, value)              将对象的指定属性设置为指定的值
8.type(object)                              返回对象的类型
'''














































































































































































































































































































































































