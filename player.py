import pygame
from fire_balls import Fireballs

class Player(pygame.sprite.Sprite):

    
   
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.health = 100
        self.max_health = 100 # constant
        self.attack = 15
        self.velocity = 23
        self.all_fb = pygame.sprite.Group()
        self.image = pygame.image.load("character_boy.png")# Player image
        self.rect = self.image.get_rect()
        self.rect.x = -300 # x coordinates
        self.rect.y = 65 # y coordinates


    def launch_fire_balls(self):
         self.all_fb.add(Fireballs(self))




    
    def move_right(self):
        if not self.game.check_collision(self,self.game.all_monsters):
           self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):
            
            pygame.draw.rect(surface,(96,96,96),[self.rect.x + 450 , 215,self.max_health , 5])
            pygame.draw.rect(surface,(0,255,0),[self.rect.x + 450, 215, self.health, 5])

    def damage(self,amount,screen):
        if self.health - amount > amount:
           self.health -= amount

        else:
            self.game.game_over(screen)
            
            
            



        

   


    
        
        

    


        

    
        
        






    

    


