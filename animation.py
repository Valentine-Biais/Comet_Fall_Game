import pygame


# Définir une classe qui va gérer les animations
class AnimateSprite(pygame.sprite.Sprite):
    
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False
        
    # Définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True
        
    # Définir une méthode pour pouvoir animer le sprite
    def animate(self, loop=False):
        
        # Vérifier si l'animation est active
        if self.animation:
        
            # Passer à l'image suivante
            self.current_image += 1
            
            # Vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # Remettre l'animation au départ
                self.current_image = 0
                
                # Vérifier si l'animation n'est pas en mode boucle
                if loop is False:
                    
                    # Désactivation de l'animation
                    self.animation = False
                
            # Modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


        
# Définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # Charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # Récupérer le chemin du dossier pour ce sprite
    path = f'assets/{sprite_name}/{sprite_name}'
    
    # Boucler sur chaque image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
        
    # Renvoyer le contenu de la liste d'images
    return images

# Définir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}