#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from datetime import time
from time import sleep

import config.globals as glob

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
    root.mainloop()

if __name__ == "__main__":
    main()
