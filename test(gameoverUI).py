import pygame
import gameoverUI

pygame.init()
g = gameoverUI.GameOverUI(1000, 800, 'Player', False)
play = True
while play:
    g.display()
    pygame.display.flip()
    
