#!/usr/bin/env python

import PySimpleGUI as sg


# Usage of Graph element.


layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), 

        graph_top_right=(400, 400), background_color='blue', 

        enable_events=True, key='graph')],

        [sg.Text('Change circle color to:'), sg.Button('Red'), 

        sg.Button('Blue'), sg.Button('Move'), sg.Button('Erase')]]


window = sg.Window('Graph test', layout, finalize=True)


graph = window['graph']         # type: sg.Graph

circle = graph.draw_circle((75, 75), 25, fill_color='black', line_color='white')

point = graph.draw_point((75, 75), 10, color='green')

oval = graph.draw_oval((25, 300), (100, 280), fill_color='purple', line_color='purple')

rectangle = graph.draw_rectangle((25, 300), (100, 280), line_color='purple')

line = graph.draw_line((0, 0), (100, 100))

arc = graph.draw_arc((0, 0), (400, 400), 160, 10, style='arc', arc_color='blue')

poly = graph.draw_polygon(((10,10), (20,0), (40,200), (10,10)), fill_color='green')

text = graph.draw_text("Hi everyone!", (200, 200), color="white", font=("Arial", 30))

while True:

    event, values = window.read()

    print(event, values)

    if event == sg.WIN_CLOSED:

        break

    if event in ('Blue', 'Red'):

        #描画の属性を変更するとき

        graph.TKCanvas.itemconfig(circle, fill=event)

        if event == "Blue":

            #描画の大きさ・範囲（左上xyと右下xy座標）を変更するとき

            #x1, y1, x2, y2に現在の左上xyと右下xy座標（ただし原点左上）が入る

            x1, y1, x2, y2= graph.TKCanvas.coords(circle)

            graph.TKCanvas.coords(circle, x1, y1, x2+10, y2)


    elif event == 'Move':

        graph.move_figure(point, 10, 10)

        graph.move_figure(circle, 10, 10)

        graph.move_figure(oval, 10, 10)

        graph.move_figure(rectangle, 10, 10)

        graph.move_figure(arc, 10, 10)

        graph.move_figure(poly, 10, 10)

    

    elif event == 'Erase':

        graph.erase()


window.close()