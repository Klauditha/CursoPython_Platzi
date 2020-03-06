Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> mystring='platzi'
>>> mystring[0]
'p'
>>> mystring[6]

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mystring[6]
IndexError: string index out of range
>>> len(mystring)
6
>>> mystring[len(mystring-1)]

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mystring[len(mystring-1)]
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> mystring[len(mystring)-1]
'i'
>>> mystring
'platzi'
>>> mystring.upper()
'PLATZI'
>>> my_other_string = 'EDIFICIO'
>>> my_other_string.lower()
'edificio'
>>> my_other_string.f

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    my_other_string.f
AttributeError: 'str' object has no attribute 'f'
>>> my_other_string.find('F')
3
>>> my_other_string(3)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    my_other_string(3)
TypeError: 'str' object is not callable
>>> my_other_string[3]
'F'
>>> 
