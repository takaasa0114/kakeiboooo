#!/usr/bin/env python
import PySimpleGUI as sg

# Usage of Graph element.

layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), 
    graph_top_right=(400, 400), background_color='white', 
    enable_events=True, key='graph')]
    ]

window = sg.Window('Graph test', layout, finalize=True)
graph = window['graph']         # type: sg.Graph
c1 = graph.draw_circle((100, 300), 40, fill_color='black', line_color='black')
c2 = graph.draw_circle((200, 300), 40, fill_color='black', line_color='black')
c3 = graph.draw_circle((150, 250), 50, fill_color='black', line_color='black')

(event, values) = window.read()
window.close()
