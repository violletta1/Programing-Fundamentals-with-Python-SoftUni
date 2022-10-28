def inventory_func(items):
    while True:
        command_data = input()

        if command_data == "Craft!":
            break

        command, item = command_data.split(' - ')

        if command == 'Collect':
            if item not in items:
                items.append(item)

        elif command == 'Drop':
            if item in items:
                items.remove(item)

        elif command == 'Combine Items':
            old_item, new_item = item.split(':')
            if old_item in items:
                old_item_index = items.index(old_item)
                items.insert(old_item_index + 1, new_item)

        elif command == 'Renew':
            if item in items:
                items.remove(item)
                items.append(item)

    return ', '.join(items)


data = input().split(', ')
result = inventory_func(data)
print(result)