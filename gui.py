#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        master = tk.Tk()
        super().__init__(master)
        master.minsize(width=240, height=180)
        # self.pack()
        self.create_widgets(master)
        self.grid_widgets()
        self.grid()

    def create_widgets(self, master):
        self.labelInput = tk.Label(self, text='路况参数')
        self.checkbuttonSafeDistance = tk.Checkbutton(self, text='与前车距离100米')
        self.lanes = 1
        self.lane = 2
        self.visibility = 3
        self.radiobuttonNoneLanes = tk.Radiobutton(
            self, text='未知车道数', variable=self.lanes)
        self.radiobuttonTwoLanes = tk.Radiobutton(
            self, text='同向二车道', variable=self.lanes, value='Two lanes')
        self.radiobuttonThreeLanes = tk.Radiobutton(
            self, text='同向三车道', variable=self.lanes, value='Three lanes')
        self.radiobuttonNoneLane = tk.Radiobutton(
            self, text='未知车道', variable=self.lane)
        self.radiobuttonLeftLane = tk.Radiobutton(
            self, text='左侧车道', variable=self.lane, value='Left lane')
        self.radiobuttonMiddleLane = tk.Radiobutton(
            self, text='中间车道', variable=self.lane, value='Middle lane')
        self.radiobuttonRightLane = tk.Radiobutton(
            self, text='右侧车道', variable=self.lane, value='Right lane')
        self.labelVisibility = tk.Label(self, text='能见度低于:')
        self.radiobuttonNoneVisibility = tk.Radiobutton(
            self, text='无', variable=self.visibility)
        self.radiobutton50Visibility = tk.Radiobutton(
            self, text='50m', variable=self.visibility, value='Visibility 50 meters')
        self.radiobutton100Visibility = tk.Radiobutton(
            self, text='100m', variable=self.visibility, value='Visibility 100 meters')
        self.radiobutton200Visibility = tk.Radiobutton(
            self, text='200m', variable=self.visibility, value='Visibility 200 meters')
        self.labelOutput = tk.Label(self, text='监控结论')
        self.labelMax = tk.Label(self, text='最高时速: ')
        self.labelMin = tk.Label(self, text='最低时速: ')
        self.labelAdvice = tk.Label(self)

    def grid_widgets(self):
        self.labelInput.grid(column=0, row=0)
        self.checkbuttonSafeDistance.grid(column=0, row=1)
        self.radiobuttonNoneLanes.grid(column=0, row=2)
        self.radiobuttonTwoLanes.grid(column=1, row=2)
        self.radiobuttonThreeLanes.grid(column=2, row=2)
        self.radiobuttonNoneLane.grid(column=0, row=3)
        self.radiobuttonLeftLane.grid(column=1, row=3)
        self.radiobuttonMiddleLane.grid(column=2, row=3)
        self.radiobuttonRightLane.grid(column=3, row=3)
        self.labelVisibility.grid(column=0, row=4)
        self.radiobuttonNoneVisibility.grid(column=1, row=4)
        self.radiobutton200Visibility.grid(column=2, row=4)
        self.radiobutton100Visibility.grid(column=3, row=4)
        self.radiobutton50Visibility.grid(column=4, row=4)
        self.labelOutput.grid(column=0, row=5)
        self.labelMax.grid(column=0, row=6)
        self.labelMin.grid(column=0, row=7)
        self.labelAdvice.grid(column=0, row=8)

if __name__ == '__main__':
    app = Application()
    app.master.title('高速公路交通监控专家系统')
    app.mainloop()
