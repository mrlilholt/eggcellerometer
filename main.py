def on_gesture_eight_g():
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.pause(2000)
    basic.show_string("" + str((input.acceleration(Dimension.STRENGTH))))
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
