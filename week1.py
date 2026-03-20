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


