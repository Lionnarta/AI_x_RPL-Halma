# Class to set basic setup for game board and pawn
class base_setup:
    def __init__(self, scale, x, y, status):
        self.scale = scale
        self.x = x
        self.y = y
        self.status = status

    def get_scale(self):
        return self.scale

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
        
    def get_status(self):
        return self.status

    def set_scale(self, scale):
        self.scale = scale

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_status(self, status):
        self.status = status