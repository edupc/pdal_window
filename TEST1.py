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

# draft_gen_data = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
# window_gen_data = []
# bom_whd_value = []
# draft.add_drafting_infomation(draft_gen_data, 0)
#
# window_gen_data.append(gvar.width)
# window_gen_data.append(gvar.height)
# window_gen_data.append(gvar.depth)
# for i in range(0, 3):
#     bom_whd_value.append(int(window_gen_data[i]))
# rescale_flag = True
# scale = 2
# while rescale_flag is True:  # checking if scale recalibration is needed
#     scale = scale + 1
#     [center_data, scale, rescale_flag] = drafting_p.projection_parameter_calculation(0, 0, 0, 'A4', scale)
#     print(scale)
# print(center_data)
#
# # -----------------------------------------------------------------------------------------------------BIG_windows
# for k in range(0,4):
#     wc.part_open(gvar.catia_save[k], gvar.full_save_dir + "\\AL500500-2022-05-16'20h10m26s'")
#     DID = (gvar.catia_save[k]+".CATPart")
#     draft.add_drafting_infomation(draft_gen_data, 0)
#     draft.window_part(center_data, scale/1.5,DID)
#     drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height, 0, gvar.catia_save[k])
#     wc.close_drafting(gvar.full_save_dir, gvar.catia_save[k], '.CATDrawing')
#     wc.part_close()
#
# # -----------------------------------------------------------------------------------------------------small_catia
# #
# for k in range(0, 4):
#     if int(k) == 0:
#         scale = scale - 6
#     elif int(k) == 1:
#         scale = scale-2
#     elif int(k) == 2:
#         scale = scale-2
#     elif int(k) == 3:
#         scale = scale - 6
#     wc.part_open(gvar.small_catia_save[k], gvar.full_save_dir + "\\AL500500-2022-05-16'20h10m26s'")
#     DID = (gvar.small_catia_save[k] + ".CATPart")
#     draft.add_drafting_infomation(draft_gen_data, 0)
#     draft.window_part(center_data, scale / 1.5, DID)
#     drafting_d.model_unfolded_view_part('front', gvar.width - 76.49, gvar.height / 2 - 49, 0, gvar.small_catia_save[k])
#     wc.close_drafting(gvar.full_save_dir, gvar.small_catia_save[k], '.CATDrawing')
#     wc.part_close()
#     if k == 0:
#         scale = scale +6
#     elif k == 1:
#         scale = scale +2
#     elif k == 2:
#         scale = scale +2
#     elif k == 3:
#         scale = scale +6
#
# # -----------------------------------------------------------------------------------------------------small2_catia
# for k in range(0, 4):
#     if int(k) == 0:
#         scale = scale - 6
#     elif int(k) == 1:
#         scale = scale - 2
#     elif int(k) == 2:
#         scale = scale - 6
#     elif int(k) == 3:
#         scale = scale - 2
#     wc.part_open(gvar.small2_catia_save[k], gvar.full_save_dir + "\\AL500500-2022-05-16'21h14m20s'")
#     DID = (gvar.small2_catia_save[k] + ".CATPart")
#     draft.add_drafting_infomation(draft_gen_data, 0)
#     draft.window_part(center_data, scale / 1.5, DID)
#     drafting_d.model_unfolded_view_part('front', gvar.width - 76.49, gvar.height / 2 - 49, 0, gvar.small2_catia_save[k])
#     wc.close_drafting(gvar.full_save_dir, gvar.small2_catia_save[k], '.CATDrawing')
#     wc.part_close()
#     if k == 0:
#         scale = scale + 6
#     elif k == 1:
#         scale = scale + 2
#     elif k == 2:
#         scale = scale + 6
#     elif k == 3:
#         scale = scale + 2
# print("DWG_finished")

# -----------------------------------------------------------------------------------------------------test

# wc.part_open(gvar.small2_catia_save[0], gvar.full_save_dir + "\\AL500500-2022-05-16'21h14m20s'")
# DID = (gvar.small2_catia_save[0]+".CATPart")
# draft.add_drafting_infomation(draft_gen_data, 0)
# draft.window_part(center_data, scale / 1.5, DID)
# drafting_d.model_unfolded_view_part('front', gvar.width- 76.49, gvar.height/ 2 - 49, 0, gvar.small2_catia_save[0])

# print(gvar.catia_save[0])

# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[2])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height ,0 ,gvar.catia_save[3])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[0])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[1])
#
# catia_save = ['top', 'right', 'following', 'left']


# -----------------------------------------------------------------------------------------------------BIG_windows
# for k in range(0,4):
#     print(gvar.catia_save[k])
#     wc.part_open(gvar.catia_save[k], gvar.full_save_dir + "\\AL500500-2022-05-11'17h40m27s'")
#
#     draft_gen_data = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
#     window_gen_data = []
#     bom_whd_value = []
#     draft.add_drafting_infomation(draft_gen_data, 0)
#
#     window_gen_data.append(gvar.width)
#     window_gen_data.append(gvar.height)
#     window_gen_data.append(gvar.depth)
#     for i in range(0, 3):
#         bom_whd_value.append(int(window_gen_data[i]))
#     print(bom_whd_value)
#     rescale_flag = True
#     scale = 1
#     while rescale_flag is True:  # checking if scale recalibration is needed
#         scale = scale + 1
#         [center_data, scale, rescale_flag] = drafting_p.projection_parameter_calculation(0, 0, 0, 'A4', scale)
#         print(scale)
#     print(center_data)
#
#     DID = (gvar.catia_save[k]+".CATPart")
#     draft.add_drafting_infomation(draft_gen_data, 0)
#     draft.window_part(center_data, scale/1.5,DID)
#
#     drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height, 0, gvar.catia_save[k])
#     wc.close_drafting(gvar.full_save_dir, gvar.catia_save[k], '.CATDrawing')
#     wc.part_close()
#     print(gvar.catia_save[k]+'_dwg_ok')

# small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following']  # 名稱再來修訂吧3457 小玻璃架
#
# small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right']
# for k in range(0,3):
#     wc.closes(gvar.full_save_dir,gvar.AL_Window_name[k],".CATDrawing")

# wc.closes(gvar.full_save_dir,gvar.AL_Window_name[3],".CATDrawing")

# wc.CATIA_ERR()
# wc.clear_all_windows()

import time
from tqdm import tqdm
for i in tqdm(range(100)):
    time.sleep(0.05)