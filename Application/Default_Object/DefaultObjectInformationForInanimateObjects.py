import pygame


class DefaultInformation:
    def __init__(self):
        self.img = None
        self.x, self.y = None, None
        self.character_img_transformation = None
        self.block_movement = False

    def set_img(self, img):
        self.img = pygame.image.load(f'Application/Objects_For_Display/Inanimate_Objects/Images/{img}')

    def set_character_img_transformation(self, img):
        self.character_img_transformation = img

    def set_coord(self, x, y):
        self.x = x
        self.y = y

