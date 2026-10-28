name = input("What's your name? ")

# if name == "Harry":
#   print("Gryffindor")
# elif name == "Ron":
#   print("Gryffindor")
# elif name == "Hermiona":
#   print("Gryffindor")
# elif name == "Draco":
#   print("Slytherin")
# else:
#   print("Who?")

match name:
  case "Harry" | "Ron" | "Hermiona":
    print("Gryffindor")
  case "Draco":
    print("Slytherin")
  case _:
    print("Who?")