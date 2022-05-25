import os, sys, win32

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QAbstractItemView
import Window_Catia as wc
import globals_var as gvar
import drafting as draft
import drafting_Part as drafting_p
import drafting_Dim as drafting_d
from untitled import Ui_MainWindow, creat, Window_dwg, about
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import bom

# ---------------------------------------------------------------資料空串列
window_gen_data = []
draft_gen_data = []  # 標題欄輸入值
bom_gen_data = {}  # bom表輸入值
bom_whd_value = []
bom_edit = []


# 主介面
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # 在這裏的是系統開啟會重新re過一次的動作
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_setup.clicked.connect(self.open)
        self.ui.pushButton_start.clicked.connect(self.create_window)
        # self.ui.label.setPixmap(QtGui.QPixmap(BASE_DIR + "\\test.jpg"))
        self.ui.label.setScaledContents(True)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + "\\icon.ico"))
        self.ui.pushButton_route.clicked.connect(self.save_file_root)
        self.ui.pushButton_catiastart.clicked.connect(wc.start_CATIA)
        self.ui.pushButton_about.clicked.connect(self.open_about)
        self.ui.pushButton_close_all.clicked.connect(self.Close)
        self.route = ''
        self.ui.pushButton_setup_dwg.clicked.connect(self.open_dwg)
        self.ui.pushButton_start_dwg.clicked.connect(self.create_window_Dwg)
        # print("123")
        # self.ui.pushButton_start_dwg.clicked.connect(self.Dwg_Winddow)

    # 關閉量測介面
    def Close(self):
        self.close()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.reply = QMessageBox.question(self, "警示", "確定離開本系統?\nAre you sure you want to close?", QMessageBox.Yes,
                                          QMessageBox.No)
        if self.reply == QMessageBox.Yes:
            self.close()
        elif self.reply == QMessageBox.No:
            self.window = MainWindow()
            self.window.show()

    # 關閉全系統(強制關閉)
    def onButtonClick(self):
        '''按鈕槽函式封裝'''
        # 獲取訊號傳送物件
        sender = self.sender()
        # 列印訊號傳送物件的文字+列印輸出
        print(sender.text() + '被按下了')
        # 建立QApplication物件並呼叫quit方法
        qApp = QApplication.instance()
        qApp.quit()

    # 儲存路徑
    def save_file_root(self):
        # directory 變數名稱
        self.route = QtWidgets.QFileDialog.getExistingDirectory(None, "選取資料夾")
        self.ui.lineEdit_file_root.setText(self.route)

    # catia圖面執行檔
    def create_window_Dwg(self):

        # wc.clear_all_windows()

        from Window_Catia import set_CATIA_workbench_env
        env = set_CATIA_workbench_env()
        env.Generative_Sheetmetal_Design()

        self.full_save_dir = gvar.full_save_dir
        wc.part_open(gvar.AL_Window_name[0], self.full_save_dir)
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

        draft.window_full_projection_from_template(center_data, scale)  # 連接圖面
        drafting_d.model_unfolded_view('front', gvar.width, gvar.height, gvar.depth)
        drafting_p.insert_picture('front', "Front view")

        drafting_p.pdf_save(gvar.full_save_dir,'A4_Window', 'pdf')

        wc.close_drafting(self.full_save_dir, 'A4_Window', '.CATDrawing')  # 'C:\\Users\\PDAL-BM-1\\Desktop\\test\\'
        # -----------------------------------------------------------------------------------------------------BIG_windows
        for k in range(0, 4):
            wc.part_open(gvar.catia_save[k], self.full_save_dir)
            DID = (gvar.catia_save[k] + ".CATPart")
            draft.add_drafting_infomation(draft_gen_data, 0)
            draft.window_part(center_data, scale / 1.5, DID)
            drafting_d.model_unfolded_view_part('front', gvar.width, gvar.height, 0, gvar.catia_save[k])
            drafting_p.pdf_save(gvar.full_save_dir, gvar.catia_save[k], 'pdf')
            wc.close_drafting(self.full_save_dir, gvar.catia_save[k], '.CATDrawing')
            # drafting_p.pdf_save(gvar.full_save_dir, gvar.catia_save[k], 'pdf')
            wc.part_close()
        # -----------------------------------------------------------------------------------------------------small_catia
        for k in range(0, 4):
            if int(k) == 0:
                scale = scale - 6
            elif int(k) == 1:
                scale = scale - 2
            elif int(k) == 2:
                scale = scale - 2
            elif int(k) == 3:
                scale = scale - 6
            wc.part_open(gvar.small_catia_save[k], self.full_save_dir)
            DID = (gvar.small_catia_save[k] + ".CATPart")
            draft.add_drafting_infomation(draft_gen_data, 0)
            draft.window_part(center_data, scale / 1.5, DID)
            drafting_d.model_unfolded_view_part('front', gvar.width - 76.49, gvar.height / 2 - 49, 0,
                                                gvar.small_catia_save[k])
            drafting_p.pdf_save(gvar.full_save_dir, gvar.small_catia_save[k], 'pdf')
            wc.close_drafting(self.full_save_dir, gvar.small_catia_save[k], '.CATDrawing')

            wc.part_close()
            if k == 0:
                scale = scale + 6
            elif k == 1:
                scale = scale + 2
            elif k == 2:
                scale = scale + 2
            elif k == 3:
                scale = scale + 6
        # -----------------------------------------------------------------------------------------------------small2_catia
        for k in range(0, 4):
            if int(k) == 0:
                scale = scale - 6
            elif int(k) == 1:
                scale = scale - 2
            elif int(k) == 2:
                scale = scale - 6
            elif int(k) == 3:
                scale = scale - 2
            wc.part_open(gvar.small2_catia_save[k], self.full_save_dir)
            DID = (gvar.small2_catia_save[k] + ".CATPart")
            draft.add_drafting_infomation(draft_gen_data, 0)
            draft.window_part(center_data, scale / 1.5, DID)
            drafting_d.model_unfolded_view_part('front', gvar.width - 76.49, gvar.height / 2 - 49, 0,
                                                gvar.small2_catia_save[k])
            drafting_p.pdf_save(gvar.full_save_dir, gvar.small_catia_save[k], 'pdf')
            wc.close_drafting(self.full_save_dir, gvar.small2_catia_save[k], '.CATDrawing')
            # drafting_p.pdf_save(gvar.full_save_dir, gvar.small2_catia_save[k], 'pdf')
            wc.part_close()
            if k == 0:
                scale = scale + 6
            elif k == 1:
                scale = scale + 2
            elif k == 2:
                scale = scale + 6
            elif k == 3:
                scale = scale + 2
        print("DWG_finished")

        # EXCEAL_BOM-------------------------------------------------------------------------------------------------------------
        print(draft_gen_data)
        # Excel_Bom(draft_gen_data)
        # 我沒辦法理解這個QQ
        import bom
        bom.Excel_Bom(draft_gen_data, self.full_save_dir)

    # ------------------------------------------------------------------------------------------------------------------------
    # catia執行檔
    def create_window(self):

        wc.clear_all_windows()
        from Window_Catia import set_CATIA_workbench_env
        env = set_CATIA_workbench_env()
        env.Part_Design()
        env.Product_Assembly()
        show_name_1 = ["following.1", 'left.1', 'right.1', 'top.1', 'small_top.1', 'small_left.1', 'small_right.1',
                       'small_following.1', 'wheel_1.1', 'wheel_2.1', 'small2_top.1', 'small2_left.1', 'small2_right.1',
                       'small2_following.1', 'wheel_3.1', 'wheel_4.1']
        show_name_2 = ["following", 'left', 'right', 'top', 'small_top', 'small_left', 'small_right', 'small_following',
                       'wheel_1', 'wheel_2', 'small2_top', 'small2_left', 'small2_right', 'small2_following', 'wheel_3',
                       'wheel_4']

        print(gvar.width, gvar.height)
        self.env = wc.set_CATIA_workbench_env()
        self.env.Generative_Sheetmetal_Design()

        wc.part_open("following", system_root + "\\big_window")
        wc.Sideplate_param_change("width", gvar.width_W)
        wc.Zoom_view()
        wc.part_open("left", system_root + "\\big_window")
        wc.Sideplate_param_change("height", gvar.height_H)
        wc.Zoom_view()
        wc.part_open("right", system_root + "\\big_window")
        wc.Sideplate_param_change("height", gvar.height_H)
        wc.Zoom_view()
        wc.part_open("top", system_root + "\\big_window")
        wc.Sideplate_param_change("width", gvar.width_W)
        wc.Zoom_view()
        print(self.route)
        if self.route == '':
            gvar.full_save_dir = wc.save_dir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        else:
            gvar.full_save_dir = wc.save_dir(self.route)
        self.full_save_dir = gvar.full_save_dir
        print("%s" % self.full_save_dir)
        self.catia_save = ['top', 'right', 'following', 'left']
        self.small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following', 'wheel_1', 'wheel_2']
        self.small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right', 'wheel_3',
                                  'wheel_4']  # ,'wheel_1','wheel_2']
        self.AL_Window = ['Product1', 'Product2', 'Product3']

        self.Product1_Standard = [1, 2, 3, 8, 13, 14, 15, 16, 20]
        self.Product2_Standard = [5, 6, 22, 24, 26]
        self.Product3_Standard = [4, 7, 23, 25, 27]

        for item in self.catia_save:
            wc.saveas_close(self.full_save_dir, item, '.CATPart')

        for j in self.Product1_Standard:
            wc.part_open("Standard_%s" % j, system_root + "\\Standard_window")
            wc.saveas_close(self.full_save_dir, "Standard_%s" % j, '.CATPart')
            wc.Zoom_view()

        wc.open_assembly()

        for i in range(0, 4):
            print(show_name_2[i])
            wc.assembly_open_file(self.full_save_dir, "%s" % show_name_2[i], 0)
            wc.saveas_specify_target(self.full_save_dir, "%s" % show_name_2[i], 'CATPart')
        for k in range(0, 4):
            print(show_name_1[k])
            wc.show('%s' % show_name_1[k])

        for j in self.Product1_Standard:
            wc.assembly_open_file(self.full_save_dir, "Standard_%s" % j, 0)
            wc.saveas_specify_target(self.full_save_dir, "Standard_%s" % j, 'CATPart')
            wc.Zoom_view()

        wc.add_offset_assembly("left", "top", gvar.width_W, "yz plane")  # 偏移組合(零件一,零件二,距離,元素)
        wc.Zoom_view()
        wc.add_offset_assembly("left", "top", 0, "err plane")
        wc.Zoom_view()
        wc.add_offset_assembly("left", "top", 42.8 + 1.51, "zx plane")
        wc.Zoom_view()
        wc.add_offset_assembly("right", "top", -gvar.width_W, "yz plane")
        wc.Zoom_view()
        wc.add_offset_assembly("right", "top", -gvar.height_H, "xy plane")
        wc.Zoom_view()
        wc.add_offset_assembly("right", "top", 42.8 - 1.49, "zx plane")
        wc.Zoom_view()
        wc.add_offset_assembly("following", "top", 0, "yz plane")
        wc.Zoom_view()
        wc.add_offset_assembly("following", "top", (-2 * gvar.height_H) + 45, "xy plane")
        wc.Zoom_view()
        wc.add_offset_assembly("following", "top", 0, "zx plane")
        wc.Zoom_view()

        for i in range(1, 3):
            wc.test_3('Product1', 'top', 'Product1', 'Standard_3', 'standard_3_%s' % i, 3)
            wc.test_3('Product1', 'top', 'Product1', 'Standard_20', 'standard_20_%s' % i, 3)
            wc.test_3('Product1', 'top', 'Product1', 'Standard_8', 'standard_8_%s' % i, 3)
            wc.test_3('Product1', 'top', 'Product1', 'Standard_2', 'standard_2_%s' % i, 3)
            wc.test_3('Product1', 'following', 'Product1', 'Standard_14', 'Standard_13_%s' % i, 3)
            wc.test_3('Product1', 'following', 'Product1', 'Standard_16', 'Standard_15_%s' % i, 3)
            wc.test_3('Product1', 'Standard_14', 'Product1', 'Standard_13', 'Standard_14_%s' % i, 3)
            wc.test_3('Product1', 'Standard_16', 'Product1', 'Standard_15', 'Standard_16_%s' % i, 3)

        wc.test_3('Product1', 'top', 'Product1', 'Standard_2', 'central', 3)
        wc.test_3('Product1', 'top', 'Product1', 'Standard_8', 'central', 3)
        wc.test_3('Product1', 'top', 'Product1', 'Standard_3', 'standard_3_3', 4)
        wc.test_3('Product1', 'top', 'Product1', 'Standard_20', 'standard_20_3', 4)
        wc.test_3('Product1', 'following', 'Product1', 'Standard_1', 'Standard_1_1', 3)
        wc.test_3('Product1', 'following', 'Product1', 'Standard_1', 'Standard_1_2', 4)
        wc.test_3('Product1', 'following', 'Product1', 'Standard_1', 'Standard_1_3', 3)

        # -------------------------------------------------------------------------------------------------------2

        wc.part_open("small_top", system_root + "\\smalll_window")
        wc.Sideplate_param_change("height", gvar.small_height / 2)  # 172.5
        wc.Zoom_view()
        wc.part_open("small_left", system_root + "\\smalll_window")
        wc.Sideplate_param_change("width", gvar.small_width / 2)  # 255
        wc.Zoom_view()
        wc.part_open("small_right", system_root + "\\smalll_window")
        wc.Sideplate_param_change("width", gvar.small_width / 2)  # 255
        wc.Zoom_view()
        wc.part_open("small_following", system_root + "\\smalll_window")
        wc.Sideplate_param_change("height", gvar.small_height / 2)  # 172.5
        wc.Zoom_view()
        wc.part_open("wheel_1", system_root + "\\smalll_window")
        wc.part_open("wheel_2", system_root + "\\smalll_window")

        print("%s" % self.full_save_dir)

        for item in self.small_catia_save:
            wc.saveas_close(self.full_save_dir, item, '.CATPart')

        for j in self.Product2_Standard:
            wc.part_open("Standard_%s" % j, system_root + "\\Standard_window")
            wc.saveas_close(self.full_save_dir, "Standard_%s" % j, '.CATPart')
            wc.Zoom_view()

        wc.open_assembly()
        for i in range(4, 10):
            wc.assembly_open_file(self.full_save_dir, "%s" % show_name_2[i], 0)
            wc.saveas_specify_target(self.full_save_dir, "%s" % show_name_2[i], 'CATPart')

        for k in range(4, 10):
            print(show_name_1[k])
            wc.show('%s' % show_name_1[k])

        wc.Zoom_view()
        for j in self.Product2_Standard:
            wc.assembly_open_file(self.full_save_dir, "Standard_%s" % j, 0)
            wc.saveas_specify_target(self.full_save_dir, "Standard_%s" % j, 'CATPart')
            wc.Zoom_view()

        wc.add_offset_assembly("small_top", "small_left", 20, "last_plane")  # 偏移組合(零件一,零件二,距離,元素)
        wc.add_offset_assembly("small_top", "small_following", 0, "yz plane")
        wc.add_offset_assembly("small_top", "small_following", 0, "zx plane")
        wc.add_offset_assembly("small_following", "small_left", gvar.small_height / 2, "yz plane")  # 變數.一半的h#-20.8
        wc.add_offset_assembly("small_following", "small_left", -31.905 + 4.225, "xy plane1")  # 變數.w-12.69
        wc.add_offset_assembly("small_following", "small_left", 31.905, "zx plane")
        wc.add_offset_assembly("small_left", "small_right", -gvar.small_height - 10.8, "yz plane")  # 變數#20.8
        wc.add_offset_assembly("small_left", "small_right", 0, "xy plane")
        wc.add_offset_assembly("small_left", "small_right", -21.255, "zx plane")
        wc.add_offset_assembly('wheel_1', 'small_following', 0, 'top_Point2')
        wc.add_offset_assembly('wheel_1', 'small_following', 0, 'Plane_wheel_B')
        wc.add_offset_assembly('wheel_2', 'small_following', 0, 'top_Point3')
        wc.add_offset_assembly('wheel_2', 'small_following', 0, 'Plane_wheel_B')

        for i in range(1, 4):
            wc.test_3('Product2', 'small_left', 'Product2', 'Standard_5', 'Standard_5-%s' % i, 4)
            wc.test_3('Product2', 'small_left', 'Product2', 'Standard_6', 'Standard_6_%s' % i, 3)
            wc.test_3('Product2', 'small_right', 'Product2', 'Standard_22', 'Standard_22_%s' % i, 3)
            wc.test_3('Product2', 'small_right', 'Product2', 'Standard_24', 'Standard_24_%s' % i, 3)
            wc.test_3('Product2', 'small_right', 'Product2', 'Standard_26', 'Standard_26_%s' % i, 3)

        wc.Zoom_view()
        # -------------------------------------------------------------------------------------------------------3

        wc.part_open("small2_following", system_root + "\\small2_window")
        wc.Sideplate_param_change("height", gvar.small_height / 2)  # height343
        wc.Zoom_view()
        wc.part_open("small2_left", system_root + "\\small2_window")
        wc.Sideplate_param_change("width", gvar.small2_width / 2)  # width267.5
        wc.Zoom_view()
        wc.part_open("small2_top", system_root + "\\small2_window")
        wc.Sideplate_param_change("height", gvar.small_height / 2)  # height343
        wc.Zoom_view()
        wc.part_open("small2_right", system_root + "\\small2_window")
        wc.Sideplate_param_change("width", gvar.small2_width / 2)  # width267.5
        wc.Zoom_view()
        wc.part_open("wheel_3", system_root + "\\small2_window")
        wc.part_open("wheel_4", system_root + "\\small2_window")
        print("%s" % self.full_save_dir)

        for item in self.small2_catia_save:
            wc.saveas_close(self.full_save_dir, item, '.CATPart')

        for j in self.Product3_Standard:
            wc.part_open("Standard_%s" % j, system_root + "\\Standard_window")
            wc.saveas_close(self.full_save_dir, "Standard_%s" % j, '.CATPart')

        wc.open_assembly()
        for i in range(10, 16):
            wc.assembly_open_file(self.full_save_dir, "%s" % show_name_2[i], 0)
            wc.saveas_specify_target(self.full_save_dir, "%s" % show_name_2[i], 'CATPart')

        for k in range(10, 16):
            print(show_name_1[k])
            wc.show('%s' % show_name_1[k])

        wc.Zoom_view()
        for j in self.Product3_Standard:
            wc.assembly_open_file(self.full_save_dir, "Standard_%s" % j, 0)
            wc.saveas_specify_target(self.full_save_dir, "Standard_%s" % j, 'CATPart')
            wc.Zoom_view()

        wc.add_offset_assembly("small2_top", "small2_following", -gvar.small2_width + 48, "xy plane")  # 變數.
        wc.add_offset_assembly("small2_following", "small2_top", 0, "yz plane")
        wc.add_offset_assembly("small2_following", "small2_top", 0, "zx plane")
        wc.add_offset_assembly("small2_left", "small2_following", gvar.small_height / 2, "yz plane")  # 變數.
        wc.add_offset_assembly("small2_left", "small2_following", -gvar.small2_width / 2, "xy plane")  # 變數.
        wc.add_offset_assembly("small2_left", "small2_following", -13.45, "zx plane")
        wc.add_offset_assembly("small2_right", "small2_following", -gvar.small_height / 2 - 10.8, "yz plane")  # 變數.
        wc.add_offset_assembly("small2_right", "small2_following", -gvar.small2_width / 2, "xy plane")
        wc.add_offset_assembly("small2_right", "small2_following", 0, "zx plane")
        wc.add_offset_assembly('wheel_3', 'small2_following', 0, 'top_Point2')
        wc.add_offset_assembly('wheel_3', 'small2_following', 0, 'Plane_wheel_A')
        wc.add_offset_assembly('wheel_4', 'small2_following', 0, 'top_Point3')
        wc.add_offset_assembly('wheel_4', 'small2_following', 0, 'Plane_wheel_A')

        for i in range(1, 4):
            wc.test_3('Product3', 'small2_left', 'Product3', 'Standard_4', 'Standard_4_%s' % i, 3)
            wc.test_3('Product3', 'small2_left', 'Product3', 'Standard_7', 'Standard_7-%s' % i, 3)
            wc.test_3('Product3', 'small2_right', 'Product3', 'Standard_23', 'Standard_23_%s' % i, 3)
            wc.test_3('Product3', 'small2_right', 'Product3', 'Standard_25', 'Standard_25_%s' % i, 3)
            wc.test_3('Product3', 'small2_right', 'Product3', 'Standard_27', 'Standard_27_%s' % i, 3)

        wc.Zoom_view()
        for item in self.AL_Window:
            wc.saveas_close(self.full_save_dir, item, '.CATProduct')

        # -------------------------------------------------------------------------------------------------------組合

        wc.open_assembly()
        wc.assembly_open_file(self.full_save_dir, "Product1", 1)
        wc.assembly_open_file(self.full_save_dir, "Product2", 1)
        wc.assembly_open_file(self.full_save_dir, "Product3", 1)

        wc.Fixed()

        wc.Zoom_view()
        for k in range(0, 4):
            print(show_name_1[k])
            wc.show_p("Product1.1", '%s' % show_name_1[k])
        for k in range(4, 10):
            print(show_name_1[k])
            wc.show_p("Product2.1", '%s' % show_name_1[k])
        for k in range(10, 16):
            print(show_name_1[k])
            wc.show_p("Product3.1", '%s' % show_name_1[k])

        wc.test_2('Product3', 'small2_left', 'Product2', 'small_left', 'Plane_Product_ZY')
        wc.test_2('Product1', 'top', 'Product3', 'small2_following', 'Plane_wheel_A')
        wc.test_2('Product2', 'small_following', 'Product1', 'top', 'Plane_wheel_B')
        wc.test_2('Product1', 'top', 'Product2', 'wheel_1', 'Plane_end_B')
        wc.test_2('Product1', 'top', 'Product3', 'wheel_3', 'Plane_end_A')
        wc.test_2('Product1', 'left', 'Product2', 'small_right', 'Plane_set_end')
        # wc.saveas(self.full_save_dir, 'AL_Window', '.CATProduct')

        # -------------------------------------------------------------------------------------------
        wc.Zoom_view()
        wc.show_off_Offset()
        wc.saveas(self.full_save_dir, 'AL_Window', '.CATProduct')
        # wc.closes
        print('Saved as CATProduct...END')
        for k in range(0, 4):
            wc.closes(self.full_save_dir, gvar.AL_Window_name[k], ".CATProduct")

    # CATIA 圖面執行檔
    def Dwg_Winddow(self):
        pass

    # 開啟關於設定參數介面
    def open(self):
        self.hide()  # 隱藏
        self.window = Create()
        self.window.show()

    def open_dwg(self):
        self.hide()  # 隱藏
        self.window = Window_DWG()
        self.window.show()

    # 開啟關於
    def open_about(self):
        self.hide()  # 隱藏
        self.window = About()
        self.window.show()


# Create介面
class Create(QtWidgets.QMainWindow, creat):

    # 在這裏的是系統開啟會重新re過一次的動作
    def __init__(self):
        super(Create, self).__init__()  # 繼承
        self.ui = creat()
        self.ui.setupUi(self)
        self.ui.pushButton_set_up.clicked.connect(self.set_ok)

        self.ui.pushButton_re.clicked.connect(self.reset)
        self.ui.pushButton_cancel.clicked.connect(self.close)
        self.ui.pushButton_set.clicked.connect(self.insert_table)
        self.ui.pushButton_delete.clicked.connect(self.dele)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + "\\icon.ico"))
        # 不能改寫
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 選定一行
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.number = 0
        # 設定表格參數'number'=0(初始化)
        self.ui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # 將右鍵菜單綁定到槽函數generateMenu
        self.ui.tableWidget.customContextMenuRequested.connect(self.generateMenu)
        # self.setLayout(Create)
        # 鎖定H,W欄位之輸入值為數字非英文跟其他符號BUT可中文未修除(有最大上限值)
        self.ui.lineEdit_H.setValidator(QtGui.QIntValidator())
        self.ui.lineEdit_W.setValidator(QtGui.QIntValidator())
        # 表達式$符號看不懂可以刪掉他看看插在哪Quantity欄位輸入，可中文未修除(可以把表格寫爆)
        my_regex = QtCore.QRegExp("[0-9]+$")
        my_validator = QtGui.QRegExpValidator(my_regex, self.ui.lineEdit_Quantity)
        self.ui.lineEdit_Quantity.setValidator(my_validator)
        self.lines = []
        self.ui.lineEdit_color.setStyleSheet("background-color: rgb(156,156,156);")
        self.ui.lineEdit_color.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ui.comboBox.activated[int].connect(self.change_color)
        # --------------圖片
        self.ui.label_window_pic.setPixmap(QtGui.QPixmap(BASE_DIR + '%s' % gvar.color_picture[3]))
        # --------------根據框框大小縮放圖片
        self.ui.label_window_pic.setScaledContents(True)

    def change_color(self, ival):
        ival += 1
        if ival == 1:
            # self.ui.lineEdit_color.setFocusPolicy(QtCore.Qt.NoFocus)
            self.ui.lineEdit_color.setStyleSheet("background-color: rgb(156,156,156);")
            self.ui.label_window_pic.setPixmap(QtGui.QPixmap(BASE_DIR + '%s' % gvar.color_picture[0]))
        elif ival == 2:
            self.ui.lineEdit_color.setStyleSheet("background-color: rgb(139,131,134);")
            self.ui.label_window_pic.setPixmap(QtGui.QPixmap(BASE_DIR + '%s' % gvar.color_picture[1]))
        elif ival == 3:
            self.ui.lineEdit_color.setStyleSheet("background-color: rgb(205,205,180);")
            self.ui.label_window_pic.setPixmap(QtGui.QPixmap(BASE_DIR + '%s' % gvar.color_picture[2]))
        elif ival == 4:
            self.ui.lineEdit_color.setStyleSheet("background-color: rgb(255,255,255);")
            self.ui.label_window_pic.setPixmap(QtGui.QPixmap(BASE_DIR + '%s' % gvar.color_picture[3]))
        elif ival == 5:
            self.ui.lineEdit_color.setStyleSheet("background-color: rgb(0 ,0 ,0);")
            self.ui.label_window_pic.setPixmap(QtGui.QPixmap(BASE_DIR + '%s' % gvar.color_picture[4]))
        print('PyQt5 lineEdit_color change:', ival)

    def insert_table(self):
        if self.ui.lineEdit_W.text() != '' and self.ui.lineEdit_H.text() != '' and self.ui.lineEdit_Quantity.text() != '':
            h = self.ui.lineEdit_H.text()
            w = self.ui.lineEdit_W.text()
            q = self.ui.lineEdit_Quantity.text()
            if int(h) <= 200:
                self.reply = QMessageBox.question(self, "錯誤", "高度數值過小", QMessageBox.Yes)
                print('No_Set_All')
            elif int(h) >= 2000:
                self.reply = QMessageBox.question(self, "錯誤", "高度數值過大", QMessageBox.Yes)
                print('No_Set_All')
            elif int(w) <= 200:
                self.reply = QMessageBox.question(self, "錯誤", "寬度數值過小", QMessageBox.Yes)
                print('No_Set_All')
            elif int(w) >= 2000:
                self.reply = QMessageBox.question(self, "錯誤", "寬度數值過大", QMessageBox.Yes)
                print('No_Set_All')
            elif int(q) == 0 :
                self.reply = QMessageBox.question(self, "錯誤", "數量不可於0", QMessageBox.Yes)
            else:
                type = self.ui.comboBox_type.currentText()
                # 設定參數tape,w,h,q,
                self.set_number()
                if self.measure_check == True:
                    # 抓取參數寫入表格(number,0123)
                    self.ui.tableWidget.setItem(self.number, 0, QTableWidgetItem(type))
                    self.ui.tableWidget.setItem(self.number, 1, QTableWidgetItem(h))
                    self.ui.tableWidget.setItem(self.number, 2, QTableWidgetItem(w))
                    self.ui.tableWidget.setItem(self.number, 3, QTableWidgetItem(q))
                    # 設定輸入文字置中以及上下置中
                    self.ui.tableWidget.item(self.number, 0).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.tableWidget.item(self.number, 1).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.tableWidget.item(self.number, 2).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.tableWidget.item(self.number, 3).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    # 設定執行1次的時候參數+1,和格子增加參數值
                    self.number += 1
                    self.ui.tableWidget.setRowCount(self.number + 1)
                    print(type, w, h, q)
                    print(self.number, self.measure_check)
                elif self.measure_check == False:
                    # 假設格子參數小於0那參數重新寫成0
                    self.number = 0
                    self.ui.tableWidget.setRowCount(self.number + 2)
                    self.ui.tableWidget.setItem(self.number, 0, QTableWidgetItem(type))
                    self.ui.tableWidget.setItem(self.number, 1, QTableWidgetItem(h))
                    self.ui.tableWidget.setItem(self.number, 2, QTableWidgetItem(w))
                    self.ui.tableWidget.setItem(self.number, 3, QTableWidgetItem(q))
                    self.ui.tableWidget.item(self.number, 0).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.tableWidget.item(self.number, 1).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.tableWidget.item(self.number, 2).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.ui.tableWidget.item(self.number, 3).setTextAlignment(
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    self.number = 1
                    print(self.number, self.measure_check)


        elif self.ui.lineEdit_H.text() == '':
            self.reply = QMessageBox.question(self, "錯誤", "高度尚未設定", QMessageBox.Yes)
            print('No_Set_All')
        elif self.ui.lineEdit_W.text() == '':
            self.reply = QMessageBox.question(self, "錯誤", "寬度尚未設定", QMessageBox.Yes)
            print('No_Set_All')
        elif self.ui.lineEdit_Quantity.text() == '':
            self.reply = QMessageBox.question(self, "錯誤", "數量尚未輸入", QMessageBox.Yes)
            print('No_Set_All')

    def generateMenu(self, pos):
        # 計算有多少條數據，默認-1,self.number

        for i in self.ui.tableWidget.selectionModel().selection().indexes():
            self.number = i.row()

        # 表格中只有兩條有效數據，所以只在前兩行支持右鍵彈出菜單
        if self.number < 80:
            menu = QMenu()
            item1 = menu.addAction(u'刪除')
            item2 = menu.addAction(u'表格鎖定解除')
            item3 = menu.addAction(u'表格鎖定')
            action = menu.exec_(self.ui.tableWidget.mapToGlobal(pos))
            # 顯示選中行的數據文本
            if action == item1:
                self.dele()
            if action == item2:
                self.ui.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
            if action == item3:
                self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        else:
            self.number = 0
            pass

    def dele(self):

        self.set_number()
        if self.measure_check == True:
            self.row = self.ui.tableWidget.currentRow()
            print(self.row)
            if self.row == -1:
                self.row = 0
            self.ui.tableWidget.removeRow(self.row)
            self.number -= 1
            print(self.number, self.measure_check)
        elif self.measure_check == False:
            self.reply = QMessageBox.question(self, "提示", "不可再刪除\nDon't dele", QMessageBox.Yes, )
            if self.reply == QMessageBox.Yes:
                print(self.number, self.measure_check)
                # self.measure_check = True
                pass

    def set_number(self):
        if self.number >= 0:
            self.measure_check = True
        elif self.number == -1:
            self.measure_check = False

    # 設定設定完成提示框(yes or no)
    def set_ok(self):
        col_num = self.ui.tableWidget.columnCount()
        print( col_num+1 )
        # print(gvar.table_number)
        if self.ui.lineEdit_W.text() != '' and self.ui.lineEdit_H.text() != '':
            gvar.width = float(self.ui.lineEdit_H.text())  # 這裡W,H寫反，帶修正
            gvar.height = float(self.ui.lineEdit_W.text())  # 這裡W,H寫反，帶修正
            gvar.width_W = float(self.ui.lineEdit_W.text()) / 2 - 13.65
            gvar.height_H = float(self.ui.lineEdit_H.text()) / 2
            gvar.small_height = float(self.ui.lineEdit_W.text()) / 2 - 49
            gvar.small_width = float(self.ui.lineEdit_H.text()) - 76.49
            gvar.small2_width = float(self.ui.lineEdit_H.text()) - 48.19
            gvar.Quantity = float(self.ui.lineEdit_Quantity.text())
            # gvar.color = self.ui.comboBox.itemData()
            intcolor = self.ui.comboBox.currentIndex()
            if intcolor == 0:
                gvar.color ="材料_rey61"
            elif intcolor == 1:
                gvar.color ="材料_LavenderBlush4"
            elif intcolor == 2:
                gvar.color="材料_LightYellow"
            elif intcolor == 3:
                gvar.color="材料_White"
            elif intcolor == 4:
                gvar.color="材料_Black"

            print('ㄏ%s'% gvar.color)
            
            print(gvar.width, gvar.height, gvar.Quantity)
            self.reply = QMessageBox.question(self, "提示", "設定完成\nSet Ok", QMessageBox.Yes, QMessageBox.No)
            if self.reply == QMessageBox.Yes:
                self.hide()
                self.window = MainWindow()
                self.window.show()
                print('Set_Ok')
            elif self.reply == QMessageBox.No:
                pass
                # QtWidgets.QCloseEvent.ignore()
        else:
            self.reply = QMessageBox.question(self, "錯誤", "設定未完成", QMessageBox.Yes)
            print('No_Set_All')

    def close(self):
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def reset(self):
        self.ui.lineEdit_H.setText('500')
        self.ui.lineEdit_W.setText('500')
        self.ui.lineEdit_Quantity.setText('5')
        self.ui.comboBox_type.setCurrentIndex(0)
        self.ui.tableWidget.clearContents()
        self.number = 0
        self.ui.tableWidget.setRowCount(self.number + 1)
        print('Reset_All')

        # self.number = 0
        # self.ui.tableWidget.setRowCount(self.number + 2)
        # self.number = 1
        # item = self.ui.tableWidget.verticalHeaderItem(0)
        # item.setText(self.ui._translate("MainWindow", "1"))
        # self.ui.tableWidget.item(self.number,1).setText('')
        # # self.ui.tableWidget.item(self.number, 2).text('')
        # # self.ui.tableWidget.item(self.number, 3).text('')


# DWG介面
class Window_DWG(QtWidgets.QMainWindow, Window_dwg):
    def __init__(self):
        super(Window_DWG, self).__init__()  # 繼承
        self.ui = Window_dwg()
        self.ui.setupUi(self)
        self.ui.pushButton_set.clicked.connect(self.DWG_set_ok)
        self.ui.pushButton_clear.clicked.connect(self.CLEAR)
        self.ui.pushButton_cancel.clicked.connect(self.Close)

    def CLEAR(self):
        self.ui.lineEdit_1.setText('2021/02/04')
        self.ui.lineEdit_2.setText('%s'%gvar.color)
        self.ui.lineEdit_3.setText('昱瑋')
        self.ui.lineEdit_4.setText('昱瑋')
        self.ui.lineEdit_5.setText('昱瑋')
        self.ui.lineEdit_6.setText('Aluminum')
        self.ui.lineEdit_7.setText('%s' % int(gvar.Quantity))
        self.ui.lineEdit_8.setText('自動化產品設計系統')
        self.ui.lineEdit_9.setText('TEST1')
        self.ui.lineEdit_10.setText('mm')
        self.ui.lineEdit_11.setText('備註:')
        # self.ui.lineEdit_12.setText('')
        # self.ui.lineEdit_13.setText('')
        print('Reset_ALL')

    def Close(self):
        self.hide()
        self.window = MainWindow()
        self.window.show()
        self.ui.pushButton_cancel.clicked.connect(self.Close)

    def DWG_set_ok(self):
        for i in range(0, len(draft_gen_data)):
            del draft_gen_data[-1]
        draft_info = [self.ui.lineEdit_1.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text(),
                      self.ui.lineEdit_4.text(), self.ui.lineEdit_5.text(), self.ui.lineEdit_6.text(),
                      self.ui.lineEdit_7.text(), self.ui.lineEdit_8.text(), self.ui.lineEdit_9.text(),
                      self.ui.lineEdit_10.text(), self.ui.lineEdit_11.text()]
        for i in range(0, len(draft_info)):
            draft_gen_data.append(draft_info[i])

        for j in range(0, len(draft_info)):
            if draft_info[j] == "":
                self.measure_dwg_check = False
            else:
                self.measure_dwg_check = True
        if self.measure_dwg_check == True:
            self.reply = QMessageBox.question(self, "提示", "設定完成\nSet Ok", QMessageBox.Yes, QMessageBox.No)
            if self.reply == QMessageBox.Yes:
                self.hide()
                self.window = MainWindow()
                self.window.show()
                print(draft_gen_data, self.measure_dwg_check, '圖面設定完成')

            elif self.reply == QMessageBox.No:
                print('請設定好您的參數')
                pass
        elif self.measure_dwg_check == False:
            self.reply = QMessageBox.question(self, "提示", "Error\n請完整輸入參數", QMessageBox.Yes, )
            if self.reply == QMessageBox.Yes:
                pass

    def close(self):
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.hide()
        self.window = MainWindow()
        self.window.show()


# about介面
class About(QtWidgets.QMainWindow, about):
    def __init__(self):
        super(About, self).__init__()  # 繼承
        self.ui = about()
        self.ui.setupUi(self)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.hide()
        self.window = MainWindow()
        self.window.show()


# 執行
if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    system_root = os.path.dirname(os.path.realpath(__file__))
    gvar.system_root = system_root
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
