# ⦁	coffee - 1.50
# ⦁	water - 1.00
# ⦁	coke - 1.40
# ⦁	snacks - 2.00



def price_of_all(order: str, num: int):
    price = 0

    if order == "coffee":
        price = 1.50
    elif order == "water":
        price = 1.00
    elif order == "coke":
        price = 1.40
    elif order == "snacks":
        price = 2.00
    return f"{price * num:.2f}"



product = input()
quantity = int(input())

print(price_of_all(product, quantity))
# ##
# cost = price_of_all(product, quantity)
# print(f"{cost:.2f}")
# print(price_of_all(product, quantity))