names = []
salaries = []
while True:
    name = input("Enter name: ")
    names.append(name)
    salary = int(input("Enter Salary: "))
    salaries.append(salary)
    do_continue = input('Continue? y/n: ')
    if do_continue == 'n':
        break
ave_salary = sum(salaries)/len(names)
print("The average salary is", ave_salary,'$')

for name, salary in zip(names, salaries):



i=0
#b=0
while i<len(salaries):
    if salaries[i] < ave_salary:
        print(names[i],'salary is below average')
        to_delete.append((name, salary))
    else:
        print(names[i],'salary is above averag')
        #b+=1
    i += 1
#print('Total Employees: ', len(names)-b)

to_delete = []
for name in to_delete:
    i = names.index(name)
    if salary=
    del names[i]
    del salaries[i]

print(f"Total Employees: {len(names)}")