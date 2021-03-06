#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from config.globals import G, DT

class Universe:

    def __init__(self, celestial_bodies):
        self.celestial_bodies = celestial_bodies

    def debug(self):
        state = "Current state:\n"
        for celestial_body in self.celestial_bodies:
            state = ("{0}\t{1} is in ({2}, {3}), current velocity ({4}, {5});\n".format(
                state,
                celestial_body.name,
                "%0.2f" % celestial_body.x,
                "%0.2f" % celestial_body.y,
                "%0.2f" % celestial_body.vx,
                "%0.2f" % celestial_body.vy)
            )
        return state

    def get_current_state(self):
        return self.celestial_bodies

    def get_next_state(self):
        new_bodies = []
        # calculating current acceleration for each body
        # a = -G * sum (m_k * r_oriented / r^3)
        for current_body in self.celestial_bodies:
            ax = 0
            ay = 0
            for other_body in self.celestial_bodies:
                # TODO: better comparison of objects!
                # (could have same names)
                if current_body.name != other_body.name:
                    # orientation of the vector is important!
                    rx = current_body.x - other_body.x
                    ry = current_body.y - other_body.y
                    r = math.hypot(
                        current_body.x - other_body.x,
                        current_body.y - other_body.y
                    )
                    ax += other_body.mass * rx / r ** 3
                    ay += other_body.mass * ry / r ** 3
            ax *= -G
            ay *= -G

            new_bodies.append(
                CelestialBody(
                    current_body.name,
                    current_body.color,
                    current_body.mass,
                    # (x,y)_new = (x,y)_old + v_old * dt + a * dt^2
                    current_body.x + current_body.vx * DT + ax * DT ** 2,
                    current_body.y + current_body.vy * DT + ay * DT ** 2,
                    # v_new = v_old + a * dt
                    current_body.vx + ax * DT,
                    current_body.vy + ay * DT
                )
            )

        self.celestial_bodies = new_bodies
        return self.celestial_bodies


class CelestialBody:

    # Initialization of an object
    def __init__(self, name, color, mass, x, y, vx, vy):
        self.name = name
        self.color = color
        self.mass = float(mass)
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)


if __name__ == "__main__":
    universe = Universe([
        CelestialBody("Sun", "yellow", 5*10**14, 0, 0, 0, 0),
        CelestialBody("Earth", "blue", 30, 50, 60, -15, 15),
        CelestialBody("Mars", "red", 40, 70, 70, 10, 5)
    ])

    universe.debug()
    universe.get_next_state()
    universe.debug()