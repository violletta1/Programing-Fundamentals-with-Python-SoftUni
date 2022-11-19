# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command "statistics".
# Sometimes you may receive a product more than once. In that case, you have to add the new quantity to the existing one.
# When you receive the "statistics" command, print the following:
# "Products in stock:
# - {product1}: {quantity1}
# - {product2}: {quantity2}
# …
# - {productN}: {quantityN}
# Total Products: {count_all_products}
# Total Quantity: {sum_all_quantities}"


command = input()
grocery = {}

while not command == "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product in grocery.keys():
        grocery[product] += quantity
    else:
        grocery[product] = quantity

    command = input()

print("Products in stock:")

for (product, quantity) in grocery.items():#минаваме през всеки елемент в речника
    print(f"- {product}: {quantity}")#принтираме елемента

count_all_products = len(grocery.keys())
sum_all_quantities = sum(grocery.values())

print(f"Total Products: {count_all_products}")
print(f"Total Quantity: {sum_all_quantities}")