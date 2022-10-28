import math
budget = float(input())
students = int(input())
price_for_flour = float(input())
price_for_one_egg = float(input())
price_for_one_apron = float(input())


total_price = 0
needed_money = 0
free_flour = 0
for student in range(1, students + 1):
    if student % 5 == 0:
        free_flour += 1

apron_price = price_for_one_apron * math.ceil(students * 0.2 + students)
egg_price = price_for_one_egg * 10 * students
flour_price = price_for_flour * (students - free_flour)
total_price = apron_price + egg_price + flour_price
diff = abs(total_price - budget)

if budget >= total_price:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")