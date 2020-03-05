Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'hola'
>>> s[0] = 'l'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[0] = 'l'
TypeError: 'str' object does not support item assignment
>>> r = 'l' + s[1:]
>>> r
'lola'
>>> nombre1 = 'lola'
>>> nombre2 = 'joaquin'
>>> nombre1==nombre2
False
>>> nombre1==nombre1
True
>>> nombre1>nombre2
True
>>> u'niño'
'niño'
>>> U'niño'
'niño'
>>> 