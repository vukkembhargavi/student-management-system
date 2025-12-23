from student import Student

students = {}

def add_student():
    sid = int(input("Enter ID: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    branch = input("Enter branch: ")

    students[sid] = Student(sid, name, marks, branch)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No records found.")
        return
    for s in students.values():
        print(s.student_id, s.name, s.marks, s.branch)

def search_student():
    sid = int(input("Enter ID to search: "))
    if sid in students:
        s = students[sid]
        print(s.student_id, s.name, s.marks, s.branch)
    else:
        print("Student not found.")

def delete_student():
    sid = int(input("Enter ID to delete: "))
    if sid in students:
        del students[sid]
        print("Student deleted.")
    else:
        print("Student not found.")

def sort_students():
    sorted_list = sorted(students.values(), key=lambda x: x.marks, reverse=True)
    for s in sorted_list:
        print(s.student_id, s.name, s.marks, s.branch)

def menu():
    while True:
        print("\n1.Add 2.View 3.Search 4.Delete 5.Sort 6.Exit")
        choice = input("Choose: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            sort_students()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

# 👇 THIS LINE IS MUST
menu()
