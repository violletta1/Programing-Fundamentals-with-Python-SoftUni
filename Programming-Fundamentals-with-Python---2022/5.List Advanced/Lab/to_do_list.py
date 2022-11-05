


to_do_list = input()
all_task = [0] * 10
while to_do_list != "End":
    importance, task = to_do_list.split("-")
    importance = int(importance) - 1
    all_task.insert(importance, task)

    to_do_list = input()


print([task for task in all_task if task != 0])

# todo_list = input()
# task_all = []
#
# while todo_list != "End":
#     importance, task = todo_list.split("-")
#     importance = int(importance)
#     task_all.append([importance, task])
#     todo_list = input()
#
# sorted_task = []
# for task in sorted(task_all):
#     sorted_task.append(task[1])
#
# print(sorted_task)