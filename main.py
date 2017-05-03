#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from engine.gravity_engine import Universe, CelestialBody
from drawer.drawer import Drawer
from time import sleep

import config.globals as glob

def zoom_in(event):
    glob.ZOOM *= 1.5

def zoom_out(event):
    glob.ZOOM /= 1.5

def pause(event):
    glob.RUNNING = False

def resume(event):
    glob.RUNNING = True

def main():
    root = tk.Tk()
    root.title("Gravitsapa")
    zoom_in_button = tk.Button(root, text="Zoom In")
    zoom_out_button = tk.Button(root, text="Zoom Out")
    resume_button = tk.Button(root, text="Resume")
    pause_button = tk.Button(root, text="Pause")
    zoom_in_button.grid(row=0, column=0)
    zoom_out_button.grid(row=0, column=1)
    resume_button.grid(row=0, column=2)
    pause_button.grid(row=0, column=3)
    canvas = tk.Canvas(root, width = glob.CANVAS_SIZE, height = glob.CANVAS_SIZE, bg='black')
    canvas.grid(row=1, column=0, columnspan=4, sticky=tk.E+tk.W)

    zoom_in_button.bind("<Button-1>", zoom_in)
    zoom_out_button.bind("<Button-1>", zoom_out)
    pause_button.bind("<Button-1>", pause)
    resume_button.bind("<Button-1>", resume)

    universe = Universe([
        CelestialBody("Sun", "yellow", 5 * 10 ** 14, 0, 0, 0, 0),
        CelestialBody("Earth", "blue", 30, 50, 60, -15, 15),
        CelestialBody("Mars", "red", 40, 70, 70, 10, 5)
    ])

    drawer = Drawer(canvas)
    while True:
        drawer.showObjects(universe.celestial_bodies)
        if glob.RUNNING:
            universe.get_next_state()
        sleep(glob.DT)

    root.mainloop()

if __name__ == "__main__":
    main()
