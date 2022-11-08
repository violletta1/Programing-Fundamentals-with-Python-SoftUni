# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# If the product doesn't exist yet, add it with its starting quantity.
# If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items.
# Finally, print all items with their names and the total price of each product.
# Input
# Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# The product data is always delimited by a single space.
# Output
# Print information about each product in the following format:
# "{product_name} -> {total_price}"
# Format the total price to the 2nd digit after the decimal separator.
command = input().split(" ")
product_price = {}
product_quantity = {}
while "buy" not in command:
    name = command[0]
    prices = float(command[1])
    quantities = int(command[2])


    if name not in product_price.keys():
        product_quantity[name] = 0
        product_price[name] = 0.00
    product_quantity[name] += quantities
    product_price[name] = prices
    command = input().split(" ")

for name, prices in product_price.items():
    price = prices * product_quantity[name]
    print(f"{name} -> {price:.2f}")


# line = input().split(" ")
# productQuantity = {}
# productPrices = {}
#
# while "buy" not in line:
#     product = line[0]
#     price = float(line[1])
#     quantity = int(line[2])
#
#     if product not in productQuantity.keys():
#         productQuantity[product] = 0
#         productPrices[product] = 0.00
#     productQuantity[product] += quantity
#     productPrices[product] = price
#     line = input().split(" ")
#
#     if "buy" in line:
#         break
#
# for key, value in productQuantity.items():
#     price = value * productPrices[key]
#     print(f"{key} -> {price:.2f}")