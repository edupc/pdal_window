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

# # class qweasd() :
# #     def create_window(self):
# #         system_root = os.path.dirname(os.path.realpath(__file__))
# #         gvar.system_root = system_root
# #         # app = QtWidgets.QApplication([])
# #         # window = MainWindow()
# #         # window.show()
# #         # sys.exit(app.exec_())
# #         show_name_1 = ["following.1", 'left.1', 'right.1', 'top.1', 'small_top.1', 'small_left.1', 'small_right.1',
# #                        'small_following.1', 'wheel_1.1', 'wheel_2.1', 'small2_top.1', 'small2_left.1', 'small2_right.1',
# #                        'small2_following.1', 'wheel_3.1', 'wheel_4.1']
# #         show_name_2 = ["following", 'left', 'right', 'top', 'small_top', 'small_left', 'small_right', 'small_following',
# #                        'wheel_1', 'wheel_2', 'small2_top', 'small2_left', 'small2_right', 'small2_following', 'wheel_3',
# #                        'wheel_4']
# #
# #         print(gvar.width, gvar.height)
# #         env = wc.set_CATIA_workbench_env()
# #         env.Generative_Sheetmetal_Design()
# #
# #         wc.part_open("following", gvar.system_root + "\\big_window")
# #         wc.Sideplate_param_change("width", gvar.width_W)
# #         wc.Zoom_view()
# #         wc.part_open("left", gvar.system_root + "\\big_window")
# #         wc.Sideplate_param_change("height", gvar.height_H)
# #         wc.Zoom_view()
# #         wc.part_open("right", gvar.system_root + "\\big_window")
# #         wc.Sideplate_param_change("height", gvar.height_H)
# #         wc.Zoom_view()
# #         wc.part_open("top", gvar.system_root + "\\big_window")
# #         wc.Sideplate_param_change("width", gvar.width_W)
# #         wc.Zoom_view()
# #
# #         if self.route == '':
# #             gvar.full_save_dir = wc.save_dir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
# #         else:
# #             gvar.full_save_dir = wc.save_dir(self.route)
# #         self.full_save_dir = gvar.full_save_dir
# #         print("%s" % self.full_save_dir)
# #         self.catia_save = ['top', 'right', 'following', 'left']
# #         self.small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following', 'wheel_1', 'wheel_2']
# #         self.small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right', 'wheel_3',
# #                                   'wheel_4']  # ,'wheel_1','wheel_2']
# #         self.AL_Window = ['Product1', 'Product2', 'Product3']
# #
# #         self.Product1_Standard = [1, 2, 3, 8, 13, 14, 15, 16, 20]
# #         self.Product2_Standard = [5, 6, 22, 24, 26]
# #         self.Product3_Standard = [4, 7, 23, 25, 27]
# #
# #         for item in self.catia_save:
# #             wc.saveas_close(self.full_save_dir, item, '.CATPart')
# #
# #         for j in self.Product1_Standard:
# #             wc.part_open("Standard_%s" % j, system_root + "\\Standard_window")
# #             wc.saveas_close(self.full_save_dir, "Standard_%s" % j, '.CATPart')
# #             wc.Zoom_view()
# #
# #         wc.open_assembly()
# #
# #         for i in range(0, 4):
# #             print(show_name_2[i])
# #             wc.assembly_open_file(self.full_save_dir, "%s" % show_name_2[i], 0)
# #             wc.saveas_specify_target(self.full_save_dir, "%s" % show_name_2[i], 'CATPart')
# #         for k in range(0, 4):
# #             print(show_name_1[k])
# #             wc.show('%s' % show_name_1[k])
# #
# #         for j in self.Product1_Standard:
# #             wc.assembly_open_file(self.full_save_dir, "Standard_%s" % j, 0)
# #             wc.saveas_specify_target(self.full_save_dir, "Standard_%s" % j, 'CATPart')
# #             wc.Zoom_view()
# #
# #         wc.add_offset_assembly("left", "top", gvar.width_W, "yz plane")  # 偏移組合(零件一,零件二,距離,元素)
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("left", "top", -gvar.height_H + 300, "xy plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("left", "top", 0, "zx plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("right", "top", -gvar.width_W, "yz plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("right", "top", -gvar.height_H + 300, "xy plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("right", "top", 0, "zx plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("following", "top", 0, "yz plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("following", "top", (-2 * gvar.height_H) + 45, "xy plane")
# #         wc.Zoom_view()
# #         wc.add_offset_assembly("following", "top", 0, "zx plane")
# #         wc.Zoom_view()
# #
# #         for i in range(1, 3):
# #             wc.test_3('Product1', 'top', 'Product1', 'Standard_3', 'standard_3_%s' % i, 3)
# #             wc.test_3('Product1', 'top', 'Product1', 'Standard_20', 'standard_20_%s' % i, 3)
# #             wc.test_3('Product1', 'top', 'Product1', 'Standard_8', 'standard_8_%s' % i, 3)
# #             wc.test_3('Product1', 'top', 'Product1', 'Standard_2', 'standard_2_%s' % i, 3)
# #             wc.test_3('Product1', 'following', 'Product1', 'Standard_14', 'Standard_13_%s' % i, 3)
# #             wc.test_3('Product1', 'following', 'Product1', 'Standard_16', 'Standard_15_%s' % i, 3)
# #             wc.test_3('Product1', 'Standard_14', 'Product1', 'Standard_13', 'Standard_14_%s' % i, 3)
# #             wc.test_3('Product1', 'Standard_16', 'Product1', 'Standard_15', 'Standard_16_%s' % i, 3)
# #
# #         wc.test_3('Product1', 'top', 'Product1', 'Standard_2', 'central', 3)
# #         wc.test_3('Product1', 'top', 'Product1', 'Standard_8', 'central', 3)
# #         wc.test_3('Product1', 'top', 'Product1', 'Standard_3', 'standard_3_3', 4)
# #         wc.test_3('Product1', 'top', 'Product1', 'Standard_20', 'standard_20_3', 4)
# #         wc.test_3('Product1', 'following', 'Product1', 'Standard_1', 'Standard_1_1', 3)
# #         wc.test_3('Product1', 'following', 'Product1', 'Standard_1', 'Standard_1_2', 4)
# #         wc.test_3('Product1', 'following', 'Product1', 'Standard_1', 'Standard_1_3', 3)
# #
# #     create_window()
# # time.sleep(1)
# # gvar.width_W = 500
# # gvar.height_H = 500
# # wc.part_open("following", gvar.system_root + "\\big_window")
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.Sideplate_param_change("width", gvar.width_W)
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.part_open("left", gvar.system_root + "\\big_window")
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.Sideplate_param_change("height", gvar.height_H)
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.part_open("right", gvar.system_root + "\\big_window")
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.Sideplate_param_change("height", gvar.height_H)
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.part_open("top", gvar.system_root + "\\big_window")
# # time.sleep(1)
# # wc.Zoom_view()
# # time.sleep(1)
# # wc.Sideplate_param_change("width", gvar.width_W)
# # time.sleep(1)
# # wc.Zoom_view()


# number_1 = True
# def number(a,b,c):
#
#     if (a + b) < c:
#         number_1 = False
#     elif (a + c) < b:
#         number_1 = False
#     elif (b + c) < a:
#         number_1 = False
#     else:
#         number_1 = True
#     if number_1 == True:
#         print('yes')
#     else:
#         print('no')
#
# a = int(input('a：'))
# b = int(input('b：'))
# c = int(input('c：'))
#
# if a<+c and b<a+c and c<a+b:
#     if a==b==c:
#         print('等腰且等邊三角形')
#     elif a==b or a==c or b==c:
#         if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#             print('等腰三角形')
#         else:
#             print('等腰三角形')
#     elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
#         print('不是等腰三角形')
#     else:
#         print('不是等腰三角形')10
# else:
#     print('無法構成三角形')
# from math import sqrt
# '''判断n是否为质数'''
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2,int(sqrt(n))+1):
#         if n%i ==0:
#             return False
#     return True
# '''累加n以内的质数，包括n'''
# a = int(input('a：'))123
# def addPrime(n):
#     sumPrime = 0
#     for i in range(n+1): #range(n)就不包括n
#         if isPrime(i):
#             sumPrime += i
#     print(sumPrime)
#
# addPrime(a)
# a = int(input('a：'))
# b=(a//10//10)
# c=(a//10%10)
# d=(a%10)
# if b== c or c==d or d==b :
#     print('重複')
# else:
#     print('數字沒重複')




for k in range(0,4):
    print(gvar.catia_save[k])
    wc.part_open(gvar.catia_save[k], gvar.full_save_dir + "\\AL500500-2022-05-09'14h21m27s'")

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
    wc.close_drafting(gvar.full_save_dir, gvar.catia_save[k], '.CATDrawing')
    wc.part_close()
    print(gvar.catia_save[k]+'_dwg_ok')

# print(gvar.catia_save[0])

# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[2])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height ,0 ,gvar.catia_save[3])
# drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height,0, gvar.catia_save[0])
# drafting_d.dim_output_only(gvar.width, gvar.height, gvar.depth,2)

# catia_save = ['top', 'right', 'following', 'left']
