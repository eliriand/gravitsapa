import tkinter as tk
from datetime import time
from time import sleep

import config.globals as glob

def main():
    root = tk.Tk()
    root.title("Gravitsapa")
    canvas = tk.Canvas(root, width = glob.CANVAS_SIZE, height = glob.CANVAS_SIZE, bg='black')
    canvas.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
