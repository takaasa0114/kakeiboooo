# coding: utf -8

import PySimpleGUI as sg # パッケージの読み込み


#いいねの数を記録する変数

count= 0 


#テキストオブジェクトを生成して変数textに割り当て

text= sg.Text("あわせて{}いいね".format(count))


#ボタンオブジェクトを生成して変数buttonに割り当て

button= sg.Button("いいね～", key="-like-")
button2=sg.Button("よくないね～", key="-unlike-")
number1=sg.Input("0", key="-number-", size=10)
button3=sg.Button("まとめて",key="-num-")

#レイアウトを表すリストを変数layoutに割り当て

#（リストのリストを使って二次元配置．テキストとボタンを縦に並べる）

layout = [[text],

          [button, button2],
          
          [number1, button3]
          
          ]


#Windowクラスのブジェクトを生成してwindowに割り当てる

window = sg.Window("いいねカウンター ", layout, size=(300, 100))


#ウィンドウからイベントを読み込み，内容に応じて処理を繰り返す

while True:

    (event, values) = window.read() #イベントを受け付ける

    print(" イベント:",event ,", 値:",values) # 確認表示

    

    if event == None: # 終了条件（クローズボタンを押したとき）

        print("終了します． ")

        break

    

    elif event == "-like-": # いいね～ボタンが押されたかの判定

        count+= 1

        text.update("あわせて{}いいね".format(count)) #テキスト更新

    elif event == "-unlike-":

        count-=1

        text.update("あわせて{}いいね".format(count))
        
    elif event == "-num-":

        count+=int(number1.get())

        text.update("あわせて{}いいね".format(count))

    
    if count>=100:
        sg.popup("おめでとう！いいね～が100を超えました！")


        


        
        
        #ウィンドウを閉じる

window.close()