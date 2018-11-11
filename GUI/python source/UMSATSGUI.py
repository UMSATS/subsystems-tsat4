#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    Jun 10, 2018 01:47:47 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import UMSATSGUI_support


def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root

    root = Tk()
    UMSATSGUI_support.set_Tk_var()
    top = UMSATS(root)
    UMSATSGUI_support.init(root, top)
    root.protocol("WM_DELETE_WINDOW", UMSATSGUI_support.destroy_window)  # use custom closing function
    root.mainloop()


w = None


def create_UMSATS(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    UMSATSGUI_support.set_Tk_var()
    top = UMSATS(w)
    UMSATSGUI_support.init(w, top, *args, **kwargs)
    return w, top


class UMSATS:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
           top is the toplevel containing window."""

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1250x700+300+88")
        top.title("UMSATS")
        top.configure(background="#3d3d3d")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.frameTerminal = LabelFrame(top)
        self.frameTerminal.place(relx=0.01, rely=0.02, relheight=0.96, relwidth=0.46)
        self.frameTerminal.configure(relief=GROOVE)
        self.frameTerminal.configure(foreground="black")
        self.frameTerminal.configure(text='''Terminals''')
        self.frameTerminal.configure(background="#d9d9d9")
        self.frameTerminal.configure(highlightbackground="#d9d9d9")
        self.frameTerminal.configure(highlightcolor="black")
        self.frameTerminal.configure(width=310)

        self.Listbox1 = Listbox(self.frameTerminal)
        self.Listbox1.place(relx=0.03, rely=0.1, relheight=0.35, relwidth=0.92, y=-12, h=12)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(highlightbackground="#d9d9d9")
        self.Listbox1.configure(highlightcolor="black")
        self.Listbox1.configure(selectbackground="#c4c4c4")
        self.Listbox1.configure(selectforeground="black")
        self.Listbox1.configure(width=284)

        self.Listbox2 = Listbox(self.frameTerminal)
        self.Listbox2.place(relx=0.03, rely=0.59, relheight=0.35, relwidth=0.92, y=-12, h=12)
        self.Listbox2.configure(background="white")
        self.Listbox2.configure(disabledforeground="#a3a3a3")
        self.Listbox2.configure(font="TkFixedFont")
        self.Listbox2.configure(foreground="#000000")
        self.Listbox2.configure(highlightbackground="#d9d9d9")
        self.Listbox2.configure(highlightcolor="black")
        self.Listbox2.configure(selectbackground="#c4c4c4")
        self.Listbox2.configure(selectforeground="black")
        self.Listbox2.configure(width=284)

        self.Terminal1Label = Label(self.frameTerminal)
        self.Terminal1Label.place(relx=0.39, rely=0.04, height=21, width=120, y=-12)
        self.Terminal1Label.configure(activebackground="#f9f9f9")
        self.Terminal1Label.configure(activeforeground="black")
        self.Terminal1Label.configure(background="#d9d9d9")
        self.Terminal1Label.configure(disabledforeground="#a3a3a3")
        self.Terminal1Label.configure(foreground="#000000")
        self.Terminal1Label.configure(highlightbackground="#d9d9d9")
        self.Terminal1Label.configure(highlightcolor="black")
        self.Terminal1Label.configure(text='''GUI Commands''')
        self.Terminal1Label.configure(width=76)

        self.Terminal2Label = Label(self.frameTerminal)
        self.Terminal2Label.place(relx=0.30, rely=0.53, height=21, width=200, y=-12)
        self.Terminal2Label.configure(activebackground="#f9f9f9")
        self.Terminal2Label.configure(activeforeground="black")
        self.Terminal2Label.configure(background="#d9d9d9")
        self.Terminal2Label.configure(disabledforeground="#a3a3a3")
        self.Terminal2Label.configure(foreground="#000000")
        self.Terminal2Label.configure(highlightbackground="#d9d9d9")
        self.Terminal2Label.configure(highlightcolor="black")
        self.Terminal2Label.configure(text='''CDH Scheduler Messages''')
        self.Terminal2Label.configure(width=76)

        self.Command1 = Entry(self.frameTerminal)
        self.Command1.configure(background="white")
        self.Command1.configure(disabledforeground="#a3a3a3")
        self.Command1.configure(font="TkFixedFont")
        self.Command1.configure(foreground="#000000")
        self.Command1.configure(highlightbackground="#d9d9d9")
        self.Command1.configure(highlightcolor="black")
        self.Command1.configure(insertbackground="black")
        self.Command1.configure(selectbackground="#c4c4c4")
        self.Command1.configure(selectforeground="black")
        self.Command1.configure(textvariable=UMSATSGUI_support.cmd1Text)
        self.Command1.bind('<Return>', lambda e: UMSATSGUI_support.command1_enter(e, self.Listbox1))

        self.Command1Label = Label(self.frameTerminal)
        self.Command1Label.configure(activebackground="#f9f9f9")
        self.Command1Label.configure(activeforeground="black")
        self.Command1Label.configure(background="#d9d9d9")
        self.Command1Label.configure(disabledforeground="#a3a3a3")
        self.Command1Label.configure(foreground="#000000")
        self.Command1Label.configure(highlightbackground="#d9d9d9")
        self.Command1Label.configure(highlightcolor="black")
        self.Command1Label.configure(text='''Command Line 1''')
        self.Command1Label.configure(width=127)

        self.Command2Label = Label(self.frameTerminal)
        self.Command2Label.configure(activebackground="#f9f9f9")
        self.Command2Label.configure(activeforeground="black")
        self.Command2Label.configure(background="#d9d9d9")
        self.Command2Label.configure(disabledforeground="#a3a3a3")
        self.Command2Label.configure(foreground="#000000")
        self.Command2Label.configure(highlightbackground="#d9d9d9")
        self.Command2Label.configure(highlightcolor="black")
        self.Command2Label.configure(text='''Command Line 2''')
        self.Command2Label.configure(width=124)

        self.Command2 = Entry(self.frameTerminal)
        self.Command2.configure(background="white")
        self.Command2.configure(disabledforeground="#a3a3a3")
        self.Command2.configure(font="TkFixedFont")
        self.Command2.configure(foreground="#000000")
        self.Command2.configure(highlightbackground="#d9d9d9")
        self.Command2.configure(highlightcolor="black")
        self.Command2.configure(insertbackground="black")
        self.Command2.configure(selectbackground="#c4c4c4")
        self.Command2.configure(selectforeground="black")
        self.Command2.configure(textvariable=UMSATSGUI_support.cmd2Text)
        self.Command2.bind('<Return>', lambda e: UMSATSGUI_support.command2_enter(e, self.Listbox2))

        self.ModuleFrameLabel = LabelFrame(top)
        self.ModuleFrameLabel.place(relx=0.47, rely=0.02, relheight=0.96, relwidth=0.52)
        self.ModuleFrameLabel.configure(relief=GROOVE)
        self.ModuleFrameLabel.configure(foreground="black")
        self.ModuleFrameLabel.configure(text='''Controller''')
        self.ModuleFrameLabel.configure(background="#d9d9d9")
        self.ModuleFrameLabel.configure(highlightbackground="#d9d9d9")
        self.ModuleFrameLabel.configure(highlightcolor="black")
        self.ModuleFrameLabel.configure(width=350)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TabsController = ttk.Notebook(self.ModuleFrameLabel)
        self.TabsController.place(relx=0.03, rely=0.04, relheight=0.60, relwidth=0.9, y=-12, h=12)
        self.TabsController.configure(width=314)
        self.TabsController.configure(takefocus="")
        self.TabsController_t0 = Frame(self.TabsController)
        self.TabsController.add(self.TabsController_t0, padding=3)
        self.TabsController.tab(0, text="Power", compound="left", underline="-1",)
        self.TabsController_t0.configure(background="#d9d9d9")
        self.TabsController_t0.configure(highlightbackground="#d9d9d9")
        self.TabsController_t0.configure(highlightcolor="black")
        self.TabsController_t1 = Frame(self.TabsController)
        self.TabsController.add(self.TabsController_t1, padding=3)
        self.TabsController.tab(1, text="Payload", compound="left", underline="-1",)
        self.TabsController_t1.configure(background="#d9d9d9")
        self.TabsController_t1.configure(highlightbackground="#d9d9d9")
        self.TabsController_t1.configure(highlightcolor="black")
        self.TabsController_t2 = Frame(self.TabsController)
        self.TabsController.add(self.TabsController_t2, padding=3)
        self.TabsController.tab(2, text="Ground Control", compound="none", underline="-1", )
        self.TabsController_t2.configure(background="#d9d9d9")
        self.TabsController_t2.configure(highlightbackground="#d9d9d9")
        self.TabsController_t2.configure(highlightcolor="black")


        self.TabsController_t3 = Frame(self.TabsController)
        self.TabsController.add(self.TabsController_t3, padding=3)
        self.TabsController.tab(3, text="Communications", compound="none", underline="-1",)
        self.TabsController_t3.configure(background="#d9d9d9")
        self.TabsController_t3.configure(highlightbackground="#d9d9d9")
        self.TabsController_t3.configure(highlightcolor="black")

        self.TabsController_t4 = Frame(self.TabsController)
        self.TabsController.add(self.TabsController_t4, padding=3)
        self.TabsController.tab(4, text="Settings", compound="none", underline="-1",)
        self.TabsController_t4.configure(background="#d9d9d9")
        self.TabsController_t4.configure(highlightbackground="#d9d9d9")
        self.TabsController_t4.configure(highlightcolor="black")

        # Comms Butons
        self.btnComms1 = Button(self.TabsController_t3)
        self.btnComms1.place(relx=0.15, rely=0.20, height=24, width=130)
        self.btnComms1.configure(activebackground="#d9d9d9")
        self.btnComms1.configure(activeforeground="#000000")
        self.btnComms1.configure(background="#d9d9d9")
        self.btnComms1.configure(disabledforeground="#a3a3a3")
        self.btnComms1.configure(foreground="#000000")
        self.btnComms1.configure(highlightbackground="#d9d9d9")
        self.btnComms1.configure(highlightcolor="black")
        self.btnComms1.configure(pady="0")
        self.btnComms1.configure(text='''Start Radio Demo''')
        self.btnComms1.bind('<Button-1>', lambda e: UMSATSGUI_support.sendComms(e,self.frameTerminal,0))

        self.btnComms2 = Button(self.TabsController_t3)
        self.btnComms2.place(relx=0.55, rely=0.20, height=24, width=130)
        self.btnComms2.configure(activebackground="#d9d9d9")
        self.btnComms2.configure(activeforeground="#000000")
        self.btnComms2.configure(background="#d9d9d9")
        self.btnComms2.configure(disabledforeground="#a3a3a3")
        self.btnComms2.configure(foreground="#000000")
        self.btnComms2.configure(highlightbackground="#d9d9d9")
        self.btnComms2.configure(highlightcolor="black")
        self.btnComms2.configure(pady="0")
        self.btnComms2.configure(text='''Stop Radio Demo''')
        self.btnComms2.bind('<Button-1>', lambda e: UMSATSGUI_support.sendComms(e,self.frameTerminal,1))

        self.entryPower = Entry(self.TabsController_t0)
        self.entryPower.place(relx=0.19, rely=0.39, height=20, relwidth=0.59)
        self.entryPower.configure(background="white")
        self.entryPower.configure(disabledforeground="#a3a3a3")
        self.entryPower.configure(font="TkFixedFont")
        self.entryPower.configure(foreground="#000000")
        self.entryPower.configure(highlightbackground="#d9d9d9")
        self.entryPower.configure(highlightcolor="black")
        self.entryPower.configure(insertbackground="black")
        self.entryPower.configure(selectbackground="#c4c4c4")
        self.entryPower.configure(selectforeground="black")
        self.entryPower.configure(width=184)
        self.entryPower.configure(textvariable=UMSATSGUI_support.powerInput)

        self.btnPowerSet = Button(self.TabsController_t0)
        self.btnPowerSet.place(relx=0.84, rely=0.39, height=24, width=47)
        self.btnPowerSet.configure(activebackground="#d9d9d9")
        self.btnPowerSet.configure(activeforeground="#000000")
        self.btnPowerSet.configure(background="#d9d9d9")
        self.btnPowerSet.configure(disabledforeground="#a3a3a3")
        self.btnPowerSet.configure(foreground="#000000")
        self.btnPowerSet.configure(highlightbackground="#d9d9d9")
        self.btnPowerSet.configure(highlightcolor="black")
        self.btnPowerSet.configure(pady="0")
        self.btnPowerSet.configure(text='''Set''')
        self.btnPowerSet.configure(width=47)
        self.btnPowerSet.bind('<Button-1>', lambda e: UMSATSGUI_support.sendPower(e, self.frameTerminal))

        self.powerValue_Label = Label(self.TabsController_t0)
        self.powerValue_Label.place(relx=0.03, rely=0.22, height=21, width=114)
        self.powerValue_Label.configure(activebackground="#f9f9f9")
        self.powerValue_Label.configure(activeforeground="black")
        self.powerValue_Label.configure(background="#d9d9d9")
        self.powerValue_Label.configure(disabledforeground="#a3a3a3")
        self.powerValue_Label.configure(foreground="#000000")
        self.powerValue_Label.configure(highlightbackground="#d9d9d9")
        self.powerValue_Label.configure(highlightcolor="black")
        self.powerValue_Label.configure(text='''Value (0 - 100 %)''')
        self.powerValue_Label.configure(width=114)

        # self.btnPayLoadSet = Button(self.TabsController_t1)
        # self.btnPayLoadSet.place(relx=0.81, rely=0.28, height=24, width=47)
        # self.btnPayLoadSet.configure(activebackground="#d9d9d9")
        # self.btnPayLoadSet.configure(activeforeground="#000000")
        # self.btnPayLoadSet.configure(background="#d9d9d9")
        # self.btnPayLoadSet.configure(disabledforeground="#a3a3a3")
        # self.btnPayLoadSet.configure(foreground="#000000")
        # self.btnPayLoadSet.configure(highlightbackground="#d9d9d9")
        # self.btnPayLoadSet.configure(highlightcolor="black")
        # self.btnPayLoadSet.configure(pady="0")
        # self.btnPayLoadSet.configure(text='''Set''')

        self.payload_Well_Input = ttk.Combobox(self.TabsController_t1)
        self.payload_Well_Input.place(relx=0.19, rely=0.28, height=23, relwidth=0.59)
        self.payload_Well_Input.configure(background="white")
        self.payload_Well_Input.configure(font="TkFixedFont")
        self.payload_Well_Input.configure(takefocus="")
        self.payload_Well_Input.configure(textvariable=UMSATSGUI_support.payloadWellInput)
        self.payload_Well_Input.configure(postcommand= lambda: UMSATSGUI_support.showWells(self.payload_Well_Input))


        self.wellNumber_Label = Label(self.TabsController_t1)
        self.wellNumber_Label.place(relx=0.03, rely=0.11, height=21, width=104)
        self.wellNumber_Label.configure(activebackground="#f9f9f9")
        self.wellNumber_Label.configure(activeforeground="black")
        self.wellNumber_Label.configure(background="#d9d9d9")
        self.wellNumber_Label.configure(disabledforeground="#a3a3a3")
        self.wellNumber_Label.configure(foreground="#000000")
        self.wellNumber_Label.configure(highlightbackground="#d9d9d9")
        self.wellNumber_Label.configure(highlightcolor="black")
        self.wellNumber_Label.configure(text='''Well # (Max: 5)''')

        self.wellValue_Label = Label(self.TabsController_t1)
        self.wellValue_Label.place(relx=0.0, rely=0.44, height=21, width=65)
        self.wellValue_Label.configure(activebackground="#f9f9f9")
        self.wellValue_Label.configure(activeforeground="black")
        self.wellValue_Label.configure(background="#d9d9d9")
        self.wellValue_Label.configure(disabledforeground="#a3a3a3")
        self.wellValue_Label.configure(foreground="#000000")
        self.wellValue_Label.configure(highlightbackground="#d9d9d9")
        self.wellValue_Label.configure(highlightcolor="black")
        self.wellValue_Label.configure(text='''Value''')

        self.payload_Value_Input = Entry(self.TabsController_t1)
        self.payload_Value_Input.place(relx=0.19, rely=0.61, height=20, relwidth=0.59)
        self.payload_Value_Input.configure(background="white")
        self.payload_Value_Input.configure(disabledforeground="#a3a3a3")
        self.payload_Value_Input.configure(font="TkFixedFont")
        self.payload_Value_Input.configure(foreground="#000000")
        self.payload_Value_Input.configure(highlightbackground="#d9d9d9")
        self.payload_Value_Input.configure(highlightcolor="black")
        self.payload_Value_Input.configure(insertbackground="black")
        self.payload_Value_Input.configure(selectbackground="#c4c4c4")
        self.payload_Value_Input.configure(selectforeground="black")
        self.payload_Value_Input.configure(textvariable=UMSATSGUI_support.payloadValueInput)

        self.btnPayload2Set = Button(self.TabsController_t1)
        self.btnPayload2Set.place(relx=0.81, rely=0.61, height=24, width=47)
        self.btnPayload2Set.configure(activebackground="#d9d9d9")
        self.btnPayload2Set.configure(activeforeground="#000000")
        self.btnPayload2Set.configure(background="#d9d9d9")
        self.btnPayload2Set.configure(disabledforeground="#a3a3a3")
        self.btnPayload2Set.configure(foreground="#000000")
        self.btnPayload2Set.configure(highlightbackground="#d9d9d9")
        self.btnPayload2Set.configure(highlightcolor="black")
        self.btnPayload2Set.configure(pady="0")
        self.btnPayload2Set.configure(text='''Set''')
        self.btnPayload2Set.bind('<Button-1>', lambda e: UMSATSGUI_support.sendPayload(e, self.frameTerminal))

        self.entryGroundControl = ttk.Combobox(self.TabsController_t2)
        self.entryGroundControl.place(relx=0.19, rely=0.20, height=23, relwidth=0.59)
        self.entryGroundControl.configure(background="white")
        self.entryGroundControl.configure(font="TkFixedFont")
        self.entryGroundControl.configure(takefocus="")
        self.entryGroundControl.configure(textvariable=UMSATSGUI_support.groundWellInput)
        self.entryGroundControl.configure(postcommand=lambda: UMSATSGUI_support.showWells(self.entryGroundControl))

        self.btnGroundControlSet = Button(self.TabsController_t2)
        self.btnGroundControlSet.place(relx=0.81, rely=0.20, height=24, width=47)
        self.btnGroundControlSet.configure(activebackground="#d9d9d9")
        self.btnGroundControlSet.configure(activeforeground="#000000")
        self.btnGroundControlSet.configure(background="#d9d9d9")
        self.btnGroundControlSet.configure(disabledforeground="#a3a3a3")
        self.btnGroundControlSet.configure(foreground="#000000")
        self.btnGroundControlSet.configure(highlightbackground="#d9d9d9")
        self.btnGroundControlSet.configure(highlightcolor="black")
        self.btnGroundControlSet.configure(pady="0")
        self.btnGroundControlSet.configure(text='''Off''')
        self.btnGroundControlSet.bind('<Button-1>', lambda e: UMSATSGUI_support.sendGroundOff(e, self.frameTerminal))

        self.btnGroundControlDump = Button(self.TabsController_t2)
        self.btnGroundControlDump.place(relx=0.19, rely=0.80, height=24, width=160)
        self.btnGroundControlDump.configure(activebackground="#d9d9d9")
        self.btnGroundControlDump.configure(activeforeground="#000000")
        self.btnGroundControlDump.configure(background="#d9d9d9")
        self.btnGroundControlDump.configure(disabledforeground="#a3a3a3")
        self.btnGroundControlDump.configure(foreground="#000000")
        self.btnGroundControlDump.configure(highlightbackground="#d9d9d9")
        self.btnGroundControlDump.configure(highlightcolor="black")
        self.btnGroundControlDump.configure(pady="0")
        self.btnGroundControlDump.configure(text='''Dump Payload Data''')
        self.btnGroundControlDump.bind('<Button-1>', lambda e: UMSATSGUI_support.sendDumpPayload(e,self.frameTerminal))

        self.wellNumGC_Label = Label(self.TabsController_t2)
        self.wellNumGC_Label.place(relx=0.03, rely=0.11, height=21, width=104)
        self.wellNumGC_Label.configure(activebackground="#f9f9f9")
        self.wellNumGC_Label.configure(activeforeground="black")
        self.wellNumGC_Label.configure(background="#d9d9d9")
        self.wellNumGC_Label.configure(disabledforeground="#a3a3a3")
        self.wellNumGC_Label.configure(foreground="#000000")
        self.wellNumGC_Label.configure(highlightbackground="#d9d9d9")
        self.wellNumGC_Label.configure(highlightcolor="black")
        self.wellNumGC_Label.configure(text='''Well # (Max: 5)''')
        self.wellNumGC_Label.configure(width=104)

        self.timeGC_Label = Label(self.TabsController_t2)
        self.timeGC_Label.place(relx=0.06, rely=0.35, height=21, width=56)
        self.timeGC_Label.configure(activebackground="#f9f9f9")
        self.timeGC_Label.configure(activeforeground="black")
        self.timeGC_Label.configure(background="#d9d9d9")
        self.timeGC_Label.configure(disabledforeground="#a3a3a3")
        self.timeGC_Label.configure(foreground="#000000")
        self.timeGC_Label.configure(highlightbackground="#d9d9d9")
        self.timeGC_Label.configure(highlightcolor="black")
        self.timeGC_Label.configure(text='''Time(s)''')
        self.timeGC_Label.configure(width=56)

        self.btnGroundControl2Set = Button(self.TabsController_t2)
        self.btnGroundControl2Set.place(relx=0.81, rely=0.42, height=24, width=47)
        self.btnGroundControl2Set.configure(activebackground="#d9d9d9")
        self.btnGroundControl2Set.configure(activeforeground="#000000")
        self.btnGroundControl2Set.configure(background="#d9d9d9")
        self.btnGroundControl2Set.configure(disabledforeground="#a3a3a3")
        self.btnGroundControl2Set.configure(foreground="#000000")
        self.btnGroundControl2Set.configure(highlightbackground="#d9d9d9")
        self.btnGroundControl2Set.configure(highlightcolor="black")
        self.btnGroundControl2Set.configure(pady="0")
        self.btnGroundControl2Set.configure(text='''On''')
        self.btnGroundControl2Set.bind('<Button-1>', lambda e: UMSATSGUI_support.sendGroundOn(e, self.frameTerminal))

        self.ADCCombobox1 = ttk.Combobox(self.TabsController_t2)
        self.ADCCombobox1.place(relx=0.19, rely=0.60, height=23, relwidth=0.59)
        self.ADCCombobox1.configure(textvariable=UMSATSGUI_support.ADC_Num)
        self.ADCCombobox1.configure(takefocus="")
        self.ADCCombobox1.configure(postcommand=lambda: UMSATSGUI_support.showADCs(self.ADCCombobox1))

        self.LabelADC = Label(self.TabsController_t2)
        self.LabelADC.place(relx=0.07, rely=0.55, height=21, width=50)
        self.LabelADC.configure(activebackground="#f9f9f9")
        self.LabelADC.configure(activeforeground="black")
        self.LabelADC.configure(background="#d9d9d9")
        self.LabelADC.configure(disabledforeground="#a3a3a3")
        self.LabelADC.configure(foreground="#000000")
        self.LabelADC.configure(highlightbackground="#d9d9d9")
        self.LabelADC.configure(highlightcolor="black")
        self.LabelADC.configure(text='''ADC #:''')

        self.btnGroundControlADC = Button(self.TabsController_t2)
        self.btnGroundControlADC.place(relx=0.81, rely=0.60, height=24, width=47)
        self.btnGroundControlADC.configure(activebackground="#d9d9d9")
        self.btnGroundControlADC.configure(activeforeground="#000000")
        self.btnGroundControlADC.configure(background="#d9d9d9")
        self.btnGroundControlADC.configure(disabledforeground="#a3a3a3")
        self.btnGroundControlADC.configure(foreground="#000000")
        self.btnGroundControlADC.configure(highlightbackground="#d9d9d9")
        self.btnGroundControlADC.configure(highlightcolor="black")
        self.btnGroundControlADC.configure(pady="0")
        self.btnGroundControlADC.configure(text='''Send''')
        self.btnGroundControlADC.bind('<Button-1>', lambda e: UMSATSGUI_support.sendADC(e, self.frameTerminal))

        self.entry_GC_Time = Entry(self.TabsController_t2)
        self.entry_GC_Time.place(relx=0.19, rely=0.42,height=20, relwidth=0.59)
        self.entry_GC_Time.configure(background="white")
        self.entry_GC_Time.configure(disabledforeground="#a3a3a3")
        self.entry_GC_Time.configure(font="TkFixedFont")
        self.entry_GC_Time.configure(foreground="#000000")
        self.entry_GC_Time.configure(highlightbackground="#d9d9d9")
        self.entry_GC_Time.configure(highlightcolor="black")
        self.entry_GC_Time.configure(insertbackground="black")
        self.entry_GC_Time.configure(selectbackground="#c4c4c4")
        self.entry_GC_Time.configure(selectforeground="black")
        self.entry_GC_Time.configure(textvariable=UMSATSGUI_support.groundValueInput)

        self.Module1_Labelframe = LabelFrame(self.TabsController_t4)
        self.Module1_Labelframe.place(relx=0.03, rely=0.06, relheight=0.47, relwidth=0.97)
        self.Module1_Labelframe.configure(relief=GROOVE)
        self.Module1_Labelframe.configure(foreground="black")
        self.Module1_Labelframe.configure(text='''Module 1''')
        self.Module1_Labelframe.configure(background="#d9d9d9")
        self.Module1_Labelframe.configure(highlightbackground="#d9d9d9")
        self.Module1_Labelframe.configure(highlightcolor="black")
        self.Module1_Labelframe.configure(width=300)

        self.COM1_Dropdown = ttk.Combobox(self.Module1_Labelframe)
        self.COM1_Dropdown.place(relx=0.37, rely=0.24, relheight=0.13, relwidth=0.48, y=-12, h=12)
        self.COM1_Dropdown.configure(textvariable=UMSATSGUI_support.Com1Input)
        self.COM1_Dropdown.configure(takefocus="")
        self.COM1_Dropdown.configure(postcommand=lambda: UMSATSGUI_support.update_com_list(self.COM1_Dropdown))

        self.Baud1_Dropdown = ttk.Combobox(self.Module1_Labelframe)
        self.Baud1_Dropdown.place(relx=0.37, rely=0.59, relheight=0.13, relwidth=0.48, y=-12, h=12)
        self.Baud1_Dropdown.configure(textvariable=UMSATSGUI_support.Baud1Input)
        self.Baud1_Dropdown.configure(width=143)
        self.Baud1_Dropdown.configure(takefocus="")
        self.Baud1_Dropdown.configure(values=UMSATSGUI_support.baudrateList)

        self.COM1_Label = Label(self.Module1_Labelframe)
        self.COM1_Label.place(relx=0.03, rely=0.24, height=21, width=99, y=-12)
        self.COM1_Label.configure(activebackground="#f9f9f9")
        self.COM1_Label.configure(activeforeground="black")
        self.COM1_Label.configure(background="#d9d9d9")
        self.COM1_Label.configure(disabledforeground="#a3a3a3")
        self.COM1_Label.configure(foreground="#000000")
        self.COM1_Label.configure(highlightbackground="#d9d9d9")
        self.COM1_Label.configure(highlightcolor="black")
        self.COM1_Label.configure(text='''COM Port''')
        self.COM1_Label.configure(width=99)

        self.Baud1_Label = Label(self.Module1_Labelframe)
        self.Baud1_Label.place(relx=0.03, rely=0.59, height=21, width=96, y=-12)
        self.Baud1_Label.configure(activebackground="#f9f9f9")
        self.Baud1_Label.configure(activeforeground="black")
        self.Baud1_Label.configure(background="#d9d9d9")
        self.Baud1_Label.configure(disabledforeground="#a3a3a3")
        self.Baud1_Label.configure(foreground="#000000")
        self.Baud1_Label.configure(highlightbackground="#d9d9d9")
        self.Baud1_Label.configure(highlightcolor="black")
        self.Baud1_Label.configure(text='''Baud rate''')
        self.Baud1_Label.configure(width=96)

        self.btn_Serial1_set = Button(self.Module1_Labelframe)
        self.btn_Serial1_set.place(relx=0.87, rely=0.35, height=24, width=27, y=-12)
        self.btn_Serial1_set.configure(activebackground="#d9d9d9")
        self.btn_Serial1_set.configure(activeforeground="#000000")
        self.btn_Serial1_set.configure(background="#d9d9d9")
        self.btn_Serial1_set.configure(disabledforeground="#a3a3a3")
        self.btn_Serial1_set.configure(foreground="#000000")
        self.btn_Serial1_set.configure(highlightbackground="#d9d9d9")
        self.btn_Serial1_set.configure(highlightcolor="black")
        self.btn_Serial1_set.configure(pady="0")
        self.btn_Serial1_set.configure(text='''Set''')
        self.btn_Serial1_set.bind('<Button-1>', lambda e: UMSATSGUI_support.setup_serial(e, UMSATSGUI_support.Com1Input.get(),
                                                                                         UMSATSGUI_support.Baud1Input.get(),
                                                                                         1))

        self.Module2_Labelframe = LabelFrame(self.TabsController_t4)
        self.Module2_Labelframe.place(relx=0.03, rely=0.5, relheight=0.47, relwidth=0.97)
        self.Module2_Labelframe.configure(relief=GROOVE)
        self.Module2_Labelframe.configure(foreground="black")
        self.Module2_Labelframe.configure(text='''Module 2''')
        self.Module2_Labelframe.configure(background="#d9d9d9")
        self.Module2_Labelframe.configure(highlightbackground="#d9d9d9")
        self.Module2_Labelframe.configure(highlightcolor="black")
        self.Module2_Labelframe.configure(width=300)

        self.COM2_Dropdown = ttk.Combobox(self.Module2_Labelframe)
        self.COM2_Dropdown.place(relx=0.37, rely=0.24, relheight=0.13, relwidth=0.48, y=-12, h=12)
        self.COM2_Dropdown.configure(textvariable=UMSATSGUI_support.Com2Input)
        self.COM2_Dropdown.configure(takefocus="")
        self.COM2_Dropdown.configure(postcommand=lambda: UMSATSGUI_support.update_com_list(self.COM2_Dropdown))

        self.Baud2_Dropdown = ttk.Combobox(self.Module2_Labelframe)
        self.Baud2_Dropdown.place(relx=0.37, rely=0.59, relheight=0.13, relwidth=0.48, y=-12, h=12)
        self.Baud2_Dropdown.configure(textvariable=UMSATSGUI_support.Baud2Input)
        self.Baud2_Dropdown.configure(width=143)
        self.Baud2_Dropdown.configure(takefocus="")
        self.Baud2_Dropdown.configure(values=UMSATSGUI_support.baudrateList)

        self.COM2_Label = Label(self.Module2_Labelframe)
        self.COM2_Label.place(relx=0.03, rely=0.24, height=21, width=99, y=-12)
        self.COM2_Label.configure(activebackground="#f9f9f9")
        self.COM2_Label.configure(activeforeground="black")
        self.COM2_Label.configure(background="#d9d9d9")
        self.COM2_Label.configure(disabledforeground="#a3a3a3")
        self.COM2_Label.configure(foreground="#000000")
        self.COM2_Label.configure(highlightbackground="#d9d9d9")
        self.COM2_Label.configure(highlightcolor="black")
        self.COM2_Label.configure(text='''COM Port''')
        self.COM2_Label.configure(width=99)

        self.Baud2_Label = Label(self.Module2_Labelframe)
        self.Baud2_Label.place(relx=0.03, rely=0.59, height=21, width=96, y=-12)
        self.Baud2_Label.configure(activebackground="#f9f9f9")
        self.Baud2_Label.configure(activeforeground="black")
        self.Baud2_Label.configure(background="#d9d9d9")
        self.Baud2_Label.configure(disabledforeground="#a3a3a3")
        self.Baud2_Label.configure(foreground="#000000")
        self.Baud2_Label.configure(width=96)

        self.btn_Serial2_set = Button(self.Module2_Labelframe)
        self.btn_Serial2_set.place(relx=0.87, rely=0.35, height=24, width=27, y=-12)
        self.Baud2_Label.configure(highlightbackground="#d9d9d9")
        self.Baud2_Label.configure(highlightcolor="black")
        self.Baud2_Label.configure(text='''Baud rate''')
        self.btn_Serial2_set.configure(activebackground="#d9d9d9")
        self.btn_Serial2_set.configure(activeforeground="#000000")
        self.btn_Serial2_set.configure(background="#d9d9d9")
        self.btn_Serial2_set.configure(disabledforeground="#a3a3a3")
        self.btn_Serial2_set.configure(foreground="#000000")
        self.btn_Serial2_set.configure(highlightbackground="#d9d9d9")
        self.btn_Serial2_set.configure(highlightcolor="black")
        self.btn_Serial2_set.configure(pady="0")
        self.btn_Serial2_set.configure(text='''Set''')
        self.btn_Serial2_set.bind('<Button-1>', lambda e: UMSATSGUI_support.setup_serial(e, UMSATSGUI_support.Com2Input.get(),
                                                                                   UMSATSGUI_support.Baud2Input.get(),
                                                                                   2))

        self.LabelStatus = LabelFrame(self.ModuleFrameLabel)
        self.LabelStatus.place(relx=0.03, rely=0.70, relheight=0.25, relwidth=0.91, y=-12, h=12)
        self.LabelStatus.configure(relief=GROOVE)
        self.LabelStatus.configure(foreground="black")
        self.LabelStatus.configure(text='''Status''')
        self.LabelStatus.configure(background="#d9d9d9")
        self.LabelStatus.configure(highlightbackground="#d9d9d9")
        self.LabelStatus.configure(highlightcolor="black")
        self.LabelStatus.configure(width=320)

        self.btnClear = Button(self.frameTerminal)
        self.btnClear.place(relx=0.05, rely=0.95, height=24, width=130)
        self.btnClear.configure(activebackground="#d9d9d9")
        self.btnClear.configure(activeforeground="#000000")
        self.btnClear.configure(background="#d9d9d9")
        self.btnClear.configure(disabledforeground="#a3a3a3")
        self.btnClear.configure(foreground="#000000")
        self.btnClear.configure(highlightbackground="#d9d9d9")
        self.btnClear.configure(highlightcolor="black")
        self.btnClear.configure(pady="0")
        self.btnClear.configure(text='''Clear All Terminals''')
        self.btnClear.bind('<Button-1>', lambda e: UMSATSGUI_support.clear_display( self.Listbox1,self.Listbox2))

        self.Message1 = Message(self.LabelStatus)
        self.Message1.place(relx=0.13, rely=0.20, relheight=0.09, relwidth=0.19, y=-12, h=12)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''Power:''')
        self.Message1.configure(width=60)

        self.Message2 = Message(self.LabelStatus)
        self.Message2.place(relx=0.12, rely=0.40, relheight=0.09, relwidth=0.22, y=-12, h=12)
        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(text='''Payload:''')
        self.Message2.configure(width=69)

        self.Message3 = Message(self.LabelStatus)
        self.Message3.place(relx=0.13, rely=0.61, relheight=0.16, relwidth=0.2, y=-12, h=12)
        self.Message3.configure(background="#d9d9d9")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''Ground Control:''')
        self.Message3.configure(width=64)

        # self.Checkbutton1 = Checkbutton(self.LabelStatus)
        # self.Checkbutton1.place(relx=0.53, rely=0.41, relheight=0.1, relwidth=0.19, y=-12, h=12)
        # self.Checkbutton1.configure(activebackground="#d9d9d9")
        # self.Checkbutton1.configure(activeforeground="#000000")
        # self.Checkbutton1.configure(background="#d9d9d9")
        # self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton1.configure(foreground="#000000")
        # self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton1.configure(highlightcolor="black")
        # self.Checkbutton1.configure(justify=LEFT)
        # self.Checkbutton1.configure(text='''Check''')
        # self.Checkbutton1.configure(variable=UMSATSGUI_support.che47)

        # self.Checkbutton2 = Checkbutton(self.LabelStatus)
        # self.Checkbutton2.place(relx=0.53, rely=0.61, relheight=0.1, relwidth=0.19, y=-12, h=12)
        # self.Checkbutton2.configure(activebackground="#d9d9d9")
        # self.Checkbutton2.configure(activeforeground="#000000")
        # self.Checkbutton2.configure(background="#d9d9d9")
        # self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        # self.Checkbutton2.configure(foreground="#000000")
        # self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        # self.Checkbutton2.configure(highlightcolor="black")
        # self.Checkbutton2.configure(justify=LEFT)
        # self.Checkbutton2.configure(text='''Check''')
        # self.Checkbutton2.configure(variable=UMSATSGUI_support.che48)


if __name__ == '__main__':
    vp_start_gui()



