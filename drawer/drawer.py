#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import config.globals as glob

class Drawer:
	def __init__(self, canvas):
		self.canvas = canvas

	def showObjects(self, celestial_objects):
		self.canvas.delete("all")
		canvas_x_center = self.canvas.winfo_width() / 2
		canvas_y_center = self.canvas.winfo_height() / 2
		zoom = glob.ZOOM
		for obj in celestial_objects:
			radius = math.log(obj.mass)
			self.canvas.create_oval(canvas_x_center + zoom * (obj.x - radius), canvas_y_center + zoom * (obj.y - radius), canvas_x_center + zoom * (obj.x + radius), canvas_y_center + zoom * (obj.y + radius), width=0,
									fill=obj.color)
		self.canvas.update()