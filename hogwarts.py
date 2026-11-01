# list

# students = ["Hermione", "Ron", "Harry"]

# for student in students:
#   print(student)

# Dictionaries

# students = {
#   "Hermione": "Gryffindore",
#   "Harry": "Gryffindore",
#   "Ron": "Gryffindore",
#   "Draco": "Slytherin"
# }

# for student in students:
#   print(student, students[student], sep=", ")


students = [
  {"name": "Hermione", "house": "Gryffindore", "patronus": "Otter"},
  {"name": "Harry", "house": "Gryffindore", "patronus": "Stag"},
  {"name": "Ron", "house": "Gryffindore", "patronus": "Jack Russel terrier"},
  {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
  print(student["name"], student["house"], student["patronus"], sep=", ")