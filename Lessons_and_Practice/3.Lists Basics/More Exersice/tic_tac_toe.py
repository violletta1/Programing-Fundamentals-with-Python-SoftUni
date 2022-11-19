line_1 = input().split(" ")
line_2 = input().split(" ")
line_3 = input().split(" ")
list_game = line_1 + line_2 + line_3
first = list_game.count("1")
second = list_game.count("2")


def the_winner():

    if first > second:
        return "First player won"
    elif second > first:
        return "Second player won"
    else:
        return "Draw!"


print(the_winner())