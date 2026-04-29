import csv
import re
import logging
from pathlib import Path

# Logging Setup
logger = logging.getLogger("employee_processor")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
console.setFormatter(formatter)
logger.addHandler(console)


# Regex Pattern
email_pattern = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)
phone_pattern = re.compile(r"^[6-9]\d{9}$")


def validate_employees(input_file, valid_file, invalid_file):
    logger.info(f"Starting Validation of {input_file}")

    valid_rows = []
    invalid_rows = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            errors = []

            if not email_pattern.match(row["email"].strip()):
                errors.append(f"Invalid email: {row['email']}")
                logger.warning(f"{row['name']} — invalid email!")

            # Validate phone
            if not phone_pattern.match(row["phone"].strip()):
                errors.append(f"Invalid phone: {row['phone']}")
                logger.warning(f"{row['name']} — invalid phone!")

            # Validate salary
            try:
                salary = float(row["salary"])
                if salary <= 0:
                    errors.append(f"Invalid salary: {row['salary']}")
                    logger.warning(f"{row['name']} — invalid salary!")
            except ValueError:
                errors.append(f"Salary not a number: {row['salary']}")
                logger.warning(f"{row['name']} — salary not a number!")

            if errors:
                row["errors"] = " | ".join(errors)
                invalid_rows.append(row)
                logger.debug(f"{row['name']} -> INVALID")
            else:
                valid_rows.append(row)
                logger.debug(f"{row['name']} -> VALID")

    with open(valid_file, "w", newline="") as f:
        fieldnames = ["name", "email", "phone", "salary", "department"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_rows)
    logger.info(f"Written {len(valid_rows)} valid employees to {valid_file}")

    with open(invalid_file, "w", newline="") as f:
        fieldnames = ["name", "email", "phone", "salary", "department", "errors"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(invalid_rows)
    logger.info(f"Written {len(invalid_rows)} Invalid employees to {invalid_file}")

    return valid_rows, invalid_rows

def generate_report(valid_file, report_file):
    logger.info(f"Generating report from {valid_file}")

    employees = []
    with open(valid_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            employees.append(row)

    if not employees:
        logger.warning("No valid employees found!")
        return

    salaries = [float(emp["salary"]) for emp in employees]
    total = sum(salaries)
    highest = max(employees, key=lambda x: float(x["salary"]))
    lowest = min(employees, key=lambda x: float(x["salary"]))

    report_content = f"""
====================================
    EMPLOYEE SALARY REPORT
====================================
Total Employees  : {len(employees)}
Total Salary Bill: Rs.{total:,.2f}
Average Salary   : Rs.{total/len(employees):,.2f}

Highest Paid:
  Name       : {highest['name']}
  Department : {highest['department']}
  Salary     : Rs.{float(highest['salary']):,.2f}

Lowest Paid:
  Name       : {lowest['name']}
  Department : {lowest['department']}
  Salary     : Rs.{float(lowest['salary']):,.2f}

====================================
Employee Breakdown:
====================================
"""
    for emp in employees:
        report_content += f"{emp['name']:<15} {emp['department']:<10} Rs.{float(emp['salary']):>10,.2f}\n"

    Path(report_file).write_text(report_content)
    logger.info(f"Report written to {report_file}")
    print(report_content)

if __name__ == "__main__":
    print("=== Starting emp ===\n")

    valid, invalid = validate_employees(
        "employees.csv",
        "valid_employees.csv",
        "invalid_employees.csv"
    )

    print(f"\nValid: {len(valid)} | Invalid: {len(invalid)}\n")

    generate_report("valid_employees.csv", "report.txt")