number = int(input())

prime_num = False

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("False")
            break
    else:
        prime_num = True

if prime_num:
    print("True")