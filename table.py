import pandas as pd

ROWS = ["A", "B", "C"]
COLUMNS = [1, 2, 3]
ALLOWED_CELLS = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]


class Game:

    def __init__(self):

        self.df = pd.DataFrame([["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]], columns=COLUMNS,
                               index=ROWS)
        print("Welcome to Tic Tac Toe.")
        print(self.df)

    def make_move_x(self):

        global selected_row, selected_col
        input_correct = False
        print("X turn. Please enter a row and column e.g. 'B2': ")
        while not input_correct:
            row_and_col = input().upper()
            if (row_and_col in ALLOWED_CELLS) and (self.df.loc[row_and_col[0]][int(row_and_col[1])] != "X") \
                    and (self.df.loc[row_and_col[0]][int(row_and_col[1])] != "O"):
                selected_row = row_and_col[0]
                selected_col = int(row_and_col[1])
                input_correct = True
            elif row_and_col not in ALLOWED_CELLS:
                print("Incorrect input. X turn. Please enter a row and column e.g. 'B2': ")
            else:
                print("The cell is occupied. X turn. Please enter a row and column e.g. 'B2': ")

        self.df.loc[selected_row][selected_col] = "X"
        print(self.df)

    def make_move_o(self):

        global selected_row, selected_col
        input_correct = False
        print("O turn. Please enter a row and column e.g. 'B2': ")
        while not input_correct:
            row_and_col = input().upper()
            if (row_and_col in ALLOWED_CELLS) and (self.df.loc[row_and_col[0]][int(row_and_col[1])] != "X") \
                    and (self.df.loc[row_and_col[0]][int(row_and_col[1])] != "O"):
                selected_row = row_and_col[0]
                selected_col = int(row_and_col[1])
                input_correct = True
            elif row_and_col not in ALLOWED_CELLS:
                print("Incorrect input. O turn. Please enter a row and column e.g. 'B2': ")
            else:
                print("The cell is occupied. O turn. Please enter a row and column e.g. 'B2': ")

        self.df.loc[selected_row][selected_col] = "O"
        print(self.df)

    def is_game_over(self):

        x_wins = False
        y_wins = False
        draw = False
        blanks_left = 0

        for row in range(3):  # check for 3 in line in rows
            y_in_line = 0
            x_in_line = 0
            for column in range(3):
                value = self.df.iloc[row, column]
                if value == "X":
                    x_in_line += 1
                elif value == "O":
                    y_in_line += 1
                if x_in_line == 3:
                    x_wins = True
                    break
                elif y_in_line == 3:
                    y_wins = True
                    break

        if not x_wins and not y_wins:
            for column in range(3):  # check for 3 in line in columns
                y_in_line = 0
                x_in_line = 0
                for row in range(3):
                    value = self.df.iloc[row, column]
                    if value == "X":
                        x_in_line += 1
                    elif value == "O":
                        y_in_line += 1
                    if x_in_line == 3:
                        x_wins = True
                        break
                    elif y_in_line == 3:
                        y_wins = True
                        break

        if not x_wins and not y_wins:  # check for 3 in line diagonally
            if (self.df.loc["A"][1] == "X" and self.df.loc["B"][2] == "X" and self.df.loc["C"][3] == "X") or \
                    (self.df.loc["A"][3] == "X" and self.df.loc["B"][2] == "X" and self.df.loc["C"][1] == "X"):
                x_wins = True
            elif (self.df.loc["A"][1] == "O" and self.df.loc["B"][2] == "O" and self.df.loc["C"][3] == "O") or \
                    (self.df.loc["A"][3] == "O" and self.df.loc["B"][2] == "O" and self.df.loc["C"][1] == "O"):
                y_wins = True

        if not x_wins and not y_wins:
            for ROWS, row in self.df.iterrows():  # check for draw and blanks left
                for COLUMNS, value in row.items():
                    if value == "_":
                        blanks_left += 1
            if blanks_left == 0:
                draw = True

        if x_wins:
            return 1
        elif y_wins:
            return 2
        elif draw:
            return 3
        else:
            return 0
