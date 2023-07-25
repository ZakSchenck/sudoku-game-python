class Sudoku:
    def __init__(self):
        self.board = [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]
        ]

        self.is_game_running = True
        self.valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win_check_num = 0

    # Print board in terminal
    def print_board(self):
        # Prints each array values on a separate line
        for row in self.board:
            print(f" {' | '.join(str(value) for value in row)}")

    # Logic to change board number 
    def update_board_number(self, get_y_coordinate, get_x_coordinate):
        if self.board[int(get_y_coordinate) - 1][int(get_x_coordinate) - 1] == 0:
            number_change = input("Enter what number you want to change: ")
            while int(number_change) not in self.valid_numbers:
                number_change = input(
                    "Need numbers 1 through 9. Enter what number you want to change: ")
            self.board[int(get_y_coordinate) -
                           1][int(get_x_coordinate) - 1] = int(number_change)
            self.print_board()

            self.check_if_win()

        else:
            print("Not a valid coordinate to change")


    # User input and game setup logic
    def start_game(self):
        self.print_board()

        while self.is_game_running:
            get_y_coordinate = input(
                "Enter your Y Coordinate to change (1-9): ")
            print(get_y_coordinate)
            get_x_coordinate = input(
                "Enter your X Coordinate to change (1-9): ")
            print(get_x_coordinate)

        self.update_board_number(get_y_coordinate, get_x_coordinate)



class SudokuGame:
    def __init__(self, board, win_check_num):
        self.all_vertical_nums_valid = False
        super().__init__(board)
        self.board = board
        self.win_check_num = win_check_num

    # Check if win on the vertical axis
    def get_all_vertical_coordinates(self):
        for i in range(len(self.board[0])):
            all_vertical_nums_valid = True
            for j in range(len(self.board)):
                if self.board[j][i] not in self.valid_numbers:
                    all_vertical_nums_valid = False
                    break
    
    def check_valid_vertical(self):
        if self.all_vertical_nums_valid:
            self.win_check_num += 1
            print(self.win_check_num)

    # Check if win on the horizontal axis
    def get_all_horizontal_coordinates(self):
        for i in self.board:
            row_numbers = set(i)
            if row_numbers == set(self.valid_numbers):
                self.win_check_num += 1
    
    # Run function to check win
    def check_is_win(self):
        self.get_all_horizontal_coordinates()
        self.get_all_vertical_coordinates()
        self.check_valid_horizontal()
        if self.win_check_num == 18:
            print("You win!")
            self.is_game_running = False


sudoku_game = Sudoku()
sudoku_game.start_game()
