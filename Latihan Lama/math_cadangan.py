import PySimpleGUI as sg
from random import randint
import matematika_raw

U = matematika_raw.keluaran_u() # 50 data
Bingkai_panjang =500
Bingkai_lebar = 500
GRAPH_SIZE = (Bingkai_panjang,Bingkai_lebar)
GRAPH_STEP_SIZE = 0

sg.change_look_and_feel('LightGreen')

layout = [  [sg.Graph(GRAPH_SIZE, (0,0), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue'),],
            [sg.Text('Milliseconds per sample:', size=(20,1)),
             sg.Slider((0,30), default_value=20, orientation='h', key='-DELAY-')],
            [sg.Text('Pixels per sample:', size=(20,1)),
             sg.Slider((1,30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
            [sg.Button('Exit')]]

window = sg.Window('Animated Line Graph Example', layout)

delay = x = lastx = lasty = 0
while True:                             # Event Loop
    event, values = window.read(timeout=delay)
    if event in (None, 'Exit'):
        break
    step_size, delay = values['-STEP-SIZE-'], values['-DELAY-']
    y = U[int(x)] # get random point for graph
    if x < GRAPH_SIZE[0]:               # if still drawing initial width of graph
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
    else:                               # finished drawing full graph width so move each time to make room
        window['-GRAPH-'].Move(-step_size, 0)
        window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
        x -= step_size
    lastx, lasty = x, y
    x += step_size
    if x== Bingkai_panjang:
        False



window.close()