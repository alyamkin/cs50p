# name = input("What's your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

def write_names_to_file(file_name):
  name = input("What's your name? ")
  with open(file_name, "a") as file:
    file.write(f"{name}\n")


def read_names_from_file(file_name):
  names = []
  with open(file_name, "r") as file:
    for line in file:
      names.append(line.rstrip())
  return names

def print_sorted_names():
  names = read_names_from_file("names.txt")
  for name in sorted(names):
    print(f"hello, {name}")

print_sorted_names()