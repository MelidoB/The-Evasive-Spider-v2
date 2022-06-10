import pygame

class DefaultInformation:
    def __init__(self):
        self.img = None
        self.x, self.y = None, None

    def set_img(self, img):
        self.img = pygame.image.load(f'Application/Objects_For_Display/Player/Images/{img}')

    def set_coord(self,x,y):
        self.x = x
        self.y = y

