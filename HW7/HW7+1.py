DEPARTMENTS = {
    "devops": [
        {
            "name": "Mary Hodges",
            "birthdate": "2005-03-12",
        },
        {
            "name": "Robert Jones",
            "birthdate": "1995-12-19",
        },
        {
            "name": "Nancy Peterson",
            "birthdate": "1999-03-27",
        },
        {
            "name": "Michaela Wilkins",
            "birthdate": "2001-12-17",
        },
    ],
    "backend": [
        {
            "name": "Jason Jacobs",
            "birthdate": "1971-08-24",
        },
        {
            "name": "Julia Jenkins",
            "birthdate": "1994-07-26",
        },
        {
            "name": "Lisa Mcgrath",
            "birthdate": "2000-07-05",
        },
        {
            "name": "Dawn Farmer",
            "birthdate": "1983-01-21",
        },
        {
            "name": "Adam Walton",
            "birthdate": "2003-08-22",
        },
        {
            "name": "James Sanchez",
            "birthdate": "1984-07-01",
        },
        {
            "name": "Danielle Smith",
            "birthdate": "1976-10-06",
        },
    ],
    "frontend": [
        {
            "name": "Alexandra Willis",
            "birthdate": "1994-06-17",
        },
        {
            "name": "Patrick Mccormick",
            "birthdate": "2005-07-16",
        },
        {
            "name": "Alexis Lane",
            "birthdate": "1982-03-06",
        },
        {
            "name": "Rachel Allen",
            "birthdate": "1999-11-30",
        },
        {
            "name": "Leslie Anderson",
            "birthdate": "1979-08-18",
        },
        {
            "name": "Patricia Salazar",
            "birthdate": "2000-12-10",
        },
    ],
}

DEPARTMENTS_LIST = []
for keys in DEPARTMENTS:
    for i in range(len(DEPARTMENTS.get(keys))):
        name_birthdate = ((DEPARTMENTS.get(keys)[i]).get('name')).split(" ")
        birthdate = (DEPARTMENTS.get(keys)[i]).get('birthdate')
        DEPARTMENTS_LIST.append({"First name": name_birthdate[0], 
                                 "Second Name": name_birthdate[1], 
                                 "birthdate": birthdate, "Department":keys})
print(DEPARTMENTS_LIST)
"""all from new line"""
# for i in range(len(DEPARTMENTS_LIST)):
#    for k, v in DEPARTMENTS_LIST[i].items():
#        print(k, '-->', v)
