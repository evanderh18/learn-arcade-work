import arcade
import random
import math

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.75
SPRITE_SCALING_STAR = .25
SPRITE_ROCK_SCALING = .35
STAR_COUNT = 60
ROCK_RANGE = 40

SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Space Star Collector"

#Rock Border Class
class Rock(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = random.randint(0,300)

        # How fast to orbit, in radians per frame
        self.circle_speed = random.randint(1,100)/8000

        # Set the center of the point we will orbit around
        self.circle_center_x = random.randint(0,SCREEN_WIDTH)
        self.circle_center_y = random.randint(0,SCREEN_HEIGHT)

    def update(self):

        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
                        + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
                        + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


#Star Border Class
class Star(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the rock
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.star_list = None
        self.rock_list = None
        self.gameOver = False

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        img = ":resources:images/space_shooter/playerShip1_blue.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the stars
        for i in range(STAR_COUNT):

            # Create the star instance
            # Star image from kenney.nl
            star = Star(":resources:images/items/star.png",
                                 SPRITE_SCALING_STAR)

            # Position the star
            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)
            star.change_x = random.randrange(-3, 4)
            star.change_y = random.randrange(-3, 4)

            # Add the star to the lists
            self.star_list.append(star)

        for i in range(ROCK_RANGE):

            # Create the rock instance
            # Rock image from kenney.nl
            rock = Rock(":resources:images/space_shooter/meteorGrey_med1.png",
                                 SPRITE_ROCK_SCALING)

            # Position the Rock
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            rock.change_x = random.randrange(-3, 4)
            rock.change_y = random.randrange(-3, 4)

            # Add the Rock to the lists
            self.rock_list.append(rock)

        rock = arcade.Sprite(":resources:images/space_shooter/meteorGrey_med1.png",
                             SPRITE_ROCK_SCALING)

        # Position the Rock
        rock.center_x = random.randrange(SCREEN_WIDTH)
        rock.center_y = random.randrange(SCREEN_HEIGHT)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.star_list.draw()
        self.rock_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.BLUE, font_size=30)
        if self.gameOver:
            arcade.draw_text(text="Game Over", start_x=300, start_y=350,
                             color=arcade.color.RED, font_size=75)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        if not self.gameOver:
            # Move the center of the player sprite to match the mouse x, y
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Extract Sound
        if len(self.star_list) > 0:
            star_sound = arcade.load_sound("star.wav")
            rock_sound = arcade.load_sound("rock.wav")
            self.rock_list.update()
            self.star_list.update()

            # Generate a list of all sprites that collided with the player.
            star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.star_list)
            rock_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.rock_list)

            # Hit Star.
            for star in star_hit_list:
                star.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(star_sound)
            # Hit Rock
            for rock in rock_hit_list:
                rock.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(rock_sound)
            # Game Over
            if len(self.star_list) == 0:
                self.gameOver = True

def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
