board_width = 20
board_height = 10


for row in range(board_height):
    print()
    for column in range(board_width):
        if column == 2:
            print("#", end="")
        else:
            print(".", end="")
