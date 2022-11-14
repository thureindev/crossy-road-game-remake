"""
Player Class to control all player inputs and behaviours
"""
import game_settings as gs


class Player():
    def __init__(self, speed=15, color="red"):
        self.pos_x = gs.SCREEN_WIDTH / 2
        self.pos_y = gs.SCREEN_HEIGHT - 50
        self.height = 20
        self.width = 20

        self.speed = speed
        self.color = color

        self.draw_x0 = 0
        self.draw_x1 = 0
        self.draw_y0 = 0
        self.draw_y1 = 0
        self.update_draw_coord()

    def update_draw_coord(self):
        self.draw_x0 = self.pos_x - (self.width / 2)
        self.draw_x1 = self.pos_x + (self.width / 2)
        self.draw_y0 = self.pos_y - (self.height / 2)
        self.draw_y1 = self.pos_y + (self.height / 2)

    def move_up(self):
        self.pos_y -= self.speed
        self.update_draw_coord()

    def move_down(self):
        self.pos_y += self.speed
        self.update_draw_coord()

    def move_right(self):
        self.pos_x += self.speed
        self.update_draw_coord()

    def move_left(self):
        self.pos_x -= self.speed
        self.update_draw_coord()
