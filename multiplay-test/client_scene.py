import pygame

from inputbox import InputBox
from client import Client


class ClientScene:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.input_box = InputBox(100, 100, 140, 32)
        self.click_box = InputBox(100, 300, 140, 32)
        self.clock = pygame.time.Clock()
        self.done = False
        self.client = None

    def run(self):
        while not self.done:
            box = self.input_box
            if self.client is not None:
                self.client.game_loop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                box.handle_event(event)
                box.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click_box.rect.collidepoint(event.pos):
                        print("ok")
                        self.submit()

            self.screen.fill((30, 30, 30))
            box.draw(self.screen)
            self.click_box.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

    def submit(self):
        ip, port = self.input_box.submitted.split(":")
        self.client = Client(ip, port, self.screen, "name")

if __name__ == '__main__':
    client_scene = ClientScene()
    client_scene.run()
