# Import "Arcade" library

import arcade

# Create a window
arcade.open_window(600,600, "snow_person")

# Background
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

arcade.start_render()
# Ground
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.LIGHT_GREY)

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

arcade.draw_polygon_filled(((335, 585),
                            (280, 570),
                            (250, 510),
                            (350, 510),
                            (320, 550)
                            ),
                           arcade.csscolor.RED)
arcade.draw_circle_filled(335, 585, 10, arcade.csscolor.ANTIQUE_WHITE)

# Snow Fall

# Left Side
arcade.draw_circle_filled(10, 590, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(40, 440, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(100, 550, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(196, 505, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(120, 590, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(50, 310, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(132, 429, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(149, 570, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(220, 450, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(190, 320, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(140, 340, 5, arcade.csscolor.WHITE)

# Right Side

arcade.draw_circle_filled(424, 543, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(450, 442, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(543, 549, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(390, 587, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(520, 429, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(530, 310, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(590, 398, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(380, 452, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(475, 532, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(409, 370, 5, arcade.csscolor.WHITE)
arcade.draw_circle_filled(500, 356, 5, arcade.csscolor.WHITE)

# Let it snow text
arcade.draw_text("Let it Snow!",
                  160, 150, arcade.color.BLUE, 40)

arcade.finish_render()
arcade.run()
