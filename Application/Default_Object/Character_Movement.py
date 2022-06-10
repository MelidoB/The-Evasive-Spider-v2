from Application.Default_Object.change_image import change_img
class CharacterMovement:
    def __init__(self):
        self.image_for_movements_exist = True
        self.images_movements = {}
        self.index_movements = {}

        self.counter_image_left = 5
        self.counter_image_right = 5
        self.counter_image_top = 5
        self.counter_image_down = 5

    def set_images_movements(self,direction, imgs):
        '''No mater how big the array of imgs is it will still work'''
        self.images_movements[direction] = imgs
        self.index_movements[direction] = 0
    def move_left(self):
        self.x -= 1
        if self.image_for_movements_exist and self.counter_image_left > 5:
            img = change_img(self.images_movements,self.index_movements, direction='left')
            self.set_img(img)
            self.counter_image_left = 0
        self.counter_image_left += 1

    def move_right(self):
        self.x += 1
        if self.image_for_movements_exist and self.counter_image_right > 5:
            img = change_img(self.images_movements, self.index_movements, direction='right')
            self.set_img(img)
            self.counter_image_right = 0
        self.counter_image_right += 1
    def move_top(self):
        self.y -= 1
        if self.image_for_movements_exist and self.counter_image_top > 5:
            img = change_img(self.images_movements, self.index_movements, direction='top')
            self.set_img(img)
            self.counter_image_top = 0
        self.counter_image_top += 1

    def move_down(self):
        self.y += 1
        if self.image_for_movements_exist and self.counter_image_down > 5:
            img = change_img(self.images_movements, self.index_movements, direction='down')
            self.set_img(img)
            self.counter_image_down = 0
        self.counter_image_down += 1
