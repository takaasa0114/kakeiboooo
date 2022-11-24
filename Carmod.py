import PySimpleGUI as sg

import Car

class Car_message(Car.Car):

    def __init__(self, name="車", pos=1, amount=3):
        self.driver=name
        self.position=pos
        self.gas=amount
        self.direction=1
        self.message=""

    def drive(self):
        if self.gas>=1:
            self.gas-=1
            self.message="ブルル、、"
            if self.direction==1:
                self.position+=1
            else:
                self.position-=1
        else:
            self.message="ガス欠で動けません！"

    def refuel(self, amount):
        self.gas+=amount
        self.message="給油します。"
    
    def turn(self):
        self.direction*=-1

    def printStatus(self):
        self.message=(f"{self.driver}さん号はいま{self.position}丁目にいます。")
        print(self.message)

car=Car_message()

layout = [

    [sg.Graph((300, 100), (0, 0), (300, 100), key="graph")],

    [sg.Button("drive"), sg.Button("turn"), sg.Button("refuel")],

    [sg.Button("printStatus")],

    [sg.Text("", key="-MESSAGE-")]

]

window = sg.Window("kettle", layout)

window.Finalize()


graph = sg.Graph((300, 100), (0, 0), (300, 100))

graph.draw_rectangle((130+int(car.position*20),20), (150+int(car.position)*20,40))

graph = window["graph"]

while True:

    event, values = window.read()


    if event is sg.WIN_CLOSED:

        break

    elif event=="drive":
        car.drive()

    elif event=="turn":
        car.turn()

    elif event=="refuel":
        car.refuel(3)

    elif event=="printStatus":
        car.printStatus()
    
    window["-MESSAGE-"].update(car.message)

    graph.erase()

    graph.draw_rectangle((130+int(car.position*20),20), (150+int(car.position*20),40))

window.close()