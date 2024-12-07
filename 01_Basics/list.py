PS D:\Code Practice\Python> python
Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> tea = ["black", "green", "milk"]

>>> tea
['black', 'green', 'milk']

>>> print(tea)
['black', 'green', 'milk']
>>> tea[0]
'black'
>>> tea[-2]
'green'
>>> tea[1:3]
['green', 'milk']
>>> tea[1:4]
['green', 'milk']
>>> tea[2] = "herbal"
>>> tea
['black', 'green', 'herbal']
>>> tea = ["black", "green", "milk", "herbal"]
>>> tea
['black', 'green', 'milk', 'herbal']
>>> tea[1:2]
['green']
>>> tea[1:2] = "lemon"
>>> tea
['black', 'l', 'e', 'm', 'o', 'n', 'milk', 'herbal']
>>> tea = ["black", "green", "milk", "herbal"]
>>> tea[1:2] = ["lemon"]
>>> tea
['black', 'lemon', 'milk', 'herbal']
>>> tea[1:3] 
['lemon', 'milk']
>>> tea
['black', 'lemon', 'milk', 'herbal']
>>> tea[1:1] 
[]
>>> tea
['black', 'lemon', 'milk', 'herbal']
>>> for t in tea:  
...     print(t)
...
black
lemon
milk
herbal
>>> for t in tea:
...     print(t, end="-")
...
black-lemon-milk-herbal->>>
>>>  if "milk" in tea:
  File "<stdin>", line 1
    if "milk" in tea:
IndentationError: unexpected indent
>>> tea
['black', 'lemon', 'milk', 'herbal']
>>> if "milk" in tea:
...     print("i have milk tea")
...
i have milk tea
>>> tea.append("oolong")
>>> tea
['black', 'lemon', 'milk', 'herbal', 'oolong']
>>> tea.pop()
'oolong'
>>> tea
['black', 'lemon', 'milk', 'herbal']
>>> tea.remove("green")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> tea.remove("green")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> tea.remove("milk")  
>>> tea
['black', 'lemon', 'herbal']
>>> tea.insert
<built-in method insert of list object at 0x00000166FA2B11C0>
>>> tea.insert(1, "green")
>>> tea
['black', 'green', 'lemon', 'herbal']
>>> teaCopy = tea.copy()
>>> teaCopy
['black', 'green', 'lemon', 'herbal']
>>> teaCopy.append("milk")
>>> teaCopy
['black', 'green', 'lemon', 'herbal', 'milk']
>>> num = [x**2 for x in range(10)]
>>> num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]