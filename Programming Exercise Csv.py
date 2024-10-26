import csv

def collect_student_data():
    # Prompt the instructor for the number of students
    num_students = int(input("Enter the number of students: "))
    students_data = []

    for _ in range(num_students):
        # Collect student information
        first_name = input("Enter the student's first name: ")
        last_name = input("Enter the student's last name: ")
        
        try:
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))
        except ValueError:
            print("Please enter valid integer grades for the exams.")
            continue
        
        # Append the student's data as a list
        students_data.append([first_name, last_name, exam1, exam2, exam3])
    
    return students_data

def write_to_csv(students_data):
    # Define the CSV header
    header = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]
    
    # Write the student data to 'grades.csv' using the with statement
    with open("grades.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header
        writer.writerows(students_data)  # Write student data

def main():
    students_data = collect_student_data()
    write_to_csv(students_data)
    print("Data has been written to grades.csv.")

main()
