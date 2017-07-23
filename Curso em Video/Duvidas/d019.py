import tkinter as tk
from time import strftime


class Clock(tk.Label):
    def __init__(self, master=None):
        super().__init__(master=master, text=strftime('%H:%M:%S'), font=('Helvetica', 80, 'bold'))
        self.run()

    def run(self):
        now = strftime('%H:%M:%S')
        if self['text'] != now:
            self['text'] = now
        self.after(90, self.run)


def clock_window():
    window = tk.Toplevel(root)
    window.title('Clock')
    clock = Clock(window)
    clock.pack()


root = tk.Tk()
root.title('Window')

btn1 = tk.Button(root, text='Open clock', width=20, height=2, command=clock_window)
btn1.pack()

root.mainloop()