    # Problem 11 — colour wave

# Create a scene called ColourWave that:

# Creates a row of 5 circles side by side using a for loop and next_to()
# Animates them appearing one by one with GrowFromCenter
# Then changes their colours one by one: RED, ORANGE, YELLOW, GREEN, BLUE
# Use self.play(circle.animate.set_color(...)) for each colour change

# Hint — store your circles in a list:
    # circles = []
    # for i in range(5):
    #     # create and position each circle
    #     circles.append(circle)

from manim import *
class ColourWave(Scene):
    def construct(self):

        # create 5 circles
        circles=[]                                      # create empty list
        colors=[RED, ORANGE, YELLOW, GREEN, BLUE]       # will be used in the end

        for i in range(5):                              # loop 5 times
            circle = Circle(radius=0.5, color=WHITE)    # create circles
            circles.append(circle)                      # add created circles in the empty list over the loop

            # This is the standard pattern for creating multiple objects
                # build them in a loop and store in a list.
                # Now circles[0] is the first circle, circles[4] is the last.
        
        # positon them in a row using next_to
        circles[0].move_to(LEFT*2)

        for i in range(1, 5):
            circles[i].next_to(circles[i-1], RIGHT, buff=0.5)

        # animate them appearing 1by1
        for circle in circles:
            self.play(GrowFromCenter(circle), run_time=0.5)

        self.wait(0.7)

        for i, circle in enumerate(circles):            # enumerate gives both the index i and the circle object simultaneously — so colors[i] picks the matching colour for each circle.
            self.play(
                circle.animate.set_color(colors[i]),
                run_time=0.5
            )

        self.wait(1)

        # The result:
            # five white circles appear one by one,
            # then ripple through red → orange → yellow → green → blue like a colour wave.
            # This is a great pattern for animating sequences in your physics videos
                # showing energy levels, spectral lines, or orbital shells one by one.

        # manim Pr11_colour_wave.py Manim11 --renderer=opengl -p
        # manim -pqk Pr11_colour_wave.py Manim11