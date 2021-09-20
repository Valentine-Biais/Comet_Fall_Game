from comet import Comet
import pygame


# Créer une classe pour gérer cet événement
class CometFallEvent:
    
    # Lors du chargement -> créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False
        
        # Définir un groupe de sprites pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()
        
    def add_percent(self):
        self.percent += self.percent_speed / 100
        
    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
        
    def meteor_fall(self):
        # Boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # Apparaître une première comète
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        # La jauge d'événement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True # Activer l'événement
        
    def update_bar(self, surface):
        
        # Ajouter du pourcentage à la barre
        self.add_percent()
        
        # Barre noire (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenêtre
            10 # épaisseur de la barre
        ])
        # Barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la fenêtre
            10 # épaisseur de la barre
        ])