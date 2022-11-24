import PySimpleGUI as sg
from PIL import Image

class photo:
    def __init__(self,n):
        self.filename=n
        self.resized_image=""
        self.right=300
        self.left=300
        image=Image.open(self.filename)

    def sizechange(self,a,b):
        self.right+=a
        self.left+=b
        image=Image.open(self.filename)
        self.resized_image= image.resize((self.right,self.left))

box=sg.InputText()
x=0

layout=[[sg.Text("ファイル"),box,sg.Button("表示",key="show")],
        [sg.Button("拡大",key="big"),sg.Button("縮小",key="small")],
        [sg.Image("",key="image")]]

window=sg.Window("画像サイズ変更アプリ",layout,size=(600,600))

while True :
    event, values = window.read()
   
    if event ==None :
        break

    if event=="show":
        pic= photo(box.get())
        window["image"].update(pic.filename)
    
    if event=="big":
            pic.sizechange(30,30)
            x+=1
            pic.resized_image.save(str(x)+pic.filename)
            window["image"].update(str(x)+pic.filename)
            f= open("log.txt","a", encoding='utf-8')
            if x>0:
                f.write(" "+(str(x-1)+pic.filename)+","+str(x)+"段階拡大,"+(str(x)+pic.filename)+"\n")
            if x<0:
                f.write(" "+(str(x-1)+pic.filename)+","+str(-x)+"段階縮小,"+(str(x)+pic.filename)+"\n")
            f.close()

    if event=="small":
            pic.sizechange(-30,-30)
            x-=1
            pic.resized_image.save(str(x)+pic.filename)
            window["image"].update(str(x)+pic.filename)
            f= open("log.txt","a", encoding='utf-8')
            if x>0:
                f.write(" "+(str(x+1)+pic.filename)+","+str(x)+"段階拡大,"+(str(x)+pic.filename)+"\n")
            if x<0:
                f.write(" "+(str(x+1)+pic.filename)+","+str(-x)+"段階縮小,"+(str(x)+pic.filename)+"\n")
            f.close()


window.close()