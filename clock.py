import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        self.center_x = 200
        self.center_y = 200
        self.radius = 150
        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        for i in range(12):
            angle = math.pi / 6 * i
            x1 = self.center_x + self.radius * math.cos(angle)
            y1 = self.center_y - self.radius * math.sin(angle)
            x2 = self.center_x + (self.radius - 20) * math.cos(angle)
            y2 = self.center_y - (self.radius - 20) * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2)

    def update_clock(self):
        self.canvas.delete("hands")
        now = time.localtime()
        self.draw_hand(now.tm_hour % 12 / 12 * 360, self.radius - 60, 6, "black")
        self.draw_hand(now.tm_min / 60 * 360, self.radius - 40, 4, "blue")
        self.draw_hand(now.tm_sec / 60 * 360, self.radius - 20, 2, "red")
        self.root.after(1000, self.update_clock)

    def draw_hand(self, degrees, length, width, color):
        angle = math.radians(degrees - 90)
        x = self.center_x + length * math.cos(angle)
        y = self.center_y + length * math.sin(angle)
        self.canvas.create_line(self.center_x, self.center_y, x, y, width=width, fill=color, tags="hands")

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClock(root)
    root.mainloop()
