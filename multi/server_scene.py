import pygame
from inputbox import InputBox
from server import Server
import threading


class ServerScene:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True
        self.input_box = InputBox(100, 100, 200, 32)
        self.click_box = InputBox(100, 300, 140, 32)
        self.font = pygame.font.SysFont("arial", self.screen.get_size()[0] // 30, True)
        self.clock = pygame.time.Clock()
        self.server = None
        self.done = False
        self.exit_text = self.font.render("Start", True, (255, 255, 255))
        self.exit_rect = self.exit_text.get_rect()
        self.exit_rect.x = self.screen.get_size()[0] / 30
        self.exit_rect.y = self.screen.get_size()[1] * 0.81

    def run(self):
        while not self.done:
            box = self.input_box
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                box.handle_event(event)
                box.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.click_box.rect.collidepoint(event.pos):
                        print("ok")
                        self.submit()
                    if self.exit_rect.collidepoint(event.pos):
                        try:
                            self.server.send_game_state()
                            print("22")
                            print(f"{self.server.clients}")
                        except Exception as e:
                            print(f"An error occurred when sending the 'game_start' event: {e}")
            self.screen.fill((30, 30, 30))
            box.draw(self.screen)
            self.click_box.draw(self.screen)
            self.screen.blit(self.exit_text, self.exit_rect)
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

    def submit(self):
        try:
            ip, port = self.input_box.submitted.split(":")
            self.server = Server(ip, port)
            threading.Thread(target=self.server.start).start()
        except Exception as e:
            print(f"An error occurred when starting the server: {e}")

if __name__ == '__main__':
    serverScene = ServerScene()
    serverScene.run()




