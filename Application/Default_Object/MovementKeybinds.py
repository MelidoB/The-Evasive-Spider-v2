class MovementKeybinds:
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.down = None

    def set_movement_keybinds(self,left,right,top,down):
        self.left = left
        self.right = right
        self.top = top
        self.down = down