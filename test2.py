from PIL import Image
import PySimpleGUI as sg


image=Image.open("picture.png")

layout=[[image]]

window = sg.Window("画像編集", layout, size=(600, 300))

while True:

    (event, values) = window.read() 

    print(" イベント:",event ,", 値:",values) 

    

    if event == None: 
        print("終了します． ")

        break

    elif event == "ROTATE":
        image.resize(int(number2.get()))

image.closed()

