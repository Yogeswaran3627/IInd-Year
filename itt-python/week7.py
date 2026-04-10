##Question 1: Finding Unique Elements
Code:

from collections import Counter
a = [5, 3, 5, 2, 3, 1, 4, 1, 2]
b = Counter(a)
for k in b:
   if b[k] == 1:
      print(k)


Sample Output:
4


##Question 2: Merging Dictionaries with ChainMap
Code:

from collections import ChainMap
a = {"a": 10, "b": 20}
b = {"b": 30, "c": 40}
c = ChainMap(a, b)
print(c["b"])


Sample Output:
20


##Question 3: Leap Year Check
Code:

import datetime as d
y = 2028
print(y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))


Sample Output:
True


##Question 4: Date Formatting
Code:

import datetime as d
a = d.datetime.now()
print(a.strftime("%d-%B-%Y %A"))


Sample Output:
10-April-2026 Friday


##Question 5: Week Number Extraction
Code:

import datetime as d
a = d.datetime.strptime("2026-03-10", "%Y-%m-%d")
print(a.strftime("%U"))


Sample Output:
10


##Question 6: Time Difference in Seconds
Code:

import datetime as d
a = d.datetime(2026, 3, 10, 10, 0, 0)
b = d.datetime(2026, 3, 10, 12, 30, 0)
print((b - a).total_seconds())


Sample Output:
9000.0


##Question 7: Generate Next 5 Days
Code:

import datetime as d
a = d.date.today()
for i in range(1, 6):
    print(a + d.timedelta(days=i))


Sample Output:
2026-04-11
2026-04-12
2026-04-13
2026-04-14
2026-04-15


##Question 8: Previous Month Calculation
Code:

import datetime as d
a = d.datetime.strptime("2026-03-10", "%Y-%m-%d")
m = a.month - 1 or 12
y = a.year - 1 if a.month == 1 else a.year
print(d.date(y, m, a.day))


Sample Output:
2026-02-10


##Question 9: Counting Sundays in a Month
Code:

import datetime as d
c = 0
for i in range(1, 32):
    try:
        if d.date(2025, 1, i).weekday() == 6:
            c += 1
    except:
        pass
print(c)


Sample Output:
4


##Question 10: Weekend Check
Code:

import datetime as d
a = d.datetime.strptime("2026-03-14", "%Y-%m-%d")
print(a.weekday() >= 5)


Sample Output:
True


##Question 11: Daily Event Counter
Code:

from collections import Counter
import datetime as d
a = ["2026-03-10 10:00", "2026-03-10 12:00", "2026-03-11 09:30", "2026-03-11 11:45", "2026-03-11 14:00"]
b = [x.split()[0] for x in a]
print(Counter(b))


Sample Output:
Counter({'2026-03-11': 3, '2026-03-10': 2})


##Question 12: Balanced Frequency Check
Code:

from collections import Counter
a = "aabbccddeeffgg"
b = Counter(a)
print(len(set(b.values())) == 1)


Sample Output:
True


##Question 13: Peak Hour Identification
Code:

from collections import Counter
a = ["2026-03-10 10:00", "2026-03-10 10:30", "2026-03-10 10:45"]
b = [x.split()[1].split(":")[0] for x in a]
c = Counter(b)
print(max(c, key=c.get))


Sample Output:
10


##Question 14: Grouping by Month
Code:

from collections import Counter
a = ["2025-01-10", "2025-01-20", "2025-02-05", "2025-02-15", "2025-03-01"]
b = [x[:7] for x in a]
print(Counter(b))


Sample Output:
Counter({'2025-01': 2, '2025-02': 2, '2025-03': 1})


##Question 15: Map Dates to Weekdays
Code:

from collections import defaultdict
import datetime as d
a = ["2025-01-10", "2025-01-20", "2025-02-05"]
b = defaultdict(list)
for x in a:
       y = d.datetime.strptime(x, "%Y-%m-%d").strftime("%A")
       b[y].append(x)
print(dict(b))


Sample Output:
{'Friday': ['2025-01-10'], 'Monday': ['2025-01-20'], 'Wednesday': ['2025-02-05']}


##Question 16: Finding the Earliest Date
Code:

import datetime as d
a = ["2025-01-10", "2023-05-01", "2024-07-09"]
b = [d.datetime.strptime(x, "%Y-%m-%d") for x in a]
print(min(b))


Sample Output:
2023-05-01 00:00:00


##Question 17: Detect Duplicate Dates
Code:

from collections import Counter
a = ["2025-01-10", "2025-01-10", "2025-02-01"]
b = Counter(a)
print([k for k in b if b[k] > 1])


Sample Output:
['2025-01-10']


##Question 18: Activity Check (Last 24 Hours)
Code:

import datetime as d
a = ["2026-03-27 09:00", "2026-03-26 15:00"]
# Assuming n = 2026-03-27 10:00:00 for the example
n = d.datetime(2026, 3, 27, 10, 0, 0) 
for x in a:
       t = d.datetime.strptime(x, "%Y-%m-%d %H:%M")
       if abs((n - t).total_seconds()) <= 86400:
           print(f"Active in last 24h: {x}")


Sample Output:
Active in last 24h: 2026-03-27 09:00
Active in last 24h: 2026-03-26 15:00


##Question 19: Finding List Discrepancies
Code:

from collections import Counter
a = [1, 2, 3, 4, 5]
b = [1, 2, 2, 3, 4, 4, 5]
c = Counter(b) - Counter(a)
print(list(c.elements()))


Sample Output:
[2, 4]


##Question 20: Grouping Words by Length
Code:

from collections import defaultdict
a = ["", "java", "go", "c", "ruby", "php"]
b = defaultdict(list)
for w in a:
    b[len(w)].append(w)
print(dict(b))


Sample Output:
{6: [''], 4: ['java', 'ruby'], 2: ['go'], 1: ['c'], 3: ['php']}


##Question 21: Grouping Scores by Name
Code:

from collections import defaultdict
a = [("Alice", 85), ("Bob", 78), ("Alice", 92), ("Bob", 88)]
b = defaultdict(list)
for n, m in a:
    b[n].append(m)
print(dict(b))


Sample Output:
{'Alice': [85, 92], 'Bob': [78, 88]}


##Question 22: First Non-Repeating Character
Code:

from collections import OrderedDict
a = "swiss"
b = OrderedDict()
for c in a:
    b[c] = b.get(c, 0) + 1
for k in b:
    if b[k] == 1:
        print(k)
        break


Sample Output:
w


##Question 23: Sliding Window Sum
Code:

from collections import deque
a = [1, 2, 3, 4, 5, 6]
w = 3
d = deque()
s = 0
for i in range(len(a)):
    d.append(a[i])
    s += a[i]
    if len(d) > w:
        s -= d.popleft()
    if len(d) == w:
        print(s)


Sample Output:
6
9
12
15


##Question 24: Palindrome Check using Deque
Code:

from collections import deque
a = "level"
d = deque(a)
print("Palindrome" if list(d) == list(reversed(d)) else "Not")


Sample Output:
Palindrome


##Question 25: Highest Earner with NamedTuple
Code:

from collections import namedtuple
E = namedtuple("E", "n s")
a = [E("A", 5000), E("B", 7000), E("C", 6000)]
print(max(a, key=lambda x: x.s))


Sample Output:
E(n='B', s=7000)
