students=[
    {"name":"Hermione","house":"Griffindor","patronous":"Otter"},
    {"name":"Harry","house":"Griffindor","patronous":"Stag"},
    {"name":"Ron","house":"Griffindor","patronous":"Jack Russel terrier"},
    {"name":"Draco","house":"Slytherin","patronous":None},
]

for student in students:
    print(student["name"],student["house"],student["patronous"],sep=", ")