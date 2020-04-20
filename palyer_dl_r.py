#-*- coding:utf-8 -*-
#*******************************************************************
#*******************************************************************
#*************************导入模块***********************************
#*******************************************************************
#*******************************************************************
from  PyQt4.QtGui  import *
from  PyQt4.QtCore  import *

import shutil
import sys
import random
import os
import json


import subprocess





reload(sys)
sys.setdefaultencoding("utf-8")

ffpmpegRoot=os.path.abspath(os.path.dirname(__file__)).replace('\\','/')

ffmpeg=ffpmpegRoot+"/ffmpeg/bin/ffmpeg.exe"
ffplay=ffpmpegRoot+"/ffmpeg/bin/ffplay.exe"
ffprobe=ffpmpegRoot+"/ffmpeg/bin/ffprobe=.exe"






#*******************************************************************
#*******************************************************************
#***************************布局类**********************************
#*******************************************************************
#*******************************************************************
class graphicsView(QGraphicsView):
    def __init__(self,parent=None):
        super(graphicsView,self).__init__(parent)
        
     
        self.image=""
        QObject.connect(self, SIGNAL('mousePressEvent()'),self.mousePressEvent)

        

        
    def wheelEvent(self, event):
        
        value=event.delta()
        if event.delta() >= 0:
            self.width =self.image.width()
            self.height=self.image.height()
            if self.width< 400:
                self.width =self.image.width()*1.5
                self.height=self.image.height()*1.5
                pic=self.image.scaled(self.width,self.height,aspectRatioMode=Qt.KeepAspectRatio)
                self.graphicsView.removeItem(self.item)
                item1= QGraphicsPixmapItem(pic)

                self.graphicsView= QGraphicsScene()
                self.graphicsView.addItem(item1)                
                self.setScene(self.graphicsView)
                #self.setAlignment(Qt.AlignCenter and Qt.AlignTop)
                self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
                self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setFrameShape(QFrame.NoFrame)
                #self.setBackgroundBrush(QBrush(QColor(70, 170, 80)))
                        
                self.item=item1
                
            elif self.width< 800:
                self.width =self.image.width()*1.2
                self.height=self.image.height()*1.2
                pic=self.image.scaled(self.width,self.height,aspectRatioMode=Qt.KeepAspectRatio)
                self.graphicsView.removeItem(self.item)

                self.graphicsView= QGraphicsScene()
                item1= QGraphicsPixmapItem(pic)               
                self.graphicsView.addItem(item1)                
                self.setScene(self.graphicsView)
                #self.setAlignment(Qt.AlignCenter and Qt.AlignTop)
                self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
                self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setFrameShape(QFrame.NoFrame)
                #self.setBackgroundBrush(QBrush(QColor(70, 170, 80)))
                self.item=item1
        elif event.delta() <=  0:
            
    
            self.width =self.image.width()
            self.height=self.image.height()
            if self.width>800:
                self.width =self.image.width()*0.5
                self.height=self.image.height()*0.5
                pic=self.image.scaled(self.width,self.height,Qt.IgnoreAspectRatio)
                
                self.graphicsView.removeItem(self.item)
        
         
                self.graphicsView= QGraphicsScene()
                
                item1 = QGraphicsPixmapItem(pic)               
                self.graphicsView.addItem(item1)
                
                self.setScene(self.graphicsView)
                #self.setAlignment(Qt.AlignCenter or Qt.AlignTop)
                self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
                self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setFrameShape(QFrame.NoFrame)
                #self.setBackgroundBrush(QBrush(QColor(50, 200, 100)))
                
                
                self.item=item1
                
                
            elif self.width>400:
                self.width =self.image.width()*0.75
                self.height=self.image.height()*0.75
                pic=self.image.scaled(self.width,self.height,Qt.IgnoreAspectRatio)
                
                self.graphicsView.removeItem(self.item)
        
         
                self.graphicsView= QGraphicsScene()
                
                item1 = QGraphicsPixmapItem(pic)               
                self.graphicsView.addItem(item1)

                self.setScene(self.graphicsView)
                #self.setAlignment(Qt.AlignCenter or Qt.AlignTop)
                self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
                self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
                self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.setFrameShape(QFrame.NoFrame)
                #self.setBackgroundBrush(QBrush(QColor(50, 200, 100)))
                
                
                self.item=item1
                

                
           
                
#*******************************************************************
#*******************************************************************
#***************************拖拽类**********************************
#*******************************************************************
#*******************************************************************

class MyLineEdit(QLineEdit):
        def __init__( self, parent=None ):
            super(MyLineEdit, self).__init__(parent)
            #self.setDragEnabled(True)
            pass
        def dragEnterEvent( self, event ):
            
            data = event.mimeData()
            urls = data.urls()
            if ( urls and urls[0].scheme() == 'file' ):
                event.acceptProposedAction()
        def dragMoveEvent( self, event ):
            data = event.mimeData()
            urls = data.urls()
            if ( urls and urls[0].scheme() == 'file' ):
                event.acceptProposedAction()

        def dropEvent( self, event ):
            data = event.mimeData()
            urls = data.urls()
            if ( urls and urls[0].scheme() == 'file' ):
                filepath = str(urls[0].path())[1:]
                filepath=filepath.decode('utf-8')
                self.setText(filepath)

#*******************************************************************
#*******************************************************************
#***************************功能类**********************************
#*******************************************************************
#*******************************************************************
class bilibili_gui(QWidget):
    
    def __init__(self):
        super(bilibili_gui,self).__init__()

        #self.setWindowFlags(Qt.Window)
        self.setWindowTitle(u"Vedio Download")
        self.initUI()

                        
    def initUI(self):
        #人员信息统计并从空添加，使用列表即可。
        #self._tree=Treeview()
        #self._list=Listview()

        down_address=QLabel(u'输入下载地址：')
        self.down_address=QLineEdit()
        analyze=QPushButton(u"记录")

        
        
        self._tree=graphicsView(self)
 
        
        
        save_adrss=QLabel(u'下载位置：')
        self.save_address=MyLineEdit()
        self.save_adrss_look=QPushButton(u"==>：")
        
        start_down=QPushButton(u"下载视频")
        open_video =QPushButton(u"缓存位置")

        file_name=QLabel(u'视频名称：')
        self.file_name=QComboBox()
        self.file_name.setEditable(True)
        time_pos=QLabel(u"进度")
        self.time_pos=QLineEdit(u"0")
        self.pbar = QProgressBar()

        #print dir(self.pbar)

        
        #groupNameData.setFrameStyle(QFrame.Panel|QFrame.Sunken)
        

        
        laty_1=QHBoxLayout()
        laty_1.addWidget(down_address)
        laty_1.addWidget(self.down_address)
        laty_1.addWidget(analyze)
     

        laty_2=QHBoxLayout()
        laty_2.addWidget(self._tree)
        
        
      

        laty_3=QHBoxLayout()
        laty_3.addWidget(save_adrss)
        laty_3.addWidget(self.save_address)
        laty_3.addWidget(self.save_adrss_look)


        laty_4=QHBoxLayout()
        laty_4.addWidget(file_name,1)
        laty_4.addWidget(self.file_name,7)
        laty_4.addWidget(time_pos,1)
        laty_4.addWidget(self.pbar ,2)

        laty_5=QHBoxLayout()
        laty_5.addWidget(start_down)
        laty_5.addWidget(open_video)


        all_lay=QVBoxLayout()
        all_lay.addLayout(laty_1)
        all_lay.addLayout(laty_2)
        all_lay.addLayout(laty_3)
        all_lay.addLayout(laty_4)
        all_lay.addLayout(laty_5)


      
        self.setLayout(all_lay)
        
        self.resize(500,650)

        self.save_adrss_look.clicked.connect(self.saveAdrss)
        start_down.clicked.connect(self.startDownload)
        open_video.clicked.connect(self.openVideo)
        analyze.clicked.connect(self.setMemory)
        self.file_name.currentIndexChanged.connect(self.setData)


        self.show()


    def setMemory(self):
        data="cache/image.png"

        memory_list=[]
        memory_dict={}
        
        if str(self.down_address.text())!="":
            
            if not os.path.exists(ffpmpegRoot+"/cache/histy.part"):
                memory_list.append(str(self.down_address.text()))
                memory_list.append(str(self.save_address.text()))
                memory_dict[str(self.file_name.text())]=memory_list#根据视频名称切换储存信息。

                with open(ffpmpegRoot+"/cache/histy.part","w") as file:
                    json.dump(memory_dict,file)
                    
            else:
                with open(ffpmpegRoot+"/cache/histy.part") as file:
                    memory_dict= json.loads(file.read())
                    file_keys=memory_dict.keys()
                    
                    
                    if str(self.down_address.text())=="":
                        QMessageBox.information(self,u"提示", u"请填写下载地址！")
                        return 
                    else:
                        memory_list.append(str(self.down_address.text()))
                        
                    if str(self.save_address.text())=="":
                        QMessageBox.information(self,u"提示", u"请填写储存地址！")
                        return 
                    else:
                        memory_list.append(str(self.save_address.text()))
                        
                    if str(self.file_name.currentText())=="":
                        QMessageBox.information(self,u"提示", u"请填写视频名称！")
                        return 
                    else:
                        if str(self.file_name.currentText()) not in file_keys:
                            memory_dict[str(self.file_name.currentText())]=memory_list
                            self.file_name.addItem(str(self.file_name.currentText()).decode("utf-8"))
                        else:
                            QMessageBox.information(self,u"提示", u"该视频已存在！")
                            return 
                
                self.loadImage(data)
                with open(ffpmpegRoot+"/cache/histy.part","w") as file:
                    json.dump(memory_dict,file)
                    
        else:
            QMessageBox.information(self,u"提示", u"地址为空，无法下载")


    def setData(self):#创建选择菜单
        with open(ffpmpegRoot+"/cache/histy.part") as file:
            memory_dict= json.loads(file.read())
        filename=str(self.file_name.currentText()).decode("utf-8")
        self.save_address.setText(memory_dict[filename][1])
        self.down_address.setText(memory_dict[filename][0])
    def createRandomString(self,len):
        print ('wet'.center(10,'*'))
        raw = ""
        range1 = range(58, 65) # between 0~9 and A~Z
        range2 = range(91, 97) # between A~Z and a~z

        i = 0
        while i < len:
            seed = random.randint(48, 122)
            if ((seed in range1) or (seed in range2)):
                continue;
            raw += chr(seed);
            i += 1
        return raw


    def startDownload(self):
        self.setMemory()
        url=str(self.down_address.text())
        save_address=str(self.save_address.text())
        if str(self.file_name.text())=="":
            save_address=save_address+"/"+self.createRandomString(6)+".mp4"
        else:
            save_address=save_address+"/"+str(self.file_name.text())+".mp4"
            
        cmd=ffmpeg + " -i "+ url + " -c copy "+save_address
        

        cmd=cmd.encode(sys.getfilesystemencoding())
        if "?" in cmd:
            cmd=cmd.replace("?","")
        print cmd
        subprocess.call(cmd , shell=True)

        
                
            
    def loadImage(self,data):
        try:
            if os.path.exists(data):
                self._tree.image=QPixmap(data)
                self._tree.graphicsView= QGraphicsScene()            
                self._tree.item = QGraphicsPixmapItem(self._tree.image)               
                self._tree.graphicsView.addItem(self._tree.item)                
                self._tree.setScene(self._tree.graphicsView)
                    
        except Exception as e:
            print e
            QMessageBox.information(self,u"提示", u"图像解析失败")
                        
       
               
                
           
    def openVideo(self):
        
        if os.path.exists(ffpmpegRoot+"/cache/histy.part"):
            with open(ffpmpegRoot+"/cache/histy.part") as file:
                filedata= json.loads(file.read())
                filelink=filedata[filedata.keys()[0]][0]
                filepos=filedata[filedata.keys()[0]][1]
                filename=filedata.keys()[0]
        else:
            filelink=""
            filepos=""
            filename=""
        if str(self.down_address.text())!="" and str(self.save_address.text())!="" and str(self.file_name.currentText())!="":
            path= str(self.save_address.text()).decode("utf-8")
            if os.path.isdir(path):
                os.startfile(path)
                
        elif str(self.down_address.text())!="" and str(self.save_address.text())!='' and str(self.file_name.currentText())=="":
            for item in filedata.keys():
                self.file_name.addItem(item)
        elif str(self.save_address.text())!='' and str(self.file_name.currentText())!="" and str(self.down_address.text())=="":                                   
            self.down_address.setText(filelink)
        elif str(self.file_name.currentText())!="" and str(self.down_address.text())!="" and  str(self.save_address.text())=='':
            self.save_address.setText(filepos)
            
        elif str(self.file_name.currentText())!="" and str(self.down_address.text())=="" and  str(self.save_address.text())=='':
            self.save_address.setText(filepos)
            self.down_address.setText(filelink)
        elif str(self.file_name.currentText())=="" and str(self.down_address.text())!="" and  str(self.save_address.text())=='':
            self.save_address.setText(filepos)
            for item in filedata.keys():
                self.file_name.addItem(item)
        elif str(self.file_name.currentText())=="" and str(self.down_address.text())=="" and  str(self.save_address.text())!='':
            self.down_address.setText(filelink)
            for item in filedata.keys():
                self.file_name.addItem(item)
        else:
            self.save_address.setText(filepos)
            self.down_address.setText(filelink) 
            if os.path.exists(ffpmpegRoot+"/cache/histy.part"):
                for item in filedata.keys():
                    self.file_name.addItem(item)
            
   
    def saveAdrss(self):
        #利用文件保存对话框获取文件的路径名称，将存在的json,txt文件拷贝至指定位置。
        
        
        filename = QFileDialog.getExistingDirectory()
        
        if filename:
            filename=str(filename).decode('utf-8')
            filename=filename.replace("\\",'/')
            self.save_address.setText(filename)
        else:
            pass
            #QMessageBox.information(self,u'提示页面',u'取消成功')



#*******************************************************************
#*******************************************************************
#***************************主函数***********************************
#*******************************************************************
#******************************************************************* 

if __name__ == '__main__': 
    app = QApplication(sys.argv)
    bili = bilibili_gui()
    bili.show()
    sys.exit(app.exec_())
