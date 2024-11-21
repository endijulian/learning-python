# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict["model"]
# x = thisdict.get("model")
# print(x)

# Get Keys
# x = thisdict.keys()
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()
# print(x)

# car["color"] = "white"
# print(x)

# Get Values
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()
# print(x)

# # car["year"] = 2020
# car["color"] = "red"
# print(x)

# Get Items
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()
# print(x)

# car["color"] = "red"
# print(x)

# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is a key in the dictionary")