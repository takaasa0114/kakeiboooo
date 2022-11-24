from PIL import Image
import PySimpleGUI as sg

button=sg.Button("確定",key="kakutei")
number1=sg.Input(default_text="画像ファイル名を入力", key="-number-", size=40)
number2=sg.Input("0", key="-rotate-",size=10)
button1=sg.Button("回転", key="ROTATE")
filename=number1
picture1=sg.Image(filename, key="image")


layout=[

        [button, number1],

        [button1, number2],

        [picture1],

        ]

window = sg.Window("画像編集", layout, size=(600, 600))

while True:

    (event, values) = window.read() 

    print(" イベント:",event ,", 値:",values) 

    

    if event == None: 
        print("終了します． ")

        break

    elif event== "kakutei":
        filename=number1.get()
        picture1=sg.Image(filename, key="image")
        image1=Image.open(filename)
        tmpimage=image1
        window["image"].update(filename)

    elif event == "ROTATE":
        tmpimage=tmpimage.rotate(int(number2.get()))
        x=int(number2.get())
        tmpimage.save(str(x)+filename)
        window["image"].update(str(x)+filename)
        
        

