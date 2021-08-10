#import python windows COM object module
import win32com.client as win32

#import python modules
import subprocess
from subprocess import CREATE_NEW_CONSOLE
import os
import psutil
import math
#import global varibles for value pass through
import global_Var as gvar
import sheetmetal_model



def model_unfolded_view(target,w,h,d):#,scale):
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.door_L: 'Door_Panel', gvar.mtplt_B: 'Mtplt_Panel'}
    view_attr = {'front': 'Front_view', 'mtplt': 'Mtplt_view', 'left': 'Left_view'}
    catapp = win32.Dispatch('CATIA.Application')
    #document = catapp.Documents
    #drawingdocument = document.Open(gvar.system_root+gvar.mother_drafting_template+'A4_Box'+'.CATDrawing')
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews = drawingsheet.Views
    result1 = DIM_REF_COORD(h,w,d)
    def execute(keyword):
        return getattr(result1, keyword)
    if target in part_attr.keys():
        drawingview = drawingviews.ActiveView
        if 'bend' in target:
            part_attr[target] = part_attr[target]+'_bend'
        print(execute(part_attr[target]))
        a = execute(part_attr[target])()
    elif target in view_attr.keys():
        #drawingview = drawingviews.Item(view_attr[target])
        print(' '.join(view_attr[target].split('_')))
        drawingview = drawingviews.Item(' '.join(view_attr[target].split('_')))
        drawingview.Activate()
        print(execute(view_attr[target]))
        a = execute(view_attr[target])()
    factory2d = drawingview.Factory2D
    for data in a:
        for i in range(0,len(a[data])):
            dim_ref_1 = a[data][i][0]
            dim_ref_2 = a[data][i][1]
            dim_ref_3 = a[data][i][2]
            print(dim_ref_1)
            print(dim_ref_2)
            print(dim_ref_3)
            point1 = factory2d.CreatePoint(dim_ref_1[0],dim_ref_1[1])
            point2 = factory2d.CreatePoint(dim_ref_2[0],dim_ref_2[1])
            geoelem = [point1,point2]
            geocoord = (dim_ref_1[0],dim_ref_1[1],dim_ref_2[0],dim_ref_2[1])
            if dim_ref_1[1] == dim_ref_2[1]:
                dim1 = drawingview.Dimensions.Add(0,geoelem,geocoord,3)
                dim1.Name = '%s_X' % data
                drawingdim = drawingview.Dimensions.Item('%s_X' % data)
            elif dim_ref_1[0] == dim_ref_2[0]:
                dim1 = drawingview.Dimensions.Add2(0,geoelem,geocoord,None,90)
                dim1.Name = '%s_Y' % data
                drawingdim = drawingview.Dimensions.Item('%s_Y' % data)
            else:
                pass
            drawingdim.MoveValue(dim_ref_3[0],dim_ref_3[1],0,0)

class DIM_REF_COORD:
    def __init__(self,box_w,box_h,box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)

    def Side_Panel_U(self):
        #Horizontal dim ref coord
        sideU_W = self.box_w/2
        sideU_D = self.box_d+14.5
        chamfer_corner = sideU_D-47.5
        X_dim = XY_coord_output(sideU_W,chamfer_corner)
        Y_dim = XY_coord_output(0,sideU_D)
        X_dim_ref = [0,sideU_D+10]
        Y_dim_ref = [-sideU_W-10,sideU_D/2]
        return {DIM_REF_COORD.Side_Panel_U.__name__:[[X_dim.quadrant_1(),X_dim.quadrant_2(),X_dim_ref],
                                                     [[0,0],Y_dim.quadrant_1(),Y_dim_ref]]}

    def Side_Panel_D(self):
        #Horizontal dim ref coord
        sideU_W = self.box_w/2
        sideU_D = self.box_d+14.5
        chamfer_corner = sideU_D-47.5
        X_dim = XY_coord_output(sideU_W,chamfer_corner)
        Y_dim = XY_coord_output(0,sideU_D)
        X_dim_ref = [0,sideU_D+10]
        Y_dim_ref = [-sideU_W-10,sideU_D/2]
        return {DIM_REF_COORD.Side_Panel_D.__name__:[[X_dim.quadrant_1(),X_dim.quadrant_2(),X_dim_ref],
                                                     [[0,0],Y_dim.quadrant_1(),Y_dim_ref]]}
    def Mtplt_Panel(self):
        mtplt_W = (self.box_w-50)/2
        mtplt_H = (self.box_h-50)/2
        dim = XY_coord_output(mtplt_W,mtplt_H)
        X_dim_ref = [0,mtplt_H+10]
        Y_dim_ref = [-mtplt_W-10,0]
        return {DIM_REF_COORD.Mtplt_Panel.__name__:[[dim.quadrant_2(),dim.quadrant_1(),X_dim_ref],
                                                    [dim.quadrant_3(),dim.quadrant_2(),Y_dim_ref]]}

    def Mtplt_Panel_bend(self):
        mtplt_W = (self.box_w - 50) / 2 + 6
        mtplt_H = (self.box_h - 50) / 2 + 6
        dim = XY_coord_output(mtplt_W, mtplt_H)
        X_dim_ref = [0, mtplt_H + 10]
        Y_dim_ref = [-mtplt_W - 10, 0]
        return {DIM_REF_COORD.Mtplt_Panel.__name__: [[dim.quadrant_2(), dim.quadrant_1(), X_dim_ref],
                                                     [dim.quadrant_3(), dim.quadrant_2(), Y_dim_ref]]}

    def Door_Panel(self):
        door_W = (self.box_w+40)/2
        door_H = (self.box_h+40)/2
        dim = XY_coord_output(door_W,door_H)
        X_dim_ref = [0,door_H+20]
        Y_dim_ref = [-door_W-20,0]
        return {DIM_REF_COORD.Door_Panel.__name__:[[dim.quadrant_3(),dim.quadrant_4(),X_dim_ref],
                                                    [dim.quadrant_3(),dim.quadrant_2(),Y_dim_ref]]}

    def Body_Panel(self):
        expand_W_half = self.box_w/2 + self.box_d+15-3
        expand_H_half = self.box_h/2-1.5
        body_flange_chamfer = expand_H_half-16.7
        chamfer_corner = expand_W_half-47.5
        X_dim = XY_coord_output(expand_W_half,body_flange_chamfer)
        Y_dim = XY_coord_output(chamfer_corner,expand_H_half)
        X_dim_ref = [0,expand_H_half+25]
        Y_dim_ref = [-expand_W_half-20,0]
        return {DIM_REF_COORD.Body_Panel.__name__:[[X_dim.quadrant_2(),X_dim.quadrant_1(),X_dim_ref],
                                                   [Y_dim.quadrant_3(),Y_dim.quadrant_2(),Y_dim_ref]]}

    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h/2
        view_half_w = view_w/2
        x_dim = XY_coord_output(view_half_w,0)
        y_dim = XY_coord_output(view_half_w,view_h)
        x_dim_ref = [0,25]
        y_dim_ref = [-view_half_w-25,-view_half_h]
        return {DIM_REF_COORD.Front_view.__name__:[[x_dim.quadrant_1(),x_dim.quadrant_2(),x_dim_ref],
                                                   [x_dim.quadrant_2(),y_dim.quadrant_3(),y_dim_ref]]}



    def Mtplt_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w-25, -25)
        y_dim = XY_coord_output(view_half_w-25, view_h-25)
        x_dim_ref = [0, 25]
        y_dim_ref = [-view_half_w - 25, -view_half_h]
        return {DIM_REF_COORD.Mtplt_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]
                                                    ]}

    def Left_view(self):
        view_h = self.box_h
        view_d = self.box_d
        view_half_d = view_d/2
        view_half_h = view_h/2
        x_dim = XY_coord_output(view_d,0)
        y_dim = XY_coord_output(0,-view_h)
        x_dim_ref = [view_half_d,25]
        y_dim_ref = [-25,-view_half_h]
        return {DIM_REF_COORD.Left_view.__name__:[[x_dim.quadrant_1(),[0,0], x_dim_ref],
                                                  [[0,0],y_dim.quadrant_1(), y_dim_ref]
                                                  ]}

model_unfolded_view()