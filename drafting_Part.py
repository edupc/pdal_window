import win32com.client as win32
# import globals_var as gvar
import Window_Catia as wc
import globals_var as gvar
import drafting as draft
import math

bom_whd_value = []
window_gen_data = []
Lframe_param = {'width': 600, 'height': 100}
save_dir = []
full_save_dir = []
# box_gen_data = []
hole_gen_data = {}
draft_gen_data = []
bom_gen_data = []


def insert_picture(face):
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingview = drawingsheet.Views.ActiveView

    DrawingPicture = drawingview.Pictures
    origin_dir = gvar.system_root + gvar.draft_mother_box + 'hole_origin.png'
    # origin_r_dir = gvar.system_root + gvar.draft_mother_box + 'hole_origin_r.png'
    picture = DrawingPicture.Add(origin_dir, 0, 0)
    width_p = picture.width
    height_p = picture.height
    picture.x = 0 - 25 - 250
    picture.y = 0 - 25 - 81.9


def projection_parameter_calculation(width, height, depth, papersize, scale):
    scale_tmp = scale  # temping original scale
    scale = 1 / scale  # proportion convert to ratio
    drafting_area_centerX = gvar.box_draft_area_center_initX
    drafting_area_centerY = gvar.box_draft_area_center_initY
    w_scale = gvar.width * scale  # box width after scaling
    h_scale = gvar.height * scale  # box height after scaling
    d_scale = gvar.depth * scale  # box depth after scaling
    # ---------------------------FULL PROJECTION PARAMETER SETTINGS-----------------------------------------(全投影計算)
    drafting_area_X_range = w_scale + d_scale + 80  # 10間距*2
    drafting_area_Y_range = h_scale + w_scale + 80
    # [xmin xmax ymin ymax]
    drafting_area_extremum = [drafting_area_centerX - drafting_area_X_range / 2,
                              drafting_area_centerX + drafting_area_X_range / 2,
                              drafting_area_centerY - drafting_area_Y_range / 2,
                              drafting_area_centerY + drafting_area_Y_range / 2]
    scale_recalibration_flag = False
    # --------------------------FULL PROJECTION PARAMETER CALCULATION-------------------------------(全投影位置計算)
    # check X LEFT extremum(確認X左極值)
    while True:
        if drafting_area_extremum[0] < 5:
            drafting_area_centerX += 2
            # recalculate
            drafting_area_extremum[0] = drafting_area_centerX - drafting_area_X_range / 2
            drafting_area_extremum[1] = drafting_area_centerX + drafting_area_X_range / 2
        elif drafting_area_extremum[0] > 10:
            drafting_area_centerX -= 2
            # recalculate
            drafting_area_extremum[0] = drafting_area_centerX - drafting_area_X_range / 2
            drafting_area_extremum[1] = drafting_area_centerX + drafting_area_X_range / 2
        else:
            break
    # check X RIGHT extremum(確認X右極值)
    while True:
        if drafting_area_extremum[1] > 212:
            scale_recalibration_flag = True
            break
        else:
            break

    # check Y extremum(確認Y極值)
    while True and scale_recalibration_flag == False:
        if drafting_area_extremum[2] < 24.4 and drafting_area_extremum[3] > 205:
            scale_recalibration_flag = True
            break
        elif drafting_area_extremum[2] < 24.4:
            drafting_area_centerY += 2
            # recalculate
            drafting_area_extremum[2] = drafting_area_centerY - drafting_area_Y_range / 2
            drafting_area_extremum[3] = drafting_area_centerY + drafting_area_Y_range / 2
        elif drafting_area_extremum[3] > 205:
            drafting_area_centerY -= 2
            # recalculate
            drafting_area_extremum[2] = drafting_area_centerY - drafting_area_Y_range / 2
            drafting_area_extremum[3] = drafting_area_centerY + drafting_area_Y_range / 2
        else:
            break
    print(drafting_area_extremum)
    # print(drafting_area_centerX)
    # print(drafting_area_centerY)
    drafting_view_center_data = []  # create list
    # drafting_view_center_data.append([drafting_area_centerX - h_scale - gvar.box_draft_X_clearence,
    #                                   drafting_area_centerY])  # Front View(MASTER) center
    # drafting_view_center_data.append([drafting_area_centerX, drafting_area_centerY])  # Front View(Door Removed) center
    # drafting_view_center_data.append([drafting_area_centerX + h_scale + d_scale + gvar.box_draft_X_clearence * 2,
    #                                   drafting_area_centerY])  # Rear View
    # drafting_view_center_data.append([drafting_view_center_data[0][0],
    #                                   drafting_area_centerY + w_scale * 0.5 + d_scale * 0.5 + gvar.box_draft_Y_clearence])  # Top View
    # drafting_view_center_data.append([drafting_view_center_data[0][0],
    #                                   drafting_area_centerY - w_scale * 0.5 - d_scale * 0.5 - gvar.box_draft_Y_clearence])  # Bottom View
    # drafting_view_center_data.append(
    #     [drafting_area_centerX - h_scale * 1.5 - d_scale * 0.5 - gvar.box_draft_X_clearence * 2,
    #      drafting_area_centerY])  # left view
    # drafting_view_center_data.append(
    #     [drafting_area_centerX + h_scale * 0.5 + d_scale * 0.5 + gvar.box_draft_X_clearence,
    #      drafting_area_centerY])  # right view
    drafting_view_center_data.append([drafting_area_centerX+25, drafting_area_centerY])
    drafting_view_center_data.append([drafting_area_centerX+25, drafting_area_centerY + gvar.depth / 2])
    drafting_view_center_data.append([drafting_area_centerX+25, drafting_area_centerY - gvar.depth / 2])
    drafting_view_center_data.append([(drafting_area_centerX - gvar.depth / 2)+25, drafting_area_centerY])
    drafting_view_center_data.append([(drafting_area_centerX + gvar.depth / 2)+25, drafting_area_centerY])
    drafting_view_center_data.append([(drafting_area_centerX + 150), drafting_area_centerY])
    return [drafting_view_center_data, scale_tmp,
            scale_recalibration_flag]  # return center_data,scale,recalibration flag

def insert_picture(part, face):
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingview_1 = drawingsheet.Views.ActiveView

    DrawingPicture = drawingview_1.Pictures
    origin_dir = gvar.system_root + gvar.draft_mother_box + 'hole_origin.png'
    origin_r_dir = gvar.system_root + gvar.draft_mother_box + 'hole_origin_r.png'
    print(gvar.height, gvar.width, gvar.depth)

    if 'bottom' in face or 'top' in face:
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = -width_p / 2 - gvar.height / 2
        picture.y = -height_p / 2
    elif 'mtplt' in face:
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = -width_p / 2 - gvar.height / 2 + 25
        picture.y = -height_p / 2 - gvar.width / 2 + 25
    elif 'front' in face:
        picture = DrawingPicture.Add(origin_r_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = width_p / 2 - gvar.height / 2
        picture.y = -height_p / 2 - gvar.width / 2
    elif 'back' in face:
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = -width_p / 2 - gvar.height / 2
        picture.y = -height_p / 2 - gvar.width / 2
    else:
        pass
    if part == 'bottom' or part == 'top':
        drawingview_2 = drawingsheet.Views
        drawingview = drawingview_2.Item("Unfolded view")
        drawingview.Activate()
        DrawingPicture = drawingview.Pictures
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = -gvar.height / 2 - width_p / 2
        picture.y = 0 - height_p / 2

    elif part == "mtplt":
        drawingview_2 = drawingsheet.Views
        drawingview = drawingview_2.Item("Unfolded view")
        drawingview.Activate()
        DrawingPicture = drawingview.Pictures
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = 0 - picture.height / 2 - ((gvar.height - 50) / 2)
        picture.y = 0 - picture.width / 2 - ((gvar.width - 50) / 2)
    elif part == 'door':
        drawingview_2 = drawingsheet.Views
        drawingview = drawingview_2.Item("Unfolded view")
        drawingview.Activate()
        DrawingPicture = drawingview.Pictures
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = - picture.width / 2 - (gvar.height / 2) - 20
        picture.y = - picture.height / 2 - (gvar.width / 2) - 20
    elif part == 'body':
        drawingview_2 = drawingsheet.Views
        drawingview = drawingview_2.Item("Unfolded view")
        drawingview.Activate()
        DrawingPicture = drawingview.Pictures
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = - picture.width / 2 - gvar.height/2
        picture.y = - picture.height / 2 - gvar.width / 2 + 3 / 2
    elif part == 'front':
        drawingview_2 = drawingsheet.Views
        drawingview = drawingview_2.Item("Front view")
        drawingview.Activate()
        DrawingPicture = drawingview.Pictures
        picture = DrawingPicture.Add(origin_dir, 0, 0)
        width_p = picture.width
        height_p = picture.height
        picture.x = - picture.width / 2 - gvar.height/2
        picture.y = - picture.height / 2




#------------------------------------------執行程式碼
# window_gen_data.append(gvar.width)
# window_gen_data.append(gvar.height)
# window_gen_data.append(gvar.depth)
#
# for i in range(0, 3):
#     bom_whd_value.append(int(window_gen_data[i]))
# print(bom_whd_value)
# rescale_flag = True
# scale = 1
# while rescale_flag is True:  # checking if scale recalibration is needed
#     scale = scale + 1
#     [center_data, scale, rescale_flag] = projection_parameter_calculation(0, 0, 0, 'A4', scale)
#     print(scale)
# print(center_data)

# draft.window_full_projection_from_template(0, scale)  # 組合圖擺圖
# draft.window_full_projection_from_template(center_data, scale)  # 連接圖面
#--------------------------------------------------------------------------------執行程式碼

# insert_picture('front', "Front view")
