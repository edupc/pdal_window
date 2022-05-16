import os, sys, win32

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView
import Window_Catia as wc
from bom import Excel_Bom
import globals_var as gvar
import drafting as draft
import drafting_Part as drafting_p
import drafting_Dim as drafting_d
from untitled import Ui_MainWindow, creat, Window_dwg, about
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

for k in range(0,4):
    print(gvar.catia_save[k])
    wc.part_open(gvar.catia_save[k], gvar.full_save_dir + "\\AL500500-2022-05-11'17h40m27s'")

    draft_gen_data = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    window_gen_data = []
    bom_whd_value = []
    draft.add_drafting_infomation(draft_gen_data, 0)

    window_gen_data.append(gvar.width)
    window_gen_data.append(gvar.height)
    window_gen_data.append(gvar.depth)
    for i in range(0, 3):
        bom_whd_value.append(int(window_gen_data[i]))
    print(bom_whd_value)
    rescale_flag = True
    scale = 1
    while rescale_flag is True:  # checking if scale recalibration is needed
        scale = scale + 1
        [center_data, scale, rescale_flag] = drafting_p.projection_parameter_calculation(0, 0, 0, 'A4', scale)
        print(scale)
    print(center_data)

    DID = (gvar.catia_save[k]+".CATPart")
    draft.add_drafting_infomation(draft_gen_data, 0)
    draft.window_part(center_data, scale/1.5,DID)

    drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height, 0, gvar.catia_save[k])
    wc.close_drafting(gvar.full_save_dir, gvar.catia_save[k], '.CATDrawing')
    wc.part_close()
    print(gvar.catia_save[k]+'_dwg_ok')

# print(gvar.catia_save[0])

# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[2])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height ,0 ,gvar.catia_save[3])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[0])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[1])
#
# catia_save = ['top', 'right', 'following', 'left']
