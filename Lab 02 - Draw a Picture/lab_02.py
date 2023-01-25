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

# Botton

arcade.run()
