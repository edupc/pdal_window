import os,sys,win32
# import win32com.client as win32com
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView
import Window_Catia as wc
from bom import Excel_Bom
import globals_var as gvar
import drafting as draft
import drafting_Part as drafting_p
import drafting_Dim as drafting_d
from untitled import Ui_MainWindow, creat,Window_dwg,about
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import win32com.client as win32
from PyQt5.QtGui import *

#---------------------------------------------------------------資料空串列
# window_gen_data = []
# draft_gen_data = []#標題欄輸入值
# bom_gen_data = {}#bom表輸入值
# bom_whd_value = []
# bom_edit = []
#
# def qwe():
# # #     full_save = str("C:\\Users\\PDAL-BM-1\\PycharmProjects\\windows\\Standard_window\\")
# # #     for j in range(1, 29):
# # #         wc.assembly_open_file(full_save, "Standard_%s"% j, 0)
# #     for k in range(1,3):
# #         wc.saveas_specify_target('C:\\Users\\PDAL-BM-1\\Desktop\\', "Product%s" % k,'.Product')
# # qwe()
# # # for k in range(1,3):
# #     wc.saveas_specify_target('C:\\Users\\PDAL-BM-1\\Desktop\\', "Product%s",'.Product')%k
# # gvar.system_root = system_root
# full_save = str("C:\\Users\\PDAL-BM-1\\PycharmProjects\\windows\\Standard_window\\")
# for j in range(1, 29):
#     wc.part_open("Standard_%s" % j, gvar.system_root + "\\Standard_window")
#     wc.saveas_specify_target(gvar.full_save_dir, "Standard_%s" % j, 'CATPart')
#     # wc.assembly_open_file(full_save, "Standard_%s" % j, 0)
#-----------------------------------------------------------------------------------
# a=['catat','asasfa','asfasf']
#
# for i in a :
#     print(i)
# a.clear()
# print(a)
#
# a=['rwere','werwe','ewrewr']
# for i in a :
#     print(i)
# a=['catat','asasfa','asfasf']
# for i in a :
#     print(a)
# print(i)
#
# name=['123','13','12','13','13456']
# for i in range(0,5):
#     print(name[i])
#     print('%s'%name[i])


# show_name=["following.1",'left.1','right.1','top.1','small_top.1','small_left.1','small_right.1','small_following.1',
#         'wheel_1.1','wheel_2.1','small2_top.1','small2_left.1','small2_right.1','small2_following.1','wheel_3.1','wheel_4.1']
# show_name_1 = ["following.1", 'left.1', 'right.1', 'top.1', 'small_top.1', 'small_left.1', 'small_right.1',
#                      'small_following.1','wheel_1.1', 'wheel_2.1', 'small2_top.1', 'small2_left.1', 'small2_right.1',
#                      'small2_following.1', 'wheel_3.1', 'wheel_4.1']
# show_name_2 = ["following", 'left', 'right', 'top', 'small_top', 'small_left', 'small_right','small_following',
#                      'wheel_1', 'wheel_2', 'small2_top', 'small2_left', 'small2_right','small2_following', 'wheel_3',
#                      'wheel_4']
# for k in range(4,10):
#     print(show_name[k])
# # for k in range(0,4):
# #     print(show_name[k])
# for i in range(1,4):
#     print(show_name_2[4])
# wc.test_4('Product1', 'top', 'Product4', 'Standard_20', 'standard_20_3')
# for i in range(1,4,1):
#     wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_4', 'Standard_4_%s' % i, 3)
#     wc.test_3('Product2', 'small_left', 'Product4', 'Standard_5', 'Standard_5-%s' % i, 4)
#     wc.test_3('Product2', 'small_left', 'Product4', 'Standard_6', 'Standard_6_%s' % i, 3)
#     wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_7', 'Standard_7-%s' % i, 3)
#     wc.test_3('Product3', 'small2_right', 'Product4', 'Standard_23', 'Standard_23_%s' % i, 3)
#     wc.test_3('Product3', 'small2_right', 'Product4', 'Standard_25', 'Standard_25_%s' % i, 3)
#     wc.test_3('Product3', 'small2_right', 'Product4', 'Standard_27', 'Standard_27_%s' % i, 3)
#     wc.test_3('Product2', 'small_right', 'Product4', 'Standard_22', 'Standard_22_%s' % i, 3)
#     wc.test_3('Product2', 'small_right', 'Product4', 'Standard_24', 'Standard_24_%s' % i, 3)
#     wc.test_3('Product2', 'small_right', 'Product4', 'Standard_26', 'Standard_26_%s' % i, 3)
# wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_4', 'Standard_4_1', 3)
# wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_4', 'Standard_4_2', 3)
# wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_4', 'Standard_4_3', 4)
# def Fixed():
#     catapp = win32.Dispatch("CATIA.Application")
#     productDocument1 = catapp.ActiveDocument
#     product1 = productDocument1.Product
#     constraints1 = product1.Connections("CATIAConstraints")
#     reference1 = product1.CreateReferenceFromName("Product5/Product1.1/!Product5/Product1.1/")
#     constraint1 = constraints1.AddMonoEltCst(0, reference1)
#     constraint1.Orientation = 0

#---------------------------------------------------------------------------------------------------3DXML
# import time
#
# time.sleep(1)
# mprog.saveas(gvar.full_save_dir, 'Product', '.3dxml')
# print('Saved as 3dxml...')
#---------------------------------------------------------------------------------------------------打包





# Fixed()
# for i in range(1, 4):
#     wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_4', 'Standard_4_%s' % i, 3)
#     wc.test_3('Product3', 'small2_left', 'Product4', 'Standard_7', 'Standard_7-%s' % i, 3)
#     wc.test_3('Product3', 'small2_right', 'Product4', 'Standard_23', 'Standard_23_%s' % i, 3)
#     wc.test_3('Product3', 'small2_right', 'Product4', 'Standard_25', 'Standard_25_%s' % i, 3)
#     wc.test_3('Product3', 'small2_right', 'Product4', 'Standard_27', 'Standard_27_%s' % i, 3)
#
#     wc.test_3('Product2', 'small_left', 'Product4', 'Standard_5', 'Standard_5-%s' % i, 4)
#     wc.test_3('Product2', 'small_left', 'Product4', 'Standard_6', 'Standard_6_%s' % i, 3)
#     wc.test_3('Product2', 'small_right', 'Product4', 'Standard_22', 'Standard_22_%s' % i, 3)
#     wc.test_3('Product2', 'small_right', 'Product4', 'Standard_24', 'Standard_24_%s' % i, 3)
#     wc.test_3('Product2', 'small_right', 'Product4', 'Standard_26', 'Standard_26_%s' % i, 3)
#
# for i in range(1, 3):
#     wc.test_3('Product1', 'top', 'Product4', 'Standard_3', 'standard_3_%s' % i, 3)
#     wc.test_3('Product1', 'top', 'Product4', 'Standard_20', 'standard_20_%s' % i, 3)
#     wc.test_3('Product1', 'top', 'Product4', 'Standard_8', 'standard_8_%s' % i, 3)
#     wc.test_3('Product1', 'top', 'Product4', 'Standard_2', 'standard_2_%s' % i, 3)
#     wc.test_3('Product1', 'following', 'Product4', 'Standard_14', 'Standard_13_%s' % i, 3)
#     wc.test_3('Product1', 'following', 'Product4', 'Standard_16', 'Standard_15_%s' % i, 3)
#     wc.test_3('Product4', 'Standard_14', 'Product4', 'Standard_13', 'Standard_14_%s' % i, 3)
#     wc.test_3('Product4', 'Standard_16', 'Product4', 'Standard_15', 'Standard_16_%s' % i, 3)
#
# wc.test_3('Product1', 'top', 'Product4', 'Standard_2', 'central', 3)
# wc.test_3('Product1', 'top', 'Product4', 'Standard_8', 'central', 3)
# wc.test_3('Product1', 'top', 'Product4', 'Standard_3', 'standard_3_3', 4)
# wc.test_3('Product1', 'top', 'Product4', 'Standard_20', 'standard_20_3', 4)
# wc.test_3('Product1', 'following', 'Product4', 'Standard_1', 'Standard_1_1', 3)
# wc.test_3('Product1', 'following', 'Product4', 'Standard_1', 'Standard_1_2', 4)
# wc.test_3('Product1', 'following', 'Product4', 'Standard_1', 'Standard_1_3', 3)
# print('Saved as CATProduct...END')
#

def show_off_product():
    for i in range(1,10):
        catapp = win32.Dispatch("CATIA.Application")
        productDocument1 = catapp.ActiveDocument
        selection1 = productDocument1.Selection
        visPropertySet1 = selection1.VisProperties
        documents1 = catapp.Documents
        productDocument2 = documents1.Item("Product1.CATProduct")
        product1 = productDocument2.Product
        constraints1 = product1.Connections("CATIAConstraints")
        constraint1 = constraints1.Item("Offset.%s" % i)
        selection1.Add(constraint1)
        visPropertySet1 = visPropertySet1.Parent
        bSTR1 = visPropertySet1.Name
        bSTR2 = visPropertySet1.Name
        visPropertySet1.SetShow(1)
        selection1.Clear()
    for j in range(10, 33):
        selection2 = productDocument1.Selection
        visPropertySet2 = selection2.VisProperties
        constraint2 = constraints1.Item("Coincidence.%s" % j)
        selection2.Add(constraint2)
        visPropertySet2 = visPropertySet2.Parent
        bSTR3 = visPropertySet2.Name
        bSTR4 = visPropertySet2.Name
        visPropertySet2.SetShow(1)
        selection2.Clear()


    for i in range(1,14):
        selection3 = productDocument1.Selection
        visPropertySet3 = selection3.VisProperties
        productDocument3 = documents1.Item("Product2.CATProduct")
        product2 = productDocument3.Product
        constraints2 = product2.Connections("CATIAConstraints")
        constraint3 = constraints2.Item("Offset.%s" % i)
        selection3.Add(constraint3)
        visPropertySet3 = visPropertySet3.Parent
        bSTR5 = visPropertySet3.Name
        bSTR6 = visPropertySet3.Name
        visPropertySet3.SetShow(1)
        selection3.Clear()
    for j in range(14, 29):
        selection4 = productDocument1.Selection
        visPropertySet4 = selection4.VisProperties
        constraint4 = constraints2.Item("Coincidence.%s" % j)
        selection4.Add(constraint4)
        visPropertySet4 = visPropertySet4.Parent
        bSTR7 = visPropertySet4.Name
        bSTR8 = visPropertySet4.Name
        visPropertySet4.SetShow(1)
        selection4.Clear()


    for i in range(1,14):
        selection5 = productDocument1.Selection
        visPropertySet5 = selection5.VisProperties
        productDocument4 = documents1.Item("Product3.CATProduct")
        product3 = productDocument4.Product
        constraints3 = product3.Connections("CATIAConstraints")
        constraint5 = constraints3.Item("Offset.%s" % i)
        selection5.Add(constraint5)
        visPropertySet5 = visPropertySet5.Parent
        bSTR9 = visPropertySet5.Name
        bSTR10 = visPropertySet5.Name
        visPropertySet5.SetShow(1)
        selection5.Clear()

    for j in range(14, 29):
        selection6 = productDocument1.Selection
        visPropertySet6 = selection6.VisProperties
        constraint6 = constraints3.Item("Coincidence.%s" % j)
        selection6.Add(constraint6)
        visPropertySet6 = visPropertySet6.Parent
        bSTR11 = visPropertySet6.Name
        bSTR12 = visPropertySet6.Name
        visPropertySet6.SetShow(1)
        selection6.Clear()

    for i in range(2,8):
        catapp = win32.Dispatch("CATIA.Application")
        productDocument1 = catapp.ActiveDocument
        selection1 = productDocument1.Selection
        visPropertySet1 = selection1.VisProperties
        product1 = productDocument1.Product
        constraints1 = product1.Connections("CATIAConstraints")
        constraint1 = constraints1.Item("Coincidence.%s" % i)
        selection1.Add(constraint1)
        visPropertySet1 = visPropertySet1.Parent
        bSTR1 = visPropertySet1.Name
        bSTR2 = visPropertySet1.Name
        visPropertySet1.SetShow(1)
        selection1.Clear()
show_off_product()
# def qwe():
#     for i in range(1,7):
#         catapp = win32.Dispatch("CATIA.Application")
#         productDocument1 = catapp.ActiveDocument
#         selection1 = productDocument1.Selection
#         visPropertySet1 = selection1.VisProperties
#         product1 = productDocument1.Product
#         constraints1 = product1.Connections("CATIAConstraints")
#         constraint1 = constraints1.Item("Coincidence.%s" % i)
#         selection1.Add(constraint1)
#         visPropertySet1 = visPropertySet1.Parent
#         bSTR1 = visPropertySet1.Name
#         bSTR2 = visPropertySet1.Name
#         visPropertySet1.SetShow(1)
#         selection1.Clear()
# qwe()