import pygame

class Fireballs(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.velocity = 32
        self.image = pygame.image.load("fire_balls.png")
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y - 40

    def remove(self):
        self.player.all_fb.remove(self)


    def move(self):
        self.rect.x += self.velocity

        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)
        
        if self.rect.x > 480:
            self.player.all_fb.remove(self)

        

    
        
        


        


