from faker import Faker


EMPLOYEES_PER_DEPARTMENT = {
    "devops": 4,
    "backend": 7,
    "frontend": 6,
}

DEPARTMENTS = {key: [] for key in EMPLOYEES_PER_DEPARTMENT}

fake = Faker()

for department, employees_qt in EMPLOYEES_PER_DEPARTMENT.items():
    for i in range(employees_qt):
        DEPARTMENTS[department].append(
            {
                "name": fake.name(),
                "birthdate": fake.date(),
            }
        )

print(DEPARTMENTS)