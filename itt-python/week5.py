##Question 1: Multi-Functional Calculator (Arithmetic & Sets)
Code:

import math

print("--- Simple Calculator ---")

while True:
    print("\ns - Square root\nu - Union\ni - Intersection\nd - difference\n")
    choice = input("\nAction (+, -, *, /, ^, s, u, i, d) or 'q' to quit: ").lower()

    if choice == 'q':
        print("Goodbye!")
        break

    if choice in ['+', '-', '*', '/', '^']:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        if choice == '+': print("\nAnswer:", num1 + num2)
        elif choice == '-': print("\nAnswer:", num1 - num2)
        elif choice == '*': print("\nAnswer:", num1 * num2)
        elif choice == '/':
            if num2 != 0:
                print("\nAnswer:", num1 / num2)
            else:
                print("\nError: Division by zero!")
        elif choice == '^': print("\nAnswer:", num1 ** num2)

    elif choice == 's':
        num = float(input("Number: "))
        if num >= 0:
            print("\nSquare Root:", math.sqrt(num))
        else:
            print("\nError: Cannot take square root of negative number!")

    elif choice in ['u', 'i', 'd']:
        set_a = set(input("Enter first set (a b c ...) (words/numbers): ").split())
        set_b = set(input("Enter second set (a b c ...) (words/numbers): ").split())

        if choice == 'u':
            result = set_a.union(set_b)
            if not result:
                print("\nNo elements found in either set!")
            else:
                print("\nUnion:", result)

        elif choice == 'i':
            result = set_a.intersection(set_b)
            if not result:
                print("\nNo matches identified!")
            else:
                print("\nIntersection:", result)

        elif choice == 'd':
            result = set_a.difference(set_b)
            if not result:
                print("\nNo difference found (Set A is a subset of Set B)!")
            else:
                print("\nDifference:", result)

    else:
        print("Invalid operator, TRY AGAIN!")
Use code with caution.

##Sample Output:
--- Simple Calculator ---
s - Square root
u - Union
i - Intersection
d - difference
Action (+, -, *, /, ^, s, u, i, d) or 'q' to quit: u
Enter first set (a b c ...) (words/numbers): Apple Banana
Enter second set (a b c ...) (words/numbers): Banana Cherry
Union: {'Apple', 'Banana', 'Cherry'}
Action (+, -, *, /, ^, s, u, i, d) or 'q' to quit: q
Goodbye!
##Question 2: Quadratic Equation Solver
Code:

import math

def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0 and returns the roots."""
    if a == 0:
        if b != 0:
            return f"Linear equation. One real root: {-c/b}"
        return "Not an equation (a and b are zero)."

    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return f"Two real roots: {root1} and {root2}"
    elif d == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-d) / (2*a)
        return f"Two complex roots: {real_part} + {imag_part}i and {real_part} - {imag_part}i"

try:
    n = int(input("How many equations do you want to solve? "))

    for i in range(1, n + 1):
        print(f"\n--- Equation {i} ---")
        a_coeff = float(input("Enter coefficient a: "))
        b_coeff = float(input("Enter coefficient b: "))
        c_coeff = float(input("Enter coefficient c: "))

        result = solve_quadratic(a_coeff, b_coeff, c_coeff)
        print(result)

except ValueError:
    print("Invalid input. Please enter numbers only.")

print("\nAll equations solved!")
Use code with caution.

##Sample Output:
How many equations do you want to solve? 1
--- Equation 1 ---
Enter coefficient a: 1
Enter coefficient b: -5
Enter coefficient c: 6
Two real roots: 3.0 and 2.0
All equations solved!
