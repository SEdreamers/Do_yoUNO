import pygame
import storyMap

pygame.init()
g = storyMap.StoryMap(1000,750)
play = True
while play:
    g.run()
    pygame.display.flip()
pygame.quit()