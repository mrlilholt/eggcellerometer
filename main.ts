input.onGesture(Gesture.EightG, function on_gesture_eight_g() {
    basic.showLeds(`
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    `)
    basic.pause(2000)
    basic.showString("" + ("" + input.acceleration(Dimension.Strength)))
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.clearScreen()
})
