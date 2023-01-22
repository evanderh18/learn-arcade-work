import arcade

arcade.open_window(600,600, "snow_person")
#background
arcade.set_background_color(arcade.csscolor.LIGHT_BLUE)

arcade.start_render()
#ground
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.WHITE_SMOKE)

#body
arcade.draw_circle_filled(300, 175, 135, arcade.csscolor.WHITE)

#arms

arcade.draw_rectangle_filled(180, 320, 10, 185, arcade.csscolor.SADDLE_BROWN, 50)
arcade.draw_rectangle_filled(420, 320, 10, 185, arcade.csscolor.SADDLE_BROWN, 130)


arcade.run()
