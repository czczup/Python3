Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> students = {"203-2012-045":"John","203-2012-037":"Peter"}
>>> tuple(students.keys())
('203-2012-045', '203-2012-037')
>>> tuple(students.values())
('John', 'Peter')
>>> tuple(students.items())
(('203-2012-045', 'John'), ('203-2012-037', 'Peter'))
>>> students.get("203-2012-045")
'John'
>>> students.pop("203-2012-045")
'John'
>>> students
{'203-2012-037': 'Peter'}
>>> students.clear()
>>> students
{}
>>> 
