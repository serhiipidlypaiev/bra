from importlib.resources import read_text
import json
import os.path
import os
import pprint
import pathlib

PERSONAL_CARD = {}


def add_new_entries():
    name = input("Please write your name: ")
    surname = input("Please write your surname: ")
    phone_number = input("Please write your number: ")
    city = input("Please write your city: ")
    state = input("Please write your state: ")
    PERSONAL_CARD[name + "_" + surname] = {
        "full_name": name + " " + surname,
        "first name": name,
        "second_name": surname,
        "telephone_number": phone_number,
        "city": city,
        "state": state,
    }


def search():
    search_value = input("Please write what do you want to find: ")
    for key in PERSONAL_CARD.values():
        for input_key in key.values():
            if input_key == search_value:
                return key


def delete():
    search_value = input("Please write what do you want to find for delete: ")
    for key in PERSONAL_CARD.values():
        for input_key in key.values():
            if input_key == search_value:
                print(key)
        delete_value = input("Please write value that you want delete: ")
        key.pop(delete_value)
        print(key)


def update():
    search_value = input("Please write what do you want to find and update: ")
    for key in PERSONAL_CARD.values():
        for input_key in key.values():
            if input_key == search_value:
                print(key)
        update_value = input("Please write value what you want update: ")
        new_value = input("Please write new value: ")
        key[update_value] = new_value
        print(key)


if os.path.exists("person_card.json") == False:
    print("file_exists")
elif (
    os.path.exists("person_card.json") == True
    and os.stat("person_card.json").st_size == 0
):
    add_new_entries()
else:
    with open("person_card.json") as file_object:
        PERSONAL_CARD = json.load(file_object)

action = input(
    "What do you want to do?\n"
    "Add new entries? number 1\n"
    "Search by first name, last name,\n"
    "by full name, elephone number\n"
    "by city or state? number 2\n"
    "Delete a record? number 3\n"
    "Update a record? number 4\n"
    "Exit the program? number 9\n"
    "Your choise: "
)

if action == "1":
    add_new_entries()
elif action == "2":
    search()
elif action == "3":
    delete()
elif action == "4":
    update()
elif action == "9":
    print("Exit")

pprint.pprint(PERSONAL_CARD)

with open("person_card.json", "w") as file_object:
    json.dump(PERSONAL_CARD, file_object)
