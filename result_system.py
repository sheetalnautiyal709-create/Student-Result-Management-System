import os


DATA_FILE = "students.txt"

def load_data():
    """Loads student data from the text file."""
    students = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    # Format: RollNo,Name,Maths,Science,English
                    parts = line.split(",")
                    roll_no = parts[0]
                    name = parts[1]
                    marks = [int(m) for m in parts[2:]]
                    students[roll_no] = {"name": name, "marks": marks}
    return students

def save_data(students):
    """Saves student data back to the text file."""
    with open(DATA_FILE, "w") as file:
        for roll_no, info in students.items():
            marks_str = ",".join(map(str, info["marks"]))
            file.write(f"{roll_no},{info['name']},{marks_str}\n")

def calculate_grade(percentage):
    """Returns a letter grade based on percentage."""
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else: return "Fail"

def add_student(students):
    """Adds a new student record."""
    print("\n--- Add New Student ---")
    roll_no = input("Enter Roll Number: ").strip()
    
    if roll_no in students:
        print(" Error: A student with this Roll Number already exists!")
        return

    name = input("Enter Student Name: ").strip()
    try:
        maths = int(input("Enter Marks for Maths (0-100): "))
        science = int(input("Enter Marks for Science (0-100): "))
        english = int(input("Enter Marks for English (0-100): "))
        
        if not (0 <= maths <= 100 and 0 <= science <= 100 and 0 <= english <= 100):
            print(" Error: Marks must be between 0 and 100.")
            return
            
        students[roll_no] = {"name": name, "marks": [maths, science, english]}
        save_data(students)
        print(f" Success: Record for {name} added successfully!")
    except ValueError:
        print("Error: Invalid input! Marks must be integers.")

def view_all_students(students):
    """Displays all student records in a table format."""
    print("\n" + "="*70)
    print(f"{'Roll No':<10}{'Name':<20}{'Maths':<8}{'Science':<9}{'English':<9}{'Total':<8}{'Grade':<5}")
    print("="*70)
    
    if not students:
        print("No student records found.")
    else:
        for roll_no, info in students.items():
            total = sum(info["marks"])
            percentage = total / 3
            grade = calculate_grade(percentage)
            m = info["marks"]
            print(f"{roll_no:<10}{info['name']:<20}{m[0]:<8}{m[1]:<9}{m[2]:<9}{total:<8}{grade:<5}")
    print("="*70)

def search_student(students):
    """Searches and displays a single student's report card."""
    print("\n--- Search Student Result ---")
    roll_no = input("Enter Roll Number to search: ").strip()
    
    if roll_no in students:
        info = students[roll_no]
        m = info["marks"]
        total = sum(m)
        percentage = round(total / 3, 2)
        grade = calculate_grade(percentage)
        
        print("\n" + "*"*30)
        print(f"   REPORT CARD: {info['name'].upper()} ")
        print("*"*30)
        print(f"Roll Number : {roll_no}")
        print(f"Maths       : {m[0]}/100")
        print(f"Science     : {m[1]}/100")
        print(f"English     : {m[2]}/100")
        print("-" * 30)
        print(f"Total Marks : {total}/300")
        print(f"Percentage  : {percentage}%")
        print(f"Final Grade : {grade}")
        print("*"*30)
    else:
        print(" Student record not found.")

def delete_student(students):
    """Deletes a student record."""
    print("\n--- Delete Student Record ---")
    roll_no = input("Enter Roll Number to delete: ").strip()
    
    if roll_no in students:
        name = students[roll_no]['name']
        del students[roll_no]
        save_data(students)
        print(f"Success: Record for {name} has been deleted.")
    else:
        print("Student record not found.")

def main():
    """Main menu interface."""
    students = load_data()
    
    while True:
        print("\n==================================")
        print(" STUDENT RESULT MANAGEMENT SYSTEM ")
        print("==================================")
        print("1. Add Student Record")
        print("2. View All Student Results")
        print("3. Search Student Result")
        print("4. Delete Student Record")
        print("5. Exit")
        print("==================================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print(" Invalid Choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
        main()