import pygame
import random

class Monster(pygame.sprite.Sprite):
        def __init__(self,game):
            super().__init__()
            self.game = game

            self.health = 100
            self.max_health = 100
            self.attack = 2.5
            self.image = pygame.image.load("monsters.png")
            self.rect = self.image.get_rect()
            self.rect.x = 380 + random.randint(0,300)
            self.rect.y = 75
            self.velocity = random.randint(25,55)

        def update_health_bar(self, surface):
            
            pygame.draw.rect(surface,(96,96,96),[self.rect.x + 440 , 235,self.max_health , 5])
            pygame.draw.rect(surface,(0,255,0),[self.rect.x + 440, 235, self.health, 5])


        def damage(self, amount):
            self.health -= amount

            if self.health <= 0:
                self.rect.x = 500 + random.randint(0,300)
                self.velocity = random.randint(25,55)
                self.health = self.max_health  
                self.game.sound_effects.play('score_sound') 
                self.game.add_score()
                
            
        


        def forward(self,screen):
            if not self.game.check_collision(self, self.game.all_players):
               self.rect.x -= self.velocity

            else:
                self.game.player.damage(self.attack,screen)

 