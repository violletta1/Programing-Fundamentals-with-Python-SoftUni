# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for index in range(len(version) - 1, -1, -1):
#     if version[index] > 9:
#         version[index] = 0
#         if index - 1 >= 0:
#             version[index - 1] += 1
# print('.'.join(str(number) for number in version))


current_version = [int(number) for number in input().split(".")]
current_version[-1] += 1
for index_num in range(len(current_version)-1, -1, -1):
    if current_version[index_num] > 9:
        current_version[index_num] = 0
        current_version[index_num - 1] += 1
print(".".join([str(number) for number in current_version]))
