# Main file for the tic-tac-toe game
import board
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

game = board.Board(screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1:
                game.draw_on_board(event.pos, screen)

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
    
    for i in game.render:
        continue    
    ### Remove End

    # Update the display
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()