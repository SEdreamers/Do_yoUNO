import os
import json
import pygame 

def load_existing_save(savefile):    ##읽기 
    with open(os.path.join(savefile), 'r+') as file:   ## 파일을 열어서 load 시킬 것.   
        controls = json.load(file)     ## controls로 불리는 dictionary에 적재 
    return controls 

def write_save(data):    ## 새로운 파일을 쓰거나 기존의 파일을 덮어쓰기.  dictionary형태의 data를 받아올 것. 
    ##기존의 것이 없다면'w', 새로 쓴다. 
    with open(os.path.join(os.getcwd(),'save.json'), 'w') as file:   
        json.dump(data, file)  ##data 딕셔너리를 file에 dump시켜 저장한다. 


def load_save():
    try:
    # Save is loaded    
        save = load_existing_save('save.json')   ##save.json이라는 파일을 찾아본다. 이게 없거나 corrupt되면 아랫줄 수행.  
    except:
    # No save file, so create one 
        save = create_save()     ## 새로운 파일을 만들어거기에 저장시킨다.
        write_save(save)
    return save


def create_save():    ##default 값 - save file이 없으면 동작.  
    new_save = {
    "controls":{
        "0" :{"Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w, "Down": pygame.K_s, 
            "Start": pygame.K_RETURN, "Action1": pygame.K_SPACE},
        "1" :{"Left": pygame.K_a, "Right": pygame.K_d, "Up": pygame.K_w, "Down": pygame.K_s, 
            "Start": pygame.K_RETURN, "Action1": pygame.K_SPACE}
        },
    "current_profile": 0
    }

    return new_save

def reset_keys(actions):   ## action 딕셔너리를 입력받아 default값으로 되돌림. 
    for action in actions:
        actions[action] = False    ## reset all the Keys to False 
    return actions