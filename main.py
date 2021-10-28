import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint # query

response = requests.get(url)
breeds = response.json()["message"]

# get a list of all breeds from API call
all_breeds = breeds.keys()

# loop and print out each key

for breed in all_breeds:
  print(breed)

# Get a list of all subbreeds w at least 3 sub-breeds
# but NOT bulldogs
# Examples include: poodles, spaniels, retrievers, terriers, mastiffs, setters exit

#Display all poodle subbreeds
poodle_subbreeds = breeds["poodle"]
input("\nPress enter to get all poodle subbreeds")
for sub in poodle_subbreeds:
  print(sub)