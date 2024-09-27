# 1. task

dictionary = {
    "name" : "v3nCll",
    "birth place" : "Zedcountry",
    "favourite_rantotthus" : "bighungary"
}
empty_dict = dict()

print(dictionary)
print(empty_dict)

#2. task

dictionary1 = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5
}
for dict_key, dict_value in numbers.items():
    if dict_key %2 == 0:
        print(dict_key, " :", dict_value)

#3. task

empty_d = dict()
for i in range(1, 11):
    empty_d[i] = i**2
print(empty_d)

#4. task

n = int(input("give me a number: "))
empty_d = dict()
for i in range(n, n+1):
    empty_d[i] = i**2
print(empty_d)

#5. task

d = {
    "data1": 2,
    "data2": 3,
    "data3": 4,
    "data4": 5,
    "data5": 6
}
equal = 1
for key in d:
    equal = equal *d[key]
print(equal)

#6. task

d = {
    "x": 762,
    "y": 821,
    "z": 321
}

print("smallest number: ", min(d.values()))
print("biggest number: ", max(d.values()))

#7. task

people = dict()
while True:
    person = input("What is the name of the next person?\n")
    if person == "":
        break
    else:
        person_attributes = []
        age = int(input("How old is " + person + "?\n"))
        gender = input("What is " + person + "'s gender?\n")
        job = input("What is " + person + "'s job?\n")
        person_attributes.append(age)
        person_attributes.append(gender)
        person_attributes.append(job)
        people[person] = person_attributes

for person in people.keys():
    print(person, ": ", people[person])

#8. task

d = {
    "Math" : 80,
    "physics" : 70,
    "English" : 90
}
keys = list(d)
print(keys)

#9. task

d = dict()
if len(d) == 0:
    print("Empity")
else:
    print("Not empity")

#9+1 task

import pprint
diak_info = {
    "id1": {"name": ["Sara"], "class": ["B"], "Subject_interogation": ["English, Math, Science"]},
    "id2": {"name": ["John"], "class": ["A"], "Subject_interogation": ["English, Math, Science"]},
    "id3": {"name": ["Sara"], "class": ["B"], "Subject_interogation": ["English, Math, Science"]},
    "id4": {"name": ["Mathev"], "class": ["C"], "Subject_interogation": ["English, Math, Science"]},
}
pprint.pprint(diak_info)

#9+1+1 task

import pprint
diak_info = {
    "id1": {"name": ["Sara"], "class": ["B"], "Subject_interogation": ["English, Math, Science"]},
    "id2": {"name": ["John"], "class": ["A"], "Subject_interogation": ["English, Math, Science"]},
    "id3": {"name": ["Sara"], "class": ["B"], "Subject_interogation": ["English, Math, Science"]},
    "id4": {"name": ["Mathev"], "class": ["C"], "Subject_interogation": ["English, Math, Science"]},
}
eredmeny = {}
for key, value in diak_info.items():
    if value not in eredmeny.values():
        eredmeny[key] = value
diak_info = eredmeny
pprint.pprint(diak_info)