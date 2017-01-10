#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        master = tk.Tk()
        super().__init__(master)
        master.minsize(width=720, height=540)
        self.pack()
        self.create_widgets()
        self.grid_widgets()
        self.grid()

    def create_widgets(self):
        self.labelHello = tk.Label(self, text='Hello')

    def grid_widgets(self):
        self.labelHello.grid(column=0, row=0)

if __name__ == '__main__':
    app = Application()
    app.master.title('高速公路交通监控专家系统')
    app.mainloop()
