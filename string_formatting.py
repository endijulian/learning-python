# txt = f"The pricen is 59 dollars"
# print(txt)

# price = 59
# tax = 0.25
# txt = f"The price is {price} dollars"
# txt = f"The price is {price:.2f} dollars"
# txt = f"The price is {95:.2f} dollars"
# txt = f"The price is {20 * 59} dollars"
# txt = f"The price is {price + (price * tax)} dollars"


# price = 49
# txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"


# fruit = "apples"
# txt = f"I love {fruit.upper()}"

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(3000)} meter altitude"
print(txt)