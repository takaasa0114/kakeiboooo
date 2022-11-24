import PySimpleGUI as sg

class Car_mod(object):
    def __init__(self, name="名無し", pos=1, amount=3):
        self.driver=name
        self.position=pos
        self.gas=amount
        self.message=""

    car=()

    def turn(self, position=1):
        self.direction=position 
    
    def drive(self):
        if self.gas>=1:
            self.gas-=1
            self.message=("ブルル、、")
            if self.direction==1:
                self.position+=1
            else:
                self.position-=1
        else:
            self.message=("ガス欠で動けません！")

    def refuel(self, amount):
        self.gas+=amount

    def printStatus(self):
        self.message=(f"{self.driver}さん号はいま{self.position}丁目にいます。")
        print(self.message)

text=sg.Text("{0:.1f}さん号はいま{1:.1f}丁目にいます。".format(car.driver, car.position))
Car=Car_mod

layout=[[sg.Button("drive"), sg.Button("turn"), sg.Button("refuel")]

    [text]]

window = sg.Window("車アプリ", layout, size=(500, 300))

while True:
    (event, values) = window.read()
    print(" イベント:",event ,", 値:",values)

    if event == None: # 終了条件（クローズボタンを押したとき）

        print("終了します． ")

        break
