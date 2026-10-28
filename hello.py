# Ask user for their name
# name = input("What is your name? ").strip().title()

# Split name
# firstName, lastName = name.split(" ")

# Say hello to user
# print(f"""Hello, {firstName}""")


def main():
  name = input("What is your name? ").strip().title()
  hello(name)

def hello(to="world"):
  print(f"Hello {to}")

main()