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

# Initialize the game
game = board.Board()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1:
                # Checks to insure that there is no funny business when the gameover screen is up to override wins cause a tie
                if game.win != True and game.tie != True:
                    # Game Logic and handles user input
                    game.draw_on_board(event.pos)
                    
    # background color
    screen.fill("black")
    
    # If the game is not over, or a tie:
    if game.win != True and game.tie != True:
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
    # Cases when the game is over or lost have an end screen to restart the game or quit
    else:
        font = pygame.font.SysFont('arial', 40)
        if game.winner == "X":
            title = font.render('Game Over: X wins!', True, (255, 255, 255))
        elif game.winner == "O":
            title = font.render('Game Over: O wins!', True, (255, 255, 255))
        restart_button = font.render('R - Restart', True, (255, 255, 255))
        quit_button = font.render('Q - Quit', True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
        screen.blit(restart_button, (SCREEN_WIDTH/2 - restart_button.get_width()/2, SCREEN_HEIGHT/1.9 + restart_button.get_height()))
        screen.blit(quit_button, (SCREEN_WIDTH/2 - quit_button.get_width()/2, SCREEN_HEIGHT/2 + quit_button.get_height()/2))
        if pygame.key.get_pressed()[pygame.K_r]:
            game.reset_game()
        if pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
            quit()
    
    # Update the display
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()