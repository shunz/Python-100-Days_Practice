"""Generator Expression

https://docs.python.org/3/tutorial/classes.html#generator-expressions

Some simple generators can be coded succinctly as expressions using a syntax
similar to list comprehensions but with parentheses instead of square brackets.
These expressions are designed for situations where the generator is used
right away by an enclosing function. Generator expressions are more compact
but less versatile than full generator definitions and tend to be more memory
friendly than equivalent list comprehensions.

Examples:

>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']

"""

print(sum(i**2 for i in range(11)))  # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))  # dot product

data = '无锡锡山山无锡，平湖湖水水平湖，常德德山山有德，长沙沙水水无沙，成都毒尘尘有毒'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
