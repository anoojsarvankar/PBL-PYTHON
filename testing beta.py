import random
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from pygame import mixer
from PIL import ImageTk, Image
#Creating GUI
from pygame.event import wait

root = Tk()
Questionans__window_width=1000
Questionans__window_height=700
Screen_width=root.winfo_screenwidth()
Screen_height=root.winfo_screenheight()
x=(Screen_width/2)-(Questionans__window_width/2)
y=(Screen_height/2)-(Questionans__window_height/2)
root.geometry("%dx%d+%d+%d"%(Questionans__window_width,Questionans__window_height,x,y))
root.resizable(width=FALSE,height=FALSE)
mixer.init()

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
            'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
            'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
            'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
            'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
            'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
            'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
            'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
            'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
            'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
            'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
            'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
            'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
            'indian red', 'saddle brown', 'sandy brown',
            'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
            'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
            'pale violet red', 'maroon', 'medium violet red', 'violet red',
            'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
            'thistle', 'snow2', 'snow3',
            'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
            'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
            'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
            'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
            'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
            'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
            'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
            'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
            'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
            'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
            'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
            'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
            'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
            'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
            'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
            'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
            'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
            'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
            'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
            'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
            'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
            'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
            'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
            'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
            'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
            'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
            'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
            'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
            'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
            'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
            'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
            'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
            'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
            'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
            'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
            'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
            'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
            'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
            'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
            'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
            'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
            'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
            'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
            'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
            'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
            'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
            'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
            'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
            'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
            'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
            'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
            'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
            'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
            'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
            'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
            'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
            'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

root.config(bg=COLORS[346])
# creation done
img = ImageTk.PhotoImage(Image.open("AMT_question.jpg"))
image = Label(root, image=img, width=316, height=317)
image.image = img
image.place(x=0, y=0)

frame1 = Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=320, height=600,
               bd=0)
frame1.place_configure(x=0, y=398)

l1 = Label(frame1, text='1. 25,000 ₹', bg='green', relief="groove", fg='White', width=28,
          font=('Tempus Sans ITC', 14))
l1.pack(side=TOP, fill=BOTH)
l2 = Label(frame1, text='2. 50,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l2.pack(side=TOP, expand=YES, fill=BOTH)
l3 = Label(frame1, text='3. 1,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l3.pack(side=TOP, expand=YES, fill=BOTH)
l4 = Label(frame1, text='4.  5,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l4.pack(side=TOP, expand=YES, fill=BOTH)
l5 = Label(frame1, text='5.  10,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l5.pack(side=TOP, expand=YES, fill=BOTH)
l6 = Label(frame1, text='6. 20,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l6.pack(side=TOP, expand=YES, fill=BOTH)
l7 = Label(frame1, text='7. 30,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l7.pack(side=TOP, expand=YES, fill=BOTH)
l8 = Label(frame1, text='8. 40,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l8.pack(side=TOP, expand=YES, fill=BOTH)
l9 = Label(frame1, text='9. 50,00,000 ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l9.pack(side=TOP, expand=YES, fill=BOTH)
l10 = Label(frame1, text='10. 1 CRORE ₹', bg=COLORS[305], relief="groove", fg='White', font=('Tempus Sans ITC', 14))
l10.pack(side=TOP, expand=YES, fill=BOTH)




def stop(z):
     mixer.music.stop()

def set_vol(val):
     volume = int(val)/100
     mixer.music.set_volume(volume)

scale = Scale(root, orient=HORIZONTAL, command=set_vol, bg=COLORS[74], fg='black')

scale.set(50)
scale.place(x=80, y=330)
#Buttons and question label
r1 = Button(root,bg='RoyalBlue1', fg='black', width=20, font=('Tempus Sans ITC', 14))
r1.place_configure(x=350, y=300)
r2 = Button(root,bg='RoyalBlue1', fg='black', width=20, font=('Tempus Sans ITC', 14))
r2.place_configure(x=700, y=300)
r3 = Button(root,bg='RoyalBlue1', fg='black', width=20, font=('Tempus Sans ITC', 14))
r3.place_configure(x=350, y=350)
r4 = Button(root,bg='RoyalBlue1',fg='black', width=20, font=('Tempus Sans ITC', 14))
r4.place_configure(x=700, y=350)
quest = Label(root,bg='RoyalBlue1', width=40, height=2)
quest.place_configure(x=400, y=200)

#For 5050lifeline
lifq=0
used=0
def Lifeline5050():
    tempx=-1
    global used
    if(used==1):
        messagebox.showerror('Sorry','No more attempts left!')
        return
    for i in range(0,2):
        temp=random.randint(1,4)
        while(str(temp)==resultset[lifq][5] or tempx==temp):
            temp=random.randint(1,4)
        if(temp==1):
            r1.configure(text="")
        if (temp == 2):
            r2.configure(text="")
        if (temp == 3):
            r3.configure(text="")
        if (temp == 4):
            r4.configure(text="")
        tempx=temp
        used=1

    rl1.configure(bg='Red')
rl1=Button(root,text="50:50",bg='RoyalBlue1',fg='black', width=20, font=('Tempus Sans ITC', 14),command=lambda: Lifeline5050())
rl1.place_configure(x=700,y=100)

#For QChange lifeline
qcused=0
def LifelineQchange():
    global lifq,qcused,qstnno
    if(qcused==1):
        messagebox.showerror('Sorry','Already used this lifeline!\n')
        return
    rl2.configure(bg='Red')
    qcused = 1
    messagebox.showinfo('Informational', '\nCorrect answer is: ' + resultset[lifq][int(resultset[lifq][5])])
    var.set(1)

rl2 = Button(root, text="Qstn Change", bg='RoyalBlue1', fg='black', width=20, font=('Tempus Sans ITC', 14),command=lambda: LifelineQchange())
rl2.place_configure(x=400, y=100)


#For Expert Advice
eaused=0
def LifelineExpadv():
    global lifq,eaused
    if(eaused==1):
        messagebox.showerror('Sorry','Already used this lifeline!\n')
        return
    rl3.configure(bg='Red')
    eaused=1
    if random.random() < 0.65:
        messagebox.showinfo('Hello User!','In my opinion:\nAnswer should probably be ' + resultset[lifq][int(resultset[lifq][5])])
    else:
        temp=random.randint(1,4)
        messagebox.showinfo('Hello User!','In my opinion:\nAnswer should probably be ' + resultset[lifq][temp])
rl3 = Button(root, text="Expert Advice!", bg='RoyalBlue1', fg='black', width=20, font=('Tempus Sans ITC', 14),command=lambda: LifelineExpadv())
rl3.place_configure(x=550, y=60)


var = tkinter.IntVar()
def AnswerCheck(temp1,selection):
    if(resultset[temp1][5]==str(selection)):
        global qstnno
        qstnno+=1
        print(qstnno)
        global lifq
        lifq=temp1
    else:
        messagebox.showinfo('Sorry','Wrong Answer\nCorrect answer was: '+resultset[temp1][int(resultset[temp1][5])])
        exit()
    var.set(1)

def QuestUI(temp1):
    # IMPORTANT! QSTN OBJECT HERE!
    quest.config(text=resultset[temp1][0], fg='White', font=('Tempus Sans ITC', 14))
    r1.configure(text=resultset[temp1][1],command=lambda: AnswerCheck(temp1, 1))
    r2.configure(text=resultset[temp1][2],command=lambda: AnswerCheck(temp1, 2))
    r3.configure(text=resultset[temp1][3],command=lambda: AnswerCheck(temp1, 3))
    r4.configure(text=resultset[temp1][4],command=lambda: AnswerCheck(temp1, 4))
    root.wait_variable(var)

resultset=[]
splitlines=[]
num_lines=0
def OpenDB(level):
    global resultset
    global num_lines
    if(level==1):
        file=open('QuestionDB1.txt','r')
        f=file.read()
        temp=f.split('\n')
        num_lines=len(temp)
        file.close()
        for i in temp:
            resultset.append(i.split('='))
    elif(level==2):
        file = open('QuestionDB2.txt', 'r')
        f = file.read()
        temp = f.split('\n')
        num_lines = len(temp)
        file.close()
        for i in temp:
            resultset.append(i.split('='))
    elif(level==3):
        file = open('QuestionDB3.txt', 'r')
        f = file.read()
        temp = f.split('\n')
        num_lines = len(temp)
        file.close()
        for i in temp:
            resultset.append(i.split('='))

repeatcheck = [-1]
def Checkrepeat(temp):
    global repeatcheck
    for i in repeatcheck:
        if(i==temp):
            return(0)
    else:
        repeatcheck=repeatcheck+[temp]
        return(1)
repeated=0
def QstnChooser():
    global repeated
    global num_lines
    temp1=random.randint(0,num_lines-1)
    if(Checkrepeat(temp1)==1):
        repeated = 0
        qstnnodb=temp1
        QuestUI(qstnnodb)
    else:
        repeated=1
qstnno=1
while(qstnno<=10):
    if(qstnno<4):
        OpenDB(1)
        if(qstnno==2):
            l1.configure(bg='green yellow')
            l2.configure(bg='green')
        if (qstnno == 3):
            l2.configure(bg='green yellow')
            l3.configure(bg='green')

        #Questionnaire Begins
        if(repeated==1):
            while(repeated!=0):
                QstnChooser()
        elif(repeated==0):
            QstnChooser()
    if(qstnno==4):
        repeatcheck.clear()
        repeatcheck+=[-1]

    if (qstnno > 3 and qstnno < 7):
        resultset.clear()
        OpenDB(2)
        if (qstnno == 4):
            l3.configure(bg='green yellow')
            l4.configure(bg='green')
        if (qstnno == 5):
            l4.configure(bg='green yellow')
            l5.configure(bg='green')
        if (qstnno == 6):
            l5.configure(bg='green yellow')
            l6.configure(bg='green')
        #Questionnaire begins
        QstnChooser()
        if (repeated == 1):
            while (repeated != 0):
                QstnChooser()
    if (qstnno == 7):
        repeatcheck.clear()
        repeatcheck += [-1]
    if (qstnno > 6 and qstnno <= 10):
        resultset.clear()
        OpenDB(3)
        if (qstnno == 7):
            l6.configure(bg='green yellow')
            l7.configure(bg='green')
        if (qstnno == 8):
            l7.configure(bg='green yellow')
            l8.configure(bg='green')
        if (qstnno == 9):
            l8.configure(bg='green yellow')
            l9.configure(bg='green')
        if (qstnno == 10):
            l9.configure(bg='green yellow')
            l10.configure(bg='green')
        QstnChooser()
        if (repeated == 1):
            while (repeated != 0):
                QstnChooser()
else:
    messagebox.showinfo('YEAHH','WINNER WINNER CHICKEN DINNER!')
root.mainloop()