import pygame 
import random 

pygame.init()

#Global constants
SCREEN_HEIGHT = 600 
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))

START = pygame.image.load("Assets\Dino\DinoStart.png")

RUNNING = [
    pygame.image.load("Assets\Dino\DinoRun1.png"),
    pygame.image.load("Assets\Dino\DinoRun2.png")
]

JUMPIMG = pygame.image.load("Assets\Dino\DinoJump.png")

DUCKING = [
    pygame.image.load("Assets\Dino\DinoDuck1.png"),
    pygame.image.load("Assets\Dino\DinoDuck2.png"),
]

LARGE_CACTUS = [
    pygame.image.load("Assets\Cactus\LargeCactus1.png"),
    pygame.image.load("Assets\Cactus\LargeCactus2.png"),
    pygame.image.load("Assets\Cactus\LargeCactus3.png"),
]

BIRD = [
    pygame.image.load("Assets\Bird\Bird1.png"),
    pygame.image.load("Assets\Bird\Bird2.png"),
]

CLOUD = pygame.image.load("Assets\Other\Cloud.png")

BG = pygame.image.load("Assets\Other\Track.png")

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5 
    
    def __init__(self):
        #Set the image of a dinosaur action
        self.duck_img = DUCKING
        self.run_img = RUNNING 
        self.jump_img = JUMPIMG 
        
        #Set the status value of the dinosaur
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        
        self.step_index = 0
        self.jump_val = self.JUMP_VEL
        self.image = self.run_image[0]
        self.rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        
        def update(self, userInput):
            if self.dino_duck:
                self.duck()
            if self.dino_run:
                self.run()
            if self.dino_jump:
                self.jump()
                
            if self.step_index >= 10:
                self.step_index = 0
                
            if userInput[pygame.K_UP] and not self.dino_jump:
                self.dino_duck = False
                self.dino_run = False
                self.dino_jump = True 
            elif userInput[pygame.K_DOWN] and not self.dino_jump:
                self.dino_duck  = True
                self.dino_run = False
                self.dino_jump = False
            elif not (userInput[pygame.K_DOWN]) or self.dino_jump:
                self.dino_duck = False
                self.dino_run = True
                self.dino_jump = False
                
        def duck(self):
            self.image = self.run_img[self.step_index // 5 ]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS_DUCK
            
        def run(self):
            self.image = self.run_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS
            self.step_index += 1  
        
        def jump(self):
            self.image = self.jump_img
             
        def jump(self):
            self.image = self.jump_img

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))  
         
            
            
                
                
            
        