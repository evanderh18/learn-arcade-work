# Import "Arcade" library

import arcade

# Create a window
arcade.open_window(600,600, "snow_person")

# Background
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

arcade.start_render()
# Ground
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.ALICE_BLUE)

# Body
arcade.draw_circle_filled(300, 175, 135, arcade.csscolor.WHITE_SMOKE)
arcade.draw_circle_filled(300, 330, 95, arcade.csscolor.MINT_CREAM)
arcade.draw_circle_filled(300, 460, 70, arcade.csscolor.WHITE)

# Arms

arcade.draw_rectangle_filled(150, 310, 10, 185, arcade.csscolor.SADDLE_BROWN, 50)
arcade.draw_rectangle_filled(450, 310, 10, 185, arcade.csscolor.SADDLE_BROWN, 130)

# Hands

# Left Hand
arcade.draw_rectangle_filled(113, 253, 10, 50, arcade.csscolor.SADDLE_BROWN, 180)
arcade.draw_rectangle_filled(100, 285, 10, 37, arcade.csscolor.SADDLE_BROWN, 100)
# Right Hand
arcade.draw_rectangle_filled(493, 250, 10, 44, arcade.csscolor.SADDLE_BROWN, 190)
arcade.draw_rectangle_filled(510, 285, 10, 55, arcade.csscolor.SADDLE_BROWN, 85)

# Buttons

arcade.draw_circle_filled(300, 300, 5, arcade.color.ARSENIC)
arcade.draw_circle_filled(300, 330, 5, arcade.color.ARSENIC)
arcade.draw_circle_filled(300, 360, 5, arcade.color.ARSENIC)

# Mouth

arcade.draw_circle_filled(300, 419, 5, arcade.color.ARSENIC)
arcade.draw_circle_filled(282, 422, 5, arcade.color.ARSENIC)
arcade.draw_circle_filled(317, 422, 5, arcade.color.ARSENIC)
arcade.draw_circle_filled(330, 433, 5, arcade.color.ARSENIC)
arcade.draw_circle_filled(270, 433, 5, arcade.color.ARSENIC)

# Nose

arcade.draw_triangle_filled(305, 450, 300, 470, 240, 460, arcade.color.ORANGE)

# Eyes

arcade.draw_arc_filled(275, 480, 20, 40, arcade.color.BLUEBERRY, 0, 180)
arcade.draw_arc_filled(325, 480, 20, 40, arcade.color.BLUEBERRY, 0, 180)

# Hat

arcade.draw_polygon_filled(((300, 575),
                            (285, 550),
                            (315, 550),
                            (310, 545),
                            (280, 545)
                            ),
                            arcade.color.REDWOOD)
arcade.run()
