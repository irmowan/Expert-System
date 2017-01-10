#!/usr/bin/python
# encoding:utf-8
__author__ = 'irmo'

import tkinter as tk
import main as expert


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
        self.safety = tk.BooleanVar()
        self.lanes = tk.StringVar()
        self.lane = tk.StringVar()
        self.visibility = tk.StringVar()
        self.checkbuttonSafeDistance = tk.Checkbutton(
            self, text='与前车距离100米', variable=self.safety)
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
        self.buttonRun = tk.Button(self, text='进行监控...', command=self.run)
        self.labelOutput = tk.Label(self, text='监控结论', justify='left')
        self.labelMax = tk.Label(
            self, text='最高时速: ', anchor='w')
        self.labelMin = tk.Label(
            self, text='最低时速: ', anchor='w')
        self.labelAdvice = tk.Label(self, anchor='w')

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
        self.buttonRun.grid(column=0, row=5, pady=4)
        self.labelOutput.grid(column=0, row=6)
        self.labelMax.grid(column=0, row=7, columnspan=4)
        self.labelMin.grid(column=0, row=8, columnspan=4)
        self.labelAdvice.grid(column=0, row=9, columnspan=4)

    def get_facts(self):
        facts = ['Freeway']
        if self.safety.get():
            facts.append('Safety distance 100 meters')
        if self.lanes.get():
            facts.append(self.lanes.get())
        if self.lane.get():
            facts.append(self.lane.get())
        if self.visibility.get():
            facts.append(self.visibility.get())
        return facts

    def run(self):
        facts = self.get_facts()
        rules = expert.import_rules()
        Max, Min, Advice = expert.test_one_case(rules, facts)
        self.labelMax['text'] = '最高时速: ' + str(Max) + 'km/h'
        self.labelMin['text'] = '最低时速: ' + str(Min) + 'km/h'
        print(self.labelMax['text'])
        print(self.labelMin['text'])
        self.labelAdvice['text'] = ''
        if len(Advice) > 0:
            t = ''
            if 'Open lights' in Advice:
                t += '开启各类警示灯 '
            if 'Leave ASAP' in Advice:
                t += '在最近的出口尽快驶离高速公路'
            self.labelAdvice['text'] = '行驶建议: ' + t
            print(self.labelAdvice['text'])
        print()

if __name__ == '__main__':
    app = Application()
    app.master.title('高速公路行驶速度监控专家系统')
    app.mainloop()
