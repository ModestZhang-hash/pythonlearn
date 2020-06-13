# Talking about Exception in Python

## What is Exception

In fact Python will report exception when it meet error. if error is not been deal with, the 

program will terminate and display a error message(traceback):

```python
>>> 1 / 0 
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
ZeroDivisionError: integer division or modulo by zero 
```

 every exception is a living example of class named 'ZeroDivisionError'.

In fact we can learn how to make exception first, and then we will learn how to deal with these exception then.



## Raise statement

if you want to make exception , you can use raise statement. and make a class(must sub class of Exception) or living example (instantiation) as argument. when you use class as argument, it will create a instantiation . the example next is using inter exception class named "Exception":

```python
raise Exception
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
Exception 
>>> raise Exception('hyperdrive overload') 
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
Exception: hyperdrive overload 
```

In the first example(raise Exception), cause a general exception, which doesn't point out what exception it caused. In the second example, and a error message "hyperdrive  overload" 

there are many inter exception class.  all these classes can be used in the raise statement:

```python
raise ArithmeticError 
Traceback (most recent call last): 
 File "<stdin>", line 1, in ? 
ArithmeticError 
```

| name of classes   | description                                                  |
| ----------------- | ------------------------------------------------------------ |
| Exception         | almost all the exception classes are derived from it         |
| AttributeError    | cause when quote property or when assign value               |
| OSError           | cause when operate system can't deal with pointed assignment(such as when search file),more than one class |
| IndexError        | cause when want to use index which not exist. sub class of LookupError |
| KeyError          | cause when want to use key which not exist. sub class of LookupError |
| NameError         | cause when can't find name of variable                       |
| SyntaxError       | cause when some code block is wrong                          |
| TypeError         | cause when some internal operate or function used for wrong type |
| ValueError        | cause when some internal operate or function used for object: right type but value wrong |
| ZeroDivisionError | cause when second variable is 0 in devision                  |

## Self-defining exception class

If you want to use specific method to deal with specific error, you have to use a self-defining exception class:

how to create a exception class? like create other class, you should inherit directly or indirectly (this means that you can inherit from any internal exception class) so, the code block which creat a self-defining exception class like this :

```python
class SomeCustomException(Exception): pass 
```

it is not difficult (of cause if you want, you can add method in the class).

## Catch exception

usually we can deal with the exception and this operation named "catch exception".

To make this , we can use try/except statement. Assume that you create a program, let user input two number, than make devision. like this :

```python
x = int(input('Enter the first number: ')) 
y = int(input('Enter the second number: ')) 
print(x / y) 
```

the program runs well, while the user input 0 as the second number:

```python
Enter the first number: 10 
Enter the second number: 0 
Traceback (most recent call last): 
 File "exceptions.py", line 3, in ? 
 print(x / y) 
ZeroDivisionError: integer division or modulo by zero 
```

to catch this exception and deal with the error (print a better message for user), we can rewrite the program like this:

```python
try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 print(x / y) 
except ZeroDivisionError: 
 print("The second number can't be zero!") 
```

------

**notice:    the exception is broadcast from function to the call function . if not be catch in call function, it will broadcast to top. this means that you can use try/except statement to catch exception created by other people.**

------

## Not have to provide arguments

after catching exception, if you want to call it. you can call 'raise' statement without argument(of cause you can explicit provide exception catch).

it is very useful, let's see a calculate class which can restrain exception "ZeroDivisionError", if we use this usage, the calculator will print a wrong message, not spread the exception. when user use this calculator, it is useful to restrain exception; but when using internal function, spread exception is better way(this time we have not to use the usage), next is a code of class like this :

```python
class MuffledCalculator: 
 muffled = False 
 def calc(self, expr): 
 try: 
 return eval(expr) 
 except ZeroDivisionError: 
 if self.muffled: 
 print('Division by zero is illegal') 
 else: 
 raise 
```

------

**notice: When we divide 0(as second number), if we use 'restrain' usage, the method ' calc ' will return None. In other word, if we restrain the exception,  we should not depend on the return value.**

------

The example below displays usage of  this class(includes the on and off restrain usage):

```python
>>> calculator = MuffledCalculator() 
>>> calculator.calc('10 / 2') 
5.0 
>>> calculator.calc('10 / 0') # off the usage of 'restrain'
Traceback (most recent call last): File "<stdin>", line 1, in ? 
 File "MuffledCalculator.py", line 6, in calc 
 return eval(expr) 
 File "<string>", line 0, in ? 
ZeroDivisionError: integer division or modulo by zero 
>>> calculator.muffled = True 
>>> calculator.calc('10 / 0') 
Division by zero is illegal 
```

 If we can't deal with exception, using 'raise' statement without arguments in except statement is a better way. but sometimes you want to cause other exception, in this case, the exception which cause into 'except' statement will be storage as the exception context. and display in the end message, some just like this :

```python
>>> try: 
... 1/0 
... except ZeroDivisionError: 
... raise ValueError 
... 
Traceback (most recent call last): 
 File "<stdin>", line 2, in <module> 
ZeroDivisionError: division by zero 
```

 when we deal with this exception, cause another exception:

```python
Traceback (most recent call last): 
 File "<stdin>", line 4, in <module> 
ValueError
```

You can use the" raise .... from ....."statement to provide its own exception context, you can also forbid exception context.

```python
>>> try: 
... 1/0 
... except ZeroDivisionError: 
... raise ValueError from None 
... 
Traceback (most recent call last): 
 File "<stdin>", line 4, in <module> 
ValueError
```

## One more 'except' statements

If you run the program above, you input a no-number value, it will cause another exception:

```python
Enter the first number: 10 
Enter the second number: "Hello, world!" 
Traceback (most recent call last): 
 File "exceptions.py", line 4, in ? 
 print(x / y) 
TypeError: unsupported operand type(s) for /: 'int' and 'str' 
```

because the program only catch the 'ZeroDivisionError' ,this exception will be not found, and cause program pause. to catch this exception at same time, we can add a 'except' statement in the "try/except" statement:

```python
try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 print(x / y) 
except ZeroDivisionError: 
 print("The second number can't be zero!") 
except TypeError: 
 print("That wasn't a number, was it?") 
```

## Kill two birds with one stone

If you want to one 'except' statement to catch one more exceptions , you can assign these exceptions in a tuple, just like this :

```python
try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 print(x / y) 
except (ZeroDivisionError, TypeError, NameError): 
 print('Your numbers were bogus ...') 
```

in this code block, if user input a string or 0 rather than a no-zero number, it will print same message. of cause, only print wrong message is not enough, another solution is that ask user input the number again until it can run.

## Catch object

The example below is still run when meet exception:

```python
try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 print(x / y) 
except (ZeroDivisionError, TypeError) as e: 
 print(e) 
```

in this code block, the 'except' still catch two exceptions, but because you explicit catch the object, you can print it out and let user knows that what happen.

## Catch the whole lot in an action

Even if the program deals with so many exceptions, there still are some Big and Little Fish. for example, for the program above which make division, if user only input a "Enter" key when we remind him input a number, it will cause a wrong message, which is some problems happened in some where(stack track). just like this:

```python
Traceback (most recent call last): 
 ... 
ValueError: invalid literal for int() with base 10: '' 
```

this exception don't be catch by the "try/except" statement, of cause, as you don't predicted this problem.

however, if you still want to catch all the exceptions using one code block, you only have to not assign any exception in "except" statement:

```python
try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 print(x / y) 
except: 
 print('Something wrong happened ...') 
```

Now, user can do anything he want :

```python
Enter the first number: "This" is *completely* illegal 123 
Something wrong happened ... 
```

## All is well

Just like 'if' or 'while' loop, we can add 'else' statement after the 'try/except' statement:

```python
try: 
 print('A simple task') 
except: 
 print('What? Something went wrong?') 
else: 
 print('Ah ... It went as planned.') 
```

if you run this code, the output will be like this:

```python
A simple task 
Ah ... It went as planned. 
```

By using 'else' statement, we can make true the loop above the program:

```python
while True: 
 try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 value = x / y 
 print('x / y is', value) 
 except: 
 print('Invalid input. Please try again.') 
 else: 
 break 
```

In here, only when there is no exception, the program will terminate the loop(this is make by the "break" statement in "else" statement), in other words, when cause error, the program will ask user to re input. Here is the output of the program:

```python
Enter the first number: 1 
Enter the second number: 0 
Invalid input. Please try again. 
Enter the first number: 'foo' 
Enter the second number: 'bar' 
Invalid input. Please try again. 
Enter the first number: baz 
Invalid input. Please try again. 
Enter the first number: 10 
Enter the second number: 2 
x / y is 5 
```

We have told about that a better solution is using empty "except" statement to catch all the exceptions which belong to the subclass of the class named "Exception", but you can't make sure to catch all the exceptions. because the code of the "try/except" statement may use the old string-exception to concurrence exceptions which are derived from the "Exception".

However, if we use the "except Exception as e", we can do like this:

```python
while True: 
 try: 
 x = int(input('Enter the first number: ')) 
 y = int(input('Enter the second number: ')) 
 value = x / y 
 print('x / y is', value) 
 except Exception as e: 
 print('Invalid input:', e) 
 print('Please try again') 
 else: 
 break
```

Here is the output of the program:

```python
Enter the first number: 1 
Enter the second number: 0 
Invalid input: integer division or modulo by zero 
Please try again 
Enter the first number: 'x' Enter the second number: 'y' 
Invalid input: unsupported operand type(s) for /: 'str' and 'str' 
Please try again 
Enter the first number: quuux 
Invalid input: name 'quuux' is not defined 
Please try again 
Enter the first number: 10 
Enter the second number: 2 
x / y is 5
```

## Finally

In the end, there is a "finally"statement. we can use it in the work of cleaning after we cause the exception. this statement is paired with the "try" statement:

```python
x = None 
try: 
 x = 1 / 0 
finally:
 print('Cleaning up ...') 
 del x 
```

in this example, no matter what exception caused in the "try" statement, it still will run the "finally" statement. But why we should default the 'x' ? Because if we don't do that, ZeroDivisionError will not have chance to assign it, then the "finally" statement will cause exception when it run "del".

If we run this program, it will crash after run the cleaning work:

```python
Cleaning up ... 
Traceback (most recent call last): 
 File "C:\python\div.py", line 4, in ? 
 x = 1 / 0 
ZeroDivisionError: integer division or modulo by zero
```

Although using 'del' to delete the variable is a stupid way .

We can include the "try", "except", "finally", "else":

```python
try: 
 1 / 0 
except NameError: 
 print("Unknown variable") 
else: 
 print("That went well!") 
finally: 
 print("Cleaning up.") 
```

## Exception and function

exceptions and functions always have association. if we don't deal with the exception of the function , it will update to the place where call this function, if not deal with in that place, it will always update until to the main program(global scope) .Let's see an example:

```python
>>> def faulty(): 
... raise Exception('Something is wrong') 
... 
>>> def ignore_exception(): 
... faulty() 
... 
>>> def handle_exception(): 
... try: 
... faulty() 
... except: 
... print('Exception handled') 
... 
>>> ignore_exception() 
Traceback (most recent call last): 
 File '<stdin>', line 1, in ? 
 File '<stdin>', line 2, in ignore_exception 
 File '<stdin>', line 2, in faulty 
Exception: Something is wrong 
>>> handle_exception() 
Exception handled
```

as you can see, the exception spread from ''faulty'' and "ignore-exception" to external. When we call the "handle-exception" ,the exception spread to the "handle-exception" and been deal with by the "try/except" statement.

## Zen of exception

Assume that you have a dictionary, you would print a value of a specified key if you find it be there. a code block to make it just like this:

```python
def describe_person(person): 
 print('Description of', person['name']) 
 print('Age:', person['age']) 
 if 'occupation' in person: 
 print('Occupation:', person['occupation']) 
```

if you call this function, you input a message just including name"Troatwobbler" and age 42, the ouput will just like this :

```python
Description of Throatwobbler Mangrove 
Age: 42
```

if you and a work "camper" in dictionary, the output will just like this:

```python
Description of Throatwobbler Mangrove 
Age: 42 
Occupation: camper
```

this code is simple but not efficiency, because it has to search key "occupation" twice: one to make sure it is there , twice to take its value and print it. Here is another solution :

```python
def describe_person(person): 
 print('Description of', person['name']) 
 print('Age:', person['age']) 
 try: 
 print('Occupation:', person['occupation']) 
 except KeyError: pass
```

In here, it only have to assume that the key is here, if the assumption is true, then it will print its value of it, if not exist, it will cause KeyError exception, and "except" statement will catch it.

You may see that to check if an object have a property , "try/except" may work. for example, to check an object have a property "write", using code just like this :

```python
try: 
 obj.write 
except AttributeError: 
 print('The object is not writeable') 
else: 
 print('The object is writeable') 
```

in here, the "try" statement just access the property "write", but do nothing with it. if it cause "AttributeError"exception, it means that there is no property "write". 

## Less exception circumstances

If you just want to warn that the condition is not right, you can use the function 'warn' in model "warnings":

```python
>>> from warnings import warn 
>>> warn("I've got a bad feeling about this.") 
__main__:1: UserWarning: I've got a bad feeling about this. 
>>> 
```

the warning just displays once, if you still run it, it will do nothing.

if code block wants to use your model, you can use the function "filterwarnings" in model "warnings" to restrain your warning, and assign method to deal with it. such as "error" or "ignore":

```python
>>> from warnings import filterwarnings 
>>> filterwarnings("ignore") 
>>> warn("Anyone out there?") 
>>> filterwarnings("error") 
>>> warn("Something is very wrong!") 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
UserWarning: Something is very wrong! 
```

 As you can see, we cause the exception "UserWarning" , when we waring that, point out exception will happen(type of waring) but must be the sub class of "Warnings" . If warning turns to error, if will use the exception. any other,  we can filter some warning according the exception.

```python
>>> filterwarnings("error") 
>>> warn("This function is really old...", DeprecationWarning) 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
DeprecationWarning: This function is really old... 
>>> filterwarnings("ignore", category=DeprecationWarning) 
>>> warn("Another deprecation warning.", DeprecationWarning)
>>> warn("Something else.") 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
UserWarning: Something else. 
```

## Summary

1. **exception object:** exception objcet works when exception is caused. for exception, there are many way to deal with it: such as ignore it, or terminate it.
2. **cause exception:** we can use "raise" statement to cause exceptions. it use an exception class or instantiation as argument, you can also use two arguments(exception and message of error) , if there is no arguments in 'raise' statement when call "except" statement, it will recause exception.
3. **self-defining exception class:** you can creat exception from "except" statement.
4. catch exception: to catch exception, you can use "except" in "try" statement , in "except" statement, if not point out exception, you can catch all the exception, you can point out all the exception classes., the method is put them in a tuple. if we provide two arguments, the second argument will associate to the object. in a same "try/except" statement, you can include one more "except" statements, different method for different exceptions.
5. **else statement:** it runs when the "try" statement doesn't run.
6. finally : make sure the code will still run whatever there is exception. you can use the "try/finally" statement and put the code block in the "finally" sub statement.
7. **exception and function:** when function cause exception, the exception will spread to where call the function.
8. warning: the warning is different to the function, but print a error message. you can point the type of the warning, it is the sub class of the Warning. 