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
                game.draw_on_board(event.pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    # Draw board lines
    for i in range(2):
        # Vertical Lines
        pygame.draw.lines(screen, (255, 255, 255), True, [(line_axis_1[i], line_axis_2[0]), (line_axis_1[i], line_axis_2[1])], 10)
        # Horizontal Lines
        pygame.draw.lines(screen, (255, 255, 255), True, [(line_axis_2[0], line_axis_1[i]), (line_axis_2[1], line_axis_1[i])], 10)
    
    # Game is updated regularly need to persist the X and O's on the screen
    for player_x_sym in game.render_x:
        pygame.draw.lines(screen, (255, 0, 0), True, player_x_sym, 5)
    for player_o_sym in game.render_y:
        pygame.draw.circle(screen, (0, 0, 255), player_o_sym, 90, 5)
    
    # Cases when the game is over or lost
    if game.win:
        print ("game over: ", game.rounds)
    
    
    # Update the display
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()