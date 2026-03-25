# --- Day 1 ---

full_name = "Dineshkumar R"
age = 24
salary = 39.99
is_employed = True

print("Name", full_name , "type", type(full_name))
print("Age", age, "type", type(age))
print("Salary", salary, "type", type(salary))
print("Employed?", is_employed , "type", type(is_employed))

print(f"Name: {full_name} | type: {type(full_name)}")


# --- Day 2 ---

student_marks = [85, 92, 78, 95, 88]

print("First= ", student_marks[0])
print("Last = ", student_marks[4])

# student_marks.push(99)
student_marks.append(99)

low_mark = min(student_marks)
student_marks.remove(low_mark)

print("Maximum Mark = ", max(student_marks))
print("Minimim Mark = ", min(student_marks))

# total_count = student_marks.count()
total_count = len(student_marks)
avg_mark = sum(student_marks)/total_count
# print("Average Mark= ", avg_mark)
print(f"Avg Mark = {avg_mark:.2f}")

# print(student_marks.sort(reverse=True))
student_marks.sort(reverse=True)
print(student_marks)


employee = ("Dinesh", 20, "IT", 12345.00)

print(f"First= {employee[0]}")
print(f"Last= {employee[-1]}")

name, age, field, salary = employee
# print(f"The Details= {name, age, field, salary}")
print(f"Name: {name}, Age: {age}, Field: {field}, Sal: {salary}")

# salary = 666666
# employee[3] = 600000 Throws Type error

my_list = list(employee)
my_list[3] = 60000
my_tuple = tuple(my_list)
print("Updated Tuple= ", my_tuple)

student = {
    "name": "Dinesh",
    "age": 33,
    "course": "Python",
    "marks": 88,
    "is_passed": True
}

print(student.get("name"))
print(student.get("course"))

student["marks"] = 95
student["grade"] = "A"

print(student)

student.pop("is_passed")
print(student)

for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

for key in student:
    print(f"Key only: {key}")

for value in student.values():
    print(f"Value Only: {value}")


my_skills = {"Python", "Node.js", "React", "Python", "Java"}

print(my_skills)

# my_skills.append("FastAPI")
my_skills.add("FastAPI")

my_skills.remove("Java")
print(my_skills)
my_skills.discard("Ruby")
print(my_skills)

team_skills = {"Node.js", "React", "Docker", "Python"}

print(my_skills | team_skills)
print(my_skills & team_skills)
print(my_skills - team_skills)


# --- Day 3 ---
# import Optional from typing
from typing import Optional


a= 15
b= 4

print("below are arithmetic operators")
# print(a+b);
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

skills: list[str]= ["Java", "Python", "node", "react"]

if "Python" in skills:
    print("Python is in Skills")

if "Ruby" not in skills:
    print("Ruby Not in skills")

# def find_employee(id: int) => name: Optional:
def find_employee(id: int) -> Optional[str]:
    if id == 1:
        return "Pablo"
    # return null
    return None

data = ["Python", "Node.js", "React", "FastAPI"]

# def data_validate(length := len(data) > 3) :
if (length := len(data)) > 3 :
    print(f"The list is larger {length}")

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a is c)

print(find_employee(1))
print(find_employee(99))


# --- Day 4 ---

students = [
    {"name": "Dinesh", "marks": 85},
    {"name": "Kumar", "marks": 45},
    {"name": "Raj", "marks": 92},
    {"name": "Priya", "marks": 38},
    {"name": "Sneha", "marks": 78}
]

print("=== Student Result ===")

for index, student in enumerate(students, start=1):
    name = student.get("name")
    marks = student.get("marks")

    if marks < 50:
        print(f"{index}. {name} - FAIL ({marks}) X")
        continue

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "D"

    print(f"{index}. {name} - Pass | Grade {grade} | Marks {marks}")

score = 90

def calculate_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        
    print(f"The Score is: {score} and Grade is {grade}")

calculate_grade(score)

i = 1
while i <= 10:
    if i == 7:
        # break;
        break
    
    print(f"Numbers: {i}")
    # i++
    i += 1

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 != 0:
        continue
    print(f"Even Numbers {num}")

skills = ["Node.js", "Python", "React", "Java"]

for index, skill in enumerate(skills, start=1):
    print(f"Skill {index} - {skill}")

students = ["Dinesh", "Kumar", "Raj"]

for index, student in enumerate(students):
    print(f"Index: {index} and Student: {student}")
