import pygame
import random


# Créer une classe pour gérer cette comète
class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        # Définir l'image associé à cette comète
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 600)
        self.comet_event = comet_event
        
    def remove(self):
        self.comet_event.all_comets.remove(self)
        # Jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        
        # Si le nombre de comètes est de 0
        if len(self.comet_event.all_comets) == 0:
            # Remettre la barre à 0
            self.comet_event.reset_percent()
            # Apparaître les monstres
            self.comet_event.game.start()
        
    def fall(self):
        self.rect.y += self.velocity
        
        # Ne tombe pas sur le sol
        if self.rect.y >= 500:
            # Retirer la comète
            self.remove()
            
            # S'il n'y a plus de comète
            if len(self.comet_event.all_comets) == 0:
                # Remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
            
        # Vérifier si la comète touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            # Retirer la comète, joueur touché
            self.remove()
            # Subir 20 points de dégâts
            self.comet_event.game.player.damage(20)