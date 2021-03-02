from tkinter import *
import datetime

class Sticker():
    def __init__(self, x, y, left):
        self.x = x
        self.y = y
        self.left = left

    def build(self, root):
        window = Toplevel(root)
        window.geometry("+{}+{}".format(self.x, self.y))
        window.overrideredirect(True)
        window.wm_attributes("-topmost" ,1)
        window.wm_attributes("-transparentcolor", "black")
        window.resizable(0, 0)

        label = Label(window, font=("D2coding", 24, 'bold'), bg="black", fg="white")
        label.pack()

        def clock():
            now = datetime.datetime.today()
            left = datetime.datetime(*self.left) - now
            label.config(text = int(left.total_seconds()))
            label.after(1, clock)

        clock()

if __name__ == '__main__':
    root = Tk()
    root.overrideredirect(True)
    root.withdraw()

    timer = Sticker(x=1400, y=800, left=(2021, 3, 13, 9, 0, 0)) #time to go home
    timer.build(root)

    root.mainloop()