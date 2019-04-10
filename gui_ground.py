from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('dark_background')
plt.rcParams['axes.facecolor'] = '#1f1f1f'
plt.rcParams['lines.color'] = 'r'

matplotlib.use("TkAgg")

fields = ['Team ID', 'Mission Time', 'Packet count', 'University']

root = Tk()
root.title("Lakshya")
root.config(bg='#4f4f4f', bd=10)

top_fr = Frame(root, bg='#4f4f4f')
top_fr.pack(side=TOP)
bottom_fr = Frame(root, bg='#4f4f4f')
bottom_fr.pack(side=TOP)

top_1 = Frame(top_fr, bg='#4f4f4f')
top_1.pack(side=LEFT, anchor=NW)
top_2 = Frame(top_fr, bg='#4f4f4f')
top_2.pack(side=LEFT, anchor=NW)
top_3 = Frame(top_fr, bg='#4f4f4f')
top_3.pack(side=LEFT, anchor=NW)

bottom_1 = Frame(bottom_fr, bg='#4f4f4f')
bottom_1.pack(side=LEFT, anchor=NW)
bottom_2 = Frame(bottom_fr, bg='#4f4f4f')
bottom_2.pack(side=LEFT, anchor=NW)


def details():
    for field in fields:
        row = Frame(top_1, bg='#4f4f4f')
        lab = Label(row, width=15, text=field, anchor='w', bg='#1f1f1f', fg='#ffffff', height=2)
        ent = Text(row, width=25, bg='#2e2e2e', fg="#ffffff", height=2, relief=FLAT)

        row.pack(side=TOP, fill=X, padx=2, pady=1, anchor=W)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT)

    soft_state()


def soft_state():
    state_label = Label(top_2, width=50, height=1, bg='black', fg='#ffffff', text='Software State')
    state_label.pack(side=TOP, anchor=W, padx=3)

    v = IntVar()
    one = Button(top_2, text='Waiting for Launch', width=50, state=NORMAL, bg='#2e2e2e', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)
    two = Button(top_2, text='Ascent', width=50, state=NORMAL, bg='#1f1f1f', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)
    three = Button(top_2, text='Rocket Deployment', width=50, state=NORMAL, bg='#2e2e2e', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)
    four = Button(top_2, text='Stabilization', width=50, state=NORMAL, bg='#1f1f1f', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)
    five = Button(top_2, text='Separation', width=50, state=NORMAL, bg='#2e2e2e', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)
    six = Button(top_2, text='Descent', width=50, state=NORMAL, bg='#1f1f1f', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)
    seven = Button(top_2, text='Landed', width=50, state=NORMAL, bg='#2e2e2e', fg='#ffffff', relief=FLAT) \
        .pack(side=TOP, anchor=W, pady=1)

    buttons()


def buttons():
    but_fr = Frame(top_2, bg='#4f4f4f')
    but_fr.pack(side=TOP, anchor=W)
    start = Button(but_fr, text=u'\u2B9E', height=2, width=12, bg='#1f1f1f', fg='#ffffff', relief=GROOVE,
                   overrelief=GROOVE, font=('Times New Roman', 12), activebackground='#4d4d4d',
                   activeforeground='#f0f0f0')
    start.pack(side=LEFT, anchor=W, pady=3, padx=2)
    reset = Button(but_fr, text=u'\u267B', height=2, width=12, bg='#1f1f1f', fg='#ffffff', relief=GROOVE,
                   overrelief=GROOVE, font=('Times New Roman', 12), activebackground='#4d4d4d',
                   activeforeground='#f0f0f0')
    reset.pack(side=LEFT, anchor=W, pady=3)
    stop = Button(but_fr, text=u'\u2718', height=2, width=12, bg='#1f1f1f', fg='#ffffff', relief=GROOVE,
                  overrelief=GROOVE, font=('Times New Roman', 12), activebackground='#4d4d4d',
                  activeforeground='#f0f0f0')
    stop.pack(side=LEFT, anchor=W, pady=3, padx=2)

    gps()


def gps():
    top_31 = Frame(top_3, bg='#4f4f4f')
    top_31.pack(side=TOP, anchor=W)
    top_32 = Frame(top_3, bg='#4f4f4f')
    top_32.pack(side=TOP, anchor=W)

    gps_label = Label(top_31, width=120, height=1, bg='black', fg='#ffffff', text='Global Positioning System')
    gps_label.pack(side=TOP, anchor=W, padx=3)

    entries = ['GPS Time', 'GPS Latitude', 'GPS Longitude', 'GPS Altitude', 'GPS SATS']

    top_321 = Frame(top_32, bg='#4f4f4f')
    top_321.pack(side=LEFT, anchor=W)
    top_322 = Frame(top_32, bg='#4f4f4f')
    top_322.pack(side=RIGHT, anchor=W)

    for entry in entries:
        row = Frame(top_321, bg='#4f4f4f')
        lab = Label(row, width=15, text=entry, anchor='w', bg='#1f1f1f', fg='#ffffff', height=3)
        ent = Text(row, width=25, bg='#2e2e2e', fg="#ffffff", height=3, relief=GROOVE)

        row.pack(side=TOP, fill=X, padx=2, anchor=W)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT)

    plots()


def plots():
    label = Label(bottom_1, width=113, height=1, bg='#2e2e2e', fg='#ffffff', text='Plots')
    label.pack(side=TOP, anchor=NW, padx=2, pady=2)

    f = Figure(figsize=(8, 9), dpi=100)

    alt = f.add_subplot(421, ylabel='Altitude')
    alt.plot([1, 2, 3, 4, 5, 6, 7, 8], [9, 6, 1, 3, 8, 9, 3, 5])

    pr = f.add_subplot(422, ylabel='Pressure')
    pr.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

    temp = f.add_subplot(423, ylabel='Temperature')
    temp.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

    gps_alt = f.add_subplot(424, ylabel='GPS Alt')
    gps_alt.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

    pitch = f.add_subplot(425, ylabel='Pitch')
    pitch.plot([1, 2, 3, 4, 5, 6, 7, 8], [9, 6, 1, 3, 8, 9, 3, 5])

    roll = f.add_subplot(426, ylabel='Roll')
    roll.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

    rpm = f.add_subplot(427, ylabel='RPM', xlabel='Time -->')
    rpm.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

    volt = f.add_subplot(428, ylabel='Voltage', xlabel='Time -->')
    volt.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

    canvas_plot = FigureCanvasTkAgg(f, bottom_1)
    canvas_plot.get_tk_widget().pack(side=TOP, anchor=NW)

    spreadsheet()


def spreadsheet():
    text = Text(bottom_2, width=88, height=34, bg='#1f1f1f', fg='#ffffff')
    text.pack(side=LEFT, anchor=NW)


def info():
    master = Tk()
    master.config(bg='#2e2e2e')
    master.title("Connection Details")
    master.resizable(0, 0)

    row_1 = Frame(master, bg='#4f4f4f')
    lab_1 = Label(row_1, width=15, text='Port', anchor=W, bg='#1f1f1f', fg='#ffffff', height=3)
    ent_1 = Text(row_1, width=25, bg='#2e2e2e', fg="#ffffff", height=3, relief=GROOVE)
    row_1.pack(side=TOP, fill=X, padx=2, anchor=W)
    lab_1.pack(side=LEFT)
    ent_1.pack(side=LEFT)

    row_2 = Frame(master, bg='#4f4f4f')
    lab_2 = Label(row_2, width=15, text='Baud Rate', anchor=W, bg='#1f1f1f', fg='#ffffff', height=3)
    ent_2 = Text(row_2, width=25, bg='#2e2e2e', fg="#ffffff", height=3, relief=GROOVE)
    row_2.pack(side=TOP, fill=X, padx=2, anchor=W)
    lab_2.pack(side=LEFT)
    ent_2.pack(side=LEFT)


menu_bar = Menu(root)
menu_bar.add_command(label='Connection details', command=info)

settings = Menu(menu_bar, tearoff=1)
settings.add_command(label='Calibrate Barometric Sensor')
settings.add_command(label='Adjust Roll/Pitch angles')

menu_bar.add_cascade(label='Calibration', menu=settings)

root.config(menu=menu_bar)

top_11 = Frame(top_1, bg='#4f4f4f')
top_11.pack(side=TOP, anchor=W)

canvas = Canvas(top_11, bg='white', height=120, width=180)
canvas.pack(side=LEFT, anchor=NW, padx=4)
can_logo = PhotoImage(file='cansatlogo.gif')
canvas.create_image(0, 0, image=can_logo, anchor=NW)

canvas_1 = Canvas(top_11, bg='black', height=120, width=120)
canvas_1.pack(side=RIGHT, anchor=NW)
off_logo = PhotoImage(file='official.gif')
canvas_1.create_image(0, 0, image=off_logo, anchor=NW)

details()

root.mainloop()
