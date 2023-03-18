""" Lab 7 - User Control """

import arcade
#Snow Fall
def draw_snow_fall(x, y):

    arcade.draw_point(x, y, arcade.color.WHITE, 5)
    # Snow Fall
    arcade.draw_circle_filled(x + 10, 153 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 40, 190 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 100, 142 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 78, 295 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 120, 45 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 50, 50 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 132, 190 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 32, 263 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 220, 75 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 190, 240 + y, 5, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x + 140, 123 + y, 5, arcade.csscolor.WHITE)

#Ground
def draw_ground():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.LIGHT_GREY)

#Background
def background():
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

#SnowPerson Body

def draw_snow_person_head(x,y):
    # Head With Hat and Face
    arcade.draw_circle_filled(x, y, 70, arcade.csscolor.WHITE)
    # Mouth

    arcade.draw_circle_filled(x, y - 41, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x - 18, y - 38, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x + 18, y - 38, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x + 30, y - 27, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x - 30, y - 27, 5, arcade.color.ARSENIC)

    # Nose

    arcade.draw_triangle_filled(x + 5, y - 10, x, 10 + y, x - 60, y, arcade.color.ORANGE)

    # Eyes

    arcade.draw_arc_filled(x - 25, 20 + y, 20, 40, arcade.color.BLUEBERRY, 0, 180)
    arcade.draw_arc_filled(x + 25, 20 + y, 20, 40, arcade.color.BLUEBERRY, 0, 180)

    # Hat

    arcade.draw_polygon_filled(((x + 35, 125 + y), (x - 20, 110 + y)
                                , (x - 50, 50 + y), (x + 50, 53 + y), (x + 20, 90 + y)), arcade.csscolor.RED)
    arcade.draw_circle_filled(x + 35, 125 + y, 10, arcade.csscolor.ANTIQUE_WHITE)

def draw_snow_person(x, y):

    # Point
    arcade.draw_point(x, y, arcade.color.BLUE, 5)

    # Body
    arcade.draw_circle_filled(x, 137 + y, 135, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_circle_filled(x, 292 + y, 95, arcade.csscolor.MINT_CREAM)

    # Arms
    arcade.draw_rectangle_filled(x - 150, 272 + y, 10, 185, arcade.csscolor.SADDLE_BROWN, 50)
    arcade.draw_rectangle_filled(x + 150, 272 + y, 10, 185, arcade.csscolor.SADDLE_BROWN, 130)

    # Hands
    # Left Hand
    arcade.draw_rectangle_filled(x - 187, 215 + y, 10, 50, arcade.csscolor.SADDLE_BROWN, 180)
    arcade.draw_rectangle_filled(x - 200, 247 + y, 10, 37, arcade.csscolor.SADDLE_BROWN, 100)
    # Right Hand
    arcade.draw_rectangle_filled(x + 193, 212 + y, 10, 44, arcade.csscolor.SADDLE_BROWN, 190)
    arcade.draw_rectangle_filled(x + 210, 247 + y, 10, 55, arcade.csscolor.SADDLE_BROWN, 85)

    # Buttons

    arcade.draw_circle_filled(x, 262 + y, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x, 292 + y, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x, 322 + y, 5, arcade.color.ARSENIC)

def head_lost_text(x,y):
    arcade.draw_text("Oh no I lost my head!!!!", x, y, arcade.color.BLUE, 25)


# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

#Snowperson Class
class Snowperson:
    def __init__(self, position_x, position_y, change_x, change_y,radius):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius

    def draw(self):
        draw_snow_person(self.position_x, self.position_y)

    def update(self):
        #Extract sound file
        error_sound = arcade.load_sound("error.wav")

        self.position_y += self.change_y
        self.position_x += self.change_x

        #Border limits
        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(error_sound)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(error_sound)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(error_sound)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(error_sound)

#Snowperson Head Class
class Snowperson_Head:
    def __init__(self, position_x, position_y, radius):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def draw(self):
        draw_snow_person_head(self.position_x, self.position_y)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """


        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(True)
        self.snph = Snowperson_Head(400, 50, 0)
        self.snp = Snowperson(250, 50, 0, 0, 1)

    #What is being drawn
    def on_draw(self):
        arcade.start_render()
        background()
        draw_ground()
        draw_snow_fall(50, 300)
        draw_snow_fall(300, 300)
        draw_snow_fall(550, 300)
        draw_snow_fall(800, 300)
        head_lost_text(600, 50)
        self.snp.draw()
        self.snph.draw()


    def update(self, delta_time):
        self.snp.update()

    #Key Press
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.snp.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.snp.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.snp.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.snp.change_y = -MOVEMENT_SPEED

    #Key Release
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.snp.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.snp.change_y = 0

    #Mouse Click Command
    def on_mouse_press(self, x, y, button, modifiers):
        coin_sound = arcade.load_sound("coin.wav")
        self.snph.position_x = x
        self.snph.position_y = y
        arcade.play_sound(coin_sound)
#Call Main
def main():
    window = MyGame()
    arcade.run()


main()