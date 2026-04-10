## Problem Statement
Create a file-based Payroll Management System that allows adding, viewing, updating, and deleting employee records. 
Salaries must be calculated based on roles with specific basic pay ranges.
  
import os

BASE_DIR = "employees"

role_salary_ranges = {
    "Manager": (50000, 100000),
    "Developer": (30000, 70000),
    "Designer": (25000, 60000),
    "Tester": (20000, 50000),
    "HR": (28000, 55000),
}

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

# ---------------- Salary Calculation ----------------
def calculate_salary(bp):
    hra = bp * 0.20
    da = bp * 0.10
    pf = bp * 0.12
    gross = bp + hra + da
    net = gross - pf
    return gross, net

# ---------------- Display Roles ----------------
def display_roles():
    print("\nAvailable Roles:")
    for role in role_salary_ranges:
        print(f"  - {role}")
    print()

# ---------------- Get Valid Basic Pay ----------------
def get_valid_basic_pay(role):
    if role not in role_salary_ranges:
        print(f"Warning: '{role}' is not listed in predefined salary ranges.")
        while True:
            bp = float(input("Please enter a Basic Pay for this role: "))
            if bp > 0:
                return bp
            else:
                print("Basic Pay must be a positive number. Please try again.")
    else:
        min_bp, max_bp = role_salary_ranges[role]
        while True:
            bp = float(input(f"Enter Basic Pay for {role} (allowed range: {min_bp} to {max_bp}): "))
            if min_bp <= bp <= max_bp:
                return bp
            else:
                print(f"Basic Pay must be between {min_bp} and {max_bp}. Please enter a valid amount.")

# ---------------- File Handling ----------------
def get_role_file_path(role):
    return os.path.join(BASE_DIR, f"{role}.txt")

def read_employees_from_file(role):
    path = get_role_file_path(role)
    employees_list = []
    if not os.path.exists(path):
        return employees_list
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 6:
                continue
            try:
                emp = {
                    "id": int(parts[0]),
                    "name": parts[1],
                    "role": parts[2],
                    "bp": float(parts[3]),
                    "gross": float(parts[4]),
                    "net": float(parts[5])
                }
                employees_list.append(emp)
            except ValueError:
                continue
    return employees_list

def write_employees_to_file(role, employees_list):
    path = get_role_file_path(role)
    with open(path, 'w') as file:
        for emp in employees_list:
            line = f"{emp['id']},{emp['name']},{emp['role']},{emp['bp']},{emp['gross']},{emp['net']}\n"
            file.write(line)

def employee_id_exists(emp_id):
    for role_file in os.listdir(BASE_DIR):
        role = role_file.replace(".txt", "")
        employees_list = read_employees_from_file(role)
        if any(emp["id"] == emp_id for emp in employees_list):
            return True
    return False

def find_employee(emp_id):
    for role_file in os.listdir(BASE_DIR):
        role = role_file.replace(".txt", "")
        employees_list = read_employees_from_file(role)
        for emp in employees_list:
            if emp["id"] == emp_id:
                return role, emp
    return None, None

# ---------------- Add Employee ----------------
def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    if employee_id_exists(emp_id):
        print("Employee ID already exists.")
        return

    name = input("Enter Employee Name: ")
    display_roles()
    role = input("Enter Employee Role: ")
    bp = get_valid_basic_pay(role)
    gross, net = calculate_salary(bp)

    employee = {
        "id": emp_id,
        "name": name,
        "role": role,
        "bp": bp,
        "gross": gross,
        "net": net
    }

    employees_list = read_employees_from_file(role)
    employees_list.append(employee)
    write_employees_to_file(role, employees_list)
    print("Employee record added successfully.")

# ---------------- View Employees ----------------
def view_employees():
    all_role_files = os.listdir(BASE_DIR)
    if not all_role_files:
        print("No employee records available.")
        return
    print("\n=========== Employee Records ===========")
    for file in all_role_files:
        role = file.replace(".txt", "")
        employees_list = read_employees_from_file(role)
        if employees_list:
            print(f"\nRole: {role}")
            for emp in employees_list:
                print("---------------------------------------")
                print(f"Employee ID   : {emp['id']}")
                print(f"Employee Name : {emp['name']}")
                print(f"Basic Pay     : {emp['bp']}")
                print(f"Gross Salary  : {emp['gross']}")
                print(f"Net Salary    : {emp['net']}")
                print("---------------------------------------")

# ---------------- Update Role ----------------
def update_role():
    emp_id = int(input("Enter Employee ID to update role: "))

    current_role, emp = find_employee(emp_id)
    if emp is None:
        print("Employee not found.")
        return

    display_roles()
    new_role = input("Enter new role: ")
    new_bp = get_valid_basic_pay(new_role)
    new_gross, new_net = calculate_salary(new_bp)

    current_employees = read_employees_from_file(current_role)
    current_employees = [e for e in current_employees if e["id"] != emp_id]
    write_employees_to_file(current_role, current_employees)

    emp["role"] = new_role
    emp["bp"] = new_bp
    emp["gross"] = new_gross
    emp["net"] = new_net

    # Add employee to new role file
    new_employees = read_employees_from_file(new_role)
    new_employees.append(emp)
    write_employees_to_file(new_role, new_employees)

    print("Employee role and salary updated successfully.")

# ---------------- Update Basic Pay ----------------
def update_basic_pay():
    try:
        emp_id = int(input("Enter Employee ID to update Basic Pay: "))
    except ValueError:
        print("Invalid input. Employee ID must be an integer.")
        return

    role, emp = find_employee(emp_id)
    if emp is None:
        print("Employee not found.")
        return

    new_bp = get_valid_basic_pay(emp["role"])
    new_gross, new_net = calculate_salary(new_bp)
    emp["bp"] = new_bp
    emp["gross"] = new_gross
    emp["net"] = new_net

    employees_list = read_employees_from_file(role)
    for i, e in enumerate(employees_list):
        if e["id"] == emp_id:
            employees_list[i] = emp
            break
    write_employees_to_file(role, employees_list)

    print("Basic Pay and salary updated successfully.")

# ---------------- Delete Employee ----------------
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    role, emp = find_employee(emp_id)
    if emp is None:
        print("Employee not found.")
        return

    employees_list = read_employees_from_file(role)
    employees_list = [e for e in employees_list if e["id"] != emp_id]
    write_employees_to_file(role, employees_list)

    print("Employee record deleted successfully.")

# ---------------- Main Menu ----------------
while True:
    print("\n====== Employee Payroll System ======")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Employee Role")
    print("4. Update Basic Pay")
    print("5. Delete Employee")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_role()
    elif choice == "4":
        update_basic_pay()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting Employee Payroll System. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

====== Employee Payroll System ======
1. Add Employee
2. View All Employees
3. Update Employee Role
4. Update Basic Pay
5. Delete Employee
6. Exit

Enter your choice: 1

Enter Employee ID: 101
Enter Employee Name: Alice

Available Roles:
  - Manager
  - Developer
  - Designer
  - Tester
  - HR

Enter Employee Role: Developer
Enter Basic Pay for Developer (allowed range: 30000 to 70000): 25000
Basic Pay must be between 30000 and 70000. Please enter a valid amount.
Enter Basic Pay for Developer (allowed range: 30000 to 70000): 40000
Employee record added successfully.

====== Employee Payroll System ======
1. Add Employee
...
Enter your choice: 1
Enter Employee ID: 101
Employee ID already exists.

====== Employee Payroll System ======
1. Add Employee
...
Enter your choice: 2

=========== Employee Records ===========

Role: Developer
---------------------------------------
Employee ID   : 101
Employee Name : Alice
Basic Pay     : 40000.0
Gross Salary  : 52000.0
Net Salary    : 47200.0
---------------------------------------

====== Employee Payroll System ======
1. Add Employee
...
Enter your choice: 4
Enter Employee ID to update Basic Pay: 101
Enter Basic Pay for Developer (allowed range: 30000 to 70000): 60000
Basic Pay and salary updated successfully.

====== Employee Payroll System ======
1. Add Employee
...
Enter your choice: 5
Enter Employee ID to delete: 101
Employee record deleted successfully.

====== Employee Payroll System ======
1. Add Employee
...
Enter your choice: 6
Exiting Employee Payroll System. Thank you!
