import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.Qt import QApplication, QWidget, QThread
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

wh0=[1000,600]
wh1_1=[1000,600]
wh1_2=[1000,600]
wh1_3=[1000,600]
wh2_1=[1000,600]
wh2_2=[1000,600]
wh2_3=[1000,600]
wh3_1=[1000,600]
wh3_2=[1000,600]
wh3_3=[1000,600]
whl=[1000,600]
s = ''
flag = 0
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.binary_location = path
browser = webdriver.Chrome(options=options)
def death():
    global browser
    global my_thread
    my_thread.terminate()
    time.sleep(0.5)
    browser.close()
    f.close()
    browser=webdriver.Chrome(options=options)
    s=''
def pause():
    button = browser.find_element(By.TAG_NAME, 'svg')
    button.click()

def listadd1():
    songlist=w4_1.selector1.text()
    # print(songlist)
    f = open(songlist + '.txt', 'a')
    # print(text)
    f.write(browser.current_url + ' ' + text + '\n')
    f.close()
def listadd2():
    songlist=w4_2.selector1.text()
    # print(songlist)
    f = open(songlist + '.txt', 'a')
    # print(text)
    f.write(browser.current_url + ' ' + text + '\n')
    f.close()

def listadd3():
    songlist=w4_3.selector1.text()
    # print(songlist)
    f = open(songlist + '.txt', 'a')
    # print(text)
    f.write(browser.current_url + ' ' + text + '\n')
    f.close()

def over():
    global browser
    global s
    browser.close()
    browser = webdriver.Chrome(options=options)
    s=''
def spider_hifini():
    global s
    global sn
    s=''
    url = 'https://www.hifini.com/search.htm'
    get = browser.get(url)
    time.sleep(0.5)
    input = browser.find_element(By.TAG_NAME, 'input')
    name=w2_1.songname.text()
    singer=w2_1.singername.text()
    input.send_keys(name+' '+singer)
    buttons=browser.find_elements(By.TAG_NAME,'button')
    button=buttons[1]
    button.click()
    time.sleep(0.5)
    songss = browser.find_elements(By.CLASS_NAME, 'subject.break-all')
    arr=[]
    s3=''
    for i in range(min(10,len(songss))):
        song = songss[i].find_element(By.TAG_NAME, 'a')
        s3+=(str(i+1)+'.'+song.text+'\n')
    arr=[s3,songss]
    s=s3
    sn=songss
    return arr

def listen_hifini():
    global text
    num=int(w3_1.selector1.text())
    songs=sn
    listen=songs[num-1].find_element(By.TAG_NAME,'a')
    text = listen.text
    # print('即将播放:'+text+'\n')
    listen.click()
    time.sleep(0.5)
    sing = browser.find_element(By.TAG_NAME, 'svg')
    sing.click()

def spider_fangpi():
    global s
    global sn
    s=''
    url = 'https://www.fangpi.net/'
    get = browser.get(url)
    time.sleep(0.5)
    name=w2_2.songname.text()
    singer=w2_2.singername.text()
    inputs = browser.find_element(By.ID, 's-input')
    inputs.send_keys(name + ' ' + singer)
    butt = browser.find_element(By.ID, 's-btn')
    butt.click()
    time.sleep(0.5)
    songname = browser.find_elements(By.CLASS_NAME, "text-primary.font-weight-bold")
    singername = browser.find_elements(By.CLASS_NAME, "text-success.col-4.col-content")
    for i in range(min(10,len(songname))):
        s+=(str(i+1)+'.'+songname[i].text+' '+singername[i].text+'\n')
    # print(s)
    arr=[s,songname]
    sn = songname
    return arr

def listen_fangpi():
    global text
    songs=sn
    num=int(w3_2.selector1.text())
    text=songs[num-1].text
    songs[num-1].click()
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    time.sleep(0.5)
    # print('即将播放:' + text + '\n')
    temporary1 = browser.find_element(By.CLASS_NAME, "aplayer-button.aplayer-play")
    plays = browser.find_element(By.TAG_NAME, "path")
    plays.click()
    return text

def spider_yinyuelingfeng():
    global s
    global sn
    s=''
    url = 'https://www.yeyulingfeng.com/tools/music/'
    get = browser.get(url)
    name=w2_3.songname.text()
    singer=w2_3.singername.text()
    time.sleep(0.5)
    inputs = browser.find_element(By.TAG_NAME, 'input')
    inputs.send_keys(name + ' ' + singer)
    butt = browser.find_element(By.ID, 'j-submit')
    butt.click()
    time.sleep(0.5)

    plays = browser.find_elements(By.CLASS_NAME, "aplayer-list-title")
    songname = browser.find_elements(By.CLASS_NAME, "aplayer-list-title")
    singername = browser.find_elements(By.CLASS_NAME, "aplayer-list-author")
    for i in range(min(10,len(songname))):
        s += (str(i + 1) + '.' + songname[i].text + ' ' + singername[i].text + '\n')
    arr = [s, songname]
    sn = songname
    button = browser.find_element(By.TAG_NAME, 'svg')
    button.click()
    return arr

def listen_yinyuelingfeng():
    global text
    songs = sn
    num = int(w3_3.selector1.text())
    songs[num-1].click()
    text = songs[num - 1].text
    return songs[num-1].text


class MyThread2(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        lst=[]
        while (1):
            global f
            listname=wl.selector1.text()
            f = open(listname + '.txt', 'r')
            songs = f.readlines()
            i = random.randint(0, len(songs) - 1)
            flag=0
            for e in lst:
                if(i==e):
                    flag=1
            if(flag==0):
                lst.append(i)
                url = ''
                for p in songs[i]:
                    if (p == ' '):
                        break
                    else:
                        url += p
                songname = songs[i].replace(url, '', 1)
                get = browser.get(url)
                time.sleep(0.5)
                # print('即将播放' + songname)
                # print('是否切歌y/s')
                # cut=input()
                # if(cut=='y'):
                #     continue
                button = browser.find_element(By.TAG_NAME, 'svg')
                button.click()
                time.sleep(0.5)
                flag=0
                while (1):
                    flag+=1
                    time.sleep(0.2)
                    ptime = browser.find_element(By.CLASS_NAME, 'aplayer-ptime').text
                    dtime = browser.find_element(By.CLASS_NAME, 'aplayer-dtime').text
                    # print(dtime)
                    # print(ptime + ' ' + dtime)
                    if (ptime == dtime or (flag>8 and (ptime=='00:00' or ptime=='00:01' or ptime=='00:02'))):
                        button = browser.find_element(By.TAG_NAME, 'svg')
                        button.click()
                        break

class MyThread1(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        global f
        while (1):
            listname=wl.selector1.text()
            f = open(listname + '.txt', 'r')
            songs = f.readlines()
            for i in range(len(songs)):
                url = ''
                for p in songs[i]:
                    if (p == ' '):
                        break
                    else:
                        url += p
                songname = songs[i].replace(url, '', 1)
                get = browser.get(url)
                time.sleep(0.5)
                # print('即将播放' + songname)
                button = browser.find_element(By.TAG_NAME, 'svg')
                button.click()
                time.sleep(0.5)
                while (1):
                    time.sleep(0.2)
                    ptime = browser.find_element(By.CLASS_NAME, 'aplayer-ptime').text
                    dtime = browser.find_element(By.CLASS_NAME, 'aplayer-dtime').text
                    # print(ptime+' '+dtime)
                    # print(dtime)
                    if (ptime == dtime or (flag>8 and (ptime=='00:00' or ptime=='00:01' or ptime=='00:02'))):
                        button = browser.find_element(By.TAG_NAME, 'svg')
                        button.click()
                        break
class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000, 600)
        self.setWindowTitle("听歌软件")
        #bg
        # palette = QPalette()
        # pix=QPixmap("./bg0.png")

        # pix = pix.scaled(self.width(),self.height())

        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)
        #bg/
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg0.png')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/#bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg0.png')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/

        self.btn_path1 = QPushButton("线路1", self)
        self.btn_path1.setParent(self)

        self.btn_path2 = QPushButton("线路2", self)
        self.btn_path2.setParent(self)

        self.btn_path3 = QPushButton("线路3", self)
        self.btn_path3.setParent(self)


        self.btn_list = QPushButton("进入我的歌单", self)
        self.btn_list.setParent(self)

        self.btn_path1.setMinimumSize(200, 50)
        self.btn_path1.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        self.btn_path2.setMinimumSize(200, 50)
        # self.btn_path2.setGeometry(QtCore.QRect(700, 300, 200, 50))
        self.btn_path2.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        self.btn_path3.setMinimumSize(200, 50)
        # self.btn_path3.setGeometry(QtCore.QRect(700, 370, 200, 50))
        self.btn_path3.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')

        self.btn_list.setMinimumSize(200, 50)
        # self.btn_list.setGeometry(QtCore.QRect(700, 440, 200, 50))
        self.btn_list.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')

        #响应式布局
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(8)
        container.addLayout(ButtLayout)
        container.addStretch(1)

        ButtLayout.addStretch(20)
        ButtLayout.addWidget(self.btn_path1)
        
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_path2)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_path3)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_list)
        ButtLayout.addStretch(8)
        self.setLayout(container)

        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh0
        if((wh2[0]-wh0[0]>0)or(wh2[1]-wh0[1]>0)):
            wh0=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh0[0]),int(wh0[1]))
        elif((wh2[0]-wh0[0]<0)or(wh2[1]-wh0[1]<0)):
            wh0=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh0[0]),int(wh0[1]))

    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

        
class NewWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('线路1')
        self.resize(1000,600)
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg1-1.jpg')

        self.fcku(self.pil_image)
        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/

        self.songname=QLineEdit()
        self.songname.setPlaceholderText("请输入歌曲名")
        self.songname.setParent(self)

        self.singername=QLineEdit()
        self.singername.setPlaceholderText("请输入歌手名")
        self.singername.setParent(self)

        self.btn_search=QPushButton("搜索")
        self.btn_search.setParent(self)

        
        self.btn_back=QPushButton("返回首页")
        self.btn_back.setParent(self)

        #设置按钮位置(x,y,width,height)
        
        #设置按钮圆角
        self.songname.setMinimumSize(300, 40)
        self.songname.setMaximumSize(300, 40)
        self.singername.setMinimumSize(300, 40)
        self.singername.setMaximumSize(300, 40)
        self.btn_search.setMinimumSize(200, 50)
        self.btn_search.setMaximumSize(200, 50)
        self.btn_search.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        self.btn_back.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(200, 50)
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        #响应式
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(8)
        container.addLayout(ButtLayout)
        container.addStretch(1)
        
        ButtLayout.addStretch(4)
        ButtLayout.addWidget(self.songname)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.singername)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_search)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_back)
        ButtLayout.addStretch(10)
        self.setLayout(container)
        #响应式/
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh1_1
        if((wh2[0]-wh1_1[0]>0)or(wh2[1]-wh1_1[1]>0)):
            wh1_1=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh1_1[0]),int(wh1_1[1]))
        elif((wh2[0]-wh1_1[0]<0)or(wh2[1]-wh1_1[1]<0)):
            wh1_1=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh1_1[0]),int(wh1_1[1]))
    
    def fcku(self,fckimage):
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)
    def refresh(self):
        w3_1.label_1.setText(s)

class SelectWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('select')
        self.resize(1000, 600)

        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg1-2.jpg')

        self.fcku(self.pil_image)

        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        #self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/

        self.label_1 = QLabel(s, self)
        QApplication.processEvents()
        self.label_1.repaint()
        self.label_1.setObjectName("label_1")
        self.label_1.setWordWrap(True)
        # self.label_1.setText(name_quanju[0] + "\n" + "消费成功")

        self.selector1 = QLineEdit()
        
        self.selector1.setPlaceholderText("请输入您选择的歌曲编号")
        self.selector1.setParent(self)

        self.btn_yes = QPushButton("确认")
        self.btn_yes.setParent(self)

        

        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)

        self.label_1.setStyleSheet("QLabel{color:rgb(14,255,255);font-size:25px;font-weight:normal;font-family:Arial;}")

        self.label_1.setMinimumSize(400, 500)
        self.label_1.setMaximumSize(550, 650)
        self.selector1.setMinimumSize(250, 50)
        self.selector1.setMaximumSize(300, 60)
        self.btn_yes.setMinimumSize(150, 40)
        self.btn_yes.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(150, 40)
        self.btn_back.setMaximumSize(200, 50)
        #self.label_1.setGeometry(QtCore.QRect(20, 20, 400, 500))#x,y,w,h
        #self.selector1.setGeometry(QtCore.QRect(20,450,250,50))
        #self.btn_yes.setGeometry(QtCore.QRect(700, 430, 150, 40))
        self.btn_yes.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')
        container = QHBoxLayout()

        # -----创建第1个组，添加多个组件-----
        # hobby 主要是保证他们是一个组。
        hobby_box = QGroupBox()
        # v_layout 保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        
        # 添加到v_layout中
        v_layout.addStretch(1)
        v_layout.addWidget(self.label_1)
        v_layout.addStretch(1)
        v_layout.addWidget(self.selector1)
        v_layout.addStretch(1)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # -----创建第2个组，添加多个组件-----
        # 性别组
        gender_box = QGroupBox()
        # 性别容器
        v1_layout = QVBoxLayout()
        # 性别选项
        
        # 追加到性别容器中
        v1_layout.addStretch(10)
        v1_layout.addWidget(self.btn_yes)
        v1_layout.addStretch(1)
        v1_layout.addWidget(self.btn_back)
        v1_layout.addStretch(3)
        # 添加到 box中
        gender_box.setLayout(v1_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh1_2
        if((wh2[0]-wh1_2[0]>0)or(wh2[1]-wh1_2[1]>0)):
            wh1_2=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh1_2[0]),int(wh1_2[1]))
        elif((wh2[0]-wh1_2[0]<0)or(wh2[1]-wh1_2[1]<0)):
            wh1_2=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh1_2[0]),int(wh1_2[1]))
    
    def fcku(self,fckimage):
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        

        pixmap = QPixmap.fromImage(pil_image)
        
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
       

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

class ListenWindow(QWidget):
    def __init__(self):
        super().__init__()
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg1-3.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/
        
        self.setWindowTitle('listen')
        self.resize(1000,600)
        
        self.btn_yes=QPushButton("播放/暂停")
        self.btn_yes.setParent(self)

        self.selector1=QLineEdit()
        self.selector1.setPlaceholderText("您需要加入到的歌单名")
        self.selector1.setParent(self)
        
        self.btn_list=QPushButton("加入歌单")
        self.btn_list.setParent(self)
        
        self.btn_back=QPushButton("返回首页")
        self.btn_back.setParent(self)

        self.btn_yes.setGeometry(QtCore.QRect(700, 360, 150, 40))
        self.btn_yes.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')

        self.selector1.setGeometry(QtCore.QRect(700,290,250,50))

        self.btn_list.setGeometry(QtCore.QRect(700, 430, 150, 40))
        self.btn_list.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        
        self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh1_3
        if((wh2[0]-wh1_3[0]>0)or(wh2[1]-wh1_3[1]>0)):
            wh1_3=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh1_3[0]),int(wh1_3[1]))
        elif((wh2[0]-wh1_3[0]<0)or(wh2[1]-wh1_3[1]<0)):
            wh1_3=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh1_3[0]),int(wh1_3[1]))
    
    def fcku(self,fckimage):
        pil_image = self.m_resize(self.width(), self.height(), fckimage)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)


class informWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('成功')
        self.setFixedSize(600, 200)
        self.label_1 = QLabel('加入成功！',self)
        self.label_1.setGeometry(QtCore.QRect(240, 20, 200, 60))#x,y,w,h
        self.label_1.setObjectName("label_1")
        self.label_1.setWordWrap(True)
        self.label_1.setParent(self)

        self.btn_yes = QPushButton("确定")
        self.btn_yes.setParent(self)
        self.btn_yes.setGeometry(QtCore.QRect(240, 100, 100, 60))  # x,y,w,h
        self.label_1.setStyleSheet("QLabel{color:rgb(1,1,1);font-size:30px;font-weight:normal;font-family:Arial;}")
# 2

class NewWindow2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('线路2')
        self.resize(1000, 600)

        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg2-1.png')

        self.fcku(self.pil_image)
        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/

        self.songname = QLineEdit()
        self.songname.setPlaceholderText("请输入歌曲名")
        self.songname.setParent(self)

        self.singername = QLineEdit()
        self.singername.setPlaceholderText("请输入歌手名")
        self.singername.setParent(self)

        self.btn_search = QPushButton("搜索")
        self.btn_search.setParent(self)

        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)
        
        self.songname.setMinimumSize(260, 50)
        self.songname.setMaximumSize(260, 50)
        self.singername.setMinimumSize(260, 50)
        self.singername.setMaximumSize(260, 50)
        self.btn_search.setMinimumSize(200, 50)
        self.btn_search.setMaximumSize(200, 50)
        self.btn_back.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(200, 50)
        
        #响应式
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(8)
        container.addLayout(ButtLayout)
        container.addStretch(1)
        
        ButtLayout.addStretch(10)
        ButtLayout.addWidget(self.songname)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.singername)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_search)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_back)
        ButtLayout.addStretch(2)
        self.setLayout(container)
        #响应式/
        #设置按钮位置(x,y,width,height)
        #self.btn_search.setGeometry(QtCore.QRect(700, 420, 200, 50))
        #设置按钮圆角
        self.btn_search.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 200, 50))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        #self.songname.setGeometry(QtCore.QRect(670, 280, 260, 50))
        #self.singername.setGeometry(QtCore.QRect(670, 350, 260, 50))
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh2_1
        if((wh2[0]-wh2_1[0]>0)or(wh2[1]-wh2_1[1]>0)):
            wh2_1=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh2_1[0]),int(wh2_1[1]))
        elif((wh2[0]-wh2_1[0]<0)or(wh2[1]-wh2_1[1]<0)):
            wh2_1=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh2_1[0]),int(wh2_1[1]))
    
    def refresh(self):
        w3_2.label_1.setText(s)
    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)
    
class SelectWindow2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('select')
        self.resize(1000, 600)

        #bg
        # palette = QPalette()
        # pix=QPixmap("./bg2-2.jpg")

        # pix = pix.scaled(self.width(),self.height())

        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)
        #bg/
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg2-2.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/
        self.label_1 = QLabel(s, self)
        QApplication.processEvents()
        self.label_1.repaint()
        self.label_1.setObjectName("label_1")
        self.label_1.setWordWrap(True)
        # self.label_1.setText(name_quanju[0] + "\n" + "消费成功")

        self.selector1 = QLineEdit()
        
        self.selector1.setPlaceholderText("请输入您选择的歌曲编号")
        self.selector1.setParent(self)

        self.btn_yes = QPushButton("确认")
        self.btn_yes.setParent(self)

        

        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)

        self.label_1.setStyleSheet("QLabel{color:rgb(14,255,255);font-size:25px;font-weight:normal;font-family:Arial;}")

        self.label_1.setMinimumSize(400, 500)
        self.label_1.setMaximumSize(550, 650)
        self.selector1.setMinimumSize(250, 50)
        self.selector1.setMaximumSize(300, 60)
        self.btn_yes.setMinimumSize(150, 40)
        self.btn_yes.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(150, 40)
        self.btn_back.setMaximumSize(200, 50)
        #self.label_1.setGeometry(QtCore.QRect(20, 20, 400, 500))#x,y,w,h
        #self.selector1.setGeometry(QtCore.QRect(20,450,250,50))
        #self.btn_yes.setGeometry(QtCore.QRect(700, 430, 150, 40))
        self.btn_yes.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')
        container = QHBoxLayout()

        # -----创建第1个组，添加多个组件-----
        # hobby 主要是保证他们是一个组。
        hobby_box = QGroupBox()
        # v_layout 保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        
        # 添加到v_layout中
        v_layout.addStretch(1)
        v_layout.addWidget(self.label_1)
        v_layout.addStretch(1)
        v_layout.addWidget(self.selector1)
        v_layout.addStretch(1)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # -----创建第2个组，添加多个组件-----
        # 性别组
        gender_box = QGroupBox()
        # 性别容器
        v1_layout = QVBoxLayout()
        # 性别选项
        
        # 追加到性别容器中
        v1_layout.addStretch(10)
        v1_layout.addWidget(self.btn_yes)
        v1_layout.addStretch(1)
        v1_layout.addWidget(self.btn_back)
        v1_layout.addStretch(3)
        # 添加到 box中
        gender_box.setLayout(v1_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)
    #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh2_2
        if((wh2[0]-wh2_2[0]>0)or(wh2[1]-wh2_2[1]>0)):
            wh2_2=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh2_2[0]),int(wh2_2[1]))
        elif((wh2[0]-wh2_2[0]<0)or(wh2[1]-wh2_2[1]<0)):
            wh2_2=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh2_2[0]),int(wh2_2[1]))
    
    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

class ListenWindow2(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('listen')
        self.resize(1000, 600)
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg2-3.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/
        self.btn_yes = QPushButton("播放/暂停")
        self.btn_yes.setParent(self)
        
        
        self.selector1 = QLineEdit()
        self.selector1.setGeometry(QtCore.QRect(20, 550, 400, 50))
        self.selector1.setPlaceholderText("您需要加入到的歌单名")
        self.selector1.setParent(self)
        

       
        self.btn_list = QPushButton("加入歌单")
        self.btn_list.setParent(self)
       
        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)

        self.selector1.setMinimumSize(250, 50)
        self.selector1.setMaximumSize(300, 60)
        self.btn_yes.setMinimumSize(150, 40)
        self.btn_yes.setMaximumSize(200, 50)
        self.btn_list.setMinimumSize(150, 40)
        self.btn_list.setMaximumSize(200, 50)
        self.btn_back.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(150, 40)
        
        #响应式
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(8)
        container.addLayout(ButtLayout)
        container.addStretch(1)
        
        ButtLayout.addStretch(10)
        ButtLayout.addWidget(self.btn_yes)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.selector1)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_list)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_back)
        ButtLayout.addStretch(3)
        self.setLayout(container)
        #响应式/
        # self.selector1.setGeometry(QtCore.QRect(700,290,250,50))

        # self.btn_list.setGeometry(QtCore.QRect(700, 430, 150, 40))
        self.btn_list.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #self.btn_yes.setGeometry(QtCore.QRect(700, 220, 150, 40))
        self.btn_yes.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh2_3
        if((wh2[0]-wh2_3[0]>0)or(wh2[1]-wh2_3[1]>0)):
            wh2_3=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh2_3[0]),int(wh2_3[1]))
        elif((wh2[0]-wh2_3[0]<0)or(wh2[1]-wh2_3[1]<0)):
            wh2_3=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh2_3[0]),int(wh2_3[1]))
    
    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

# 3
class NewWindow3(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('线路3')
        self.resize(1000, 600)

        #bg
        # palette = QPalette()
        # pix=QPixmap("./bg3-1.jpg")

        # pix = pix.scaled(self.width(),self.height())

        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)
        #bg/
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg3-1.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/
        
        self.songname = QLineEdit()
        self.songname.setPlaceholderText("请输入歌曲名")
        self.songname.setParent(self)

        self.singername = QLineEdit()
        self.singername.setPlaceholderText("请输入歌手名")
        self.singername.setParent(self)

        self.btn_search = QPushButton("搜索")
        self.btn_search.setParent(self)

        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)
        
        self.songname.setMinimumSize(260, 50)
        self.songname.setMaximumSize(260, 50)
        self.singername.setMinimumSize(260, 50)
        self.singername.setMaximumSize(260, 50)
        self.btn_search.setMinimumSize(200, 50)
        self.btn_search.setMaximumSize(200, 50)
        self.btn_back.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(200, 50)
        
        #响应式
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(8)
        container.addLayout(ButtLayout)
        container.addStretch(1)
        
        ButtLayout.addStretch(10)
        ButtLayout.addWidget(self.songname)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.singername)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_search)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_back)
        ButtLayout.addStretch(2)
        self.setLayout(container)
        #响应式/
        #设置按钮位置(x,y,width,height)
        #self.btn_search.setGeometry(QtCore.QRect(700, 420, 200, 50))
        #设置按钮圆角
        self.btn_search.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 200, 50))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh3_1
        if((wh2[0]-wh3_1[0]>0)or(wh2[1]-wh3_1[1]>0)):
            wh3_1=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh3_1[0]),int(wh3_1[1]))
        elif((wh2[0]-wh3_1[0]<0)or(wh2[1]-wh3_1[1]<0)):
            wh3_1=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh3_1[0]),int(wh3_1[1]))
    
    def fcku(self,fckimage):
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)
    def refresh(self):
        w3_3.label_1.setText(s)

class SelectWindow3(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('select')
        self.resize(1000, 600)

        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg3-2.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/

        self.label_1 = QLabel(s, self)
        QApplication.processEvents()
        self.label_1.repaint()
        self.label_1.setObjectName("label_1")
        self.label_1.setWordWrap(True)
        # self.label_1.setText(name_quanju[0] + "\n" + "消费成功")

        self.selector1 = QLineEdit()
        
        self.selector1.setPlaceholderText("请输入您选择的歌曲编号")
        self.selector1.setParent(self)

        self.btn_yes = QPushButton("确认")
        self.btn_yes.setParent(self)

        

        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)

        self.label_1.setStyleSheet("QLabel{color:rgb(225,22,173);font-size:20px;font-weight:normal;font-family:Arial;}")
        self.label_1.setMinimumSize(400, 500)
        self.label_1.setMaximumSize(550, 650)
        self.selector1.setMinimumSize(250, 50)
        self.selector1.setMaximumSize(300, 60)
        self.btn_yes.setMinimumSize(150, 40)
        self.btn_yes.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(150, 40)
        self.btn_back.setMaximumSize(200, 50)
        #self.label_1.setGeometry(QtCore.QRect(20, 20, 400, 500))#x,y,w,h
        #self.selector1.setGeometry(QtCore.QRect(20,450,250,50))
        #self.btn_yes.setGeometry(QtCore.QRect(700, 430, 150, 40))
        self.btn_yes.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')
        container = QHBoxLayout()

        # -----创建第1个组，添加多个组件-----
        # hobby 主要是保证他们是一个组。
        hobby_box = QGroupBox()
        # v_layout 保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        
        # 添加到v_layout中
        v_layout.addStretch(1)
        v_layout.addWidget(self.label_1)
        v_layout.addStretch(1)
        v_layout.addWidget(self.selector1)
        v_layout.addStretch(1)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # -----创建第2个组，添加多个组件-----
        # 性别组
        gender_box = QGroupBox()
        # 性别容器
        v1_layout = QVBoxLayout()
        # 性别选项
        
        # 追加到性别容器中
        v1_layout.addStretch(10)
        v1_layout.addWidget(self.btn_yes)
        v1_layout.addStretch(1)
        v1_layout.addWidget(self.btn_back)
        v1_layout.addStretch(3)
        # 添加到 box中
        gender_box.setLayout(v1_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)
    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh3_2
        if((wh2[0]-wh3_2[0]>0)or(wh2[1]-wh3_2[1]>0)):
            wh3_2=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh3_2[0]),int(wh3_2[1]))
        elif((wh2[0]-wh3_2[0]<0)or(wh2[1]-wh3_2[1]<0)):
            wh3_2=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh3_2[0]),int(wh3_2[1]))
    
    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

class ListenWindow3(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('listen')
        self.resize(1000, 600)
        #bg
        # palette = QPalette()
        # pix=QPixmap("./bg3-3.jpg")

        # pix = pix.scaled(self.width(),self.height())

        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)
        #bg/
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./bg3-3.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/
        self.btn_yes = QPushButton("播放/暂停")
        self.btn_yes.setParent(self)
        
        
        self.selector1 = QLineEdit()
        self.selector1.setGeometry(QtCore.QRect(20, 550, 400, 50))
        self.selector1.setPlaceholderText("您需要加入到的歌单名")
        self.selector1.setParent(self)
        

       
        self.btn_list = QPushButton("加入歌单")
        self.btn_list.setParent(self)
       
        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)

        self.selector1.setMinimumSize(250, 50)
        self.selector1.setMaximumSize(300, 60)
        self.btn_yes.setMinimumSize(150, 40)
        self.btn_yes.setMaximumSize(200, 50)
        self.btn_list.setMinimumSize(150, 40)
        self.btn_list.setMaximumSize(200, 50)
        self.btn_back.setMaximumSize(200, 50)
        self.btn_back.setMinimumSize(150, 40)
        
        #响应式
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(8)
        container.addLayout(ButtLayout)
        container.addStretch(1)
        
        ButtLayout.addStretch(10)
        ButtLayout.addWidget(self.btn_yes)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.selector1)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_list)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_back)
        ButtLayout.addStretch(3)
        self.setLayout(container)
        #响应式/
        # self.selector1.setGeometry(QtCore.QRect(700,290,250,50))

        # self.btn_list.setGeometry(QtCore.QRect(700, 430, 150, 40))
        self.btn_list.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #self.btn_yes.setGeometry(QtCore.QRect(700, 220, 150, 40))
        self.btn_yes.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        
        #self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')

        
        self.btn_back.setGeometry(QtCore.QRect(700, 500, 150, 40))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);border-radius: 10px;font-size:25px; border: 2px groove gray;border-style: outset;')
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        
        # self.timer1=threading.Timer(0.002,self.comp(wh2))
        # self.timer1.start()
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global wh3_3
        if((wh2[0]-wh3_3[0]>0)or(wh2[1]-wh3_3[1]>0)):
            wh3_3=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(wh3_3[0]),int(wh3_3[1]))
        elif((wh2[0]-wh3_3[0]<0)or(wh2[1]-wh3_3[1]<0)):
            wh3_3=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(wh3_3[0]),int(wh3_3[1]))
    
    def fcku(self,fckimage):
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)


######新歌单类
class SelectListWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Lists')
        self.resize(1000, 600)

        #bg
        # palette = QPalette()
        # pix=QPixmap("./list.jpg")

        # pix = pix.scaled(self.width(),self.height())

        # palette.setBrush(QPalette.Background,QBrush(pix))
        # self.setPalette(palette)
        #bg/
        #bg2
        self.lbl = QLabel(self)
        self.pil_image=QImage('./list.jpg')

        self.fcku(self.pil_image)


        #self.show()
        self.timer = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率

        self.timer.timeout.connect(lambda:self.fcku(self.pil_image))
        self.timer.start(10)
        #bg2/

        self.label_1 = QLabel(s, self)
        QApplication.processEvents()
        self.label_1.repaint()
        self.label_1.setObjectName("label_1")
        self.label_1.setWordWrap(True)

        self.selector1 = QLineEdit()
        self.selector1.setPlaceholderText("请输入您选择的歌单全名")
        self.selector1.setParent(self)

        self.btn_circle = QPushButton("顺序播放")
        self.btn_circle.setParent(self)
        

        self.btn_random = QPushButton("随机播放")
        self.btn_random.setParent(self)

        self.btn_pause = QPushButton("播放/暂停")
        self.btn_pause.setParent(self)



        self.btn_back = QPushButton("返回首页")
        self.btn_back.setParent(self)
        
        self.selector1.setMinimumSize(200,50)
        self.selector1.setMaximumSize(250,60)
        self.btn_circle.setMinimumSize(200,50)
        self.btn_circle.setMaximumSize(250,60)
        self.btn_random.setMinimumSize(200,50)
        self.btn_random.setMaximumSize(250,60)
        self.btn_pause.setMinimumSize(200,50)
        self.btn_pause.setMaximumSize(250,60)
        self.btn_back.setMinimumSize(200,50)
        self.btn_back.setMaximumSize(250,60)
        #设置按钮位置(x,y,width,height)
        #self.selector1.setGeometry(QtCore.QRect(400, 50, 200, 50))
        #设置按钮圆角
                #响应式
        container=QHBoxLayout()
        ButtLayout=QVBoxLayout()
        container.addStretch(1)
        container.addLayout(ButtLayout)
        container.addStretch(1)
        
        ButtLayout.addStretch(2)
        ButtLayout.addWidget(self.selector1)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_circle)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_random)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_pause)
        ButtLayout.addStretch(1)
        ButtLayout.addWidget(self.btn_back)
        ButtLayout.addStretch(2)
        self.setLayout(container)
        #响应式/

        self.selector1.setStyleSheet('background-color: rgb(192, 192, 192);font-size:15px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        #self.btn_circle.setGeometry(QtCore.QRect(400, 150, 200, 50))
        self.btn_circle.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        
        #self.btn_random.setGeometry(QtCore.QRect(400, 250, 200, 50))
        self.btn_random.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #self.btn_pause.setGeometry(QtCore.QRect(400, 350, 200, 50))
        self.btn_pause.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #self.btn_back.setGeometry(QtCore.QRect(400, 450, 200, 50))
        self.btn_back.setStyleSheet('background-color: rgb(192, 192, 192);font-size:25px;border-radius: 10px; border: 2px groove gray;border-style: outset;')
        #窗口等比缩放
        self.timer2 = QtCore.QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        self.timer2.timeout.connect(lambda:self.resizewindow())
        self.timer2.start(400)
        
    def wh(self):
        return [self.width(),self.height()]
    def resizewindow(self):
        time.sleep(0.002)
        wh2=self.wh()
        self.comp(wh2)
    def comp(self,wh2):
        global whl
        if((wh2[0]-whl[0]>0)or(wh2[1]-whl[1]>0)):
            whl=[max(self.width(),self.height()*5/3),max(self.height(),self.width()*0.6)]
            self.resize(int(whl[0]),int(whl[1]))
        elif((wh2[0]-whl[0]<0)or(wh2[1]-whl[1]<0)):
            whl=[min(self.width(),self.height()*5/3),min(self.height(),self.width()*0.6)]
            self.resize(int(whl[0]),int(whl[1]))
    
    def fcku(self,fckimage):
        # hbox = QHBoxLayout(self)
        #print(fckimage.size())
        pil_image = self.m_resize(self.width(), self.height(), fckimage)
        # fckimage=cv2.cvtColor(fckimage,cv2.COLOR_RGB2BGR)
        #fckimage = QImage(fckimage.width, fckimage.height, QImage.Format_RGB888)
        # print(fckimage.width)

        pixmap = QPixmap.fromImage(pil_image)
        # print(pixmap.height())
        # pixmap = self.m_resize(self.width(), self.height(), pixmap)
        self.lbl.resize(pil_image.width(),pil_image.height())
        self.lbl.setPixmap(pixmap)
        #print(pixmap.size())
        # hbox.addWidget(lbl)
        # self.setLayout(hbox)

    def m_resize(self,w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片

        w, h = pil_image.width(), pil_image.height() # 获取图像的原始大小

        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h

        factor = min([f1, f2])

        width = int(w * factor)

        height = int(h * factor)
        #return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

    def click_1(self):
        global my_thread
        my_thread = MyThread1()  # 创建线程
        my_thread.start()  # 开始线程
    def click_2(self):
        global my_thread
        my_thread = MyThread2()  # 创建线程
        my_thread.start()  # 开始线程
        
if __name__ == '__main__':
    while(1):
        try:
            app = QApplication(sys.argv)
            w1 = Mywindow()
            w1.show()

            w2_1 = NewWindow()

            w1.btn_path1.clicked.connect(w2_1.show)
            w1.btn_path1.clicked.connect(w1.close)
            w2_1.btn_search.clicked.connect(spider_hifini)
            w2_1.btn_search.clicked.connect(w2_1.refresh)
            w3_1 = SelectWindow()
            w2_1.btn_search.clicked.connect(w3_1.show)
            w2_1.btn_search.clicked.connect(w2_1.close)
            w2_1.btn_back.clicked.connect(w1.show)
            w2_1.btn_back.clicked.connect(w2_1.close)
            w2_1.btn_back.clicked.connect(over)

            w4_1 = ListenWindow()

            w3_1.btn_yes.clicked.connect(w4_1.show)
            w3_1.btn_yes.clicked.connect(w3_1.close)
            w3_1.btn_yes.clicked.connect(listen_hifini)
            w3_1.btn_back.clicked.connect(w1.show)
            w3_1.btn_back.clicked.connect(w3_1.close)
            w3_1.btn_back.clicked.connect(over)
            w4_1.btn_yes.clicked.connect(pause)
            w4_1.btn_list.clicked.connect(listadd1)

            w5_2 = informWindow()
            w4_1.btn_list.clicked.connect(w5_2.show)
            w5_2.btn_yes.clicked.connect(w5_2.close)

            w4_1.btn_back.clicked.connect(w1.show)
            w4_1.btn_back.clicked.connect(w4_1.close)
            w4_1.btn_back.clicked.connect(over)


            # 线路2
            w2_2 = NewWindow2()

            w1.btn_path2.clicked.connect(w2_2.show)
            w1.btn_path2.clicked.connect(w1.close)

            w3_2 = SelectWindow2()
            w2_2.btn_search.clicked.connect(spider_fangpi)
            w2_2.btn_search.clicked.connect(w2_2.refresh)
            w2_2.btn_search.clicked.connect(w3_2.show)
            w2_2.btn_search.clicked.connect(w2_2.close)

            w2_2.btn_back.clicked.connect(w1.show)
            w2_2.btn_back.clicked.connect(w2_2.close)
            w2_2.btn_back.clicked.connect(over)
            w4_2 = ListenWindow2()
            w3_2.btn_yes.clicked.connect(w4_2.show)
            w3_2.btn_yes.clicked.connect(w3_2.close)
            w3_2.btn_yes.clicked.connect(listen_fangpi)
            w3_2.btn_back.clicked.connect(w1.show)
            w3_2.btn_back.clicked.connect(w3_2.close)
            w3_2.btn_back.clicked.connect(over)


            w4_2.btn_yes.clicked.connect(pause)
            w4_2.btn_list.clicked.connect(listadd2)

            w5 = informWindow()
            w4_2.btn_list.clicked.connect(w5.show)
            w5.btn_yes.clicked.connect(w5.close)


            w4_2.btn_back.clicked.connect(w1.show)
            w4_2.btn_back.clicked.connect(w4_2.close)
            w4_2.btn_back.clicked.connect(over)
            # 线路3
            w2_3 = NewWindow3()

            w2_3.btn_search.clicked.connect(spider_yinyuelingfeng)
            w2_3.btn_search.clicked.connect(w2_3.refresh)
            w1.btn_path3.clicked.connect(w2_3.show)
            w1.btn_path3.clicked.connect(w1.close)

            w3_3 = SelectWindow3()
            w2_3.btn_search.clicked.connect(w3_3.show)
            w2_3.btn_search.clicked.connect(w2_3.close)


            w2_3.btn_back.clicked.connect(w1.show)
            w2_3.btn_back.clicked.connect(w2_3.close)
            w2_3.btn_back.clicked.connect(over)

            w4_3 = ListenWindow3()
            w3_3.btn_yes.clicked.connect(w4_3.show)
            w3_3.btn_yes.clicked.connect(w3_3.close)
            w3_3.btn_yes.clicked.connect(listen_yinyuelingfeng)
            w3_3.btn_back.clicked.connect(w1.show)
            w3_3.btn_back.clicked.connect(w3_3.close)
            w3_3.btn_back.clicked.connect(over)

            w4_3.btn_yes.clicked.connect(pause)
            w4_3.btn_list.clicked.connect(listadd3)

            w5_1 = informWindow()
            w4_3.btn_list.clicked.connect(w5_1.show)
            w5_1.btn_yes.clicked.connect(w5_1.close)



            w4_3.btn_back.clicked.connect(w1.show)
            w4_3.btn_back.clicked.connect(w4_3.close)
            w4_3.btn_back.clicked.connect(over)

            # 歌单选择
            wl = SelectListWindow()

            w1.btn_list.clicked.connect(wl.show)
            w1.btn_list.clicked.connect(w1.close)

            wl.btn_circle.clicked.connect(wl.click_1)
            wl.btn_random.clicked.connect(wl.click_2)
            wl.btn_pause.clicked.connect(pause)
            wl.btn_back.clicked.connect(death)
            wl.btn_back.clicked.connect(w1.show)
            wl.btn_back.clicked.connect(wl.close)
            app.exec()
        except:
            # print('出现错误')
            browser.close()
            continue