
#
# def tribonacci_sequence(num_digits):
#     sequence = [1]
#     for i in range(1, num_digits):
#         if len(sequence) < 3:
#             sequence.append(i)
#         else:
#             sequence.append(sum(sequence[-3:]))
#     return ' '.join(str(x) for x in sequence)
#
#
# number = int(input())
# result = tribonacci_sequence(number)
# print(result)

#

def tribonacci_sequence(times_of_sequence):
    sequence = [1]
    for i in range(1, times_of_sequence):
        if len(sequence) < 3:
            sequence.append(i)
        else:
            sequence.append(sum(sequence[-3:]))
    return sequence


number = int(input())
result = tribonacci_sequence(number)
print(*result)
