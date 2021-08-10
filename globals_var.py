# globals設定參數的地方
import os
# 變數
width = float()  # 窗體寬
height = float()  # 窗體高
width_W = float()   #零件參數
height_H = float()   #零件參數
Quantity = float()
# width_dwg = float()
# height_dwg = float()
depth=float(112.76)
thickness_all = float(87.5)
small_width = float()  # -132.5#255
small_height = float()  # 172.5
small2_width = float()  # -120#267.5
# 檔案名稱
catia_save = ['top', 'right', 'following', 'left']
small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following']  # 名稱再來修訂吧3457 小玻璃架
small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right']  # 名稱再來修訂吧.1235 小玻璃架
AL_Window = ['Product', 'Product1', 'Product2']
#標註用的不知道是啥
sideU = "Side_Panel_U"
sideD = "Side_Panel_D"
body = "Body_Panel"
door = "Door_Panel"
door_L = ""
mtplt = 'Mtplt_Panel'
mtplt_B = ''
# 設定空
full_save_dir = str("C:\\Users\\PDAL-BM-1\\Desktop\\123")#"C:\\Users\\PDAL-BM-1\\Desktop\\123"
#v資料夾路徑
mother_drafting_template = '\\drafting\\'
system_root = os.path.dirname(os.path.realpath(__file__))
draft_mother_box ='\\Dwg\\'
body='AL_Window'
#[445, 40.5, 5, 6, 6]比例座標
#--------------------------------------------組合圖面參數14項，尚未修改
drafting_info_text_position_A4 = [[146, 41, 3.5, 3, 1], [146, 34.5, 3.5, 3, 1], [127, 15, 3.5, 3, 1],
                                  [145,15, 3.5,3, 1],[162, 15, 3.5, 3, 1],[200, 37, 3.5, 3, 1],
                                  [210, 11,3.5, 3, 1],[251 , 38, 3.5, 3, 1],
                                  [251, 26, 3.5, 3, 1],[0, 0, 3.5, 3, 1],[150,50, 3.5, 3, 1],]#到這目前有使用11項+1備註


#--------------------------------------圖紙邊框
box_draft_X_clearence = 10
box_draft_Y_clearence = 25
#--------------------------------------中心軸座標
box_draft_area_center_initX = 148.5
box_draft_area_center_initY = 105
#--------------------------------------中心軸座標
bom_isomertic_view_center_initX = 250
bom_isometric_view_center_initY = 135
#--------------------------------------中心軸座標
box_isomertic_view_center_initX = 275
box_isometric_view_center_initY = 115
#--------------------------------------中心軸座標
box_isometric_view_clearence = 5
drawingview_para = [[594.5,420.5],[928.126221,420.5],[594.5,205.066765],[594.5,665.083374],[761.31331,420.5],[342.570679,420.5],[861.31311,665.083374]]

#-----------------------------------------------------------------------------------BOM表
# drafting_info_text_position_A4 = [[135.2, 0.5, 2, 3, 0], [135.2, 8.7, 2, 3, 1], [135.2, 4.6, 2, 3, 5],
#                                   [163.2, 0.75, 2, 6, 6],
#                                   [178.75, 0.75, 3, 6, 4], [192.55, 0.75, 3, 6, 5], [206.35, 0.75, 3, 6, 6],
#                                   [186.9, 13.3, 3.5, 3, 7], [224.7, 6.9, 3, 3, 8],
#                                   [224.7, 0.75, 3, 3, 9], [273.8, 6.9, 3, 3, 10], [266.2, 0.75, 3, 3, 11],
#                                   [13, 1, 3.5, 3, 312], [150, 22, 3, 3]]
drafting_info_text_position_A4_part = [[135.2, 0.5, 2, 3, 0], [135.2, 8.7, 2, 3, 1], [135.2, 4.6, 2, 3, 5],
                                       [163.2, 0.75, 2, 6, 6],
                                       [178.75, 0.75, 3, 6, 4], [192.55, 0.75, 3, 6, 5], [206.35, 0.75, 3, 6, 6],
                                       [186.9, 13.3, 3.5, 3, 7], [224.7, 6.9, 3, 3, 8],
                                       [224.7, 0.75, 3, 3, 9], [273.8, 6.9, 3, 3, 10], [266.2, 0.75, 3, 3, 11],
                                       [13, 1, 3.5, 3, 312], [156.5, 199.75], [184.5, 199.75],
                                       [208.25, 199.75], [223, 199.75], [234, 199.75], [246, 199.75], [256.5, 199.75],
                                       [276.5, 199.75], [294, 199.75]]
packing_item_text_position_A4 = [[141, 123.5, 3.5, 3.5], [158, 123.5, 3.5, 3.5], [190, 123.5, 3.5, 3.5]]
part_list_item_text_position_A4 = [[121, 100.4, 2.5, 2], [158.75, 100.4, 2.5, 5], [162.5, 100.4, 2.5, 2],
                                   [209.25, 100.4, 2.5, 5]]