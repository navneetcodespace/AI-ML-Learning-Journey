

# Step 1 - Initialize Employee Data

employees = {
    101: {
        'name': 'Satya',
        'age': 27,
        'department': 'HR',
        'salary': 50000
    },

    102: {
        'name': 'Rahul',
        'age': 30,
        'department': 'IT',
        'salary': 65000
    },

    103: {
        'name': 'Priya',
        'age': 25,
        'department': 'Finance',
        'salary': 55000
    }
}


# Function to Add Employee


def add_employee():

    emp_id = int(input("Enter Employee ID: "))

    # Check if employee ID already exists
    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))


    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee added successfully.\n")



# Function to View All Employees


def view_employees():


    if not employees:
        print("No employees available.\n")
        return

    print("\n Employee Records \n")


    print(f"{'ID':<10}{'Name':<15}{'Age':<10}{'Department':<15}{'Salary':<10}")

    print("-" * 60)


    for emp_id, details in employees.items():

        print(
            f"{emp_id:<10}"
            f"{details['name']:<15}"
            f"{details['age']:<10}"
            f"{details['department']:<15}"
            f"{details['salary']:<10}"
        )

    print()



# Function to Search Employee


def search_employee():

    emp_id = int(input("Enter Employee ID to Search: "))


    if emp_id in employees:

        details = employees[emp_id]

        print("\nEmployee Found\n")

        print(f"Employee ID : {emp_id}")
        print(f"Name        : {details['name']}")
        print(f"Age         : {details['age']}")
        print(f"Department  : {details['department']}")
        print(f"Salary      : {details['salary']}")

        print()

    else:
        print("Employee not found.\n")



# Main Menu Function


def main_menu():

    while True:

        print(" Employee Management System ")

        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter Your Choice: ")


        if choice == '1':
            add_employee()


        elif choice == '2':
            view_employees()


        elif choice == '3':
            search_employee()


        elif choice == '4':
            print("Thank you for using EMS.")
            break


        else:
            print("Invalid choice. Please try again.\n")


main_menu()