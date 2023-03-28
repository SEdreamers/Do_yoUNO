import pygame, sys
from util import write_save

class Controls_Handler():
    def __init__(self, save):    # 
        self.save_file = save
        self.curr_block = save["current_profile"]    #current_profile이라는 키값. 
        self.controls = self.save_file["controls"][str(self.curr_block)]
        self.setup()

    def update(self, actions):
        if self.selected: self.set_new_control()
        else: self.navigate_menu(actions)

    def render(self, surface):
        self.draw_text(surface, "Control Profile " + str(self.curr_block+1) , 20, pygame.Color((0,0,0)), 480 / 2, 270/8)
        self.display_controls(surface, self.save_file["controls"][str(self.curr_block)])
        if self.curr_block == self.save_file["current_profile"]: self.draw_text(surface, "*"  , 20, pygame.Color((0,0,0)), 20, 20)

    def navigate_menu(self, actions):
        # Move the cursor up and down
        if actions["Down"]: self.curr_index = (self.curr_index + 1) % (len(self.save_file["controls"][str(self.curr_block)]) + 1)
        if actions["Up"]: self.curr_index = (self.curr_index - 1) % (len(self.save_file["controls"][str(self.curr_block)]) + 1)
        # Switch between profiles
        if actions["Left"]: self.curr_block = (self.curr_block -1) % len(self.save_file["controls"]) 
        if actions["Right"]: self.curr_block = (self.curr_block +1) % len(self.save_file["controls"]) 
        # Handle Selection
        if actions["Action1"] or actions["Start"]:
            # Set the current profile to be the main one
            if self.cursor_dict[self.curr_index] == "Set":
                self.controls = self.save_file["controls"][str(self.curr_block)]
                self.save_file["current_profile"] = self.curr_block
                write_save(self.save_file)
            else: 
                self.selected = True

    def set_new_control(self):
        selected_control = self.cursor_dict[self.curr_index]
        done = False
        while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True
                            pygame.quit()
                            sys.exit()
                        elif event.key not in self.save_file["controls"][str(self.curr_block)].values():
                            self.save_file["controls"][str(self.curr_block)][selected_control] = event.key
                            write_save(self.save_file)
                            self.selected = False
                            done = True

    def display_controls(self,surface, controls):
        color = (255,13,5) if self.selected else (255,250,239)
        pygame.draw.rect(surface, color, (80 , 270/4 - 10 + (self.curr_index*30), 320, 20) )
        i = 0
       
    def setup(self):
        self.selected = False                    ## 사용자가 설정을 바꾸었는지 확인할 수 있는 flag
        self.font = pygame.font.Font(None, 20)
        self.cursor_dict = {}                   ## empty dictionary 
        self.curr_index = 0
        i = 0
        for control in self.controls:
            self.cursor_dict[i] = control                  #0는 left 에 대응됨, 1은 right에 대응됨. 
            i += 1
        self.cursor_dict[i] = "Set"
