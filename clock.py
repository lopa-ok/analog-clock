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
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius, 
                                outline="black", width=2)

        for i in range(12):
            angle = math.pi / 6 * i
            x1 = self.center_x + (self.radius - 20) * math.cos(angle - math.pi / 2)
            y1 = self.center_y + (self.radius - 20) * math.sin(angle - math.pi / 2)
            x2 = self.center_x + (self.radius - 10) * math.cos(angle - math.pi / 2)
            y2 = self.center_y + (self.radius - 10) * math.sin(angle - math.pi / 2)
            self.canvas.create_line(x1, y1, x2, y2, width=2)
            
            number = str((i + 11) % 12 + 1)
            number_x = self.center_x + (self.radius - 40) * math.cos(angle - math.pi / 2)
            number_y = self.center_y + (self.radius - 40) * math.sin(angle - math.pi / 2)
            self.canvas.create_text(
                number_x,
                number_y,
                text=number,
                font=("Arial", 12),
                fill="black"
            )

    def update_clock(self):
        now = time.localtime()
        self.canvas.delete("hands")
        self.draw_hand(now.tm_hour % 12 / 12 * 360 + (now.tm_min / 60 * 30), self.radius - 60, 6, "black")
        self.draw_hand(now.tm_min / 60 * 360 + (now.tm_sec / 60 * 6), self.radius - 40, 4, "blue")
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
