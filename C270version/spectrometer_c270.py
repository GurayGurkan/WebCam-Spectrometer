# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:31:47 2017

@author: g.gurkan

"""
import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import gui_c270
import pyqtgraph as pg
import numpy as np
from cv2 import *

class myApp(QMainWindow,gui_c270.Ui_MainWindow):
    def __init__(self,parent=None):
        super(myApp,self).__init__(parent)
        self.setupUi(self)
        
       
        self.cam_image = pg.ImageItem()
        self.cam_image.setScale(1)
        self.dummy = np.array(np.zeros((330,210,3),dtype='uint8'))
        self.vector = np.zeros((20*60*5,3),dtype='uint8')
        self.frame = 0
        #self.dummy = np.array(np.zeros((270,160,3),dtype='uint8'))
        #self.cam_image.setOpts(axisOrder='row-major')
        self.figure2.addItem(self.cam_image)
        
        self.zoom_image = pg.ImageItem()
        self.zoom_image.setScale(2.5)
        self.figure3.addItem(self.zoom_image)
        
        
        self.row = pg.PlotDataItem()
        
        self.figure1.addItem(self.row)
        self.figure1.plotItem.setTitle('Spectrum')
        
        self.figure1.plotItem.setLabels(bottom='Wavelength (nm)')
        self.figure1.plotItem.setXRange(370,699,padding=0)
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.updateImage)
        
        self.buttonStart.clicked.connect(self.startCapture)
        self.buttonStop.clicked.connect(self.stopCapture)
        
        self.initFlag = False
        self.sliderExpo.valueChanged.connect(self.changeExpo)
        self.sliderGain.valueChanged.connect(self.changeGain)
        self.sliderContr.valueChanged.connect(self.changeContr)
        self.sliderBrigh.valueChanged.connect(self.changeBrigh)
        self.sliderWB.valueChanged.connect(self.changeWB)
        
        
       

        self.vid_obj = None
     
    def startCapture(self):
        self.vid_obj = VideoCapture(0)
        
        
        if self.vid_obj:
            #self.vid_obj.set(5,-1)
            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_WIDTH,1280)
            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_HEIGHT,960)

            
            self.initParams()
            
            self.timer1.start(50)
            self.cam_image.show()
            self.zoom_image.show()
            self.row.show()

            
    def stopCapture(self):
        
        self.timer1.stop()
        self.vid_obj.release()
        self.cam_image.hide()
        self.row.hide()
        self.frame = 0

  
    
    def updateImage(self):
        t,fr =self.vid_obj.read()
        
        fr = fr[320:530,370:700,:]
        
        if t:
            
            self.vector[self.frame,0]=fr[20,20,0]
            self.vector[self.frame,1]=fr[20,20,1]
            self.vector[self.frame,2]=fr[20,20,2]
            self.dummy[:,:,2]=fr[:,:,0].T #B
            self.dummy[:,:,1]=fr[:,:,1].T #G
            self.dummy[:,:,0]=fr[:,:,2].T #R
            self.dummy2 = self.dummy[:,85:135,:]
            
            # gray = cvtColor(fr,COLOR_BGR2GRAY)
            self.cam_image.setImage(image=self.dummy,autolevels=False)
            self.zoom_image.setImage(image=self.dummy2,autolevels=False)
            fr = fr.astype('double')
            spectrum =(np.sum(np.sum(fr[85:135,:,:],0),1))
            #spectrum_n = spectrum/np.max(spectrum)
            
            #self.row.setData(np.linspace(363,680,180),spectrum_n)
            self.row.setData(370+np.arange(330),spectrum)
            self.frame= self.frame +1
        
    ## VIDEO CONTROLS
    
    def changeGain(self,val):
        if self.vid_obj:
            if self.initFlag:
                self.vid_obj.set(cv.CV_CAP_PROP_GAIN,np.uint8(val))
    
    def changeExpo(self,val):
        if self.vid_obj:
            if self.initFlag:
                self.vid_obj.set(cv.CV_CAP_PROP_EXPOSURE,-1*val)
    def changeBrigh(self,val):
        if self.vid_obj:
            if self.initFlag:
                self.vid_obj.set(cv.CV_CAP_PROP_BRIGHTNESS,val)
    def changeContr(self,val):
        if self.vid_obj:
            if self.initFlag:
                self.vid_obj.set(cv.CV_CAP_PROP_CONTRAST,val)
    def changeWB(self,val):
        if self.vid_obj:
            if self.initFlag:
                self.vid_obj.set(17,val)
    
    def initParams(self):
        if self.vid_obj:
            self.sliderExpo.setValue(-1*self.vid_obj.get(cv.CV_CAP_PROP_EXPOSURE))
            self.sliderGain.setValue(self.vid_obj.get(cv.CV_CAP_PROP_GAIN))
            self.sliderContr.setValue(self.vid_obj.get(cv.CV_CAP_PROP_CONTRAST))
            self.sliderBrigh.setValue(self.vid_obj.get(cv.CV_CAP_PROP_BRIGHTNESS))
            self.sliderWB.setValue(self.vid_obj.get(17))
            self.initFlag=True
            
       
        
        
        
        



app=QApplication(sys.argv)
form=myApp()
form.show()
app.exec_()
