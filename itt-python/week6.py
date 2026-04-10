##Question 1: Cartesian Product (itertools.product)
Code:

from itertools import product

l = ['red', 'green', 'blue']
p = list(product(l, repeat=2))

print(p)


##Sample Output:
[('red', 'red'), ('red', 'green'), ('red', 'blue'), ('green', 'red'), ('green', 'green'), ('green', 'blue'), ('blue', 'red'), ('blue', 'green'), ('blue', 'blue')]


##Question 2: Simple Combinations (itertools.combinations)
Code:

from itertools import combinations

l = ['A', 'B', 'C', 'D']
c = list(combinations(l, 2))

print(c)


##Sample Output:
[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]


##Question 3: Infinite Counting (itertools.count)
Code:

from itertools import count

c = count(10)
r = [next(c) for _ in range(5)]

print(r)


##Sample Output:
[10, 11, 12, 13, 14]


##Question 4: Cycling Through Elements (itertools.cycle)
Code:

from itertools import cycle

l = [5, 10, 15]
c = cycle(l)
r = [next(c) for _ in range(9)]

print(r)


##Sample Output:
[5, 10, 15, 5, 10, 15, 5, 10, 15]


##Question 5: Sliced Cycle (itertools.islice)
Code:

from itertools import cycle, islice

l = ['a', 'b']
c = cycle(l)
r = list(islice(c, 6))

print(r)


##Sample Output:
['a', 'b', 'a', 'b', 'a', 'b']


##Question 6: String Permutations (itertools.permutations)
Code:

from itertools import permutations

s = '123'
p = list(permutations(s))

for x in p:
    print(''.join(x))


##Sample Output:
123
132
213
231
312
321


##Question 7: List Permutations (itertools.permutations)
Code:

from itertools import permutations

l = ['X', 'Y', 'Z']
p = list(permutations(l))

print(p)


##Sample Output:
[('X', 'Y', 'Z'), ('X', 'Z', 'Y'), ('Y', 'X', 'Z'), ('Y', 'Z', 'X'), ('Z', 'X', 'Y'), ('Z', 'Y', 'X')]


##Question 8: Combinations with Replacement
Code:

from itertools import combinations_with_replacement

l = [1, 2]
r = list(combinations_with_replacement(l, 2))

print(r)


##Sample Output:
[(1, 1), (1, 2), (2, 2)]
