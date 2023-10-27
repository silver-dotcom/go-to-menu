from tkinter import *
from tkinter import ttk
from datetime import datetime
import random
from tkcalendar import Calendar
from PIL import ImageTk, Image
import math
from tkinter import messagebox 
from time import strftime
import tkinter.messagebox

win=Tk()
win.title("Go-To Menu")
win.geometry("525x400+490+150")
win.resizable(0, 0)

icon=PhotoImage(file="main.png")
win.iconphoto(False, icon)

bg_colour="#66d9ff"
secbg_colour="#9cbbd2"
tabcontrol_colour="#4a4a4a"
tab_colour="#000000"
seltab_colour="#0000ff"
tabtext_colour="#ffffff"

path='Main Window.ico'
path1='Line.png'


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground=self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
    def on_enter(self, e):
        self['background']="#4a4a4a"
    def on_leave(self, e):
        self['background']=self.defaultBackground


#================================================MAIN WINDOW================================================

style=ttk.Style()
style.theme_create("tabStyle", settings={
        "TNotebook": {"configure":{"tabmargins": [2, 2, 2, 0], "background":tabcontrol_colour}},
        "TNotebook.Tab": {
            "configure": {"padding":[5, 1], "background":tab_colour, "foreground":tabtext_colour, "font":['tahoma', '11', 'bold']},
            "map":       {"background":[("selected", seltab_colour)],
                          "expand":[("selected", [1, 1, 1, 0])]}}})
style.theme_use("tabStyle")


tabControl=ttk.Notebook(win)
tab0=Frame(tabControl, background=bg_colour)
tab1=Frame(tabControl, background=secbg_colour)
tab2=Frame(tabControl, background=bg_colour)
tab3=Frame(tabControl, background=bg_colour)
tab4=Frame(tabControl, background=bg_colour)
tabControl.add(tab0, text="Home")
tabControl.add(tab1, text="Calculator")
tabControl.add(tab2, text="Converter")
tabControl.add(tab3, text="Clock")
tabControl.add(tab4, text="Expense Tracker")
tabControl.pack(expand=1, fill="both")

dt=datetime.now()
today=dt.strftime("%A, %d %B %Y")
#%A-current day, %d-current date, %B-current month in words, %Y-current year
day=Label(tab0, text="Today is "+today, background=bg_colour, font=('Times', 22, "bold"))
day.grid(padx=25, row=2, sticky=S)

img=ImageTk.PhotoImage(Image.open(path))
panel=Label(tab0, image=img, background=bg_colour)
panel.grid(row=1, sticky=EW)

img1=ImageTk.PhotoImage(Image.open(path1))
panel1=Label(tab0, image=img1, background=bg_colour)
panel1.grid(row=3, sticky=EW)

quotes=["Everything in writing begins with language. Language begins with listening.",
        "The human species thinks in metaphors and learns through stories.",
        "No matter what people tell you, words and ideas can change the world.",
        "You are never too old to set another goal or to dream a new dream.",
        "Shallow men believe in luck. Strong men believe in cause and effect.",
        "Great things are done by a series of small things brought together",
        "Simplicity is about subtracting the obvious and adding the meaningful.",
        "Our kindness may be the most persuasive argument for that which we believe.",
        "As we work to create light for others, we naturally light our own way.",
        "Logic will get you from A to B. Imagination will take you everywhere.",
        ]
names=["Jeanette Winterson",
       "Mary Catherine Bateson",
       "Robin Williams",
       "C.S. Lewis",
       "Ralph Waldo Emerson",
       "Vincent Van Gogh",
       "John Maeda",
       "Gordon B. Hinckley",
       "Mary Anne Radmacher",
       "Albert Einstein",
       ]

c=int(10*random.random())
quote=Label(tab0, text='"'+quotes[c]+'"', background=bg_colour, font=('Times', 13))
quote.grid()
name=Label(tab0, text="-"+names[c], background=bg_colour, font=('Times', 13, "italic"))
name.grid(sticky=EW)




#================================================EXPENSE TRACKER================================================

col1_heading=Label(tab4, text="DATE", font=('tahoma', 11), background=bg_colour)
col2_heading=Label(tab4, text="TITLE", font=('tahoma', 11), background=bg_colour)
col3_heading=Label(tab4, text="AMOUNT", font=('tahoma', 11), background=bg_colour)

col1_heading.grid(row=1, column=0)
col2_heading.grid(row=1, column=1)
col3_heading.grid(row=1, column=2)


height=10
width=3
entrylist=[]
       
for i in range(height): #rows
    for j in range(width): #columns
        b=Entry(tab4, width=11, text="", font=('tahoma', 10), bd=3, fg=tabtext_colour, bg=tab_colour)
        b.grid(row=i+3, column=j, sticky=W)
        entrylist.append(b)
        

global week
week=dt.strftime("%V")#shows current week number with Monday as the first day

def forward():
    global week
    week=int(week)+1
    week_display['text']=f"WEEK {week}"
    for entries in entrylist:
        entries.delete(0, END)
    
def backward():
    global week
    week=int(week)-1
    week_display['text']=f"WEEK {week}"
    for entries in entrylist:
        entries.delete(0, END)

backward_button=HoverButton(tab4, text="<<", command=backward, fg=tabtext_colour, bg=tab_colour, font=('bold'), width=3)
week_display=Label(tab4, text="WEEK "+week, background=bg_colour, font=('tahoma', 11, 'bold'))
forward_button=HoverButton(tab4, text=">>", command=forward, fg=tabtext_colour, bg=tab_colour, font=('bold'), width=3)

backward_button.grid(row=0, column=2, pady=10, ipady=2, sticky=W)
backward_button.place(x=100, y=10)

week_display.grid(row=0, column=3, pady=10, sticky=W)
week_display.place(x=220, y=17)

forward_button.grid(row=0, column=4, pady=10, ipady=2, sticky=W)

cal=Calendar(tab4, background=tab_colour, font=('tahoma', 9),
             headersbackground=tabcontrol_colour, headersforeground=tabtext_colour,
             selectbackground=seltab_colour, selectforeground=tabtext_colour, 
             state="normal")
cal.grid(column=3, padx=10, row=3, rowspan=10, columnspan=2, sticky=W)



#====================================CALCULATOR====================================

global pi
pi=3.14

disp=Entry(tab1, bg=bg_colour, bd=10, width=45, font=('tahoma', 16), justify=CENTER)
disp.grid(row=0, column=0, columnspan=6, padx=2, pady=7, ipady=18)
disp.focus()

def click(n):
    #disp.delete(0,END)
    now=disp.get()
    disp.delete(0,END)
    disp.insert(0,str(now)+str(n))
def clear():
    disp.delete(0,END)

def add():
    global m
    global p
    n1=disp.get()
    m=float(n1)
    p="add"
    disp.delete(0,END)
    
def sub():
    global m
    global p
    n1=disp.get()
    p="sub"
    m=float(n1)
    disp.delete(0,END)

def mul():
    global m
    global p
    n1=disp.get()
    p="mul"
    m=float(n1)
    disp.delete(0,END)

def div():
    global m
    global p
    n1=disp.get()
    p="div"
    m=float(n1)
    disp.delete(0,END)

def sqroot():
    global m
    global p
    n1=disp.get()
    m=float(n1)
    p="root"
    disp.delete(0,END)
def inverse():
    global m
    global p
    n1=disp.get()
    m=float(n1)
    p="1/x"
    disp.delete(0,END)

def sin():
    global m
    global p
    n1=disp.get()
    m=float(n1)
    p="sin"
    disp.delete(0,END)

def cos():
    global m
    global p

    n1=disp.get()
    m=float(n1)
    p="cos"
    disp.delete(0,END)

def tan():
    global m
    global p
    n1=disp.get()
    m=float(n1)
    p="tan"
    disp.delete(0,END)

def equal():
    n2=disp.get()
    disp.delete(0,END)
    
    if p=="add":
        l=float(n2)
        disp.insert(0,m+l)
    elif p=="sub":
        l=float(n2)
        disp.insert(0,m-l)
    elif p=="mul":
        l=float(n2)
        disp.insert(0,m*l)
    elif p=="div":
        l=float(n2)
        if l==0:
            disp.insert(0,"ERROR!!!!")
        else:
            disp.insert(0,m/l)
    elif p=="root":
        disp.insert(0,math.sqrt(m))
    elif p=="1/x":
        if m==0:
            disp.insert(0,"ERROR!!")
        else:
            disp.insert(0,1/m)
    elif p=="sin":
        disp.insert(0,math.sin(m*pi/180))
    elif p=="cos":
        disp.insert(0,math.cos(m*pi/180))
    elif p=="tan":
        disp.insert(0,math.tan(m*pi/180))
    
    
    
button1=Button(tab1, text="1", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(1)).grid(row=3, column=0, sticky=NSEW)
button2=Button(tab1, text="2", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(2)).grid(row=3, column=1, sticky=NSEW)
button3=Button(tab1, text="3", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(3)).grid(row=3, column=2, sticky=NSEW)
button4=Button(tab1, text="4", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(4)).grid(row=2, column=0, sticky=NSEW)
button5=Button(tab1, text="5", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(5)).grid(row=2, column=1, sticky=NSEW)
button6=Button(tab1, text="6", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(6)).grid(row=2, column=2, sticky=NSEW)
button7=Button(tab1, text="7", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(7)).grid(row=1, column=0, sticky=NSEW)
button8=Button(tab1, text="8", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(8)).grid(row=1, column=1, sticky=NSEW)
button9=Button(tab1, text="9", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(9)).grid(row=1, column=2, sticky=NSEW)
button10=Button(tab1, text="0", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click(0)).grid(row=4, column=0, sticky=NSEW)

bdot=Button(tab1, text=".", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=lambda:click('.')).grid(row=4, column=1, sticky=NSEW)
bclear=Button(tab1, text="A/C", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=clear).grid(row=4, column=2, sticky=NSEW)
badd=Button(tab1, text="+", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=add).grid(row=1, column=3, rowspan=2, sticky=NSEW)
bsub=Button(tab1, text="-", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=sub).grid(row=1, column=4, sticky=NSEW)
bmul=Button(tab1, text="*", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=mul).grid(row=1, column=5, sticky=NSEW)
bdiv=Button(tab1, text="/", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=div).grid(row=3, column=5, sticky=NSEW)
bcos=Button(tab1, text="cos", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=cos).grid(row=4, column=4, sticky=NSEW)
btan=Button(tab1, text="tan", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=tan).grid(row=4, column=5, sticky=NSEW)
bsin=Button(tab1, text="sin", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=sin).grid(row=4, column=3, sticky=NSEW)

bequal=Button(tab1, text="=", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=equal).grid(row=3, columnspan=2, column=3, sticky=NSEW)
brecip=Button(tab1, text="1/x", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=inverse).grid(row=2, column=4, sticky=NSEW)
broot=Button(tab1, text="√x", padx=30, pady=10, fg="white", bg="black", height=2, width=1, font=('tahoma', 11, 'bold'), command=sqroot).grid(row=2, column=5, sticky=NSEW)



#================================================CLOCK================================================


#========================TIMER========================

def timer():
    import time
## creating Tk window
    win=Toplevel(background=bg_colour)
  
## Using title() to display a message in the dialogue box of the message in the title bar.
    win.title("Timer")
    win.geometry("525x400+490+150")

    timericon=PhotoImage(file="clock.png")
    win.iconphoto(False, timericon)
    
    L0=Label(win, font=('tahoma', 20, 'bold'), height=2, width=75, text='Countdown Time', bg="#ccf2ff")
    L0.place(x=270, y=35, anchor='center')

    def countdown():
        temp = int(hrs.get())*3600 + int(mins.get())*60 + int(secs.get())
        while temp > -1:
            minute = temp // 60 ##it gives floor division/quotient
            second = temp % 60 ##it gives remainder

            hour = 0
            if minute > 60:
                hour = minute // 60 
                minute = minute % 60
      
            secs.set(second)
            mins.set(minute)
            hrs.set(hour)

            
            win.update()
            time.sleep(1)
        ## when temp value = 0; then a messagebox pop's up with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
         
        ## after every one sec the value of temp will be decremented by one
            temp -= 1


## Declaration of variables
    hrs=StringVar()
    mins=StringVar()
    secs=StringVar()
  
## setting the default value as 0
    hrs.set("00")
    mins.set("00")
    secs.set("00")
    
## Use of Entry class to take input from the user
    hrsEntry= Entry(win, width=3, font=('tahoma', 20), textvariable=hrs)
    hrsEntry.place(x=210, y=130)

    minsEntry= Entry(win, width=3, font=('tahoma', 20), textvariable=mins)
    minsEntry.place(x=255, y=130)

    secsEntry=Entry(win, width=3, font=('tahoma', 20), textvariable=secs)
    secsEntry.place(x=300, y=130)

    L1=Label(win, font=('tahoma', 15), text="Enter :", bg=bg_colour)
    L1.place(x=125, y=132)

    L2=Label(win, font=('tahoma', 12), text="hrs", bg=bg_colour)
    L2.place(x=210, y=105) 

    L3=Label(win, font=('tahoma', 12), text="mins", bg=bg_colour)
    L3.place(x=253, y=105)

    L4=Label(win, font=('tahoma', 12), text="secs", bg=bg_colour)
    L4.place(x=301, y=105)

    btn = HoverButton(win, font=('tahoma', 18, 'bold'), width=20, text='Set Time Countdown', bg=tab_colour, fg=tabtext_colour, command=countdown)
    btn.place(x=110, y=210)
    

#========================STOPWATCH========================
    
counter = -1
running = False

def stop():
    import tkinter
    
    win=Toplevel(background=bg_colour)
    win.title("Stopwatch")
    win.geometry("525x400+490+150")
    stopicon=PhotoImage(file="clock.png")
    win.iconphoto(False, stopicon)
    
    label=Label(win, text="Welcome!", fg=tab_colour, bg=bg_colour, font=('tahoma', 24, 'bold'))
    label.place(x=270, y=90, anchor='center')
    
    def counter_label(label):
        def count():
            if running:
                global counter
                if counter==-1:             ## To manage the intial delay.
                    display="Starting..."
                else:
                    display=str(counter)
                label.configure(text=display)

                label.after(1000, count)    ## Delays by 1000ms=1 seconds and call count again
                counter += 1
        ##Triggering the start of the counter
        count()     

    ##start function of the stopwatch
    def Start(label):
        global running
        running=True
        counter_label(label)
        start['state']='disabled'
        stop['state']='normal'
        reset['state']='normal'

    ##Stop function of the stopwatch
    def Stop():
        global running
        start['state']='normal'
        stop['state']='disabled'
        reset['state']='normal'
        running = False

    ##Reset function of the stopwatch
    def Reset(label):
        global counter
        counter=-1
        if running==False:      ## If rest is pressed after pressing stop.
            reset['state']='disabled'
            label['text']='Welcome!'
        else:                          ## If reset is pressed while the stopwatch is running.
            label['text']='Starting...'

    start=HoverButton(win, font=('tahoma', 15, 'bold'), text='Start', bd='5', width=15, bg=tab_colour, fg=tabtext_colour, command=lambda:Start(label))
    stop=HoverButton(win, font=('tahoma', 15, 'bold'), text='Stop', bd='5', width=15, bg=tab_colour, fg=tabtext_colour, state='disabled', command=Stop)
    reset=HoverButton(win, font=('tahoma', 15, 'bold'), text='Reset', bd='5',width=15, bg=tab_colour, fg=tabtext_colour, state='disabled', command=lambda:Reset(label))

    start.place(x=160, y=140)
    stop.place(x=160, y=200)
    reset.place(x=160, y=260)

    
  
## This function is used to display time on the label 
def time(): 
    s=strftime('%H:%M:%S %p') 
    A.configure(text=s) 
    A.after(1000, time) ##here we are passing two arguments(arg1,arg2)arg1:millsec=1000,arg2=time 

## Styling the label widget so that clock will look more attractive 
A=Label(tab3, font=('tahoma', 30, 'bold'), background=tab_colour, foreground=tabtext_colour) 
## Placing clock at the centre of the tkinter window
A.grid(row=0, column=0, ipady=5, ipadx=5, padx=125, pady=70)

time()

##button for timer 
btn=HoverButton(tab3, font=('tahoma', 18, 'bold'), width=12, text='Timer', bg=tab_colour, fg=tabtext_colour, command=timer)
btn.grid(row=1, column=0, pady=10)

##button for stopwatch 
btn1=HoverButton(tab3, font=('tahoma', 18, 'bold'), width=12, text='Stopwatch', bg=tab_colour, fg=tabtext_colour, command=stop)
btn1.grid(row=2, column=0, pady=6)



#================================================CONVERTER================================================

#hoverable button code for Currency
def currenter(k):
    currbut['background'] = '#4A4A4A'
    currbut['foreground'] = 'WHITE'

def currleave(k):
    currbut['background'] = 'BLACK'
    currbut['foreground'] = 'WHITE'
    
#hoverable button code for Length
def lenenter(k):
    Lengthbut['background'] = '#4A4A4A'
    Lengthbut['foreground'] = 'WHITE'

def lenleave(k):
    Lengthbut['background'] = 'BLACK'
    Lengthbut['foreground'] = 'WHITE'

#hoverable button code for Temperature
def tempenter(m):
    tempbut['background'] = '#4A4A4A'
    tempbut['foreground'] = 'WHITE'

def templeave(m):
    tempbut['background'] = 'BLACK'
    tempbut['foreground'] = 'WHITE'

#hoverable button code fo Weight
def weightenter(n):
    weightbut['background'] = '#4A4A4A'
    weightbut['foreground'] = 'WHITE'

def weightleave(n):
    weightbut['background'] = 'BLACK'
    weightbut['foreground'] = 'WHITE'

def currency_window():
    #hoverable button code for Convert
    def conenter(m):
        Label_8['background'] = '#4A4A4A'
        Label_8['foreground'] = 'WHITE'

    def conleave(m):
        Label_8['background'] = 'BLACK'
        Label_8['foreground'] = 'WHITE'

    #hoverable button code for clear all
    def clrenter(n):
        Label_9['background'] = '#4A4A4A'
        Label_9['foreground'] = 'WHITE'

    def clrleave(n):
        Label_9['background'] = 'BLACK'
        Label_9['foreground'] = 'WHITE'
        
    currtop = Toplevel()
    currtop.title("Currency Conversion")
    #icon
    curricon = PhotoImage(file ="currency.png")
    currtop.iconphoto(False, curricon)

    Tops = Frame(currtop,bg = '#CCF2FF',pady = 2, width =1850, height = 100, relief = "ridge")
    Tops.grid(row=0,column=0)

    headlabel = Label(Tops,font=('tahoma', 24,'bold'),
                         text = '              Convert Currency              ',
                         bg= '#CCF2FF',fg='black')  
    headlabel.grid(row=1, column=0,sticky=W)

    #to save units chosen 
    currvar1 = StringVar(currtop) 
    currvar2 = StringVar(currtop) 
     
    currvar1.set("currency")
    currvar2.set("currency")


    #conversion code
    def CurrencyConversion():
        from forex_python.converter import CurrencyRates
        c=CurrencyRates()
        
        from_currunit = currvar1.get() 
        to_currunit = currvar2.get()
        
        if (currval1_field.get()==""):
            tkinter.messagebox.showinfo("Error !!","Value Not Entered.\n Please Enter a Value.")
            
        elif (from_currunit=="currency" or to_currunit=="currency"):
            tkinter.messagebox.showinfo("Error !!","Currency Not Selected.\n Please select a Currency from the Options.")

        else:
            valuein = c.convert(from_currunit,to_currunit,float(currval1_field.get()))
            converted = float("{:.4f}".format(valuein))
            currval2_field.insert(0, str(converted))

    #Erase everything code
    def clear_all() : 
            currval1_field.delete(0, END) 
            currval2_field.delete(0, END)

    #Option list    
    CurrencyUnit_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    #window
    currtop.configure(background = '#66D9FF') 
    currtop.geometry("525x400+490+150")

    #labels
    label1 = Label(currtop, font=('tahoma', 15,'bold'), text = "\t  Value  :  ", bg="#66D9FF",fg = "black") 
    label1.place(x=0, y=90)

    label1 = Label(currtop, font=('tahoma', 15,'bold'), text = "\t  From Currency   :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=140)

    label1 = Label(currtop, font=('tahoma', 15,'bold'), text = "\t  To Currency   :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=190)

    label1 = Label(currtop, font=('tahoma', 15,'bold'), text = "\t  Converted Value  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=308)

    #blank label to create space to align
    Label_1 =Label(currtop, font=('tahoma', 15,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=250)

    #blank label to create space to align
    Label_1 =Label(currtop, font=('tahoma', 15,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=350)

    #dropdown
    Fromcurrunit_option = OptionMenu(currtop, currvar1, *CurrencyUnit_list) 
    Tocurrunit_option = OptionMenu(currtop, currvar2, *CurrencyUnit_list) 

    Fromcurrunit_option.place(x=300, y=140)
    Tocurrunit_option.place(x=300, y=190) 

    #Input and output textbox
    currval1_field = Entry(currtop) 
    currval1_field.place(x=300, y=95)
    currval2_field = Entry(currtop)
    currval2_field.place(x=300, y=315) 

    #Convert Button Code
    Label_8 =Button(currtop, font=('tahoma', 15,'bold'), text="   Convert  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=CurrencyConversion)
    Label_8.place(x=105, y=245)
    Label_8.bind("<Enter>", conenter)
    Label_8.bind("<Leave>", conleave)

    #blank label to create space to align
    Label_1 =Label(currtop, font=('tahoma', 7,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=180)

    #Clear all button code
    Label_9 =Button(currtop, font=('tahoma', 15,'bold'), text="   Clear All  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=clear_all)
    Label_9.place(x=300, y=245)
    Label_9.bind("<Enter>", clrenter)
    Label_9.bind("<Leave>", clrleave)

def length_window():
    #hoverable button code for Convert
    def conenter(e):
        Label_8['background'] = '#4A4A4A'
        Label_8['foreground'] = 'WHITE'

    def conleave(e):
        Label_8['background'] = 'BLACK'
        Label_8['foreground'] = 'WHITE'

    #hoverable button code for clear all
    def clrenter(f):
        Label_9['background'] = '#4A4A4A'
        Label_9['foreground'] = 'WHITE'

    def clrleave(f):
        Label_9['background'] = 'BLACK'
        Label_9['foreground'] = 'WHITE'
        
    lentop=Toplevel()
    lentop.title("Length Conversion")
    #icon
    lenicon = PhotoImage(file = "length.png")
    lentop.iconphoto(False,lenicon)

    lentops = Frame(lentop,bg = '#CCF2FF',pady = 2, width =1850, height = 100, relief = "ridge")
    lentops.grid(row=0,column=0)

    headlabel = Label(lentops,font=('tahoma', 24,'bold'),
                     text = '               Convert Length                          ',
                     bg= '#CCF2FF',fg='black')  
    headlabel.grid(row=1, column=0,sticky=W)

    #to save units chosen 
    lenvar1 = StringVar() 
    lenvar2 = StringVar() 
 
    lenvar1.set("unit")
    lenvar2.set("unit")


    #conversion code
    def LengthConversion(): 
        from_lenunit = lenvar1.get() 
        to_lenunit = lenvar2.get()
    
        if (lenval1_field.get()==""):
            tkinter.messagebox.showinfo("Error !!","Value Not Entered.\n Please Enter a Value.")
        
        elif (from_lenunit=="unit" or to_lenunit=="unit"):
            tkinter.messagebox.showinfo("Error !!","Length Unit Not Selected.\n Please select the Units of Length from the Options.")

    ##["km", "m", "cm", "mm", "foot", "inch"]
    ##from mm to all
        elif (from_lenunit=="mm" and to_lenunit=="cm"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 10)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="mm" and to_lenunit=="m"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 1000)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="mm" and to_lenunit=="km"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 1000000)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="mm" and to_lenunit=="foot"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 305)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="mm" and to_lenunit=="inch"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 25.4)
            lenval2_field.insert(0, str(converted))

    ##["km", "m", "cm", "mm", "foot", "inch"]
    ##from cm to all
        elif (from_lenunit=="cm" and to_lenunit=="mm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 10)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="cm" and to_lenunit=="m"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 100)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="cm" and to_lenunit=="km"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 100000)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="cm" and to_lenunit=="foot"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 30.48)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="cm" and to_lenunit=="inch"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 2.54)
            lenval2_field.insert(0, str(converted))

    ##["km", "m", "cm", "mm", "foot", "inch"]
    ##from m to all
        elif (from_lenunit=="m" and to_lenunit=="cm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 100)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="m" and to_lenunit=="mm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 1000)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="m" and to_lenunit=="km"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 1000)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="m" and to_lenunit=="foot"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 3.281)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="m" and to_lenunit=="inch"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 39.37)
            lenval2_field.insert(0, str(converted))

    ##["km", "m", "cm", "mm", "foot", "inch"]
    ##from km to all
        elif (from_lenunit=="km" and to_lenunit=="m"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 1000)
            lenval2_field.insert(0, str(converted))
            
        elif (from_lenunit=="km" and to_lenunit=="cm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 100000)
            lenval2_field.insert(0, str(converted))
            
        elif (from_lenunit=="km" and to_lenunit=="mm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 1000000)
            lenval2_field.insert(0, str(converted))
            
        elif (from_lenunit=="km" and to_lenunit=="foot"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 3281)
            lenval2_field.insert(0, str(converted))
        
        elif (from_lenunit=="km" and to_lenunit=="inch"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 39370)
            lenval2_field.insert(0, str(converted))

    ##["km", "m", "cm", "mm", "foot", "inch"]
    ##from foot to all
        elif (from_lenunit=="foot" and to_lenunit=="mm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 305)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="foot" and to_lenunit=="cm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 30.48)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="foot" and to_lenunit=="m"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 3.281)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="foot" and to_lenunit=="km"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 3281)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="foot" and to_lenunit=="inch"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 12)
            lenval2_field.insert(0, str(converted))

    ##["km", "m", "cm", "mm", "foot", "inch"]
    ##from inch to all
        elif (from_lenunit=="inch" and to_lenunit=="mm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 25.4)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="inch" and to_lenunit=="cm"):
            valuein = int(lenval1_field.get())
            converted= (valuein * 2.54)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="inch" and to_lenunit=="m"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 39.37)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="inch" and to_lenunit=="km"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 39370)
            lenval2_field.insert(0, str(converted))

        elif (from_lenunit=="inch" and to_lenunit=="foot"):
            valuein = int(lenval1_field.get())
            converted= (valuein / 12)
            lenval2_field.insert(0, str(converted))

        else:
            tkinter.messagebox.showinfo("Error !!","Try Again!")

    #Erase everything code
    def clear_all() : 
            lenval1_field.delete(0, END) 
            lenval2_field.delete(0, END)

    #Option list    
    LengthUnit_list = ["km", "m", "cm", "mm", "foot", "inch"]

    lentop.configure(background = '#66D9FF')
    lentop.geometry("525x400+490+150")
##    button1= Button(lentop, text="close", command=lentop.destroy)
##    button1.pack()
    #labels
    label1 = Label(lentop, font=('tahoma', 15, 'bold'), text = "\t  Value  :  ", bg="#66D9FF",fg = "black") 
    label1.place(x=0, y=90)

    label1 = Label(lentop, font=('tahoma', 15, 'bold'), text = "\t  From Length in  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=140)

    label1 = Label(lentop, font=('tahoma', 15,'bold'), text = "\t  To Length in  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=190)

    label1 = Label(lentop, font=('tahoma', 15, 'bold'), text = "\t  Converted Value  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=308)

    #blank label to create space to align
    Label_1 =Label(lentop, font=('tahoma', 15, 'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=250)

    #blank label to create space to align
    Label_1 =Label(lentop, font=('tahoma', 15, 'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=350)

    #dropdown
    FromLenunit_option = OptionMenu(lentop, lenvar1, *LengthUnit_list) 
    ToLenunit_option = OptionMenu(lentop, lenvar2, *LengthUnit_list) 

    FromLenunit_option.place(x=300, y=140)
    ToLenunit_option.place(x=300, y=190) 

    #Input and output textbox
    lenval1_field = Entry(lentop) 
    lenval1_field.place(x=300, y=95)
    lenval2_field = Entry(lentop)
    lenval2_field.place(x=300, y=315) 

    #Convert Button Code
    Label_8 =Button(lentop, font=('tahoma', 15, 'bold'), text="   Convert  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=LengthConversion)
    Label_8.place(x=105, y=245)
    Label_8.bind("<Enter>", conenter)
    Label_8.bind("<Leave>", conleave)

    #blank label to create space to align
    Label_1 =Label(lentop, font=('tahoma', 7, 'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=180)

    #Clear all button code
    Label_9 =Button(lentop, font=('tahoma', 15, 'bold'), text="   Clear All  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=clear_all)
    Label_9.place(x=300, y=245)
    Label_9.bind("<Enter>", clrenter)
    Label_9.bind("<Leave>", clrleave)

def temperature_window():
    #hoverable button code for Convert
    def conenter(g):
        Label_8['background'] = '#4A4A4A'
        Label_8['foreground'] = 'WHITE'

    def conleave(g):
        Label_8['background'] = 'BLACK'
        Label_8['foreground'] = 'WHITE'

    #hoverable button code for clear all
    def clrenter(h):
        Label_9['background'] = '#4A4A4A'
        Label_9['foreground'] = 'WHITE'

    def clrleave(h):
        Label_9['background'] = 'BLACK'
        Label_9['foreground'] = 'WHITE'

    temptop = Toplevel() 
    temptop.title("Temperature Conversion")
    #icon
    icon = PhotoImage(file = "temp.png")
    temptop.iconphoto(False,icon)

    Tops = Frame(temptop, bg = '#CCF2FF',pady = 2, width =1850, height = 100, relief = "ridge")
    Tops.grid(row=0,column=0)

    headlabel = Label(Tops,font=('tahoma', 24, 'bold'),
                         text = '          Convert Temperature                         ',
                         bg= '#CCF2FF',fg='black')  
    headlabel.grid(row=1, column=0,sticky=W)

    #to save units chosen 
    tempvar1 = StringVar(temptop) 
    tempvar2 = StringVar(temptop) 
     
    tempvar1.set("unit")
    tempvar2.set("unit")


    #conversion code
    def TemperatureConversion(): 
        from_tempunit = tempvar1.get() 
        to_tempunit = tempvar2.get()
        
        if (tempval1_field.get()==""):
            tkinter.messagebox.showinfo("Error !!","Value Not Entered.\n Please Enter a Value.")
            
        elif (from_tempunit=="unit" or to_tempunit=="unit"):
            tkinter.messagebox.showinfo("Error !!","Temperature Unit Not Selected.\n Please select the Units of Temperature from the Options.")

    ##["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
    ##from Celsius to all
        elif (from_tempunit=="Celsius" and to_tempunit=="Fahrenheit"):
            valuein = int(tempval1_field.get())
            converted= ((valuein * 9/5) +32)
            tempval2_field.insert(0, str(converted))

        elif (from_tempunit=="Celsius" and to_tempunit=="Kelvin"):
            valuein = int(tempval1_field.get())
            converted= (valuein + 273.15)
            tempval2_field.insert(0, str(converted))

        elif (from_tempunit=="Celsius" and to_tempunit=="Rankine"):
            valuein = int(tempval1_field.get())
            converted= ((valuein + 273.15) * 9/5)
            tempval2_field.insert(0, str(converted))

    ##["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
    ##from Fahrenheit to all
        elif (from_tempunit=="Fahrenheit" and to_tempunit=="Celsius"):
            valuein = int(tempval1_field.get())
            converted= ((valuein - 32) * 5/9)
            tempval2_field.insert(0, str(converted))

        elif (from_tempunit=="Fahrenheit" and to_tempunit=="Kelvin"):
            valuein = int(tempval1_field.get())
            converted= ((valuein - 32) * 5/9 + 273.15)
            tempval2_field.insert(0, str(converted))

        elif (from_tempunit=="Fahrenheit" and to_tempunit=="Rankine"):
            valuein = int(tempval1_field.get())
            converted= (valuein + 459.67)
            tempval2_field.insert(0, str(converted))

    ##["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
    ##from Kelvin to all
        elif (from_tempunit=="Kelvin" and to_tempunit=="Celsius"):
            valuein = int(tempval1_field.get())
            converted= (valuein - 273.15)
            tempval2_field.insert(0, str(converted))

        elif (from_tempunit=="Kelvin" and to_tempunit=="Fahrenheit"):
            valuein = int(tempval1_field.get())
            converted= ((valuein - 273.15) * 9/5 + 32)
            tempval2_field.insert(0, str(converted))

        elif (from_tempunit=="Kelvin" and to_tempunit=="Rankine"):
            valuein = int(tempval1_field.get())
            converted= (valuein * 9/5)
            tempval2_field.insert(0, str(converted))

    ##["Celsius", "Fahrenheit", "Kelvin", "Rankine"]
    ##from Rankine to all
        elif (from_tempunit=="Rankine" and to_tempunit=="Celsius"):
            valuein = int(tempval1_field.get())
            converted= ((valuein - 491.67) * 5/9)
            tempval2_field.insert(0, str(converted))
            
        elif (from_tempunit=="Rankine" and to_tempunit=="Fahrenheit"):
            valuein = int(tempval1_field.get())
            converted= (valuein - 459.67)
            tempval2_field.insert(0, str(converted))
            
        elif (from_tempunit=="Rankine" and to_tempunit=="Kelvin"):
            valuein = int(tempval1_field.get())
            converted= (valuein *  5/9)
            tempval2_field.insert(0, str(converted))

    #Erase everything code
    def clear_all() : 
            tempval1_field.delete(0, END) 
            tempval2_field.delete(0, END)

    #Option list    
    TemperatureUnit_list = ["Celsius", "Fahrenheit", "Kelvin", "Rankine"]

    #window
    temptop.configure(background = '#66D9FF') 
    temptop.geometry("525x400+490+150")

    #labels
    label1 = Label(temptop,font=('tahoma', 15,'bold'), text = "\t  Value  :  ", bg="#66D9FF",fg = "black") 
    label1.place(x=0, y=90)

    label1 = Label(temptop,font=('tahoma', 15,'bold'), text = "\t  From Temperature in  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=140)

    label1 = Label(temptop,font=('tahoma', 15,'bold'), text = "\t  To Temperature in  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=190)

    label1 = Label(temptop,font=('tahoma', 15,'bold'), text = "\t  Converted Value  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=308)

    #blank label to create space to align
    Label_1 =Label(temptop, font=('tahoma', 15,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=250)

    #blank label to create space to align
    Label_1 =Label(temptop, font=('tahoma', 15,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=350)

    #dropdown
    Fromtempunit_option = OptionMenu(temptop, tempvar1, *TemperatureUnit_list) 
    Totempunit_option = OptionMenu(temptop, tempvar2, *TemperatureUnit_list) 

    Fromtempunit_option.place(x=360, y=140)
    Totempunit_option.place(x=360, y=190) 

    #Input and output textbox
    tempval1_field = Entry(temptop) 
    tempval1_field.place(x=300, y=95)
    tempval2_field = Entry(temptop)
    tempval2_field.place(x=300, y=315) 

    #Convert Button Code
    Label_8 =Button(temptop, font=('tahoma', 15,'bold'), text="   Convert  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=TemperatureConversion)
    Label_8.place(x=105, y=245)
    Label_8.bind("<Enter>", conenter)
    Label_8.bind("<Leave>", conleave)

    #blank label to create space to align
    Label_1 =Label(temptop, font=('tahoma', 7,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=180)

    #Clear all button code
    Label_9 =Button(temptop, font=('tahoma', 15,'bold'), text="   Clear All  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=clear_all)
    Label_9.place(x=300, y=245)
    Label_9.bind("<Enter>", clrenter)
    Label_9.bind("<Leave>", clrleave)

def weight_window():
    #hoverable button code for Convert
    def conenter(i):
        Label_8['background'] = '#4A4A4A'
        Label_8['foreground'] = 'WHITE'

    def conleave(i):
        Label_8['background'] = 'BLACK'
        Label_8['foreground'] = 'WHITE'

    #hoverable button code for clear all
    def clrenter(j):
        Label_9['background'] = '#4A4A4A'
        Label_9['foreground'] = 'WHITE'

    def clrleave(j):
        Label_9['background'] = 'BLACK'
        Label_9['foreground'] = 'WHITE'

    weighttop = Toplevel() 
    weighttop.title("Weight Conversion")
    #icon
    icon = PhotoImage(file = "weight.png")
    weighttop.iconphoto(False,icon)

    Tops = Frame(weighttop,bg = '#CCF2FF',pady = 2, width =1850, height = 100, relief = "ridge")
    Tops.grid(row=0,column=0)

    headlabel = Label(Tops,font=('tahoma', 24,'bold'),
                         text = '                Convert Weight               ',
                         bg= '#CCF2FF',fg='black')  
    headlabel.grid(row=1, column=0,sticky=W)

    #to save units chosen 
    weightvar1 = StringVar(weighttop) 
    weightvar2 = StringVar(weighttop) 
     
    weightvar1.set("unit")
    weightvar2.set("unit")


    #conversion code
    def WeightConversion(): 
        from_weightunit = weightvar1.get() 
        to_weightunit = weightvar2.get()
        
        if (weightval1_field.get()==""):
            tkinter.messagebox.showinfo("Error !!","Value Not Entered.\n Please Enter a Value.")
            
        elif (from_weightunit=="unit" or to_weightunit=="unit"):
            tkinter.messagebox.showinfo("Error !!","Weight Unit Not Selected.\n Please select the Units of Weight from the Options.")

    ##["Tonne", "Kilograms", "Grams", "Pound", "Ounce"]
    ##from Tonne to all
        elif (from_weightunit=="Tonne" and to_weightunit=="Kilograms"):
            valuein = int(weightval1_field.get())
            converted= (valuein *1000)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Tonne" and to_weightunit=="Grams"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 1000000)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Tonne" and to_weightunit=="Pound"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 2205)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Tonne" and to_weightunit=="Ounce"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 35274)
            weightval2_field.insert(0, str(converted))

    ##["Tonne", "Kilograms", "Grams", "Pound", "Ounce"]
    ##from Kilograms to all
        elif (from_weightunit=="Kilograms" and to_weightunit=="Tonne"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 1000)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Kilograms" and to_weightunit=="Grams"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 1000)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Kilograms" and to_weightunit=="Pound"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 2.205)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Kilograms" and to_weightunit=="Ounce"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 35.274)
            weightval2_field.insert(0, str(converted))

    ##["Tonne", "Kilograms", "Grams", "Pound", "Ounce"]
    ##from Grams to all
        elif (from_weightunit=="Grams" and to_weightunit=="Tonne"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 1000000)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Grams" and to_weightunit=="Kilograms"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 1000)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Grams" and to_weightunit=="Pound"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 454)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Grams" and to_weightunit=="Ounce"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 28.35)
            weightval2_field.insert(0, str(converted))

    ##["Tonne", "Kilograms", "Grams", "Pound", "Ounce"]
    ##from Pound to all
        elif (from_weightunit=="Pound" and to_weightunit=="Tonne"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 2205)
            weightval2_field.insert(0, str(converted))
            
        elif (from_weightunit=="Pound" and to_weightunit=="Kilograms"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 2.205)
            weightval2_field.insert(0, str(converted))
            
        elif (from_weightunit=="Pound" and to_weightunit=="Grams"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 454)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Pound" and to_weightunit=="Ounce"):
            valuein = int(weightval1_field.get())
            converted= (valuein * 16)
            weightval2_field.insert(0, str(converted))

    ##["Tonne", "Kilograms", "Grams", "Pound", "Ounce"]
    ##from Ounce to all
        elif (from_weightunit=="Ounce" and to_weightunit=="Tonne"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 35274)
            weightval2_field.insert(0, str(converted))
            
        elif (from_weightunit=="Ounce" and to_weightunit=="Kilograms"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 35.274)
            weightval2_field.insert(0, str(converted))
            
        elif (from_weightunit=="Ounce" and to_weightunit=="Grams"):
            valuein = int(weightval1_field.get())
            converted= (valuein *28.35)
            weightval2_field.insert(0, str(converted))

        elif (from_weightunit=="Ounce" and to_weightunit=="Pound"):
            valuein = int(weightval1_field.get())
            converted= (valuein / 16)
            weightval2_field.insert(0, str(converted))

    #Erase everything code
    def clear_all() : 
            weightval1_field.delete(0, END) 
            weightval2_field.delete(0, END)

    #Option list    
    WeightUnit_list = ["Tonne", "Kilograms", "Grams", "Pound", "Ounce"]

    #window
    weighttop.configure(background = '#66D9FF') 
    weighttop.geometry("525x400+490+150")

    #labels
    label1 = Label(weighttop,font=('tahoma', 15,'bold'), text = "\t  Value  :  ", bg="#66D9FF",fg = "black") 
    label1.place(x=0, y=90)

    label1 = Label(weighttop,font=('tahoma', 15,'bold'), text = "\t  From Weight in  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=140)

    label1 = Label(weighttop,font=('tahoma', 15,'bold'), text = "\t  To Weight in  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=190)

    label1 = Label(weighttop,font=('tahoma', 15,'bold'), text = "\t  Converted Value  :  ", bg="#66D9FF",
                      fg = "black") 
    label1.place(x=0, y=308)

    #blank label to create space to align
    Label_1 =Label(weighttop, font=('tahoma', 15,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=250)

    #blank label to create space to align
    Label_1 =Label(weighttop, font=('tahoma', 15,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=350)

    #dropdown
    Fromweightunit_option = OptionMenu(weighttop, weightvar1, *WeightUnit_list) 
    Toweightunit_option = OptionMenu(weighttop, weightvar2, *WeightUnit_list) 

    Fromweightunit_option.place(x=300, y=140)
    Toweightunit_option.place(x=300, y=190) 

    #Input and output textbox
    weightval1_field = Entry(weighttop) 
    weightval1_field.place(x=300, y=95)
    weightval2_field = Entry(weighttop)
    weightval2_field.place(x=300, y=315) 

    #Convert Button Code
    Label_8 =Button(weighttop, font=('tahoma', 15,'bold'), text="   Convert  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=WeightConversion)
    Label_8.place(x=105, y=245)
    Label_8.bind("<Enter>", conenter)
    Label_8.bind("<Leave>", conleave)

    #blank label to create space to align
    Label_1 =Label(weighttop, font=('tahoma', 7,'bold'), text="",padx=2,pady=2, bg="#66D9FF",fg ="black")
    Label_1.place(x=0, y=180)

    #Clear all button code
    Label_9 =Button(weighttop, font=('tahoma', 15,'bold'), text="   Clear All  ",padx=2,pady=2,
                    bg= "BLACK", fg= "WHITE", command=clear_all)
    Label_9.place(x=300, y=245)
    Label_9.bind("<Enter>", clrenter)
    Label_9.bind("<Leave>", clrleave)    

########################################################
    

#Currency Button Code
currbut =Button(tab2, font=('tahoma', 15, 'bold'), text="   Currency  ", padx=2, pady=2,
                bg="BLACK", fg="WHITE", command=currency_window)
currbut.place(x=192, y=60)
currbut.bind("<Enter>", currenter)
currbut.bind("<Leave>", currleave)

#Length Button Code
Lengthbut =Button(tab2, font=('tahoma', 15, 'bold'), text="   Length   ", padx=2, pady=2,
                bg="BLACK", fg="WHITE", command=length_window)
Lengthbut.place(x=202, y=130)
Lengthbut.bind("<Enter>", lenenter)
Lengthbut.bind("<Leave>", lenleave)

#Temperature Button Code
tempbut =Button(tab2, font=('tahoma', 15, 'bold'), text="   Temperature  ", padx=2, pady=2,
                bg="BLACK", fg="WHITE", command=temperature_window)
tempbut.place(x=175, y=200)
tempbut.bind("<Enter>", tempenter)
tempbut.bind("<Leave>", templeave)

#Weight Button Code
weightbut=Button(tab2, font=('tahoma', 15, 'bold'), text="   Weight  ", padx=2, pady=2,
                bg="BLACK", fg="WHITE", command=weight_window)
weightbut.place(x=202, y=270)
weightbut.bind("<Enter>", weightenter)
weightbut.bind("<Leave>", weightleave)




win.mainloop()
