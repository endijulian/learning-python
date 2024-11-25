import re


# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# txt = "The rain in Spain"
# x = re.findall("Portugal", txt)
# print(x)

# txt = "The rain in Spain"
# # x = re.split("\s", txt)
# # print(x)

# x = re.split("\s", txt, 1)
# print(x)

# txt = "The rain in spain"
# x = re.sub('\s', "9", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

# print(x.span())
print(x.string)