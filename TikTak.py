failed = [" ", " ", " ",
          " ", " ", " ",
          " ", " ", " "]
move = 2
win_x = False
win_O = False
game = True
place = 0

try:
    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
except:
    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))


def count_pl():
    global column, row, place
    if row == 2 and column == 1:
        place = row * column * 2
    elif row == 2 and column == 2:
        place = row * column + 1
    elif row == 3 and column == 1:
        place = row * column * 2 + 1
    elif row == 3 and column == 2:
        place = row * column + 2
    else:
        place = row * column
count_pl()


while game:
    if move % 2 == 0:
        for i in range(1, 10):
            if place == i and failed[i-1] == " ":
                failed[i-1] = "O"
                print(f" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      f"———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      f"———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      f"———————\n",
                      )
                if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                    or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                    or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                    print("X wins")
                    game = False
                elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                    print("O wins")
                    game = False
                elif(failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                    print("Draw")
                    game = False
                else:
                    move += 1
                    print("Move X")
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
            elif place == i and failed[i - 1] != " ":
                print("Invalid")
                print("Move 0")
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        count_pl()
    elif move % 2 != 0:
        for i in range(1, 10):
            if place == i and failed[i - 1] == " ":
                failed[i - 1] = "X"
                print(f" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      f"———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      f"———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      f"———————\n",
                      )
                if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                        or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                        or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                    print("X wins")
                    game = False
                elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                    print("O wins")
                    game = False
                elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4]
                      and failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                    print("Draw")
                    game = False
                else:
                    move += 1
                    print("Move O")
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
            elif place == i and failed[i - 1] != " ":
                print("Invalid")
                print("Move X")
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        count_pl()
