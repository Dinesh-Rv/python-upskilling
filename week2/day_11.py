from pydantic import BaseModel, field_validator
from typing import List

class Employee(BaseModel):
    id: int
    name: str
    email: str
    salary: float
    department: str
    is_active: bool = True

    # @validator(salary)
    @field_validator("salary")
    @classmethod
    def validate_salary(cls, salary):
        if salary <= 0:
            raise ValueError("Salary must be positive!")
        return salary

    # @validator(name)
    @field_validator("name")
    @classmethod
    def validate_name(cls, name):
        # if name != None or name == "":
        if name.strip() == "":
            raise ValueError("Name must not be Empty!")
        return name

    # @validator(email)
    @field_validator("email")
    @classmethod
    def validate_email(cls, email):
        # if not email.contains("@"):
        if "@" not in email:
            raise ValueError("Email must contain @")
        return email
        
class Company(BaseModel):
    name: str
    location: str
    employees: List[Employee]


employee_1 = Employee(id=1, name="Dinesh", email="dinesh1@gmail.com", salary=50000, department="Development", is_active=True)
employee_2 = Employee(id=2, name="Kumar", email="kumar950@yahoo.com", salary=20000, department="Testing", is_active=True)
employee_3 = Employee(id=3, name="Sanjay", email="samjay@yopmail.com", salary=20000, department="Finance", is_active=True)

new_company = Company(name="Ideas2IT", location="India", employees=[employee_1, employee_2, employee_3])

# new_company.employees.append(employee_1, employee_2, employee_3)
# new_company.employees.extend([employee_1, employee_2, employee_3])

for employee in new_company.employees:
    print(employee)

try: 
    employee_4 = Employee( 
        id = 4,
        name= "",
        email= "vijay.com",
        salary= -10000,
        department= "Development"
        )
# catch e:
except Exception as e:
    print(f"Validation Error: {e}")

# employee_dict = employee_1.dict()
print("===Employee Dict===")
employee_dict = employee_1.model_dump()
print(employee_dict)

print("===Employee Json===")
# employee_json = employee_1.json()
employee_json = employee_1.model_dump_json()
print(employee_json)

