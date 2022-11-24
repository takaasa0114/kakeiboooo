# coding: utf -8

import PySimpleGUI as sg # パッケージの読み込み


#レイアウトの設定

layout = [[]]


#Windowクラスのブジェクトを生成してwindowに割り当てる

window = sg.Window("シンプルウィンドウ ", layout, size=(700, 500))


#ウィンドウからイベントを読み込む

(event, values) = window.read()


#ウィンドウを閉じる

window.close()