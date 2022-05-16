import win32com.client as win32
import globals_var as gvar

def model_unfolded_view(target, w, h, d):  # ,scale):
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.door_L: 'Door_Panel', gvar.mtplt_B: 'Mtplt_Panel'}
    view_attr = {'front': 'Front_view', 'mtplt': 'Mtplt_view', 'left': 'Left_view'}
    catapp = win32.Dispatch('CATIA.Application')
    # document = catapp.Documents
    # drawingdocument = document.Open(gvar.system_root+gvar.mother_drafting_template+'A4_Box'+'.CATDrawing')
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews = drawingsheet.Views
    result1 = DIM_REF_COORD(h, w, d)

    def execute(keyword):
        return getattr(result1, keyword)

    if target in part_attr.keys():
        drawingview = drawingviews.ActiveView
        if 'bend' in target:
            part_attr[target] = part_attr[target] + '_bend'
        print(execute(part_attr[target]))
        a = execute(part_attr[target])()
    elif target in view_attr.keys():
        # drawingview = drawingviews.Item(view_attr[target])
        print(' '.join(view_attr[target].split('_')))
        drawingview = drawingviews.Item(' '.join(view_attr[target].split('_')))
        drawingview.Activate()
        print(execute(view_attr[target]))
        a = execute(view_attr[target])()
    factory2d = drawingview.Factory2D
    for data in a:
        for i in range(0, len(a[data])):
            dim_ref_1 = a[data][i][0]
            dim_ref_2 = a[data][i][1]
            dim_ref_3 = a[data][i][2]
            print(dim_ref_1)
            print(dim_ref_2)
            print(dim_ref_3)
            point1 = factory2d.CreatePoint(dim_ref_1[0], dim_ref_1[1])
            point2 = factory2d.CreatePoint(dim_ref_2[0], dim_ref_2[1])
            geoelem = [point1, point2]
            geocoord = (dim_ref_1[0], dim_ref_1[1], dim_ref_2[0], dim_ref_2[1])
            if dim_ref_1[1] == dim_ref_2[1]:
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
def model_unfolded_view_part(target, w, h, d,view):  # ,scale):
    print(view)
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.door_L: 'Door_Panel', gvar.mtplt_B: 'Mtplt_Panel'}
    view_attr = {'front': 'Front_view', 'mtplt': 'Mtplt_view', 'left': 'Left_view'}
    catapp = win32.Dispatch('CATIA.Application')
    # document = catapp.Documents
    # drawingdocument = document.Open(gvar.system_root+gvar.mother_drafting_template+'A4_Box'+'.CATDrawing')
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews = drawingsheet.Views
    if view == 'following':
        result1 = DIM_REF_COORD_following(h, w, d)
    elif view == 'left':
        result1 = DIM_REF_COORD_left(h, w, d)
    elif view == 'right':
        result1 = DIM_REF_COORD_right(h, w, d)
    elif view == 'top':
        result1 = DIM_REF_COORD_top(h, w, d)

    elif view == 'small_top':
        result1 = DIM_REF_COORD_small_top(h, w, d)
    elif view == 'small_left':
        result1 = DIM_REF_COORD_small_left(h, w, d)
    elif view == 'small_right':
        result1 = DIM_REF_COORD_small_right(h, w, d)
    elif view == 'small_following':
        result1 = DIM_REF_COORD_small_following(h, w, d)

    elif view == 'small2_following':
        result1 = DIM_REF_COORD_small2_following(h, w, d)
    elif view == 'small2_left':
        result1 = DIM_REF_COORD_small2_left(h, w, d)
    elif view == 'small2_top':
        result1 = DIM_REF_COORD_small2_top(h, w, d)
    elif view == 'small2_right':
        result1 = DIM_REF_COORD_small2_right(h, w, d)
    # catia_save = ['top', 'right', 'following', 'left']
    # small_catia_save = ['small_top', 'small_left', 'small_right', 'small_following']  # 名稱再來修訂吧3457 小玻璃架
    # small2_catia_save = ['small2_following', 'small2_left', 'small2_top', 'small2_right']

    def execute(keyword):
        return getattr(result1, keyword)

    if target in part_attr.keys():
        drawingview = drawingviews.ActiveView
        if 'bend' in target:
            part_attr[target] = part_attr[target] + '_bend'
        print(execute(part_attr[target]))
        a = execute(part_attr[target])()
    elif target in view_attr.keys():
        # drawingview = drawingviews.Item(view_attr[target])
        print(' '.join(view_attr[target].split('_')))
        drawingview = drawingviews.Item(' '.join(view_attr[target].split('_')))
        drawingview.Activate()
        print(execute(view_attr[target]))
        a = execute(view_attr[target])()
    factory2d = drawingview.Factory2D
    for data in a:
        for i in range(0, len(a[data])):
            dim_ref_1 = a[data][i][0]
            dim_ref_2 = a[data][i][1]
            dim_ref_3 = a[data][i][2]
            print(dim_ref_1)
            print(dim_ref_2)
            print(dim_ref_3)
            point1 = factory2d.CreatePoint(dim_ref_1[0], dim_ref_1[1])
            point2 = factory2d.CreatePoint(dim_ref_2[0], dim_ref_2[1])
            geoelem = [point1, point2]
            geocoord = (dim_ref_1[0], dim_ref_1[1], dim_ref_2[0], dim_ref_2[1])
            if dim_ref_1[1] == dim_ref_2[1]:
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
class DIM_REF_COORD_small_top:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w, 0)  # -187.51.-187.81
        y_dim = XY_coord_output(view_half_w, -48)
        x_dim_ref = [0, 48 +40]  # 座標+位置
        y_dim_ref = [-view_half_w - 40, 25]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}
class DIM_REF_COORD_small_left:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output((79.71/2), view_half_h)  # -187.51.-187.81
        y_dim = XY_coord_output((79.71/2), view_half_h)
        x_dim_ref = [0, 48 + 40]  # 座標+位置
        y_dim_ref = [-view_half_h - 40, 25]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}
class DIM_REF_COORD_small_right:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(48.2/2, view_half_h)  # -187.51.-187.81
        y_dim = XY_coord_output(48.2/2, view_half_h)
        x_dim_ref = [0, 48 + 40]  # 座標+位置
        y_dim_ref = [-view_half_h - 40, 25]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}
class DIM_REF_COORD_small_following:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w, 55.06/2)#改這69.7
        y_dim = XY_coord_output(view_half_w, 55.06/2)
        x_dim_ref = [0, 25+69.7]  # 座標+位置
        y_dim_ref = [-view_half_w, 35]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}


class DIM_REF_COORD_following:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)

    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w-(27.3/2), 0)
        y_dim = XY_coord_output(view_half_w-(27.3/2), 84.81)
        x_dim_ref = [0, 25]  # 座標+位置
        y_dim_ref = [-view_half_w, -40]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}
class DIM_REF_COORD_left:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(43.5, view_half_h)
        y_dim = XY_coord_output(43.5, view_half_h)
        x_dim_ref = [0, view_half_h+25]  # 座標+位置
        y_dim_ref = [-27.5-45, 0]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}
class DIM_REF_COORD_top:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w-(27.3/2), 69.7)#改這69.7
        y_dim = XY_coord_output(view_half_w-(27.3/2), 0)
        x_dim_ref = [0, 25+69.7]  # 座標+位置
        y_dim_ref = [-view_half_w, 35]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}
class DIM_REF_COORD_right:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(86.7/2, view_h / 2)
        y_dim = XY_coord_output(86.7/2, view_h / 2)
        x_dim_ref = [0, view_half_h+25]  # 座標+位置
        y_dim_ref = [-86.7/2-40, 0]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}


class DIM_REF_COORD_small2_following:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(86.7/2, view_h / 2)
        y_dim = XY_coord_output(86.7/2, view_h / 2)
        x_dim_ref = [0, view_half_h+25]  # 座標+位置
        y_dim_ref = [-86.7/2-40, 0]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}

class DIM_REF_COORD_small2_left:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(86.7/2, view_h / 2)
        y_dim = XY_coord_output(86.7/2, view_h / 2)
        x_dim_ref = [0, view_half_h+25]  # 座標+位置
        y_dim_ref = [-86.7/2-40, 0]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}

class DIM_REF_COORD_small2_top:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(86.7/2, view_h / 2)
        y_dim = XY_coord_output(86.7/2, view_h / 2)
        x_dim_ref = [0, view_half_h+25]  # 座標+位置
        y_dim_ref = [-86.7/2-40, 0]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}

class DIM_REF_COORD_small2_right:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)
    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_d = self.box_d
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(86.7/2, view_h / 2)
        y_dim = XY_coord_output(86.7/2, view_h / 2)
        x_dim_ref = [0, view_half_h+25]  # 座標+位置
        y_dim_ref = [-86.7/2-40, 0]  # 位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}












def dim_output_only(w, h, d, scale):
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.mtplt_B: 'Mtplt_Panel', gvar.door_L: 'Door_Panel'}
    result1 = DIM_REF_COORD(w, h, d)
    print(part_attr)
    print(part_attr.values())

    def execute(keyword):
        return getattr(result1, keyword)

    # print(execute(part_attr[target]))
    for data in part_attr.values():
        print(execute(data)())


def bending_direction_indicatior(target, w, h, d):
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.door_L: 'Door_Panel', gvar.mtplt_B: 'Mtplt_Panel'}
    catapp = win32.Dispatch('CATIA.Application')
    drawingdocument = catapp.ActiveDocument
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews = drawingsheet.Views
    drawingview = drawingviews.Item('Unfolded view')
    drawingview.Activate()
    result1 = BEND_IND_COORD(h, w, d)

    def execute(keyword):
        return getattr(result1, keyword)

    a = execute(part_attr[target])()
    for data in a:
        for i in range(0, len(a[data])):
            print(a[data][i])
            dim_data = a[data][i]
            sheettext1 = drawingview.Texts.Add(dim_data[2], dim_data[0], dim_data[1])
            sheettext1.SetFontSize(0, 0, 3)
            sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
            sheettext1.AnchorPosition = dim_data[3]
            # TopL=1,MidL=2,BottomL=3,TopM=4,MidM=5,BottomM=6,TopR=7,MidR=8,BottomR=9


def bending_output_only(target, w, h, d):
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.door_L: 'Door_Panel', gvar.mtplt_B: 'Mtplt_Panel'}
    result1 = BEND_IND_COORD(h, w, d)

    def execute(keyword):
        return getattr(result1, keyword)

    a = execute(part_attr[target])()
    print(a)
    for data in a:
        for i in range(0, len(a[data])):
            print(a[data][i])


def detail_view_indicator(target, w, h, d):
    part_attr = {gvar.sideU: 'Side_Panel_U', gvar.sideD: 'Side_Panel_D', gvar.body: 'Body_Panel',
                 gvar.door_L: 'Door_Panel', gvar.mtplt_B: 'Mtplt_Panel'}
    catapp = win32.Dispatch('CATIA.Application')
    drawingdocument = catapp.ActiveDocument
    drawingsheets = drawingdocument.Sheets
    drawingsheet = drawingsheets.Item('Sheet.1')
    drawingviews = drawingsheet.Views
    if target == gvar.sideD or target == gvar.sideU:
        try:
            drawingview = drawingviews.Item('Left view')
        except:
            drawingview = drawingviews.Item('Right view')
    elif target == gvar.body:
        drawingview = drawingviews.Item('Bottom view')
    else:
        return
    drawingview.Activate()

    result1 = DETAIL_IND_COORD(h, w, d)

    def execute(keyword):
        return getattr(result1, keyword)

    a = execute(part_attr[target])()
    for data in a:
        for i in range(0, len(a[data][0])):
            # add circle
            factory2d = drawingview.Factory2D
            circle_data = a[data][0]
            circle1 = factory2d.CreateClosedCircle(circle_data[i][0], circle_data[i][1], circle_data[i][2])
            # add word
            text_data = a[data][1]
            sheettext1 = drawingview.Texts.Add('A', text_data[i][0], text_data[i][1])
            sheettext1.SetFontSize(0, 0, 3)
            sheettext1.SetFontName(0, 0, 'Arial Unicode MS (TrueType)')
            sheettext1.AnchorPosition = 3
            # TopL=1,MidL=2,BottomL=3,TopM=4,MidM=5,BottomM=6,TopR=7,MidR=8,BottomR=9
    selection = drawingdocument.Selection
    selectedproduct = drawingdocument.Selection.Search('Drafting.View.Name=Detail A,all')
    vispropertyset = selection.VisProperties
    vispropertyset = vispropertyset.Parent
    vispropertyset.SetShow(0)


class XY_coord_output:
    def __init__(self, in_X, in_Y):
        self.in_X = in_X
        self.in_Y = in_Y
        self.scale = 1

    def quadrant_1(self):
        return [self.in_X * self.scale, self.in_Y * self.scale]

    def quadrant_2(self):
        return [-self.in_X * self.scale, self.in_Y * self.scale]

    def quadrant_3(self):
        return [-self.in_X * self.scale, -self.in_Y * self.scale]

    def quadrant_4(self):
        return [self.in_X * self.scale, -self.in_Y * self.scale]


class DIM_REF_COORD:
    def __init__(self, box_w, box_h, box_d):
        self.box_w = float(box_w)
        self.box_h = float(box_h)
        self.box_d = float(box_d)

    def Side_Panel_U(self):
        # Horizontal dim ref coord
        sideU_W = self.box_w / 2
        sideU_D = self.box_d + 14.5
        chamfer_corner = sideU_D - 47.5
        X_dim = XY_coord_output(sideU_W, chamfer_corner)
        Y_dim = XY_coord_output(0, sideU_D)
        X_dim_ref = [0, sideU_D + 10]
        Y_dim_ref = [-sideU_W - 10, sideU_D / 2]
        return {DIM_REF_COORD.Side_Panel_U.__name__: [[X_dim.quadrant_1(), X_dim.quadrant_2(), X_dim_ref],
                                                      [[0, 0], Y_dim.quadrant_1(), Y_dim_ref]]}

    def Side_Panel_D(self):
        # Horizontal dim ref coord
        sideU_W = self.box_w / 2
        sideU_D = self.box_d + 14.5
        chamfer_corner = sideU_D - 47.5
        X_dim = XY_coord_output(sideU_W, chamfer_corner)
        Y_dim = XY_coord_output(0, sideU_D)
        X_dim_ref = [0, sideU_D + 10]
        Y_dim_ref = [-sideU_W - 10, sideU_D / 2]
        return {DIM_REF_COORD.Side_Panel_D.__name__: [[X_dim.quadrant_1(), X_dim.quadrant_2(), X_dim_ref],
                                                      [[0, 0], Y_dim.quadrant_1(), Y_dim_ref]]}

    def Mtplt_Panel(self):
        mtplt_W = (self.box_w - 50) / 2
        mtplt_H = (self.box_h - 50) / 2
        dim = XY_coord_output(mtplt_W, mtplt_H)
        X_dim_ref = [0, mtplt_H + 10]
        Y_dim_ref = [-mtplt_W - 10, 0]
        return {DIM_REF_COORD.Mtplt_Panel.__name__: [[dim.quadrant_2(), dim.quadrant_1(), X_dim_ref],
                                                     [dim.quadrant_3(), dim.quadrant_2(), Y_dim_ref]]}

    def Mtplt_Panel_bend(self):
        mtplt_W = (self.box_w - 50) / 2 + 6
        mtplt_H = (self.box_h - 50) / 2 + 6
        dim = XY_coord_output(mtplt_W, mtplt_H)
        X_dim_ref = [0, mtplt_H + 10]
        Y_dim_ref = [-mtplt_W - 10, 0]
        return {DIM_REF_COORD.Mtplt_Panel.__name__: [[dim.quadrant_2(), dim.quadrant_1(), X_dim_ref],
                                                     [dim.quadrant_3(), dim.quadrant_2(), Y_dim_ref]]}

    def Door_Panel(self):
        door_W = (self.box_w + 40) / 2
        door_H = (self.box_h + 40) / 2
        dim = XY_coord_output(door_W, door_H)
        X_dim_ref = [0, door_H + 20]
        Y_dim_ref = [-door_W - 20, 0]
        return {DIM_REF_COORD.Door_Panel.__name__: [[dim.quadrant_3(), dim.quadrant_4(), X_dim_ref],
                                                    [dim.quadrant_3(), dim.quadrant_2(), Y_dim_ref]]}

    def Body_Panel(self):
        expand_W_half = self.box_w / 2 + self.box_d + 15 - 3
        expand_H_half = self.box_h / 2 - 1.5
        body_flange_chamfer = expand_H_half - 16.7
        chamfer_corner = expand_W_half - 47.5
        X_dim = XY_coord_output(expand_W_half, body_flange_chamfer)
        Y_dim = XY_coord_output(chamfer_corner, expand_H_half)
        X_dim_ref = [0, expand_H_half + 25]
        Y_dim_ref = [-expand_W_half - 20, 0]
        return {DIM_REF_COORD.Body_Panel.__name__: [[X_dim.quadrant_2(), X_dim.quadrant_1(), X_dim_ref],
                                                    [Y_dim.quadrant_3(), Y_dim.quadrant_2(), Y_dim_ref]]}

    def Front_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w, view_h-62.19)#-187.51.-187.81
        y_dim = XY_coord_output(view_half_w, 62.19)
        x_dim_ref = [0, view_h-62.19+25]#座標+位置
        y_dim_ref = [-view_half_w-25 ,view_half_h-62.19]#位置+座標
        return {DIM_REF_COORD.Front_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}

    def Mtplt_view(self):
        view_h = self.box_h
        view_w = self.box_w
        view_half_h = view_h / 2
        view_half_w = view_w / 2
        x_dim = XY_coord_output(view_half_w - 25, -25)
        y_dim = XY_coord_output(view_half_w - 25, view_h - 25)
        x_dim_ref = [0, 25]
        y_dim_ref = [-view_half_w - 25, -view_half_h]
        return {DIM_REF_COORD.Mtplt_view.__name__: [[x_dim.quadrant_1(), x_dim.quadrant_2(), x_dim_ref],
                                                    [x_dim.quadrant_2(), y_dim.quadrant_3(), y_dim_ref]]}

    def Left_view(self):
        view_h = self.box_h
        view_d = self.box_d
        view_half_d = view_d / 2
        view_half_h = view_h / 2
        x_dim = XY_coord_output(view_d, 0)
        y_dim = XY_coord_output(0, -view_h)
        x_dim_ref = [view_half_d, 25]
        y_dim_ref = [-25, -view_half_h]
        return {DIM_REF_COORD.Left_view.__name__: [[x_dim.quadrant_1(), [0, 0], x_dim_ref],
                                                   [[0, 0], y_dim.quadrant_1(), y_dim_ref]
                                                   ]}


class BEND_IND_COORD:
    def __init__(self, w, h, d):
        self.w = float(w)
        self.h = float(h)
        self.d = float(d)

    def Side_Panel_U(self):
        expand_d = self.d + 14.5
        text_pos = [[-20, expand_d - 8], [0, expand_d - 26.5], [20, expand_d - 47.5]]
        anchor_pos = 5
        text_content = ['上', '上', '下']
        result = []
        for i in range(0, len(text_pos)):
            result.append([text_pos[i][0], text_pos[i][1], text_content[i], anchor_pos])
        return {BEND_IND_COORD.Side_Panel_U.__name__: result}

    def Side_Panel_D(self):
        expand_d = self.d + 14.5
        text_pos = [[-20, expand_d - 8], [0, expand_d - 26.5], [20, expand_d - 47.5]]
        anchor_pos = 5
        text_content = ['上', '上', '下']
        result = []
        for i in range(0, len(text_pos)):
            result.append([text_pos[i][0], text_pos[i][1], text_content[i], anchor_pos])
        return {BEND_IND_COORD.Side_Panel_D.__name__: result}

    def Mtplt_Panel(self):
        text_pos = [[self.w / 2 - 40, 0], [0, self.h / 2 - 40], [-self.w / 2 + 40, 0], [0, -self.h / 2 + 40]]
        anchor_pos = 5
        text_content = ['下', '下', '下', '下']
        result = []
        for i in range(0, len(text_pos)):
            result.append([text_pos[i][0], text_pos[i][1], text_content[i], anchor_pos])
        return {BEND_IND_COORD.Mtplt_Panel.__name__: result}

    def Door_Panel(self):
        text_pos = [[0, self.h / 2], [self.w / 2, 0], [0, -self.h / 2], [-self.w / 2, 0]]
        anchor_pos = 5
        text_content = ['下', '下', '下', '下']
        result = []
        for i in range(0, len(text_pos)):
            result.append([text_pos[i][0], text_pos[i][1], text_content[i], anchor_pos])
        return {BEND_IND_COORD.Door_Panel.__name__: result}

    def Body_Panel(self):
        expand_half_w = self.h / 2 + self.d + 15 - 3
        text_pos = [[self.h / 2 - 1.5, 0], [expand_half_w - 46.85 - 55, 25], [expand_half_w - 26.45 - 55, 0],
                    [expand_half_w - 7.7 - 55, -25],
                    [-self.h / 2 + 1.5, 0], [-expand_half_w + 46.85 + 55, 25], [-expand_half_w + 26.45 + 55, 0],
                    [-expand_half_w + 7.7 + 55, -25]]
        anchor_pos = 5
        text_content = ['上', '上', '下', '下', '上', '上', '下', '下']
        result = []
        for i in range(0, len(text_pos)):
            result.append([text_pos[i][0], text_pos[i][1], text_content[i], anchor_pos])
        return {BEND_IND_COORD.Body_Panel.__name__: result}


class DETAIL_IND_COORD:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

    def Side_Panel_U(self):
        circle_dim = [10, self.d - 20, 30]  # stands for [X,Y,RADIUS]
        letter_dim = [circle_dim[0] + circle_dim[2], circle_dim[1] + circle_dim[2]]
        result = [[circle_dim], [letter_dim]]
        return {BEND_IND_COORD.Side_Panel_U.__name__: result}

    def Side_Panel_D(self):
        circle_dim = [10, self.d - 20, 30]  # stands for [X,Y,RADIUS]
        letter_dim = [circle_dim[0] + circle_dim[2], circle_dim[1] + circle_dim[2]]
        result = [[circle_dim], [letter_dim]]
        return {BEND_IND_COORD.Side_Panel_D.__name__: result}

    def Body_Panel(self):
        circle_dim = [self.w / 2 - 20, self.d - 20, 30]  # stands for [X,Y,RADIUS]
        circle_m_dim = [-self.w / 2 + 20, self.d - 20, 30]
        letter_dim = [circle_dim[0] + circle_dim[2], circle_dim[1] + circle_dim[2]]
        letter_m_dim = [-letter_dim[0], letter_dim[1]]
        result = [[circle_dim, circle_m_dim], [letter_dim, letter_m_dim]]
        return {BEND_IND_COORD.Body_Panel.__name__: result}


if __name__ == '__main__':
    a = BEND_IND_COORD(1000, 600, 200)
    x = a.Body_Panel()
    print(x)
