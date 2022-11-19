happiness_rate_list = list(map(int, input().split(" ")))
multiply_factor = int(input())

multiply_rate = list(map(lambda x: x * multiply_factor, happiness_rate_list))
average = sum(multiply_rate) // len(multiply_rate)

filtered_happy = list(filter(lambda x: x > average, multiply_rate))


if len(filtered_happy) >= len(multiply_rate) / 2:
    print(f"Score: {len(filtered_happy)}/{len(multiply_rate)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happy)}/{len(multiply_rate)}. Employees are not happy!")
