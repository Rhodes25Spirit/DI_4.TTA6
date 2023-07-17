>>> numbers = (1,2,4,5,6)
>>> numbers[0]
1
>>> fruits = ("apple", "pear", "apple")
>>> fruits[0] = "melon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> first, second = ("apple", "pear")
>>> first
'apple'
>>> second
'pear'
>>> (1,2) + ("a", "b")
(1, 2, 'a', 'b')

my_tuple = 1,2,3,4
>>> my_tuple
(1, 2, 3, 4)

set(["ab","ba","ew"])
{'ab', 'ew', 'ba'}

>>> set(["apple", "pear", "apple"])
{'pear', 'apple'}
>>> fruits = ["apple", "banana", "apple"]
>>> fruits_set = set(fruits)
>>> fruits_set
{'apple', 'banana'}
>>> list(fruits_set)
['apple', 'banana']

>>> from sys import getsizeof
>>> a = [1, 2, 3]
>>> getsizeof(a)
88
>>> b = (1, 2, 3)
>>> getsizeof(b)
64