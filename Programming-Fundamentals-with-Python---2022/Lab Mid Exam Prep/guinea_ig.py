


quantity_food_kilograms = float(input()) * 1000
quantity_hay_kilograms = float(input()) * 1000
quantity_cover_kilograms = float(input()) * 1000
guinea_weight = float(input()) * 1000

its_enough = True

for day in range(1, 31):
    if quantity_food_kilograms < 300:
        its_enough = False
        break
    quantity_food_kilograms -= 300
    if day % 2 == 0:
        if quantity_hay_kilograms < quantity_food_kilograms * 0.05:
            its_enough = False
            break
        else:
            quantity_hay_kilograms -= quantity_food_kilograms * 0.05

    if day % 3 == 0:
        if quantity_cover_kilograms < guinea_weight / 3:
            its_enough = False
            break
        else:
            quantity_cover_kilograms -= guinea_weight / 3


food_left_in_grams = quantity_food_kilograms / 1000
hay_left_in_grams = quantity_hay_kilograms / 1000
cover_left_in_grams = quantity_cover_kilograms / 1000
if its_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_left_in_grams:.2f}, Hay: {hay_left_in_grams:.2f}, Cover: {cover_left_in_grams:.2f}.")
else:
    print("Merry must go to the pet store!")
