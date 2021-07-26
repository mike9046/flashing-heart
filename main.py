led.set_brightness(255)
for index in range(2):
    basic.show_leds("""
        . # . # .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)

def on_forever():
    basic.show_leds("""
        . # . # .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
basic.forever(on_forever)
