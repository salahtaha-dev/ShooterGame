import pygame
pygame.init()

# generer la fenetre de mon jeu

pygame.display.set_caption("Dragon Shooter")
screen = pygame.display.set_mode((1080,720))


#importer et charger l'arriere plan de mon Jeu
background = pygame.image.load('assets/bg.jpg') #permet de charger une image a un chemin speciphique


running = True

# Boucle tant que la condition est vrai

while running:
    #Appliqer l'arriere plan de mon jeu
    screen.blit(background,(0,-200)) # (0,0) on met l'image au centre

    #Mettre a jour l'ecran
    pygame.display.flip()

    # Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #pour verifier l'evenement et fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeux")

