import random
import pygame

players = []

player_input = int(input('How many players? '))
for _ in range(player_input):
    user_input = input("Enter player names: ")
    players.append(user_input)

pygame.init()

# Set up the window
window_size = (1111, 888)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Catan')  # Set the window title

# Board
board = pygame.image.load(r'C:\Users\colby\Downloads\catan.jpg')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.blit(board, (0,0))
    pygame.display.update()

# Clean up
pygame.quit()








