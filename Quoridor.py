
# Author: Nicholas Daters
# Date: 8/10/2021
# Description: Game of Quoridor.

class Player:
    """Represents players of the game Quoridor. Player objects will include data members of player number, pawn
    location, and quantity of fences. """
    def __init__(self, player_number, pawn_location):
        """Initializes a player"""
        self._player_number = player_number
        self._pawn_location = pawn_location
        self._fence_qty = 10

    def __repr__(self):
        """Represents player number P#"""
        return str('P' + str(self._player_number))

    def __str__(self):
        """Represents player number P#"""
        return str('P' + str(self._player_number))

    def get_pawn_location(self):
        """Returns the location of the players pawn"""
        return self._pawn_location

    def set_pawn_location(self, pawn_location):
        """Takes as parameter a tuple and sets the location of the players pawn"""
        self._pawn_location = pawn_location

    def get_fence_qty(self):
        """Returns the quantity of the current players fence inventory"""
        return self._fence_qty

    def reduce_fence_qty(self):
        """Takes no parameter, reduces the quantity of the current players fence inventory by one"""
        self._fence_qty -= 1


class QuoridorGame:
    """Represents a two player game of Quoridor"""

    def __init__(self):
        """Initializes the board with the fences (four edges) and pawns (P1 and P2) placed in the correct positions"""
        self._spaces_for_pawn_and_vertical_fences = [["|", "  ", " ", "  ", " ", "  ", " ", "  ", " ", "  ", " ", "  ",
                                                      " ", "  ", " ", "  ", " ", "  ", "|"] for b in range(9)]
        self._spaces_for_horizontal_fences = [["+", "  ", "+", "  ", "+", "  ", "+", "  ", "+", "  ", "+", "  ", "+",
                                               "  ", "+", "  ", "+", "  ", "+"] for b in range(9)]
        self._P1 = Player(1, (4, 0))
        self._P2 = Player(2, (4, 8))
        self._spaces_for_pawn_and_vertical_fences[0][9] = self._P1  # location is 9 because both cells and edges are counted
        self._spaces_for_pawn_and_vertical_fences[8][9] = self._P2
        self._current_player = self._P1  # player 1 starts
        self._current_state = "UNFINISHED"
        self._outcomes = ["P1_WON", "P2_WON", "UNFINISHED"]
        self._pawn_matrix = [['' for a in range(9)] for b in range(9)]
        self._fence_matrix = [['' for a in range(9)] for b in range(9)]
        self._pawn_matrix[0][4] = self._P1
        self._pawn_matrix[8][4] = self._P2

    def get_pawn_matrix(self):
        """Returns the pawn matrix, which is used to keep track of where the pawns are"""
        return self._pawn_matrix

    def set_pawn_matrix(self, new_location, value):
        """Returns the pawn matrix, which is used to keep track of where the pawns are"""
        self._pawn_matrix[new_location[1]][new_location[0]] = value

    def get_fence_matrix(self):
        """Returns the pawn matrix, which is used to keep track of where the pawns are"""
        return self._fence_matrix

    def set_fence_matrix(self, new_location, value):
        """Returns the pawn matrix, which is used to keep track of where the pawns are"""
        self._fence_matrix[new_location[1]][new_location[0]] += value

    def get_current_player(self):
        """Returns the current player"""
        return self._current_player

    def set_current_player(self, player):
        """Sets the current player"""
        self._current_player = player

    def get_current_state(self):
        """Returns the current player"""
        return self._current_state

    def set_current_state(self, state):
        """Sets the current player"""
        self._current_state = state

    def change_player(self):
        """Changes the current player between P1 and P2"""
        if self.get_current_player() == self._P1:
            self.set_current_player(self._P2)
        elif self.get_current_player() == self._P2:
            self.set_current_player(self._P1)

    def valid_move_jump(self, player, new_location):
        """Method that takes parameters of player and new location and returns True if the move is a valid jump."""
        current_location = self.get_current_player().get_pawn_location()

        if player == 1:
            if (new_location[0] - current_location[0]) == 0 \
                    and (new_location[1] - current_location[1]) == 2:
                # checks that movement is two spaces downwards
                if self.get_pawn_matrix()[new_location[0]][new_location[1] - 1] != '' and \
                        'h' not in self.get_fence_matrix()[new_location[0]][new_location[1] - 1]:
                    # checks to see that the opposing pawn is in the next space, and that there is no fence blocking
                    return True
                else:
                    return False
        if player == 2:
            if (new_location[0] - current_location[0]) == 0 \
                    and (current_location[1] - new_location[1]) == 2:
                # checks that movement is two spaces upwards
                if self.get_pawn_matrix()[new_location[0]][new_location[1] + 1] != '' and \
                        'h' not in self.get_fence_matrix()[new_location[0]][new_location[1] + 1]:
                    # checks to see that the opposing pawn is in the next space, and that there is no fence blocking
                    return True
                else:
                    return False

    def valid_move_cardinal(self, new_location):
        """Method that takes parameter of  new location and returns True if the move is valid and
        False otherwise for a move up, down, left or right."""
        current_location = self.get_current_player().get_pawn_location()

        if (new_location[0] == current_location[0]) and (new_location[1] - current_location[1]) == 1:
            # Move is 1 space downward on board
            if 'h' not in self.get_fence_matrix()[new_location[1]][new_location[0]]:
                return True

        if (new_location[0] == current_location[0]) and (current_location[1] - new_location[1]) == 1:
            # Move is 1 space upwards on board
            if 'h' not in self.get_fence_matrix()[new_location[1] + 1][new_location[0]]:
                return True

        if (new_location[0] - current_location[0]) == 1 and (new_location[1] == current_location[1]):
            # Move is 1 space right on board
            if 'v' not in self.get_fence_matrix()[new_location[1]][new_location[0]]:
                return True

        if (current_location[0] - new_location[0]) == 1 and (current_location[1] == new_location[1]):
            # Move is 1 space left on board
            if 'v' not in self.get_fence_matrix()[new_location[0]][new_location[1] + 1]:
                return True

    def valid_move_diagonal(self, new_location):
        """Method that takes parameters of new location and returns True if the move is valid and
        False otherwise for a diagonal move."""
        current_location = self.get_current_player().get_pawn_location()

        if (new_location[0] - current_location[0]) == 1 and (new_location[1] - current_location[1]) == 1:
            # Move is diagonal down and right
            if self.get_pawn_matrix()[current_location[1] + 1][current_location[0]] != '' and \
                    'h' in self.get_fence_matrix()[current_location[1] + 2][current_location[0]]:
                return True

        if (new_location[0] - current_location[0]) == 1 and (current_location[1] - new_location[1]) == 1:
            # Move is diagonal up and right
            if self.get_pawn_matrix()[current_location[1] - 1][current_location[0]] != '' and \
                    'h' in self.get_fence_matrix()[current_location[1] - 1][current_location[0]]:
                return True

        if (current_location[0] - new_location[0]) == 1 and (new_location[1] - current_location[1]) == 1:
            # Move is diagonal down and left
            if self.get_pawn_matrix()[current_location[1] + 1][current_location[0]] != '' and \
                    'h' in self.get_fence_matrix()[current_location[1] + 2][current_location[0]]:
                return True

        if (current_location[0] - new_location[0]) == 1 and (current_location[1] - new_location[1]) == 1:
            # Move is diagonal up and left
            if self.get_pawn_matrix()[current_location[1] - 1][current_location[0]] != '' and \
                    'h' in self.get_fence_matrix()[current_location[1] - 1][current_location[0]]:
                return True

    def valid_move(self, new_location):
        """Method that takes parameter of new location and returns True if the move is valid and
        False otherwise for basic locations on the board."""
        current_location = self.get_current_player().get_pawn_location()

        if new_location[1] not in range(9) or new_location[0] not in range(9):
            # invalid move - new location is not on the board
            return False

        if (new_location[0] - current_location[0]) == 0 \
                and (new_location[1] - current_location[1]) == 0:
            # invalid move - new location is the same as the current location
            return False

        if self.get_pawn_matrix()[new_location[1]][new_location[0]] != '':
            # invalid move - new location is already occupied
            return False

        else:
            # move is valid for basic rules and will now have to pass rules for either a cardinal direction move,
            # diagonal direction move, or a jump move
            return True

    def move_pawn(self, player, new_location):
        """Method takes following two parameters in order: an integer that represents which player (1 or 2) is making
        the move and a tuple with the coordinates of where the pawn is going to be moved to. Calls the the following
        methods to check if a move is valid: valid_move, valid_move_diagonal and valid_move_cardinal"""
        current_player = self.get_current_player()
        if ('P' + str(player)) == str(self.get_current_player()) and self.get_current_state() == "UNFINISHED":
            if self.valid_move(new_location) is False:
                # Performs basic checks within valid move method
                return False

            else:
                if self.valid_move_jump(player, new_location) or self.valid_move_cardinal(new_location) or \
                        self.valid_move_diagonal(new_location):
                    # check to see if any of the valid move types are possible with the player and new location inputs
                    for i in range(len(self._spaces_for_pawn_and_vertical_fences)):
                        for j in range(len(self._spaces_for_pawn_and_vertical_fences[i])):
                            if self._spaces_for_pawn_and_vertical_fences[i][j] == self.get_current_player():
                                self._spaces_for_pawn_and_vertical_fences[i][j] = '  '
                    # find players current location in graphical board and replaces with two spaces
                    self._pawn_matrix[current_player.get_pawn_location()[1]][current_player.get_pawn_location()[0]] = ''
                    # set the players current location in pawn matrix to ''
                    self._pawn_matrix[new_location[1]][new_location[0]] = self.get_current_player()
                    # set the new location in the pawn matrix to the current player
                    self._spaces_for_pawn_and_vertical_fences[new_location[1]][new_location[0] * 2 + 1] \
                        = self.get_current_player()
                    # update the graphical board to have the current player in the new space
                    self.get_current_player().set_pawn_location((new_location[0], new_location[1]))
                    # update player pawn location parameter
                    self.is_winner(player)
                    # check to see if the current player won the game with current move
                    self.change_player()
                    # move complete, change current player
                return True
        else:
            return False

    def place_fence(self, player, fence_orientation, new_location):
        """Method takes following parameters in order: an integer that represents which player (1 or 2) is making the
        move, a letter indicating whether it is vertical (v) or horizontal (h) fence, a tuple of integers that
        represents the position on which the fence is to be placed."""
        if ('P' + str(player)) == str(self._current_player) and self._current_state == "UNFINISHED" \
                and self.get_current_player().get_fence_qty() > 0 and new_location[0] in range(1, 9) \
                and new_location[1] in range(1, 9):
            if fence_orientation == 'h':
                self.set_fence_matrix(new_location, 'h')
                # update fence matrix
                self._spaces_for_horizontal_fences[new_location[1] - 1][new_location[0] * 2 + 1] = '=='
                # update the graphical board
            if fence_orientation == 'v':
                self.set_fence_matrix(new_location, 'v')
                # update fence matrix
                self._spaces_for_pawn_and_vertical_fences[new_location[1]][new_location[0] * 2] = '|'
                # update the graphical board
            self.get_current_player().reduce_fence_qty()
            # update the current players inventory of fences
            self.change_player()
            # move complete, change current player
            return True
        else:
            return False

    def is_winner(self, player):
        """Method that takes a single integer representing the player number as a parameter and returns True if that
        player has won and False if that player has not won."""
        if player == 1:
            if 'P1' in str(self.get_pawn_matrix()[8]):
                # If P1 is in row 8, the player has crossed the board and won
                self.set_current_state("P1_WON")
                return True
        elif player == 2:
            if 'P2' in str(self.get_pawn_matrix()[0]):
                # If P2 is in column 0, the player has crossed the board and won
                self.set_current_state("P2_WON")
                return True
        else:
            return False

    def print_board(self):
        """Method that prints the board to the screen."""
        print("+==+==+==+==+==+==+==+==+==+")
        for i in range(0, 8):
            print("".join(str(x) for x in self._spaces_for_pawn_and_vertical_fences[i]))  # call repr or str func
            print("".join(self._spaces_for_horizontal_fences[i]))
        print("".join(str(x) for x in self._spaces_for_pawn_and_vertical_fences[8]))
        print("+==+==+==+==+==+==+==+==+==+")


q = QuoridorGame()
q.move_pawn(1, (4, 1))
q.move_pawn(2, (4, 7))

q.move_pawn(1, (4, 2))
q.move_pawn(2, (4, 6))

q.move_pawn(1, (4, 3))
q.move_pawn(2, (4, 5))

q.move_pawn(1, (4, 4))  # now they are face to face
q.place_fence(2, 'h', (7, 1))  # just so that we can finish the turn

q.place_fence(1, 'h', (6, 6))  # this fence will *not* block the jump by player2

wrong_right_diagonal_move = q.move_pawn(2, (5, 4))
q.print_board()
