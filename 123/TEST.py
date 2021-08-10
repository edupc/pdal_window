import os
import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QApplication

import Window_Catia as wc
import globals_var as gvar
from untitled import Ui_MainWindow, creat, about

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # 在這裏的是系統開啟會重新re過一次的動作
    def __init__(self):
        super(MainWindow, self).__init__
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_setup.clicked.connect(self.open)
        self.ui.pushButton_start.clicked.connect(self.create_window)
        self.ui.label.setPixmap(QtGui.QPixmap(BASE_DIR + "\\test.jpg"))
        self.ui.label.setScaledContents(True)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + "\\icon.ico"))
        self.ui.pushButton_route.clicked.connect(self.save_file_root)
        self.ui.pushButton_catiastart.clicked.connect(wc.start_CATIA)
        self.ui.pushButton_about.clicked.connect(self.open_about)
        self.ui.pushButton_close_all.clicked.connect(self.Close)
        self.route = ''

    # 關閉量測介面
    def Close(self):
        # self.close()
        self.reply = QMessageBox.question(self, "警示", "確定離開本系統?\nAre you sure you want to close?", QMessageBox.Yes, QMessageBox.No)
        if self.reply == QMessageBox.Yes:
            self.close()
        elif self.reply == QMessageBox.No:
            pass


    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.reply = QMessageBox.question(self, "警示", "確定離開本系統?\nAre you sure you want to close?", QMessageBox.Yes, QMessageBox.No)
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

    #儲存路徑
    def save_file_root(self):
        #directory 變數名稱
        self.route = QtWidgets.QFileDialog.getExistingDirectory(None, "選取資料夾")
        self.ui.lineEdit_file_root.setText(self.route)

    #catia執行檔
    def create_window(self):
        print(gvar.width, gvar.height)
        self.env = wc.set_CATIA_workbench_env()
        self.env.Generative_Sheetmetal_Design()
        wc.part_open("following", system_root+"\\big_window")
        wc.Sideplate_param_change("width", gvar.width)
        wc.part_open("left", system_root+"\\big_window")
        wc.Sideplate_param_change("height", gvar.height)
        wc.part_open("right", system_root+"\\big_window")
        wc.Sideplate_param_change("height", gvar.height)
        wc.part_open("top", system_root+"\\big_window")
        wc.Sideplate_param_change("width", gvar.width)
        print(self.route)
        if self.route == '':
            gvar.full_save_dir = wc.save_dir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        else:
            gvar.full_save_dir = wc.save_dir(self.route)
        self.full_save_dir = gvar.full_save_dir
        print("%s" % self.full_save_dir)
        self.catia_save = ['top', 'right', 'following', 'left']
        self.small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following','wheel_1','wheel_2']
        self.small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right','wheel_3','wheel_4']#,'wheel_1','wheel_2']
        self.AL_Window = ['Product','Product1','Product2']
        for item in self.catia_save:
            wc.saveas_close(self.full_save_dir, item, '.CATPart')
        wc.open_assembly()
        wc.assembly_open_file(self.full_save_dir, "following", 0)
        wc.assembly_open_file(self.full_save_dir, "left", 0)
        wc.assembly_open_file(self.full_save_dir, "right", 0)
        wc.assembly_open_file(self.full_save_dir, "top", 0)
        wc.saveas_specify_target(self.full_save_dir,"following",'CATPart')
        wc.saveas_specify_target(self.full_save_dir,"left",'CATPart')
        wc.saveas_specify_target(self.full_save_dir,"right",'CATPart')
        wc.saveas_specify_target(self.full_save_dir,"top",'CATPart')
        wc.show("following.1")
        wc.show("left.1")
        wc.show("right.1")
        wc.show("top.1")
        wc.add_offset_assembly("left", "top", gvar.width/2, "yz plane")  # 偏移組合(零件一,零件二,距離,元素)
        wc.add_offset_assembly("left", "top", -gvar.height/2 + 300, "xy plane")
        wc.add_offset_assembly("left", "top", 0, "zx plane")
        wc.add_offset_assembly("right", "top", -gvar.width/2, "yz plane")
        wc.add_offset_assembly("right", "top", -gvar.height/2 + 300, "xy plane")
        wc.add_offset_assembly("right", "top", 0, "zx plane")
        wc.add_offset_assembly("following", "top", 0, "yz plane")
        wc.add_offset_assembly("following", "top", (-gvar.height) + 45, "xy plane")
        wc.add_offset_assembly("following", "top", 0, "zx plane")
        # wc.saveas(self.full_save_dir, 'Product', '.CATProduct')
        # print('Saved as CATProduct...')

        # -------------------------------------------------------------------------------------------------------2

        wc.part_open("small_top", system_root + "\\smalll_window")
        wc.Sideplate_param_change("height", gvar.small_width/2)  # 172.5
        wc.part_open("small_left", system_root + "\\smalll_window")
        wc.Sideplate_param_change("width", gvar.small_height)  # 255
        wc.part_open("small_right", system_root + "\\smalll_window")
        wc.Sideplate_param_change("width", gvar.small_height)  # 255
        wc.part_open("small_following", system_root + "\\smalll_window")
        wc.Sideplate_param_change("height", gvar.small_width/2)  # 172.5
        wc.part_open("wheel_1", system_root + "\\smalll_window")
        wc.part_open("wheel_2", system_root + "\\smalll_window")
        print("%s" % self.full_save_dir)
        for item in self.small_catia_save:
            wc.saveas_close(self.full_save_dir, item, '.CATPart')
        wc.open_assembly()
        wc.assembly_open_file(self.full_save_dir, "small_top", 0)
        wc.assembly_open_file(self.full_save_dir, "small_left", 0)
        wc.assembly_open_file(self.full_save_dir, "small_right", 0)
        wc.assembly_open_file(self.full_save_dir, "small_following", 0)
        wc.assembly_open_file(self.full_save_dir, "wheel_1", 0)
        wc.assembly_open_file(self.full_save_dir, "wheel_2", 0)
        wc.saveas_specify_target(self.full_save_dir, "small_top", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "small_left", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "small_right", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "small_following", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "wheel_1", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "wheel_2", 'CATPart')
        wc.show("small_top.1")#small_top
        wc.show("small_left.1")#small_left
        wc.show("small_right.1")#small_right
        wc.show("small_following.1")#small_following
        wc.show("wheel_1.1")
        wc.show("wheel_2.1")
        wc.add_offset_assembly("small_top", "small_following", (-gvar.small_height+50),
                            "xy plane")  # 偏移組合(零件一,零件二,距離,元素)
        wc.add_offset_assembly("small_top", "small_following", 0, "yz plane")
        wc.add_offset_assembly("small_top", "small_following", 0, "zx plane")
        wc.add_offset_assembly("small_following", "small_left", gvar.small_width/4, "yz plane")  # 變數.一半的h
        wc.add_offset_assembly("small_following", "small_left", gvar.small_height/2, "xy plane")  # 變數.w-12.69
        wc.add_offset_assembly("small_following", "small_left", 0, "zx plane")
        wc.add_offset_assembly("small_left", "small_right", -gvar.small_width/2, "yz plane")  # 變數
        wc.add_offset_assembly("small_left", "small_right", 0, "xy plane")
        wc.add_offset_assembly("small_left", "small_right", 0, "zx plane")
        wc.add_offset_assembly('wheel_1','small_following',0,'top_Point2')
        wc.add_offset_assembly('wheel_1','small_following',0,'Plane_wheel_B')
        wc.add_offset_assembly('wheel_2', 'small_following', 0, 'top_Point3')
        wc.add_offset_assembly('wheel_2', 'small_following', 0, 'Plane_wheel_B')
        # wc.saveas(self.full_save_dir, 'Product1', '.CATProduct')
        # print('Saved as CATProduct...')

# -------------------------------------------------------------------------------------------------------3

        wc.part_open("small2_following", system_root + "\\small2_window")
        wc.Sideplate_param_change("height", gvar.small_width/2)  # height343
        wc.part_open("small2_left", system_root + "\\small2_window")
        wc.Sideplate_param_change("width", gvar.small_height)  # width267.5
        wc.part_open("small2_top", system_root + "\\small2_window")
        wc.Sideplate_param_change("height", gvar.small2_width/2)  # height343
        wc.part_open("small2_right", system_root + "\\small2_window")
        wc.Sideplate_param_change("width", gvar.small_height)  # width267.5
        wc.part_open("wheel_3", system_root + "\\small2_window")
        wc.part_open("wheel_4", system_root + "\\small2_window")
        print("%s" % self.full_save_dir)
        for item in self.small2_catia_save:
            wc.saveas_close(self.full_save_dir, item, '.CATPart')
        wc.open_assembly()
        wc.assembly_open_file(self.full_save_dir, "small2_following", 0)
        wc.assembly_open_file(self.full_save_dir, "small2_left", 0)
        wc.assembly_open_file(self.full_save_dir, "small2_top", 0)
        wc.assembly_open_file(self.full_save_dir, "small2_right", 0)
        wc.assembly_open_file(self.full_save_dir, "wheel_3", 0)
        wc.assembly_open_file(self.full_save_dir, "wheel_4", 0)
        wc.saveas_specify_target(self.full_save_dir, "small2_following", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "small2_left", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "small2_top", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "small2_right", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "wheel_3", 'CATPart')
        wc.saveas_specify_target(self.full_save_dir, "wheel_4", 'CATPart')
        wc.show("small2_following.1")  # small2_following
        wc.show("small2_left.1")  # small2_left
        wc.show("small2_top.1")  # small2_top
        wc.show("small2_right.1")  # small2_right
        wc.show("wheel_3.1")
        wc.show("wheel_4.1")
        wc.add_offset_assembly("small2_top", "small2_following", -gvar.small_height+50, "xy plane")  # 變數.
        wc.add_offset_assembly("small2_following", "small2_top", 0, "yz plane")
        wc.add_offset_assembly("small2_following", "small2_top", 0, "zx plane")
        wc.add_offset_assembly("small2_left", "small2_following", gvar.small2_width/4, "yz plane")  # 變數.
        wc.add_offset_assembly("small2_left", "small2_following", -gvar.small_height/2, "xy plane")  # 變數.
        wc.add_offset_assembly("small2_left", "small2_following", 0, "zx plane")
        wc.add_offset_assembly("small2_right", "small2_following", -gvar.small2_width/4, "yz plane")  # 變數.
        wc.add_offset_assembly("small2_right", "small2_following", -gvar.small_height/2, "xy plane")
        wc.add_offset_assembly("small2_right", "small2_following", 0, "zx plane")
        wc.add_offset_assembly('wheel_3', 'small2_following', 0, 'top_Point2')
        wc.add_offset_assembly('wheel_3', 'small2_following', 0, 'Plane_wheel_A')
        wc.add_offset_assembly('wheel_4', 'small2_following', 0, 'top_Point3')
        wc.add_offset_assembly('wheel_4', 'small2_following', 0, 'Plane_wheel_A')
        # wc.saveas(self.full_save_dir, 'Product2', '.CATProduct')
        # print('Saved as CATProduct...')

        for item in self.AL_Window:
            wc.saveas_close(self.full_save_dir, item, '.CATProduct')
#-------------------------------------------------------------------------------------------------------組合

        wc.open_assembly()
        wc.assembly_open_file(self.full_save_dir, "Product", 1)
        wc.assembly_open_file(self.full_save_dir, "Product1", 1)
        wc.assembly_open_file(self.full_save_dir, "Product2", 1)
        wc.show_p("Product1.1", "following.1")
        wc.show_p('Product1.1','left.1')
        wc.show_p('Product1.1','right.1')
        wc.show_p('Product1.1','top.1')
        wc.show_p('Product2.1','small_top.1')
        wc.show_p('Product2.1','small_left.1')
        wc.show_p('Product2.1','small_right.1')
        wc.show_p('Product2.1','small_following.1')
        wc.show_p('Product2.1','wheel_1.1')
        wc.show_p('Product2.1','wheel_2.1')
        wc.show_p('Product3.1','small2_top.1')
        wc.show_p('Product3.1','small2_left.1')
        wc.show_p('Product3.1','small2_right.1')
        wc.show_p('Product3.1','small2_following.1')
        wc.show_p('Product3.1','wheel_3.1')
        wc.show_p('Product3.1','wheel_4.1')
        wc.test_2('Product3','small2_left','Product2','small_left','Plane_Product_ZY')
        wc.test_2('Product1','top','Product3','small2_following','Plane_wheel_A')
        wc.test_2('Product2','small_following','Product1','top','Plane_wheel_B')
        wc.test_2('Product1','top','Product2','wheel_1','Plane_end_B')
        wc.test_2('Product1','top','Product3','wheel_3','Plane_end_A')
        wc.test_2('Product1','left','Product2','small_right','Plane_set_end')
        wc.saveas(self.full_save_dir, 'AL_Window', '.CATProduct')
        print('Saved as CATProduct...END')


    # 開啟關於設定參數介面
    def open(self):
        self.hide()#隱藏
        self.window = Create()
        self.window.show()

    #開啟關於
    def open_about(self):
        self.hide()  # 隱藏
        self.window = About()
        self.window.show()





class Create(QtWidgets.QMainWindow, creat):

    #在這裏的是系統開啟會重新re過一次的動作
    def __init__(self):
        super(Create, self).__init__()#繼承
        self.ui = creat()
        self.ui.setupUi(self)
        self.ui.pushButton_setup.clicked.connect(self.set_ok)
        self.ui.pushButton__restset.clicked.connect(self.reset)
        self.ui.pushButton_close.clicked.connect(self.close)
        self.setWindowIcon(QtGui.QIcon(BASE_DIR + "\\icon.ico"))
        #--------------圖片
        self.ui.label_image.setPixmap(QtGui.QPixmap(BASE_DIR+'\\window_test_image'))
        #--------------根據框框大小縮放圖片
        self.ui.label_image.setScaledContents(True)
        # self.ui.pushButton_setup.clicked.connect(self.set_ok)

    #設定設定完成提示框(yes or no)
    def set_ok(self):
        if self.ui.lineEdit_width.text() != '' and self.ui.lineEdit_height.text() != '':
            gvar.width = float(self.ui.lineEdit_width.text())
            gvar.height = float(self.ui.lineEdit_height.text())
            gvar.small_width = float(self.ui.lineEdit_width.text())
            gvar.small_height = float(self.ui.lineEdit_height.text())
            gvar.small2_width = float(self.ui.lineEdit_width.text())
            self.reply = QMessageBox.question(self, "提示", "設定完成\nSet Ok", QMessageBox.Yes, QMessageBox.No)
            if self.reply == QMessageBox.Yes:
                self.hide()
                self.window = MainWindow()
                self.window.show()
                # QtWidgets.QCloseEvent.ignore()
        else:
            self.reply = QMessageBox.question(self, "錯誤", "設定未完成", QMessageBox.Yes)


    def close(self):
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.hide()
        self.window = MainWindow()
        self.window.show()

    def reset(self):
        self.ui.lineEdit_width.setText('')
        self.ui.lineEdit_height.setText('')

#about介面
class About(QtWidgets.QMainWindow, about):
    def __init__(self):
        super(About, self).__init__()#繼承
        self.ui = about()
        self.ui.setupUi(self)
#執行
if __name__ == '__main__' :
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    system_root = os.path.dirname(os.path.realpath(__file__))
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())