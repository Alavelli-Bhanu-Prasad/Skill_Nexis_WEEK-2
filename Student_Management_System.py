import csv
import os
filename = "students.csv"

def create_file():
    if os.path.exists(filename) == False:
        file = open(filename, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["Roll Number", "Name", "Marks"])
        file.close()

#function to add a new student
def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    #open file in append mode so old data is not lost
    file = open(filename, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([roll, name, marks])
    file.close()
    print("Student added successfully!")
    
#function to search a student by roll number
def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")

    file = open(filename, "r", newline="")
    reader = csv.reader(file)

    found = False
    for row in reader:
        if row[0] == roll:
            print("Roll Number:", row[0])
            print("Name       :", row[1])
            print("Marks      :", row[2])
            found = True
            break

    file.close()

    if found == False:
        print("Student not found.")

#function to delete a student by roll number
def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")

    #reading all existing rows first
    file = open(filename, "r", newline="")
    reader = csv.reader(file)
    all_rows = []
    for row in reader:
        all_rows.append(row)
    file.close()
    #creating a new list without the deleted student
    new_rows = []
    found = False
    for row in all_rows:
        if row[0] == roll:
            found = True
        else:
            new_rows.append(row)

    if found == False:
        print("Student not found.")
        return
    #writing the updated list back to the file (permanent change)
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    for row in new_rows:
        writer.writerow(row)
    file.close()

    print("Student deleted successfully!")

#function to display all students
def display_students():
    print("\n--- All Students ---")
    file = open(filename, "r", newline="")
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        print(row[0], "|", row[1], "|", row[2])
        row_count = row_count + 1
    file.close()
    if row_count == 1:
        print("No records found.")
def main():
    create_file()
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
main()