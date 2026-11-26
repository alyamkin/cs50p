import re

email = input("What's your email? ")

# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else:
  print("Invalid")