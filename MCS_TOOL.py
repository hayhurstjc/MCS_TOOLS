#! C:/Python27/python27.exe
import os
import Tkinter as tk
from Tkinter import *
import fileinput
from operator import itemgetter
import Tix
import csv
import tkFileDialog



def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Coo Coooo")
    label = Tix.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    b1 = Tix.Button(popup, text="Close", command=popup.destroy)
    b1.pack()
    popup.mainloop()

class popupWindow(object):
    def __init__(self,parent):
        top=self.top=Toplevel(parent)
        self.l=Label(top,text="Hello World")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class popupWindow2(object):
    def __init__(self,parent):
        top=self.top=Toplevel(parent)
        self.v = StringVar()
        self.l=Radiobutton(top,text="Option1", variable=self.v, value=1, highlightcolor='red', activebackground='red', activeforeground='white')
        self.l.pack()
        self.e=Radiobutton(top,text="Option2", variable=self.v, value=2, highlightcolor='red')
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack(side=BOTTOM)
    def cleanup(self):
        self.radiooption =self.v.get()
        print self.radiooption
        self.top.destroy()

def simulate_control_t(e):
    e.widget.tag_add("sel", "1.0", "end-1c")

def simulate_control_e(event):
    app.nb.after(50, select_all, event.widget)

def select_all(widget):
    widget.select_range(0, 'end')
    widget.icursor('end')
def paste(self):
    self.text.event_generate('<Control-v>')
def cut(self):
    self.text.event_generate('<Control-x>')
def copy(self):
    self.text.event_generate('<Control-c>')

class Text0(Frame):
    def __init__(self, master, width=0, height=0, **kwargs):
        self.width = width
        self.height = height

        Frame.__init__(self, master, width=self.width, height=self.height)
        self.text_widget = Text(self, **kwargs)
        self.text_widget.pack(expand=YES, fill=BOTH)

    def pack(self, *args, **kwargs):
        Frame.pack(self, *args, **kwargs)
        self.pack_propagate(False)
        self.grid(row=4, rowspan=4, column=0, columnspan=4, padx=10, pady=10)

    def grid(self, *args, **kwargs):
        Frame.grid(self, *args, **kwargs)
        self.grid_propagate(False)

class Text3(Frame):
    def __init__(self, master, width=0, height=0, *args, **kwargs):
        self.width = width
        self.height = height
        Frame.__init__(self, master, width=self.width, height=self.height, *args, **kwargs)
        self.text_widget1 = Text(self,background='white', width=50, height=15, wrap=WORD)
        self.text_widget1.grid(row=0, column=0)
        self.text_widget2 = Text(self,background='white', width=50, height=15, wrap=WORD)
        self.text_widget2.grid(row=1, column=0)
        self.text_widget = Text(self,background='white', width=80, height=30, wrap=WORD)
        self.text_widget.grid(row=0, rowspan=2,column=1,sticky='nsew')

    def pack(self, *args, **kwargs):
        Frame.pack(self, *args, **kwargs)
        self.pack_propagate(False)
        self.grid(row=1, rowspan=13, column=2, padx=10, pady=10)

    def grid(self, *args, **kwargs):
        Frame.grid(self, *args, **kwargs)
        self.grid_propagate(False)


class gui_akl(Tix.Tk):
    def __init__(self, parent):
        Tix.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        tab1frame = tk.Frame(self)
        tab1frame.grid(column=0, row=0, sticky='NSEW')
        self.nb = Tix.NoteBook(tab1frame)
        self.nb.grid(column=0, row=1, columnspan=50, rowspan=49, sticky=NSEW)

        self.nb.add('tab0', label='TAB0')
        page0 = self.nb.subwidget('tab0')
        self.Frame0 = Tix.Frame(page0)
        self.nb.add("tab1", label='TAB1')
        page1 = self.nb.subwidget("tab1")
        self.Frame1 = Tix.Frame(page1)
        self.nb.add("tab2", label='TAB2')
        page2 = self.nb.subwidget("tab2")
        self.Frame2 = Tix.Frame(page2)
        self.nb.add('tab3', label='TAB3')
        page3 = self.nb.subwidget('tab3')
        self.Frame3 = Tix.Frame(page3)




        self.bind_class("Text", "<Control-a>", simulate_control_t)
        self.bind_class("Entry", "<Control-a>", simulate_control_e)
        self.bind('<Control-s>', self.save)
        self.bind('<Control-o>', self.database)

        self.menubar = Menu(self)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.SS_menu = Menu(self.filemenu, tearoff=0)
        self.SS_menu.add_command(label="Open Database", command=self.database)
        self.SS_menu.add_command(label="Save Profile", command=self.save)
        self.SS_menu.add_command(label="Load Profile", command=self.load)
        self.filemenu.add_cascade(label="SS", menu=self.SS_menu)
        self.AWP_menu = Menu(self.filemenu, tearoff=0)
        self.AWP_menu.add_command(label="Execute ADM script", command=self.admload)  # Need filepath to ADM on the ground and on the jet
        self.AWP_menu.add_command(label="Open ADM script", command=self.admopen)
        self.AWP_menu.add_command(label="Launch AWP",
            command=self.awplaunch)  # need to figure out how to run script to initialize commands from the command line
        self.filemenu.add_cascade(label="AWP", menu=self.AWP_menu)
        self.FH_menu = Menu(self.filemenu, tearoff=0)
        self.FH_menu.add_command(label="Launch FH", command=self.fhlaunch)
        self.FH_menu.add_command(label="Load Mpriority file", command=self.fhload)
        self.filemenu.add_cascade(label="FH", menu=self.FH_menu)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Cut", command=lambda: self.event_generate("<Control-x>"))
        self.editmenu.add_command(label="Copy", command=lambda: self.event_generate("<Control-c>"))
        self.editmenu.add_command(label="Paste", command=lambda: self.event_generate("<Control-v>"))
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Manual", command=self.manuals)
        self.helpmenu.add_command(label="About", command=lambda: popupmsg(
            "This MCS TOOL is brought to you by Pigeon Power inc.\nemail: joshua.hayhurst@us.af.mil"))
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)


        #################MCS main tab###############

        Label(page0, text="Welcome to MCS Tools", font=('Times New Roman', 50)).grid(row=0, columnspan=4)
        Label(page0, text="AWP", font=('Helvetica 10 bold')).grid(row=1, column=0)
        Button(page0, text="Run ADM script", command=self.admload).grid(row=2, column=0, sticky='we')
        Button(page0, text="Launch AWP", command=self.awplaunch).grid(row=3, column=0, sticky='we')
        Label(page0, text="FIREHAWK", font=('Helvetica 10 bold')).grid(row=1, column=1)
        Button(page0, text="Run Mpriority", command=self.fhload).grid(row=2, column=1, sticky='we')
        Button(page0, text="Launch FH VNC", command=self.fhlaunch).grid(row=3, column=1, sticky='we')
        Label(page0, text="ENVIOUS LEMUR", font=('Helvetica 10 bold')).grid(row=1, column=2)
        Button(page0, text="Set Mission file", command=self.elload).grid(row=2, column=2, sticky='we')
        Button(page0, text="Launch Alaska", command=self.ellaunch).grid(row=3, column=2, sticky='we')
        Label(page0, text="SHARKBYTE", font=('Helvetica 10 bold')).grid(row=1, column=3)
        Button(page0, text="Launch SB", command=self.sblaunch).grid(row=2, column=3, sticky='we')


        self.text0 = Text0(page0, width=600, height=200)
        self.text0.pack()




        #################SS KL tool#################
        #   self.var1 shouldn't be a thing anymore, the system automatically pulls your position number.
        #   If it is set to something else then something is wrong with the function.
        #   If the user changes the position number then the tool won't work anyways since it needs to be tied to their sid as well.
        self.text1 = Text3(page1, width=800, height=450)
        self.text1.pack()

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.ifile = 'newHooked.txt'
        self.ofile = dir_path+'\oldHooked.txt'

        f1 = open(self.ifile, 'w')
        f2 = open(self.ofile, 'r')
        read1 = f2.readlines()
        for line in read1:
            f1.write(line)
        self.text1.text_widget.insert(END, open(self.ifile).read())  # update with KL shell
        f3 = open(dir_path+'\Hooked_OWS9.txt', "r")
        lines = f3.readlines()
        # self.ll = lines[1].split(":")[1].strip().split()  # seperates the location line
        # self.elp1 = lines[2].strip() + " " + lines[3].strip()  # ties the two elp lines together
        # self.elp2 = self.elp1.split()  # indexes the elp line for easy print
        # self.id = lines[7].split("S_")[1]  # setup for HSID
        # self.elp = '/ELP:' + str(float(self.elp2[0])) + 'NM-' + str(float(self.elp2[2])) + 'NM-' + str(
        #     float(self.elp2[4])) + '//\n'
        f1.close()
        f2.close()

        self.var1 = StringVar(page1)
        self.var1.set('1')
        option1 = OptionMenu(page1, self.var1, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        option1.pack()
        option1.grid(row=0, column=1)

        self.var2 = StringVar(page1)
        self.var2.set('DATA2')
        option2 = OptionMenu(page1, self.var2, 'CHOICE1', 'CHOICE2')
        option2.pack()
        option2.grid(row=5, column=1)

        self.var3 = StringVar(page1)
        self.var3.set('DATA5')
        option3 = OptionMenu(page1, self.var3, 'CHOICE1', 'CHOICE2')
        option3.pack()
        option3.grid(row=7, column=1)

        self.var4 = StringVar(page1)
        self.var4.set('DATA1')
        option4 = OptionMenu(page1, self.var4, 'CHOICE1', 'CHOICE2')
        option4.pack()
        option4.grid(row=1, column=1)

        self.var5 = StringVar(page1)
        self.var5.set('DATA3')
        option5 = OptionMenu(page1, self.var5, 'CHOICE1', 'CHOICE2')
        option5.pack()
        option5.grid(row=6, column=1)

        Label(page1, text="Select your POSN#").grid(row=0)
        Label(page1, text="ACTY").grid(row=1)
        Label(page1, text="CASECASE").grid(row=2)
        Label(page1, text="DATA3").grid(row=3)
        Label(page1, text="DATA4").grid(row=4)
        Label(page1, text="MODEL1").grid(row=5)
        Label(page1, text="MODEL2").grid(row=6)
        Label(page1, text="DATA5").grid(row=7)
        Label(page1, text="DATA6").grid(row=8)
        Label(page1, text="DATA7").grid(row=9)
        Label(page1, text="TIMEUP").grid(row=10)
        Label(page1, text="TIMEDOWN").grid(row=11)
        Label(page1, text="NAMES").grid(row=12)
        Label(page1, text="DATA8").grid(row=13)

        self.ErrorVar = StringVar(page1)
        Label(page1, textvariable=self.ErrorVar).grid(row=0, column=2, sticky='WE')

        Button(page1, text="Add Primary Hooked SS LOC", command=self.addloc).grid(row=15, column=0, columnspan=2,
                                                                                  sticky='we')
        Button(page1, text="Clear KL", command=self.clearKL).grid(row=14, column=2, sticky='w', padx=10)
        Button(page1, text="Run KL Tool", command=self.run).grid(row=14, column=0, sticky='we')
        Button(page1, text="Reset", command=self.reset).grid(row=14, column=1, sticky='we')
        Button(page1, text="Dump", command=self.dumpToFreetext).grid(row=14, column=2)
        self.B1 = Button(page1, text="Save SSRCKL", command=lambda: self.save_file(self.text1.text_widget.get(1.0,END)+'\n\n\n=-=-=HEADER INFO=-=-=\n\nsoon i think there will be things here\n\n\n=-=-=HANDSCAN=-=-=\n\n'+self.text1.text_widget.get(1.0,END)))
        self.B1.grid(row=14, column=2, sticky='e')



        self.e2 = Entry(page1)
        self.e2.grid(row=2, column=1)
        add_placeholder_to(self.e2, 'CASENOTE')
        self.e3 = Entry(page1)
        self.e3.grid(row=3, column=1)
        self.e4 = Entry(page1)
        self.e4.grid(row=4, column=1)
        self.e7 = Entry(page1)
        self.e7.grid(row=8, column=1)
        self.e9 = Entry(page1)
        self.e9.grid(row=9, column=1)
        self.e12 = Entry(page1)
        self.e12.grid(row=10, column=1)
        self.e13 = Entry(page1)
        self.e13.grid(row=11, column=1)
        self.e14 = Entry(page1)
        self.e14.grid(row=12, column=1)
        self.e15 = Entry(page1)
        self.e15.grid(row=13, column=1)
        #if we_are_airborne = True:
            #self.e16 = Label(page1, text='Mission #').grid(row=0, column=3)
        #else:
            #self.e16 = Button(page1, text='Mission #', command=self.default_project)
        self.e16 = Label(page1, text='Mission #').grid(row=0, column=3)



        #################SA KL tool#################

        self.text2 = Text3(page2, width=800, height=450)
        self.text2.pack()


        Label(page2, text="Position").grid(row=0,column=0)
        self.var6 = StringVar(page2)
        self.var6.set('1')
        option6 = OptionMenu(page2, self.var1, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        option6.pack()
        option6.grid(row=0, column=1)

        Label(page2, text="ACTY").grid(row=1,column=0)
        self.var7 = StringVar(page2)
        self.var7.set('DATA2')
        option2 = OptionMenu(page2, self.var2, 'CHOICE1', 'CHOICE2')
        option2.pack()
        option2.grid(row=1, column=1)

        Label(page2, text="CASE").grid(row=2,column=0)
        self.e16 = Entry(page2)
        self.e16.grid(row=2, column=1)

        Label(page2, text="PHONE #").grid(row=3, column=0)
        self.e17 = Entry(page2)
        self.e17.grid(row=3, column=1)

        Label(page2, text="PASSWORD").grid(row=4,column=0)
        self.var8 = StringVar(page2)
        self.var8.set('DATA')
        option7 = OptionMenu(page2, self.var2, 'CHOICE1', 'CHOICE2')
        option7.pack()
        option7.grid(row=4, column=1)

        Label(page2, text="OFFICE").grid(row=5,column=0)
        self.e19 = Entry(page2)
        self.e19.grid(row=5, column=1)

        Label(page2, text="Time").grid(row=6,column=0)
        self.e20 = Entry(page2)
        self.e20.grid(row=6,column=1)

        Label(page2, text="NAME").grid(row=7, column=0)
        self.e21 = Entry(page2)
        self.e21.grid(row=7,column=1)

        Label(page2, text="NICK").grid(row=8,column=0)
        self.e22 = Entry(page2)
        self.e22.grid(row=8,column=1)

        Button(page2, text="RUN").grid(row=9, column=0, columnspan=2, sticky='WE')
        Button(page2, text="ADD LOC").grid(row=10, column=0, columnspan=2, sticky='WE')
        Button(page2, text="DUMP").grid(row=11, column=0, columnspan=2, sticky='WE')
        Button(page2, text="CLEAR KL").grid(row=12, column=0, columnspan=2, sticky='WE')
        Button(page2, text="RESET").grid(row=13, column=0, columnspan=2, sticky='WE')
        self.b = Button(page1, text='REFRESH ', command=self.popup)
        self.b.grid(row=6, column=3)
        Button(page2, text='REFRESH', command=self.tupdate).grid(row=6, column=3)
        Button(page2, text='Save CHICANEKL', command=self.save_file).grid(row=14, column=0, sticky='e')

        Label(page2, text='Mission #').grid(row=0, column=3)


        self.ssrcraid = Tix.ScrolledHList(page1, options='hlist.columns 1 hlist.header 1')
        self.ssrcraid.grid(row=1, rowspan=5, column=3)
        self.hlist2 = self.ssrcraid.hlist
        self.hlist2.config(browsecmd=self.ssrcselect)
        self.hlist2.header_create(0, itemtype=Tix.TEXT, text='SSRC files in RAID')

        self.traid = Tix.ScrolledHList(page2, options='hlist.columns 1 hlist.header 1')
        self.traid.grid(row=1, rowspan=5, column=3)
        self.hlist3 = self.traid.hlist
        self.hlist3.config(browsecmd=self.tselect)
        self.hlist3.header_create(0, itemtype=Tix.TEXT, text='CHICANE files in RAID')

        self.awpvalue = StringVar()
        self.dsvalue = StringVar()
        self.elvalue = StringVar()
        self.fhvalue = StringVar()
        self.fbvalue = StringVar()
        self.hgvalue = StringVar()
        self.ilvalue = StringVar()
        self.savalue = StringVar()
        self.sbvalue = StringVar()
        self.ssvalue = StringVar()
        self.stvalue = StringVar()
        self.tlvalue = StringVar()
        self.tvvalue = StringVar()
        self.tsvalue = StringVar()

        system = LabelFrame(page3, text="SYSTEM")
        system.grid(row=0, column=0, sticky='ns')
        self.awplabel = Label(system, text='AWP', pady=3)
        self.awplabel.grid(row=0, sticky='w')
        self.dslabel = Label(system, text='DREAMSTALKER', pady=3).grid(row=1, sticky='w')
        self.ellabel = Label(system, text='ENVIOUS LEMUR', pady=3).grid(row=2, sticky='w')
        self.fhlabel = Label(system, text='FIREHAWK', pady=3).grid(row=3, sticky='w')
        self.fblabel = Label(system, text='FIREBAT', pady=3).grid(row=4, sticky='w')
        self.hglabel = Label(system, text='HOBGOBLIN', pady=3).grid(row=5, sticky='w')
        self.illabel = Label(system, text='ICELAND', pady=3).grid(row=6, sticky='w')
        self.salabel = Label(system, text='SALVAGE', pady=3).grid(row=7, sticky='w')
        self.sblabel = Label(system, text='SHARKBYTE', pady=3).grid(row=8, sticky='w')
        self.sslabel = Label(system, text='STAMPEDING SEROW', pady=3).grid(row=9, sticky='w')
        self.stlabel = Label(system, text='SEATURTLE', pady=3).grid(row=10, sticky='w')
        self.tllabel = Label(system, text='TEALIGHT', pady=3).grid(row=11, sticky='w')
        self.tvlabel = Label(system, text='TEX VIRUS', pady=3).grid(row=12, sticky='w')
        self.tslabel = Label(system, text='TOXICSMOKE', pady=3).grid(row=13, sticky='w')

        status = LabelFrame(page3, text="STATUS")
        status.grid(row=0, column=1)
        self.awpradio = Radiobutton(status, text="OPERATIONAL", variable=self.awpvalue, value='OPERATIONAL').grid(row=0, column=0)
        self.dsradio = Radiobutton(status, text="OPERATIONAL", variable=self.dsvalue, value='OPERATIONAL').grid(row=1, column=0)
        self.elradio = Radiobutton(status, text="OPERATIONAL", variable=self.elvalue, value='OPERATIONAL').grid(row=2, column=0)
        self.fhradio = Radiobutton(status, text="OPERATIONAL", variable=self.fhvalue, value='OPERATIONAL').grid(row=3, column=0)
        self.fbradio = Radiobutton(status, text="OPERATIONAL", variable=self.fbvalue, value='OPERATIONAL').grid(row=4, column=0)
        self.hgradio = Radiobutton(status, text="OPERATIONAL", variable=self.hgvalue, value='OPERATIONAL').grid(row=5, column=0)
        self.ilradio = Radiobutton(status, text="OPERATIONAL", variable=self.ilvalue, value='OPERATIONAL').grid(row=6, column=0)
        self.saradio = Radiobutton(status, text="OPERATIONAL", variable=self.savalue, value='OPERATIONAL').grid(row=7, column=0)
        self.sbradio = Radiobutton(status, text="OPERATIONAL", variable=self.sbvalue, value='OPERATIONAL').grid(row=8, column=0)
        self.ssradio = Radiobutton(status, text="OPERATIONAL", variable=self.ssvalue, value='OPERATIONAL').grid(row=9, column=0)
        self.stradio = Radiobutton(status, text="OPERATIONAL", variable=self.stvalue, value='OPERATIONAL').grid(row=10, column=0)
        self.tlradio = Radiobutton(status, text="OPERATIONAL", variable=self.tlvalue, value='OPERATIONAL').grid(row=11, column=0)
        self.tvradio = Radiobutton(status, text="OPERATIONAL", variable=self.tvvalue, value='OPERATIONAL').grid(row=12, column=0)
        self.tsradio = Radiobutton(status, text="OPERATIONAL", variable=self.tsvalue, value='OPERATIONAL').grid(row=13, column=0)

        self.awpradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.awpvalue, value='NON-OPERATIONAL').grid(row=0, column=1)
        self.dsradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.dsvalue, value='NON-OPERATIONAL').grid(row=1, column=1)
        self.elradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.elvalue, value='NON-OPERATIONAL').grid(row=2, column=1)
        self.fhradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.fhvalue, value='NON-OPERATIONAL').grid(row=3, column=1)
        self.fbradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.fbvalue, value='NON-OPERATIONAL').grid(row=4, column=1)
        self.hgradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.hgvalue, value='NON-OPERATIONAL').grid(row=5, column=1)
        self.ilradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.ilvalue, value='NON-OPERATIONAL').grid(row=6, column=1)
        self.saradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.savalue, value='NON-OPERATIONAL').grid(row=7, column=1)
        self.sbradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.sbvalue, value='NON-OPERATIONAL').grid(row=8, column=1)
        self.ssradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.ssvalue, value='NON-OPERATIONAL').grid(row=9, column=1)
        self.stradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.stvalue, value='NON-OPERATIONAL').grid(row=10, column=1)
        self.tlradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.tlvalue, value='NON-OPERATIONAL').grid(row=11, column=1)
        self.tvradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.tvvalue, value='NON-OPERATIONAL').grid(row=12, column=1)
        self.tsradio = Radiobutton(status, text="NON-OPERATIONAL", variable=self.tsvalue, value='NON-OPERATIONAL').grid(row=13, column=1)

        self.awptime = StringVar()
        self.dstime = StringVar()
        self.eltime = StringVar()
        self.fhtime = StringVar()
        self.fbtime = StringVar()
        self.hgtime = StringVar()
        self.iltime = StringVar()
        self.satime = StringVar()
        self.sbtime = StringVar()
        self.sstime = StringVar()
        self.sttime = StringVar()
        self.tltime = StringVar()
        self.tvtime = StringVar()
        self.tstime = StringVar()

        self.awpentry = Entry(status, textvariable=self.awptime)
        self.dsentry = Entry(status, textvariable=self.dstime)
        self.elentry = Entry(status, textvariable=self.eltime)
        self.fhentry = Entry(status, textvariable=self.fhtime)
        self.fbentry = Entry(status, textvariable=self.fbtime)
        self.hgentry = Entry(status, textvariable=self.hgtime)
        self.ilentry = Entry(status, textvariable=self.iltime)
        self.saentry = Entry(status, textvariable=self.satime)
        self.sbentry = Entry(status, textvariable=self.sbtime)
        self.ssentry = Entry(status, textvariable=self.sstime)
        self.stentry = Entry(status, textvariable=self.sttime)
        self.tlentry = Entry(status, textvariable=self.tltime)
        self.tventry = Entry(status, textvariable=self.tvtime)
        self.tsentry = Entry(status, textvariable=self.tstime)

        self.awpentry.grid(row=0, column=2)
        self.dsentry.grid(row=1, column=2)
        self.elentry.grid(row=2, column=2)
        self.fhentry.grid(row=3, column=2)
        self.fbentry.grid(row=4, column=2)
        self.hgentry.grid(row=5, column=2)
        self.ilentry.grid(row=6, column=2)
        self.saentry.grid(row=7, column=2)
        self.sbentry.grid(row=8, column=2)
        self.ssentry.grid(row=9, column=2)
        self.stentry.grid(row=10, column=2)
        self.tlentry.grid(row=11, column=2)
        self.tventry.grid(row=12, column=2)
        self.tsentry.grid(row=13, column=2)

        totals = LabelFrame(page3, text="TOTALS")
        totals.grid(row=0,column=2, sticky='ns')

        self.awpval = StringVar()
        self.dsval = StringVar()
        self.elval = StringVar()
        self.fhval = StringVar()
        self.fbval = StringVar()
        self.hgval = StringVar()
        self.ilval = StringVar()
        self.saval = StringVar()
        self.sbval = StringVar()
        self.ssval = StringVar()
        self.stval = StringVar()
        self.tlval = StringVar()
        self.tvval = StringVar()
        self.tsval = StringVar()

        self.awptotals = Entry(totals, textvariable=self.awpval, width=100)
        self.dstotals = Entry(totals, textvariable=self.dsval, width=100)
        self.eltotals = Entry(totals, textvariable=self.elval, width=100)
        self.fhtotals = Entry(totals, textvariable=self.fhval, width=100)
        self.fbtotals = Entry(totals, textvariable=self.fbval, width=100)
        self.hgtotals = Entry(totals, textvariable=self.hgval, width=100)
        self.iltotals = Entry(totals, textvariable=self.ilval, width=100)
        self.satotals = Entry(totals, textvariable=self.saval, width=100)
        self.sbtotals = Entry(totals, textvariable=self.sbval, width=100)
        self.sstotals = Entry(totals, textvariable=self.ssval, width=100)
        self.sttotals = Entry(totals, textvariable=self.stval, width=100)
        self.tltotals = Entry(totals, textvariable=self.tlval, width=100)
        self.tvtotals = Entry(totals, textvariable=self.tvval, width=100)
        self.tstotals = Entry(totals, textvariable=self.tsval, width=100)

        self.awptotals.grid(row=0, pady=3)
        self.dstotals.grid(row=1, pady=3)
        self.eltotals.grid(row=2, pady=3)
        self.fhtotals.grid(row=3, pady=3)
        self.fbtotals.grid(row=4, pady=3)
        self.hgtotals.grid(row=5, pady=3)
        self.iltotals.grid(row=6, pady=3)
        self.satotals.grid(row=7, pady=3)
        self.sbtotals.grid(row=8, pady=3)
        self.sstotals.grid(row=9, pady=3)
        self.sttotals.grid(row=10, pady=3)
        self.tltotals.grid(row=11, pady=3)
        self.tvtotals.grid(row=12, pady=3)
        self.tstotals.grid(row=13, pady=3)

        outages = LabelFrame(page3, text="OUTAGES")
        outages.grid(row=1, column=0, columnspan=3, sticky='w')
        self.outages = Text0(outages, height=200, width=750)
        self.outages.pack()
        buttons = PanedWindow(page3)
        buttons.grid(row=1, column=2, sticky='ne')
        Button(buttons, text="Run Totals", command=self.runtotals).grid(row=0)
        Button(buttons, text="Reset Totals", command=self.totalsreset).grid(row=1)
        Button(buttons, text="Dump to Freetext", command=self.totalsdump).grid(row=2)
        Button(buttons, text="Save", command=self.save_totals).grid(row=3)

    def save_totals(self):
        t1 = self.awplabel.cget('text') + '/' + self.awpvalue.get() + '/' + self.awpentry.get() + '/\n'
        t2 = self.dslabel.cget('text') + '/' + self.dsvalue.get() + '/' + self.dsentry.get() + '/\n'
        t3 = self.ellabel.cget('text') + '/' + self.elvalue.get() + '/' + self.elentry.get() + '/\n'
        t4 = self.fhlabel.cget('text') + '/' + self.fhvalue.get() + '/' + self.fhentry.get() + '/\n'
        t5 = self.fblabel.cget('text') + '/' + self.fbvalue.get() + '/' + self.fbentry.get() + '/\n'
        t6 = self.hglabel.cget('text') + '/' + self.hgvalue.get() + '/' + self.hgentry.get() + '/\n'
        t7 = self.illabel.cget('text') + '/' + self.ilvalue.get() + '/' + self.ilentry.get() + '/\n'
        t8 = self.salabel.cget('text') + '/' + self.savalue.get() + '/' + self.saentry.get() + '/\n'
        t9 = self.sblabel.cget('text') + '/' + self.sbvalue.get() + '/' + self.sbentry.get() + '/\n'
        t10 = self.stlabel.cget('text') + '/' + self.stvalue.get() + '/' + self.stentry.get() + '/\n'
        t11 = self.sslabel.cget('text') + '/' + self.ssvalue.get() + '/' + self.ssentry.get() + '/\n'
        t12 = self.tllabel.cget('text') + '/' + self.tlvalue.get() + '/' + self.tlentry.get() + '/\n'
        t13 = self.tvlabel.cget('text') + '/' + self.tvvalue.get() + '/' + self.tventry.get() + '/\n'
        t14 = self.tslabel.cget('text') + '/' + self.tsvalue.get() + '/' + self.tsentry.get() + '/\n'
        t15 = self.awptotals.get()+'\n'+self.dstotals.get()+'\n'+self.eltotals.get()+'\n'+self.fhtotals.get()+'\n'+self.fbtotals.get()+'\n'+self.hgtotals.get()+'\n'+self.iltotals.get()+'\n'+self.satotals.get()+'\n'+self.sbtotals.get()+'\n'+self.sttotals.get()+'\n'+self.sstotals.get()+'\n'+self.tltotals.get()+'\n'+self.tvtotals.get()+'\n'+self.tstotals.get()+'\n'
        totalsfile = t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+'/\n\nTOTALS:\n'+t15+'/\n\nOUTAGES:\n'+self.text3.text_widget.get(1.0,END)

        self.save_file(totalsfile)

    def totalsdump(self):
        print self.awpvalue.get()

    def runtotals(self):
        outagelist = {
            'AWP':self.awpvalue.get(),
            'DREAMSTALKER':self.dsvalue.get(),
            'ENVIOUS LEMUR':self.elvalue.get(),
            'FIREHAWK':self.fhvalue.get(),
            'FIREBAT':self.fbvalue.get(),
            'HOPGOBLIN':self.hgvalue.get(),
            'ICELAND':self.ilvalue.get(),
            'SALVAGE':self.savalue.get(),
            'SHARKBYTE':self.sbvalue.get(),
            'STAMPEDING SEROW':self.ssvalue.get(),
            'SEATURTLE': self.stvalue.get(),
            'TEALIGHT':self.tlvalue.get(),
            'TEXVIRUS':self.tvvalue.get(),
            'TOXICSMOKE':self.tsvalue.get(),
        }
        self.outages.text_widget.delete(1.0, END)
        m = 0
        for sys, val in outagelist.items():
            if sys =='AWP':
                systime = self.awptime.get()
            elif sys =='DREAMSTALKER':
                systime = self.dstime.get()
            elif sys =='ENVIOUSLEMUR':
                systime = self.eltime.get()
            elif sys =='FIREHAWK':
                systime = self.fhtime.get()
            elif sys =='FIREBAT':
                systime = self.fbtime.get()
            elif sys =='HOBGOBLIN':
                systime = self.hgtime.get()
            elif sys =='ICELAND':
                systime = self.iltime.get()
            elif sys =='SALVAGE':
                systime = self.satime.get()
            elif sys =='SHARKBYTE':
                systime = self.sbtime.get()
            elif sys =='STAMPEDING SEROW':
                systime = self.sstime.get()
            elif sys =='SEATURTLE':
                systime = self.sttime.get()
            elif sys =='TEALIGHT':
                systime = self.tltime.get()
            elif sys =='TEXVIRUS':
                systime = self.tvtime.get()
            elif sys =='TOXICSMOKE':
                systime = self.tstime.get()

            if val == '':
                print 'not all systems were given a status'
                break
            elif val =='OPERATIONAL':
                m += 1
                if m == 14:
                    self.outages.text_widget.insert(END,'ALL SYSTEMS OPERATIONAL. THERE ARE NO OUTAGES TO DISPLAY.')
                    break
                else:
                    pass
            elif val == 'NON-OPERATIONAL':
                self.outages.text_widget.insert(END, sys+'/NON-OPERATIONAL/'+systime+'/ (insert detailed description) /MSN IMPACT (MINIMAL/HIGH)/\n')

    #def default_project(self):
        #print 'Set Default Mission #'
    def tupdate(self):
        m = 0
        self.chicane = []
        self.hlist3.delete_all()
        chicane_tuple = ['CHICANE0', 'CHICANE1', 'CHICANE3']
        for path, dir, files in os.walk('C:/Users/iSpartacus/.PyCharmCE2018.1/config/scratches/RAID'):
            for f in files:
                for p in chicane_tuple:
                    if f.startswith(p):
                        self.chicane.append(f)
                        self.hlist3.add(m,itemtype=Tix.TEXT, text=f)
                        m += 1
                    else:
                        pass

    def ssrcupdate(self):
        m = 0
        self.ssrc = []
        self.hlist2.delete_all()
        ssrc_tuple = ['SSRC0','SSRC1','SSRC2']
        for path, dir, files in os.walk('C:/Users/iSpartacus/.PyCharmCE2018.1/config/scratches/RAID'):
            for f in files:
                for p in ssrc_tuple:
                    if f.startswith(p):
                        self.ssrc.append(f)
                        self.hlist2.add(m, itemtype=Tix.TEXT, text=f)
                        m += 1
                    else:
                        pass

    def tselect(self, event=None):
        self.text2.text_widget.delete(1.0, END)
        selItem = 'C:/Users/iSpartacus/.PyCharmCE2018.1/config/scratches/RAID/'+self.chicane[int(self.hlist3.info_selection()[0])]
        self.text2.text_widget.insert('end', open(selItem, 'r').read())

    def ssrcselect(self, event=None):
        self.text1.text_widget.delete(1.0, END)
        selItem = 'C:/Users/iSpartacus/.PyCharmCE2018.1/config/scratches/RAID/'+self.ssrc[int(self.hlist2.info_selection()[0])]
        self.text1.text_widget.insert('end', open(selItem, 'r').read())


    def admload(self):
        self.text0.text_widget.insert('end', 'Updating ADM script ... awaiting user input\n')  # update with KL shell
        f = open("Hooked_OWS9.txt", 'r')
        lines = f.readlines()
        o = open("testees.txt", 'w')
        for line in lines:
            o.write(line)
        f.close()
        o.close()
        self.text0.text_widget.insert('end', 'ADM update complete\n')
        self.text0.text_widget.see('end')

    def awplaunch(self):
        self.text0.text_widget.insert('end', 'Launching AWP/start\n')
        self.text0.text_widget.see('end')

    def admopen(self):
        self.text0.text_widget.insert('end', 'Opening ADM SIFILE.txt\n')
        os.startfile("testees.txt")
        self.text0.text_widget.see('end')

    def fhload(self):
        self.text0.text_widget.insert('end', 'Updating Mpriority tasking file ... Awaiting user input\n')
        self.text0.text_widget.insert('end', 'Mpriority update complete\n')
        self.text0.text_widget.see('end')

    def fhopen(self):
        self.text0.text_widget.insert('end', 'Opening Mpriority file\n')
        self.text0.text_widget.see('end')

    def fhlaunch(self):
        self.text0.text_widget.insert('end', 'Launching FH VNC\n')
        self.text0.text_widget.see('end')

    def elload(self):
        self.text0.text_widget.insert('end', 'Placing ALASKA mission file in correct directory\n')
        self.text0.text_widget.see('end')

    def ellaunch(self):
        self.text0.text_widget.insert('end', 'Launching ALASKA VNC\n')
        self.text0.text_widget.see('end')

    def sblaunch(self):
        self.text0.text_widget.insert('end', 'Launching SB client')
        self.text0.text_widget.see('end')

    def save(self, event=None):
        self.ErrorVar.set('')
        myCsvRow = self.e7.get().upper() + ',' + self.e2.get()[
                                                 0:2].upper() + ' ' + self.var4.get() + ',' + self.e2.get().upper() + ',' + self.e4.get().upper() + ',' + self.e3.get().upper() + ',' + self.e9.get().upper() + ',' + self.var2.get() + ',' + self.var5.get() + ',' + self.var3.get()
        fd = open('C:\Users\iSpartacus\Desktop\SAVEFILE.csv', 'a')
        fd.write(myCsvRow)
        fd.close()
        seen = set()
        fp = open('C:\Users\iSpartacus\Desktop\SAVEFILE.csv', 'r')
        data = [line for line in csv.reader(fp)]
        fp.close()
        data.sort(key=itemgetter(0))
        fp = open('C:\Users\iSpartacus\Desktop\SAVEFILE.csv', 'w')
        csv.writer(fp).writerows(data)
        fp.close()
        for line in fileinput.FileInput('C:\Users\iSpartacus\Desktop\SAVEFILE.csv', inplace=1):
            if line in seen:
                continue
            seen.add(line)
            print line.strip()
        self.ErrorVar.set('Profile saved to SSRC database')

    def database(self, event=None):
        self.text0.text_widget.insert('end', 'Opening SSRC database\n')
        os.system('DB.csv')
        self.text0.text_widget.see('end')

    def addloc(self):
        self.w =popupWindow2(self.parent)
        self.b["state"] = "disabled"
        self.nb.wait_window(self.w.top)
        self.b["state"] = "normal"

        self.text1.text_widget.delete('1.0', END)
        self.ErrorVar.set('')
        if "MS" in lines[7]:
            infile = open(self.ifile, 'r')
            buf = infile.readlines()
            outfile = open(self.ifile, 'w')
            for line in buf:
                if "1ST LINE/" in line:
                    outfile.write(line + '2ND LINE/' + self.e1.get() + '/' + self.e2.get() + '/--/--/LS:' + self.ll[0] + self.ll[1] + '\n' + self.elp)
                else:
                    outfile.write(line)
            self.text1.text_widget.insert('end', open(self.ifile, 'r').read())
            infile.close()
            outfile.close()

    def save_file(self, file):
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        print file
        f.write(str(file))
        f.close()  # `()` was missing.

    def run(self):
        self.text1.text_widget.delete('1.0', END)
        f = open(self.ofile, "r")
        lines = f.readlines()
        f2 = open(self.ifile, "w")
        for line in lines:
            f2.write(line)
        f.close()
        f2.close()
        f = open(self.ifile, "r")
        lines = f.readlines()
        f2 = open(self.ifile, "w")
        for line in lines:
            if '1ST LINE/' in line:
                f2.write(line.strip() + self.e3.get() + '//\n')
            elif '5TH LINE/' in line:
                f2.write(line.strip() + 'COLORS:' + self.e4.get() + '/COSTUME:' + self.e7.get() + '//\n')
            elif '4TH LINE/' in line:
                f2.write('3RD LINE/' + self.e3.get() + '/' + self.e4.get() + '/1/' + self.e2.get() + '/ABCD/-/-/LS:' +
                         self.ll[0] + self.ll[1] + '\n/NAMES:' + self.e9.get() + '//\n' + line)
            else:
                f2.write(line)
        self.text1.text_widget.insert(END, open(self.ifile, 'r').read())
        f.close()
        f2.close()

    def clearKL(self):
        self.text1.text_widget.delete('1.0', END)
        self.text1.text_widget1.delete('1.0', END)
        self.text1.text_widget1.insert(END, 'HANDSCAN:\nTIME    TO      FROM    TEXT\n----------------------------\n')
        self.text1.text_widget2.delete('1.0', END)
        self.text1.text_widget2.insert(END, 'GIST/DURING THE ')
        f = open(self.ofile, "r")
        lines = f.readlines()
        f2 = open(self.ifile, "w")
        for line in lines:
            f2.write(line)
        f.close()
        f2.close()

    def reset(self):
        self.var4.set("Choose One")
        self.var2.set("DATA")
        self.var5.set("DATA")
        self.var3.set("DATA")
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e7.delete(0, END)
        self.e9.delete(0, END)
        self.e12.delete(0, END)
        self.e13.delete(0, END)
        self.e14.delete(0, END)
        self.e15.delete(0, END)
        self.ErrorVar.set("Reset Complete")

    def dumpToFreetext(self):
        f11 = open(self.ifile, 'w')
        self.text1.text_widget.delete(0, END)
        self.text1.text_widget.insert(END, 'Dumped to Freetext')

    def manuals(event=None):
        os.system("C:\Users\iSpartacus\Desktop\Manuals.txt")

    def load(self):  # Instantiates the Load Profile Application Class
        loadframe = tk.Toplevel(app)
        loadframe.geometry('1050x350')
        loadframe.title('Load a Profile from DB')
        startload(loadframe)



    def popup(self):
        self.w=popupWindow(self.parent)
        self.b["state"] = "disabled"
        self.nb.wait_window(self.w.top)
        self.b["state"] = "normal"


    def entryValue(self):
        return self.w.value

    def totalsreset(self):
        self.awptime.set('BOM-EOM')
        self.dstime.set('BOM-EOM')
        self.eltime.set('BOM-EOM')
        self.fhtime.set('BOM-EOM')
        self.fbtime.set('BOM-EOM')
        self.hgtime.set('BOM-EOM')
        self.iltime.set('BOM-EOM')
        self.satime.set('BOM-EOM')
        self.sbtime.set('BOM-EOM')
        self.sstime.set('BOM-EOM')
        self.sttime.set('BOM-EOM')
        self.tltime.set('BOM-EOM')
        self.tvtime.set('BOM-EOM')
        self.tstime.set('BOM-EOM')
        self.awpvalue.set('1')
        self.dsvalue.set('1')
        self.elvalue.set('1')
        self.fhvalue.set('1')
        self.fbvalue.set('1')
        self.hgvalue.set('1')
        self.ilvalue.set('1')
        self.savalue.set('1')
        self.sbvalue.set('1')
        self.stvalue.set('1')
        self.ssvalue.set('1')
        self.tlvalue.set('1')
        self.tvvalue.set('1')
        self.tsvalue.set('1')
        self.awpval.set('0 totals')
        self.dsval.set('0 totals')
        self.elval.set('0 totals')
        self.fhval.set('0 totals')
        self.fbval.set('0 totals')
        self.hgval.set('0 totals')
        self.ilval.set('0 totals')
        self.saval.set('0 totals')
        self.sbval.set('0 totals')
        self.ssval.set('0 totals')
        self.stval.set('0 totals')
        self.tlval.set('0 totals')
        self.tvval.set('0 totals')
        self.tsval.set('0 totals')


TCL_ALL_EVENTS = 0

def startload(loadframe):
    shlist = Load(loadframe,app)
    shlist.mainloop()
    shlist.destroy()

class Load:
    SortDir = True  # descending
    def __init__(self,w,app): #Creates the Frame for the Load Profiles GUI
        self.app = app
        self.loadframe = w
        self.exit = -1
        z = w.winfo_toplevel()
        z.wm_protocol('WM_DELETE_WINDOW', lambda self=self: self.quitcmd())

        top = Tix.Frame(w, relief=Tix.RAISED, bd=1)
        top.pack()

        self.search_var = StringVar()
        self.search_var.trace('w', lambda name, index, mode: self.update_list())
        self.entry = Entry(top, textvariable=self.search_var, width=13)
        self.entry.pack(expand=1, fill=Tix.BOTH, padx=10, pady=10)
        self.dataCols = ('First', 'Last', 'Position', 'Department', 'Office', 'Phone Number')

        top.a = Tix.ScrolledHList(top, options='hlist.columns 6 hlist.header 1')
        top.a.pack(expand=1, fill=Tix.BOTH, padx=10, pady=10)

        box = Tix.ButtonBox(top, orientation=Tix.HORIZONTAL)
        box.add('ok', text='Ok', underline=0, width=6, command=self.okcmd)
        box.add('delete', text='Delete', underline=0, width=6, command=self.scrub)
        box.add('cancel', text='Cancel', underline=0, width=6,
                command=self.quitcmd)

        box.pack(side=Tix.BOTTOM, fill=Tix.X)
        top.pack(side=Tix.TOP, fill=Tix.BOTH, expand=1)

        self.hlist = top.a.hlist

        self.style = {}
        self.style['header'] = Tix.DisplayStyle(Tix.TEXT, refwindow=self.hlist,
                                                anchor=Tix.CENTER, padx=8, pady=2)
        self.style['style1'] = Tix.DisplayStyle(Tix.TEXT, refwindow=self.hlist)

        num = 0
        for c in self.dataCols:
            self.hlist.header_create(num, itemtype=Tix.TEXT, text=c, style=self.style['header'])
            num += 1
        self.hlist.config(width=25, drawbranch=0, indent=10)

        self.update_list()

    def update_list(self):
        self.hlist.delete_all()

        search_term = self.search_var.get()
        in_file = open('DB.csv', 'r')
        lbox_list = []
        for row in in_file:
            lbox_list.append(row.split(','))
        in_file.close()

        self.refresh = []
        for item in lbox_list:
            if search_term.upper() in ''.join(item).upper():
                self.refresh.append(item)

        i = 0
        for first, last, position, department, office, phonenumber in self.refresh:
            self.hlist.add(i, itemtype=Tix.TEXT, text=first, style=self.style['style1'])
            self.hlist.item_create(i, 1, itemtype=Tix.TEXT, text=last, style=self.style['style1'])
            self.hlist.item_create(i, 2, itemtype=Tix.TEXT, text=position, style=self.style['style1'])
            self.hlist.item_create(i, 3, itemtype=Tix.TEXT, text=department, style=self.style['style1'])
            self.hlist.item_create(i, 4, itemtype=Tix.TEXT, text=office, style=self.style['style1'])
            self.hlist.item_create(i, 5, itemtype=Tix.TEXT, text=phonenumber.strip(), style=self.style['style1'])
            i += 1

    def _column_sort(self, col, descending=False):

        data = [(self.hlist.set(child, col), child) for child in self.hlist.get_children('')]
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            self.hlist.move(item[1], '', indx)  # item[1] = item Identifier

            startload.SortDir = not descending

    def okcmd(self):
        curItem = self.refresh[int(self.hlist.info_selection()[0])]
        self.app.reset()
        self.app.e2.insert(END,curItem[0])
        self.app.e3.insert(END,curItem[1])
        self.app.e4.insert(END,curItem[2])
        self.app.e7.insert(END,curItem[3])
        self.app.e9.insert(END,curItem[4])
        self.app.e12.insert(END,curItem[5].strip())
        self.quitcmd()

    def scrub(self):
        reader = open('DB.csv', 'r')
        lines = reader.readlines()
        writer = open('DB.csv', 'w')
        curItem = lines[int(self.hlist.info_selection()[0])]
        self.hlist.delete_all()
        for line in lines:
            if curItem != line:
                writer.write(line)
        reader.close()
        writer.close()
        self.update_list()


    def quitcmd(self):
        self.exit = 0

    def mainloop(self):
        while self.exit < 0:
            self.loadframe.tk.dooneevent(TCL_ALL_EVENTS)

    def destroy(self):
        self.loadframe.destroy()




class Placeholder_State(object):
    __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color = normal_color
    state.normal_font = normal_font
    state.placeholder_color = color
    state.placeholder_font = font
    state.placeholder_text = placeholder
    state.with_placeholder = True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg=state.normal_color, font=state.normal_font)

            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg=state.placeholder_color, font=state.placeholder_font)

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg=color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state

    add_placeholder_to(self.app.e2  , 'CASENOTE')
    add_placeholder_to(self.text1.text_widget1, 'Handscan')

if __name__ == "__main__":
    app = gui_akl(None)
    app.ssrcupdate()
    app.tupdate()
    app.totalsreset()
    app.title('MCS TOOLS')
    app.geometry('1200x675')
    app.mainloop()
