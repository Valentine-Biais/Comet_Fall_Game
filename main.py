import pygame
import math
from game import Game
pygame.init()

# Définir une clock
clock = pygame.time.Clock()
FPS = 60

# Générer la fenêtre de notre jeu
pygame.display.set_caption('Comet fall Game')
screen = pygame.display.set_mode((1080, 720))

# Importer l'arrière plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# Importer notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4) #arrondir

# Importer le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Charger notre jeu
game = Game()

running = True

# Boucle tant que cette condition est vraie
while running:
    
    # Appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, -200))
    
    # Vérifier si notre jeu a commencé ou non
    if game.is_playing:
        # Déclencher les instructions de la partie
        game.update(screen)
    # Vérifier si notre jeu n'a pas commencé
    else:
        # Ajouter mon écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
    
    # Mettre à jour l'écran
    pygame.display.flip()
    
    # Si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # Vérif que l'évènement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeu')
            
        # Détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            # Détecter si la touche espace est enclenchée pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # Mettre le jeu en mode lancer
                    game.start()
                    # Jouer le son
                    game.sound_manager.play('click')
                    
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # Mettre le jeu en mode lancer
                game.start()
                # Jouer le son
                game.sound_manager.play('click')
    # Fixer le nombre de fps sur ma clock
    clock.tick(FPS)