Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(5,4,3)
[]
>>>  range(5,40,3)
 
  File "<pyshell#2>", line 2
    range(5,40,3)
    ^
IndentationError: unexpected indent
>>> range(5,4,3)
[]
>>> range(5,40,3)
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38]
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(5):
	print('Hello wordl')

	
Hello wordl
Hello wordl
Hello wordl
Hello wordl
Hello wordl
>>> for i in range(30):
	if i % 3 != 0 :
		continue
	else:
		print(i**2)

		
0
9
36
81
144
225
324
441
576
729
>>> for i in range(30):
	if i % 3 ==0:
		print(i**2)
	elif i == 22:
		break

	
0
9
36
81
144
225
324
441
>>> for i in range(30):
	if i % 3 == 0:
		print(i)
	elif:
		
SyntaxError: invalid syntax
>>> for i in range(30):
	if i%3==0:
		print(i)
	elif i == 22:
		break

	
0
3
6
9
12
15
18
21
>>> r = 'ferrocarril'
>>> for letter in r:
	print(letter)

	
f
e
r
r
o
c
a
r
r
i
l
>>> 
