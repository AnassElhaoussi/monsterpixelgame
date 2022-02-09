import pygame
from fire_balls import Fireballs
from monster import Monster
from player import Player
from sounds import SoundEffects



class Game():
    def __init__(self):
        self.player = Player(self)
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monsters()
        self.score = 0

        
        self.sound_effects = SoundEffects()
        


    def start(self):
        self.is_playing = True

        self.spawn_monsters() 
        
    def game_over(self,screen):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        
        self.is_playing = False
        self.score = 0
        self.sound_effects.play('gameover')
        self.font = pygame.font.SysFont("monospace",30)
        self.text = self.font.render(f"GAME OVER",1,(0,0,0))
    
        screen.blit(self.text,(20,20))
        


    def add_score(self,points=10):
        self.score += points



    


      


    def update(self,screen):

        font = pygame.font.SysFont("monospace",16)
        score_text = font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text, (20,20))

        screen.blit(self.player.image,self.player.rect) # Defining and showing up the player image 

        for fire_balls in self.player.all_fb:
           fire_balls.move()     


        for monster in self.all_monsters:
           monster.forward(screen)
           monster.update_health_bar(screen)

        self.player.all_fb.draw(screen)
        self.player.update_health_bar(screen)



        self.all_monsters.draw(screen)

 

        if self.pressed.get(pygame.K_RIGHT) and  self.player.rect.x < 390:     
           self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -390:
              self.player.move_left()

        

        

        
        
        
        

    def spawn_monsters(self):
        
        self.all_monsters.add(Monster(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        





