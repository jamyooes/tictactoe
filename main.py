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

    print((x_min_val, y_min_val), (x_max_val, y_max_val))
    return (x_min_val, y_min_val), (x_max_val, y_max_val)

def calc_min_max(val):
    """
    Utility function for calc_pos to help find the min and max coordinates
    
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

def draw_player():
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
    
    # Draw board lines
    for i in range(2):
        # Vertical Lines
        pygame.draw.lines(screen, (255, 255, 255), True, [(line_axis_1[i], line_axis_2[0]), (line_axis_1[i], line_axis_2[1])], 10)
        # Horizontal Lines
        pygame.draw.lines(screen, (255, 255, 255), True, [(line_axis_2[0], line_axis_1[i]), (line_axis_2[1], line_axis_1[i])], 10)
        
        # Track the coordinates being drawn onto the screen for placing X and O
        
    # Testing X
    
    # Testing O 
    
    # Update the display
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()