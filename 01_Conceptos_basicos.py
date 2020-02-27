Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> python

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python
NameError: name 'python' is not defined
>>> print

>>> hola

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    hola
NameError: name 'hola' is not defined
>>> def my_first_function():
	return "Hello World"

>>> my_first_function()
'Hello World'
>>> A = 3
>>> B = A
>>> A
3
>>> 
>>> L = [22,True, "una lista", [1,2]]
>>> L[0]
22
>>> T = (22, True, "una trupla")
>>> T[0]
22
>>> D = {"KILL BILL":"Tamarino", "AMELIE":"Jean-Pierre Jeunet"}
>>> D["KILL BILL"]
'Tamarino'
>>> int(4.2)
4
>>> float(4)
4.0
>>> str(4.3)
'4.3'
>>> list((4,5,2))
[4, 5, 2]
>>> len("key")
3
>>> type(4.5)
<type 'float'>
>>> map(str, [1, 2, 3, 4])
['1', '2', '3', '4']
>>> round(5.2222,1)
5.2
>>> range(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> sum([1, 2, 4])
7
>>> sorted([5, 2, 1])
[1, 2, 5]
>>> Li = [5, 2, 1]
>>> dir(Li)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(sorted)
Help on built-in function sorted in module __builtin__:

sorted(...)
    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

>>> class Estudiante(object):
	def __init__(self,nombre_r,edad_r):
		self.nombre = nombre_r
		self.edad = edad_r
		def hola(self):
			return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)

		
>>> e = Estudiante("Claudia",20)
>>> print e.hola()

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print e.hola()
AttributeError: 'Estudiante' object has no attribute 'hola'
>>> e.hola

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    e.hola
AttributeError: 'Estudiante' object has no attribute 'hola'
>>> e.hola()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    e.hola()
AttributeError: 'Estudiante' object has no attribute 'hola'
>>> hola()

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    hola()
NameError: name 'hola' is not defined
>>> e
<__main__.Estudiante object at 0x0000000003A6C320>
>>>  if ( a > b ):
 	elementos 
 elif ( a == b ): 
 	elementos 
 else:
 	elementos
 	
  File "<pyshell#44>", line 2
    if ( a > b ):
    ^
IndentationError: unexpected indent
>>> 
