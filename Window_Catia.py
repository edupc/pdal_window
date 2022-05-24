import win32com.client as win32
import datetime, string, os, psutil
import globals_var as gvar
import re
import subprocess
from subprocess import CREATE_NEW_CONSOLE
from datetime import datetime, timezone, timedelta
from PyQt5.QtWidgets import QMessageBox, QApplication


def start_CATIA(self):
    # try to CATIA enviorment file
    env_dir = 'C:\ProgramData\DassaultSystemes\CATEnv'
    list_dir = os.listdir(env_dir)
    print(list_dir)
    if any('V5-6R' in file for file in list_dir):
        for file in list_dir:
            if 'V5-6R' in file:
                env_file = open(env_dir + '\\' + file, 'rt')
                env_line = env_file.read().splitlines()
                for line in env_line:
                    if 'CATInstallPath' in line:
                        CATIA_dir = re.sub('CATInstallPath=', '', line)
                        env_name = re.sub('.txt', '', file)
                        print('get CATIA dir and env is %s , %s' % (CATIA_dir, env_name))

    else:
        self.reply = QMessageBox.question(self, "警示", "catia未完整開啟?\nAre you sure you want to close?", QMessageBox.Yes,
                                          QMessageBox.No)
        # tk.messagebox.showwarning('WARNING', 'No Suitable V5-6R Version CATIA installation found on this machine',
        #                           parent=self.master)

    chk = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'CNEXT' in p.info['name']]
    print(chk)
    if chk == []:
        args = [r"%s\code\bin\CATSTART.exe" % CATIA_dir, "-run", "CNEXT.exe", "-env %s -direnv" % env_name,
                "C:\ProgramData\DassaultSystemes\CATEnv", "-nowindow"]
        print(args)
        request = subprocess.Popen(args, shell=False, creationflags=CREATE_NEW_CONSOLE)
        print(str(request))
        print(os.getpid())
        return False
    else:
        return True


class set_CATIA_workbench_env:
    def __init__(self):
        # self.catapp = win32.Dispatch("CATIA.Application")
        self.env_name = {'Part_Design': 'PrtCfg', 'Product_Assembly': 'Assembly',
                         'Generative_Sheetmetal_Design': 'SmdNewDesignWorkbench', 'Drafting': 'Drw'}
        self.catapp = win32.Dispatch("CATIA.Application")
        # add some CATIA-specific settings here (Seeing CATIA Automation manual-Application section)
        self.catapp.DisplayFileAlerts = False
        self.catapp.Visible = False

    def Part_Design(self):
        self.catapp.Visible = False
        self.catapp.StartWorkbench(self.env_name[self.Part_Design.__name__])
        try:
            temp = self.catapp.ActiveDocument
            temp.close()
        except:
            pass
        return

    def Product_Assembly(self):
        self.catapp.Visible = False
        self.catapp.StartWorkbench(self.env_name[self.Product_Assembly.__name__])
        try:
            temp = self.catapp.ActiveDocument
            temp.close()
        except:
            pass
        return

    def Generative_Sheetmetal_Design(self):
        self.catapp.Visible = False
        self.catapp.StartWorkbench(self.env_name[self.Generative_Sheetmetal_Design.__name__])
        try:
            temp = self.catapp.ActiveDocument
            temp.close()
        except:
            pass
        return

    def Drafting(self):
        self.catapp.Visible = True
        self.catapp.StartWorkbench(self.env_name[self.Drafting.__name__])
        try:
            temp = self.catapp.ActiveDocument
            temp.close()
        except:
            pass
        return


# Part 開啟
def Zoom_view():
    catapp = win32.Dispatch("CATIA.Application")
    specsAndGeomWindow1 = catapp.ActiveWindow
    viewer3D1 = specsAndGeomWindow1.ActiveViewer
    viewer3D1.Reframe()


def part_open(target, dir):
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    try:
        partdoc = document.Open("%s\%s.%s" % (dir, target, "CATPart"))

    except:
        partdoc = document.Open("%s\%s.%s" % (dir, target, "CATProduct"))
    # part = partdoc.Part
    # part.Update()


def Standard_part_open_(target, dir):
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    # try:

    partdoc = document.Open("%s\%s.%s" % (dir, target, "CATPart"))
    # except:
    #     partdoc = document.Open("%s\%s.%s" % (dir,target,"CATProduct"))


# 開啟零件檔案
def file_open(target, dir):
    # 連結CATIA
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    # 將路徑設為目錄的文字宣告
    directory = str(dir)
    # directory = '\\'.join(directory.split('/'))
    print(directory)
    # gvar.folderdir = directory
    # 定義零件檔檔名
    part_dir = directory + target + '.CATPart'
    print(part_dir)
    # partdoc = document.Open("%s%s.%s" % (directory,target,"CATPart"))
    # 開啟該零件檔
    partdoc = document.Open(part_dir)
    return target + '.CATPart'


# 開啟組立檔案
def assembly_open_file(folder, target, type):
    catapp = win32.Dispatch("CATIA.Application")
    productdoc = catapp.ActiveDocument
    product = productdoc.Product
    products = product.Products
    # print(type(gvar.folderdir))
    # print(type(target))
    # directory = '\\'.join(folder.split('/'))
    # 開啟 0為零件檔/1為組立檔 進入該組立檔
    if type == 0:
        filedir = "%s\%s.%s" % (folder, target, "CATPart")
    elif type == 1:
        filedir = "%s\%s.%s" % (folder, target, "CATProduct")
    print(filedir)
    import_file = filedir,
    list(import_file)
    productsvarient = products.AddComponentsFromFiles(import_file, "All")
    return productsvarient


# 改變parameter內的數值
def Sideplate_param_change(target, value):
    catapp = win32.Dispatch("CATIA.Application")
    partdoc = catapp.ActiveDocument
    part = partdoc.Part
    parameter = part.Parameters
    # 按照介面輸入的參數找出相對應的面建出板子
    length = parameter.Item(target)
    if target == "width":
        length.Value = value
    elif target == "depth":
        D_value = float(value) + 14.5
        length.Value = D_value
    elif target == "height":
        length.Value = value
    part.Update()


def open_assembly():
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    productdoc = document.Add("Product")
    product = productdoc.Product
    products = product.Products


# def open_assembly():
#     catapp = win32.Dispatch("CATIA.Application")
#     document = catapp.Documents
#     productdoc = document.Add("Product")
#     product = productdoc.Product
#     products = product.Products


def save_dir(save_dir):
    time_now = datetime.now()
    # 資料夾名稱
    product_name = ('AL%s%s' % (str(int(gvar.width)), str(int(gvar.height))))
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))  # 轉換時區 -> 東八區
    # print(dt2.strftime("%Y-%m-%d'%Hh%Mm%Ss'"))  # 將時間轉換為 string
    print(dt2.strftime("%Y-%m-%d'%Hh%Mm%Ss'"))
    file_name = ("%s-%s" % (product_name, dt2.strftime("%Y-%m-%d'%Hh%Mm%Ss'")))

    try:
        save_dir = '\\'.join(save_dir.split('/'))  # if using GUI to set file_dir
    except:  # if using API call method, which file_dir has benn processed
        pass
    newpath = os.path.join(save_dir, file_name)
    print(newpath)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


def saveas_close(save_dir, target, data_type):
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    # catia 儲存只有組立跟零件，只有兩種可能並結果可預測
    try:
        saveas = document.Item('%s%s' % (target, data_type))
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    except:
        saveas = catapp.ActiveDocument
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    finally:
        saveas.Save()
        # saveas.Close()


def close_drafting(save_dir, target, data_type):
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    # catia 儲存只有組立跟零件，只有兩種可能並結果可預測
    try:
        saveas = document.Item('%s%s' % (target, data_type))
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    except:
        saveas = catapp.ActiveDocument
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    finally:
        saveas.Save()
        saveas.Close()


def open_drafting(save_dir, target):
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = document.Open(r'%s\%s.CATDrawing' % (save_dir, target))
    # drawingdocument = document.Open('C:\\Users\\PDAL-BM-1\\Desktop\\%s\\%s.CATDrawing'%save_dir,target)


def saveas_specify_target(save_dir, target, data_type):
    catapp = win32.Dispatch('CATIA.Application')
    doc = catapp.Documents
    saveas = doc.Item('%s.%s' % (target, data_type))
    saveas.Save()
    saveas.Close()


def saveas(save_dir, target, data_type):
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    try:
        saveas = document.Item('%s%s' % (target, data_type))
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    except:
        saveas = catapp.ActiveDocument
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    finally:
        saveas.Save()


def closes(save_dir, target, data_type):
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    try:
        saveas = document.Item('%s%s' % (target, data_type))
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    except:
        saveas = catapp.ActiveDocument
        saveas.SaveAs('%s\%s%s' % (save_dir, target, data_type))
    finally:
        # saveas.Save()
        saveas.Close()


# 增加偏移拘束
def add_offset_assembly(element1, element2, dist, relation):
    catapp = win32.Dispatch("CATIA.Application")
    productdoc = catapp.ActiveDocument
    product = productdoc.Product
    product = product.ReferenceProduct
    constraints = product.Connections("CATIAConstraints")
    ref1 = product.CreateReferenceFromName("Product1/%s.1/!PartBody/%s" % (element1, relation))
    ref2 = product.CreateReferenceFromName("Product1/%s.1/!PartBody/%s" % (element2, relation))
    # 1表示偏移拘束
    constraint = constraints.AddBiEltCst(1, ref1, ref2)
    length = constraint.Dimension
    length.value = dist
    constraint.Orientation = 0
    product.Update()
    return True


# 隱藏組立線
def show_off_Offset():
    for i in range(1, 10):
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

    for i in range(1, 14):
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

    for i in range(1, 14):
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

    # for i in range(1, 7):
    #     catapp = win32.Dispatch("CATIA.Application")
    #     productDocument1 = catapp.ActiveDocument
    #     selection1 = productDocument1.Selection
    #     visPropertySet1 = selection1.VisProperties
    #     product1 = productDocument1.Product
    #     constraints1 = product1.Connections("CATIAConstraints")
    #     constraint1 = constraints1.Item("Coincidence.%s" % i)
    #     selection1.Add(constraint1)
    #     visPropertySet1 = visPropertySet1.Parent
    #     bSTR1 = visPropertySet1.Name
    #     bSTR2 = visPropertySet1.Name
    #     visPropertySet1.SetShow(1)
    #     selection1.Clear()


# catia零件組合
def test_1(element1, element2, dist, relation):
    catapp = win32.Dispatch("CATIA.Application")
    productdoc = catapp.ActiveDocument
    product = productdoc.Product
    product = product.ReferenceProduct
    constraints1 = product.Connections("CATIAConstraints")
    ref1 = product.CreateReferenceFromName("Product1/%s.1/!PartBody/%s" % (element1, relation))
    ref2 = product.CreateReferenceFromName("Product1/%s.1/!PartBody/%s" % (element2, relation))
    constraint1 = constraints1.AddBiEltCst(2, ref1, ref2)
    constraint1.Orientation = 0
    product.Update()
    return True


# catia組件之組合
def test_2(element1, element2, element4, element5, element3):
    catapp = win32.Dispatch("CATIA.Application")
    productdoc = catapp.ActiveDocument
    product = productdoc.Product
    product = product.ReferenceProduct
    constraints1 = product.Connections("CATIAConstraints")
    ref1 = product.CreateReferenceFromName("Product4/%s.1/%s.1/!PartBody/%s" % (element1, element2, element3))
    ref2 = product.CreateReferenceFromName("Product4/%s.1/%s.1/!PartBody/%s" % (element4, element5, element3))
    constraint1 = constraints1.AddBiEltCst(2, ref1, ref2)
    constraint1.Orientation = 1
    product.Update()


def test_3(element1, element2, element4, element5, element3, value):
    catapp = win32.Dispatch("CATIA.Application")
    productdoc = catapp.ActiveDocument
    product = productdoc.Product
    product = product.ReferenceProduct
    constraints1 = product.Connections("CATIAConstraints")
    ref1 = product.CreateReferenceFromName("Product5/%s.1/%s.1/!PartBody/%s" % (element1, element2, element3))
    ref2 = product.CreateReferenceFromName("Product5/%s.1/%s.1/!PartBody/%s" % (element4, element5, element3))
    constraint1 = constraints1.AddBiEltCst(2, ref1, ref2)
    if value == 3:
        constraint1.Orientation = 1
        product.Update()
    elif value == 4:
        constraint1.Orientation = 2
        product.Update()


def Fixed():
    catapp = win32.Dispatch("CATIA.Application")
    productDocument1 = catapp.ActiveDocument
    product1 = productDocument1.Product
    constraints1 = product1.Connections("CATIAConstraints")
    reference1 = product1.CreateReferenceFromName("Product5/Product1.1/!Product5/Product1.1/")
    constraint1 = constraints1.AddMonoEltCst(0, reference1)
    constraint1.Orientation = 0


# 小燈泡零件
def show(item):
    catapp = win32.Dispatch("CATIA.Application")
    productdoc = catapp.ActiveDocument
    product = productdoc.Product
    products1 = product.Products
    product2 = products1.Item("%s" % item)
    product2.ActivateDefaultShape()


# 小燈泡組合
def show_p(item, item1):
    catapp = win32.Dispatch("CATIA.Application")
    productDocument1 = catapp.ActiveDocument
    product1 = productDocument1.Product
    products1 = product1.Products
    product2 = products1.Item("%s" % item)
    products2 = product2.Products
    product3 = products2.Item("%s" % item1)
    product3.ActivateDefaultShape()


# 組合拘束隱藏
def show_off():
    catapp = win32.Dispatch("CATIA.Application")
    productDocument1 = catapp.ActiveDocument
    selection1 = productDocument1.Selection
    visPropertySet1 = selection1.VisProperties
    documents1 = catapp.Documents
    productDocument2 = documents1.Item("Product3.CATProduct")
    product1 = productDocument2.Product
    constraints1 = product1.Connections("CATIAConstraints")
    constraint1 = constraints1.Item("Offset.1")
    selection1.Add.constraint1()
    visPropertySet1 = visPropertySet1.Parent
    bSTR1 = str
    bSTR1 = visPropertySet1.Name
    bSTR2 = str
    bSTR2 = visPropertySet1.Name
    visPropertySet1.SetShow(1)
    selection1.Clear()


def clear_all_windows():
    catapp = win32.Dispatch('CATIA.Application')
    catapp.RefreshDisplay = False
    catapp.DisplayFileAlerts = False
    all_window = [x for x in catapp.Windows]
    print(all_window)
    for window in all_window:
        window.Close()


def part_close():
    catapp = win32.Dispatch("CATIA.Application")
    partdoc = catapp.ActiveDocument
    partdoc.Close()


# ------------------------------------------------------------------------------------------------------執行

# #抓part名稱
catia_save = ['top', 'right', 'following', 'left']
small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following']  # 名稱再來修訂吧3457 小玻璃架
small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right']  # 名稱再來修訂吧.1235 小玻璃架

# 但你可以在代碼的開頭使用 CATIA.Visible = False 並在最後使用 CATIA.Visible = True 。然後catia會​​消失，但你不會看到閃爍。
