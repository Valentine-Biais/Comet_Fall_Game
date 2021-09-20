import pygame
import random
import animation


# Définir la classe qui va gérer la notion de monstre sur notre jeu
class Monster(animation.AnimateSprite):
    
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()
        
    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)
        
    def set_loot_amount(self, amount):
        self.loot_amount = amount
        
    def damage(self, amount):
        # Infliger les dégâts
        self.health -= amount
        
        # Vérifier si son nouveau nombre de points de vie est inférieur ou égal à 0
        if self.health <= 0:
            # Réapparaître comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # AJouter le nombre de points au score
            self.game.add_score(self.loot_amount)
            
            # Si la barre d'événement est chargée au max
            if self.game.comet_event.is_full_loaded():
                # Retirer le monstre du jeu
                self.game.all_monsters.remove(self)
                        
                # Appel de la méthode pour essayer de déclencher la pluie de comètes
                self.game.comet_event.attempt_fall()
                
    def update_animation(self):
        self.animate(loop=True)
        
    def update_health_bar(self, surface):
        # Dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        
    def forward(self):
        # Le déplacement ne se fait que s'il n'y a pas de collision avec un joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # Si le monstre est en collision avec le joueur
        else:
            # Infliger des dégâts au joueur
            self.game.player.damage(self.attack)
            

# Définir une classe pour la momie
class Mummy(Monster):
    
    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)
        

# Définir une classe pour l'alien
class Alien(Monster):
    
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)