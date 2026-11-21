# students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     students.append(
#       {
#         "name": name,
#         "house": house
#       }
#     )

# def get_name(student):
#   return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in {student['house']}")

# csv library
# import csv
# students = []

# with open("students.csv") as file:
#   reader = csv.reader(file)
#   for name, house in reader:
#     students.append({
#       "name": name,
#       "house": house
#     })

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in {student['house']}")

# DictReader
# import csv
# students = []

# with open("students.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({
#       "name": row["name"],
#       "house": row["house"]
#     })

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in {student['house']}")

# Write csv
import csv

name = input("What's your name? ")
house = input("What's your house? ")

with open("students.csv", "a") as file:
  writer = csv.writer(file)
  writer.writerow([name, house])