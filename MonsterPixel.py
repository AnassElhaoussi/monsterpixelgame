import pygame
from game import Game
from fire_balls import Fireballs

pygame.init()
game = Game()



screen = pygame.display.set_mode((1020,600))  # Screen
name = pygame.display.set_caption("MonsterPixel") # Name of the game
background = pygame.image.load("bgg.png") #The background
banner = pygame.image.load("banner.png")
play_button = pygame.image.load("playbutton.png")
play_button = pygame.transform.scale(play_button,(800,500))
play_button_rect = play_button.get_rect()
play_button_rect.x = 85
play_button_rect.y = 140



run = True
while run:

    screen.blit(background,(0,0)) # Defining and showing up the background
    
    
    if game.is_playing:
        game.update(screen)
    

    else:
           screen.blit(banner,(-30,-45))
           screen.blit(play_button, play_button_rect)

        


    pygame.display.flip()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.is_playing:              
                     game.player.launch_fire_balls()
                     game.sound_effects.play('tir')
                     

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                game.start()
                game.sound_effects.play('click')

                

                     

                



      
            

pygame.quit()



    




