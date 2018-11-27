import pygame as pg
import random as rnjuzus
import keyboard as key
import time
from tkinter import *
from pygame.font import *

###Function###
Play_YL3=False
Play_YL1=False
Open_info=False
Open_settings=False
softwareDisplayed=False
Stats=(0,0)
state_info_button=0
state_settings_button=0
state_yl1_button=0
state_yl3_button=0
Window=2
money=500
storeAppLit=False
gamesAppLit=False
channelName='mightypaw'
stat_timer=1
s_icon_open=False
closepos=(0,0)
Settings_open=False
pg.init()
disp=pg.display.set_mode((1900,1030))
pg.display.set_caption('YouLose 3')
clock=pg.time.Clock()
white=(200,200,200)

def MOUSE():
    global mouse_pos,click
    mouse_pos=pg.mouse.get_pos()
    click=pg.mouse.get_pressed()

def NECESSITIES():
    global mouse_pos,click,open,Stats,money
    mouse_pos=pg.mouse.get_pos()
    click=pg.mouse.get_pressed()
    if key.is_pressed('0'):
        money=money+1
        UPDATE_ALL()
    if key.is_pressed('9'):
        money=money+0.01
        UPDATE_ALL()
    if key.is_pressed('-'):
        money=money-0.01
        UPDATE_ALL()
    for event in pg.event.get():
        print(event)
        if event.type==pg.QUIT:
            open=False
            quit()
    pg.display.update()
    clock.tick(60)

def TEXT_OBJECTS(text,font):
    Text_surface=font.render(text,False,white)
    return Text_surface,Text_surface.get_rect()

def MSG_DISPLAY(text,subject,x,y):
    global med_text,Subs
    Med_text=pg.font.Font('C:\Windows\Fonts\COUR.ttf',50)
    TextSurf,TextRect=TEXT_OBJECTS(text,Med_text)
    TextRect.center=((x-120)+(len(str(subject))*15),y)
    disp.blit(TextSurf,TextRect)

def MONEY_ROUND():
    global money
    money=money*100
    money=int(money)
    money=money/100

def MOUSE_HOVER_BUTTON():
    global Window,state_info_button,state_settings_button,state_yl1_button,state_yl3_button,Play_YL3,Play_YL1,\
    Open_settings,Open_info
    if 550<mouse_pos[0]<850 and 400<mouse_pos[1]<460:
        if state_info_button == 0:
            disp.blit(info_2, (550, 400))
            state_info_button = 1
    elif state_info_button == 1 and not 550<mouse_pos[0]<850 or not 400<mouse_pos[1]<460:
            disp.blit(info_1, (550, 400))
            state_info_button = 0

    if 1050<mouse_pos[0]<1350 and 400<mouse_pos[1]<460:
        if state_settings_button == 0:
            disp.blit(settings_2, (1050, 400))
            state_settings_button = 1
    elif state_settings_button == 1 and not 1050 < mouse_pos[0] < 1350 or not 400 < mouse_pos[1] < 460:
            disp.blit(settings_1, (1050, 400))
            state_settings_button = 0

    if 550<mouse_pos[0]<850 and 560<mouse_pos[1]<620:
        if state_yl1_button == 0:
            disp.blit(YL1_2, (550, 560))
            state_yl1_button = 1
    elif state_yl1_button == 1 and not 550 < mouse_pos[0] < 850 or not 560 < mouse_pos[1] < 620:
            disp.blit(YL1_1, (550, 560))
            state_yl1_button = 0

    if 1050<mouse_pos[0]<1350 and 560<mouse_pos[1]<620:
        if state_yl3_button==0:
            disp.blit(YL3_2,(1050,560))
            state_yl3_button=1
    elif state_yl3_button==1 and not 1050<mouse_pos[0]<1350 or not 560<mouse_pos[1]<620:
        disp.blit(YL3_1,(1050,560))
        state_yl3_button=0

    if click[0]==1:
        if 1050<mouse_pos[0]<1350 and 560<mouse_pos[1]<620:   #yl3
            Play_YL3=True
            REL_ALL_YL3()
            Window=2
        elif 550<mouse_pos[0]<850 and 560<mouse_pos[1]<620:   #yl1
            Play_YL1=True
            YE_OLDE()
        elif 1050<mouse_pos[0]<1350 and 400<mouse_pos[1]<460: #settings
            Open_settings=True
        elif 550<mouse_pos[0]<850 and 400<mouse_pos[1]<460:   #info
            Open_info=True
        else:
            pass

def REL_ALL_YL3():
    BACK(0,0)
    SETTINGS_ICON_REL(947,5)
    WI2(635,20)
    WI1(325,20)
    WI0(15,20)
    WINDOW_BACKGROUND()
    UPDATE_ALL()
    if Window==0:
        URL_BOTS(1510, 20)
        WINC(330,75)
    elif Window==2:
        URL_RECORD(1510, 20)
        WINC(20,75)
        APPLICATIONS()
    else:
        URL_UPLOAD(1510,20)
        CH_PROFILE()
        WINC(640,75)

def CLICK_EVENT_CHANNEL():
    if 280<mouse_pos[0]<880 and 90<mouse_pos[1]<170 and click[0]==1:
        CH_RENAME()

def CLICK_EVENT_SOFTWARE():
    global gamesAppLit,storeAppLit,gamesApp2,storeApp2
    if 30<mouse_pos[0]<290 and 100<mouse_pos[1]<360 and gamesAppLit==False:
        disp.blit(gamesApp2,(30,100))
        gamesAppLit=True
    elif 300<mouse_pos[0]<560 and 100<mouse_pos[1]<360 and storeAppLit==False:
        disp.blit(storeApp2,(300,100))
        storeAppLit=True
    elif not 30<mouse_pos[0]<290 or not 100<mouse_pos[1]<360 and not gamesAppLit==False:
        disp.blit(gamesApp,(30,100))
        gamesAppLit=False
    elif not 300<mouse_pos[0]<560 or not 100<mouse_pos[1]<360 and not storeAppLit==False:
        disp.blit(storeApp,(300,100))
        storeAppLit=False
    else:
        pass

stat_cover=pg.image.load('money_box.png')
def STAT_COVER(x,y):
    disp.blit(stat_cover,(x,y))

def UPDATE_STATS_TIMED():
    global stat_timer,money
    stat_timer=stat_timer-1
    if stat_timer<0:
        stat_timer=5
        STAT_COVER(1510,90)
        MONEY_ROUND()
        MSG_DISPLAY('£'+str(money),money,1660,120)
        STAT_COVER(1510, 160)
        MSG_DISPLAY(u'\u25ba'+str(Stats[0]),Stats[0], 1660, 190)
        STAT_COVER(1510, 230)
        MSG_DISPLAY('V' + str(Stats[1]), Stats[1], 1660, 260)
def UPDATE_ALL():
    global stat_timer,money
    stat_timer=30
    STAT_COVER(1510,90)
    MONEY_ROUND()
    MSG_DISPLAY('£'+str(money),money, 1660, 120)
    STAT_COVER(1510,160)
    MSG_DISPLAY(u'\u25ba'+str(Stats[0]),Stats[0], 1660, 190)
    STAT_COVER(1510,230)
    MSG_DISPLAY('V' + str(Stats[1]), Stats[1], 1660, 260)

def YE_OLDE():
    Relevant=True
    root = Tk()
    DaysWait = 1
    stream = False
    rec_done = False
    spaces = ''
    spaceamount = 0
    QUALITY = 0
    Name = 'i was too lazy to name my channel :/'

    def snooze(event):
        global Creation
        # print('omg this is working')
        Creation = False
        root.destroy()

    def makevid(event):
        global Creation
        # print('omg this is working 2')
        Creation = True
        root.destroy()

    def proceed(event):
        root.destroy()

    def showname(event):
        global Name, FullName
        print('name:', (namechannel_entry.get()))
        Name = namechannel_entry.get()
        FullName = 'Logged in as: ' + Name

    def waiting(event):
        global DaysWait
        print('wait:', (howlong_entry.get()))
        DaysWait = (howlong_entry.get())
        DaysWait = int(DaysWait)
        print(DaysWait)

    def streaming(event):
        global stream
        stream = True
        root.destroy()

    def recording(event):
        global stream
        stream = False
        root.destroy()

    def stop(event):
        global spaceamount, rec_done
        if spaceamount == 5:
            wow()
        elif spaceamount == 5:
            good()
        elif spaceamount == 6 or spaceamount > 11 and spaceamount < 17:
            med()
        else:
            bad()
        rec_done = True
        root.destroy()

    def delete():
        root.destroy()

    def bad():
        global QUALITY
        QUALITY = 2

    def med():
        global QUALITY
        QUALITY = 3

    def good():
        global QUALITY
        QUALITY = 4

    def wow():
        global QUALITY
        QUALITY = 6

    #######################################################
    welcome_label = Label(root, text='Welcome 2 TwitchSim')
    Name = StringVar()
    namechannel_label = Label(root, text='Name ur channel')
    namechannel_entry = Entry(root, textvariable=Name)
    continue_button = Button(root, text='[Continue]')
    showname_button = Button(root, text='Save name')

    showname_button.bind('<Button-1>', showname)
    continue_button.bind('<Button-1>', proceed)

    showname_button.grid(row=2, sticky=W)
    welcome_label.grid(row=0, columnspan=2, sticky=W)
    namechannel_label.grid(row=1, sticky=E)
    namechannel_entry.grid(row=1, column=1)
    continue_button.grid(row=2, column=1, sticky=E)
    root.mainloop()
    print(Name)
    while Relevant == True:
        root = Tk()
        loop_button = Button(root, text='   [b lazy]    ')
        loop_button.bind('<Button-1>', snooze)

        create_button = Button(root, text='[Create content]')
        create_button.bind('<Button-1>', makevid)

        loop_button.pack(side=LEFT)
        create_button.pack(side=RIGHT)
        root.mainloop()
        if Creation == False:
            root = Tk()
            wait = IntVar()
            howlong_label = Label(root, text='wait for how long?')
            howlong_entry = Entry(root, textvariable=wait)
            continue_button2 = Button(text='[Continue]')

            enter_button = Button(root, text='Press this before continue')
            continue_button2.bind('<Button-1>', proceed)
            enter_button.bind('<Button-1>', waiting)

            enter_button.grid(row=1, sticky=W)
            continue_button2.grid(row=1, column=1, sticky=E)
            howlong_label.grid(row=0)
            howlong_entry.grid(row=0, column=1)
            root.mainloop()
            # wait=int(wait)
            while DaysWait > 0:
                time.sleep(0.5)
                print('Iterations remaining:', DaysWait)
                DaysWait = DaysWait - 1
            time.sleep(0.5)
            Creation = True
        else:
            root = Tk()
            decision_label = Label(root, text='streaming TBA')
            stream_button = Button(root, text='[Begin stream]')
            record_button = Button(root, text='[Start recording]')

            stream_button.bind('<Button-1>', streaming)
            record_button.bind('<Button-1>', recording)

            decision_label.grid(row=0, columnspan=2, sticky=W)
            stream_button.grid(row=1, sticky=W)
            record_button.grid(row=1, column=1, sticky=E)
            root.mainloop()
            if stream == True:
                print('stream feature not added yet')
                stream = False
            else:
                rec_done = False
                #root=Tk()
                text = Text(root)
                text.configure(font=("Courier new", 16, "bold"))
                while rec_done == False:
                    root = Tk()
                    if spaceamount < 20:
                        spaces = spaces + '_'
                        spaceamount = spaceamount + 1
                    else:
                        spaces = ''
                        spaceamount = 0
                    arrow = spaces + '^'
                    nameL = Label(root, text=FullName)
                    recL = Label(root, text='now recording.stop arrow under heavier shade for higher quality.')
                    barL = Label(root, text=' ░░░░█▒░░░░░▒▒▒▒▒▓░▓░')
                    arrowL = Label(root, text=arrow)
                    stopB = Button(root, text='[stop]')

                    stopB.bind('<Button-1>', stop)
                    nameL.grid(row=2, column=1, sticky=E)
                    recL.grid(row=0, columnspan=2)
                    barL.grid(row=1, sticky=W)
                    arrowL.grid(row=2, sticky=W)
                    stopB.grid(row=1, column=1, sticky=W)
                    root.after(500,lambda:root.destroy())
                    root.mainloop()

def CLICK_EVENT_WINDOW():
    WI0(15, 20)
    WI1(325, 20)
    WI2(635, 20)

def CH_RENAME():
    global channelName,entry666,root5
    def getName(event):
        global channelName, entry666, root5
        channelName = entry666.get()
        root5.destroy()
    print('tk not work dud')
    root5=Tk()
    label=Label(root5,text='Rename your channel:')
    entry666=Entry(root5,textvariable=channelName)
    button=Button(root5,text='OK')
    button.bind('<Button-1>',getName)
    label.pack(side=LEFT)
    entry666.pack()
    button.pack(side=RIGHT)
    root5.mainloop()
    MSG_DISPLAY(channelName,channelName,610,125)
    REL_CHANNEL()

def SETTINGS_BUTTONS():
    global Play_YL1,Play_YL3,Open_settings,Open_info,Settings_open
    if 1550<mouse_pos[0]<1850 and 960<mouse_pos[1]<1040 and click[0]==1 and Open_settings==True:
        Play_YL3=False
        Open_settings=False
        Settings_open=False
        REL_ALL_START()

def REL_CHANNEL():
    CH_PROFILE()
    MSG_DISPLAY(channelName, channelName, 610, 125)

#def REL_RECORD():


#def REL_BOTS():


def BUTTON_WINDOW():
    global Window, Settings_open,s_icon_open,Open_settings
    if mouse_pos[1]<80 and Play_YL3==True:
        if 15<mouse_pos[0]<315 and 20<mouse_pos[1]<80 and click[0]==1:
            CLICK_EVENT_WINDOW()
            URL_RECORD(1510,20)
            WINC(20,75)
            WINDOW_BACKGROUND()
            APPLICATIONS()
            Window=2
            #software

        elif 325<mouse_pos[0]<625 and 20<mouse_pos[1]<80 and click[0]==1:
            CLICK_EVENT_WINDOW()
            URL_UPLOAD(1510,20)
            WINC(330,75)
            WINDOW_BACKGROUND()
            REL_CHANNEL()
            Window=1
            #channel

        elif 635<mouse_pos[0]<945 and 20<mouse_pos[1]<80 and click[0]==1:
            CLICK_EVENT_WINDOW()
            URL_BOTS(1510,20)
            WINC(640,75)
            WINDOW_BACKGROUND()
            #REL_BOTS()
            Window=0
            #bots

        elif 947<mouse_pos[0]<1017 and 5<mouse_pos[1]<75:
            if s_icon_open == False:
                SETTINGS_ICON_2(947, 5)
                s_icon_open=True
            elif click[0]==1 and Settings_open==False:
                Settings_open=True
                Open_settings=True
                SETTINGS_P(0,0)
                X_BUTTON(1840, 10)
                if 947<mouse_pos[0]<1017 and 5<mouse_pos[1]<75:
                    if not s_icon_open==True:
                        SETTINGS_ICON_2(947,5)
                        s_icon_open=True
                    else:
                        pass
                else:
                    pass
        elif s_icon_open==True and not 947<mouse_pos[0]<1017 or not 5<mouse_pos[1]<75:
            SETTINGS_ICON_REL(947,5)
            s_icon_open=False
        elif 1840<mouse_pos[0]<1900 and 10<mouse_pos[1]<70\
                and click[0]==1 and Settings_open==True:
            REL_ALL_YL3()
            s_icon_open=False
            Settings_open=False
            Open_settings=False

###Graphics###
bg=pg.image.load('YL3back.png')
def BACK(bX,bY):
    disp.blit(bg,(bX,bY))

xout=pg.image.load('x-out.png')
def X_BUTTON(x,y):
    disp.blit(xout,(x,y))

exit_yl3=pg.image.load('Exit_yl3.png')
settings_pg=pg.image.load('yl-settings-0.png')
def SETTINGS_P(x,y):
    disp.blit(settings_pg,(x,y))
    disp.blit(exit_yl3, (1550, 960))

W0=pg.image.load('softwareWindow.png')
def WI0(w0x,w0y):
    disp.blit(W0,(w0x,w0y))
W1=pg.image.load('channel window.png')
def WI1(w1x,w1y):
    disp.blit(W1,(w1x,w1y))
W2=pg.image.load('bots window.png')
def WI2(w2x,w2y):
    disp.blit(W2,(w2x,w2y))

Settings_icon_opened=pg.image.load('YL-settings-selected.png')
Settings_icon=pg.image.load('YL-settings-default.png')
def SETTINGS_ICON_REL(x,y):
    disp.blit(Settings_icon,(x,y))
def SETTINGS_ICON_2(x,y):
    disp.blit(Settings_icon_opened,(x,y))

wc=pg.image.load('windowcover.png')
def WINC(wcx,wcy):
    disp.blit(wc,(wcx,wcy))

wb=pg.image.load('windowBackgroundv3.png')
def WINDOW_BACKGROUND():
    disp.blit(wb,(0,80))

nb=pg.image.load('ch_name_box.png')
img123=pg.image.load('123.png')
donate_img=pg.image.load('donate.png')
merch_img=pg.image.load('merch.png')
def CH_PROFILE():
    disp.blit(nb,(280,90))
    disp.blit(img123,(10,90))
    disp.blit(donate_img,(280,180))
    disp.blit(merch_img,(590,180))

gamesApp=pg.image.load('gamesApplication.png')
gamesApp2=pg.image.load('gamesApplication2.png')
storeApp=pg.image.load('storeApplication.png')
storeApp2=pg.image.load('storeApplication2.png')
def APPLICATIONS():
    disp.blit(gamesApp,(30,100))
    disp.blit(storeApp,(300,100))

def REL_ALL_START():
    global info_1,info_2,settings_1,settings_2,YL1_1,YL1_2,YL3_1,YL3_2,start_bg
    start_bg=pg.image.load('bad background.png')
    logo=pg.image.load('YouLose logo.png')
    info_1=pg.image.load('INFO_button.png')
    info_2=pg.image.load('INFO_button_1.png')
    settings_1=pg.image.load('SETTINGS_button.png')
    settings_2=pg.image.load('SETTINGS_button_1.png')
    YL1_1=pg.image.load('YL1_button.png')
    YL1_2=pg.image.load('YL1_button_1.png')
    YL3_1=pg.image.load('YL3_button.png')
    YL3_2=pg.image.load('YL3_button_1.png')

    disp.blit(start_bg,(0,0))
    disp.blit(logo,(862,100))
    disp.blit(info_1,(550,400))
    disp.blit(settings_1,(1050,400))
    disp.blit(YL1_1,(550,560))
    disp.blit(YL3_1,(1050,560))

url_record=pg.image.load('url-record.png')
def URL_RECORD(x,y):
    disp.blit(url_record,(x,y))
url_upload=pg.image.load('url-upload.png')
def URL_UPLOAD(x,y):
    disp.blit(url_upload,(x,y))
url_bots=pg.image.load('url-bots.png')
def URL_BOTS(x,y):
    disp.blit(url_bots,(x,y))

winCx=25
winCy=75

open=True
REL_ALL_START()
while open:
    NECESSITIES()
    MOUSE_HOVER_BUTTON()
    while Play_YL3==True:
        BUTTON_WINDOW()
        NECESSITIES()
        UPDATE_STATS_TIMED()
        if Settings_open:
            SETTINGS_BUTTONS()
        elif Window==0:
            pass
        elif Window==1:
            CLICK_EVENT_CHANNEL()
        elif Window==2:
            CLICK_EVENT_SOFTWARE()
    if Play_YL1==True:
        YE_OLDE()