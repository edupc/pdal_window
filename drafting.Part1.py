
import win32com.client as win32

import globals_var as gvar
import sheetmetal_model


# import CATIA common function python module

# enviorment initialation
# catapp = win32.Dispatch("CATIA.Application")

def drafting_part_parameter_calculation(target_part, drawingview_para, scale):
    # ---------------------------INITIAL PARAMETER SETTINGS-----------------------------------------------------(初始參數設定)
    scale_p = 1 / scale
    drafting_part_centerX = drawingview_para[0][0]
    drafting_part_centerY = drawingview_para[0][1]
    w_scale = gvar.width * scale_p  # box width after scaling
    h_scale = gvar.height * scale_p  # box height after scaling
    d_scale = gvar.depth * scale_p  # box depth after scaling

    # ---------------------------FULL PROJECTION PARAMETER SETTINGS-----------------------------------------(全投影)
    # #drafting area extremums, format:[X-min,X-max,Y-min,Y-max]
    if gvar.sideU == target_part or gvar.sideD == target_part:
        drafting_area_X_range = h_scale
        drafting_area_Y_range = d_scale
        drafting_area_extremum = [drafting_part_centerX - h_scale / 2, drafting_part_centerX + h_scale / 2,
                                  drafting_part_centerY - d_scale / 2, drafting_part_centerY + d_scale / 2]
    elif gvar.mtplt_B == target_part:
        drafting_area_X_range = (h_scale - 50)
        drafting_area_Y_range = (w_scale - 50)
        drafting_area_extremum = [drafting_part_centerX - (h_scale - 50) / 2,
                                  drafting_part_centerX + (h_scale - 50) / 2,
                                  drafting_part_centerY - (w_scale - 50) / 2,
                                  drafting_part_centerY + (w_scale - 50) / 2]
    elif gvar.door_L == target_part:
        drafting_area_X_range = w_scale
        drafting_area_Y_range = h_scale
        drafting_area_extremum = [drafting_part_centerX - w_scale / 2, drafting_part_centerX + w_scale / 2,
                                  drafting_part_centerY - h_scale / 2, drafting_part_centerY + h_scale / 2]
    elif gvar.body == target_part:
        drafting_area_X_range = h_scale + 2 * d_scale
        drafting_area_Y_range = w_scale
        drafting_area_extremum = [drafting_part_centerX - drafting_area_X_range / 2,
                                  drafting_part_centerX + drafting_area_X_range / 2,
                                  drafting_part_centerY - w_scale / 2, drafting_part_centerY + w_scale / 2]

    # -----------------------------SETTING SCALE RECALIBRATION FLAG---------------------------------------
    scale_recalibration_flag = False
    # --------------------------FULL PROJECTION PARAMETER CALCULATION-------------------------------------
    # check X extremum(確認X極值)
    if gvar.sideU == target_part or gvar.sideD == target_part:
        while True:
            if drafting_area_extremum[0] < 40 and drafting_area_extremum[1] > 150:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[0] < 40:
                drafting_part_centerX += 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            elif drafting_area_extremum[1] > 150:
                drafting_part_centerX -= 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            else:
                break
        # check Y extremum(確認Y極值)
        while True and scale_recalibration_flag == False:
            if drafting_area_extremum[2] < 40 and drafting_area_extremum[3] > 160:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[2] < 40:
                drafting_part_centerY += 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            elif drafting_area_extremum[3] > 160:
                drafting_part_centerY -= 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            else:
                break
    elif gvar.mtplt_B == target_part:
        while True:
            if drafting_area_extremum[0] < 50 and drafting_area_extremum[1] > 140:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[0] < 50:
                drafting_part_centerX += 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            elif drafting_area_extremum[1] > 140:
                drafting_part_centerX -= 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            else:
                break
        # check Y extremum(確認Y極值)
        while True and scale_recalibration_flag == False:
            if drafting_area_extremum[2] < 50 and drafting_area_extremum[3] > 160:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[2] < 50:
                drafting_part_centerY += 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            elif drafting_area_extremum[3] > 160:
                drafting_part_centerY -= 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            else:
                break
    elif gvar.door_L == target_part:
        while True:
            if drafting_area_extremum[0] < 50 and drafting_area_extremum[1] > 150:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[0] < 50:
                drafting_part_centerX += 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            elif drafting_area_extremum[1] > 150:
                drafting_part_centerX -= 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            else:
                break
        # check Y extremum(確認Y極值)
        while True and scale_recalibration_flag == False:
            if drafting_area_extremum[2] < 80 and drafting_area_extremum[3] > 180:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[2] < 80:
                drafting_part_centerY += 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            elif drafting_area_extremum[3] > 180:
                drafting_part_centerY -= 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            else:
                break
    elif gvar.body == target_part:
        while True:
            if drafting_area_extremum[0] < 40 and drafting_area_extremum[1] > 200:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[0] < 40:
                drafting_part_centerX += 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            elif drafting_area_extremum[1] > 200:
                drafting_part_centerX -= 5
                # recalculate
                drafting_area_extremum[0] = drafting_part_centerX - drafting_area_X_range / 2
                drafting_area_extremum[1] = drafting_part_centerX + drafting_area_X_range / 2
            else:
                break
        # check Y extremum(確認Y極值)
        while True and scale_recalibration_flag == False:
            if drafting_area_extremum[2] < 90 and drafting_area_extremum[3] > 180:
                scale_recalibration_flag = True
                break
            elif drafting_area_extremum[2] < 90:
                drafting_part_centerY += 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            elif drafting_area_extremum[3] > 180:
                drafting_part_centerY -= 5
                # recalculate
                drafting_area_extremum[2] = drafting_part_centerY - drafting_area_Y_range / 2
                drafting_area_extremum[3] = drafting_part_centerY + drafting_area_Y_range / 2
            else:
                break

    return scale_recalibration_flag


def drafting_parameter_calculation(width, height, depth, scale_p):
    # ---------------------------INITIAL PARAMETER SETTINGS-----------------------------------------------------
    scale_tmp = scale_p  # temping original scale
    scale = 1 / scale_p  # proportion convert to ratio
    drafting_area_centerX = 90
    drafting_area_centerY = 70
    w_scale = width * scale  # box width after scaling
    h_scale = height * scale  # box height after scaling
    d_scale = depth * scale  # box depth after scaling

    # ---------------------------UNFOLDED VIEW RANGE CALCULATION-----------------------------------------


def part_unfold_projection_drafting(target_part, drawingview_para, scale_p):
    # -------------------Convert scale proportion to ratio--------
    scale = 1 / scale_p
    # -------------------Load Template---------------------------
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = catapp.ActiveDocument
    drawingdocument.Standard = 1
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews1 = drawingsheet.Views
    partdoc = document.Item('%s.CATPart' % target_part)
    selection = drawingdocument.Selection
    product = partdoc.GetItem(target_part)
    # --------------------accquiring parameter--------------------
    part = partdoc.Part
    parameter = part.Parameters
    if gvar.mtplt_B == target_part or gvar.sideU == target_part or gvar.sideD == target_part:
        height = parameter.Item('Height')
        received_param = height.Value
        recalibrate_param1 = received_param * scale
    else:  # Which is Body and Door
        height = parameter.Item('Height')
        received_param = height.Value
        recalibrate_param1 = received_param * scale
        width = parameter.Item('Width')
        received_param2 = width.Value
        recalibrate_param2 = recalibrate_param1 * scale
    # --------------------initial front view vector direction definition--------------
    v_d_f = {gvar.door_L: (-1, 0, 0, 0, 0, 1), gvar.sideU: (1, 0, 0, 0, 1, 0,), gvar.sideD: (1, 0, 0, 0, 1, 0),
             gvar.body: (-1, 0, 0, 0, 0, 1), gvar.mtplt_B: (1, 0, 0, 0, 0, 1),
             'Mtplt_Panel_bend': (-1, 0, 0, 0, 0, 1)}  # vector direction dict

    # --------------------initial front view create
    drawingview1 = drawingviews1.Add('AutomaticNaming')
    drawingview1.X = drawingview_para[0][0]
    drawingview1.Y = drawingview_para[0][1]
    drawingview1.Scale = scale
    drawingviewgenerativelinks1 = drawingview1.GenerativeLinks
    drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
    drawingviewgenerativebehavior1.Document = product
    drawingviewgenerativebehavior1.DefineFrontView(v_d_f[target_part][0], v_d_f[target_part][1], v_d_f[target_part][2],
                                                   v_d_f[target_part][3], v_d_f[target_part][4],
                                                   v_d_f[target_part][5])  # Vector Direction Value
    drawingviewgenerativebehavior1.Update()

    drawingview1 = drawingviews1.Item('Front view')
    drawingtexts1 = drawingview1.Texts
    drawingtext1 = drawingtexts1.Item(1)
    drawingtexts1 = drawingtext1.Parent
    selection.Add(drawingtext1)
    selection.Delete()
    selection.Clear()

    if gvar.body != target_part:
        # ------------------right projection view crete-----------------
        drawingview3 = drawingviews1.Add('AutomaticNaming')
        if gvar.door_L == target_part:
            drawingview3.X = drawingview_para[0][0] + recalibrate_param1 / 2 + 40
        else:
            drawingview3.X = drawingview_para[0][0] + recalibrate_param1 / 2 + 30
        drawingview3.Y = drawingview_para[0][1]
        drawingview3.Scale = scale
        drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
        drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
        drawingviewgenerativebehavior3.Document = product
        drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
        if gvar.sideD == target_part:
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1,
                                                                1)  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
        elif gvar.sideU == target_part or gvar.mtplt_B == target_part or gvar.door_L == target_part:
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, 0)
        else:
            pass
        drawingviewgenerativebehavior3.Update()
        drawingtexts3 = drawingview3.Texts
        drawingtext3 = drawingtexts3.Item(1)
        drawingtexts3 = drawingtext3.Parent
        selection.Add(drawingtext3)
        selection.Delete()
        selection.Clear()

    else:  # if target_part is body, then ONLY make bottom view instead of right view
        pass
    # ------------------Bottom projetion view for door-----
    if gvar.mtplt_B == target_part or gvar.sideU == target_part or gvar.sideD == target_part:
        print('BOTTOM VIEW PASSED')
    else:
        # ---------------
        drawingview4 = drawingviews1.Add('AutomaticNaming')
        drawingview4.X = drawingview_para[0][0]
        if gvar.door_L == target_part:
            drawingview4.Y = drawingview_para[0][1] - recalibrate_param1 / 2 - 50
        elif gvar.body == target_part:
            drawingview4.Y = drawingview_para[0][1] - recalibrate_param1 / 2 - 50
        else:
            pass
        drawingview4.Scale = scale
        drawingviewgenerativelinks4 = drawingview4.GenerativeLinks
        drawingviewgenerativebehavior4 = drawingview4.GenerativeBehavior
        drawingviewgenerativebehavior4.Document = product
        drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
        drawingviewgenerativebehavior4.DefineProjectionView(drawingviewgenerativebehavior1,
                                                            3)  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
        drawingviewgenerativebehavior4.Update()

        drawingtexts4 = drawingview4.Texts
        drawingtext4 = drawingtexts4.Item(1)
        drawingtexts4 = drawingtext4.Parent
        selection.Add(drawingtext4)
        selection.Delete()
        selection.Clear()

    # ------------------Hide initial front view------------------------
    selection = drawingdocument.Selection
    selectedproduct = drawingdocument.Selection.Search('Drafting.View.Name=Front view,all')
    vispropertyset = selection.VisProperties
    vispropertyset = vispropertyset.Parent
    vispropertyset.SetShow(1)
    # ------------------initial unfold view vector direction definition--
    v_d_u = {gvar.door_L: (-1, 0, 0, 0, 0, 1), gvar.sideU: (1, 0, 0, 0, 1, 0,), gvar.sideD: (-1, 0, 0, 0, 1, 0),
             gvar.body: (-1, 0, 0, 0, 0, 1), gvar.mtplt_B: (-1, 0, 0, 0, 0, 1),
             'Mtplt_Panel_bend': (-1, 0, 0, 0, 0, 1)}  # vector direction dict

    # ------------------initial unfold view create----------------------
    drawingview1 = drawingviews1.Add('AutomaticNaming')
    drawingview1.X = drawingview_para[0][0]
    drawingview1.Y = drawingview_para[0][1]
    drawingview1.Scale = scale
    drawingviewgenerativelinks1 = drawingview1.GenerativeLinks
    drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
    drawingviewgenerativebehavior1.Document = product
    drawingviewgenerativebehavior1.DefineUnfoldedView(v_d_u[target_part][0], v_d_u[target_part][1],
                                                      v_d_u[target_part][2],
                                                      v_d_u[target_part][3], v_d_u[target_part][4],
                                                      v_d_u[target_part][5])  # Vector Direction Value
    # if target_part== gvar.door_L:
    #     drawingview1.Angle = -1.570796
    # else:
    #     pass
    drawingviewgenerativebehavior1.Update()

    drawingtexts1 = drawingview1.Texts
    drawingtext1 = drawingtexts1.Item(1)
    drawingtexts1 = drawingtext1.Parent
    selection.Add(drawingtext1)
    selection.Delete()
    selection.Clear()

    drawingview7 = drawingviews1.Add('Isometric view.1')
    if gvar.sideU == target_part or gvar.sideD == target_part:
        drawingview7.X = 220
        drawingview7.Y = 155
        drawingview7.Scale = scale
    elif gvar.mtplt_B == target_part or gvar.door_L == target_part:
        drawingview7.X = 240
        drawingview7.Y = 110
        drawingview7.Scale = scale
    elif gvar.body == target_part:
        drawingview7.X = 225
        drawingview7.Y = 145
        scale = 1 / ((1 / scale) + 2)
        drawingview7.Scale = scale
    drawingviewgenerativelinks7 = drawingview7.GenerativeLinks
    drawingviewgenerativebehavior7 = drawingview7.GenerativeBehavior
    drawingviewgenerativebehavior7.Document = product
    drawingviewgenerativebehavior7.DefineIsometricView(-0.707, 0.707, 0, -0.4082, -0.4082, 0.8164)
    drawingviewgenerativebehavior7.Update()

    drawingview7 = drawingviews1.Item('Isometric view.1')
    drawingtexts7 = drawingview7.Texts
    drawingtext7 = drawingtexts7.Item(1)
    drawingtexts7 = drawingtext7.Parent
    selection.Add(drawingtext7)
    selection.Delete()
    selection.Clear()

    # --------------Activate View---------------------
    drawingview1.Activate()
    # ---------------resetting view to full-view-----------
    SpecsAndGeomWindow = catapp.ActiveWindow
    specViewer = SpecsAndGeomWindow.ActiveViewer
    specViewer.Reframe()


def add_dimension_to_view(target, width, height, depth):
    catapp = win32.Dispatch('CATIA.Application')
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews = drawingsheet.Views
    drawingview = drawingviews.Item('Unfolded view')
    # drawingview.Scale = 1/7
    factory2d = drawingview.Factory2D
    # result = sheetmetal_model.MODEL(gvar.width,gvar.height,gvar.depth)
    # print('%s , %s' % (type(result),result))
    # data_key = 'mtplt_%s*%s*%s' % (w,h,d)
    result1 = sheetmetal_model.DIM_REF_COORD(width, height, depth)

    # print(method())
    command = target
    method = getattr(result1, command)
    print(method())
    for data in method():
        for i in range(0, len(method()[data])):
            dim_ref_1 = method()[data][i][0]
            dim_ref_2 = method()[data][i][1]
            dim_ref_3 = method()[data][i][2]
            print(dim_ref_1)
            print(dim_ref_2)
            point1 = factory2d.CreatePoint(dim_ref_1[0], dim_ref_1[1])
            point2 = factory2d.CreatePoint(dim_ref_2[0], dim_ref_2[1])
            # line1 = factory2d.CreateLine(dim_ref_1[0],dim_ref_1[1]+100,dim_ref_2[0],dim_ref_2[1]+100)
            # dim_refpoint = factory2d.CreatePoint(dim_ref_3[0],dim_ref_3[1])
            geoelem = [point1, point2]
            geocoord = (dim_ref_1[0], dim_ref_1[1], dim_ref_2[0], dim_ref_2[1])
            if dim_ref_1[1] == dim_ref_2[1]:
                # dim1 = drawingview.Dimensions.Add2(0,geoelem,geocoord,None,0)
                dim1 = drawingview.Dimensions.Add(0, geoelem, geocoord, 3)
                dim1.Name = '%s_X' % data
                drawingdim = drawingview.Dimensions.Item('%s_X' % data)
            elif dim_ref_1[0] == dim_ref_2[0]:
                dim1 = drawingview.Dimensions.Add2(0, geoelem, geocoord, None, 90)
                dim1.Name = '%s_Y' % data
                drawingdim = drawingview.Dimensions.Item('%s_Y' % data)
            else:
                pass
            drawingdim.MoveValue(dim_ref_3[0], dim_ref_3[1], 0, 0)

    print(dir(sheetmetal_model.DIM_REF_COORD))


def add_drafting_infomation(draft_info, target, scale):
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = document.Open(gvar.system_root + gvar.mother_drafting_template + 'A4_Part' + '.CATDrawing')
    # drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingview = drawingsheet.Views.Item('Background View')
    drawingsheet.Activate
    for i in range(0, 12):  # len(gvar.drafting_info_text_position_A4)-9):
        if '##' in draft_info[i]:  # a spacer for replacing part's name
            # replacing ## spacer for part's name
            serial = draft_info[i][:-2] + ' %s ' % target
            sheettext1 = drawingview.Texts.Add(serial, gvar.drafting_info_text_position_A4[i][0],
                                               gvar.drafting_info_text_position_A4[i][1])
            sheettext1.SetFontSize(0, 0, gvar.drafting_info_text_position_A4[i][2])
            sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
            sheettext1.AnchorPosition = gvar.drafting_info_text_position_A4[i][
                3]  # TopL=1,MidL=2,BottomL=3,TopM=4,MidM=5,BottomM=6,TopR=7,MidR=8,BottomR=9
        elif i == 3:
            sheettext1 = drawingview.Texts.Add('SCALE 1:' + str(scale), gvar.drafting_info_text_position_A4[i][0],
                                               gvar.drafting_info_text_position_A4[i][1])
            sheettext1.SetFontSize(0, 0, gvar.drafting_info_text_position_A4[i][2])
            sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
            sheettext1.AnchorPosition = gvar.drafting_info_text_position_A4[i][
                3]  # TopL=1,MidL=2,BottomL=3,TopM=4,MidM=5,BottomM=6,TopR=7,MidR=8,BottomR=9

        else:
            sheettext1 = drawingview.Texts.Add(draft_info[i], gvar.drafting_info_text_position_A4[i][0],
                                               gvar.drafting_info_text_position_A4[i][1])
            sheettext1.SetFontSize(0, 0, gvar.drafting_info_text_position_A4[i][2])
            sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
            sheettext1.AnchorPosition = gvar.drafting_info_text_position_A4[i][
                3]  # TopL=1,MidL=2,BottomL=3,TopM=4,MidM=5,BottomM=6,TopR=7,MidR=8,BottomR=9

    sheettext1 = drawingview.Texts.Add('此圖面為CATIA生成', 13, 4)
    sheettext1.SetFontSize(0, 0, 3)
    sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
    sheettext1.AnchorPosition = 2


def insert_picture(face):
    catapp = win32.Dispatch("CATIA.Application")
    document = catapp.Documents
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingview = drawingsheet.Views.ActiveView

    DrawingPicture = drawingview.Pictures
    origin_dir = gvar.system_root + gvar.mother_drafting_template + 'hole_origin.png'
    origin_r_dir = gvar.system_root + gvar.mother_drafting_template + 'hole_origin_r.png'

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