import pygame as pg
import random as rnd
import keyboard as key
import time

###Function###
Window=0
s_icon_open=False
closepos=(0,0)
Settings_open=False
pg.init()
disp=pg.display.set_mode((1900,1030))
pg.display.set_caption('YouLose 3')
clock=pg.time.Clock()
white=(200,200,200)

def CLICK_EVENT_WINDOW():
    WI0(15, 20)
    WI1(325, 20)
    WI2(635, 20)
#bots
def BUTTON_WINDOW():
    global window, Settings_open,s_icon_open
    if mouse_pos[1]<80:
        if 15<mouse_pos[0]<315 and 20<mouse_pos[1]<80 and click[0]==1:
            CLICK_EVENT_WINDOW()
            URL_RECORD(1510,20)
            WINC(20,75)
            window=0
        elif 325<mouse_pos[0]<625 and 20<mouse_pos[1]<80 and click[0]==1:
            CLICK_EVENT_WINDOW()
            URL_UPLOAD(1510,20)
            WINC(330,75)
            window=1
        elif 635<mouse_pos[0]<945 and 20<mouse_pos[1]<80 and click[0]==1:
            CLICK_EVENT_WINDOW()
            URL_BOTS(1510,20)
            WINC(640,75)
            window=2

        elif 947<mouse_pos[0]<1017 and 5<mouse_pos[1]<75:
            if s_icon_open == False:
                SETTINGS_ICON_2(947, 5)
                s_icon_open=True
            elif click[0]==1 and Settings_open==False:
                Settings_open=True
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
        elif s_icon_open==True and not 947<mouse_pos[0]<1017 and 5<mouse_pos[1]<75:
            SETTINGS_ICON_REL(947,5)
            s_icon_open=False
        elif 1840<mouse_pos[0]<1900 and 10<mouse_pos[1]<70\
                and click[0]==1 and Settings_open==True:
            REL_ALL()
            s_icon_open=False
            Settings_open=False
        else:
            pass

###Graphics###
bg=pg.image.load('YL3back2.png')
def BACK(bX,bY):
    disp.blit(bg,(bX,bY))

xout=pg.image.load('x-out.png')
def X_BUTTON(x,y):
    disp.blit(xout,(x,y))

settings_pg=pg.image.load('yl-settings-0.png')
def SETTINGS_P(x,y):
    disp.blit(settings_pg,(x,y))

W0=pg.image.load('record window.png')
def WI0(w0x,w0y):
    disp.blit(W0,(w0x,w0y))
W1=pg.image.load('upload window.png')
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

def REL_ALL():
    BACK(0,0)
    SETTINGS_ICON_REL(947,5)
    WI2(635,20)
    WI1(325,20)
    WI0(15,20)
    if Window==0:
        URL_BOTS(1510, 20)
    elif Window==1:
        URL_RECORD(1510, 20)
    else:
        URL_UPLOAD(1510, 20)

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
BACK(0,0)
WI0(15,20)
WI1(325,20)
WI2(635,20)
WINC(winCx,winCy)
SETTINGS_ICON_REL(947,5)
while open:
    mouse_pos=pg.mouse.get_pos()
    click=pg.mouse.get_pressed()
    BUTTON_WINDOW()
    for event in pg.event.get():
        print(event)
        if event.type==pg.QUIT:
            open=False
    pg.display.update()
    clock.tick(60)
