# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:31:47 2017

@author: g.gurkan
"""
import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import gui_1
import pyqtgraph as pg
import numpy as np
from cv2 import *

class myApp(QMainWindow,gui_1.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myApp,self).__init__(parent)
        self.setupUi(self)
        
       
        self.cam_image = pg.ImageItem()
        self.cam_image.setScale(2)
        self.dummy = np.array(np.zeros((180,60,3),dtype='uint8'))
        #self.cam_image.setOpts(axisOrder='row-major')
        self.figure2.addItem(self.cam_image)
        
        
        self.row = pg.PlotDataItem(background='w')
        
        self.figure1.addItem(self.row)
        self.figure1.plotItem.setTitle('Spectrum')
        self.figure1.plotItem.setLabels(bottom='Wavelength (nm)')
        self.figure1.plotItem.setTitle('Spectrum')
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.updateImage)
        
        self.buttonStart.clicked.connect(self.startCapture)
        self.buttonStop.clicked.connect(self.stopCapture)
        
        self.sliderExpo.valueChanged.connect(self.changeExpo)
        self.sliderGain.valueChanged.connect(self.changeGain)
        self.sliderContr.valueChanged.connect(self.changeContr)
        self.sliderBrigh.valueChanged.connect(self.changeBrigh)
        
        
       

        self.vid_obj = None
     
    def startCapture(self):
        self.vid_obj = VideoCapture(0)
        
        if self.vid_obj:
            #self.vid_obj.set(5,-1)
            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_WIDTH,640)
            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_HEIGHT,480)

            
            self.vid_obj.set(17,5000.)
            
            self.timer1.start(50)
            self.cam_image.show()
            self.row.show()

            
    def stopCapture(self):
        
        self.timer1.stop()
        self.vid_obj.release()
        self.cam_image.hide()
        self.row.hide()
  
    
    def updateImage(self):
        t,fr =self.vid_obj.read()
        
        fr = fr[210:270,140:320,:]
        
        if t:
            self.dummy[:,:,2]=fr[:,:,0].T #B
            self.dummy[:,:,1]=fr[:,:,1].T #G
            self.dummy[:,:,0]=fr[:,:,2].T #R
            
            gray = cvtColor(fr,COLOR_BGR2GRAY)
            self.cam_image.setImage(image=self.dummy,autolevels=False)
            spectrum =np.sum(gray,0).astype('float')
            spectrum_n = spectrum/np.max(spectrum)
            self.row.setData(np.linspace(313,682,180),spectrum_n)
        
    ## VIDEO CONTROLS
    
    def changeGain(self,val):
        if self.vid_obj:
            self.vid_obj.set(cv.CV_CAP_PROP_GAIN,np.uint8(val))
    
    def changeExpo(self,val):
        if self.vid_obj:
            self.vid_obj.set(cv.CV_CAP_PROP_EXPOSURE,-1*val)
    def changeBrigh(self,val):
        if self.vid_obj:
            self.vid_obj.set(cv.CV_CAP_PROP_BRIGHTNESS,val)
    def changeContr(self,val):
        if self.vid_obj:
            self.vid_obj.set(cv.CV_CAP_PROP_CONTRAST,val)
        
        
        
        
        
        



app=QApplication(sys.argv)
form=myApp()
form.show()
app.exec_()
