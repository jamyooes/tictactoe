# Main file for the tic-tac-toe game
import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 540, 540
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Board Line Coordinates 
line_axis_1 = [180, 360]
line_axis_2 = [0, 540]

rounds = 0
# Move this into class initalization 
game_state_list = [[0]*3, [0]*3, [0]*3]

def calc_pos(pos):
    """
    Function to find coordinates to draw player O or X
    Need to find the min and max coordinates to draw O or X
    
    Arguments:
    pos (tuple) - tuple of integers for current mouse position when clicking    
    
    Return:
    min_val, max_val (tuple) - min and max coordinates for the quadrant clicked between the x and y coordinates. 
    """
    x, y = pos
    x_min_val, x_max_val = 0, 0
    y_min_val, y_max_val = 0, 0

    x_min_val, x_max_val = calc_min_max(x)
    y_min_val, y_max_val = calc_min_max(y)

    # print((x_min_val, y_min_val), (x_max_val, y_max_val))
    return (x_min_val, y_min_val), (x_max_val, y_max_val)

def calc_min_max(val):
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

def draw_on_board(game_state, rounds, mouse_pos, surface, round):
    """
    The purpose of this function is drawing player symbols on the board
    
    1-First check if the player's move is legal
    2-Calculate the quadarant that the mouse is in using the coordinates
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
    
    # Check if player move is legal
    valid_move = is_box_valid()
    
    # Calculate quadrant coordinates
    top_left, bottom_right = calc_pos(mouse_pos)
    
    # if not a valid_move then break out of this function
    if not valid_move:
        pass
    
    # Plot the player symbol onto the surface
    plot_player(surface, round, top_left, bottom_right)
    
    update_game_state(game_state, top_left, bottom_right)
    
    pass

def update_game_state(game_state, top_left, rounds):
    """
    Function to update game state
    The game state is represented as a list
    0 -> Empty
    1 -> X
    2 -> O
    
    Arguments:
    game_state (list) - List representation of board
    top_left (tuple) - integer tuple representing top left coordinates of the quadrant the user clicked on
    rounds(tuple) -  integer representation of the number or rounds to help plot X (even) or O (odd)
    """
    if rounds % 2 == 0:
        game_state_list[top_left[0] // 180][top_left[1] // 180] = 1
    else:
        game_state_list[top_left[0] // 180][top_left[1] // 180] = 2

    # Remove this as we will handle the attributes in the class
    return game_state
    

def plot_player(surface, rounds, top_left, bot_right):
    """
    Function handling drawing the player symbols
    
    Arguments:
    surface (surface)- object that is used to display the game
    rounds (int) - integer representation of the number or rounds to help plot X (even) or O (odd) 
    top_left (tuple) - integer tuple representing top left coordinates of the quadrant the user clicked on
    bot_right (tuple) - integer tuple representing bottom right coordinates of the quadrant the user clicked on
    """
    # If the number of rounds is even, then draw 2 diagonal lines
    if rounds % 2 == 0:
        pygame.draw.lines(surface, (255, 0, 0), True, [top_left, bot_right], 5)
        # We can find the upper right and bottom left by simply adding and subtracting 180 from the bottom right and upper left respectively
        pygame.draw.lines(surface, (255, 0, 0), True, [(top_left[0], top_left[1] + 180), (bot_right[0], bot_right[1] - 180)], 5)
    else:
        # Circle center is the midpoint of the top left and bottomr right
        circle_center = (top_left[0] + bot_right[0]) // 2
        pygame.draw.circle(surface, (0, 0, 255), [circle_center, circle_center], 90, 5)

def is_box_valid ():
    """
    Function of handling wheather a player is "legally" allowed to make the move 
    A "legal" move is placing an O or X on an empty square
    An "illegal" move is placing an O or X on an occupied square
    
    Arguments
    """
    pass

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1:
                calc_pos(event.pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    ### Remove Start
    # Draw board lines
    for i in range(2):
        # Vertical Lines
        pygame.draw.lines(screen, (255, 255, 255), True, [(line_axis_1[i], line_axis_2[0]), (line_axis_1[i], line_axis_2[1])], 10)
        # Horizontal Lines
        pygame.draw.lines(screen, (255, 255, 255), True, [(line_axis_2[0], line_axis_1[i]), (line_axis_2[1], line_axis_1[i])], 10)
        
        # Track the coordinates being drawn onto the screen for placing X and O
        
    # # Testing X
    # pygame.draw.lines(screen, (255, 0, 0), True, [(0, 0), (180, 180)], 5)
    # pygame.draw.lines(screen, (255, 0, 0), True, [(0, 180), (180, 0)], 5)
    # # Testing O 
    # circle_center = (0 + 180) // 2
    # pygame.draw.circle(screen, (0, 0, 255), [circle_center, circle_center], 90, 5)
    
    # game_state_list[180 // 180][180 // 180] = 1
    # print(game_state_list)
    ### Remove End

    # Update the display
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()