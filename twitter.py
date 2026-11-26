import re

url = input("URL: ").strip()

# username = url.replace("https://twitter.com/", "")

# print(f"Username: {username}")



# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# print(f"Username: {username}")


matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url)

if matches:
  print("Username: ",matches.group(1))