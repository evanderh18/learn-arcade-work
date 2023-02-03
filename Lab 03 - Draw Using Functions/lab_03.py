import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
# Create a window


def draw_ground():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.LIGHT_GREY)

def draw_snow_person(x, y):

    # Point

    arcade.draw_point(x, y, arcade.color.BLUE, 5)

    # Body

    arcade.draw_circle_filled(x, 137 + y, 135, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_circle_filled(x, 292 + y, 95, arcade.csscolor.MINT_CREAM)
    arcade.draw_circle_filled(x, 422 + y, 70, arcade.csscolor.WHITE)

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

    # Mouth

    arcade.draw_circle_filled(x, 381 + y, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x - 18, 384 + y, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x + 18, 384 + y, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x + 30, 395 + y, 5, arcade.color.ARSENIC)
    arcade.draw_circle_filled(x - 30, 395 + y, 5, arcade.color.ARSENIC)

    # Nose

    arcade.draw_triangle_filled(x + 5, 412 + y, x, 432 + y, x - 60, 422 + y, arcade.color.ORANGE)

    # Eyes

    arcade.draw_arc_filled(x - 25, 442 + y, 20, 40, arcade.color.BLUEBERRY, 0, 180)
    arcade.draw_arc_filled(x + 25, 442 + y, 20, 40, arcade.color.BLUEBERRY, 0, 180)

    # Hat

    arcade.draw_polygon_filled(((x + 35, 547 + y), (x - 20, 532 + y), (x - 50, 472 + y), (x + 50, 472 + y), (x + 20, 512 + y)), arcade.csscolor.RED)
    arcade.draw_circle_filled(x + 35, 547 + y, 10, arcade.csscolor.ANTIQUE_WHITE)

def draw_snow_fall(x,y):

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


def let_it_snow_text(x, y):
    # Text Point
    arcade.draw_point(x, y, arcade.color.BLUE, 5)
    # Let it snow text
    arcade.draw_text("Let it Snow!", x - 8, y - 5, arcade.color.BLUE, 45)




def on_draw(delta_time):
    arcade.start_render()

    draw_ground()
    draw_snow_fall(50, 300)
    draw_snow_fall(300, 300)
    draw_snow_fall(550, 300)
    draw_snow_fall(800, 300)
    draw_snow_person(250, 50)
    draw_snow_person(750, 40)
    let_it_snow_text(on_draw.let_it_snow1_x, 75)

    on_draw.let_it_snow1_x += 1

on_draw.let_it_snow1_x = 100

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "snow_person")
    arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)
    arcade.schedule(on_draw, (1/60))
    arcade.run()

main()


