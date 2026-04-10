##Question 1: Student Attendance Tracker

Code:

d1 = input("Enter the students in DAY1 :")
d2 = input("Enter the students in DAY2 :")
s1, s2 = set(d1.split()), set(d2.split())

print("\nStudents PRESENT in BOTH days :")
for x in (s1 & s2): print(x)

print("\nStudents ABSENT in SECOND days :")
for x in (s1 - s2): print(x)

print("\nStudents PRESENT in EITHER day :")
for x in (s1 | s2): print(x)


##Sample Output:

Enter the students in DAY1 : Arun Bala Chitra
Enter the students in DAY2 : Bala Divya

Students PRESENT in BOTH days : Bala
Students ABSENT in SECOND days : Arun, Chitra
Students PRESENT in EITHER day : Arun, Bala, Chitra, Divya


##Question 2: Network Security Log Analysis
Code:

L = set(input("Enter Successful IPs: ").split())
F = set(input("Enter Failed IPs: ").split())
B = set(input("Enter Blacklisted IPs: ").split())

print("\nBoth Successful & Failed (Not Blacklisted):", (L & F) - B)
print("Attempted but NEVER succeeded:", F - L)
print("Blacklisted but NEVER attempted:", B - (L | F))


##Sample Output:

Enter Successful IPs: 10.0.1 10.0.2
Enter Failed IPs: 10.0.1 10.0.3
Enter Blacklisted IPs: 10.0.3 10.0.4

Both Successful & Failed (Not Blacklisted): {'10.0.1'}
Attempted but NEVER succeeded: {'10.0.3'}
Blacklisted but NEVER attempted: {'10.0.4'}


##Question 3: Student-Club Mapping & Data Extraction
Code:

records = ["Arun:AI,ML,Robotics", "Bala:ML,IoT", "Chitra:AI,CyberSecurity"]
names, clubs, student_clubs = set(), set(), {}

for r in records:
    name, cl = r.split(":")
    cl_set = set(cl.split(","))
    names.add(name); student_clubs[name] = cl_set; clubs |= cl_set

print("Unique Names:", names)
print("Unique Clubs:", clubs)
print("Mapping:", student_clubs)


##Sample Output:

Unique Names: {'Arun', 'Bala', 'Chitra'}
Unique Clubs: {'ML', 'AI', 'IoT', 'Robotics', 'CyberSecurity'}
Mapping: {'Arun': {'AI', 'ML', 'Robotics'}, 'Bala': {'ML', 'IoT'}...}


##Question 4: Advanced Club Membership Filtering
Code:

# (Using student_clubs from Q3)
print("Students in BOTH AI and ML:")
for s, c in student_clubs.items():
    if {"AI", "ML"} <= c: print(s)

print("\nStudents in AI but NOT Robotics:")
for s, c in student_clubs.items():
    if "AI" in c and "Robotics" not in c: print(s)


##Sample Output:

Students in BOTH AI and ML: Arun
Students in AI but NOT Robotics: Chitra


##Question 5: Inventory Management (Stock vs. Sold)
Code:

stock = set(input("Enter current stock: ").split())
sold = set(input("Enter sold items: ").split())

print("\nProducts STILL in stock:")
for x in (stock - sold): print(x)


##Sample Output:

Enter current stock: Laptop Mouse Keyboard
Enter sold items: Mouse
Products STILL in stock: Laptop, Keyboard


##Question 6: Peer-to-Peer Course Recommendations
Code:

u1 = set(input("User 1 Interests: ").split())
u2 = set(input("User 2 Interests: ").split())

print("\nCommon Interests:", u1 & u2)
print("Suggested for User 1 (from User 2):", u2 - u1)
print("Suggested for User 2 (from User 1):", u1 - u2)


##Sample Output:

User 1 Interests:  Java
User 2 Interests:  SQL
Common Interests: {''}
Suggested for User 1: {'SQL'}
Suggested for User 2: {'Java'}
