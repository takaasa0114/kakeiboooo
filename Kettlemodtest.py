#Kettleクラスを継承してディスプレイみたいなメッセージをあらわすインスタンス変数を追加

#すぐにprintせずにインスタンス変数messageに表示したい文字列を割り当てるようにしています．

#こうするとメッセージをGUIで受け取れるので便利．

import PySimpleGUI as sg

import Kettle


class Kettle_message(Kettle.Kettle):

 

    def __init__(self, maxw=1000.0):

        super().__init__(maxw)

        self.message = ""

 

    def putWater(self, amount=100, temperature=20):

        self.message = "水を入れます。"

        super().putWater()

 

    def printStatus(self):

        self.message = "容量{0:.1f}mlのポットには{1:.1f}℃のお湯が{2:.1f}mlはいっています。".format(self.maxwater, self.temp, self.water)

        print(self.message)

 

    def heat(self):

        self.message = "水をあたためています。"

        super().heat()

 

    def pour(self):

        self.message = "{0:.1f}℃のお湯を{1:.1f}ml注ぎました．".format(self.temp, self.water)

        self.super().pour()



#ここからアプリの定義

kettle = Kettle_message()


layout = [

    [sg.Graph((300, 100), (0, 0), (300, 100), key="graph")],

    [sg.Button("putWater"), sg.Button("printStatus")],

    [sg.Text("", key="-MESSAGE-")]

]


window = sg.Window("kettle", layout)

window.Finalize()


graph = sg.Graph((300, 100), (0, 0), (300, 100))


graph = window["graph"]

graph.draw_rectangle((20, 20), (40, 20 + int(60 * kettle.water / 1000)), fill_color="blue")


while True:

    event, values = window.read()


    if event is sg.WIN_CLOSED:

        break

    elif event == "putWater":

        kettle.putWater()

    elif event == "printStatus":

        kettle.printStatus()

    window["-MESSAGE-"].update(kettle.message)

    graph.erase()

    graph.draw_rectangle((20, 20), (40, 20 + int(60 * kettle.water / 1000)), fill_color="blue")


window.close()