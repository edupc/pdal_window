import win32com.client as win32
import globals_var as gvar
import FINAL
import Window_Catia as wc


def add_informations(draft, window):  # 區標題欄位#
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = document.Open(gvar.system_root + gvar.draft_mother_box + 'A4_Window' + '.CATDrawing')
    # drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingview = drawingsheet.Views.Item('Background View')  # working
    sheettext1 = drawingview.Texts.Add('此圖面為CATIA生成', 30, 20)
    sheettext1.SetFontSize(0, 0, 3)
    sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
    sheettext1.AnchorPosition = 2
    # wc.saveas_close('C:\\Users\\PDAL-BM-1\\Desktop\\test\\', 'A4_Window', '.CATDrawing')
    # wc.open_drafting('C:\\Users\\PDAL-BM-1\\Desktop\\test\\', 'A4_Window')


def window_full_projection_from_template(drawingview_para, scale_p):
    # view_name = ['Front view', 'Mtplt view', 'Rear view', 'Top view', 'Bottom view', 'Left view', 'Right view']
    drawingview_para = drawingview_para  #
    drawingview_direction = [4, 2, 3, 1, 0]
    scale = 1 / scale_p
    # -------------------Load Template---------------------------
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = catapp.ActiveDocument
    # drawingdocument = document.Open(gvar.system_root+gvar.mother_drafting_template+'A4_Box'+'.CATDrawing')
    # --------------drafting parameter settings---------------
    drawingview_direction = [4, 2, 3, 1, 0]
    # -------------main program----------------------
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews1 = drawingsheet.Views
    productdoc = document.Item("AL_Window.CATProduct")
    # activedoc = catapp.ActiveDocument
    # productdoc =catapp.ActiveDocument
    product = productdoc.Product
    selection = productdoc.Selection
    # --------------------initial front view create
    drawingview1 = drawingviews1.Add('AutomaticNaming')
    drawingview1.X = drawingview_para[0][0]
    drawingview1.Y = drawingview_para[0][1]
    drawingview1.Scale = scale
    drawingviewgenerativelinks1 = drawingview1.GenerativeLinks
    drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
    drawingviewgenerativebehavior1.Document = product
    drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
    drawingviewgenerativebehavior1.Update()
    # ----------------------------------------------------投影前視圖
    drawingview1 = drawingviews1.Item('Front view')
    drawingtexts1 = drawingview1.Texts
    drawingtext1 = drawingtexts1.Item(1)
    drawingtexts1 = drawingtext1.Parent
    # ------------------------------------------------------------消除多於文字
    selection.Add(drawingtext1)
    selection.Delete()
    selection.Clear()

    # drawingview2 = drawingviews1.Add('Mtplt view')
    # drawingview2.X = 215
    # drawingview2.Y = 105
    # drawingview2.Scale = scale
    # drawingviewgenerativelinks2 = drawingview2.GenerativeLinks
    # drawingviewgenerativebehavior2 = drawingview2.GenerativeBehavior
    # drawingviewgenerativebehavior2.Document = product
    # drawingviewgenerativebehavior2.DefineFrontView(-1, 0, 0, 0, 1, 0)  # Vector Direction Value
    # drawingviewgenerativebehavior2.Update()
    #
    # drawingview2 = drawingviews1.Item('Mtplt view')
    # drawingtexts2 = drawingview2.Texts
    # drawingtext2 = drawingtexts2.Item(1)
    # drawingtexts2 = drawingtext2.Parent
    # selection.Add(drawingtext2)
    # selection.Delete()
    # selection.Clear()

    view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
    for i in range(1, len(drawingview_para) - 1):
        print(i)
        drawingview3 = drawingviews1.Add('AutomaticNaming')
        drawingview3.X = drawingview_para[i][0]
        drawingview3.Y = drawingview_para[i][1]
        drawingview3.Scale = scale
        drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
        drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
        drawingviewgenerativebehavior3.Document = product
        drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
        drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
            i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
        drawingviewgenerativebehavior3.Update()

        drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
        drawingtexts3 = drawingview3.Texts
        drawingtext3 = drawingtexts3.Item(1)
        drawingtexts3 = drawingtext3.Parent
        selection.Add(drawingtext3)
        selection.Delete()
        selection.Clear()

        # selection.Add(product2)
        # vispropertyset = vispropertyset.Parent
        # vispropertyset.SetShow(0)
        # selection.Clear()
    # ----------------------------------------------------------------------立體圖
    drawingview7 = drawingviews1.Add('Isometric view.2')
    drawingview7.X = drawingview_para[-1][0]
    drawingview7.Y = drawingview_para[-1][1]
    drawingview7.Scale = scale
    drawingviewgenerativelinks7 = drawingview7.GenerativeLinks
    drawingviewgenerativebehavior7 = drawingview7.GenerativeBehavior
    drawingviewgenerativebehavior7.Document = product
    drawingviewgenerativebehavior7.DefineIsometricView(-0.707, 0.707, 0, -0.4082, -0.4082, 0.8164)
    drawingviewgenerativebehavior7.Update()
    # ----------------Delete isometric text label--------------------------------
    drawingview7 = drawingviews1.Item('Isometric view.2')
    drawingtexts7 = drawingview7.Texts
    drawingtext7 = drawingtexts7.Item(1)
    drawingtexts8 = drawingtext7.Parent
    selection.Add(drawingtext7)
    selection.Delete()
    selection.Clear()
    # --------------Activate View---------------------
    drawingview1.Activate()
    # ---------------resetting view to full-view-----------
    SpecsAndGeomWindow = catapp.ActiveWindow
    specViewer = SpecsAndGeomWindow.ActiveViewer
    specViewer.Reframe()
    print('window_full_projection_from_template_set')


# ------------------------------------------------------------------------TEST
# drawingview7 = drawingviews1.Add('Isometric view.1')
# drawingview7.X = drawingview_para[len(drawingview_para) - 2][0]
# drawingview7.Y = drawingview_para[len(drawingview_para) - 2][1] - 30
# drawingview7.Scale = scale
# drawingviewgenerativelinks7 = drawingview7.GenerativeLinks
# drawingviewgenerativebehavior7 = drawingview7.GenerativeBehavior
# drawingviewgenerativebehavior7.Document = product
# drawingviewgenerativebehavior7.DefineIsometricView(-0.707, 0.707, 0, -0.4082, -0.4082, 0.8164)
# drawingviewgenerativebehavior7.Update()

def add_drafting_infomation(draft_info, box_info):
    # draft_gen_data = ['1','2']
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = document.Open(gvar.system_root + gvar.draft_mother_box + 'A4_Window' + '.CATDrawing')
    # drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingview = drawingsheet.Views.Item('Background View')
    print('add_drafting_infomation_set')
    print(draft_info[0])
    # for value in draft_gen_data[].values():#len(gvar.drafting_info_text_position_A4)-3):
    #     print(value)
    for i in range(0, 11):
        sheettext1 = drawingview.Texts.Add(draft_info[i], gvar.drafting_info_text_position_A4[i][0],
                                           gvar.drafting_info_text_position_A4[i][1])
        sheettext1.SetFontSize(0, 0, gvar.drafting_info_text_position_A4[i][2])
        sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
        sheettext1.AnchorPosition = gvar.drafting_info_text_position_A4[i][
            3]  # TopL=1,MidL=2,BottomL=3,TopM=4,MidM=5,BottomM=6,TopR=7,MidR=8,BottomR=9
    # --------------------------------add material info----------------------
    # material_info = '材料:%s-%s\n烤漆:%s' % (draft_info[12],'Aluminum','函數顏色')
    # sheettext1 = drawingview.Texts.Add(material_info,gvar.drafting_info_text_position_A4[13][0],gvar.drafting_info_text_position_A4[13][1])
    # sheettext1.SetFontSize(0,0,gvar.drafting_info_text_position_A4[13][2])
    # sheettext1.SetFontName(0,0,'Arial Unicode MS (TrueType)')
    # sheettext1.AnchorPosition = gvar.drafting_info_text_position_A4[13][3]

    sheettext1 = drawingview.Texts.Add('此圖面為CATIA生成', 26, 15)
    sheettext1.SetFontSize(0, 0, 3)
    sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
    sheettext1.AnchorPosition = 2


# ------------------------------------------執行程式碼
# window_full_projection_from_template(0,0)

# add_drafting_infomation(0,0)



def window_part(drawingview_para, scale_p, DID):
    # view_name = ['Front view', 'Mtplt view', 'Rear view', 'Top view', 'Bottom view', 'Left view', 'Right view']
    drawingview_para = drawingview_para  #
    drawingview_direction = [4, 2, 3, 1, 0]
    scale = 1 / scale_p
    # -------------------Load Template---------------------------
    catapp = win32.Dispatch('CATIA.Application')
    document = catapp.Documents
    drawingdocument = catapp.ActiveDocument
    # drawingdocument = document.Open(gvar.system_root+gvar.mother_drafting_template+'A4_Box'+'.CATDrawing')
    # --------------drafting parameter settings---------------
    drawingview_direction = [4, 2, 3, 1, 0]
    # -------------main program----------------------
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews1 = drawingsheet.Views

    productdoc = document.Item(DID)
    # activedoc = catapp.ActiveDocument
    # productdoc =catapp.ActiveDocument
    product = productdoc.Product
    selection = productdoc.Selection
    # --------------------initial front view create
    drawingview1 = drawingviews1.Add('AutomaticNaming')
    drawingview1.X = drawingview_para[0][0]
    drawingview1.Y = drawingview_para[0][1]
    drawingview1.Scale = scale
    drawingviewgenerativelinks1 = drawingview1.GenerativeLinks
    drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
    drawingviewgenerativebehavior1.Document = product
    print(DID)
    variable = []
    if DID == "top.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, 4, 2):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()


    elif DID == "following.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 1, 0)  # Vector Direction Value
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, 4, 2):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()
    elif DID == "left.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(0, 1, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593/2
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()
    elif DID == "right.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(0, -1, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593 / 2
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()

    # small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following']
    elif DID == "small_top.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()


    elif DID == "small_left.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(0, 1, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593 / 2
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()

    elif DID == "small_right.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593 / 2
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()
    elif DID == "small_following.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 0
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()
    elif DID == "small2_top.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()


    elif DID == "small2_left.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(0, 1, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593 / 2
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()

    elif DID == "small2_right.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 3.141593 / 2
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        drawingview1 = drawingviews1.Item('Front view')
        drawingtexts1 = drawingview1.Texts
        drawingtext1 = drawingtexts1.Item(1)
        drawingtexts1 = drawingtext1.Parent
        # ------------------------------------------------------------消除多於文字
        selection.Add(drawingtext1)
        # selection.Delete()
        selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()
    elif DID == "small2_following.CATPart":
        drawingviewgenerativebehavior1.DefineFrontView(-1, 0, 0, 0, 0, 1)  # Vector Direction Value
        drawingview1.Angle = 0
        drawingviewgenerativebehavior1.Update()
        # ----------------------------------------------------投影前視圖
        # drawingview1 = drawingviews1.Item('Front view')
        # drawingtexts1 = drawingview1.Texts
        # drawingtext1 = drawingtexts1.Item(1)
        # drawingtexts1 = drawingtext1.Parent
        # # ------------------------------------------------------------消除多於文字
        # selection.Add(drawingtext1)
        # # selection.Delete()
        # selection.Clear()

        view_name = ['Top view', 'Bottom view', 'Left view', 'Right view']
        # for i in range(1, len(drawingview_para)-1):
        for i in range(1, len(drawingview_para)-1):
            print(i)
            drawingview3 = drawingviews1.Add('AutomaticNaming')
            drawingview3.X = drawingview_para[i][0]
            drawingview3.Y = drawingview_para[i][1]
            drawingview3.Scale = scale
            drawingviewgenerativelinks3 = drawingview3.GenerativeLinks
            drawingviewgenerativebehavior3 = drawingview3.GenerativeBehavior
            drawingviewgenerativebehavior3.Document = product
            drawingviewgenerativebehavior1 = drawingview1.GenerativeBehavior
            drawingviewgenerativebehavior3.DefineProjectionView(drawingviewgenerativebehavior1, drawingview_direction[
                i])  # define projection direction (catRightView = 0, catLeftView = 1, catTopView = 2, catBottomView = 3, catRearView = 4)
            drawingviewgenerativebehavior3.Update()

            drawingview3 = drawingviews1.Item('%s' % view_name[i - 1])
            drawingtexts3 = drawingview3.Texts
            drawingtext3 = drawingtexts3.Item(1)
            drawingtexts3 = drawingtext3.Parent
            selection.Add(drawingtext3)
            # selection.Delete()
            selection.Clear()

    # ----------------------------------------------------------------------立體圖
    drawingview7 = drawingviews1.Add('Isometric view.2')
    drawingview7.X = drawingview_para[-1][0]
    drawingview7.Y = drawingview_para[-1][1]
    drawingview7.Scale = scale
    drawingviewgenerativelinks7 = drawingview7.GenerativeLinks
    drawingviewgenerativebehavior7 = drawingview7.GenerativeBehavior
    drawingviewgenerativebehavior7.Document = product
    drawingviewgenerativebehavior7.DefineIsometricView(-0.707, 0.707, 0, -0.4082, -0.4082, 0.8164)
    drawingviewgenerativebehavior7.Update()
    # ----------------Delete isometric text label--------------------------------
    drawingview7 = drawingviews1.Item('Isometric view.2')
    drawingtexts7 = drawingview7.Texts
    drawingtext7 = drawingtexts7.Item(1)
    drawingtexts8 = drawingtext7.Parent
    selection.Add(drawingtext7)
    # selection.Delete()
    selection.Clear()
    # --------------Activate View---------------------
    drawingview1.Activate()
    # ---------------resetting view to full-view-----------
    SpecsAndGeomWindow = catapp.ActiveWindow
    specViewer = SpecsAndGeomWindow.ActiveViewer
    specViewer.Reframe()

    print('window_full_projection_from_template_set')

