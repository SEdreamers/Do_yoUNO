import pygame
import gameoverUI

pygame.init()
g = gameoverUI.GameOverUI(1000, 800, 'Player', False)
play = True
while play:
    g.display([0,1,2,3,4,5])
    pygame.display.flip()
    
