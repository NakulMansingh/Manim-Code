    # Problem 31 — physics graph

# Create a scene called ProjectileGraph that plots the trajectory of a projectile:

# y(x) = x·tan(θ) − gx²/(2v₀²cos²θ)

# Use θ = 45°, v₀ = 20 m/s, g = 9.81. Plot y vs x for x from 0 to the range R = v₀²sin(2θ)/g.

# Create axes with appropriate ranges
# Plot the trajectory in YELLOW
# Add a dot that moves along the path
# Add a title "Projectile Motion" above the axes

import numpy as np
import math, cmath
from manim import *

class ProjectileGp(Scene):
    def construct(self):

        title = Text("Projectile motion", font_size=36)
        title.move_to(UP*2.8 + RIGHT*0.7)

        theta = math.radians(45)
        v0 = 20
        g = 9.81
        
        # Range & Height of the projectile
        R = v0**2 *np.sin(2*theta)/g         # 40.77 m
        H = v0**2 *np.sin(theta)**2 / (2*g)  # 10.19 m

        axes = Axes(
            x_range=[0, R+3, 5],
            y_range=[0, H+3, 5],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE},
            tips=True
        )
        labels = axes.get_axis_labels("x\ (m)","y\ (m)").scale(1)

        def trajectory(x):
            return x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta)**2)
        
        # Defining the trajectory as a proper def function instead of a lambda — cleaner when the formula is long.
            # Manim's axes.plot() accepts both.
        
        curve = axes.plot(
            trajectory,
            x_range=[0, R],
            color=TEAL
        )

        dot= Dot(color=YELLOW).move_to(axes.c2p(0, 0))

        self.play(Write(title))
        self.play(Create(axes), Write(labels))
        self.play(Create(curve), run_time=1.5)
        
        self.play(
            MoveAlongPath(dot, curve),
            run_time=3,
            rate_func=linear
        )
        self.wait(1)

        # manim Pr30_projectile.py Manim30 --renderer=opengl -p
        # manim -pqk Pr30_projectile.py Manim30
        # manim -pqh Pr30_projectile.py Manim30
                        
        