min_salary = 400
dop_salary = 20
dop_child = 30
years = int(input('Work years: '))
children = int(input('Number of child: '))
missing_days = int(input('Missing days: '))
dop_years = years*dop_salary
dop_children = dop_child*children
full_salary = min_salary+dop_years+dop_children
template = 'The total amount is {full_salary}$. 400$ minimum wage, {dop_years}$ for {years} years experience, {dop_children}$ for {children} kids, {dop_missing_days}$ for {missing_days} missing a day at work'
if missing_days == 0:
    full_salary = full_salary+100
    dop_missing_days = 100
    print(template.format(full_salary=full_salary, dop_years=dop_years,years=years, dop_children=dop_children, children=children, dop_missing_days=dop_missing_days, missing_days=missing_days))
else:
    dop_missing_days = 0
    print(template.format(full_salary=full_salary, dop_years=dop_years, years=years, dop_children=dop_children, children=children, dop_missing_days=dop_missing_days, missing_days=missing_days))

