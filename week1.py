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

# --- Day 5 ---

from typing import Optional

def calculate_bonus(
    name: str,
    salary: float,
    performance: str = "average"
) -> Optional[float]:
    bonus_rates = {
        "excellent": 0.20,
        "good": 0.15,
        "average": 0.10,
        "poor": None 
    }

    rate = bonus_rates.get(performance)

    if rate is None:
        print(f"{name} is not eligible for bonus")
        return None
    
    bonus = salary * rate
    return bonus

print(calculate_bonus("Dinesh", 40000))
print(calculate_bonus("Kumar", 50000, "excellent"))
print(calculate_bonus(name="Raj", salary=60000, performance="good"))

def calculate_tax (
    salary: float,
    rate: float = 0.1,
):
    return salary * rate

print(calculate_tax(50000))           
print(calculate_tax(50000, 0.2))     

def student_summary( name, *subjects, **details):
    print(name)
    for subject in subjects:
        # print(subject);
        print(subject)

    for key, value in details.items():
        print(f"{key} : {value}")

student_summary(
    "Dinesh",
    "Python", "Node.js", "React",
    age=24, city="Coimbatore"
)

def countdown(num):
    # if num == 1:
    #     return 1
    
    # return num, countdown(num - 1)
    if num == 0:
        return
    print(num)
    countdown(num-1)

countdown(7)

# square = lamda x: x ** 2
square = lambda x: x**2
print(square(5))

numbers = [5, 2, 8, 1, 9, 3]

# numbers_sorted = sorted(numbers, descending)
numbers_sorted = sorted(numbers, reverse=True)
print(numbers_sorted)

app_name= "application"

def modify_global():
    app_name = "cation"

def modify_global_valid():
    global app_name
    app_name = "appli"

print(f"Before: {app_name}")

modify_global()
print(f"After modify_global: {app_name}")

modify_global_valid()
print(f"After modify_global_valid: {app_name}")

# --- Day 6 ---

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n ** 2 for n in numbers]

# print(numbers)
print(squares)

employees = [
    {"name": "Dinesh", "salary": 50000},
    {"name": "Kumar",  "salary": 60000},
    {"name": "Raj",    "salary": 45000},
    {"name": "Priya",  "salary": 75000}
]

names_salary = [emp["name"] for emp in employees if emp["salary"] > 50000]

print(names_salary)

employee_dict = { emp["name"]: emp["salary"] for emp in employees }
print(employee_dict)

names = ["Dinesh", "David", "Kumar", "Kiran", "Raj"]
unique_letter = {name[0] for name in names}
print(unique_letter)

square_gen = (i**2 for i in range(1,6))

for num in square_gen:
    print(f"First Loop: {num}")

for num2 in square_gen:
    print(f"Second loop: {num2}")