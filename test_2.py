from PyQt5.QtWidgets import QWidget,QHBoxLayout,QTableWidget,QPushButton,QApplication,QVBoxLayout,QTableWidgetItem,QCheckBox,QAbstractItemView,QHeaderView,QLabel,QFrame
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QColor
from faker import Factory
import random
import sys,win32
def full_projection_drafting():
    #--------------drafting parameter settings---------------
    drawingview_para = [[594.5,420.5],[928.126221,420.5],[594.5,205.066765],[594.5,665.083374],[761.31331,420.5],[342.570679,420.5],[861.31311,665.083374]]
    drawingview_direction = [4,2,3,1,0]
    drawing_scale = 0.5
    #-------------main program----------------------
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = document.Add('Drawing')
    #drawingdocument.Stardard = (0) #catANSI = 0, catISO = 1, catJIS = 2
    drawingdocument.standard = 1
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingsheet.PaperSize = 2 # A0=2, A1=3, A2=4, A3=5, A4=6
    drawingsheet.scale = drawing_scale
    drawingsheet.Orientation = 1 #Portrait = 0, LandScape = 1, BestFit = 2
    drawingviews1 = drawingsheet.Views
    partdoc = document.Item('Door_Panel.CATPart')
    product = partdoc.GetItem('Door_Panel')
    #--------------------initial front view create

    drawingview1 = drawingviews1.Add('AutomaticNaming')
    drawingview1.X = drawingview_para[0][0]
    drawingview1.Y = drawingview_para[0][1]
    drawingview1.Scale = drawing_scale
    drawingviewgenerativelinks1 = drawingview1.GenerativeLinks
    drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
    drawingviewgenerativebehavior1.Document = product
    drawingviewgenerativebehavior1.DefineFrontView(-1,0,0,0,0,1) #Vector Direction Value
    drawingviewgenerativebehavior1.Update()

    drawingview1 = drawingviews1.Item('Front view')
    drawingtexts1 = drawingview1.Texts
    drawingtext1 = drawingtexts1.Item(1)
    drawingtexts1 = drawingtext1.Parent
    # selection.Add(drawingtext1)
    # selection.Delete()
    # selection.Clear()
#----------------2nd to 6th------------------------------
    for i in range(1,len(drawingview_para)-1):
        drawingview2 = drawingviews1.Add('AutomaticNaming')
        drawingview2.X = drawingview_para[i][0]
        drawingview2.Y = drawingview_para[i][1]
        drawingview2.Scale = drawing_scale
        drawingviewgenerativelinks2 = drawingview2.GenerativeLinks
        drawingviewgenerativebehavior2 = drawingview2.GenerativeBehavior
        drawingviewgenerativebehavior2.Document = product
        drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
        drawingviewgenerativebehavior2.DefineProjectionView(drawingviewgenerativebehavior1,drawingview_direction[i-1]) #define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
        drawingviewgenerativebehavior2.Update()
#------------------7th----------------------
    drawingview7 = drawingviews1.Add('AutomaticNaming')
    drawingview7.X = drawingview_para[len(drawingview_para)-1][0]
    drawingview7.Y = drawingview_para[len(drawingview_para)-1][1]
    drawingview7.Scale = drawing_scale
    drawingviewgenerativelinks7 = drawingview7.GenerativeLinks
    drawingviewgenerativebehavior7 = drawingview7.GenerativeBehavior
    drawingviewgenerativebehavior7.Document = product
    drawingviewgenerativebehavior7.DefineIsometricView(-0.707,0.707,0,-0.4082,-0.4082,0.8164)
#----------------Model update----------------------
    drawingviewgenerativebehavior1.Update()
    drawingviewgenerativebehavior7.Update()
    drawingview1.Activate()
#---------------resetting view to full-view-----------
    SpecsAndGeomWindow = catapp.ActiveWindow
    specViewer = SpecsAndGeomWindow.ActiveViewer
    specViewer.Reframe()

# full_projection_drafting()