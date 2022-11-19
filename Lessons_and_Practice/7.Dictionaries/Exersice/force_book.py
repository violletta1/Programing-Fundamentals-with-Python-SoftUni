# If you receive "force_side | force_user":
# If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# Only if there is no such force user in any force side -> add the force user to the corresponding side.
# If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
#If there is such force user already -> change their side.
# If there is no such force user in any force side -> add the force user to the corresponding force side.
# If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# Then you should print on the console: "{force_user} joins the {force_side} side!".

# some_string = input()
# both_side = {}
# while "Lumpawaroo" not in some_string:
#     if "|" in some_string:
#         force_side, force_user = some_string.split(" | ")
#
#         if force_user not in both_side.values() and force_side not in both_side.keys():
#             both_side[force_side] = [force_user]
#
#         elif force_user in both_side.values() is True:
#             both_side[force_side].append(force_user)
#         else:
#             some_string = input()
#             continue
#
#
#     elif "->" in some_string:
#         force_user, force_side = some_string.split(" -> ")
#
#         if force_side not in both_side.keys() and force_user not in both_side.values():
#             both_side[force_side] = [force_user]
#
#         elif force_user in both_side is True:
#             both_side.pop(force_user)#both_side.pop(force_user)
#             both_side[force_side].append(force_user)
#             print(f"{force_user} joins the {force_side} side!")
#         elif force_user in both_side is False:
#             both_side[force_side].append(force_user)
#
#
#
#     some_string = input()
#
# for side, members in both_side.items():
#     print(f"Side: {side}, Members: {len(members)}")
#     for member in members:
#         print(f"! {member}")
force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        user_is_part_of_the_force = False
        for value in force_side_dictionary.values():
            if force_user in value:  # value is list!!!
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = [force_user]
            else:
                force_side_dictionary[force_side].append(force_user)
    elif "->" in command:  # else
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_side_dictionary.items():
            if force_user in value:  # value is list!!!
                force_side_dictionary[key].pop(value.index(force_user))
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = [force_user]
        else:
            force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")
        # [print(f"! {user}") for user in force_side_dictionary[force_side]]