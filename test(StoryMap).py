import pygame
import storyMap

pygame.init()
g = storyMap.StoryMapUI(1000,750)
play = True
while play:
    g.run()
    pygame.display.flip()
pygame.quit()