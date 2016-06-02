# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> List and tuples are similar in that they can both store any type of data. However, only tuples can be used as keys for dictionaries since they are immutable unlike lists which can be changed. Another difference is that lists tend to be filled with homogenous data, whereas tuples tend to be stored with heterogenous data. Contrary to the idea of tuples being immutable, (yet still being considered immutable,) tuples are able to seemingly change in some rounadabout ways. Tuples and lists can both be added to, however, when something is added to a list its ID stays the same but with a tuple its ID will change, therefore it is considered immutable. Another seeming exception to tuples being immutable is when a tuple stores a list. The list can be changed and thereby seemingly changing the tuple that is holding it, however, the ID to the list has not changed and therefore the tuple which stores that reference to the list has not really been changed. For further reading see [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets and lists both allow for `x in set`, `len(set)`, and `for x in set`. Also, as long as the set is not a `frozenset`, both sets and lists can be changed, for instance, by adding or removing elements. However, there are many differences between sets and lists. Sets are unordered, cannot contain any duplicates, the elements in a set must be hashable, and can use operations such as intersection, union, difference, and symmetric difference.

>> Regarding performance, finding an element in a set can be, and usually is, much faster than in a list. However, in a worst case scenario they can be the same as stated in [this wiki](https://wiki.python.org/moin/TimeComplexity) on time complexity.

Examples:
```python
>>> a = [1,1,2,3,3,3,4]
>>> b = [2,4,5,5]
>>> list(a) 
[1, 1, 2, 3, 3, 3, 4]  # Notice the duplicates in the list
>>> set(a) 
set([1, 2, 3, 4])  # No more duplicates since now a set
>>> set(a).symmetric_difference(set(b)) 
set([1, 3, 5])  # Outputs differences between both lists
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `Lambda` is a simple way of creating an easy function. Usually is very short and is not given a name since it is only being used in that instance as part of another function.

Example:
```python
>>> simpsons_family = [
  ['Homer', 38],
  ['Maggie', 1],
  ['Lisa', 8],
  ['Marge', 34],
  ['Bart', 10]
]
>>> simpsons_family
[['Homer', 38], ['Maggie', 1], ['Lisa', 8], ['Marge', 34], ['Bart', 10]]
>>> sorted(simpsons_family, key=lambda x: x[1]) 
[['Maggie', 1], ['Lisa', 8], ['Bart', 10], ['Marge', 34], ['Homer', 38]]  # Sorted by age from youngest to oldest
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions make a new list by evaluating an expression and performing it on each element of a list.
>> `Map` makes a new list by perfoming a function on each element of a list.
>> `Filter` makes a new list by performing a function on each element of a list and if true, appends it to the new list.

>> List comprehensions are the preferred method of acheiving the same goal since it is usually easier to read, even though `map` can sometimes be faster.

Examples:
```python
>>> num_list = [1, 2, 3, 4, 5]
>>> squares_lc = [x * x for x in num_list]  # List comprehension to get squares
>>> squares_lc
[1, 4, 9, 16, 25]
>>> squares_map = map(lambda x: x*x, num_list)  # Same using map & lambda
>>> squares_map
[1, 16, 49, 196, 225]
>>> even_squares = filter(lambda x: x % 2 == 0, squares_map)  # Filter squares by even
>>> even_squares
[16, 196]
>>> [x*x for x in num_list if x%2==0]  # List comprehension with filtering squares by even
[16, 196]
>>> map(lambda x: x*x if x**2%2==0 else False, num_list)  # Using map, list of squares that are even and False if odd (Not pretty but shown for comparison to two options above)
[False, 16, False, 196, False]
>>>
>>> alpha_bet = {i+1 : chr(65+i) for i in range(26)}  # Dictionary comprehension
>>> alpha_bet
{1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
>>>
>>> set_comp = {x*x for x in num_list if x%2==0}  # Set comprehension with filtering squares by even
>>> set_comp
set([16, 196])
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





