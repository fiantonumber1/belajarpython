import time
import tkinter
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


def grafik_diam(y):
    root = tkinter.Tk()
    root.wm_title("Embedding in Tk")

    fig = Figure(figsize=(5, 4), dpi=100)
    hitungan = len(y)
    t = []
    for i in range(hitungan):
        t.append("")
        t[i] = i
    fig.add_subplot(111).plot(t, y)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect("key_press_event", on_key_press)

    def _quit():
        root.quit()  # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()
    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.

import main

U=main.u
def grafik_bergerak(U):
    GRAPH_SIZE = (500, 500)
    GRAPH_STEP_SIZE = 5

    sg.change_look_and_feel('LightGreen')

    layout = [[sg.Graph(GRAPH_SIZE, (500, 500), GRAPH_SIZE, key='-GRAPH-', background_color='lightblue'), ],
              [sg.Text('Milliseconds per sample:', size=(20, 1)),
               sg.Slider((0, 30), default_value=15, orientation='h', key='-DELAY-')],
              [sg.Text('Pixels per sample:', size=(20, 1)),
               sg.Slider((1, 30), default_value=GRAPH_STEP_SIZE, orientation='h', key='-STEP-SIZE-')],
              [sg.Button('Exit')]]

    window = sg.Window('Animated Line Graph Example', layout)

    delay = x = lastx = lasty = 0
    while True:  # Event Loop
        event, values = window.read(timeout=delay)
        if event in (None, 'Exit'):
            break
        step_size, delay = values['-STEP-SIZE-'], values['-DELAY-']
        U_max = max(U)
        y = U[int(x)]
        # get random point for graph
        if x < GRAPH_SIZE[0]:  # if still drawing initial width of graph
            window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)

        else:  # finished drawing full graph width so move each time to make room
            window['-GRAPH-'].Move(-step_size, 0)
            window['-GRAPH-'].DrawLine((lastx, lasty), (x, y), width=1)
            x -= step_size
        lastx, lasty = x, y
        x += step_size
        if x==len(U):
            grafik_bergerak(U)

    window.close()

grafik_bergerak(U)

#https://github.com/abhishek305/ProgrammingKnowlegde-Tkinter-Series/blob/master/13th/matplot%20with%20tkinter.py
