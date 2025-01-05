import pygame
# Board Class to set up the tic-tac-toe board
class Board():
    def __init__(self, surface):
        self.game_state = [[0]*3, [0]*3, [0]*3]
        self.rounds = 0
        self.legal = True
        self.top_left = None
        self.bot_right = None
        self.tie = None
        self.win = None
        self.render = []
        self.surface = surface
    
    def draw_on_board(self, mouse_pos, surface):
        """
        The purpose of this function is drawing player symbols on the board
        
        1-Calculate the quadarant that the mouse is in using the coordinates
        2-Check if the player's move is legal
        3A-If illegal, do nothing and redo 1 and player has to choose again
        3B-If legal, then plot the X or O
        4-Update the game state
        5-Calculate if the game is over
        6A-If game is over, then the user can click a button to restart state
        6B-If the game is not over, then change player and increment rounds by 1

        Arguments:
        rounds (int) - integer representation of the number or rounds to help plot X (even) or O (odd)
        mouse_pos (tuple) - A tuple value representing the x and y coordinates of the mouse when left clicking on a box
        surface (surface) - surface object in pygame that will be used to display when calling update function
        
        Return:
        
        """ 
        # Calculate quadrant coordinates
        self.calc_pos(mouse_pos)
        
        # Check if player move is legal
        self.is_box_valid()
        
        # if not a valid_move then break out of this function
        if not self.legal:
            return
        
        self.player_moves()
        
        self.plot_player()
        
        # Update the game state array
        self.update_game_state()
        
        # Check if the game is over
        self.calculate_outcome()
        
        # Handle cases for game over?
        # if True:
        #     pass
        # if False:
        #     pass
        
        # rounds function incrementation figure this out later
        self.rounds += 1
        
    
    def calc_pos(self, pos):
        """
        Function to find coordinates to draw player O or X
        Need to find the min and max coordinates to draw O or X

        Arguments:
        pos (tuple) - tuple of integers for current mouse position when clicking    
        
        top_left and bot_right is of form
        min_val, max_val (tuple) - min and max coordinates for the quadrant clicked between the x and y coordinates. 
        """
        x, y = pos
        x_min_val, x_max_val = 0, 0
        y_min_val, y_max_val = 0, 0

        x_min_val, x_max_val = self.calc_min_max(x)
        y_min_val, y_max_val = self.calc_min_max(y)

        # print((x_min_val, y_min_val), (x_max_val, y_max_val))
        self.top_left = (x_min_val, y_min_val)
        self.bot_right = (x_max_val, y_max_val)
    
    def calc_min_max(self, val):
        """
        Utility function for calc_pos to help find the min and max coordinates
        -This function is needed as a utility to calculate the min and max value and 
        did not want to write this code twice in the calc_pos function for each x and y
        -We retrieve the min values for both x and y to obtain the top-left coordinate
        -We retrieve the max values for both x and y to obtain the bottom-right coordinate
        
        Arguments:
        val (int) - int representing the coordinate
        
        Return
        min_val, max_val (int) - returns the min and max value ranges for the quadrant the user clicked on
        """
        min_val, max_val = 0, 0

        # Go through each quadrant
        for i in range (180, 541, 180):
            # Value is greater than quadrant then update the min
            if val > i:
                min_val = i
            # Value is less than quadrant then update max and return
            else:
                max_val = i
                return min_val, max_val

        # This case should never happen (use as a buffer)
        return min_val, max_val
    
    def is_box_valid (self):
        """
        Function of handling wheather a player is "legally" allowed to make the move 
        A "legal" move is placing an O or X on an empty square
        An "illegal" move is placing an O or X on an occupied square
        Updates legal attribute to True, if the move is legal and False if the move is illegal
        """
        if self.game_state[self.top_left[0] // 180][self.top_left[1] // 180] != 0:
            self.legal = False 
        else:
            self.legal = True
    
    def player_moves(self):
        """
        Function that will contain all the moves from the player to aid with plotting
        Handle 0's and 1's in the saving into the list and  save the values from plot_player
        """
        if self.legal and self.top_left is not None:
            pass
    
    def plot_player(self):
        """
        Function handling drawing the player symbols
        
        Arguments:
        surface (surface)- object that is used to display the game
        """
        if self.legal and self.top_left is not None:
            # If the number of rounds is even, then draw 2 diagonal lines
            if self.rounds % 2 == 0:
                self.render.append(pygame.draw.lines(self.surface, (255, 0, 0), True, [self.top_left, self.bot_right], 5))
                # We can find the upper right and bottom left by simply adding and subtracting 180 from the bottom right and upper left respectively
                self.render.append(pygame.draw.lines(self.surface, (255, 0, 0), True, [(self.top_left[0], self.top_left[1] + 180), (self.bot_right[0], self.bot_right[1] - 180)], 5))
            else:
                # Circle center is the midpoint of the top left and bottom right
                circle_center = (self.top_left[0] + self.bot_right[0]) // 2
                self.render.append(pygame.draw.circle(self.surface, (0, 0, 255), [circle_center, circle_center], 90, 5))
    
    def update_game_state(self):
        """
        Function to update game state
        The game state is represented as a list
        0 -> Empty
        1 -> X
        2 -> O
        """
        if self.rounds % 2 == 0:
            self.game_state[self.top_left[0] // 180][self.top_left[1] // 180] = 1
        else:
            self.game_state[self.top_left[0] // 180][self.top_left[1] // 180] = 2

    def calculate_outcome(self):
        """
        Function to calculate the game outcome
        A player can win or lose or tie
        Hard coded
        *** Need to add who won in the return

        Return:
        True - if the game is a win for one of the players
        False - if the game is a tie
        """
        quad_x = self.top_left[0] // 180
        quad_y = self.top_left[1] // 180
        
        # Check the horizonals
        if quad_x == 0:
            if self.game_state[quad_x][quad_y] == self.game_state[quad_x + 1][quad_y] == self.game_state[quad_x + 2][quad_y]:
                self.win = True
        elif quad_x == 1:
            if self.game_state[quad_x - 1][quad_y] == self.game_state[quad_x][quad_y] == self.game_state[quad_x + 1][quad_y]:
                self.win = True
        else:
            if self.game_state[quad_x - 2][quad_y] == self.game_state[quad_x - 1][quad_y] == self.game_state[quad_x][quad_y]:
                self.win = True
        
        # Check vertical    
        if quad_y == 0:
            if self.game_state[quad_x][quad_y] == self.game_state[quad_x][quad_y + 1] == self.game_state[quad_x][quad_y + 2]:
                self.win = True
        elif quad_y == 1:
            if self.game_state[quad_x][quad_y - 1] == self.game_state[quad_x][quad_y] == self.game_state[quad_x][quad_y + 1]:
                self.win = True
        else:
            if self.game_state[quad_x][quad_y - 2] == self.game_state[quad_x][quad_y - 1] == self.game_state[quad_x][quad_y]:
                self.win = True
        
        # In the case of corners or center need to check diagonals otherwise there are no other outcomes
        if quad_x == 1 and quad_y == 1:
            if self.game_state[quad_x][quad_y] == self.game_state[quad_x - 1][quad_y - 1] == self.game_state[quad_x + 1][quad_y + 1]:
                self.win = True
            elif self.game_state[quad_x][quad_y] == self.game_state[quad_x + 1][quad_y - 1] == self.game_state[quad_x - 1][quad_y + 1]: 
                self.win = True
        elif (quad_x + quad_y) % 2 == 0 and self.game_state[quad_x][quad_y] == self.game_state[1][1] == self.game_state[2 - quad_x][2 - quad_y]:
            self.win = True
        
        # If the game is a draw 9 rounds
        if self.rounds == 8:
            self.tie = True
