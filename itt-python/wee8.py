1. Count word frequency (ignore case & punctuation)

with open("file.txt", "r") as f:
    t = f.read().lower()

p = "!.,?:;\"'()-"

for c in p:
    t = t.replace(c, "")

w = t.split()

d = {}

for i in w:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for k in d:
    print(k + ":", d[k])

Input (file.txt): Hello world! Hello AI. 
Output: hello: 2 world: 1 ai: 1

**************************************************************

2. Find longest and shortest word 

with open("file.txt", "r") as f:
    t = f.read().lower()

w = t.split()

l = w[0]   # longest
s = w[0]   # shortest

for i in w:
    if len(i) > len(l):
        l = i
    if len(i) < len(s):
        s = i

print("Longest:", l)
print("Shortest:", s)

Input: 
Python is powerful and easy 
Output: 
Longest: powerful   
Shortest: is 

**************************************************************

3. Reverse file line by line 

with open("file.txt", "r") as f:
    for l in f:
        print(l.strip()[::-1])

Input: 
Hello 
World 

Output: 
olleH   
dlroW

**************************************************************

4. Merge two files alternately 

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    l1 = f1.readlines()
    l2 = f2.readlines()

n = min(len(l1), len(l2))

for i in range(n):
    print(l1[i].strip())
    print(l2[i].strip())

Input (file1): 
A 
B 
C 
Input (file2): 
1 
2 
3 
Output: 
A   
1   
B   
2   
C   
3

**************************************************************

5. Remove duplicate lines 

with open("file.txt", "r") as f:
    s = set()   # to store unique lines

    for l in f:
        l = l.strip()
        if l not in s:
            print(l)
            s.add(l)

Input:  
apple   
banana   
apple   
orange   
banana 

Output: 
apple   
banana   
orange

**************************************************************

6. Remove duplicate lines 

with open("file.txt", "r") as f:
    l = []

    for i in f:
        i = i.strip()
        if i not in l:
            l.append(i)
            print(i)

Input: 
apple   
banana   
apple   
orange   
banana 

Output: 
apple   
banana   
orange

**************************************************************

7. Count vowels, consonants, digits, spaces 
8.

with open("file.txt", "r") as f:
    t = f.read().lower()

v = c = d = s = 0

for i in t:
    if i in "aeiou":
        v += 1
    elif i.isalpha():
        c += 1
    elif i.isdigit():
        d += 1
    elif i == " ":
        s += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", s)

Input: 
Hello 123 

Output: 
Vowels: 2   
Consonants: 3   
Digits: 3   
Spaces: 1 

**************************************************************

9. Copy file excluding blank lines 

with open("file.txt", "r") as f, open("out.txt", "w") as o:
    for l in f:
        if l.strip() != "":
            o.write(l)

Input: 
Hello 
World 
AI 
Output: 
Hello   
World   
AI

**************************************************************

10. Sort lines alphabetically 

with open("file.txt", "r") as f:
    l = f.readlines()

l = [i.strip() for i in l]
l.sort()

for i in l:
    print(i)

Input: 
banana   
apple   
orange 

Output: 
apple   
banana   
orange
