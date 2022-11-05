# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
# ⦁	If you have the product, print "We have {quantity} of {product} left".
# ⦁	Otherwise, print "Sorry, we don't have {product}".
grocery = input().split() # създаваме списък от дадения вход и го разделяме по празно място
# print(grocery)
wanted_products = input().split()
bakery = {} # създаваме празен речник

for index in range(0, len(grocery), 2): # преминаваме през веки ВТОРИ елемент (със стъпка 2)от списъка
    food = grocery[index] # задаваме стойност на ключа
    quantity = grocery[index + 1] # посоваме кой елемент заема място на стойнот към ключ от предходен индекс
    bakery[food] = int(quantity) # обузнаваме съдействие мейду клуч и стйност

for product in wanted_products: #проверяваме всеки елемент от списъкА
    if product in bakery.keys():# ако дадения елемент е в речника
        print(f"We have {bakery[product]} of {product} left")# bakery[product] ст-ста на елемента заема място на ключ и чрез него взимаме ст-ста която стои към този ключ
    else:
        print(f"Sorry, we don't have {product}")#