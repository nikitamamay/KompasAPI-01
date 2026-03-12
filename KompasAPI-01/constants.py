"""
Константы и перечисления (enums) Компас API.
"""

#
# Файл 'constants.py'
# сгенерирован автоматически 2026-03-11 20:38:41
# с помощью 'https://github.com/nikitamamay/KompasAPI-stubs-generator'
#


class ButtonTypeEnum:  # buttontypeenum.html
    """ ## ButtonTypeEnum - Типы кнопок для элемента панели свойств "Набор кнопок" """
    ksPushButton  = 0
    """ Набор обычных нефиксируемых кнопок """
    ksCheckButton = 1
    """ Набор фиксируемых кнопок """
    ksRadioButton = 2
    """ Набор кнопок с возможностью фиксации только одной кнопки """


class CheckStateEnum:  # checkstateenum.html
    """ ## CheckStateEnum - Возможные состояния элемента управления Панели свойств "Переключатель состояния поля ввода" """
    ksCheckUndefined = 0
    """ Значение поля не задано; на переключателе пусто, """
    ksCheckCurrent   = 1
    """ Поле ввода активно; на переключателе значок "галочка", """
    ksCheckFixed     = 2
    """ Содержание поля ввода зафиксировано; на переключателе перекрестие. """
    ksCheckVariable  = 3
    """ Значение поля ввода задано; на переключателе пусто. """


class ControlTypeEnum:  # controltypeenum.html
    """ ## ControlTypeEnum - Типы элементов управления Панели свойств """
    ksControlUnknown         = 0
    """ Неизвестный тип """
    ksControlSeparator       = 1
    """
    Разделитель (сепаратор)

    IPropertySeparator
    """
    ksControlEditInt         = 2
    """
    Редактор целочисленных значений

    IPropertyEdit
    """
    ksControlEditReal        = 3
    """
    Редактор дробных значений

    IPropertyEdit
    """
    ksControlEditStr         = 4
    """
    Редактор строковых значений

    IPropertyEdit
    """
    ksControlListInt         = 5
    """
    Раскрывающийся список целочисленных значений

    IPropertyList
    """
    ksControlListReal        = 6
    """
    Раскрывающийся список дробных значений

    IPropertyList
    """
    ksControlListStr         = 7
    """
    Раскрывающийся список строковых значений

    IPropertyList
    """
    ksControlCheckBox        = 8
    """
    Опция

    IPropertyCheckBox
    """
    ksControlMultiButton     = 9
    """
    Набор кнопок

    IPropertyMultiButton
    """
    ksControlGrid            = 10
    """
    Сетка

    IPropertyGrid
    """
    ksControlSlideBox        = 11
    """
    Окно отображения слайда, растрового изображения, группы или файла документа КОМПАС

    IPropertySlideBox
    """
    ksControlUser            = 12
    """
    Пользовательский элемент управления

    IPropertyUserControl
    """
    ksControlTextButton      = 13
    """
    Кнопка с текстом

    IPropertyTextButton
    """
    ksControlSpinInt         = 14
    """
    Счетчик целочисленных значений с полем ввода

    IPropertySpinEdit
    """
    ksControlSpinReal        = 15
    """
    Счетчик дробных значений с полем ввода

    IPropertySpinEdit
    """
    ksControlFileName        = 16
    """
    Выбор файла

    IPropertyFileName
    """
    ksControlColor           = 17
    """
    Выбор цвета

    IPropertyColor
    """
    ksControlEditList        = 18
    """
    Список

    IPropertyEdit
    """
    ksControlEditLength      = 19
    """
    Редактор длины

    IPropertyEdit
    """
    ksControlEditAngle       = 20
    """
    Редактор угла

    IPropertyEdit
    """
    ksControlEditPoint       = 21
    """
    Редактор координат

    IPropertyEdit
    """
    ksControlListLength      = 22
    """
    Комбобокс длин

    IPropertyList
    """
    ksControlListAngle       = 23
    """
    Комбобокс углов

    IPropertyList
    """
    ksControlBmpList         = 24
    """
    Комбобокс со строкой и битмапом

    IPropertyBmpList
    """
    ksControlLibExplorer     = 25
    """ Отображение библиотеки документов """
    ksControlListScale       = 26
    """
    Комбобокс со списком масштабов

    IPropertyList
    """
    ksControlLineStyle       = 27
    """
    Комбобокс со списком стилей линий

    IPropertyStyleList
    """
    ksControlOpticalProps    = 28
    """
    Контрол оптических свойств

    IPropertyOpticalProps
    """
    ksControlEditCheckBox    = 29
    """
    Редактор строковых значений c чекбоксом

    IPropertyEdit
    """
    ksControlPointStyle      = 30
    """
    Комбобокс со списком стилей точек

    IPropertyStyleList
    """
    ksControlPointStyle3D    = 31
    """
    Комбобокс со списком стилей точек 3D

    IPropertyStyleList
    """
    ksControlLineStyle3D     = 32
    """
    Комбобокс со списком стилей линий 3D

    IPropertyStyleList
    """
    ksControlHatchStyle      = 33
    """
    Комбобокс со списком стилей штриховок

    IPropertyStyleList
    """
    ksControlGroupBegin      = 34
    """ Начало группы контролов """
    ksControlGroupEnd        = 35
    """ Конец группы контролов """
    ksControlTwinSwitcher    = 36
    """ Переключатель """
    ksControlPoint3D         = 37
    """ Точка 3D """
    ksControlPreviewText     = 38
    """ Предпросмотр текста """
    ksControlAggregateTriple = 40
    """ Составной контрол из трех контролов """
    ksControlBasePoint       = 41
    """ Базовая точка """
    ksControlLinkButton      = 42
    """ Набор кнопок в виде ссылок """
    ksControlMarking         = 43
    """ Контрол обозначение """
    ksControlReplaceList     = 44
    """ Список замен текстов """


class ConvertCoordTypeEnum:  # convertcoordtypeenum.html
    """ ## ConvertCoordTypeEnum - Типы преобразования логических координат в координаты документа """
    kcDocument     = 1
    """ В СК документа. """
    kcGeoView      = 2
    """ В геометрическую точку текущего вида. """
    kcCurrentPlane = 3
    """ В СК текущего плоского объекта. """


class DefaultFixTypeEnum:  # defaultfixtypeenum.html
    """ ## DefaultFixTypeEnum - Тип фиксированности для умолчательных элементов управления Панели свойств """
    ksAllFixOff = -1
    """ Все элементы управления расфиксированы """
    ksAllFix    = 0
    """ Все элементы управления фиксированы """
    ksPointFix  = 1
    """ Фиксирована точка """
    ksAngleFix  = 2
    """ Фиксирован угол """


class DocumentCloseOptions:  # documentcloseoptions.html
    """ ## DocumentCloseOptions - Действия при закрытии документа КОМПАС """
    kdDoNotSaveChanges    = 0
    """ Закрыть документ без сохранения, если документ был изменен. """
    kdSaveChanges         = 1
    """ Закрыть документ, сохранив сделанные изменения. """
    kdPromptToSaveChanges = 2
    """ Выдать запрос на сохранение документа, если он изменен. """


class DrawingObjectTypeEnum:  # drawingobjecttypeenum.html, objtypes.html
    """
    ## DrawingObjectTypeEnum - Типы графических объектов

    В API5 соответствует Типам объектов и интерфейсов....

    ----------

    ## Типы объектов графического документа; соответствие интерфейсов API5 и API7

    В таблице представлены типы графических объектов и соответствующие им интерфейсы API5 и API7.

    Для SHEET_ALLPARAM используются те же структуры, что и для ALLPARAM.
    """
    ksUnknown             = -1
    """
    Название объекта: Неизвестный объект

    ----------

    Название объекта: Неизвестный объект
    """
    ksAllObj              = 0
    """
    Название объекта: Все объекты

    ----------

    Название объекта: Все объекты

    Старый тип: ALL_OBJ
    """
    ksDrLineSeg           = 1
    """
    Название объекта: Отрезок

    Интерфейс параметров: ILineSegment

    ----------

    Название объекта: Отрезок

    Старый тип: LINESEG_OBJ

    Тип параметров: ALLPARAM

    Структура: LineSegParam

    Интерфейс API5: ksLineSegParam

    Интерфейс API7: ILineSegment
    """
    ksDrCircle            = 2
    """
    Название объекта: Окружность

    Интерфейс параметров: ICircle

    ----------

    Название объекта: Окружность

    Старый тип: CIRCLE_OBJ

    Тип параметров: ALLPARAM

    Структура: CircleParam

    Интерфейс API5: ksCircleParam

    Интерфейс API7: ICircle
    """
    ksDrArc               = 3
    """
    Название объекта: Дуга

    Интерфейс параметров: IArc

    ----------

    Название объекта: Дуга

    Старый тип: ARC_OBJ

    Тип параметров: ALLPARAM

    Структура: ArcParam

    Интерфейс API5: ksArcByAngleParam

    Интерфейс API7: IArc
    """
    ksDrDrawText          = 4
    """
    Название объекта: Текст на чертеже

    Интерфейс параметров: IDrawingText

    ----------

    Название объекта: Текст на чертеже

    Старый тип: TEXT_OBJ

    Тип параметров: ALLPARAM

    Структура: TextParam

    Интерфейс API5: ksTextParam

    Интерфейс API7: IDrawingText IText
    """
    ksDrPoint             = 5
    """
    Название объекта: Точка

    Интерфейс параметров: IPoint

    ----------

    Название объекта: Точка

    Старый тип: POINT_OBJ

    Тип параметров: ALLPARAM

    Структура: PointParam

    Интерфейс API5: ksPointParam

    Интерфейс API7: IPoint
    """
    ksDrHatch             = 7
    """
    Название объекта: Штриховка

    Интерфейс параметров: IHatch

    ----------

    Название объекта: Штриховка

    Старый тип: HATCH_OBJ

    Тип параметров: ALLPARAM

    Структура: HatchParam

    Интерфейс API5: ksHatchParam

    Интерфейс API7: IHatch IHatchParam
    """
    ksDrBezier            = 8
    """
    Название объекта: Bezier сплайн

    Интерфейс параметров: IBezier

    ----------

    Название объекта: Кривая Безье, сплайн

    Старый тип: BEZIER_OBJ

    Тип параметров: ALLPARAM

    Структура: BezierParam

    Интерфейс API5: ksBezierParam

    Интерфейс API7: IBezier
    """
    ksDrLDimension        = 9
    """
    Название объекта: Линейный размер

    Интерфейс параметров: ILineDimension

    ----------

    Название объекта: Линейный размер

    Старый тип: LDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: LdimParam

    Интерфейс API5: ksLDimParam

    Интерфейс API7: ILineDimension
    """
    ksDrADimension        = 10
    """
    Название объекта: Угловой размер

    Интерфейс параметров: IAngleDimension

    ----------

    Название объекта: угловой размер

    Старый тип: ADIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: AdimParam

    Интерфейс API5: ksADimParam

    Интерфейс API7: IArcDimension
    """
    ksDrDDimension        = 13
    """
    Название объекта: Диаметральный размер

    Интерфейс параметров: IDiametralDimension

    ----------

    Название объекта: Диаметральный размер

    Старый тип: DDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: RdimParam

    Интерфейс API5: ksRDimParam

    Интерфейс API7: IDiametralDimension
    """
    ksDrRDimension        = 14
    """
    Название объекта: Радиальный размер

    Интерфейс параметров: IRadialDimension

    ----------

    Название объекта: Радиальный размер

    Старый тип: RDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: RdimParam

    Интерфейс API5: ksRDimParam

    Интерфейс API7: IRadialDimension
    """
    ksDrRBreakDimension   = 15
    """
    Название объекта: Радиальный размер с изломом

    Интерфейс параметров: IBreakRadialDimension

    ----------

    Название объекта: Радиальный размер с изломом

    Старый тип: RBREAKDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: RbreakDimParam

    Интерфейс API5: ksRBreakDimParam

    Интерфейс API7: IBreakRadialDimension
    """
    ksDrRough             = 16
    """
    Название объекта: Шероховатость

    Интерфейс параметров: IRough

    ----------

    Название объекта: Шероховатость

    Старый тип: ROUGH_OBJ

    Тип параметров: ALLPARAM

    Структура: RoughParam

    Интерфейс API5: ksRoughParam

    Интерфейс API7: IRough
    """
    ksDrBase              = 17
    """
    Название объекта: База

    Интерфейс параметров: IBase

    ----------

    Название объекта: База

    Старый тип: BASE_OBJ

    Тип параметров: ALLPARAM

    Структура: BaseParam

    Интерфейс API5: ksBaseParam

    Интерфейс API7: IBase
    """
    ksDrWPointer          = 18
    """
    Название объекта: Стрелка вида

    Интерфейс параметров: IViewPointer

    ----------

    Название объекта: Стрелка направления взгляда

    Старый тип: WPOINTER_OBJ

    Тип параметров: ALLPARAM

    Структура: ViewPointerParam

    Интерфейс API5: ksViewPointerParam

    Интерфейс API7: IViewPointer
    """
    ksDrCut               = 19
    """
    Название объекта: Линия разреза

    Интерфейс параметров: ICutLine

    ----------

    Название объекта: Линия разреза

    Старый тип: CUT_OBJ

    Тип параметров: ALLPARAM

    Структура: CutLineParam

    Интерфейс API5: ksCutLineParam

    Интерфейс API7: ICutLine
    """
    ksDrLeader            = 20
    """
    Название объекта: Простая линия-выноска

    Интерфейс параметров: IBaseLeader

    ----------

    Название объекта: Простая линия выноска

    Старый тип: LEADER_OBJ

    Тип параметров: ALLPARAM

    Структура: LeaderParam

    Интерфейс API5: ksLeaderParam

    Интерфейс API7: ILeader
    """
    ksDrPosLeader         = 21
    """
    Название объекта: Линия-выноска для обозначения позиции

    Интерфейс параметров: IPositionLeader

    ----------

    Название объекта: Линия выноска для обозначения позиции

    Старый тип: POSLEADER_OBJ

    Тип параметров: ALLPARAMа

    Структура: PosLeaderParam

    Интерфейс API5: ksPosLeaderParam

    Интерфейс API7: IPositionLeader
    """
    ksDrBrandLeader       = 22
    """
    Название объекта: Линия-выноска для обозначения клеймения

    Интерфейс параметров: IBrandLeader

    ----------

    Название объекта: Линия выноска для обозначения клеймения

    Старый тип: BRANDLEADER_OBJ

    Тип параметров: ALLPARAM

    Структура: BrandLeaderParam

    Интерфейс API5: ksBrandLeaderParam

    Интерфейс API7: IBrandLeader
    """
    ksDrMarkerLeader      = 23
    """
    Название объекта: Линия-выноска для обозначения маркирования

    Интерфейс параметров: IMarkLeader

    ----------

    Название объекта: Линия выноска для обозначения маркирования

    Старый тип: MARKERLEADER_OBJ

    Тип параметров: ALLPARAM

    Структура: MarkerLeaderParam

    Интерфейс API5: ksMarkerLeaderParam

    Интерфейс API7: IMarkLeader
    """
    ksDrTolerance         = 24
    """
    Название объекта: Допуск формы

    Интерфейс параметров: ITolerance

    ----------

    Название объекта: Допуск формы

    Старый тип: TOLERANCE_OBJ

    Тип параметров: ALLPARAM

    Структура: ksTolerancePar

    Интерфейс API5: ksToleranceParam

    Интерфейс API7: ITolerance
    """
    ksDrTable             = 25
    """
    Название объекта: Таблица

    Интерфейс параметров: ITable

    ----------

    Название объекта: Таблица

    Старый тип: TABLE_OBJ

    Тип параметров: ALLPARAM

    Структура: нереализовано

    Интерфейс API5: нереализовано

    Интерфейс API7: IDrawingTable ITable
    """
    ksDrContour           = 26
    """
    Название объекта: Контур

    Интерфейс параметров: IContour

    ----------

    Название объекта: Контур

    Старый тип: CONTOUR_OBJ

    Тип параметров: ALLPARAM

    Структура: short (стиль)

    Интерфейс API5: ksContourParam

    Интерфейс API7: IDrawingContour IContour
    """
    ksDrMacro             = 27
    """
    Название объекта: Нетипизированный макроэлемент

    Интерфейс параметров: IMacroObjec

    ----------

    Название объекта: Нетипизированный макроэлемент

    Старый тип: MACRO_OBJ

    Тип параметров: ALLPARAM

    Структура: нереализовано

    Интерфейс API5: нереализовано

    Интерфейс API7: IMacroObject
    """
    ksDrLine              = 28
    """
    Название объекта: Линия

    Интерфейс параметров: ILine

    ----------

    Название объекта: Линия

    Старый тип: LINE_OBJ

    Тип параметров: ALLPARAM

    Структура: LineParam

    Интерфейс API5: ksLineParam

    Интерфейс API7: ILine
    """
    ksLayer               = 29
    """
    Название объекта: Слой

    Интерфейс параметров: ILayer

    ----------

    Название объекта: Слой

    Старый тип: LAYER_OBJ

    Тип параметров: ALLPARAM

    Структура: LayerParam

    Интерфейс API5: ksLayerParam

    Интерфейс API7: ILayer
    """
    ksDrFragment          = 30
    """
    Название объекта: Вставной фрагмент

    Интерфейс параметров: ksFragment

    ----------

    Название объекта: Вставленный фрагмент

    Старый тип: FRAGMENT_OBJ

    Тип параметров: ALLPARAM

    Структура: InsertFragmentParamEx

    Интерфейс API5: ksInsertFragmentParam

    Интерфейс API7: IInsertionFragment
    """
    ksDrPolyline          = 31
    """
    Название объекта: Полилиния

    Интерфейс параметров: IPolyLine

    ----------

    Название объекта: Полилиния

    Старый тип: POLYLINE_OBJ

    Тип параметров: ALLPARAM

    Структура: PolylineParamEx

    Интерфейс API5: ksPolylineParam

    Интерфейс API7: IPolyline
    """
    ksDrEllipse           = 32
    """
    Название объекта: Эллипс

    Интерфейс параметров: IEllipse

    ----------

    Название объекта: Эллипс

    Старый тип: ELLIPSE_OBJ

    Тип параметров: ALLPARAM

    Структура: EllipseParam

    Интерфейс API5: ksEllipseParam

    Интерфейс API7: IEllipse
    """
    ksDrNurbs             = 33
    """
    Название объекта: NURBS сплайн

    Интерфейс параметров: INurbs

    ----------

    Название объекта: NURBS-кривая по полюсам

    Старый тип: NURBS_OBJ

    Тип параметров: ALLPARAM

    Структура: NurbsParam

    Интерфейс API5: ksNurbsParam

    Интерфейс API7: INurbs
    """
    ksDrEllipseArc        = 34
    """
    Название объекта: Дуга эллипса

    Интерфейс параметров: IEllipseArc

    ----------

    Название объекта: Дуга эллипса

    Старый тип: ELLIPSE_ARC_OBJ

    Тип параметров: ALLPARAM

    Структура: EllipseArcParam

    Интерфейс API5: ksEllipseArcParam

    Интерфейс API7: IEllipseArc
    """
    ksDrRectangle         = 35
    """
    Название объекта: Прямоугольник

    Интерфейс параметров: IRectangle

    ----------

    Название объекта: Прямоугольник

    Старый тип: RECTANGLE_OBJ

    Тип параметров: ALLPARAM

    Структура: RectangleParam

    Интерфейс API5: ksRectangleParam

    Интерфейс API7: IRectangle
    """
    ksDrRegularPolygon    = 36
    """
    Название объекта: Многоугольник

    Интерфейс параметров: IRegularPolygon

    ----------

    Название объекта: Многоугольник

    Старый тип: REGULARPOLYGON_OBJ

    Тип параметров: ALLPARAM

    Структура: RegularPolygonParam

    Интерфейс API5: ksRegularPolygonParam

    Интерфейс API7: IRegularPolygon
    """
    ksDrEquid             = 37
    """
    Название объекта: Эквидистанта

    Интерфейс параметров: IEquidistant

    ----------

    Название объекта: Эквидистанта

    Старый тип: EQUID_OBJ

    Тип параметров: ALLPARAM

    Структура: EquidistantParam

    Интерфейс API5: ksEquidistantParam

    Интерфейс API7: IEquidistant
    """
    ksDrLBreakDimension   = 38
    """
    Название объекта: Линейный размер с обрывом

    Интерфейс параметров: IBreakLineDimension

    ----------

    Название объекта: Линейный размер с обрывом

    Старый тип: LBREAKDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: LbreakDimParam

    Интерфейс API5: ksLBreakDimParam

    Интерфейс API7: IBreakLineDimension
    """
    ksDrABreakDimension   = 39
    """
    Название объекта: Угловой размер с обрывом

    Интерфейс параметров: IBreakAngleDimension

    ----------

    Название объекта: Угловой размер с обрывом

    Старый тип: ABREAKDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: AbreakDimParam

    Интерфейс API5: ksABreakDimParam

    Интерфейс API7: IBreakAngleDimension
    """
    ksDrOrdinateDimension = 40
    """
    Название объекта: Размер высоты

    Интерфейс параметров: IHeightDimension

    ----------

    Название объекта: Размер высоты

    Старый тип: ORDINATEDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: OrdinatedDimParam

    Интерфейс API5: ksOrdinatedDimParam

    Интерфейс API7: IHeightDimension
    """
    ksDrColorFill         = 41
    """
    Название объекта: Фоновая заливка цветом

    Интерфейс параметров: IColouring

    ----------

    Название объекта: Фоновая заливка цветом

    Старый тип: COLORFILL_OBJ

    Тип параметров: ALLPARAM

    Структура: long (цвет)

    Интерфейс API5: ksLtVariant (цвет)

    Интерфейс API7: IColouring
    """
    ksDrCentreMarker      = 42
    """
    Название объекта: Обозначение центра

    Интерфейс параметров: ICentreMarker

    ----------

    Название объекта: Обозначение центра

    Старый тип: CENTREMARKER_OBJ

    Тип параметров: ALLPARAM

    Структура: CentreParam

    Интерфейс API5: ksCentreParam

    Интерфейс API7: ICentreMarker IAxisLineParam
    """
    ksDrArcDimension      = 43
    """
    Название объекта: Размер длины дуги

    Интерфейс параметров: IArcDimension

    ----------

    Название объекта: Размер длины дуги

    Старый тип: ARCDIMENSION_OBJ

    Тип параметров: ALLPARAM

    Структура: нереализовано

    Интерфейс API5: нереализовано

    Интерфейс API7: IArcDimension
    """
    ksDrRaster            = 45
    """
    Название объекта: Растровый объект

    Интерфейс параметров: IRaster

    ----------

    Название объекта: Растровый объект

    Старый тип: RASTER_OBJ

    Тип параметров: ALLPARAM

    Структура: RasterParam

    Интерфейс API5: ksRasterParam

    Интерфейс API7: IRaster
    """
    ksDrChangeLeader      = 46
    """
    Название объекта: Обозначение изменения

    Интерфейс параметров: IChangeLeader

    ----------

    Название объекта: Обозначение изменения

    Старый тип: CHANGE_LEADER_OBJ

    Тип параметров: ALLPARAM

    Структура: ChangeLeaderParam

    Интерфейс API5: ksChangeLeaderParam

    Интерфейс API7: IChangeLeader
    """
    ksDrRemoteElement     = 47
    """
    Название объекта: Выносной элемент

    Интерфейс параметров: IRemoteElement

    ----------

    Название объекта: Выносной элемент

    Старый тип: REMOTE_ELEMENT_OBJ

    Тип параметров: ALLPARAM

    Структура: RemoteElementParam

    Интерфейс API5: ksRemoteElementParam

    Интерфейс API7: IRemoteElement
    """
    ksDrAxisLine          = 48
    """
    Название объекта: Осевая линия

    Интерфейс параметров: IAxisLine

    ----------

    Название объекта: Осевая линия

    Старый тип: AXISLINE_OBJ

    Тип параметров: ALLPARAM

    Структура: AxisLineParam

    Интерфейс API5: ksAxisLineParam

    Интерфейс API7: IAxisLine IAxisLineParam
    """
    ksDrOLEObject         = 49
    """
    Название объекта: Вставка OLE объекта

    Интерфейс параметров: IOleDrawingObject

    ----------

    Название объекта: Вставка OLE объекта

    Старый тип: OLEOBJECT_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IOleDrawingObject
    """
    ksDrUnitNumber        = 50
    """
    Название объекта: Номер узла

    Интерфейс параметров: IUnitNumber

    ----------

    Название объекта: Номер узла

    Старый тип: KNOTNUMBER_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IUnitMarking
    """
    ksDrBrace             = 51
    """
    Название объекта: Фигурная скобка

    Интерфейс параметров: IBrace

    ----------

    Название объекта: Фигурная скобка

    Старый тип: BRACE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IBrace
    """
    ksDrMarkOnLeader      = 52
    """
    Название объекта: Марка/позиционное обозначение с линией-выноской

    Интерфейс параметров: IMarkOnLeader

    ----------

    Название объекта: Марка/Марка/позиционное обозначение с линией-выноской

    Старый тип: POSNUM_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IMarkOnLeader
    """
    ksDrMarkOnLine        = 53
    """
    Название объекта: Марка/позиционное обозначение на линии

    Интерфейс параметров: IMarkOnLine

    ----------

    Название объекта: Марка/позиционное обозначение на линии

    Старый тип: MARKONLDR_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IMarkOnLine
    """
    ksDrMarkInsideForm    = 54
    """
    Название объекта: Марка/позиционное обозначение без линии-выноски

    Интерфейс параметров: IMarkInsideForm

    ----------

    Название объекта: Марка/позиционное обозначение без линии-выноски

    Старый тип: MARKWOLDR_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IMarkInsideForm
    """
    ksDrWaveLine          = 55
    """
    Название объекта: Волнистая линия

    Интерфейс параметров: IWaveLine

    ----------

    Название объекта: Волнистая линияВолнистая

    Старый тип: WAVELINE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IWaveLine
    """
    ksDrStraightAxis      = 56
    """
    Название объекта: Прямая ось

    Интерфейс параметров: IStraightAxis

    ----------

    Название объекта: Прямая ось

    Старый тип: DIRAXIS_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IStraightAxis
    """
    ksDrBrokenLine        = 57
    """
    Название объекта: Линия обрыва с изломами

    Интерфейс параметров: IBrokenLine

    ----------

    Название объекта: Линия обрыва с изломами

    Старый тип: BROKENLINE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IBrokenLine
    """
    ksDrCircleAxis        = 58
    """
    Название объекта: Круговая ось

    Интерфейс параметров: ICircleAxis

    ----------

    Название объекта: Круговая ось

    Старый тип: CIRCLEAXIS_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: ICircleAxis
    """
    ksDrArcAxis           = 59
    """
    Название объекта: Дуговая ось

    Интерфейс параметров: IArcAxis

    ----------

    Название объекта: Дуговая ось

    Старый тип: ARCAXIS_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IArcAxis
    """
    ksDrCutUnitMarking    = 60
    """
    Название объекта: Обозначение узла в сечении

    Интерфейс параметров: ICutUnitMarking

    ----------

    Название объекта: Обозначение узла в сечении

    Старый тип: CUTUNITMARKING

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: ICutUnitMarking
    """
    ksDrUnitMarking       = 61
    """
    Название объекта: Обозначение узла

    Интерфейс параметров: IUnitMarking

    ----------

    Название объекта: Обозначение узла

    Старый тип: UNITMARKING

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IUnitMarking
    """
    ksDrMultiTextLeader   = 62
    """
    Название объекта: Выносная надпись к многослойным конструкциям

    Интерфейс параметров: IMultiTextLeader
    """
    ksDrExternalView      = 63
    """
    Название объекта: Вставка внешнего вида

    Интерфейс параметров: IInsertionView

    ----------

    Название объекта: Вставка внешнего вида

    Старый тип: EXTERNALVIEW_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IInsertionView
    """
    ksDrAnnLineSeg        = 64
    """
    Название объекта: Аннотационный отрезок

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационный отрезок

    Старый тип: ANNLINESEG_OBJ

    Тип параметров: ALLPARAM

    Структура: LineSegParam

    Интерфейс API5: ksLineSegParam

    Интерфейс API7: ILineSegment IAnnotativeObject
    """
    ksDrAnnCircle         = 65
    """
    Название объекта: Аннотационная окружность

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационная окружность

    Старый тип: ANNCIRCLE_OBJ

    Тип параметров: ALLPARAM

    Структура: CircleParam

    Интерфейс API5: ksCircleParam

    Интерфейс API7: ICircle IAnnotativeObject
    """
    ksDrAnnEllipse        = 66
    """
    Название объекта: Аннотационный эллипс

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационный эллипс

    Старый тип: ANNELLIPSE_OBJ

    Тип параметров: ALLPARAM

    Структура: EllipseParam

    Интерфейс API5: ksEllipseParam

    Интерфейс API7: IEllipse IAnnotativeObject
    """
    ksDrAnnArc            = 67
    """
    Название объекта: Аннотационная дуга

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационная дуга

    Старый тип: ANNARC_OBJ

    Тип параметров: ALLPARAM

    Структура: ArcParam

    Интерфейс API5: ksArcByAngleParam

    Интерфейс API7: IArc IAnnotativeObject
    """
    ksDrAnnEllipseArc     = 68
    """
    Название объекта: Аннотационная дуга эллипса

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационная дуга эллипса

    Старый тип: ANNELLIPSE_ARC_OBJ

    Тип параметров: ALLPARAM

    Структура: EllipseArcParam

    Интерфейс API5: ksEllipseArcParam

    Интерфейс API7: IEllipseArc IAnnotativeObject
    """
    ksDrAnnPolyline       = 69
    """
    Название объекта: Аннотационная полилиния

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационная полилиния

    Старый тип: ANNPOLYLINE_OBJ

    Тип параметров: ALLPARAM

    Структура: PolylineParamEx

    Интерфейс API5: ksPolylineParam

    Интерфейс API7: IPolyline IAnnotativeObject
    """
    ksDrAnnPoint          = 70
    """
    Название объекта: Аннотационная точка

    Интерфейс параметров: IAnnotativeObject

    ----------

    Название объекта: Аннотационная точка

    Старый тип: ANNPOINT_OBJ

    Тип параметров: ALLPARAM

    Структура: PointParam

    Интерфейс API5: ksPointParam

    Интерфейс API7: IPoint IAnnotativeObject
    """
    ksDrMultiLine         = 72
    """
    Название объекта: Мультилиния

    Интерфейс параметров: IMultiline

    ----------

    Название объекта: Мультилиния

    Старый тип: MULTILINE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IMultiline
    """
    ksDrBuildingCutLine   = 73
    """
    Название объекта: Линия разреза/сечения для СПДС

    Интерфейс параметров: ICutLine

    ----------

    Название объекта: Линия разреза/сечения для СПДС

    Старый тип: BUILDINGCUTLINE_OBJ

    Тип параметров: ALLPARAM

    Структура: CutLineParam

    Интерфейс API5: ksCutLineParam

    Интерфейс API7: ICutLine
    """
    ksDrAttachedLeader    = 74
    """
    Название объекта: Присоединенная линия выноски (не имеет текстов)

    Интерфейс параметров: ILeader

    ----------

    Название объекта: Присоединенная линия выноски

    Старый тип: ATTACHED_LEADER_OBJ

    Тип параметров: ALLPARAM

    Структура: LeaderParam

    Интерфейс API5: ksLeaderParam

    Интерфейс API7: ILeader
    """
    ksDrConditionCrossing = 75
    """
    Название объекта: Условное пересечение

    ----------

    Название объекта: Условное пересечение

    Старый тип: CONDITIONCROSSING_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IConditionCrossing
    """
    ksReportTable         = 76
    """
    Название объекта: Ассоциативная таблица отчета

    Интерфейс параметров: IAssociationTable

    ----------

    Название объекта: Ассоциативная таблица отчета

    Старый тип: REPORTTABLE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IAssociationTable
    """
    ksEmbodimentsTable    = 77
    """
    Название объекта: Таблица иcполнений

    Интерфейс параметров: IAssociationTable

    ----------

    Название объекта: Таблица исполнений

    Старый тип: EMBODIMENTSTABLE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IAssociationTable
    """
    ksDrSpecialCurve      = 78
    """ Название объекта: Кривая общего вида """
    ksArrayParamTable     = 79
    """
    Название объекта: Таблица параметров массива

    Интерфейс параметров: IAssociationTable

    ----------

    Название объекта: Таблица параметров массива

    Старый тип: ARRAYPARAMTABLE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IAssociationTable
    """
    ksDrNurbsByPoints     = 80
    """
    Название объекта: NURBS-кривая по точкам

    ----------

    Название объекта: NURBS-кривая по точкам

    Старый тип: NURBS_BY_POINTS_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: INurbsByPoints INurbs
    """
    ksDrConicCurve        = 81
    """
    Название объекта: Коническая кривая

    ----------

    Название объекта: Коническая кривая

    Старый тип: CONIC_CURVE_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IConicCurve
    """
    ksDrConicCurve4Point  = 82
    """ Название объекта: Коническая кривая по 4 точкам и направлению """
    ksDrConicCurve5Point  = 83
    """ Название объекта: Коническая кривая по 5 точкам """
    ksView                = 123
    """
    Название объекта: Вид

    Интерфейс параметров: iView

    ----------

    Название объекта: Вид

    Старый тип: VIEW_OBJ

    Тип параметров: ALLPARAM

    Структура: ViewParam

    Интерфейс API5: ksViewParam

    Интерфейс API7: IView
    """
    ksDrMultiTextLeade    = 62
    """
    Название объекта: Выносная надпись к многослойным конструкциям

    Старый тип: MULTITEXTLEADER

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: IMultiTextLeade
    """
    ksDrAnnText           = 71
    """
    Название объекта: Текст с аннатационной точкой привязки

    Старый тип: ANNTEXT_OBJ

    Тип параметров: ALLPARAM

    Структура: TextParam

    Интерфейс API5: ksTextParam

    Интерфейс API7: IDrawingText IText IAnnotativeObject
    """
    ksDrCircularCentres   = 84
    """
    Название объекта: Круговая сетка центров

    Старый тип: CIRCULAR_CENTRES_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: ICircularCentres
    """
    ksDrLinearCentres     = 85
    """
    Название объекта: Линейная сетка центров

    Старый тип: LINEAR_CENTRES_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: ILinearCentres
    """
    ksDrEllipseArcAxis    = 86
    """
    Название объекта: Дуговая осевая линия

    Старый тип: ELLIPSE_ARC_AXIS_OBJ

    Тип параметров: ALLPARAM

    Структура: не реализовано

    Интерфейс API5: не реализовано

    Интерфейс API7: не реализовано
    """


class DocumentTypeEnum:  # documenttypeenum.html
    """ ## DocumentTypeEnum - Типы документов КОМПАС """
    ksDocumentUnknown            = 0
    """ Неизвестный тип """
    ksDocumentDrawing            = 1
    """ Чертеж """
    ksDocumentFragment           = 2
    """ Фрагмент """
    ksDocumentSpecification      = 3
    """ Спецификация """
    ksDocumentPart               = 4
    """ Деталь """
    ksDocumentAssembly           = 5
    """ Сборка """
    ksDocumentTextual            = 6
    """ Текстовый документ """
    ksDocumentTechnologyAssembly = 7
    """ Технологическая сборка """


class FilterConditionStateEnum:  # filterconditionstateenum.html
    """ ## FilterConditionStateEnum - Состояние параметрав условии фильтрации слоев """
    ksStateUndefined = -1
    """ Состояние не определено """
    ksStateFALSE     = 0
    """ Состояние FALSE """
    ksStateTRUE      = 1
    """ Состояние TRUE """


class FrameRegimeEnum:  # frameregimeenum.html
    """ ## FrameRegimeEnum - Режим отображения окна """
    ksFrameMinimize = 0
    """ Свернуть окно """
    ksFrameMaximize = 1
    """ Развернуть окно """
    ksFrameRestore  = 2
    """ Восстановить окно """


class KompasAPIObjectTypeEnum:  # kompasapiobjecttypeenum.html
    """ ## KompasAPIObjectTypeEnum - Типы объектов КОМПАС API """
    ksObjectUnknown                                         = 0
    """ Неизвестный тип """
    ksObjectApplication                                     = 10001
    """ Приложение - основной объект API """
    ksObjectDocuments                                       = 10002
    """ Коллекция документов, открытых в приложении """
    ksObjectKompasError                                     = 10003
    """ Информация о ошибке системы КОМПАС """
    ksObjectProcessParam                                    = 10004
    """ Параметры процесса """
    ksObjectPropertyTabs                                    = 10005
    """ Коллекция закладок панели свойств """
    ksObjectPropertyTab                                     = 10006
    """ Закладка панели свойств """
    ksObjectPropertyControls                                = 10007
    """ Коллекция элементов управления вкладки Панели свойств """
    ksObjectPropertySeparator                               = 10008
    """ Разделитель (сепаратор) """
    ksObjectPropertyEdit                                    = 10009
    """ Редактор """
    ksObjectPropertyList                                    = 10010
    """ Раскрывающийся список """
    ksObjectPropertyCheckBox                                = 10011
    """ Опция """
    ksObjectPropertyMultiButton                             = 10012
    """ Набор кнопок """
    ksObjectPropertyUserControl                             = 10013
    """ Пользовательский элемент управления """
    ksObjectPropertyBmpList                                 = 10014
    """ Комбобокс со строкой и битмапом """
    ksObjectPropertySlideBox                                = 10016
    """ Окно отображения слайда, растрового изображения, файла документа КОМПАС или группы файлов. """
    ksObjectPropertyGrid                                    = 10017
    """ Сетка """
    ksObjectDocumentFrame                                   = 10018
    """ Окно документа """
    ksObjectDocumentFrames                                  = 10019
    """ Коллекция окон документа """
    ksObjectPropertyManager                                 = 10020
    """ Панель свойств """
    ksObjectDrawingDocument                                 = 10021
    """ Документ - Чертеж """
    ksObjectFragmentDocument                                = 10022
    """ Документ - Фрагмент """
    ksObjectSpcDocument                                     = 10023
    """ Документ - Спецификация """
    ksObjectPartDocument                                    = 10024
    """ Документ - Деталь """
    ksObjectAssemblyDocument                                = 10025
    """ Документ - Сборка """
    ksObjectTextDocument                                    = 10026
    """ Документ - Текстовый """
    ksObjectPropertyTextButton                              = 10027
    """ Кнопка с текстом """
    ksObjectPropertySpinEdit                                = 10028
    """ Поле ввода со счетчиком """
    ksObjectViewsAndLayersManager                           = 10029
    """ Менеджер слоев и видов графического документа """
    ksObjectViews                                           = 10030
    """ Коллекция видов """
    ksObjectView                                            = 10031
    """ Вид """
    ksObjectAssociationView                                 = 10032
    """ Ассоциативный вид """
    ksObjectLayerGroups                                     = 10033
    """ Коллекция групп слоев """
    ksObjectDrawingOblects                                  = 10034
    """ Коллекция объектов графического документа """
    ksObjectLayerGroup                                      = 10035
    """ Группа слоев """
    ksObjectLayers                                          = 10036
    """ Коллекция слоев """
    ksObjectLayer                                           = 10037
    """ Слой """
    ksObjectLayerFilterCondition                            = 10038
    """ Условие фильтрации слоев """
    ksObjectLayerFilterConditions                           = 10039
    """ Коллекция условий фильтрации слоев """
    ksObjectDocumentSettings                                = 10040
    """ Настройки документа """
    ksObjectDocument2DSettings                              = 10041
    """ Настройки графического документа """
    ksObjectDrawingDocumentSettings                         = 10042
    """ Настройки чертежа """
    ksObjectFragmentDocumentSettings                        = 10043
    """ Настройки фрагмента """
    ksObjectDocument3DSettings                              = 10045
    """ Настройки 3D документа """
    ksObjectFormatLabelRules                                = 10046
    """ Правила формирования отображаемых имен объектов в дереве документа """
    ksObjectLibraryManager                                  = 10050
    """ Менеджер библиотек """
    ksObjectProcedure                                       = 10051
    """ Процедура прикладной библиотеки """
    ksObjectProceduresLibraries                             = 10052
    """ Коллекция прикладных библиотек """
    ksObjectProceduresLibrary                               = 10053
    """ Прикладная библиотека """
    ksObjectProcedures                                      = 10054
    """ Коллекция процедур прикладной библиотеки """
    ksObjectInsertsLibraries                                = 10055
    """ Коллекция библиотек элементов (документов) """
    ksObjectInsertsLibrary                                  = 10056
    """ Библиотека элементов (документов) """
    ksObjectInserts                                         = 10057
    """ Коллекция элементов (документов) библиотеки элементов (документов) """
    ksObjectInsert                                          = 10058
    """ Элемент библиотеки элементов (документов) """
    ksObjectSpecificationDescriptions                       = 10059
    """ Коллекция описаний спецификации """
    ksObjectSpecificationDescription                        = 10060
    """ Описание спецификации """
    ksObjectSpecificationStyle                              = 10061
    """ Стиль спецификации """
    ksObjectSpecificationColumnStyles                       = 10062
    """ Коллекция стилей колонок спецификации """
    ksObjectSpecificationColumnStyle                        = 10063
    """ Стиль колонки спецификации """
    ksObjectSpecificationSectionStyles                      = 10064
    """ Коллекция стилей разделов спецификации """
    ksObjectSpecificationSectionStyle                       = 10065
    """ Стиль раздела спецификации """
    ksObjectSpecificationTuning                             = 10066
    """ Настройки спецификации """
    ksObjectSpecificationTuningSections                     = 10067
    """ Коллекция настроек разделов спецификации """
    ksObjectSpecificationTuningSection                      = 10068
    """ Настройка раздела спецификации """
    ksObjectSpecificationSubsections                        = 10069
    """ Коллекция подразделов спецификации """
    ksObjectSpecificationSubsection                         = 10070
    """ Подраздел спецификации """
    ksObjectAdditionalBlockStyles                           = 10071
    """ Коллекция стилей блоков дополнительных разделов """
    ksObjectAdditionalBlockStyle                            = 10072
    """ Стиль блока дополнительных разделов """
    ksObjectAdditionalBlockTunings                          = 10073
    """ Коллекция настроек блоков дополнительных разделов """
    ksObjectAdditionalBlockTuning                           = 10074
    """ Настройка блока дополнительных разделов """
    ksObjectAdditionalBlockSectionTunings                   = 10075
    """ Коллекция настроек разделов блока дополнительных разделов """
    ksObjectAdditionalBlockSectionTuning                    = 10076
    """ Настройка раздела блока дополнительных разделов """
    ksObjectSheetFormat                                     = 10077
    """ Формат листа """
    ksObjectTextStyle                                       = 10078
    """ Параметры стиля текста """
    ksObjectFont                                            = 10079
    """ Параметры шрифта """
    ksObjectTabulators                                      = 10080
    """ Коллекция позиции табуляторов """
    ksObjectTabulator                                       = 10081
    """ Позиция табулятора """
    ksObjectSpecificationBaseObjects                        = 10083
    """ Коллекция базовых объектов спецификации """
    ksObjectSpecificationCommentObjects                     = 10084
    """ Коллекция вспомогательных объектов спецификации """
    ksObjectSpecificationObject                             = 10085
    """ Объект спецификации """
    ksObjectSpecificationBaseObject                         = 10086
    """ Базовый объект спецификации """
    ksObjectSpecificationCommentObject                      = 10087
    """ Вспомогательный объект спецификации """
    ksObjectSpecificationColumns                            = 10088
    """ Коллекция колонок объекта спецификации """
    ksObjectSpecificationColumn                             = 10089
    """ Колонка объекта спецификации """
    ksObjectSpecificationColumnItems                        = 10090
    """ Коллекция элементов колонки объекта спецификации """
    ksObjectSpecificationColumnItem                         = 10091
    """ Элемент колонки объекта спецификации """
    ksObjectAttachedDocuments                               = 10092
    """ Коллекция присоединенных документов к объекту спецификации """
    ksObjectAttachedDocument                                = 10093
    """ Параметры присоединенного документа к объекту спецификации """
    ksObjectPropertyFileName                                = 10094
    """ Выбор файла """
    ksObjectPropertyEditList                                = 10095
    """ Список """
    ksObjectLayoutSheets                                    = 10096
    """ Коллекция листов оформления """
    ksObjectLayoutSheet                                     = 10097
    """ Параметры листа оформления """
    ksObjectConverter                                       = 10098
    """ Конвертер КОМПАС-документов """
    ksObjectCheckSum                                        = 10099
    """ Контрольная сумма """
    ksObjectProgressBar                                     = 10100
    """ Индикатор процесса """
    ksObjectPropertyEditList                                = 10101
    """ Список """
    ksObjectPropertyLibExplorer                             = 10102
    """ Отображение библиотеки документов """
    ksObjectVariable7                                       = 10103
    """ Параметрическая переменная модели """
    ksObjectInsertionParameters                             = 10104
    """ Параметры вставки фрагмента и растрового объекта в текст """
    ksObjectMath2D                                          = 10105
    """ Математика 2D """
    ksObjectSelectionManager                                = 10106
    """ Менеджер селектированных объектов """
    ksObjectChooseManager                                   = 10107
    """ Менеджер выбора (подсветки) объектов """
    ksObjectStamp                                           = 10108
    """ Штамп """
    ksObjectPropertyStyleList                               = 10109
    """ Комбобокс со стилем """
    ksObjectPrintJob                                        = 10110
    """ Задание на печать """
    ksObjectPrintJob_Sheet                                  = 10111
    """ Задание на печать::Интерфейс листа документа """
    ksObjectPropertyOpticalProps                            = 10112
    """ Контрол оптических свойств """
    ksObjectPropertyEditCheckBox                            = 10113
    """ Объединенный редактор с чекбоксом """
    ksObjectPropertyGroupBegin                              = 10116
    """ Начало группы контролов """
    ksObjectPropertyGroupEnd                                = 10117
    """ Конец группы контролов """
    ksObjectThreadPattern                                   = 10118
    """ Параметры стандарта резьбы """
    ksObjectThreadDialogParam                               = 10119
    """ Параметры диалога выбора стандарта резьбы """
    ksObjectPropertyPreviewText                             = 10120
    """ Предпросмотр текста """
    ksObjectPropertyAggregateControl                        = 10121
    """ Составной контрол """
    ksObjectPropertyLinkButton                              = 10122
    """ Набор кнопок в виде ссылок """
    ksObjectPropertyMarking                                 = 10123
    """ Контрол обозначение """
    ksObjectContentDialogParam                              = 10124
    """ Параметры диалога с произвольным наполнением """
    ksObjectPropertyBasePoint                               = 10125
    """ Базовая точка """
    ksObjectTextDocumentSection                             = 10126
    """ Раздел текстового документа """
    ksIntervalVariable                                      = 10127
    """ Интервальная переменная """
    ksSpecificationObjectCreateParam                        = 10128
    """ Расширенные параметры создания объекта спецификации """
    ksObjectPropertyReplaceList                             = 10129
    """ Элемент панели свойств - Список замен текстов """
    ksObjectRasterConvertParameters                         = 10130
    """ Параметры для конвертации в растровые форматы """
    ksObjectAdditionConvertParameters                       = 10131
    """ Параметры для конвертации в дополнительные форматы """
    ksObjectCommonNameObject                                = 10132
    """ Объект спецификации - Общее наименование """
    ksObjectUserDataStoragesMng                             = 10500
    """ Менеджер пользовательских хранилищ """
    ksObjectUserDataStorages                                = 10501
    """ Коллекция объектов пользовательского хранилища """
    ksObjectUserDataStorage                                 = 10502
    """ Объект пользовательского хранилища данных """
    ksObjectAttribute                                       = 10504
    """ Атрибут """
    ksObjectColumnInfo                                      = 10505
    """ Параметры столбца табличного атрибута """
    ksObjectAttributeType                                   = 10506
    """ Параметры типа атрибута """
    ksObjectAttrTypeMng                                     = 10507
    """ Менеджер типов атрибутов """
    ksObjectProperty                                        = 10508
    """ Свойство """
    ksObjectPropertyMng                                     = 10509
    """ Менеджер свойств """
    ksObjectReportProcess                                   = 10510
    """ Интерфейс для управления процессом Создать отчет """
    ksObjectReport                                          = 10511
    """ Интерфейс Отчета """
    ksObjectReportStyle                                     = 10512
    """ Интерфейс стиля Отчета """
    ksObjectReportStyleColumn                               = 10513
    """ Интерфейс колонки стиля Отчета """
    ksObjectPropertyKeeper                                  = 10514
    """ Объект дерева СЧИ """
    ksObjectStyles                                          = 10515
    """ Коллекция стилей """
    ksObjectCurvesStyles                                    = 10516
    """ Коллекция стилей кривых """
    ksObjectHatchsStyles                                    = 10517
    """ Коллекция стилей штриховок """
    ksObjectTextsStyles                                     = 10518
    """ Коллекция стилей текстов """
    ksObjectStyle                                           = 10519
    """ Cтиль """
    ksObjectCurveStyle                                      = 10520
    """ Стиль кривой """
    ksObjectHatchStyle                                      = 10521
    """ Стиль штриховки """
    ksObjectSpecificationStyles                             = 10522
    """ Коллекция стилей спецификации """
    ksObjectText                                            = 10700
    """ Текст """
    ksObjectTextLine                                        = 10701
    """ Cтрока текста """
    ksObjectTextItem                                        = 10702
    """ Компонент строки текста """
    ksObjectTableCell                                       = 10703
    """ Ячейка таблицы """
    ksObjectExternalTessellation                            = 10704
    """ Объект с внешней триангуляцией """
    ksObjectExternalGDI                                     = 10709
    """ Внешний GDI-объект """
    ksObjectLibArraySettings                                = 10710
    """ Интерфейс для выбора состояний библиотек в настройках """
    ksObjectTextTable                                       = 10711
    """ Таблица в тексте текстового документа """
    ksObjectPropertyTwinSwitcher                            = 10713
    """ Переключатель """
    ksObjectPropertyPoint3D                                 = 10714
    """ Точка 3D """
    ksObjectPart7                                           = 11000
    """ 3D компонент """
    ksObjectModelObject                                     = 11001
    """ 3D объект """
    ks3dMateConstraint                                      = 11002
    """ 3D сопряжение """
    ksObjectParts7                                          = 11003
    """ Коллекция 3D компонентов """
    ksObjectVariableTable                                   = 11004
    """ Таблица переменных """
    ksObjectProgressBar                                     = 11005
    """ Индикатор прогресса """
    ksObjectLineDimensions3D                                = 11030
    """ Коллекция линейных размеров 3D """
    ksObjectBaseLineDimension3D                             = 11031
    """ Линейный размер 3D (от отрезка до точки) """
    ksObjectLineDimension3D                                 = 11032
    """ Линейный размер 3D (на плоскости) """
    ksObjectRadialDimension3D                               = 11033
    """ Радиальный размер 3D """
    ksObjectDiametralDimension3D                            = 11034
    """ Диаметральный размер 3D """
    ksObjectRadialDimensions3D                              = 11035
    """ Коллекция радиальных размеров 3D """
    ksObjectDiametralDimensions3D                           = 11036
    """ Коллекция диаметральных размеров 3D """
    ksObjectAngleDimension3D                                = 11037
    """ Угловой размер 3D """
    ksObjectAngleDimensions3D                               = 11038
    """ Коллекция угловых размеров 3D """
    ksObjectLocalCoordinateSystems                          = 11039
    """ Коллекция локальных систем координат """
    ksObjectLocalCoordinateSystem                           = 11040
    """ Локальная система координат """
    ksObjectLocalCSAxesDirectionParam                       = 11041
    """ Параметры для типа ориентации ЛСК-направление осей """
    ksObjectLocalCSRotateParam                              = 11042
    """ Параметры для типа ориентации ЛСК-вращение вокруг осей СК """
    ksObjectLocalCSEulerParam                               = 11043
    """ Параметры для типа ориентации ЛСК-система углов Эйлера """
    ksObjectSpline3D                                        = 11044
    """ Сплайн """
    ksObjectSplines3D                                       = 11045
    """ Коллекция сплайнов """
    ksObjectCurveVertexParam                                = 11046
    """ Параметры вершины кривой """
    ksObjectPolyLines                                       = 11047
    """ Коллекция 3D ломаных """
    ksObjectPolyLine                                        = 11048
    """ 3D ломаная """
    ksObjectLeaders3D                                       = 11049
    """ Коллекция линий-выносок 3D """
    ksObjectLeader3D                                        = 11050
    """ Линия-выноска 3D """
    ksObjectMarkLeader3D                                    = 11051
    """ Знак маркировки 3D """
    ksObjectRough3D                                         = 11052
    """ Обозначение 3D шероховатости """
    ksObjectRoughs3D                                        = 11053
    """ Коллекция обозначений 3D шероховатости """
    ksObjectPositionLeader3D                                = 11054
    """ Линия-выноска для обозначения позиции 3D """
    ksObjectBrandLeader3D                                   = 11055
    """ Знак клеймения 3D """
    ksObjectBase3D                                          = 11056
    """ Обозначение 3D базы """
    ksObjectBases3D                                         = 11057
    """ Коллекция обозначений 3D базы """
    ksObjectTolerances3D                                    = 11058
    """ Коллекция допуска формы 3D """
    ksObjectTolerance3D                                     = 11059
    """ Обозначение допуска формы 3D """
    ksObjectControlPoints                                   = 11060
    """ Коллекция контрольных точек """
    ksObjectControlPoint                                    = 11061
    """ Контрольная точка """
    ksObjectConjunctivePoints                               = 11062
    """ Коллекция присоединительных точек """
    ksObjectConjunctivePoint                                = 11063
    """ Присоединительная точка """
    ksObjectSplitLines                                      = 11064
    """ Коллекция линий разъема """
    ksObjectSplitLine                                       = 11065
    """ Линия разъема """
    ksObjectSurfacePatches                                  = 11066
    """ Коллекция заплаток """
    ksObjectSurfacePatch                                    = 11067
    """ Заплатка """
    ksObjectFaceRemovers                                    = 11068
    """ Коллекция операций удаления граней """
    ksObjectFaceRemover                                     = 11069
    """ Операция удаления граней """
    ksObjectSurfaceSewers                                   = 11070
    """ Коллекция операций сшивки поверхностей """
    ksObjectSurfaceSewer                                    = 11071
    """ Операция сшивки поверхностей """
    ksObjectNurbsSurfaces                                   = 11072
    """ Коллекция NURBS-поверхностей """
    ksObjectNurbsSurface                                    = 11073
    """ NURBS-поверхность """
    ksObjectSurfacesIntersectionCurves                      = 11074
    """ Коллекция кривых пересечений поверхностей """
    ksObjectSurfacesIntersectionCurve                       = 11075
    """ Кривая пересечения поверхностей """
    ksObjectEquidistants3D                                  = 11076
    """ Коллекция эквидистант 3D """
    ksObjectEquidistant3D                                   = 11077
    """ Эквидистанта 3D """
    ksObjectTrimmedCurves                                   = 11078
    """ Коллекция операций усечения кривой """
    ksObjectTrimmedCurve                                    = 11079
    """ Операция усечения кривой """
    ksObjectFeaturePatterns                                 = 11080
    """ Коллекция операций копирования """
    ksObjectLinearPattern                                   = 11081
    """ Массив операций по сетке """
    ksObjectCircularPattern                                 = 11082
    """ Массив операций по концентрической сетке """
    ksObjectPathPattern                                     = 11083
    """ Массив операций вдоль кривой """
    ksObjectPartsLinearPattern                              = 11084
    """ Массив компонентов по сетке для сборки """
    ksObjectPartsCircularPattern                            = 11085
    """ Массив компонентов по концентрической сетке для сборки """
    ksObjectPartsPathPattern                                = 11086
    """ Массив компонентов вдоль кривой для сборки """
    ksObjectAuxLinearPattern                                = 11087
    """ Массив вспомогательной геометрии по сетке """
    ksObjectAuxCircularPattern                              = 11088
    """ Массив вспомогательной геометрии по концентрической сетке """
    ksObjectAuxPathPattern                                  = 11089
    """ Массив вспомогательной геометрии вдоль кривой """
    ksObjectPointDrivenPattern                              = 11090
    """ Массив операций по точкам """
    ksObjectPartsPointDrivenPattern                         = 11091
    """ Массив компонентов по точкам """
    ksObjectDerivedPattern                                  = 11092
    """ Массив по образцу """
    ksObjectMirrorPattern                                   = 11093
    """ Зеркальный массив """
    ksObjectShellMirrorPattern                              = 11094
    """ Зеркально отобразить тело или операцию """
    ksObjectAuxMirrorPattern                                = 11095
    """ Зеркальный массив вспомогательной геометрии """
    ksObjectRuledSurfaces                                   = 11096
    """ Коллекция операций создания линейчатой поверхности """
    ksObjectRuledSurface                                    = 11097
    """ Линейчатая поверхность """
    ksObjectExtensionSurfaces                               = 11098
    """ Коллекция операций продления поверхности """
    ksObjectExtensionSurface                                = 11099
    """ Операция продления поверхности """
    ksObjectEquidistantSurfaces                             = 11100
    """ Коллекция операций построения эквидистант поверхности """
    ksObjectEquidistantSurface                              = 11101
    """ Операция построения эквидистанты поверхности """
    ksObjectTrimmedSurfaces                                 = 11102
    """ Коллекция Операций усечения поверхности """
    ksObjectTrimmedSurface                                  = 11103
    """ Операция усечения поверхности """
    ksObjectVector3D                                        = 11104
    """ Вектор 3D """
    ksObjectVector3DBy2VertexesParameters                   = 11105
    """ Параметры вектора 3D по двум вершинам """
    ksObjectVector3DByCoefficientsParameters                = 11106
    """ Параметры вектора 3D по коэффициентам """
    ksObjectVector3DBy2AnglesParameters                     = 11107
    """ Параметры вектора 3D по двум углам """
    ksObjectVector3DByObjectParameters                      = 11108
    """ Параметры вектора 3D по ребру или плоскости """
    ksObjectVector3DAlongSurfaceNormalParameters            = 11109
    """ Параметры вектора 3D, перпендикулярного грани в указанной точке """
    ksObjectVector3DByCurveParameters                       = 11110
    """ Параметры вектора 3D по базисному вектору в точке кривой """
    ksObjectVector3DByScreenNormalParameters                = 11111
    """ Параметры вектора 3D перпендикулярно плоскости экрана """
    ksObjectVector3DByLocalCSParameters                     = 11112
    """ Параметры вектора 3D по углу в плоскости СК и по оси СК """
    ksObjectConnectCurves                                   = 11113
    """ Коллекция операций соединения кривых """
    ksObjectConnectCurve                                    = 11114
    """ Операция соединения кривых """
    ksObjectFilletCurves                                    = 11115
    """ Коллекция операций скругления кривых """
    ksObjectFilletCurve                                     = 11116
    """ Операция соединения кривых """
    ksObjectSurfaceThickenings                              = 11117
    """ Коллекция операций придания толщины поверхности """
    ksObjectSurfaceThickening                               = 11118
    """ Операция придания толщины поверхности """
    ksObjectArcs3D                                          = 11119
    """ Коллекция дуг 3D """
    ksObjectArc3D                                           = 11120
    """ 3D дуга """
    ksObjectAuxPointDrivenPattern                           = 11121
    """ Массив вспомогательной геометрии по точкам """
    ksObjectBodiesPointDrivenPattern                        = 11122
    """ Массив тел по точкам """
    ksObjectTablePattern                                    = 11123
    """ Массив операций по таблице из файла """
    ksObjectPartsTablePattern                               = 11124
    """ Массив компонентов по таблице из файла """
    ksObjectAuxTablePattern                                 = 11125
    """ Массив компонентов по таблице из файла """
    ksObjectBodiesTablePattern                              = 11126
    """ Массив вспомогательной геометрии по таблице из файла """
    ksObjectRotateds                                        = 11127
    """ Коллекция операций вращения """
    ksObjectRotated                                         = 11128
    """ Операция вращения """
    ksObjectCutRotated                                      = 11129
    """ Операция 'вырезать вращением' """
    ksObjectExtrusionSurfaces                               = 11130
    """ Коллекция поверхностей выдавливания """
    ksObjectExtrusionSurface                                = 11131
    """ Операция поверхность выдавливания """
    ksObjectRotatedSurfaces                                 = 11132
    """ Коллекция поверхностей вращения """
    ksObjectRotatedSurface                                  = 11133
    """ Операция поверхность вращения """
    ksObjectPoint3DParamBySphere                            = 11134
    """ Точка, заданная сферическими координатами """
    ksObjectPoint3DParamByCylinder                          = 11135
    """ Точка, заданная цилиндрическими координатами """
    ksObjectMeshPointsSurfaces                              = 11136
    """ Коллекция поверхностей по сети точек """
    ksObjectMeshPointsSurface                               = 11137
    """ Поверхность по сети точек """
    ksObjectCloudPointsSurfaces                             = 11138
    """ Коллекция поверхностей по пласту (облаку) точек """
    ksObjectCloudPointsSurface                              = 11139
    """ Поверхность по пласту (облаку) точек """
    ksObjectImportedSurfaces                                = 11140
    """ Коллекция импортированных поверхностей """
    ksObjectImportedSurface                                 = 11141
    """ Импортированная поверхность """
    ksObjectBodiesLinearPattern                             = 11142
    """ Массив тел по сетке """
    ksObjectBodiesCircularPattern                           = 11143
    """ Массив тел по концентрической сетке """
    ksObjectBodiesPathPattern                               = 11144
    """ Массив тел вдоль кривой """
    ksObjectScalings3D                                      = 11145
    """ Коллекция операций масштабирования тел и поверхностей """
    ksObjectScaling3D                                       = 11146
    """ Масштабирование тел и поверхностей """
    ksObjectCurveOutLine                                    = 11147
    """ Линия очерка """
    ksObjectCurveOutLines                                   = 11148
    """ Коллекция линий очерка """
    ksObjectCurveByLaw                                      = 11149
    """ Кривая по закону """
    ksObjectCurveByLaws                                     = 11150
    """ Коллекция кривых по закону """
    ksObjectIsoparametricCurve                              = 11151
    """ Изопараметрическая кривая """
    ksObjectIsoparametricCurves                             = 11152
    """ Коллекция изопараметрических кривых """
    ksObjectIsoparametricCurvesSet                          = 11153
    """ Группа изопараметрических кривых """
    ksObjectIsoparametricCurvesSets                         = 11154
    """ Коллекция групп изопараметрических кривых """
    ksObjectSplineOnSurface                                 = 11155
    """ Сплайн по поверхности """
    ksObjectSplinesOnSurfaces                               = 11156
    """ Коллекция сплайнов по поверхностям """
    ksObjectProjectionCurve                                 = 11157
    """ Проекционная кривая """
    ksObjectProjectionCurves                                = 11158
    """ Коллекция проекционных кривых """
    ksObjectCurveBy2Projections                             = 11159
    """ Проекционная кривая """
    ksObjectCurvesBy2Projectionses                          = 11160
    """ Коллекция проекционных кривых """
    ksObjectContour3D                                       = 11161
    """ Контур 3D """
    ksObjectContours3D                                      = 11162
    """ Коллекция контуров 3D """
    ksObjectLineSegment3D                                   = 11163
    """ Отрезок 3D """
    ksObjectLineSegments3D                                  = 11164
    """ Коллекция отрезков 3D """
    ksObjectConicSpiral3D                                   = 11179
    """ Коническая спираль """
    ksObjectCylindricSpiral3D                               = 11180
    """ Цилиндрическая спираль """
    ksObjectSpirals3D                                       = 11181
    """ Коллекция спиралей """
    ksObjectPointsArrOnCurve                                = 11182
    """ Группа точек по кривой """
    ksObjectPointsArrsOnCurves                              = 11183
    """ Коллекция групп точек по кривым """
    ksObjectPointsArrOnSurfaces                             = 11184
    """ Группа точек по поверхности """
    ksObjectPointsArrsOnSurfaces                            = 11185
    """ Коллекция групп точек по поверхностям """
    ksObjectPointsArrFromFile                               = 11186
    """ Группа точек из файла """
    ksObjectPointsArrsFromFiles                             = 11187
    """ Коллекция групп точек из файлов """
    ksObjectAxis3D                                          = 11188
    """ Вспомогательная ось 3D """
    ksObjectAxes3D                                          = 11189
    """ Коллекция вспомогательных осей 3D """
    ksObjectAxis3DBy2Points                                 = 11190
    """ Ось через две вершины """
    ksObjectAxis3DBy2Planes                                 = 11191
    """ Ось на пересечении плоскостей """
    ksObjectAxis3DByConeface                                = 11192
    """ Ось конической поверхности """
    ksObjectAxis3DByEdge                                    = 11193
    """ Ось через ребро """
    ksObjectAxis3DByPointAndObject                          = 11194
    """ Ось через вершину по объекту """
    ksObjectAxis3DByOperation                               = 11195
    """ Ось операции """
    ksObjectPlanes3D                                        = 11196
    """ Коллекция плоскостей 3D """
    ksObjectPlane3D                                         = 11197
    """ Плоскость 3D """
    ksObjectPlane3DByPlaneCurve                             = 11198
    """ Плоскость через плоскую кривую """
    ksObjectPlane3DTangentToFaceInPoint                     = 11199
    """ Плоскость касательная к грани в точке 3D """
    ksObjectPlane3DByOffset                                 = 11200
    """ Смещенная плоскость """
    ksObjectPlane3DBy3Points                                = 11201
    """ Плоскость, проходящая через три вершины """
    ksObjectPlane3DByAngle                                  = 11202
    """ Плоскость, под углом к другой плоскости """
    ksObjectPlane3DByEdgeAndPoint                           = 11203
    """ Плоскость через ребро и вершину """
    ksObjectPlane3DParallelByPoint                          = 11204
    """ Плоскость через вершину параллельно другой плоскости """
    ksObjectPlane3DPerpendicularByEdge                      = 11205
    """ Плоскость, проходящая через вершину перпендикулярно ребру """
    ksObjectPlane3DNormalToSurface                          = 11206
    """ Нормальная плоскость """
    ksObjectPlane3DMiddle                                   = 11207
    """ Средняя плоскость 3D """
    ksObjectPlane3DByEdgeAndPlane                           = 11208
    """ Плоскость через ребро параллельно / перпендикулярно грани 3D """
    ksObjectPlane3DBy2Edge                                  = 11209
    """ Плоскость через ребро параллельно /перпендикулярно другому ребру 3D """
    ksObjectPlane3DTangentToFace                            = 11210
    """ Плоскость касательная к грани 3D """
    ksObjectUserObject3D                                    = 11211
    """ Пользовательский объект 3D """
    ksObjectUserObjects3D                                   = 11212
    """ Коллекция пользовательских объектов 3D """
    ksObjectLinearPatternAnyCopy                            = 11213
    """ Копирование произвольных объектов по сетке """
    ksObjectCircularPatternAnyCopy                          = 11214
    """ Копирование произвольных объектов по окружности """
    ksObjectPathPatternAnyCopy                              = 11215
    """ Копирование произвольных объектов по кривой """
    ksObjectPointDrivenPatternAnyCopy                       = 11217
    """ Копирование произвольных объектов по точкам """
    ksObjectTablePatternAnyCopy                             = 11218
    """ Копирование произвольных объектов по таблице """
    ksObjectLinearUnhistoriedDimension                      = 11219
    """ Импортированный линейный размер """
    ksObjectAngularUnhistoriedDimension                     = 11220
    """ Импортированный угловой размер """
    ksObjectRadialUnhistoriedDimension                      = 11221
    """ Импортированный радиальный размер """
    ksObjectDiametralUnhistoriedDimension                   = 11222
    """ Импортированный диаметральный размер """
    ksObjectPlacement3D                                     = 11223
    """ Интерфейс локальной системы координат (положение объекта) """
    ksObjectLayers3D                                        = 11224
    """ Коллекция слоев в 3D """
    ksObjectLayer3D                                         = 11225
    """ Слой в 3D """
    ksObjectLayerGroups3D                                   = 11226
    """ Коллекция групп слоев в 3D """
    ksObjectLayerGroup3D                                    = 11227
    """ Группа слоев в 3D """
    ksObjectDocument3DManager                               = 11228
    """ Менеджер 3D документа """
    ksObjectToleranceRecalc                                 = 11229
    """ Пересчет модели """
    ksObjectSpecRough3D                                     = 11230
    """ Неуказанная шероховатость 3D """
    ksObjectSketchBreakLinearDimension                      = 11231
    """ Управляющий линейный размер эскиза 3D с обрывом """
    ksObjectMathCurve3D                                     = 11232
    """ Математическая кривая в трехмерном пространстве """
    ksObjectMathSurface3D                                   = 11233
    """ Математическая поверхность в трехмерном пространстве """
    ksObjectBilletObsolete                                  = 11234
    """ Деталь заготовка и Зеркальная деталь """
    ksObjectBilletsObsoletes                                = 11235
    """ Коллекция деталей заготовок и зеркальных деталей """
    ksObjectCopyGeometry                                    = 11236
    """ Копия геометрии """
    ksObjectCopiesGeometry                                  = 11237
    """ Коллекция копий геометрии """
    ksObjectCollectionGeometry                              = 11238
    """ Коллекция геометрии """
    ksObjectCollectionsGeometry                             = 11239
    """ Коллекции геометрии """
    ksObjectUserWireFrame3D                                 = 11240
    """ Пользовательский объект Каркас 3D """
    ksObjectThreads                                         = 11241
    """ Коллекция условных обозначений резьбы """
    ksObjectThread                                          = 11242
    """ Условное обозначение резьбы """
    ks3dMateConstraints                                     = 11243
    """ Коллекция 3D сопряжений """
    ksMate3DByAngle                                         = 11244
    """ Сопряжение под углом """
    ksMate3DByTangent                                       = 11245
    """ Сопряжение по касательной """
    ksMate3DSymmetry                                        = 11246
    """ Сопряжение симметрия """
    ksMate3DTransmission                                    = 11247
    """ Сопряжение механическое перемещение """
    ksMate3DCamGear                                         = 11248
    """ Сопряжение кулачок-толкатель """
    ksMate3DDependentPosition                               = 11249
    """ Сопряжение зависимое положение """
    ksObjectHoles3D                                         = 11250
    """ Коллекции отверстий 3D """
    ksObjectHole3D                                          = 11251
    """ Отверстие 3D """
    ksObjectCountersinkHoleParameters                       = 11252
    """ Параметры отверстия с зенковкой """
    ksObjectSpotfacingHoleParameters                        = 11253
    """ Параметры отверстия с цековкой """
    ksObjectCountersinkSpotfacingHoleParameters             = 11254
    """ Параметры отверстия с зенковкой и цековкой """
    ksObjectConicHoleParameters                             = 11255
    """ Параметры конического отверстия """
    ksObjectChamfers                                        = 11256
    """ Коллекции фасок """
    ksObjectChamfer                                         = 11257
    """ Фаска """
    ksObjectFillets                                         = 11258
    """ Коллекции скруглений """
    ksObjectFillet                                          = 11259
    """ Скругление """
    ksObjectInclines                                        = 11260
    """ Коллекции операций уклон """
    ksObjectIncline                                         = 11261
    """ Операция Уклон """
    ksObjectRibs                                            = 11262
    """ Коллекции операций Ребро жесткости """
    ksObjectRib                                             = 11263
    """ Ребро жесткости """
    ksObjectShells                                          = 11264
    """ Коллекции операций Оболочка """
    ksObjectShell                                           = 11265
    """ Оболочка """
    ksObjectBooleans                                        = 11266
    """ Коллекция булевых операций """
    ksObjectBoolean                                         = 11267
    """ Булева операция """
    ksObjectCuts                                            = 11268
    """ Коллекция операций 'сечение' """
    ksObjectCut                                             = 11269
    """ Операция 'сечение' """
    ksObjectLofts                                           = 11270
    """ Коллекция операций по сечениям """
    ksObjectLoft                                            = 11271
    """ Операция по сечениям """
    ksObjectLoftSurfaces                                    = 11272
    """ Коллекция поверхностей по сечениям """
    ksObjectLoftSurface                                     = 11273
    """ Операция поверхность по сечениям """
    ksObjectCoupling                                        = 11274
    """ Цепочка в операции по сечениям """
    ksObjectEvolutions                                      = 11275
    """ Коллекция кинематических операций """
    ksObjectEvolution                                       = 11276
    """ Кинематическая операция """
    ksObjectEvolutionSurfaces                               = 11277
    """ Коллекция кинематических поверхностей """
    ksObjectEvolutionSurface                                = 11278
    """ Кинематическая поверхность """
    ksObjectVertex                                          = 11279
    """ Вершина """
    ksObjectEdge                                            = 11280
    """ Ребро """
    ksObjectFace                                            = 11281
    """ Грань """
    ksObjectLoop7                                           = 11282
    """ Цикл """
    ksObjectOrientedEdge7                                   = 11283
    """ Ориентированное ребро """
    ksObjectUnionsComponents                                = 11284
    """ Коллекция операций объединение компонентов """
    ksObjectUnionComponents                                 = 11285
    """ Операция объединения компонентов """
    ksObjectMoldCavities                                    = 11286
    """ Коллекция операций вычитания компонентов """
    ksObjectMoldCavity                                      = 11287
    """ Операция вычитания компонентов """
    ksObjectMacroObjects3D                                  = 11288
    """ Коллекция макроэлементов 3D """
    ksObjectMacroObject3D                                   = 11289
    """ 3D макроэлемент """
    ksObjectNurbsSurfacesByCurvesMeshs                      = 11290
    """ Коллекция поверхностей по сети кривых """
    ksObjectNurbsSurfaceByCurvesMesh                        = 11291
    """ Поверхность по сети кривых """
    ksObjectJointSurfaces                                   = 11292
    """ Коллекция поверхностей соединения """
    ksObjectJointSurface                                    = 11293
    """ Поверхность соединения """
    ksObjectBodyRepositions                                 = 11294
    """ Коллекция операций перепозиционирования тела, поверхности """
    ksObjectBodyReposition                                  = 11295
    """ Перепозиционирование тела, поверхности """
    ksObjectDistanceAngleMeasurements3D                     = 11296
    """ Коллекция измерений расстояния и угла """
    ksObjectDistanceAngleMeasurement3D                      = 11297
    """ Измерение расстояния и угла """
    ksObjectEdgeLengthMeasurements3D                        = 11298
    """ Коллекция измерений длины ребра """
    ksObjectEdgeLengthMeasurement3D                         = 11299
    """ Измерение длины ребра """
    ksObjectAreaMeasurements3D                              = 11300
    """ Коллекция измерений площади """
    ksObjectAreaMeasurement3D                               = 11301
    """ Измерение площади """
    ksObjectSheetMetalSketchBends                           = 11302
    """ Коллекция операций сгиб по эскизу """
    ksObjectSheetMetalSketchBend                            = 11303
    """ Сгиб по эскизу """
    ksObjectSheetMetalClosedCorners                         = 11304
    """ Коллекция операций Замыкание углов """
    ksObjectSheetMetalClosedCorner                          = 11305
    """ Замыкание углов """
    ksObjectSheetMetalPlates                                = 11306
    """ Коллекция операций Пластина """
    ksObjectSheetMetalPlate                                 = 11307
    """ Пластина """
    ksObjectSheetMetalUndercuts                             = 11308
    """ Коллекция операций Подсечка """
    ksObjectSheetMetalUndercut                              = 11309
    """ Подсечка """
    ksObjectSheetMetalBendedStraightens                     = 11310
    """ Коллекция операций Согнуть/Разогнуть """
    ksObjectSheetMetalBendedStraighten                      = 11311
    """ Согнуть/Разогнуть """
    ksObjectSheetMetalPressFormings                         = 11312
    """ Коллекция операций открытая или закрытая штамповка """
    ksObjectSheetMetalPressForming                          = 11313
    """ Открытая или закрытая штамповка """
    ksObjectSheetMetalShoulders                             = 11314
    """ Коллекция операций буртик """
    ksObjectSheetMetalShoulder                              = 11315
    """ Буртик """
    ksObjectSheetMetalJalousies                             = 11316
    """ Коллекция операций жалюзи """
    ksObjectSheetMetalJalousie                              = 11317
    """ Жалюзи """
    ksObjectSheetMetalRibs                                  = 11318
    """ Коллекция операций ребро усиления """
    ksObjectSheetMetalRib                                   = 11319
    """ Ребро усиления """
    ksObjectSheetMetalRuledShells                           = 11320
    """ Коллекция операций Обечайка """
    ksObjectSheetMetalRuledShell                            = 11321
    """ Обечайка """
    ksObjectSheetMetalLinearRuledShells                     = 11322
    """ Коллекция операций Линейчатая обечайка """
    ksObjectSheetMetalLinearRuledShell                      = 11323
    """ Линейчатая обечайка """
    ksObjectLibraryHoleParameters                           = 11324
    """ Параметры отверстия из библиотеки """
    ksObjectFullFillets                                     = 11325
    """ Коллекция операций полного скругления """
    ksObjectFullFillet                                      = 11326
    """ Полное скругление """
    ksObjectZone                                            = 11327
    """ Зона """
    ksObjectZonesManager                                    = 11328
    """ Менеджер зон """
    ksObjectZoneParametersByObjects                         = 11329
    """ Параметры зоны по суммарному габариту объектов """
    ksObjectZoneParametersByBorderPoints                    = 11330
    """ Параметры зоны, заданной габаритным параллелепипедом """
    ksObjectZoneDivision                                    = 11331
    """ Разбить зону """
    ksObjectZoneDivisionParametersByPlanes                  = 11332
    """ Параметры разбиения зоны для способа По набору плоскостей """
    ksObjectZoneDivisionParametersRegular                   = 11333
    """ Параметры разбиения зоны для способа Равномерно по осям """
    ksObjectDynamicCrossSection                             = 11334
    """ Динамическое сечение """
    ksObjectDynamicCrossSectionStep                         = 11335
    """ Шаг динамического сечения """
    ksObjectDynamicCrossSectionStepParametersByFreePlane    = 11336
    """ Параметры шага динамического сечения по произвольной плоскости """
    ksObjectDynamicCrossSectionStepParametersByOffsetPlane  = 11337
    """ Параметры шага динамического сечения по смещенной плоскости """
    ksObjectDynamicCrossSectionStepParametersByRotatedPlane = 11338
    """ Параметры шага динамического сечения по плоскости под углом """
    ksObjectDynamicCrossSectionStepParametersByZone         = 11339
    """ Параметры шага динамического сечения по зоне """
    ksObjectDynamicCrossSectionStepParametersByBorderPoints = 11340
    """ Параметры шага динамического сечения по габаритному параллелепипеду заданному точками """
    ksObjectAxisLine3D                                      = 11341
    """ Осевая линия """
    ksObjectRestoredSurfaces                                = 11342
    """ Коллекция операций восстановленная поверхность """
    ksObjectRestoredSurface                                 = 11343
    """ Восстановленная поверхность """
    ksObjectWireFrames3D                                    = 11344
    """ Коллекция трехмерных каркасов """
    ksObjectWireFrame3D                                     = 11345
    """ Трехмерный каркас """
    ksObjectDismantleStep                                   = 11346
    """ Шаг разнесения сборки """
    ksObjectArcDimension3D                                  = 11347
    """ Размер дуги окружности 3D """
    ksObjectArcDimensions3D                                 = 11348
    """ Коллекция размеров дуги окружностей 3D """
    ksObjectSheetMetalPunch                                 = 11349
    """ Листовой металл, штамповка телом """
    ksObjectSheetMetalPunchs                                = 11350
    """ Коллекция операций Листовой металл, штамповка телом """
    ksObjectSheetMetalFlanging                              = 11351
    """ Листовой металл, отбортовка """
    ksObjectSheetMetalFlangings                             = 11352
    """ Коллекция операций Листовой металл, отбортовка """
    ksObjectFaceMovers                                      = 11353
    """ Коллекция операций перемещения граней """
    ksObjectFaceMover                                       = 11354
    """ Операция перемещения граней """
    ksObjectSplitSolid                                      = 11355
    """ Операция “Разрезать” """
    ksObjectSplitSolids                                     = 11356
    """ Коллекция операций “Разрезать” """
    ksObjectModelText                                       = 11357
    """ Текст в модели """
    ksObjectModelTexts                                      = 11358
    """ Коллекция текстов в модели """
    ksObjectModelTable                                      = 11359
    """ Таблица в модели """
    ksObjectModelTables                                     = 11360
    """ Коллекция таблиц в модели """
    ksObjectConicCurve3D                                    = 11361
    """ Коническая 3D кривая """
    ksObjectConicCurves3D                                   = 11362
    """ Коллекция конических кривых 3D """
    ksObjectComponentPositioner                             = 11363
    """ Интерфейс управления положением компонентов в сборке """
    ksObjectConicSurface                                    = 11364
    """ Поверхность конического сечения """
    ksObjectConicSurfaces                                   = 11365
    """ Коллекция поверхностей конического сечения """
    ksObjectConvertToSheetMetal                             = 11366
    """ Операции преобразования в листовое тело """
    ksObjectConvertsToSheetMetals                           = 11367
    """ Коллекция операций преобразования в листовое тело """
    ksObjectExtensionCurves                                 = 11368
    """ Коллекция продлений кривых """
    ksObjectExtensionCurve                                  = 11369
    """ Продления кривой """
    ksObjectRuledSurfaceParametersByFaces                   = 11370
    """ Параметры линейчатой поверхности "По двум поверхностям" """
    ksObjectRuledSurfaceTangentParametersByCurveAndFace     = 11371
    """ Параметры линейчатой поверхности "По кривой с касанием к поверхности" """
    ksObjectRuledSurfaceParametersByCurveAndFace            = 11372
    """ Параметры линейчатой поверхности "'По кривой и поверхности" """
    ksObjectRuledSurfaceParametersByCurveAndDir             = 11373
    """ Параметры линейчатой поверхности "По кривой и направлению" """
    ksObjectViewProjection                                  = 11374
    """ Интерфейс проекции отображения модели в окне """
    ksObjectViewProjectionManager                           = 11375
    """ Менеджер проекций отображения модели в окне """
    ksObjectPlane3DUnhistoried                              = 11376
    """ Плоскость без истории """
    ksObjectDraftFromEdges                                  = 11377
    """ Уклон от базовой линии """
    ksObjectDraftsFromEdges                                 = 11378
    """ Коллекции операций Уклон от базовой линии """
    ksObjectPoint3DParamBetweenPoints                       = 11379
    """ Интерфейс параметров пространственной точки между точками """
    ksObjectDrawingObject                                   = 13000
    """ Графический объект """
    ksObjectDrawingText                                     = 13001
    """ Текст на чертеже """
    ksObjectDrawingTexts                                    = 13002
    """ Коллекция текстов на чертеже """
    ksObjectStraightAxis                                    = 13003
    """ Прямая ось """
    ksObjectCircleAxis                                      = 13004
    """ Круговая ось """
    ksObjectArcAxis                                         = 13005
    """ Дуговая ось """
    ksObjectBuildingAxes                                    = 13006
    """ Коллекция строительных осей """
    ksObjectAxisJut                                         = 13007
    """ Выступ оси """
    ksObjectMarkNodes                                       = 13008
    """ Kоллекция узлов для вставки марки """
    ksObjectMarkNode                                        = 13009
    """ Узел для вставки дополнительных марок """
    ksObjectMarkOnLeader                                    = 13010
    """ Марка/позиционное обозначение с линией-выноской """
    ksObjectMarkOnLine                                      = 13011
    """ Марка/позиционное обозначение на линии """
    ksObjectMarkInsideForm                                  = 13012
    """ Марка/позиционное обозначение без линии-выноски """
    ksObjectMarks                                           = 13013
    """ Коллекция марок """
    ksObjectCutUnitMarking                                  = 13014
    """ Обозначение узла в сечении """
    ksObjectCutUnitMarkings                                 = 13015
    """ Коллекция обозначений узла в сечении """
    ksObjectUnitMarking                                     = 13016
    """ Обозначение узла """
    ksObjectUnitMarkings                                    = 13017
    """ Коллекция обозначений узлов """
    ksObjectUnitNumber                                      = 13018
    """ Номер узла """
    ksObjectUnitNumbers                                     = 13019
    """ Коллекция номеров узлов """
    ksObjectMultiTextLeader                                 = 13020
    """ Выносная надпись к многослойным конструкциям """
    ksObjectMultiTextLeaders                                = 13021
    """ Коллекция выносных надписей к многослойным конструкциям """
    ksObjectBrace                                           = 13022
    """ Фигурная скобка """
    ksObjectBraces                                          = 13023
    """ Коллекция фигурных скобок """
    ksObjectLineSegments                                    = 13024
    """ Коллекция отрезков """
    ksObjectLineSegment                                     = 13025
    """ Отрезок """
    ksObjectRadialDimension                                 = 13028
    """ Радиальный размер """
    ksObjectDiametralDimension                              = 13029
    """ Диаметральный размер """
    ksObjectBreakRadialDimension                            = 13030
    """ Радиальный размер с изломом """
    ksObjectRadialDimensions                                = 13031
    """ Коллекция радиальных размеров """
    ksObjectBreakRadialDimensions                           = 13032
    """ Коллекция радиальных размеров с изломом """
    ksObjectDiametralDimensions                             = 13033
    """ Коллекция диаметральных размеров """
    ksObjectLineDimension                                   = 13041
    """ Линейный размер """
    ksObjectLineDimensions                                  = 13042
    """ Коллекция линейных размеров """
    ksObjectBreakLineDimension                              = 13043
    """ Линейный размер с обрывом """
    ksObjectBreakLineDimensions                             = 13044
    """ Коллекция линейных размеров с обрывом """
    ksObjectHeightDimension                                 = 13045
    """ Размер высоты """
    ksObjectHeightDimensions                                = 13046
    """ Коллекция размеров высоты """
    ksObjectAngleDimension                                  = 13047
    """ Угловой размер """
    ksObjectBreakAngleDimension                             = 13048
    """ Угловой размер c обрывом """
    ksObjectAngleDimensions                                 = 13049
    """ Коллекция угловых размеров """
    ksObjectArcDimension                                    = 13050
    """ Размер дуги окружности """
    ksObjectArcDimensions                                   = 13051
    """ Коллекция размеров дуг окружностей """
    ksObjectLeader                                          = 13052
    """ Простая линия выноски """
    ksObjectLeaders                                         = 13053
    """ Коллекция линий выносок """
    ksObjectRough                                           = 13054
    """ Обозначение шероховатости """
    ksObjectRoughs                                          = 13055
    """ Коллекция обозначений шероховатости """
    ksObjectMarkLeader                                      = 13056
    """ Знак маркировки """
    ksObjectBrandLeader                                     = 13057
    """ Знак клеймения """
    ksObjectPositionLeader                                  = 13058
    """ Линия выноски для обозначения позиции """
    ksObjectChangeLeader                                    = 13059
    """ Обозначение изменения """
    ksObjectBase                                            = 13060
    """ Обозначение базы """
    ksObjectBases                                           = 13061
    """ Коллекция обозначений базы """
    ksObjectDrawingTable                                    = 13062
    """ Таблица на чертеже """
    ksObjectDrawingTables                                   = 13063
    """ Коллекция таблиц на чертеже """
    ksObjectTolerance                                       = 13064
    """ Допуск формы """
    ksObjectTolerances                                      = 13065
    """ Коллекция допусков формы """
    ksObjectCutLines                                        = 13066
    """ Коллекция линий разреза/сечения """
    ksObjectCutLine                                         = 13067
    """ Линия разреза/сечения """
    ksObjectViewPointer                                     = 13068
    """ Cтрелка взгляда """
    ksObjectViewPointers                                    = 13069
    """ Коллекция стрелок взгляда """
    ksObjectDrawingContour                                  = 13072
    """ Контур на чертеже """
    ksObjectDrawingContours                                 = 13073
    """ Коллекция контуров на чертеже """
    ksObjectCircles                                         = 13074
    """ Коллекция окружностей """
    ksObjectCircle                                          = 13075
    """ Окружность """
    ksObjectPoints                                          = 13076
    """ Коллекция точек """
    ksObjectPoint                                           = 13077
    """ Точка """
    ksObjectBeziers                                         = 13078
    """ Коллекция Bezier сплайнов """
    ksObjectBezier                                          = 13079
    """ Bezier сплайн """
    ksObjectMacroObjects                                    = 13080
    """ Коллекция макроэлементов """
    ksObjectMacroObject                                     = 13081
    """ Макроэлемент """
    ksObjectLines                                           = 13082
    """ Коллекция линий """
    ksObjectLine                                            = 13083
    """ Линия """
    ksObjectPolyLines2D                                     = 13084
    """ Коллекция полилиний """
    ksObjectPolyLine2D                                      = 13085
    """ Полилиния """
    ksObjectNurbses                                         = 13086
    """ Коллекция Nurbs-сплайнов """
    ksObjectNurbs                                           = 13087
    """ Nurbs-сплайн """
    ksObjectRasters                                         = 13088
    """ Коллекция растровых объектов """
    ksObjectRaster                                          = 13089
    """ Растровый объект """
    ksObjectOleDrawingObjects                               = 13090
    """ Коллекция OLE-объектов """
    ksObjectOleDrawingObject                                = 13091
    """ OLE-объект """
    ksObjectEllipses                                        = 13092
    """ Коллекция эллипсов """
    ksObjectEllipse                                         = 13093
    """ Эллипс """
    ksObjectEllipseArcs                                     = 13094
    """ Коллекция дуг эллипсов """
    ksObjectEllipseArc                                      = 13095
    """ Дуга эллипса """
    ksObjectRectangles                                      = 13096
    """ Коллекция прямоугольников """
    ksObjectRectangle                                       = 13097
    """ Прямоугольник """
    ksObjectRegularPolygons                                 = 13098
    """ Коллекция многоугольников """
    ksObjectRegularPolygon                                  = 13099
    """ Многоугольник """
    ksObjectEquidistants                                    = 13100
    """ Коллекция эквидистант """
    ksObjectEquidistant                                     = 13101
    """ Эквидистанта """
    ksObjectInsertionFragment                               = 13102
    """ Вставка фрагмента """
    ksObjectInsertionView                                   = 13103
    """ Вставка вида из другого чертежа """
    ksObjectInsertionObjects                                = 13104
    """ Коллекция вставок фрагментов и видов """
    ksObjectInsertionDefinition                             = 13105
    """ Описание вставки фрагмента и вида """
    ksObjectCentreMarkers                                   = 13106
    """ Коллекция обозначений центров """
    ksObjectCentreMarker                                    = 13107
    """ Обозначение центра """
    ksObjectRemoteElements                                  = 13108
    """ Коллекция выносных элементов """
    ksObjectRemoteElement                                   = 13109
    """ Выносной элемент """
    ksObjectAxisLines                                       = 13110
    """ Коллекция осевых линий """
    ksObjectAxisLine                                        = 13111
    """ Осевая линия """
    ksObjectHatchParam                                      = 13112
    """ Параметры штриховки """
    ksObjectDrawingGroup                                    = 13113
    """ Группа объектов """
    ksObjectDrawingGroups                                   = 13114
    """ Коллекция групп объектов """
    ksObjectCurve2D                                         = 13115
    """ Математическая 2D кривая """
    ksObjectHatches                                         = 13116
    """ Коллекция штриховок """
    ksObjectHatch                                           = 13117
    """ Штриховка """
    ksObjectColourings                                      = 13118
    """ Коллекция заливок """
    ksObjectColouring                                       = 13119
    """ Заливка """
    ksObjectSpecRough                                       = 13120
    """ Неуказанная шероховатость """
    ksObjectTechnicalDemand                                 = 13121
    """ Технические требования """
    ksObjectAnnotativeLineSegment                           = 13122
    """ Аннотационный отрезок """
    ksObjectAnnotativeCircle                                = 13123
    """ Аннотационная окружность """
    ksObjectAnnotativeEllipse                               = 13124
    """ Аннотационный эллипс """
    ksObjectAnnotativeArc                                   = 13125
    """ Аннотационная дуга """
    ksObjectAnnotativeEllipseArc                            = 13126
    """ Аннотационная дуга эллипса """
    ksObjectAnnotativePolyLine                              = 13127
    """ Аннотационная полилиния """
    ksObjectAnnotativePoint                                 = 13128
    """ Аннотационная точка """
    ksObjectAnnotativeText                                  = 13129
    """ Т екст с аннотационной точкой привязки """
    ksObjectBuildingCutLines                                = 13131
    """ Коллекция линий разреза/сечения для СПДС """
    ksObjectBuildingCutLine                                 = 13132
    """ Линия разреза/сечения для СПДС """
    ksObjectWaveLines                                       = 13133
    """ Коллекция волнистых линий """
    ksObjectWaveLine                                        = 13134
    """ Волнистая линия """
    ksObjectBrokenLines                                     = 13135
    """ Коллекция линий обрыва с изломами """
    ksObjectBrokenLine                                      = 13136
    """ Линия обрыва с изломами """
    ksObjectCopyObjectParam                                 = 13137
    """ Параметры копирования объектов """
    ksObjectCurveCopyObjectParam                            = 13138
    """ Параметры копирования объектов вдоль кривой """
    ksObjectCircleCopyObjectParam                           = 13139
    """ Параметры копирования объектов по окружности """
    ksObjectCircularCopyObjectParam                         = 13140
    """ Параметры копирования объектов по концентрической сетке """
    ksObjectMeshCopyObjectParam                             = 13141
    """ Параметры копирования объектов по сетке """
    ksObjectLocalCoordinateSystem2D                         = 13142
    """ Локальная система координат """
    ksObjectLocalCoordinateSystems2D                        = 13143
    """ Коллекция локальных систем координат """
    ksObjectAttachedLeader                                  = 13144
    """ Присоединенная линия выноски (не имеет текстов) """
    ksObjectAttachedLeaders                                 = 13145
    """ Коллекция присоединенных линий выносок """
    ksObjectLoadCombinationsParam                           = 13146
    """ Параметры типа загрузки документа """
    ksObjectOpenDocumentParam                               = 13147
    """ Параметры открытия документа """
    ksObjectAssociationTables                               = 13148
    """ Коллекция ассоциативных таблиц """
    ksObjectAssociationTable                                = 13149
    """ Ассоциативная таблица """
    ksObjectNurbsesByPoints                                 = 13150
    """ Коллекция NURBS-кривых по точкам """
    ksObjectNurbsByPoints                                   = 13151
    """ NURBS-кривая по точкам """
    ksObjectProcess2D                                       = 13152
    """ Процесс 2D из библиотеки """
    ksObjectPhantom2D                                       = 13153
    """ Параметры фантома 2D """
    ksObjectProcess3D                                       = 13154
    """ Процесс 3D из библиотеки """
    ksObjectUserDesignationCompObj                          = 13155
    """ Составной пользовательский объект обозначение 3D """
    ksObjectUserFolder                                      = 13156
    """ Пользовательская директория """
    ksObjectUserFolders                                     = 13157
    """ Пользовательские директории """
    ksObjectMeshObject3D                                    = 13158
    """ Пространственный полигональный объект """
    ksObjectConicCurves                                     = 13159
    """ Коллекция конический кривых """
    ksObjectConicCurve                                      = 13160
    """ Коническая кривая """
    ksObjectCircularsCentries                               = 13161
    """ Коллекция круговых сеток центров """
    ksObjectCircularCentres                                 = 13162
    """ Круговая сетка центров """
    ksObjectLinearsCentries                                 = 13163
    """ Коллекция линейных сеток центров """
    ksObjectLinearCentres                                   = 13164
    """ Линейная сетка центров """
    ksObjectFindObjectParameters                            = 13165
    """ Параметры поиска объектов """
    ksObjectManipulators                                    = 13166
    """ Коллекция манипуляторов """
    ksObjectPlacement3DManipulator                          = 13167
    """ Манипулятор системы координат """
    ksObjectEditDoubleManipulator                           = 13168
    """ Манипулятор в виде редактора числового значения """
    ksObjectMouseEnterLeaveParameters                       = 13169
    """ Параметры отображения точки, позволяющей определить место применения контрола """
    ksObjectConditionIntersect                              = 13170
    """ Условное пересечение """
    ksObjectConditionIntersects                             = 13171
    """ Коллекция условных пересечений """
    ksObjectSaveAsDetailParam                               = 13172
    """ Параметры преобразования в модель """
    ksObjectFindObject3DParameters                          = 13173
    """ Параметры поиска объектов 3D """
    ksObjectNumericGroup                                    = 13174
    """ Группа автонумерации. """


class ksAccuracyEnum:  # ksaccuracyenum.html
    """ ## ksAccuracyEnum - Количество знаков после запятой """
    ksAccuracyDefault = -1
    """ По умолчанию. Использовать настройки """
    ksAccuracy0       = 0
    """ 0. """
    ksAccuracy1       = 1
    """ 0,1. """
    ksAccuracy2       = 2
    """ 0,12. """
    ksAccuracy3       = 3
    """ 0,123. """
    ksAccuracy4       = 4
    """ 0,1234. """
    ksAccuracy5       = 5
    """ 0,12345. """
    ksAccuracy6       = 6
    """ 0,123456. """
    ksAccuracy7       = 7
    """ 0,1234567. """
    ksAccuracy8       = 8
    """ 0,12345678. """
    ksAccuracy9       = 9
    """ 0,123456789. """


class ksAlignEnum:  # ksalignenum.html
    """ ## ksAlignEnum - Выравнивание """
    ksAlignLeft     = 0
    """ Выравнивание слева """
    ksAlignCenter   = 1
    """ Выравнивание по центру """
    ksAlignRight    = 2
    """ Выравнивание справа """
    ksAlignAllWidth = 3
    """ Выравнивание на всю ширину """
    ksAlignDecimal  = 3
    """ Выравнивание по десятичной точке """
    ksAlignDefault  = -1
    """ По умолчанию (из стиля) """


class ksAlignmentTypeEnum:  # ksalignmenttypeenum.html
    """ ## ksAlignmentTypeEnum – Тип ориентации объекта """
    ksATArbitrary  = 0
    """ Произвольная """
    ksATHorizontal = 1
    """ Горизонтальная """
    ksATVertical   = 2
    """ Вертикальная """


class ksAllocationEnum:  # ksallocationenum.html
    """ ## ksAllocationEnum – Размещение текста относительно точки привязки """
    ksAlLeft   = 0
    """ Слева """
    ksAlCentre = 1
    """ По центру """
    ksAlRight  = 2
    """ Справа """


class ksAngleDimTypeEnum:  # ksangledimtypeenum.html
    """ ## ksAngleDimTypeEnum - Тип углового размера """
    ksADMinAngle  = 0
    """ На минимальный (острый) угол """
    ksADMaxAngle  = 1
    """ На максимальный (тупой) угол """
    ksADMoreAngle = 2
    """ На угол более 180 гр """


class ksAngleEnum:  # ksangleenum.html
    """ ## ksAngleEnum - Углы поворота, кратные 90 градусам """
    ksAngle0   = 0
    """ 0 градусов """
    ksAngle90  = 1
    """ 90 градусов """
    ksAngle180 = 2
    """ 180 градусов """
    ksAngle270 = 3
    """ 270 градусов """


class ksAngleTypeEnum:  # ksangletypeenum.html
    """ ## ksAngleTypeEnum - Признак типа угла """
    ksError   = -2
    """ Ошибка """
    ksConcave = -1
    """ Угол вогнутый """
    ksNeutral = 0
    """ Плоский угол """
    ksConvex  = 1
    """ Угол выпуклый """


class ksAnnotationSymbolEnum:  # ksannotationsymbolenum.html
    """ ## ksAnnotationSymbolEnum - Аннотационные символы """
    ksUnknownSymbol     = 0
    """ Символ не определен """
    ksDotPoint          = 1
    """ Точка """
    ksPlusPoint         = 2
    """ Крестик """
    ksXPoint            = 3
    """ X-точка """
    ksSquarePoint       = 4
    """ Квадрат """
    ksTrianglePoint     = 5
    """ Треугольник """
    ksCirclePoint       = 6
    """ Окружность """
    ksAsteriskPoint     = 7
    """ Звезда """
    ksStrikeSquarePoint = 8
    """ Перечеркнутый квадрат """
    ksPlusPointTwo      = 9
    """ Утолщенный плюс """


class ksAnnotativeTerminatorSignEnum:  # ksannotativeterminatorsignenum.html
    """ ## ksAnnotativeTerminatorSignEnum - Типы специальных символов для аннотационных объектов """
    ksASUnknown            = 0
    """ Не задан """
    ksASArrowInside        = 101
    """ Стрелка (ласточкин хвост) изнутри """
    ksASArrowOutside       = 102
    """ Стрелка (ласточкин хвост) снаружи """
    ksASNotchTail          = 103
    """ Засечка с продолжением кривой (с хвостиком) """
    ksASUpHalfArrow        = 104
    """ Верхняя половина стрелки изнутри """
    ksASDownHalfArrow      = 105
    """ Нижняя половина стрелки изнутри """
    ksASBigArrowInside     = 106
    """ Большая стрелка изнутри (7мм) """
    ksASArrowOrdinate      = 107
    """ Стрелка для размера высоты (штрихи длиной 4мм под углом 45гр) """
    ksASTriangle           = 108
    """ Треугольник по направлению кривой """
    ksAScircleRad2         = 109
    """ Окружность радиусом 2мм тонкой линией - для шероховатости и линии-выноски """
    ksASCentreMarker       = 110
    """ Обозначение фиктивного центра в виде большого креста """
    ksASGlueSign           = 111
    """ Знак склеивания """
    ksASSolderingSign      = 112
    """ Знак пайки """
    ksASSewingSign         = 113
    """ Знак сшивания """
    ksASCrampSign          = 114
    """ Знак соединения внахлестку металлическими скобами """
    ksASCornerCrampSign    = 115
    """ Знак углового соединения металлическими скобами """
    ksASMontageJointSign   = 116
    """ Знак монтажного шва """
    ksASNotch              = 117
    """ Засечка без продолжения кривой (без хвостика) """
    ksASBaseTriangle       = 118
    """ Треугольник по текущей СК - для базы """
    ksASClosedArrowInside  = 119
    """ Закрытая стрелка изнутри """
    ksASClosedArrowOutside = 120
    """ Закрытая стрелка снаружи """
    ksASOpenArrowInside    = 121
    """ Открытая стрелка изнутри """
    ksASOpenArrowOutside   = 122
    """ Открытая стрелка снаружи """
    ksASRightAngleInside   = 123
    """ Стрелка 90гр изнутри """
    ksASRightAngleOutside  = 124
    """ Стрелка 90гр снаружи """
    ksASDot                = 125
    """ Точка (диаметр равен длине стрелки размера) """
    ksASSmallDot           = 126
    """ Точка маленькая (диаметр равен 0,6 длины стрелки размера) """
    ksASPoint              = 127
    """ Вспомогательная точка """
    ksASLeftNotch          = 128
    """ Засечка с наклоном влево """


class ksAPITypeEnum:  # ksapitypeenum.html
    """ ## ksAPITypeEnum - Тип API """
    ksAPIUndef = 0
    """ Интерфейс неопределённого типа """
    ksAPI5Auto = 1
    """ API5 - интерфейсы автоматизации """
    ksAPI7Dual = 2
    """ API7 - дуальные интерфейсы """
    ksAPI3DCom = 3
    """ API 3D COM - интерфейсы """
    ksAPI22    = 4
    """ API22 - интерфейсы """


class ksArc3DBuildingTypeEnum:  # ksarc3dbuildingtypeenum.html
    """ ## ksArc3DBuildingTypeEnum - Способ создания 3D дуги """
    ksArc3DByPoints     = 0
    """ По трем точкам """
    ksArc3DByCentre     = 1
    """ По центру, углам и плоскости """
    ksArc3DByDirrection = 2
    """ По двум точкам и направлению """
    ksArc3DByTanCurve   = 3
    """ Касательно к кривой """


class ksArc3DParameterEnum:  # ksarc3dparameterenum.html
    """ ## ksArc3DParameterEnum - Индекс параметра 3D дуги """
    ksArc3DCenter = 0
    """ Точка центра """
    ksArc3DPoint1 = 1
    """ Точка 1 """
    ksArc3DPoint2 = 2
    """ Точка 2 """
    ksArc3DPoint3 = 3
    """ Точка 3 """
    ksArc3DAngle1 = 1
    """ Угол 1 """
    ksArc3DAngle2 = 2
    """ Угол 2 """
    ksArc3DRadius = 3
    """ Радиус """


class ksArchMeasureEnum:  # ksarchmeasureenum.html
    """ ## ksArchMeasureEnum - Способ задания глубины прогиба """
    ksArchMeasureByCoefficient = 0
    """ Глубина прогиба задана коэффициентом прогиба, в % """
    ksArchMeasureByLength      = 1
    """ Глубина прогиба задана расстоянием """


class ksArrowEnum:  # ksarrowenum.html
    """ ## ksArrowEnum – Тип стрелки линии-выноски """
    ksLeaderWithoutArrow = 0
    """
    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksLeaderPoint        = 1
    """
    Вспомогательная точка

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +

    Обозначения шероховатости: +
    """
    ksLeaderArrow        = 2
    """
    Стрелка

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksWithoutArrow       = 0
    """
    Без стрелки

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +

    Обозначения шероховатости: +
    """
    ksPoint              = 1
    """
    Вспомогательная точка

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksArrow              = 2
    """
    Стрелка

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksUpHalfArrow        = 3
    """
    Верхняя половина стрелки изнутри

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: -

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksDownHalfArrow      = 4
    """
    Нижняя половина стрелки изнутри

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: -

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksNotch              = 5
    """
    Засечка

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: -

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +

    Обозначения шероховатости: +
    """
    ksLeftNotch          = 6
    """
    Засечка с наклоном влево

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: -

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +

    Обозначения шероховатости: +
    """
    ksRightAngle         = 7
    """
    Угол 90 град

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksClosedArrow        = 8
    """
    Стрелка закрытая

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +

    Обозначения шероховатости: +
    """
    ksOpenArrow          = 9
    """
    Стрелка открытая

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +

    Обозначения шероховатости: +
    """
    ksDot                = 10
    """
    Точка

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksSmallDot           = 11
    """
    Точка маленькая

    Размеры: +

    Линии-выноски: +

    Обозначения позиций: +

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksTriangle60         = 12
    """
    Треугольник 60 град

    Размеры: -

    Линии-выноски: +

    Обозначения позиций: -

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """
    ksTriangle90         = 13
    """
    Треугольник 90 град

    Размеры: -

    Линии-выноски: +

    Обозначения позиций: -

    Многослойные линии-выноски: +

    Марки и позиционные обозначения: +
    """


class ksAttributeTypeEnum:  # ksattributetypeenum.html
    """ ## ksAttributeTypeEnum - Тип данных для типа атрибута """
    ksATUnknown       = -1
    """ Неизвестный """
    ksATString        = 0
    """ Строка """
    ksATDouble        = 1
    """ Число """
    ksATFixedTable    = 2
    """ Таблица с фиксированным числом строк """
    ksATVariableTable = 3
    """ Таблица с переменным числом строк """


class ksBasisVectorTypeEnum:  # ksbasisvectortypeenum.html
    """ ## ksBasisVectorTypeEnum - Типы базисного вектора """
    ksTangentVector  = 0
    """ Касательный вектор """
    ksNormalVector   = 1
    """ Вектор главной нормали """
    ksBinormalVector = 2
    """ Вектор бинормали """


class ksBendAngleReleaseTypeEnum:  # ksbendanglereleasetypeenum.html
    """ ## ksBendAngleReleaseTypeEnum - Способ освобождения угла сгиба """
    ksBendAngleBendOnly = 0
    """ Только сгиб """
    ksBendAngleIn       = 1
    """ Сгиб и продолжение """
    ksBendAngleAllBends = 2
    """ Все сгибы """


class ksBendDisposalEnum:  # ksbenddisposalenum.html
    """ ## ksBendDisposalEnum - Тип размещения сгиба на ребре """
    ksBendDisposalAllLength     = 0
    """ По всей длине """
    ksBendDisposalCentre        = 1
    """ По центру """
    ksBendDisposalLeft          = 2
    """ Отступ слева """
    ksBendDisposalRight         = 3
    """ Отступ справа """
    ksBendDisposalTwo           = 4
    """ Два отступа """
    ksBendDisposalLeftAndWidth  = 5
    """ Отступ слева и по ширине """
    ksBendDisposalRightAndWidth = 6
    """ Отступ справа и по ширине """


class ksBendLengthTypeEnum:  # ksbendlengthtypeenum.html
    """ ## ksBendLengthTypeEnum - Тип определения длины """
    ksBendLengthByContinue        = 0
    """ По продолжению """
    ksBendLengthByContour         = 1
    """ По контуру """
    ksBendLengthByTouch           = 2
    """ По касанию """
    ksBendLengthByContourInternal = 3
    """ По контуру внутри """
    ksBendLengthByTangentInternal = 4
    """ По касанию внутри """


class ksBendOffsetTypeEnum:  # ksbendoffsettypeenum.html
    """ ## ksBendOffsetTypeEnum - Тип смещения """
    ksBendOffsetIn          = 0
    """ Смещение внутрь """
    ksBendOffsetOut         = 1
    """ Смещение наружу """
    ksBendOffsetLineOutside = 2
    """ По внешней линии контура """
    ksBendOffsetLineInside  = 3
    """ По внутренней линии контура """
    ksBendOffsetByTouch     = 4
    """ По касанию к сгибу """
    ksBendByCentre          = 5
    """ По центру """


class ksBendReleaseTypeEnum:  # ksbendreleasetypeenum.html
    """ ## ksBendReleaseTypeEnum - Тип освобождения cгиба """
    ksBendReleaseByRect   = 0
    """ Прямоугольное """
    ksBendReleaseByCircle = 1
    """ Скругленное """


class ksBendSideTypeEnum:  # ksbendsidetypeenum.html
    """ ## ksBendSideTypeEnum - Тип построения боковой стороны сгиба """
    ksBendSideByAngle    = 0
    """ По уклону и углу """
    ksBendSideByWidening = 1
    """ По расширению """


class ksBendTypeEnum:  # ksbendtypeenum.html
    """ ## ksBendTypeEnum - Способ сгиба """
    ksLineBend        = 0
    """ По линии сгиба """
    ksBendLineOutside = 1
    """ Линия сгиба снаружи """
    ksBendLineInside  = 2
    """ Линия сгиба внутри """
    ksBendByTouch     = 3
    """ По касанию """
    ksBendByCentre    = 4
    """ По центру """


class ksBisectorVariant:  # ksbisectorvariant.html
    """ ## ksBisectorVariant - Вариант решения биссектрисы для двух прямых """
    ksBVNone       = 0
    """ Неопределенное направление (ближайшее решение) """
    ksBVNormalSum  = 1
    """ Биссектриса вдоль суммы нормалей прямых/отрезков """
    ksBVNormalDiff = 2
    """ Биссектриса вдоль разности нормалей прямых/отрезков """


class ksBmpSizeEnum:  # ksbmpsizeenum.html
    """ ## ksBmpSizeEnum - Размеры иконок """
    ksBmp1616 = 0
    """ 16*16 """
    ksBmp2424 = 1
    """ 24*24 """
    ksBmp3232 = 2
    """ 32*32 """
    ksBmp4848 = 3
    """ 48*48 """


class ksBreakLineTypeEnum:  # ksbreaklinetypeenum.html
    """ ## ksBreakLineTypeEnum - Тип линии разрыва """
    ksBLNotImage = 0
    """ Не отображается """
    ksBLStraight = 1
    """ Прямая """
    ksBLBreak    = 2
    """ С изломом """
    ksBLVawe     = 3
    """ Волнистая """


class ksCentreMarkerEnum:  # kscentremarkerenum.html
    """ ## ksCentreMarkerEnum - Тип обозначения центра """
    ksCMUnknown   = -1
    """ Неизвестный """
    ksCMPlusPoint = 0
    """ Маленький крестик """
    ksCMOneAxis   = 1
    """ Одна ось """
    ksCMTwoAxis   = 2
    """ Две оси """


class ksChamferBuildingTypeEnum:  # kschamferbuildingtypeenum.html
    """ ## ksChamferBuildingTypeEnum - Типы построения фаски """
    ksChamferSideAngle = 0
    """ По стороне и углу """
    ksChamferTwoSides  = 1
    """ По двум сторонам """


class ksChangeLeaderSignEnum:  # kschangeleadersignenum.html
    """ ## ksChangeLeaderSignEnum - Тип значка для обозначения изменения """
    ksCLSSquare        = 0
    """ Квадрат """
    ksCLSCircle        = 1
    """ Окружность """
    ksCLSBracketSquare = 2
    """ Квадратные скобки """
    ksCLSBracketCircle = 3
    """ Круглые скобки """
    ksCLSBracketCorner = 4
    """ Угловые скобки """


class ksChangeOrderType:  # kschangeordertype.html
    """ ## ksChangeOrderType - Тип изменения порядка объектов """
    ksChangeOrderTop                      = 1
    """ Выше всех """
    ksChangeOrderBottom                   = 2
    """ Ниже всех """
    ksChangeOrderBeforeObject             = 3
    """ Перед объектом """
    ksChangeOrderAfterObject              = 4
    """ За объектом """
    ksChangeOrderUpLevel                  = 5
    """ На уровень вперед """
    ksChangeOrderDownLevel                = 6
    """ На уровень назад """
    ksChangeOrderBeforeObjectByGroupOrder = 7
    """ Перед объектом (расположить объекты группы в порядке их добавления в группу) """
    ksChangeOrderAfterObjectByGroupOrder  = 8
    """ За объектом (расположить объекты группы в порядке их добавления в группу) """


class ksCheckBoxVisualStyleEnum:  # kscheckboxvisualstyleenum.html
    """ ## ksCheckBoxVisualStyleEnum - Визуальный стиль чекбокса """
    ksCheckBoxDefault  = 0
    """ Обычный """
    ksCheckBoxSwitcher = 1
    """ Переключатель """


class ksCheckSumVersionEnum:  # kschecksumversionenum.html
    """
    ## ksCheckSumVersionEnum - Версии контрольных сумм

    ksCsrKompas10SP2 = 0x0A001023

    ksCsrKompas13SP1 - До выхода КОМПАС 13 SP1 равен версии текущей задачи.
    """
    KsCsrCurrent     = 0
    """ Версия текущей задачи КОМПАС """
    ksCsrKompas10SP2 = -1
    """ Версия KOMPAS 10 SP2 """
    ksCsrKompas11    = -5
    """ Версия KOMPAS 11 """
    ksCsrKompas11SP1 = -6
    """ Версия KOMPAS 11 SP1 """
    ksCsrKompas12    = -10
    """ Версия KOMPAS 12 """
    ksCsrKompas12SP1 = -11
    """ Версия KOMPAS 12 SP1 """
    ksCsrKompas13    = -15
    """ Версия KOMPAS 13 """
    ksCsrKompas13SP1 = -16
    """ Версия KOMPAS 13 SP1 """
    ksCsrKompas14SP1 = -21
    """ Версия KOMPAS 14 SP1 """
    ksCsrKompas14SP2 = -22
    """ Версия KOMPAS 14 SP2 """
    ksCsrKompas15    = -25
    """ Версия KOMPAS 15 """
    ksCsrKompas15Sp2 = -27
    """ Версия KOMPAS 15 SP2 """
    ksCsrKompas16    = -30
    """ Версия KOMPAS 16 """
    ksCsrKompas16Sp1 = -31
    """ Версия KOMPAS 16 SP1 """
    ksCsrKompas17    = -35
    """ Версия KOMPAS 17 """
    ksCsrKompas17Sp1 = -36
    """ Версия KOMPAS 17 SP1 """
    ksCsrKompas18    = -37
    """ Версия KOMPAS 18 """


class ksChooseBodiesType:  # kschoosebodiestype.html
    """
    ## ksChooseBodiesType - Типы действий над телами для операций

    Для операций сечение плоскостью и сечение эскизом значение ksNewBody интерпретируется как ksAutomaticDefinition.
    """
    ksNewBody             = 0
    """ Новое тело. """
    ksAutomaticDefinition = 1
    """ Автоматический выбор тел. """
    ksManualEditing       = 2
    """ Ручное указание тел. """
    ksAllBodies           = 3
    """ Все тела. """


class ksChooseManagerTypeEnum:  # kschoosemanagertypeenum.html
    """ ## ksChooseManagerTypeEnum - Тип менеджера выбора объектов """
    ksChMUnknown         = -2
    """ Неизвестный """
    ksChMAllColors       = -1
    """ Любой менеджер """
    ksChMLevel1ColorBase = 0
    """ Основная группа выбора. Цвет - Указание 1 """
    ksChMLevel1Color1    = 1
    """ Дополнительная группа выбора. Цвет - Указание 2 """
    ksChMLevel1Color2    = 2
    """ Дополнительная группа выбора. Цвет - Указание 3 """
    ksChMLevel2ColorBase = 100
    """ Основная группа выбора. Уровень 2. Цвет - Указание 1 """
    ksChMLevel2Color1    = 101
    """ Дополнительная группа выбора. Уровень 2. Цвет - Указание 2 """
    ksChMLevel2Color2    = 102
    """ Дополнительная группа выбора. Уровень 2. Цвет - Указание 3 """
    ksChMUser1           = 201
    """ Пользовательская группа выбора 1 """
    ksChMUser2           = 202
    """ Пользовательская группа выбора 2 """
    ksChMUser3           = 203
    """ Пользовательская группа выбора 3 """
    ksChMUser4           = 204
    """ Пользовательская группа выбора 4 """
    ksChMUser5           = 205
    """ Пользовательская группа выбора 5 """
    ksChMUser6           = 206
    """ Пользовательская группа выбора 6 """
    ksChMUser7           = 207
    """ Пользовательская группа выбора 7 """
    ksChMUser8           = 208
    """ Пользовательская группа выбора 8 """
    ksChMUser9           = 209
    """ Пользовательская группа выбора 9 """
    ksChMUser10          = 210
    """ Пользовательская группа выбора 10 """


class ksChoosePartsType:  # kschoosepartstype.html
    """ ## ksChoosePartsType - Способ определения области применения для компонентов в сборочной операции """
    ksChAutomaticDefinition = 1
    """ Автоопределение """
    ksChManualEditing       = 2
    """ Ручное редактирование """
    ksChAllParts            = 3
    """ Все компоненты """
    ksChNoLibraryParts      = 4
    """ Все компоненты, кроме библиотечных """


class ksChooseType:  # kschoosetype.html
    """ ## ksChooseType - Область применения """
    ksChBodiesAndParts = 1
    """ Компоненты и тела """
    ksChParts          = 2
    """ Компоненты """
    ksChBodies         = 3
    """ Все компоненты """


class ksCircularPatternBuildingTypeEnum:  # kscircularpatternbuildingtypeenum.html
    """ ## ksCircularPatternBuildingTypeEnum - Способ построения массива по концентрической сетке """
    ksCPSaveAll           = 0
    """ Стандартная схема """
    ksCPChessOrderByAxis1 = 1
    """ Шахматный порядок - сдвиг вдоль первой оси (концентрическое направление """
    ksCPChessOrderByAxis2 = 2
    """ Шахматный порядок - сдвиг вдоль второй оси (радиальное направление) """


class ksCloudPointsSurfaceBuildingTypeEnum:  # kscloudpointssurfacebuildingtypeenum.html
    """ ## ksCloudPointsSurfaceBuildingTypeEnum - Тип поверхности по пласту (облаку) точек """
    ksCLByPoints   = 0
    """ Сплайновая поверхность по точкам """
    ksCLByPole     = 1
    """ Сплайновая поверхность по полюсам """
    ksCLPolyhedral = 2
    """ Многогранная поверхность """


class ksCloudTypeEnum:  # kscloudtypeenum.html
    """ ## ksCloudTypeEnum - Способ распознавания сети точек """
    ksCLAuto    = 0
    """ Автоматически """
    ksCLLocalCS = 1
    """ В плоскости CK """
    ksCLScreen  = 2
    """ В плоскости экрана """


class ksColouringTypeEnum:  # kscolouringtypeenum.html
    """ ## ksColouringTypeEnum - Тип заливки """
    ksColouringSolid    = 0
    """ Одноцветная """
    ksColouringLinear   = 1
    """ Линейная """
    ksColouringAngle    = 2
    """ Угловая """
    ksColouringCone     = 3
    """ Коническая """
    ksColouringCircle   = 4
    """ Радиальная """
    ksColouringSquare   = 5
    """ Квадратная """
    ksColouringCylinder = 6
    """ Цилиндрическая """


class ksConicCurvePontIndexEnum:  # ksconiccurvepontindexenum.html
    """ ## ksConicCurvePontIndexEnum - Индекс точки конической кривой """
    ksCCBeginPoint     = 0
    """ Начальная точка """
    ksCCEndPoint       = 1
    """ Конечная точка """
    ksCCIntersectPoint = 2
    """ Точка пересечения """
    ksCCPointOnCurve   = 3
    """ Точка на кривой """


class ksConjunctivePointTypeEnum:  # ksconjunctivepointtypeenum.html
    """ ## ksConjunctivePointTypeEnum - Способ построение присоединительной точки """
    ksCPByObject        = 0
    """ По объекту """
    ksCPManualDirection = 1
    """ Ручное задание направление осей """


class ksConnectTypeEnum:  # ksconnecttypeenum.html
    """ ## ksConnectTypeEnum - Тип соединения кривых """
    ksCTUnknown  = -1
    """ Неизвестный """
    ksCTPosition = 0
    """ Соединение по позиции """
    ksCTTangent  = 1
    """ Соединение по касательной """
    ksCTNormal   = 2
    """ Соединение перпендикулярно """
    ksCTSmooth   = 3
    """ Гладкое соединение """


class ksConstraintTypeEnum:  # ksconstrainttypeenum.html
    """
    ## ksConstraintTypeEnum – Типы параметрических ограничений

    При использовании API 5 частичным аналогом данного перечисления является набор типов параметрических ограничений.
    """
    ksCUnknown            = 0
    """ Неизвестный тип """
    ksCFixedPoint         = 1
    """ Фиксировать точку """
    ksCPointOnCurve       = 2
    """ Точка на кривой """
    ksCHorizontal         = 3
    """ Горизонталь """
    ksCVertical           = 4
    """ Вертикаль """
    ksCParallel           = 5
    """ Параллельность двух прямых или отрезков """
    ksCPerpendicular      = 6
    """ Перпендикулярность двух прямых или отрезков """
    ksCEqualLength        = 7
    """ Равенство длин двух отрезков """
    ksCEqualRadius        = 8
    """ Равенство радиусов двух дуг/окружностей. """
    ksCHAlignPoints       = 9
    """ Выравнивать две точки по горизонтали """
    ksCVAlignPoints       = 10
    """ Выравнивать две точки по вертикали """
    ksCMergePoints        = 11
    """ Совпадение двух точек """
    ksCAssociation        = 12
    """ Ассоциативная связь """
    ksCDimWithVariable    = 13
    """ Размер с переменной """
    ksCFixedDim           = 14
    """ Фиксированный размер """
    ksCTangentTwoCurves   = 15
    """ Касание двух кривых """
    ksCSymmetryTwoPoints  = 16
    """ Симметрия двух точек относительно отрезка """
    ksCCollinear          = 17
    """ Коллинеарность двух отрезков """
    ksCFixedAngle         = 18
    """ Фиксированный угол """
    ksCFixedLenght        = 19
    """ Фиксированная длина """
    ksCPointOnCurveMiddle = 20
    """ Точка на середине кривой """
    ksCBisector           = 21
    """ Биссектриса """
    ksCConcentricity      = 22
    """ Cовпадение центров окружностей, дуг, эллипсов и точек """


class ksConstraintsStateEnum:  # ksconstraintsstateenum.html
    """ ## ksConstraintsStateEnum - Параметрическое состояние системы """
    ksStateUnknown              = 0
    """ Состояние не известно """
    ksStateWellConstrained      = 1
    """ Полностью определенная система - все степени свободы нулевые """
    ksStateUnderConstrained     = 2
    """ Недоопределенная система - имеются ненулевые степени свободы """
    ksStateUnresolvedRedundancy = 3
    """ Имеются не удовлетворенные избыточные ограничения """


class ksClosingClosedTypeEnum:  # ksclosingclosedtypeenum.html
    """ ## ksClosingClosedTypeEnum - Способ замыкания углов листового тела """
    ksClosingCJoint        = 0
    """ Замыкание встык """
    ksClosingCOver         = 1
    """ Замыкание с перекрытием """
    ksClosingCTightClosure = 2
    """ Плотное замыкание """


class ksClosingCorneringEnum:  # ksclosingcorneringenum.html
    """ ## ksClosingCorneringEnum - Обработка угла при замыкании """
    ksCorneringNone          = 0
    """ Без обработки """
    ksCorneringJointOnBorder = 1
    """ Стык по кромке """
    ksCorneringJointOnChord  = 2
    """ Стык по хорде """
    ksCorneringCircled       = 3
    """ Круговая """


class ksClosingHolePlacementEnum:  # ksclosingholeplacementenum.html
    """ ## ksClosingHolePlacementEnum - Размещение отверстия при круговой обработке угла """
    ksCorneringHPBend  = 0
    """ На пересечении сгибов """
    ksCorneringHPAngle = 1
    """ В точке угла """
    ksCorneringHPPoint = 2
    """ Через точку угла """


class ksClosingTypeEnum:  # ksclosingtypeenum.html
    """ ## ksClosingTypeEnum - Тип замыкания операции сгиб по эскизу листового тела """
    ksClosingAngles = 0
    """ Замыкание смежных углов """
    ksClosingBegin  = 1
    """ Замыкание в начале """
    ksClosingEnd    = 2
    """ Замыкание в конце """


class ksCornerFormEnum:  # kscornerformenum.html
    """ ## ksCornerFormEnum - Способы обработки углов стыковки """
    ksCornerFormUnknown = 0
    """ Не срезать углы """
    ksCornerFormUniform = 2
    """ Срезать углы """


class ksCreateCommonNameState:  # kscreatecommonnamestate.html
    """ ## ksCreateCommonNameState - Состояние общего наименования """
    ksCommonNameCreationAvailable             = 0
    """ Доступно создание общего наименования """
    ksCommonNameDocIsReadOnly                 = 1
    """ Недоступно: документ открыт только для чтения """
    ksCommonNameRequiredConvert               = 2
    """ Недоступно: необходимо преобразовать спецификацию """
    ksCommonNameHideObjects                   = 3
    """ Недоступно: в режиме показа скрытых объектов """
    ksCommonNameAllObjects                    = 4
    """ Недоступно: в режиме показа всех объектов """
    ksCommonNameExcludedObjects               = 5
    """ Недоступно: в режиме показа исключенных объектов """
    ksCommonNameEnableSortSpcObj              = 6
    """ Недоступно: объект спецификации должен быть базовым """
    ksCommonNameInvalidSection                = 7
    """ Недоступно: неподходящий раздел """
    ksCommonNameInvalidSection                = 8
    """ Недоступно: объект уже в составе общего наименования """
    ksCommonNameRequireNameColumnStandardInfo = 9
    """ Недоступно: в наименовании объекта отсутствует информация о стандарте """
    ksCommonNameRequiredSPDoc                 = 10
    """ Недоступно: создание объекта доступно в документе спецификации и в спецификации на листе """


class ksCrossSectionPlaneBuildingTypeEnum:  # kscrosssectionplanebuildingtypeenum.html
    """ ## ksCrossSectionPlaneBuildingTypeEnum - Способ построения секущей плоскости для шага динамического сечения """
    ksCrossSectionPlaneByModelPlan = 0
    """ По плоскости модели """
    ksCrossSectionPlaneByOtherStep = 1
    """ По плоскости сечения предыдущего шага """


class ksCurvesIntersectFormEnum:  # kscurvesintectformenum.html
    """ ## ksCurvesIntersectFormEnum - Тип пересечения """
    ksCurvesIntersectSimple  = 0
    """ Обыкновенная точка пересечения """
    ksCurvesIntersectTangent = 1
    """ Касательная точка персечения """


class ksCurveStyleTypeEnum:  # kscurvestyletypeenum.html
    """ ## ksCurveStyleTypeEnum - Тип стиля кривой """
    ksCSTSoldLine   = 0
    """ Сплошная """
    ksCSTBrokenLine = 1
    """ Прерывистая """


class ksCurvePenTypeEnum:  # kscurvepentypeenum.html
    """ ## ksCurvePenTypeEnum - Способ задания параметров пера """
    ksCPTIndependent = 0
    """ Задано значением """
    ksCPTBasicLine   = 1
    """ Как у основной линии """
    ksCPTThinLine    = 2
    """ Как у тонкой линии """
    ksCPTHeavyLine   = 3
    """ Как у утолщенной линии """


class ksConicCurve3DBuildingTypeEnum:  # ksconiccurve3dbuildingtypeenum.html
    """ ## ksConicCurve3DBuildingTypeEnum - Способ построения конической 3D кривой """
    ksConicCurve3DVertexAndHeight         = 0
    """ Коническая кривая по вершине и дискриминанту """
    ksConicCurve3DVertexAndPointOnCurve   = 1
    """ Коническая кривая по вершине и точке на кривой """
    ksConicCurve3DTangentsAndHeight       = 2
    """ Коническая кривая по касательным и дискриминанту """
    ksConicCurve3DTangentsAndPointOnCurve = 3
    """ Коническая кривая по касательным и точке на кривой """


class ksConicCurve3DParameterEnum:  # ksconiccurve3dparameterenum.html
    """ ## ksConicCurve3DParameterEnum - Индекс параметра конической 3D кривой """
    ksConicCurve3DBeginPoint = 0
    """ Начальная точка """
    ksConicCurve3DEndPoint   = 1
    """ Конечная точка """
    ksConicCurve3DVertex     = 2
    """ Вершина """
    ksConicCurve3DOnCurve    = 3
    """ Точка на кривой """
    ksConicCurve3DCount      = 4
    """ Количество опорных точек """


class ksConicSurfaceBuildingTypeEnum:  # ksconicsurfacebuildingtypeenum.html
    """ ## ksConicSurfaceBuildingTypeEnum - Способ построения треугольника """
    ksConicSurfaceBuildBySides = 0
    """ Через задание углов двух сторон """
    ksConicSurfaceBuildByCurve = 1
    """ По вершинной кривой """


class ksConicSurfaceMovementTypeEnum:  # ksconicsurfacemovementtypeenum.html
    """ ## ksConicSurfaceMovementTypeEnum - Движение сечения """
    ksConicSectionSelfParallel = 0
    """ Параллельно самому себе """
    ksConicSectionAllongAxis   = 1
    """ По осевой линии """
    ksConicSectionByRadial     = 2
    """ По осевой линии """


class ksConicSurfaceSectionCurveFormEnum:  # ksconicsurfacesectioncurveformenum.html
    """ ## ksConicSurfaceSectionCurveFormEnum - Способ задания формы кривой конического сечения """
    ksSectionCurveByCoefficient    = 0
    """ По коэффициенту """
    ksSectionCurveByCurveOnSurface = 1
    """ По кривой на поверхности """
    ksSectionCurveByTangentSurface = 2
    """ По касательной поверхности """
    ksSectionCurveByLeastTension   = 3
    """ Минимальное напряжение """


class ksConicSectionTrianglePointEnum:  # ksconicsectiontrianglepointenum.html
    """ ## ksConicSectionTrianglePointEnum - Движение сечения """
    ksConicSectionTrianglePointLeft   = 0
    """ Левая точка """
    ksConicSectionTrianglePointRight  = 1
    """ Правая точка """
    ksConicSectionTrianglePointTop    = 2
    """ Верхняя точка """
    ksConicSectionTrianglePointMedian = 3
    """ Медиана из верхней точки """


class ksConicSurfaceSideAngleBuildingTypeEnum:  # ksconicsurfacesideanglebuildingtypeenum.html
    """ ## ksConicSurfaceSideAngleBuildingTypeEnum - Условие построения угла треугольника конической поверхности при построении по грани """
    ksConicSectionSurfaceSideAngleTangent = 0
    """ По касательной. Результирующий угол - угол между касательной к грани и основанием треугольника """
    ksConicSectionSurfaceSideAngleNormal  = 1
    """ Перпендикулярно. Результирующий угол - угол между перпендикуляром к грани и основанием треугольника """


class ksConicSurfaceSideBuildingTypeEnum:  # ksconicsurfacesidebuildingtype.html
    """ ## ksConicSurfaceSideBuildingTypeEnum - Способ построения стороны в треугольнике """
    ksConicSectionSurfaceSideByAngle = 0
    """ От хорды. По функции угла """
    ksConicSectionSurfaceSideByFace  = 1
    """ От объекта. По направляющей грани """


class ksConicTypeEnum:  # ksconictypeenum.html
    """ ## ksConicTypeEnum - Способ определения параметров конического отверстия """
    ksCNDiameter = 0
    """ По диаметру верхнего основания конуса """
    ksCNAngle    = 1
    """ По углу конуса """


class ksContentDialogNotifyEnum:  # kscontentdialognotifyenum.html
    """ ## ksContentDialogNotifyEnum - События диалога с произвольным наполнением """
    ksCDCreateContentCallback = 1
    """ Создание контента """
    ksCDDestroyContent        = 2
    """ Удаление контента """
    ksCDExecuteCommand        = 3
    """ Выполнить команду """
    ksCDButtonUpdate          = 4
    """ Установка состояния кнопки панели """


class ksColorBPPEnum:  # kscolorbppenum.html
    """ ## ksColorBPPEnum - Цвет """
    ksColorBPP_O1 = 1
    """ Черный """
    ksColorBPP_O2 = 2
    """ 4 цвета """
    ksColorBPP_O4 = 4
    """ 16 цветов """
    ksColorBPP_O8 = 8
    """ 256 цветов """
    ksColorBPP_16 = 16
    """ 16 разрядов """
    ksColorBPP_24 = 24
    """ 24 разряда """
    ksColorBPP_32 = 32
    """ 32 разряда """


class ksContourSegmentEnum:  # kscontoursegmentenum.html
    """ ## ksContourSegmentEnum - Типы сегментов контура """
    ksCSUnknown    = -1
    """ Неизвестный объект """
    ksCSLineSeg    = 1
    """ Отрезок """
    ksCSCircle     = 2,
    """ Окружность """
    ksCSArc        = 3
    """ Дуга """
    ksCSBezier     = 8
    """ Bezier сплайн """
    ksCSEllipse    = 32
    """ Эллипс """
    ksCSNurbs      = 33
    """ Nurbs сплайн """
    ksCSEllipseArc = 34
    """ Дуга эллипса """


class ksContour3DTypeEnum:  # kscontour3dtypeenum.html
    """ ## ksContour3DTypeEnum - Тип контура """
    ksCTAuto    = 0
    """ Автоопределение типа """
    ksCTSpace   = 1
    """ Произвольный контур """
    ksCTSurface = 2
    """ Контур на грани """
    ksCTSketch  = 3
    """ Контур эскиза """


class ksCoordLawEnum:  # kscoordlawenum.html
    """ ## ksCoordLawEnum - Порядок законов """
    ksCLawX = 0
    """ Закон X """
    ksCLawY = 1
    """ Закон Y """
    ksCLawZ = 2
    """ Закон Z """


class ksCopyGeometryBuildingTypeEnum:  # kscopygeometrybuildingtypeenum.html
    """ ## ksCopyGeometryBuildingTypeEnum - Способ построения операции копия геометрии """
    ksCGBTWithoutGrouping  = 0
    """ Без группировки. """
    ksCGBTBodyFaceGrouping = 1
    """ Собрать грани по исходным элементам. C группировкой граней одного тела """


class ksCornerTypeEnum:  # kscornertypeenum.html
    """ ## ksCornerTypeEnum - Тип угла объекта для прямоугольника и многоугольника """
    ksCTNoProcess = 0
    """ Без обработки """
    ksCTChamfer   = 1
    """ Фаска """
    ksCTFillet    = 2
    """ Скругление """


class ksCountersinkTypeEnum:  # kscountersinktypeenum.html
    """ ## ksCountersinkTypeEnum - Способ определения параметров зенковки """
    ksCTDiameterAngle = 0
    """ По диаметру и углу """
    ksCTDepthAngle    = 1
    """ По глубине и углу """
    ksCTDiameterDepth = 2
    """ По диаметру и глубине """


class ksCurveProjectionTypeEnum:  # kscurveprojectiontypeenum.html
    """ ## ksCurveProjectionTypeEnum - Тип проекции кривой """
    ksCPNearest            = 0
    """ Ближайшая проекция """
    ksCPNearestByDirection = 1
    """ По направлению """


class ksCutBuildingTypeEnum:  # kscutbuildingtypeenum.html
    """ ## ksCutBuildingTypeEnum - Способ создания сечения """
    ksCutByContour = 0
    """ Сечение контуром """
    ksCutByPlane   = 1
    """ Сечение плоскостью """


class ksCurveStyleEnum:  # kscurvestyleenum.html
    """ ## ksCurveStyleEnum – Системные стили линии """
    ksCSHidden                   = -1
    """ - Невидимая (скрытая; для кривых) """
    ksCSUnvisible                = 0
    """ - Невидимая (для таблицы) """
    ksCSNormal                   = 1
    """ - основная, """
    ksCSThin                     = 2
    """ - тонкая, """
    ksCSAxial                    = 3
    """ - осевая, """
    ksCSDashed                   = 4
    """ - штриховая, """
    ksCSBrokenLine               = 5
    """ - для линии обрыва """
    ksCSConstruction             = 6
    """ - вспомогательная, """
    ksCSThick                    = 7
    """ - утолщенная, """
    ksCSDash2Dots                = 8
    """ - пунктир 2, """
    ksCSDashedNormal             = 9
    """ - штриховая осн. """
    ksCSNormalDashDot            = 10
    """ - осевая осн. """
    ksCSISO02Dashed              = 12
    """ - ISO 02 штриховая линия, """
    ksCSISO03DashedLSpace        = 13
    """ - ISO 03 штриховая линия (дл. пробел), """
    ksCSISO04DashDotLDash        = 14
    """ - ISO 04 штрихпунктирная линия (дл. штрих), """
    ksCSISO05DashDotLDash2Dots   = 15
    """ - ISO 05 штрихпунктирная линия (дл. штрих 2 пунктира), """
    ksCSISO06DashDotLDash3Dots   = 16
    """ - ISO 06 штрихпунктирная линия (дл. штрих 3 пунктира), """
    ksCSISO07Dotted              = 17
    """ - ISO 07 пунктирная линия, """
    ksCSISO08DashDotLShDashes    = 18
    """ - ISO 08 штрихпунктирная линия (дл. и кор. штрихи), """
    ksCSISO09DashDot1L2ShDashes  = 19
    """ - ISO 09 штрихпунктирная линия (дл. и 2 кор. штриха), """
    ksCSISO10DashDot             = 20
    """ - ISO 10 штрихпунктирная линия, """
    ksCSISO11DashDot2Dashes      = 21
    """ - ISO 11 штрихпунктирная линия (2 штриха), """
    ksCSISO12DashDot2Dots        = 22
    """ - ISO 12 штрихпунктирная линия (2 пунктира), """
    ksCSISO13DashDot3Dots        = 23
    """ - ISO 13 штрихпунктирная линия (3 пунктира), """
    ksCSISO14DashDot2Dashes2Dots = 24
    """ - ISO 14 штрихпунктирная линия (2 штриха 2 пунктира), """
    ksCSISO15DashDot2Dashes3Dots = 25
    """ - ISO 15 штрихпунктирная линия (2 штриха 3 пунктира). """


class ksDecimalDelimiterTypeEnum:  # ksdecimaldelimitertypeenum----.html
    """ ## ksDecimalDelimiterTypeEnum - Разделитель десятичной части размеров """
    ksDecimalComma = 0
    """ Десятичная запятая """
    ksDecimalPoint = 1
    """ Десятичная точка """


class ksDepthTypeEnum:  # ksdepthtypeenum.html
    """ ## ksDepthTypeEnum - Способ определения глубины отверстия """
    ksDTValue        = 0
    """ На расстояние """
    ksDTReachThrough = 1
    """ Через все """
    ksDTObject       = 2
    """ До объекта """


class ksDesignationPointEnum:  # ksdesignationpointenum.html
    """ ## ksDesignationPointEnum - Типы точек обозначений """
    ksDesignationBasePoint  = 1
    """ Точка указания """
    ksDesignationShelfPoint = 2
    """ Точка на линии выноски обозначения """


class ksDimensionPointEnum:  # ksdimensionpointenum.html
    """ ## ksDimensionPointEnum - Типы точек размеров """
    ksDimensionTextPoint  = 0
    """ Точка привязки текста """
    ksDimensionBasePoint  = 1
    """ Точка указания размера """
    ksDimensionShelfPoint = 2
    """ Точка на линии выноске размера """
    ksDimensionLinePoint  = 3
    """ Точка на размерной линии """


class ksDimensionArrowPosEnum:  # ksdimensionarrowposenum.html
    """ ## ksDimensionArrowPosEnum - Размещение стрелок относительно выносной линии """
    ksDimArrowInside  = 0
    """ Стрелки изнутри """
    ksDimArrowOutside = 1
    """ Стрелки снаружи """
    ksDimArrowAuto    = 2
    """ Авторазмещение стрелок """


class ksDimensionBaseEnum:  # ksdimensionbaseenum.html
    """ ## ksDimensionBaseEnum - Параметр отрисовки текста """
    ksDimBaseCenter      = 0
    """ От центра """
    ksDimBaseP1          = 1
    """ От первой выносной линии """
    ksDimBaseP2          = 2
    """ От второй выносной линии """
    ksDimCommonBase      = 3
    """ Размер с общей размерной линией (текст размера выводится вертикально у второй выносной линии) """
    ksDimFirstCommonBase = 4
    """ Первый размер в цепочке размерных линий (у первой выносной линии отрисовывается текст '0', текст размера выводится вертикально у второй выносной линии). """


class ksDimensionDeviationEnum:  # ksdimensiondeviationenum.html
    """ ## ksDimensionDeviationEnum - Отклонения номинального значения размера """
    ksDimDeviation  = 0
    """ Отклонения """
    ksDimLimits     = 1
    """ Предельные значения (предельные значения записываются одно над другим) """
    ksDimLineLimits = 2
    """ Предельные значения в одну строку (предельные значения записываются друг за другом через дефис) """


class ksDimensionTextAlignEnum:  # ksdimensiontextalignenum.html
    """ ## ksDimensionTextAlignEnum - Выравнивание размерной надписи """
    ksDimACentreLowFont = 0
    """ По центру, с уменьшенным шрифтом """
    ksDimAUpperBoundary = 1
    """ По верхней границе """
    ksDimACentre        = 2
    """ По центру """
    ksDimALowerBoundary = 3
    """ По нижней границе """


class ksDimensionTextBracketsEnum:  # ksdimensiontextbracketsenum.html
    """ ## ksDimensionTextBracketsEnum - Размер в скобках """
    ksDimBracketsOff    = 0
    """ Размер без скобок """
    ksDimBrackets       = 1
    """ Размер в круглых скобках """
    ksDimSquareBrackets = 2
    """ Размер в квадратных скобках """


class ksDimensionTextPosEnum:  # ksdimensiontextposenum.html
    """ ## ksDimensionTextPosEnum - Положение размерной надписи отноcительно выносной линии """
    ksDimTextParallelOnLine  = 0
    """ Параллельно, над линией """
    ksDimTextParallelInCut   = 1
    """ Параллельно, в разрезе линии """
    ksDimTextHorizontalInCut = 2
    """ Горизонтально, в разрезе линии """


class ksDimensionTextTypeEnum:  # ksdimensiontexttypeenum.html
    """ ## ksDimensionTextTypeEnum - Тип размерной надписи """
    ksDimTAuto   = 0
    """ Автоматическое """
    ksDimTManual = 1
    """ Ручное """
    ksDTPOnShelf = 2
    """ На полке """


class ksDimTextFormatEnum:  # ksdimtextformatenum.html
    """
    ## ksDimTextFormatEnum - Формат отображения размерной надписи

    Используется только для углового размера.
    """
    ksDimTextFormatGMS = 0
    """ Градусы-минуты-секунды """
    ksDimTextFormatGDD = 1
    """ Градусы и десятичные доли градуса """


class ksDirectionTypeEnum:  # ksdirectiontypeenum.html
    """
    ## ksDirectionTypeEnum - Типы направлений выдавливания

    1. При типе направления dtMiddlePlane в методах SetSideParam и GetSideParam параметр depth интерпретируется как общая глубина выдавливания и задается следующим образом:

    SetSideParam(TRUE, etBlind, depth, ...)

    2. В API5 соответствует перечислению Direction_Type.
    """
    dtNormal      = 0
    """ прямое направление (для тонкой стенки - наружу) """
    dtReverse     = 1
    """ обратное направление (для тонкой стенки - внутрь) """
    dtBoth        = 2
    """ в обе стороны """
    dtMiddlePlane = 3
    """ от средней плоскости """


class ksDocumentFormatEnum:  # ksdocumentformatenum.html
    """ ## ksDocumentFormatEnum - Форматы листа """
    ksFormatA0   = 0
    """ Формат А0 """
    ksFormatA1   = 1
    """ Формат А1 """
    ksFormatA2   = 2
    """ Формат А2 """
    ksFormatA3   = 3
    """ Формат А3 """
    ksFormatA4   = 4
    """ Формат А4 """
    ksFormatA5   = 5
    """ Формат А5 """
    ksFormatUser = 6
    """ ksFormatUser """


class ksDocumentsLibraryInsertionTypeEnum:  # ksdocumentslibraryinsertiontypeenum.html
    """ ## ksDocumentsLibraryInsertionTypeEnum – Типы документов в библиотеке документов КОМПАС """
    ksInsertionUnknown  = 0
    """ Неизвестный тип """
    ksInsertionFragment = 2
    """ Фрагмент """
    ksInsertionPart     = 4
    """ Деталь """
    ksInsertionAssembly = 5
    """ Сборка """
    ksInsertionTextual  = 6
    """ Текстовый документ """
    ksInsertionRaster   = 20
    """ Растр """
    ksInsertionTable    = 21
    """ Таблица """
    ksInsertionTxtFile  = 22
    """ Текстовый документ. *.txt """


class ksDrawingObjecParamTypeEnum:  # ksdrawingobjecparamtypeenum.html
    """
    ## ksDrawingObjecParamTypeEnum – Тип параметров объекта

    При выдаче параметров в системе координат владельца для геометрических объектов учитывается также текущая суммарная матрица, задаваемая функцией Mtr.

    Примерами параметров, зависящих от суммарной матрицы, являются координаты точек, углы, длины, радиусы и т.п. Она не распространяется на параметры аннотационных объектов, так как аннотационные объекты не масштабируются. Примерами параметров аннотационных объектов, не зависящих от текущей суммарной матрицы, являются высота шрифта, сужение.
    """
    ksAllParam      = -1
    """ Параметры в системе координат владельца. """
    ksSheetAllParam = -2
    """ Параметры в системе координат листа. """
    ksViewAllParam  = -7
    """ Параметры в системе координат вида. """


class ksDynamicCrossSectionStepBuildingTypeEnum:  # ksdynamiccrosssectionstepbuildingtypeenum.html
    """ ## ksDynamicCrossSectionStepBuildingTypeEnum - Способ создания шага сечения модели """
    ksDCSTUnknown        = -1
    """ Неопределенный """
    ksDCSTByFreePlane    = 0
    """ Произвольная плоскость """
    ksDCSTByOffsetPlane  = 1
    """ Смещенная плоскость """
    ksDCSTByRotatedPlane = 2
    """ Повернутая плоскость """
    ksDCSTByZone         = 3
    """ Задано зоной """
    ksDCSTByBorderPoints = 4
    """ Параллелепипед """


class ksD3ConverterOptionsEnum:  # ksd3converteroptionsenum.html
    """ ## ksD3ConverterOptionsEnum - Константы, управляющие разрешением на чтение или запись объектов в дополнительные форматы jgs, sat, xt, step, stl, VRML """
    ksD3COBodyes               = 0
    """ Разрешение на чтение\\запись твёрдых тел """
    ksD3COSurfaces             = 2
    """ Разрешение на чтение\\запись поверхностей """
    ksD3COCurves               = 4
    """ Разрешение на чтение\\запись кривых """
    ksD3COSketches             = 6
    """ Разрешение на чтение (не применяется) \\запись эскизов """
    ksD3COInvisibleObjects     = 8
    """ Разрешение на чтение (не применяется) \\запись невидимых объектов """
    ksD3COPoints               = 10
    """ Разрешение на чтение\\запись точек """
    ksD3CODocumentProperties   = 12
    """ Разрешение на чтение\\запись информации о документе (автор, организация, комментарии) """
    D3COTechnicalDemand        = 14
    """ Разрешение на чтение\\запись технических требований """
    ksD3CODimensions           = 16
    """ Разрешение на чтение\\запись размеров """
    ksD3COAttributes           = 18
    """ Разрешение на чтение\\запись атрибутов объектов """
    ksD3CBRep                  = 20
    """ Разрешение на чтение\\запись форм изделий в граничном представлении (только в JT) """
    ksD3CPolygonal             = 22
    """ Разрешение на чтение\\запись полигональных форм изделий """
    ksD3CPolygonalLOD0         = 24
    """ Разрешение на чтение\\запись полигональных форм изделий уровня детализации 0 """
    ksD3CAssociated            = 26
    """ Разрешение на чтение ассоциированной геометрии (резьбы и др) """
    ksD3COStyle                = 28
    """ Разрешение на чтение\\запись элементов оформления (цвет, начертание, и т.п.) """
    ksD3CODensity              = 30
    """ Разрешение на чтение\\запись единиц плотности """
    ksD3COValidationProperties = 32
    """ Разрешение на чтение\\запись контрольных параметров - объёма, площади поверхности, центра масс """


class ksFindObject3DParametersNotifyEnum:  # ksfindobject3dparametersnotifyenum.html
    """ ## ksFindObject3DParametersNotifyEnum - События функции поиска объектов 3D """
    ksFOPFilterObject3D = 1
    """ 1Фильтрация объектов """


class ksEditableStateEnum:  # kseditablestateenum.html
    """ ## ksEditableStateEnum - Способ редактирования """
    ksESUndefined = -1
    """ Неопределенное состояние """
    ksESDisable   = 0
    """ Не проецировать """
    ksESEnable    = 1
    """ Проецировать """
    ksESByLayer   = 2
    """ По слою """


class ksEditColorTypeEnum:  # kseditcolortypeenum.html
    """ ## ksEditColorTypeEnum -Тип цвета редактирования """
    ksECSelectObject  = 0
    """ Подсвечивание - Выделенный объект """
    ksECChooseObject1 = 1
    """ Подсвечивание - Указанный объект 1 """
    ksECChooseObject2 = 2
    """ Подсвечивание - Указанный объект 2 """
    ksECChooseObject3 = 3
    """ Подсвечивание - Указанный объект 3 """
    ksECPassiveParts  = 4
    """ Контекстное редактирование - Пассивные компоненты """
    ksECFacePhantom   = 5
    """ Фантом грани """
    ksECLabelsPhantom = 6
    """ Фантом надписи """
    ksECDimensions    = 7
    """ Размеры """


class ksEditListCommandEnum:  # kseditlistcommandenum.html
    """ ## ksEditListCommandEnum - Идентификаторы стандартных команд для элемента панели свойств - Список """
    ksListItemNew      = 1
    """ Создать новый элемент в списке """
    ksListItemDelete   = 2
    """ Удалить выделенные элементы из списка """
    ksListItemMoveUp   = 3
    """ Переместить вверх """
    ksListItemMoveDown = 4
    """ Переместить вниз """
    ksListItemEdit     = 5
    """ Редактировать элемент в списке """


class ksEditListTypeEnum:  # kseditlisttypeenum.html
    """ ## ksEditListTypeEnum - Тип списка панели свойств """
    ksEditList  = 0
    """ Обычный список """
    ksCheckList = 1
    """ Список флагов """
    ksRadioList = 2
    """ Список переключателей """


class ksEquidistantTypeEnum:  # ksequidistanttypeenum.html
    """ ## ksEquidistantTypeEnum - Тип построения эквидистанты """
    ksETUnknown = -1
    """ Неизвестный """
    ksETLeft    = 0
    """ Слева по направлению """
    ksETRight   = 1
    """ Справа по направлению """
    ksETBoth    = 2
    """ С двух сторон """


class ksEquidistant3DCutModeEnum:  # ksequidistant3dcutmodeenum.html
    """ ## ksEquidistant3DCutModeEnum - Обход углов эквидистанты 3D """
    ksECMUnknown = 0
    """ Не определен """
    ksECMLineSeg = 1
    """ Обход срезом """
    ksECMCircle  = 2
    """ Обход дугой """


class ksEndFaceTypeEnum:  # ksendfacetypeenum.html
    """ ## ksEndFaceTypeEnum - Форма торца отверстия """
    ksEFFlat   = 0
    """ Плоский """
    ksEFConic  = 1
    """ Конический """
    ksEFSphere = 2
    """ Сферический """


class ksEndTypeEnum:  # ksendtypeenum.html
    """
    ## ksEndTypeEnum - типы операций выдавливания

    1. При типах выдавливания etUpToVertexTo, etUpToVertexFrom, etUpToSurfaceTo и etUpToSurfaceFrom в методах SetSideParam и GetSideParam параметр depth интерпретируется как глубина, вычитаемая или добавляемая к расстоянию до указанного объекта. Объект, определяющий глубину, задается с помощью метода SetDepthObject.

    2. В API5 соответствует перечислению End_Type.
    """
    etBlind           = 0
    """ строго на глубину """
    etThroughAll      = 1
    """ через всю деталь """
    etUpToVertexTo    = 2
    """ на расстояние до вершины """
    etUpToVertexFrom  = 3
    """ на расстояние за вершину """
    etUpToSurfaceTo   = 4
    """ на расстояние до поверхности """
    etUpToSurfaceFrom = 5
    """ на расстояние за поверхность """
    etUpToNearSurface = 6
    """ до ближайшей поверхности """


class ksEvolutionShiftSketchTypeEnum:  # ksevolutionshiftsketchtypeenum.html
    """ ## ksEvolutionShiftSketchTypeEnum - Тип движения сечения в кинематической операции """
    ksEvShiftParallel  = 0
    """ Образующая переносится параллельно самой себе """
    ksEvShiftKeepAngle = 1
    """ Образующая при переносе сохраняет исходный угол с направляющей """
    ksEvShiftOrtogonal = 2
    """ Плоскость образующей выставляется и сохраняется ортогональной направляющей """


class ksEvolutionVersionEnum:  # ksevolutionversionenum.html
    """ ## ksEvolutionVersionEnum - Версия оптимизации """
    ksEvolutionVersion1 = 1
    """ Вариант 1 """
    ksEvolutionVersion2 = 2
    """ Вариант 2 """


class ksExtensionCurveTypeEnum:  # ksextensioncurvetypeenum.html
    """ ## ksExtensionCurveTypeEnum - Тип продления кривой """
    ksExtensionCurveByCurve   = 0
    """ Продление той же кривой """
    ksExtensionCurveByTangent = 1
    """ По касательной """
    ksExtensionCurveByCircle  = 2
    """ По окружности """


class ksExtensionLimitTypeEnum:  # ksextensionlimittypeenum.html
    """ ## ksExtensionLimitTypeEnum - Способ ограничения """
    ksETLUnknown = -1
    """ Неизвестный """
    ksETLength   = 0
    """ На заданную длину """
    ksETLVertex  = 1
    """ До вершины """


class ksExtensionSurfaceTypeEnum:  # ksextensionsurfacetypeenum.html
    """ ## ksExtensionSurfaceTypeEnum - Тип продления поверхности """
    ksESTUnknown   = -1
    """ Неизвестный """
    ksESTSelf      = 0
    """ Той же поверхностью """
    ksESTTangent   = 1
    """ По касательной """
    ksESTDirection = 2
    """ По направлению """


class ksExternalFilesTypesEnum:  # ksexternalfilestypesenum.html
    """ ## ksExternalFilesTypesEnum - Тип внешнего файла """
    ksEFTUnknown                         = -1
    """ Неизвестный тип """
    ksEFTDocumentFile                    = 0
    """ Файл документа """
    ksEFTCurveStyleLibrary               = 1
    """ Библиотека стилей кривых """
    ksEFTTextStyleLibrary                = 2
    """ Библиотека стилей текстов """
    ksEFTHatchStyleLibrary               = 3
    """ Библиотека стилей штриховок """
    ksEFTAttributeTypesLibrary           = 4
    """ Библиотека типов атрибутов """
    ksEFTLayoutsLibrary                  = 5
    """ Библиотека оформлений """
    ksEFTFragmentFile                    = 6
    """ Фрагмент """
    ksEFTFragmentsLibrary                = 7
    """ Библиотека фрагментов """
    ksEFTSheetConnectedToSpc             = 8
    """ Лист сборки, подключенный к спецификации """
    ksEFTSystemFile                      = 9
    """ Системный файл """
    ksEFTIngotsLibrary                   = 10
    """ Библиотека типовых элементов (3D) """
    ksEFTPartFile                        = 11
    """ Деталь (3D) """
    ksEFTRasterFile                      = 12
    """ Растровое изображение """
    ksEFTDocConnectedToSpcObj            = 13
    """ Документ, подключенный к объекту спецификации """
    ksEFTSpcConnectedToSheet             = 14
    """ Спецификация, подключенная к листу сборки """
    ksEFTDocConnectedToSpcObjInOtherDocs = 15
    """ Документ, подключенный к объектам спецификации в других документах """
    ksEFTAssemblyFile                    = 16
    """ Файл-сборка (3D) """
    ksEFTModelsLibrary                   = 17
    """ Библиотека моделей """
    ksEFTTemporaryFile                   = 18
    """ Временный файл """
    ksEFTSourceFileForVariable           = 19
    """ Файлы-источники для переменных """
    ksEFTServiceFile                     = 20
    """ Служебный файл """
    ksEFTDraftFile                       = 21
    """ Чертеж """
    ksEFTHyperLink                       = 22
    """ Гиперссылка """
    ksEFTDataFile                        = 23
    """ Файл данных """
    ksEFTReadingRegimFile                = 24
    """ Файл режима чтения компонента """
    ksEFTCopyExternalGeometry            = 27
    """ Файл-источник копии внешней геометрии """
    ksEFExternalBilletPart               = 28
    """ Файлы деталей заготовок """
    ksEFTExternalLayoutGeometry          = 29
    """ Файлы компоновочной геометрии """
    ksEFTMetaDataSource                  = 30
    """ Файл-источник метаданных """
    ksEFTSheet                           = 31
    """ Файлы чертежей """
    ksEFTExternalRefContextFile          = 32
    """ Файл контекста внешней ссылки """
    ksEFTImportingInstanceSource         = 33
    """ Файлы импортированной вставки """
    ksEFTDummy                           = 34
    """ Файлы вставки-макета """
    ksEFTBendTable                       = 35
    """ Файл таблицы сгибов """
    ksEFTStandartProducts                = 36
    """ Файлы стандартных изделий """
    ksEFTProductPartSource               = 37
    """ Документ-источник свойств составной части """


class ksFeatureStateEnum:  # ksfeaturestateenum.html
    """ ## ksFeatureStateEnum - Состояние объекта """
    ksFSNone              = 0
    """ Состояния не определены """
    ksFSLocked            = 0x1
    """ Объект заблокирован\\Только чтение """
    ksFSRebuild           = 0x2
    """ Необходимо перестроить модель """
    ksFSInside3dMacro     = 0x4
    """ Объект включен в состав трехмерного макроэлемента """
    ksFSLCSDependent      = 0x8
    """ Зависимость от ЛСК """
    ksFSComprisedOfParts  = 0x10
    """ Тело состоит из частей """
    ksFSCurrent           = 0x20
    """ Текущая СК """
    ksFSReadOnlyAccessM3d = 0x40
    """ Файл компонента (m3d) имеет доступ “Только чтение” """
    ksFSDetailedFold      = 0x80
    """ Развернутый сгиб """
    ksFSSketchUndefined   = 0x100
    """ Эскиз не определен """
    ksFSSketchDefined     = 0x200
    """ Эскиз определен """
    ksFSSketchRedefined   = 0x400
    """ Эскиз переопределен """
    ksFSEditRestricted    = 0x800
    """ Редактирование запрещено, но запрет можно снять """
    ksFSEditImpossible    = 0x1000
    """ Редактирование запрещено """
    ksFSFixedComponent    = 0x2000
    """ Компонент зафиксирован """
    ksFSPutInRecalcState  = 0x4000
    """ Вставка компонента в пересчитанном состоянии """
    ksFSReadOnlyAccessA3d = 0x8000
    """ Файл компонента (a3d) имеет доступ “Только чтение” """
    ksFSUncuttable        = 0x10000
    """ Неразрезаемый компонент """
    ksFSUpdateNeeded      = 0x100000
    """ Необходимость обновления """
    ksFSBrokenLink        = 0x200000
    """ Разрыв связи копии геометрии с источником """


class ksFacetCullingMode:  # ksfacetcullingmode.html
    """ ## ksFacetCullingMode - Режим фильтрации отображаемых граней внешнего объекта """
    ksFSMNone  = 0
    """ Отображается всё (не фильтруется) """
    ksFSMFront = 1
    """ Отбрасывается передняя грань """
    ksFSMBack  = 2
    """ Отбрасывается задняя грань """
    ksFSMAll   = 3
    """ Ничего не отображается """


class ksFileNameMakeModeEnum:  # ksfilenamemakemodeenum.html
    """ ## ksFileNameMakeModeEnum - Способ форматирования имени файла при первом сохранении """
    ksFileNameMakeByType                = 0
    """ Тип документа """
    ksFileNameMakeByDessignation        = 1
    """ Обозначение """
    ksFileNameMakeByName                = 2
    """ Наименование """
    ksFileNameMakeByDessignationAndName = 3
    """ Обозначение + Наименование """
    ksFileNameMakeByNameAndDessignation = 4
    """ Наименование + Обозначение """


class ksFilletBuildingTypeEnum:  # ksfilletbuildingtypeenum.html
    """ ## ksFilletBuildingTypeEnum - Типы построения скругления """
    ksFilletCircleArc   = 0
    """ Дугой окружности """
    ksFilletEllipseArc  = 1
    """ Дугой эллипса """
    ksFilletCoefficient = 2
    """ С коэффициентом (0 < K < 1) """
    ksFilletHord        = 3
    """ С постоянной хордой """


class ksFilletOffsetModeEnum:  # ksfilletoffsetmodeenum.html
    """ ## ksFilletOffsetModeEnum - Способ расчета смещения для точек останова скругления """
    ksFilletOffsetByPersent = 0
    """ В процентах от длины кривой. """
    ksFilletOffsetByLength  = 1
    """ По длине сегмента """
    ksFilletOffsetByAngle   = 2
    """ По центральному углу дуги """


class ksFindObjectsTypeEnum:  # ksfindobjectstypeenum.html
    """ ## ksFindObjectsTypeEnum - Тип поиска объектов """
    ksFindObjByType     = -1
    """ Объект заданного типа """
    ksFindAll           = 0
    """ Любые объекты """
    ksFindAnyCurve      = 1
    """ Любая кривая или прямая """
    ksFindCircleAnalog  = 4
    """ Дуга или окружность """
    ksFindtTimmedCurve  = 8
    """ Кривая, имеющая граничные точки """
    ksFindEllipseAnalog = 13
    """ Эллипc или дуга эллипса. """
    ksFindHatchBoundary = 15
    """ Кривые, подходящие для границы штриховки. (Дополнительно проверяется стиль кривых) """


class ksFindObjectParametersNotifyEnum:  # ksfindobjectparametersnotifyenum.html
    """ ## ksFindObjectParametersNotifyEnum - События функции поиска объектов """
    ksFOPFilterObjectr = 1
    """ Фильтрация объетов """


class ksGabaritBuildingTypeEnum:  # ksgabaritbuildingtypeenum.html
    """ ## ksGabaritBuildingTypeEnum - Способ задания габаритов """
    ksGabaritByBorderPoints    = 0
    """ По двум вершинам """
    ksGabaritByCenterAndBorder = 1
    """ По центру и вершине """


class ksHatchStyleEnum:  # kshatchstyleenum.html
    """ ## ksHatchStyleEnum - Системные стили штриховки """
    ksHatchMetal                   = 0
    """ Mеталл """
    ksHatchNonMetal                = 1
    """ Не металл """
    ksHatchTimber                  = 2
    """ Дерево """
    ksHatchNaturalStone            = 3
    """ Камень естественный """
    ksHatchCeramics                = 4
    """ Керамика """
    ksHatchConcrete                = 5
    """ Бетон """
    ksHatchGlass                   = 6
    """ Стекло """
    ksHatchLiquid                  = 7
    """ Жидкость """
    ksHatchNaturallyGround         = 8
    """ Естественный грунт """
    ksHatchSpreadGround            = 9
    """ Насыпной грунт """
    ksHatchArtificialStone         = 10
    """ Камень искусственный """
    ksHatchReinforcedConcrete      = 11
    """ Железобетон """
    ksHatchTenseReinforcedConcrete = 12
    """ Напряженный железобетон """
    ksHatchLongitudalTimber        = 13
    """ Дерево в продольном сечении """
    ksHatchSand                    = 14
    """ Песок """


class ksHeightDimTypeEnum:  # ksheightdimtypeenum.html
    """ ## ksHeightDimTypeEnum - Тип размеров высоты """
    ksHDFrontView     = 0
    """ Для вида спереди или разреза, с полкой и стрелкой, возможна выносная линия. """
    ksHDTopView       = 1
    """ Для вида сверху без линии-выноски """
    ksHDTopViewLeader = 2
    """ Для вида сверху с линией-выноской """


class ksHoleCutTypeEnum:  # ksholecuttypeenum.html
    """ ## ksHoleCutTypeEnum – Тип построения отверстия и выреза """
    ksHoleCutByWidth     = 0
    """ По толщине """
    ksHoleCutByDepth     = 1
    """ На глубину """
    ksHoleCutUpToSurface = 2
    """ До грани """


class ksHoleTypeEnum:  # ksholetypeenum.html
    """ ## ksHoleTypeEnum - Тип отверстия """
    ksHTBase           = 0
    """ Простое """
    ksHTCounterbore    = 1
    """ С цековкой """
    ksHTCountersinking = 2
    """ С зенковкой """
    ksHTCounterdrill   = 3
    """ С цековкой и зенковкой """
    ksHTConic          = 4
    """ Коническое. """
    ksHTLfrLibrary     = 5
    """ Отверстие из библиотеки """


class ksHyperLinkTypeEnum:  # kshyperlinktypeenum.html
    """ ## ksHyperLinkTypeEnum - Тип гиперссылки """
    ksHLUnknown = 0
    """ Неизвестный """
    ksHLFile    = 1
    """ Ссылка на файл или web-страницу """
    ksHLObject  = 2
    """ Ссылка на объект """
    ksHLMail    = 3
    """ Адрес электронной почты """


class ksJalousieBuildingTypeEnum:  # ksjalousiebuildingtypeenum.html
    """ ## ksJalousieBuildingTypeEnum - Способ построения жалюзи """
    ksJalousieExtract = 0
    """ Вытяжка """
    ksJalousieTrim    = 1
    """ Подрезка """


class ksJalousieFormEndEnum:  # ksjalousieformendenum.html
    """ ## ksJalousieFormEndEnum - Форма торца жалюзи """
    ksJalousieTangent = 0
    """ По направлению """
    ksJalousieNormal  = 1
    """ По нормали к толщине """


class ksJalousieHeightTypeEnum:  # ksjalousieheighttypeenum.html
    """ ## ksJalousieHeightTypeEnum - Способ задания высоты жалюзи """
    ksJalousieAllHeight      = 0
    """ Полная """
    ksJalousieUpToFaceHeight = 1
    """ От грани """
    ksJalousieSlotHeight     = 2
    """ Высота прорези """


class ksInsertionTypeEnum:  # ksinsertiontypeenum.html
    """ ## ksInsertionTypeEnum - Тип вставки фрагмента или вида """
    ksTUnknown           = -1
    """ Неизвестный """
    ksTBodyFragment      = 0
    """ Вставка внешнего фрагмента. Взять в документ """
    ksTReferenceFragment = 1
    """ Вставка внешнего фрагмента. Внешней ссылкой """
    ksTLocalFragment     = 3
    """ Вставка локального фрагмента """
    ksTBodyView          = 4
    """ Вставка вида другого чертежа. Взять в документ """
    ksTReferenceView     = 5
    """ Вставка вида другого чертежа. Внешней ссылкой """


class ksKOMPASConverterEnum:  # kskompasconverterenum.html
    """ ## ksKOMPASConverterEnum - Типы внутренних конвертеров КОМПАС 3D """
    ksConverterToRaster  = 0
    """ Конвертация в растровый формат """
    ksConverterToSAT     = 1
    """ Конвертация в формат SAT """
    ksConverterToXT      = 2
    """ Конвертация в формат XT """
    ksConverterToSTEP    = 3
    """ Конвертация в формат STEP """
    ksConverterToIGES    = 4
    """ Конвертация в формат IGES """
    ksConverterToVRML    = 5
    """ Конвертация в формат VRML """
    ksConverterToSTL     = 6
    """ Конвертация в формат STL """
    ksConverterToJT      = 8
    """ Конвертация в формат JT """
    ksConverterFromSAT   = -1
    """ Конвертация из формата SAT. Для открытия документов """
    ksConverterFromXT    = -2
    """ Конвертация из формата XTT. Для открытия документов """
    ksConverterFromSTEP  = -3
    """ Конвертация из формата STEP. Для открытия документов """
    ksConverterFromIGES  = -4
    """ Конвертация из формата IGES. Для открытия документов """
    ksConverterFromSTL   = -5
    """ Конвертация из формата STL. Для открытия документов """
    ksConverterFromSAT   = -6
    """ Конвертация из формата SAT. Для открытия документов """
    ksConverterFromC3D   = -7
    """ Конвертация из формата C3D. Для открытия документов """
    ksConverterFromJT    = -8
    """ Конвертация из формата JT. Для открытия документов """
    ksConverterFromOBJ   = -9
    """ Конвертация из формата OBJ. Для открытия документов """
    ksConverterFromNX    = 100
    """ Формат NX. Для открытия документов """
    ksConverterFromCREO  = 101
    """ ФорматCREO. Для открытия документов """
    ksConverterFromSW    = 102
    """ Формат SW. Для открытия документов """
    ksConverterFromINV   = 103
    """ Формат INV. Для открытия документов """
    ksConverterFromCATIA = 104
    """ Формат CATIA. Для открытия документов """
    ksConverterFromSE    = 105
    """ Формат SE. Для открытия документов """


class ksKompasModuleEnum:  # kskompasmoduleenum.html
    """ ## ksKompasModuleEnum - Модули Компас """
    ksKompasModule2D = 1
    """ Модуль 2D """
    ksKompasModule3D = 2
    """ Модуль 3D """
    ksKompasPrint    = 100
    """ Модуль печати """
    ksKompasExport   = 101
    """ Модуль экспорта """


class ksKompasVariantEnum:  # kskompasvariantenum.html
    """ ## ksKompasVariantEnum - Константы вариантов реализаций Компас """
    ksKompasPro       = 0
    """ КОМПАС. """
    ksKompasHome      = 1
    """ КОМПАС-Home. """
    ksKompasViewer    = 2
    """ КОМПАС-Viewer. """
    ksKompasSpds      = 4
    """ КОМПАС-SPDS. """
    ksKompasGraphic   = 256
    """ КОМПАС-График. """
    ksKompasInvisible = 512
    """ КОМПАС-Invisible. """
    ksKompasLatin     = 1024
    """ КОМПАС - иностранная версия. """
    ksKompasConsumer  = 4096
    """ КОМПАС-Consumer. """
    ksKompasStudy     = 8192
    """ КОМПАС-Study. """


class ksLawTypeEnum:  # kslawtypeenum.html
    """ ## ksLawTypeEnum - Типы законов """
    ksTLawConst        = 0
    """ Константный """
    ksTLawLinear       = 1
    """ Линейный """
    ksTLawCube         = 2
    """ Кубический """
    ksTLawByExpression = 3
    """ По выражению """


class ksLeaderSignEnum:  # ksleadersignenum.html
    """ ## ksLeaderSignEnum - Тип значка для линии-выноски """
    ksLSignNone         = 0
    """ Без знака """
    ksLGlueSign         = 1
    """ Знак склеивания """
    ksLSolderingSign    = 2
    """ Знак пайки """
    ksLSewingSign       = 3
    """ Знак сшивания """
    ksLCrampSign        = 4
    """ Знак соединения внахлестку металлическими скобками """
    ksLcornerCrampSign  = 5
    """ Знак углового соединения металлическими скобами """
    ksLMontageJointSign = 6
    """ Знак монтажного шва """


class ksLengthBuildingTypeEnum:  # kslengthbuildingtypeenum.html
    """ ## ksLengthBuildingTypeEnum - Способ расчета длины продолжения сгиба листового тела """
    ksLBDistance  = 0
    """ На расстояние """
    ksLBToVertex  = 2
    """ До вершины """
    ksLBToSurface = 3
    """ До поверхности """


class ksLengthUnitEnum:  # kslengthunitenum.html
    """ ## ksLengthUnitEnum – Единицы измерения длины """
    ksLUMillimetres = 0
    """ Миллиметры """
    ksLUCentimetres = 1
    """ Сантиметры """
    ksLUnDecimetres = 2
    """ Дециметры """
    ksLUnMetres     = 3
    """ Метры """
    ksLUKilometres  = 4
    """ Километры """


class ksLengthUnitsEnum:  # kslengthunitsenum.html
    """ ## ksLengthUnitsEnum – Единицы измерения длины """
    ksLUnSM       = 0
    """ Сантиметры """
    ksLUnMM       = 1
    """ Миллиметры """
    ksLUnDM       = 2
    """ Дециметры """
    ksLUnM        = 3
    """ Метры """
    ksLUnDocument = 4
    """ Настройки документа """


class ksLibraryStyleEnum:  # kslibrarystyleenum.html
    """ ## ksLibraryStyleEnum - Стили отображения прикладных библиотек """
    ksLibraryStyleUnknown   = 0
    """ Неизвестный стиль """
    ksLibraryStyleMenu      = 1
    """ Отображение в виде меню """
    ksLibraryStyleDialog    = 2
    """ Отображение в виде диалога """
    ksLibraryStyleWindow    = 3
    """ Отображение в виде специального окна """
    ksLibraryStyleBar       = 4
    """ Отображение в виде панели инструментов """
    ksLibraryStyleInvisible = 5
    """ Невидимый режим """


class ksLibraryTypeEnum:  # kslibrarytypeenum.html
    """ ## ksLibraryTypeEnum - Типы библиотек """
    ksLibraryUnknown   = 0
    """ Неизвестный тип. """
    ksLibraryProcedure = 1
    """ Прикладная библиотека. """
    ksLibraryFragment  = 2
    """ Библиотека фрагментов. """
    ksLibraryModel     = 3
    """ Библиотека моделей. """
    ksLibraryDocuments = 4
    """ Универсальная библиотека документов """


class ksLineDimensionOrientationEnum:  # kslinedimensionorientationenum.html
    """ ## ksLineDimensionOrientationEnum - Тип ориентации линейного размера """
    ksLinDParallel   = 0
    """ Параллельно объекту """
    ksLinDHorizontal = 1
    """ Горизонтально """
    ksLinDVertical   = 2
    """ Вертикально """


class ksLinearPatternBuildingTypeEnum:  # kslinearpatternbuildingtypeenum.html
    """ ## ksLinearPatternBuildingTypeEnum - Способ построения массива по сетке """
    ksLPSaveAll            = 0
    """ Оставлять копии внутри сетки """
    ksLPSaveAlongPerimeter = 1
    """ Оставлять копии только по периметру сетки """
    ksLPSaveAlongAxially   = 2
    """ Оставлять копии только по осям сетки """
    ksLPChessOrderByAxis1  = 3
    """ Шахматный порядок - сдвиг вдоль первой оси """
    ksLPChessOrderByAxis2  = 4
    """ Шахматный порядок - сдвиг вдоль второй оси """


class ksLineSegment3DTypeEnum:  # kslinesegment3dtypeenum.html
    """ ## ksLineSegment3DTypeEnum - Тип построения отрезка 3D """
    ksLSTTwoPoints        = 0
    """ По 2 точкам """
    ksLSTPointLenghtAngle = 1
    """ По точке, длине и углу наклона """


class ksLoadStateEnum:  # ksloadstateenum.html
    """
    ## ksLoadStateEnum - Тип загрузки компонента

    Компонент загружен полностью - загружена триангуляция (для отрисовки), загружена модель. Можно редактировать.

    Компонент не загружен - не отображается в окне документа. Редактировать нельзя.

    Компонент загружен частично - загружена только триангуляция (для отрисовки). Редактировать нельзя.

    Тип загрузки относится к вставкам компонентов в сборке 3D.
    """
    ksLUnknown    = -1
    """ Неопределен """
    ksLCompletely = 0
    """ Загружен полностью """
    ksLUnload     = 1
    """ Пустой, не загружен """
    ksLTriangles  = 2
    """ Упрощенный. Триангуляция """
    ksLPartially  = 3
    """ Частичная загрузка """
    ksLGabarit    = 4
    """ Габарит """


class ksLoftBuildingType:  # ksloftbuildingtype.html
    """ ## ksLoftBuildingType - Способы построения элемента по сечениям у крайних сечений """
    ksLoftAuto     = 0
    """ Автоматически """
    ksLoftByNormal = 1
    """ По нормали """
    ksLoftByObject = 2
    """ По объекту """
    ksLoftCupola   = 3
    """ Купол """


class ksManipulatorTypeEnum:  # ksmanipulatortypeenum.html
    """ ## ksManipulatorTypeEnum - Способ разбиения зоны """
    ksPlacement3DManipulator = 1
    """ Манипулятор системы координат """
    ksEditDoubleManipulator  = 2
    """ Манипулятор - редактор вещественного значения """


class ksManipulatorPrimitiveEnum:  # ksmanipulatorprimitiveenum.html
    """ ## ksManipulatorPrimitiveEnum - Тип примитива манипулятора """
    ksMPNone     = 0
    """ Неизвестный тип """
    ksMPAxisX    = 1
    """ Ось X """
    ksMPAxisY    = 2
    """ Ось Y """
    ksMPAxisZ    = 3
    """ Ось Z """
    ksMPPlaceXOY = 4
    """ Плоскость XOY """
    ksMPPlaceXOZ = 5
    """ Плоскость XOZ """
    ksMPPlaceYOZ = 6
    """ Плоскость YOZ """
    ksMPConturXY = 7
    """ Граница плоскости XOY """
    ksMPConturXZ = 8
    """ Граница плоскости XOZ """
    ksMPConturYZ = 9
    """ Граница плоскости YOZ. """
    ksMPTextX    = 10
    """ Текст X """
    ksMPTextY    = 11
    """ Текст Y. """
    ksMPTextZ    = 12
    """ Текст Z. """
    ksMPOriginal = 13
    """ Начало координат """


class ksManipulatorModeEnum:  # ksmanipulatormodeenum.html
    """ ## ksManipulatorModeEnum - Режимы работы манипулятора """
    ksManipulatorModeDefault         = 1
    """ По умолчанию """
    ksManipulatorModeNotHandleEditor = 2
    """ Запрет ручного редактирования """


class ksMateConstraintAlignmentEnum:  # ksmateconstraintalignmentenum.html
    """ ## ksMateConstraintAlignmentEnum - Варианты выравнивания направлений для сопряжений """
    ksMCAlignmentOpposite   = -1
    """ Противонаправленные """
    ksMCAlignmentClosest    = 0
    """ Ориентация согласно ближайшего решения """
    ksMCAlignmentCooriented = 1
    """ Сонаправленные, с одинаковой ориентацией """
    ksMCAlignmentUnknown    = 2
    """ Нет определенной ориентации """
    ksMCAlignment_1         = 3
    """ Дополнительный вариант 1 """
    ksMCAlignment_2         = 4
    """ Дополнительный вариант 2 """
    ksMCAlignment_3         = 5
    """ Дополнительный вариант 3 """
    ksMCReverse_1           = 6
    """ Противонаправленные. Дополнительный вариант 1 """
    ksMCReverse_2           = 7
    """ Противонаправленные. Дополнительный вариант 2 """
    ksMCReverse_3           = 8
    """ Противонаправленные. Дополнительный вариант 3 """


class ksMarkInsideFormEnum:  # ksmarkinsideformenum.html
    """ ## ksMarkInsideFormEnum – тип формы для марки (без линии-выноски) """
    ksMFormEmpty                      = 0
    """ Без формы. """
    ksMFormCircle                     = 1
    """ Окружность. """
    ksMFormRectangle                  = 2
    """ Прямоугольник """
    ksMFormSquare                     = 3
    """ Квадрат """
    ksMFormRhomb1                     = 4
    """ Ромб 1 """
    ksMFormRhomb2                     = 5
    """ Ромб 2 """
    ksMFormHexagon                    = 6
    """ Шестиугольник """
    ksMFormTriangle1                  = 7
    """ Треугольник 1 """
    ksMFormTriangle2                  = 8
    """ Треугольник 2 """
    ksMFormChamferedRectangle         = 9
    """ Скругленный прямоугольник """
    ksMFormCircleWidthVerticalDelimer = 10
    """ Окружность с вертикальным разделителем """
    ksMFormDoubleCircle               = 11
    """ Двойная окружность """


class ksMarkNodeEnum:  # ksmarknodeenum.html
    """ ## ksMarkNodeEnum – Тип узла марки """
    ksMarkCircle    = 0
    """ Окружность """
    ksMarkRefCircle = 1
    """ Указатель ориентации оси c окружностью """
    ksMarkText      = 2
    """ Текст """


class ksMarkOnLinePosTypeEnum:  # ksmarkonlinepostypeenum.html
    """ ## ksMarkOnLinePosTypeEnum – Положение марки относительно линии """
    ksMTextAboveLine = 0
    """ Текст над линией """
    ksMTextOnLine    = 1
    """ Текст на линии """
    ksMTextUnderLine = 2
    """ Текст под линией """


class ksMassSettingModeEnum:  # ksmasssettingmodeenum.html
    """ ## ksMassSettingModeEnum – Варианты задания МЦХ """
    ksCalculateParam = 0
    """ Расчет параметров """
    ksManualMass     = 1
    """ Ручное задание массы """


class ksMassUnitsEnum:  # ksmassunitsenum.html
    """ ## ksMassUnitsEnum – Единицы измерения массы """
    ksMUnGR       = 0
    """ Граммы """
    ksMUnKG       = 1
    """ Килограммы """
    ksMUnT        = 2
    """ Тонны """
    ksMUnDocument = 4
    """ Настройки документа """


class ksMaterialPropertyTypeEnum:  # ksmaterialpropertytypeenum.html
    """ ## ksMaterialPropertyTypeEnum - Тип события выбора материала """
    ksMPNewPartDocumentSettings = 1
    """ Вызов из настроек новых документов для настроек детали """


class ksMateTangentTypeEnum:  # ksmatetangenttypeenum.html
    """ ## ksMateTangentTypeEnum - Вид касания для сопряжения касание """
    ksMTangentUnknown          = 0
    """ Неопределено """
    ksMTangentByPoint          = 1
    """ Касание в общем случае (контакт точкой) """
    ksMTangentByGeneratrixLine = 2
    """ Касание по образующей прямой (например два цилиндра с параллельными осями) """
    ksMTangentByCircle         = 3
    """ Касание по окружности (например сфера в конусе) """


class ksMateMotionTypeEnum:  # ksmatemotiontypeenum.html
    """ ## ksMateMotionTypeEnum - Тип движения компонента для механического сопряжения """
    ksMMotionUnknown  = 0
    """ Неопределено """
    ksMMotionLinear   = 1
    """ Линейное перемещение """
    ksMMotionRotation = 2
    """ Вращение """


class ksMathCurve2DTypeEnum:  # ksmathcurve2dtypeenum-----2d-.html
    """ ## ksMathCurve2DTypeEnum - Тип математической 2D кривой """
    ksUndefinetCurveType = 0
    """ Неизвестно """
    ksLine               = 202
    """ Прямая """
    ksLineSegment        = 203
    """ Отрезок """
    ksArc                = 204
    """ Окружность или дуга """
    ksCosinusoid         = 205
    """ Кривая-косинусоида. Волнистая линия """
    ksPolyCurve          = 206
    """ Сплайновая кривая """
    ksPolyLine           = 207
    """ Полилиния """
    ksBezier             = 208
    """ Безье-сплайн """
    ksHermit             = 209
    """ Составной кубический сплайн Эрмита """
    ksNurbs              = 210
    """ NURBS кривая """
    ksCubicSpline        = 211
    """ Кубический сплайн """
    ksTrimmedCurve       = 212
    """ Усеченная кривая """
    ksOffsetCurve        = 213
    """ Эквидистантная продленная кривая """
    ksReparamCurve       = 214
    """ Репараметризованная кривая """
    ksPointCurve         = 215
    """ Кривая - точка """
    ksCharacterCurve     = 216
    """ Кривая, координатные функции которой заданы в символьном виде """
    ksProjCurve          = 217
    """ Проекционная кривая """
    ksSweptImageCurve    = 218
    """ Образ трехмерной кривой на поверхности при движении по направляющей """
    ksTransformedCurve   = 219
    """ Трансформированная кривая """
    ksConeBendedCurve    = 220
    """ Кривая в параметрической области конуса, соответствующая кривой в параметрической области плоскости при коническом сгибе """
    ksConeUnbendedCurve  = 221
    """ Кривая в параметрической области плоскости, соответствующая кривой в параметрической области конуса при коническом сгибе """
    ksContour            = 301
    """ Контур """
    ksContourWithBreaks  = 302
    """ Контур с разрывами """


class ksMathCurve3DTypeEnum:  # ksmathcurve3dtypeenum.html
    """ ## ksMathCurve3DTypeEnum - Тип математической кривой в трехмерном пространстве """
    ks3DCurve                  = 0
    """ Кривая """
    ksLine3D                   = 1
    """ Прямая """
    ksLineSegment3D            = 2
    """ Отрезок прямой """
    ksArc3D                    = 3
    """ Окружность, эллипс, дуга """
    ksSpiral                   = 4
    """ Спираль """
    ksConeSpiral               = 5
    """ Коническая спираль """
    ksCurveSpiral              = 6
    """ Спираль по образующей кривой """
    ksCrookedSpiral            = 7
    """ Спираль по направляющей кривой """
    ksPolyCurve3D              = 8
    """ Кривая, построенная по точкам """
    ksPolyline3D               = 9
    """ Полилиния """
    ksNurbs3D                  = 10
    """ NURBS кривая """
    ksBezier3D                 = 11
    """ Кривая Безье """
    ksHermit3D                 = 12
    """ Составной кубический сплайн Эрмита """
    ksCubicSpline3D            = 13
    """ Кубический сплайн """
    ksPlaneCurve               = 14
    """ Плоская кривая в пространстве """
    ksOffsetCurve3D            = 15
    """ Эквидистантная кривая """
    ksTrimmedCurve3D           = 16
    """ Усеченная кривая """
    ksReparamCurve3D           = 17
    """ Репараметризованная кривая """
    ksBridgeCurve3D            = 18
    """ Кривая-мостик, соединяющая две кривые """
    ksCharacterCurve3D         = 19
    """ Кривая, координатные функции которой заданы в символьном виде """
    ksContourOnSurface         = 20
    """ Контур на поверхности """
    ksContourOnPlane           = 21
    """ Контур на плоскости """
    ksSurfaceCurve             = 22
    """ Кривая на поверхности """
    ksSilhouetteCurve          = 23
    """ Силуэтная кривая """
    ksSurfaceIntersectionCurve = 24
    """ Кривая пересечения поверхностей """
    ksBSpline                  = 25
    """ В-сплайн """
    ksContour3D                = 26
    """ Контур """


class ksMathSurface3DTypeEnum:  # ksmathsurface3dtypeenum.html
    """ ## ksMathSurface3DTypeEnum - Тип математической поверхности в трехмерном пространстве """
    ks3DSurface                = 0
    """ Поверхность """
    ksElementarySurface        = 1
    """ Элементарная поверхность """
    ksPlane                    = 2
    """ Плоскость """
    ksConeSurface              = 3
    """ Коническая поверхность """
    ksCylinderSurface          = 4
    """ Цилиндрическая поверхность """
    ksSphereSurface            = 5
    """ Сфера """
    ksTorusSurface             = 6
    """ Тор """
    ksSweptSurface             = 7
    """ Поверхность движения """
    ksExtrusionSurface         = 8
    """ Поверхность перемещения """
    ksRevolutionSurface        = 9
    """ Поверхность вращения """
    ksEvolutionSurface         = 10
    """ Кинематическая поверхность """
    ksExactionSurface          = 11
    """ Кинематическая поверхность с поворотными торцами """
    ksExpansionSurface         = 12
    """ Плоскопараллельная поверхность """
    ksElevationSurface         = 13
    """ Поверхность по сечениям с направляющей """
    ksSpiralSurface            = 14
    """ Спиральная поверхность """
    ksRuledSurface             = 15
    """ Линейчатая поверхность """
    ksSectorSurface            = 16
    """ Секториальная поверхность """
    ksPolySurface              = 17
    """ Поверхность, определяемая точками """
    ksHermitSurface            = 18
    """ Hermit - поверхность, определяемая точками """
    ksSplineSurface            = 19
    """ NURBS поверхность, определяемая точками """
    ksGridSurface              = 20
    """ Поверхность, определяемая точками """
    ksTriBezierSurface         = 21
    """ Треугольная Bezier поверхность, определяемая точками """
    ksTriSplineSurface         = 22
    """ Треугольная NURBS поверхность, определяемая точками """
    ksOffsetSurface            = 23
    """ Эквидистантная поверхность """
    ksDeformedSurface          = 24
    """ Деформированная поверхность """
    ksNurbsSurface             = 25
    """ NURВS поверхность, определяемая кривыми """
    ksCornerSurface            = 26
    """ Поверхность по трем кривым """
    ksCoverSurface             = 27
    """ Поверхность по четырем кривым """
    ksCoonsPatchSurface        = 28
    """ Бикубическая поверхность Кунса по четырем кривым """
    ksMeshSurface              = 29
    """ Поверхность на сетке кривых """
    ksLoftedSurface            = 30
    """ Поверхность Эрмита, определяемая кривыми """
    ksSmoothSurface            = 31
    """ Поверхность coпряжения """
    ksChamferSurface           = 32
    """ Поверхность фаски """
    ksFilletSurface            = 33
    """ Поверхность cкругления """
    ksChannelSurface           = 34
    """ Поверхность cкругления с переменным радиусом """
    ksJoinSurface              = 35
    """ Поверхность соединения """
    ksCurveBoundedSurface      = 36
    """ Поверхность, усеченная кривыми (контурами) на поверхности """
    ksBendedUnbendedSurface    = 37
    """ Поверхность, полученная сгибом/разгибом """
    ksCylindricBendedSurface   = 38
    """ Поверхность, полученная цилиндрическим сгибом """
    ksCylindricUnbendedSurface = 39
    """ Поверхность, полученная цилиндрическим разгибом """
    ksConicBendedSurface       = 40
    """ Поверхность, полученная коническим сгибом """
    ksConicUnbendedSurface     = 41
    """ Поверхность, полученная коническим разгибом """
    ksExplorationSurface       = 42
    """ Поверхность заметания с масштабированием и поворотом образующей кривой """
    ksFreeSurface              = 200
    """ Тип для поверхностей, созданных пользователем """


class ksMeasureResultEnum:  # ksmeasureresultenum.html
    """ ## ksMeasureResultEnum - Результат измерения расстояния и угла между поверхностями """
    ksMResUnknown              = 0
    """ Не определен """
    ksMResAxisAxisCoaxial      = 1
    """ Оси совпадают """
    ksMResAxisAxisParallel     = 2
    """ Оси параллельны """
    ksMResAxisAxisIntersect    = 3
    """ Оси пересекаются """
    ksMResAxisAxisDistant      = 4
    """ Оси на расстоянии """
    ksMResAxisSurfColinear     = 5
    """ Ось лежит на поверхности """
    ksMResAxisSurfParallel     = 6
    """ Ось параллельна поверхности """
    ksMResAxisSurfIntersect    = 7
    """ Ось пересекает поверхность """
    ksMResAxisSurfDistant      = 8
    """ Ось на расстоянии от поверхности """
    ksMResSurfSurfColinear     = 9
    """ Одна поверхность лежит на другой """
    ksMResSurfSurfParallel     = 10
    """ Поверхности параллельны """
    ksMResSurfSurfIntersecting = 11
    """ Поверхности пересекаются """


class ksMeshAroundPointTypeEnum:  # ksmesharoundpointtypeenum.html
    """ ## ksMeshAroundPointTypeEnum - Тип сетки, построенной вокруг точки """
    ksMALinear    = 0
    """ Прямоугольная сетка (метрический шаг) """
    ksMAUVLinear  = 1
    """ Прямоугольная сетка (параметрический шаг) """
    ksMACircular  = 2
    """ Концентрическая сетка """
    ksMAHexagonal = 3
    """ Гексогональная сетка """


class ksMeshPointsSurfaceBuildingTypeEnum:  # ksmeshpointssurfacebuildingtypeenum.html
    """ ## ksMeshPointsSurfaceBuildingTypeEnum - Тип поверхности по сети точек """
    ksMPByPoints = 0
    """ Сплайновая поверхность по точкам """
    ksMPByPole   = 1
    """ Сплайновая поверхность по полюсам """


class ksMetaSplineApproximationTypeEnum:  # ksmetasplineapproximationtypeenum.html
    """ ## ksMetaSplineApproximationTypeEnum - Тип аппроксимации метасплайна """
    ksMetaSplineApproximationBezier  = 0
    """ Безье """
    ksMetaSplineApproximationBSpline = 1
    """ B-сплайн """


class ksMetaSplineBuildingTypeEnum:  # ksmetasplinebuildingtypeenum.html
    """ ## ksMetaSplineBuildingTypeEnum - Способ построения метасплайна """
    ksMetaSplineByPoints  = 0
    """ По точкам """
    ksMetaSplineByTangent = 1
    """ С касанием """


class ksMetaSplineDensityDegreeEnum:  # ksmetasplinedensitydegreeenum.html
    """ ## ksMetaSplineDensityDegreeEnum - Уплотнение метасплайна """
    ksMetaSplineDensityDegreeNo     = 0
    """ Без уплотнения """
    ksMetaSplineDensityDegreeSingle = 1
    """ Однократно """
    ksMetaSplineDensityDegreeDouble = 2
    """ Двукратно """


class ksMetaSplineSmoothingEnum:  # ksmetasplinesmoothingenum.html
    """ ## ksMetaSplineSmoothingEnum - Сглаживание метасплайна """
    ksMetaSplineSmoothingNo         = 0
    """ Сглаживание отключено """
    ksMetaSplineSmoothingYes        = 1
    """ Сглаживание включено """
    ksMetaSplineSmoothingFixCorners = 2
    """ Сглаживание острых углов """


class ksMlEndLimiterEnum:  # ksmlendlimiterenum.html
    """ ## ksMlEndLimiterEnum - Типы ограничений на концах мультилинии """
    ksMEndUnknown  = 0
    """ Без ограничения """
    ksMEndLine     = 1
    """ Прямолинейный """
    ksMEndArc      = 2
    """ Дуговой """
    ksMEndPolyline = 3
    """ Ломаный """


class ksMlVertexLimiterEnum:  # ksmlvertexlimiterenum.html
    """ ## ksMlVertexLimiterEnum - Типы ограничений в вершинах мультилинии """
    ksMVeUnknown = 0
    """ Без ограничения """
    ksMVeArc     = 1
    """ Дуговой """
    ksMVeAngle   = 2
    """ Угловой стык """
    ksMVeTangent = 3
    """ Касательный стык """


class ksMlVertexTrackingEnum:  # ksmlvertextrackingenum.html
    """ ## ksMlVertexTrackingEnum - Типы обхода вершин мультилинии """
    ksMTrShear      = 0
    """ Обход срезом """
    ksMTrFillet     = 1
    """ Обход скруглением """
    ksMTrEquaFillet = 2
    """ Обход скруглением с одинаковым радиусом """


class ksModelDrawingElementsEnum:  # ksmodeldrawingelementsenum.html
    """ ## ksModelDrawingElementsEnum - Возможные элементы отрисовки модели """
    ksModelDrawingElementNone       = 0x0000
    """ Пусто """
    ksModelDrawingElementBackground = 0x0001
    """ Фоновая подложка """
    ksModelDrawingElementCompBodies = 0x0010,
    """ Тела компонента """
    ksModelDrawingElementCompObjs   = 0x0020
    """ Объекты компонента """
    ksModelDrawingElementAuxObjs    = 0x0100
    """ Внешние объекты """
    ksModelDrawingElementNotifyLibs = 0x0200
    """ Библиотеки на подписке """
    ksModelDrawingElementEditor     = 0x1000
    """ Элементы редактора, включая эскиз и фантомы """
    ksModelDrawingElementWidgets    = 0x2000
    """ Элементы управления, оконная сетка и пр. """
    ksModelDrawingElementMeshCutter = 0x4000
    """ Сечение модели """
    ksModelDrawingElementAll        = 0xffff
    """ Все элементы сразу """


class ksModelRenderTypeEnum:  # ksmodelrendertypeenum.html
    """ ## ksModelRenderTypeEnum - Вариант отрисовки """
    ksModelRenderNone      = -1
    """ Без аппаратного ускорения """
    ksModelRenderAuto      = 0
    """ Автоматическое определение """
    ksModelRenderPerfected = 1
    """ Улучшенный. Триангуляция лежит на GPU. Минимальное число отрисовочных вызовов """
    ksModelRenderMedium    = 2
    """ Базовый. Триангуляция лежит на GPU. Группировка по телам """
    ksModelRenderLow       = 3
    """ Совместимый. Старая реализация. Минимальные требования к GPU """


class ksModelPerformanceLevelEnum:  # ksmodelperformancelevelenum.html
    """ ## ksModelPerformanceLevelEnum - Качество сглаживания """
    ksMPLDisabledAntialiasing = 0
    """ Без сглаживания """
    ksMPLLowAntialiasing      = 1
    """ Низкое качество сглаживания """
    ksMPLNormalAntialiasing   = 2
    """ Среднее качество сглаживания """
    ksMPLHightAntialiasing    = 3
    """ Высокое качество сглаживания """


class ksModelTransparencyTypeEnum:  # ksmodeltransparencytypeenum.html
    """ ## ksModelTransparencyTypeEnum - Прозрачность """
    ksModelTransparencyMesh      = 1
    """ Сетчатая прозрачность """
    ksModelTransparencyRealistic = 2
    """ Реалистичная прозрачность """


class ksModelObjectParamTypeEnum:  # ksmodelobjectparamtypeenum.html
    """ ## ksModelObjectParamTypeEnum - Тип параметров объекта """
    ksMOAllParam           = 0
    """ Параметры в системе координат ЛСК объекта """
    ksMOPartAllParam       = 1
    """ Параметры в системе координат детали """
    ksMOCurrentLSKAllParam = 2
    """ Параметры в системе текущей ЛСК """


class ksMultiPageOutputEnum:  # ksmultipageoutputenum.html
    """ ## ksMultiPageOutputEnum - Многостраничный вывод """
    ksMultiPageOff = 0
    """ Сохранять листы в отдельных файлах """
    ksMultiPageOn  = 1
    """ Сохранять листы в одном файле """
    ksMultiPageOn2 = 2
    """ Сохранять листы одним изображением """


class ksMultiThicknessGroupTypeEnum:  # ksmultithicknessgrouptypeenum.html
    """ ## ksMultiThicknessGroupTypeEnum - Тип разнотолщинной группы """
    ksArbitraryThicknesses = 0
    """ Группы произвольных толщин """
    ksSetsThicknesses      = 1
    """ Группы наборов толщин """


class ksNewDocumentSettingsTypeEnum:  # ksnewdocumentsettingstypeenum.html
    """ ## ksNewDocumentSettingsTypeEnum - Тип настроек новых документов """
    ksNewPartDocumentSettings = 1
    """ Настройки новых документов для детали """


class ksNumericGroupTypeEnum:  # ksnumericgrouptypeenum.html
    """ ## ksNumericGroupTypeEnum - Тип группы нумерации. Тип номера """
    ksNumericGroupNumbers = 0
    """ 1, 2, 3, 4, 5... """
    ksNumericGroupSymbols = 1
    """ Заданные символы """


class ksNurbsByPointsAproximationTypeEnum:  # ksnurbsbypointsaproximationtypeenum.html
    """ ## ksNurbsByPointsAproximationTypeEnum - Способ вычисления шага аппроксимации для точек сплайна """
    ksNBPAproximationStepByCurvature = 0
    """ Вычисление шага аппроксимации с учетом радиуса кривизны """
    ksNBPAproximationStepByDeviation = 1
    """ Вычисление шага аппроксимации по угловой толерантности """


class ksNurbsByPointsBuildingTypeEnum:  # ksnurbsbypointsbuildingtypeenum.html
    """ ## ksNurbsByPointsBuildingTypeEnum - Способ формирования точек сплайна """
    ksNByPBTUndefined  = 0
    """ Неопределенный """
    ksNByPBLinear      = 1
    """ Линейный """
    ksNByPBChordLength = 2
    """ По длине хорды """
    ksNByPBCentripetal = 3
    """ Центростремительный """


class ksNurbsByPointsPointConstraintsEnum:  # ksnurbsbypointspointconstraintsenum.html
    """ ## ksNurbsByPointsPointConstraintsEnum - Вариант управления точкой сплайна """
    ksNByPBPCNone     = 0
    """ Нет """
    ksNByPBPCTangent  = 1
    """ Касательностью """
    ksNByPBPCSmoothG2 = 2
    """ Касательностью и кривизной """
    ksNByPBPCNormal   = 3
    """ Перпендикулярно """


class ksObjectsFilter3DEnum:  # ksobjectsfilter3denum.html
    """ ## ksObjectsFilter3DEnum - Способ фильтрации 3D объектов """
    ksFilterAll           = 0
    """ Фильтровать все """
    ksFilterFaces         = 1
    """ Фильтровать грани """
    ksFilterEdges         = 2
    """ Фильтровать ребра """
    ksFilterVertexs       = 3
    """ Фильтровать вершины """
    ksFilterCPlanes       = 4
    """ Фильтровать конструктивные плоскости """
    ksFilterCAxis         = 5
    """ Фильтровать конструктивные оси """
    ksFilterParts         = 6
    """ Фильтровать компоненты """
    ksFilterBodies        = 7
    """ Фильтровать тела """
    ksFilterSurfaces      = 8
    """ Фильтровать поверхности """
    ksFilterSketches      = 9
    """ Фильтровать эскизы """
    ksFilterCurves        = 10
    """ Фильтровать кривые """
    ksFilterCS            = 11
    """ Фильтровать системы координат """
    ksFilterControlPoints = 12
    """ Фильтровать контрольные и присоединительные точки """
    ksFilterPoints3D      = 13
    """ Фильтровать точки """
    ksFilterDesignations  = 14
    """ Фильтровать обозначения """
    ksFilterThread        = 15
    """ Фильтровать условные обозначения резьбы """


class ksObjectColorTypeEnum:  # ksobjectcolortypeenum.html
    """ ## ksObjectColorTypeEnum - Тип цвета """
    ksColorBw            = 0
    """ Черный """
    ksColorView          = 1
    """ Установленный для вида """
    ksColorLayer         = 2
    """ Установленный для слоя """
    ksColorObject        = 3
    """ Установленный для объекта """
    ksCurrentColorScheme = 4
    """ Установленный для объекта в текущей цветовой схеме """


class ksObjectConstraintsStateEnum:  # ksobjectconstraintsstateenum.html
    """ ## ksObjectConstraintsStateEnum - Параметрическое состояние объекта """
    ksObjectStateUnknown     = 0
    """ Обычный не параметризованный объект """
    ksObjectStateFullDefined = 1
    """ Полностью определенный объект """
    ksObjectStateOverDefined = 2
    """ Переопределённый объект(размер) """
    ksObjectStateInformative = 3
    """ Информационный объект(размер) """
    ksObjectWrongProjection  = 4
    """ Потерянная проекционная связь. """


class ksOperationResultEnum:  # ksoperationresultenum.html
    """ ## ksOperationResultEnum - Результат операции """
    ksOperationUnion     = 0
    """ Объединение """
    ksOperationNewBody   = 1
    """ Новое тело """
    ksOperationCut       = 2
    """ Вычитание """
    ksOperationIntersect = 3
    """ Пересечение """


class ksOffsetGapType:  # ksoffsetgaptype.html
    """ ## ksOffsetGapType - Типы смещений зазора """
    ksOGParametrU     = 0
    """ По параметру U """
    ksOGLength        = 1
    """ По длине """
    ksOGDraftPosition = 2
    """ Угол расположения """


class ksOrientationTypeEnum:  # ksorientationtypeenum.html
    """ ## ksOrientationTypeEnum - Тип ориентирования ЛСК """
    ksAxisOrientation = 0
    """ Направление осей """
    ksEulerCorners    = 1
    """ Система углов Эйлера """
    ksOrientByObject  = 2
    """ Ориентирование по объекту """


class ksOutputColorTypeEnum:  # ksoutputcolortypeenum.html
    """ ## ksOutputColorTypeEnum - Цвет вывода на печать """
    ksPJ_OCBlack    = 0
    """ В черных линиях """
    ksPJ_OCByView   = 1
    """ Цветом вида """
    ksPJ_OCByLayer  = 2
    """ Цветом слоя """
    ksPJ_OCByObject = 3
    """ Цветом объекта """


class ksParametersTypeEnum:  # ksparameterstypeenum.html
    """ ## ksParametersTypeEnum - Тип задания параметров сгибов """
    ksGeneral    = 0
    """ Общие параметры """
    ksIndividual = 1
    """ Индивидуальные параметры """


class ksPartAccessTypeEnum:  # kspartaccesstypeenum.html
    """ ## ksPartAccessTypeEnum - Тип доступа к компоненту """
    ksATUncertainty = -1
    """ Неопределенный """
    ksATEditable    = 0
    """ Редактирование """
    ksATReadOnly    = 1
    """ Только чтение """
    ksATDisable     = 2
    """ Доступ запрещен """


class ksPart7CollectionTypeEnum:  # kspart7collectiontypeenum.html
    """ ## ksPart7CollectionTypeEnum – Тип коллекции компонентов """
    ksAllParts    = 0
    """ Все компоненты (включая копии из операций копирования) """
    ksUniqueParts = 1
    """ Первые экземпляры вставок компонентов """


class ksPatternBasePointTypeEnum:  # kspatternbasepointtypeenum.html
    """ ## ksPatternBasePointTypeEnum - Способ задания базовой точки """
    ksCRAuto        = 0
    """ Автоопределение """
    ksCRManual      = 1
    """ Ручное указание """
    ksCRFirstObject = 2
    """ По первому в списке """


class ksPatternExemplarsOrientationTypeEnum:  # kspatternexemplarsorientationtypeenum.html
    """ ## ksPatternExemplarsOrientationTypeEnum - Способ ориентации экземпляров массива """
    ksOrientationSave     = 0
    """ Сохранять исходную ориентацию """
    ksOrientationByNormal = 1
    """ Доворачивать до нормали """
    ksOrientationByObject = 2
    """ Ориентировать по объекту """


class ksPhantomTypeEnum:  # ksphantomtypeenum.html
    """ ## ksPhantomTypeEnum - Типы фантома """
    ksUnknownPhantom       = 0
    """ Нет фантома """
    ksMoveGroupPhantom     = 1
    """ Cдвиг группы """
    ksLineSegPhantom       = 2
    """ Отрезок """
    ksRectanglePhantom     = 3
    """ Прямоугольник """
    ksAngleLineSegPhantom  = 4
    """ Отрезок с заданным углом """
    ksHalfRectanglePhantom = 5
    """ Половина прямоугольника """
    ksUserPhantom          = 6
    """ Пользовательский фантом """
    ksCirclePhantom        = 7
    """ Окружность """


class ksPLMChangesEnum:  # ksplmchangesenum.html
    """ ## ksPLMChangesEnum - Отличие в системе версионирования """
    ksPLMChangeUndefined    = 0
    """ Состояние не задано """
    ksPLMNoChanges          = 1
    """ Нет различий """
    ksPLMChangesNotCommited = 2
    """ Изменения не загружены в ЛОЦМАН:PLM """
    ksPLMUpdateNeeded       = 3
    """ Есть изменения в ЛОЦМАН:PLM """
    ksPLMConflict           = 4
    """ Ошибка """


class ksPLMPropertyEnum:  # ksplmpropertyenum.html
    """ ## ksPLMPropertyEnum - Свойства объектов версионирования """
    ksPLMPropertyVersion     = 1
    """ Версия """
    ksPLMPropertyAuthor      = 2
    """ Создал """
    ksPLMPropertyBlocked     = 3
    """ Заблокировал """
    ksPLMPropertySession     = 4
    """ Сессия """
    ksPLMPropertyAccessLevel = 5
    """ Уровень доступа """
    ksPLMPropertyCondition   = 6
    """ Состояние """


class ksPLMStatusEnum:  # ksplmstatusenum.html
    """ ## ksPLMStatusEnum - Статус в системе версионирования """
    ksPLMStateUndefined     = 0
    """ Состояние не задано """
    ksPLMStateNotRegistered = 1
    """ Не зарегистрирован в ЛОЦМАН:PLM """
    ksPLMStateAvailable     = 2
    """ Просмотр """
    ksPLMStateInProgress    = 3
    """ Взят в работу """
    ksPLMStateBlocked       = 4
    """ Заблокирован """
    ksPLMStateError         = 5
    """ Ошибка """


class ksPLMObjectNotifyEnum:  # ksplmobjectnotifyenum.html
    """ ## ksPLMObjectNotifyEnum - Cобытия объектов версионирования """
    ksPLMStatusChanged    = 1001
    """ Изменение статуса в системе версионирования """
    ksOrientationByObject = 1002
    """ Изменение признака отличия в системе версионирования """
    ksPLMValueChanged     = 1003
    """ Изменение значения свойств объекта версионирования """


class ksPointsArrOnCurveTypeEnum:  # kspointsarroncurvetypeenum.html
    """ ## ksPointsArrOnCurveTypeEnum - Способ построения точек группы по кривой """
    ksPAOCByPointsCount    = 0
    """ Равномерно по длине (Построение по заданному количеству точек) """
    ksPAOCByStep           = 1
    """ Шаг по кривой (Построение по расстоянию между точками) """
    ksPAOCByParametricStep = 2
    """ Равномерный шаг по параметру кривой (Построение по параметрическому расстоянию между точками) """


class ksPointsArrOnSurfaceTypeEnum:  # kspointsarronsurfacetypeenum.html
    """ ## ksPointsArrOnSurfaceTypeEnum - Способ построения точек группы по поверхности """
    ksPAOSByPointsUVCount     = -1
    """ По количеству точек по U и V """
    ksPAOSByLinearDeflection  = 0
    """ По линейному отклонению """
    ksPAOSByAngularDeflection = 1
    """ По угловому отклонению """
    ksPAOSByMeshAroundPoint   = 2
    """ По сетке вокруг заданной точки """


class ksPoint3DCurveParamTypeEnum:  # kspoint3dcurveparamtypeenum.html
    """ ## ksPoint3DCurveParamTypeEnum - Типы смещений при способе построения точки вдоль кривой """
    ksOffsetByU     = 1
    """ По параметру U,% """
    ksOffsetByLen   = 2
    """ По длине дуги """
    ksOffsetByAngle = 3
    """ По центральному углу дуги """


class ksPoint3DSurfaceParamTypeEnum:  # kspoint3dsurfaceparamtypeenum.html
    """ ## ksPoint3DSurfaceParamTypeEnum - Типы смещений при способе построения точки на поверхности """
    ksOffsetByUV             = 1
    """ По параметрам U и V,% """
    ksOffsetByLenFromObj     = 2
    """ По расстояниям от плоских объектов """
    ksOffsetByCoords         = 3
    """ По координатам на плоскости """
    ksOffsetByCylinderCoords = 4
    """ Смещение по цилиндрическим координатам """
    ksOffsetBySphereCoords   = 5
    """ Смещение по сферическим координатам """


class ksPoint3DTypeEnum:  # kspoint3dtypeenum.html
    """ ## ksPoint3DTypeEnum - Способы построения пространственной точки """
    ksPUnknown       = 0
    """ Неизвестный тип """
    ksPParamCoord    = 1
    """ По координатам от опорного объекта """
    ksPDisplace      = 2
    """ По смещению от опорного объекта """
    ksPIntersect     = 3
    """ На пересечении опорных объектов """
    ksPCenter        = 4
    """ В центре опорного объекта """
    ksPCurve         = 5
    """ На кривой со смещением """
    ksPSurface       = 6
    """ На поверхности """
    ksPProjection    = 7
    """ Проецированием """
    ksPCylindrCoord  = 8
    """ По цилиндрическим координатам """
    ksPSphericCoord  = 9
    """ По сферическим координатам """
    ksPBetweenPoints = 10
    """ Между точками """


class ksPointLocationTypeEnum:  # kspointlocationtypeenum.html
    """ ## ksPointLocationTypeEnum - Положение двумерной точки относительно двумерной кривой """
    ksPLUndefined = 0
    """ Положение не определено, кривая разомкнута """
    ksPLOutside   = 1
    """ Точка снаружи замкнутой кривой """
    ksPLOnCurve   = 2
    """ Точка на кривой """
    ksLPInside    = 3
    """ Точка внутри замкнутой кривой """


class ksPositionLederFormEnum:  # kspositionlederformenum.html
    """ ## ksPositionLederFormEnum - Тип формы для позиционной линии-выноски """
    ksPLSingleText          = 0
    """ Простой текст """
    ksPLOpenText            = 1
    """ Открытый текст """
    ksPLCircle              = 2
    """ Круг """
    ksPLHexagon             = 3
    """ Шестиугольник """
    ksPLCircleWithSeparator = 4
    """ Круг с разделителем """


class ksPressFormingHeightTypeEnum:  # kspressformingheighttypeenum.html
    """ ## ksPressFormingHeightTypeEnum - Способ задания высоты штамповки """
    ksPressFormingAllHeight = 0
    """ Полная """
    ksPressFormingOutHeight = 1
    """ Снаружи """
    ksPressFormingInHeight  = 2
    """ Внутри """


class ksProcessContextMenuType:  # ksprocesscontextmenutype.html
    """ ## ksProcessContextMenuType - Тип процессного меню """
    ksProcessDefaultContextMenu = 0
    """ Обычное меню процесса """
    ksProcessContextMenuHide    = -2
    """ Без меню """
    ksProcessContextPanel       = -3
    """ Контекстная панель с контролами """
    ksProcessContextIconMenu    = -4
    """ Меню с иконками """


class ksProcess3DManipulatorsNotifyEnum:  # ksprocess3dmanipulatorsnotifyenum.html
    """ ## ksProcess3DManipulatorsNotifyEnum - События манипуляторов процесса 3D """
    ksRotateManipulator         = 1
    """ Вращение манипулятора относительно оси на угол """
    ksMoveManipulator           = 2
    """ Перемещение манипулятора """
    ksClickManipulatorPrimitive = 3
    """ Клик или двойной клик по примитиву манипулятора """
    ksBeginDragManipulator      = 4
    """ Начало перемещения манипулятором примитива """
    ksEndDragManipulator        = 5
    """ Завершение перемещения манипулятором примитива """
    ksCreateManipulatorEdit     = 6
    """ Создание редактора для ввода значения, управляющего положением манипулятора """
    ksDestroyManipulatorEdit    = 7
    """ Удаление редактора для ввода значения, управляющего положением манипулятора """
    ksChangeManipulatorValue    = 8
    """ Завершение редактирования значения в редакторе манипулятора """


class ksProcessObjectsFilter3DEnum:  # ksprocessobjectsfilter3denum.html
    """ ## ksProcessObjectsFilter3DEnum - Режим использования прямоугольной рамки для выделения объектов в процессе """
    ksProcessFilterBodies                 = 0
    """ Фильтровать тела """
    ksProcessFilterSurfaces               = 1
    """ Фильтровать поверхности """
    ksProcessFilterObjects                = 2
    """ Объекты модели, не являющиеся операциями """
    ksProcessFilterOperations             = 3
    """ Операции """
    ksProcessFilterParts                  = 4
    """ Фильтровать компоненты """
    ksProcessFilterExcludeExternalObjects = 1000
    """ Отсекать объекты других компонентов, не находящиеся сейчас в режиме редактирования на месте """


class ksProjectionOptionEnum:  # ksprojectionoptionenum.html
    """ ## ksProjectionOptionEnum - Опции проецирования """
    ksPOUndefined = -1
    """ Неопределенное состояние """
    ksPODisable   = 0
    """ Не проецировать """
    ksPOEnable    = 1
    """ Проецировать """
    ksPOByLayer   = 2
    """ По слою """


class ksPropertyTypeEnum:  # kspropertytypeenum.html
    """ ## ksPropertyTypeEnum - Типы свойств """
    ksPropertyDataTypeUnknown    = 0
    """ Неизвестный """
    ksPropertyDataTypeLong       = 1
    """ Целый """
    ksPropertyDataTypeDouble     = 2
    """ Вещественный """
    ksPropertyDataTypeString     = 3
    """ Строка """
    ksPropertyDataTypeBoolean    = 4
    """ Логический """
    ksPropertyDataTypeColorRGB   = 5
    """ Цвет RGB """
    ksPropertyDataTypeHatchStyle = 6
    """ Стиль штриховки """
    ksPropertyDataTypeGroup      = 7
    """ Группа свойств """


class ksProtectProductStatusEnum:  # ksprotectproductstatusenum.html
    """ ## ksProtectProductStatusEnum - Состояния (статус) защиты продукта """
    ksProtectUnknown  = 0
    """ Неопределенный, состояние неизвестно """
    ksProtectDemo     = 1
    """ Недоступный, деморежим. """
    ksProtectDisabled = 2
    """ Запрещенный, отключенный """
    ksProtectExpired  = 3
    """ Недействительный, просроченный """
    ksProtectNormal   = 4
    """ Нормальный, рабочий """
    ksProtectFailed   = 5
    """ Неудачный, неисправный, повреждённый """


class ksRasterFormatEnum:  # ksrasterformatenum.html
    """ ## ksRasterFormatEnum - Типы изображений """
    ksRasterFormatBMP = 0
    """ BMP """
    ksRasterFormatGIF = 1
    """ GIF """
    ksRasterFormatJPG = 2
    """ JPG """
    ksRasterFormatPNG = 3
    """ PNG """
    ksRasterFormatTIF = 4
    """ TIFF """
    ksRasterFormatTGA = 5
    """ TGA """
    ksRasterFormatPCX = 6
    """ PCX """
    ksRasterFormatWMF = 16
    """ WMF """
    ksRasterFormatEMF = 17
    """ EMF """


class ksRedrawDocumentModeEnum:  # ksredrawdocumentmodeenum.html
    """ ## ksRedrawDocumentModeEnum - Режим перерисовки окон документа """
    ksRedrawFull             = 0
    """ Полная перерисовка """
    ksRedrawAnimation        = 1
    """ Выполнение анимации сцены """
    ksRedrawSelection        = 2
    """ Селектирование или подсветка """
    ksRedrawOperationPhantom = 3
    """ Операционные фантомы """
    ksRedrawDimensions       = 4
    """ Операционные размеры """
    ksRedrawPhantomObjects   = 5
    """ Фантомные объекты """
    ksRedrawHighlightObjects = 6
    """ Подсветка объектов под курсором """
    ksRedrawWidgets          = 7
    """ Манипуляторы, 3D хот-точки и т.п """


class ksRecoverErrorEnum:  # ksrecovererrorenum.html
    """ ## ksRecoverErrorEnum - Признак ошибок при открытии документа с восстановлением """
    ksRNoError     = 0
    """ Проверка завершена. Ошибок не найдено """
    ksRecover      = 1
    """ Проверка завершена. Найденные ошибки исправлены """
    ksRNoOpen      = 2
    """ Проверка завершена. Открыть документ не удалось """
    ksRAlreadyOpen = 3
    """ Файл уже открыт в одном из окон. Проверка невозможна """
    ksRProtected   = 4
    """ Файл защищен с помощью приложения КОМПАС-Защита. Проверка невозможна """


class ksRegionTypeEnum:  # ksregiontypeenum.html
    """ ## ksRegionTypeEnum - Тип региона """
    ksRTInside   = 1
    """ Полностью внутри """
    ksRTOutside  = 2
    """ Cнаружи """
    ksRTCutFrame = 3
    """ Секущей рамкой """


class ksRelativeProjectionTypeEnum:  # ksrelativeprojectiontypeenum.html
    """ ## ksRelativeProjectionTypeEnum - Тип проекции стандартного вида относительно главного вида """
    ksPtNone   = -1
    """ Не определена """
    ksPtFront  = 1
    """ Спереди - Фронтальная плоскость """
    ksPtRear   = 2
    """ Сзади """
    ksPtUp     = 3
    """ Сверху - Горизонтальная плоскость """
    ksPtDown   = 4
    """ Снизу """
    ksPtLeft   = 5
    """ Слева - Профильная плоскость """
    ksPtRight  = 6
    """ Справа """
    ksPtIsoXYZ = 7
    """ Изометрия XYZ """


class ksRelationTypeEnum:  # ksrelationtypeenum.html
    """ ## ksRelationTypeEnum - Тип родственных отношений """
    ksRTUnknown     = 0
    """ Не определен """
    ksRTIndifferent = 1
    """ Все отношения """
    ksRTStrong      = 2
    """ Сильные отношения """


class ksReportFiltersTypeEnum:  # ksreportfilterstypeenum.html
    """ ## ksReportFiltersTypeEnum - Типы фильтров в команде Создать отчет """
    ksFilterConditionUnknown        = 0
    """ Неизвестный """
    ksFilterConditionEqual          = 1
    """ = """
    ksFilterConditionSmaller        = 2
    """ < """
    ksFilterConditionLarger         = 3
    """ > """
    ksFilterConditionEqualOrSmaller = 4
    """ =< """
    ksFilterConditionEqualOrLarger  = 5
    """ => """
    ksFilterConditionContain        = 6
    """ содержит """
    ksFilterConditionNotContain     = 7
    """ не содержит """


class ksRequestFilesTypeEnum:  # ksrequestfilestypeenum.html
    """ ## ksRequestFilesTypeEnum - Тип процесса, запрашивающего файл или список файлов """
    ksRFUnknown                               = 0
    """ Неизвестный тип """
    ksRFSaveBody                              = 1
    """
    Cохранение тела в модель

    Допустимые расширения: m3d

    Множественный выбор: -
    """
    koRFUnitParts                             = 2
    """
    Объединение вставок в подсборку

    Допустимые расширения: a3d

    Множественный выбор: -
    """
    koRFCopyBilletPart                        = 3
    """
    Вставка детали заготовки

    Допустимые расширения: m3d

    Множественный выбор: -
    """
    koRFSavePartAs                            = 4
    """
    Сохранение вставки в файл

    Допустимые расширения: m3d, a3d

    Множественный выбор: -
    """
    koRFAddDetail                             = 5
    """
    Вставка детали в сборку

    Допустимые расширения: m3d

    Множественный выбор: -
    """
    koRFAddAssembly                           = 6
    """
    Вставка подсборки в сборку

    Допустимые расширения: a3d

    Множественный выбор: -
    """
    koRFAddPartFromFile                       = 7
    """
    Добавить компонент из файла

    Допустимые расширения: m3d, a3d

    Множественный выбор: -
    """
    koRFChangeDetailFile                      = 8
    """
    Заменить файл источник для вставки детали

    Допустимые расширения: m3d

    Множественный выбор: -
    """
    koRFChangeAssemblyFile                    = 9
    """
    Заменить файл источник для вставки сборки

    Допустимые расширения: a3d

    Множественный выбор: -
    """
    koRFChangeBilletPartFile                  = 10
    """
    Заменить файл источник для детали заготовки

    Допустимые расширения: a3d

    Множественный выбор: -
    """
    koRFSpcObjAddDocument                     = 11
    """
    Подключение документов КОМПАС к объекту спецификации

    Допустимые расширения: frw,cdw,m3d,a3d,kdw

    Множественный выбор: +
    """
    koRFSpcAssemblyAddDocument                = 12
    """
    Подключение документов КОМПАС к спецификации - Управление сборкой

    Допустимые расширения: cdw,a3d

    Множественный выбор: +
    """
    koRFAddLocalDetail                        = 13
    """
    Добавить локальную деталь

    Допустимые расширения: m3d
    """
    koRFAddLayoutGeometry                     = 14
    """
    Добавить компоновочную геометрию

    Допустимые расширения: m3d, a3d
    """
    koRFSelectDummyFile                       = 15
    """ Выбор файла макета """
    koRFSelectCopyGeometryFile                = 16
    """ Выбор файла модели для копирования геометрии """
    koRFSelectModelForAssociationView         = 17
    """ Выбор файла модели для создания проекционного вида """
    koRFSelectModelForStandartAssociationView = 18
    """ Выбор файла модели для создания стандартных видов """


class ksRibSideEnum:  # ksribsideenum.html
    """ ## ksRibSideEnum - Положение ребра жесткости """
    ksRibSideLeft  = 0
    """ Прямое направление в плоскости эскиза. Ребро выдавливается в левую сторону от кривой вдоль плоскости """
    ksRibSideRight = 1
    """ Обратное направление в плоскости эскиза. Ребро выдавливается в правую сторону от кривой вдоль плоскости """
    ksRibSideUp    = 2
    """ Прямое направление ортогонально эскизу. Ребро выдавливается в сторону нормали плоскости """
    ksRibSideDown  = 3
    """ Обратное направление ортогонально эскизу. Ребро выдавливается в сторону против нормали плоскости """


class ksRotatedTypeEnum:  # ksrotatedtypeenum.html
    """ ## ksRotatedTypeEnum - Способы определения угла вращения """
    ksRTAngle   = 0
    """ Угол """
    ksRTVertex  = 1
    """ До вершины """
    ksRTSurface = 2
    """ До поверхности """


class ksRoughModificationEnum:  # ksroughmodificationenum.html
    """ ## ksRoughModificationEnum - Вариант создания шероховатости """
    ksRoughModification1973 = 0
    """ Старая версия ГОСТ 2.309-73 """
    ksRoughModification2003 = 1
    """ Шероховатость в соответствии с изменением №3 от 2003 г. в ГОСТ 2.309-73 """


class ksRoughSignEnum:  # ksroughsignenum.html
    """ ## ksRoughSignEnum - Тип значка шероховатости """
    ksNoProcessingType      = 0
    """ Без указания типа обработки """
    ksDeleteMaterial        = 1
    """ С удалением слоя материала """
    ksWithoutDeleteMaterial = 2
    """ Без удаления слоя материала """


class ksRuledBorderEnum:  # ksruledborderenum.html
    """ ## ksRuledBorderEnum - Типы кромки оснований """
    ksRuledBodder1 = 0
    """ Перпендикулярно плоскости листа """
    ksRuledBodder2 = 1
    """ Совпадение с поверхностями оснований """


class ksRuledSurfaceBuildingTypeEnum:  # ksruledsurfacebuildingtypeenum.html
    """ ## ksRuledSurfaceBuildingTypeEnum - Способ построения при скруглении с переменным радиусом """
    ksRuledSurfaceByCurves              = 0
    """ Линейчатая поверхность по двум кривым """
    ksRuledSurfaceBySurfaces            = 1
    """ Линейчатая поверхность по двум поверхностям """
    ksRuledSurfaceByCurveAndSurface     = 2
    """ Линейчатая поверхность по кривой и поверхности """
    ksRuledSurfaceBySurfaceTangentCurve = 3
    """ Линейчатая поверхность по кривой с касанием к поверхности """
    ksRuledSurfaceByCurveAndDir         = 4
    """ Линейчатая поверхность по кривой и направлению """


class ksRuledSurfaceDirectionTypeEnum:  # ksruledsurfacedirectiontypeenum.html
    """ ## ksRuledSurfaceDirectionTypeEnum - Направление построения линейчатой поверхности """
    ksRuledSurfaceDirectionTangent = 0
    """ По касательной """
    ksRuledSurfaceDirectionNormal  = 1
    """ Перпендикулярно """


class ksRuledSurfaceSectionAlignmentTypeEnum:  # ksruledsurfacesectionalignmenttypeenum.html
    """ ## ksRuledSurfaceSectionAlignmentTypeEnum - Параметры линейчатой поверхности "По двум кривым" """
    ksRuledSurfaceSectionAlignmentByParam  = 0
    """ По направлению, заданному вектором """
    ksRuledSurfaceSectionAlignmentByLen    = 1
    """ Вдоль траектории, заданной кривой """
    ksRuledSurfaceSectionAlignmentByVertex = 2
    """ Радиально, вокруг заданной оси """
    ksRuledSurfaceSectionAlignmentByPath   = 3
    """ Радиально, вокруг заданной оси """


class ksRuledSurfaceMovementTypeEnum:  # ksruledsurfacemovementtypeenum.html
    """ ## ksRuledSurfaceMovementTypeEnum - Типы движения конического сечения """
    ksRuledSurfaceMovementByVector = 0
    """ По направлению, заданному вектором """
    ksRuledSurfaceMovementByCurve  = 1
    """ Вдоль траектории, заданной кривой """
    ksRuledSurfaceMovementByRadial = 2
    """ Радиально, вокруг заданной оси """


class ksRuledJointEnum:  # ksruledjointenum.html
    """ ## ksRuledJointEnum - Типы кромки стыка """
    ksRuledJoint1 = 0
    """ Перпендикулярно поверхности листа """
    ksRuledJoint2 = 1
    """ Параллельно друг другу """


class ksScalingTypeEnum:  # ksscalingtypeenum.html
    """ ## ksScalingTypeEnum - Способ масштабирования """
    ksScalingByCoefficient = 0
    """ Равномерно """
    ksScalingByAxis        = 1
    """ По осям CK """


class ksSketchEdgesTypeEnum:  # kssketchedgestypeenum.html
    """ ## ksSketchEdgesTypeEnum - Тип ребер эскиза """
    ksSketchEdgesFromCurves2D = 1
    """ Ребра исходных кривых эскиза """
    ksSketchEdgesFromFaces    = 2
    """ Ребра замкнутых областей эскиза """


class ksSideAngleTypeEnum:  # kssideangletypeenum.html
    """ ## ksSideAngleTypeEnum - Движение сечения """
    ksSideAngleValueConstant = 0
    """ Константное значение """
    ksSideAngleValueStart    = 1
    """ Начальное значение """
    ksSideAngleValueEnd      = 2
    """ Конечное значение """


class ksSHRibBuildingTypeEnum:  # ksshribbuildingtypeenum.html
    """ ## ksSHRibBuildingTypeEnum - Способ построения ребра усиления """
    ksSHRibBuildingHeightAngle = 0
    """ По стороне и углу """
    ksSHRibBuildingTwoHeights  = 1
    """ По двум сторонам """
    ksSHRibBuildingDepthAngle  = 2
    """ По глубине и углу """


class ksSHRibCutingTypeEnum:  # ksshribcutingtypeenum.html
    """ ## ksSHRibCutingTypeEnum - Форма сечения ребра усиления """
    ksSHRibCuttingV = 0
    """ V-образная """
    ksSHRibCuttingU = 1
    """ U-образная """


class ksSegmentationMethodEnum:  # kssegmentationmethodenum.html
    """ ## ksSegmentationMethodEnum - Способ сегментации эскиза """
    ksSmQuantity = 0
    """ По количеству сегментов """
    ksSmLength   = 1
    """ По длине сегментов """
    ksSmAngle    = 2
    """ По углу """
    ksSmHeight   = 3
    """ По величине отклонения от хорды """


class ksSelectionBandMode:  # ksselectionbandmode.html
    """ ## ksSelectionBandMode - Режим использования прямоугольной рамки для выделения объектов """
    ksSelectionNoBand              = 0
    """ Не использовать селектирование рамкой """
    ksSelectionWhenNoNearestObject = 2
    """ Начинать тащить рамку, когда под курсором нет объекта """


class ksSemiAxisTypeEnum:  # kssemiaxistypeenum.html
    """ ## ksSemiAxisTypeEnum - Тип полуоси для обозначения центра """
    ksAxisUnknown = -1
    """ Неизвестный """
    ksAxisXPlus   = 0
    """ Полуось по оси X """
    ksAxisXMinus  = 1
    """ Полуось против оси X """
    ksAxisYPlus   = 2
    """ Полуось по оси Y """
    ksAxisYMinus  = 3
    """ Полуось против оси Y """


class ksSheetsRangeEnum:  # kssheetsrangeenum.html
    """ ## ksSheetsRangeEnum - Тип диапазона страниц """
    ksAllSheets    = 0
    """ Все страницы """
    ksUnevenSheets = 1
    """ Нечетные страницы """
    ksEvenSheets   = 2
    """ Четные страницы """


class ksSheetMetalPunchBuildingTypeEnum:  # kssheetmetalpunchbuildingtypeenum.html
    """ ## ksSheetMetalPunchBuildingTypeEnum - Способ построения для штамповки телом. Инструмент """
    ksSheetMetalPunch  = 0
    """ Пуансон """
    ksSheetMetalMatrix = 1
    """ Матрица """


class ksSheetMetalPunchEdgeTypeEnum:  # kssheetmetalpunchedgetypeenum.html
    """ ## ksSheetMetalPunchEdgeTypeEnum - Тип вырубки кромки """
    ksPetCutted = 0
    """ Обрезка гранью вырубки """
    ksPetNormal = 1
    """ По нормали к листовым граням """


class ksSheetMetalPunchThicknessTypeEnum:  # kssheetmetalpunchthicknesstypeenum.html
    """ ## ksSheetMetalPunchThicknessTypeEnum - Способ задания толщины для штамповки телом """
    ksSheetMetalPunchHeightByBody  = 0
    """ Листовое тело """
    ksSheetMetalPunchHeightByValue = 1
    """ Заданное значение """


class ksShelfDirectionEnum:  # ksshelfdirectionenum.html
    """ ## ksShelfDirectionEnum – Направление полки """
    ksLSLeft  = -1
    """ Влево """
    ksLSNone  = 0
    """ Нет полки """
    ksLSRight = 1
    """ Вправо """
    ksLSUp    = 2
    """ Вверх """
    ksLSDown  = 3
    """ Вниз """


class ksSketchBendBuildingTypeEnum:  # kssketchbendbuildingtypeenum.html
    """ ## ksSketchBendBuildingTypeEnum - Способы построения сгиба по эскизу """
    ksSBFromSketch = 1
    """ От эскиза """
    ksSBSomeEdges  = 2
    """ Вдоль всего ребра """


class ksShoulderBuildingTypeEnum:  # ksshoulderbuildingtypeenum.html
    """ ## ksShoulderBuildingTypeEnum - Способ построения буртика """
    ksShoulderUnknown                     = 0
    """ Не определено """
    ksShoulderWidth1                      = 1
    """ Использовать при расчете ширину основания """
    ksShoulderHeight                      = 2
    """ Использовать при расчете высоту """
    ksShoulderAngle                       = 4
    """ Использовать при расчете угол """
    ksShoulderWidth2                      = 8
    """ Использовать при расчете ширину дна """
    ksShoulderRadius2                     = 16
    """ Использовать при расчете радиус буртика """
    ksShoulderWidth1Off                   = -1
    """ Не использовать при расчете ширину основания """
    ksShoulderHeightOff                   = -2
    """ Не использовать при расчете высоту """
    ksShoulderAngleOff                    = -4
    """ Не использовать при расчете угол """
    ksShoulderWidth2Off                   = -8
    """ Не использовать при расчете ширину дна """
    ksShoulderRadius2Off                  = -16
    """ Не использовать при расчете радиус буртика """
    ksShoulderCircleByHeightWidth1        = 3
    """ Круговая по высоте и ширине основания """
    ksShoulderCircleByHeightRadius2       = 18
    """ Круговая по высоте и радиусу буртика """
    ksShoulderCircleByRadiusWidth1        = 17
    """ Круговая по радиусу буртика и ширине основания """
    ksShoulderUByHeighAngleWidth1         = 7
    """ U-образная по высоте, углу и ширине основания """
    ksShoulderUByHeighAngleWidthRadius2   = 23
    """ U-образная по высоте, углу и ширине основания со скруглением дна """
    ksShoulderUByHeighWidth1Width2        = 11
    """ U-образная по высоте, ширине основания и ширине дна (две ширины) """
    ksShoulderUByHeighWidth1Width2Radius2 = 27
    """ U-образная по высоте, ширине основания и ширине дна (две ширины) со скруглением дна """
    ksShoulderUByAngleWidth1Width2        = 13
    """ U-образная по углу, ширине основания и ширине дна (две ширины) """
    ksShoulderUByAngleWidth1Width2Radius2 = 29
    """ U-образная по углу, ширине основания и ширине дна (две ширины) со скруглением дна """
    ksShoulderUByHeighAngleWidth2         = 14
    """ U-образная по высоте, углу и ширине дна """
    ksShoulderUByHeighAngleWidth2Radius2  = 30
    """ U-образная по высоте, углу и ширине дна со скруглением дна """
    ksShoulderVByHeighAngleWidth1         = 7
    """ V-образная по высоте, углу и ширине основания """
    ksShoulderVByHeighAngleRadius2        = 22
    """ V-образная по высоте, углу и радиусу буртика """
    ksShoulderVByRadius2AngleWidth1       = 21
    """ V-образная по радиусу буртика, углу и ширине основания """
    ksShoulderVByHeighRadius2Width1       = 19
    """ V-образная по высоте, радиусу буртика и ширине основания """


class ksShoulderCutingTypeEnum:  # ksshouldercutingtypeenum.html
    """ ## ksShoulderCutingTypeEnum - Форма сечения буртика """
    ksShoulderCutingCircle = 0
    """ Круговая """
    ksShoulderCutingU      = 1
    """ U-образная """
    ksShoulderCutingV      = 2
    """ V-образная """


class ksShoulderTypeEnum:  # ksshouldertypeenum.html
    """ ## ksShoulderTypeEnum - Тип буртика. Способ обработки концов буртика """
    ksShoulderClosed  = 0
    """ Закрытый """
    ksShoulderOpened  = 1
    """ Открытый """
    ksShoulderChopped = 2
    """ Рубленый """


class ksSlaveDocumentTypeEnum:  # ksslavedocumenttypeenum.html
    """ ## ksSlaveDocumentTypeEnum -Типы подчиненных режимов редактирования документов КОМПАС """
    ksSDSketchMode         = 1000
    """ Режим редактирования эскиза """
    ksSDSpecificationSlave = 1001
    """ Слейв режим редактирования спецификации """


class ksSmoothingMethodEnum:  # kssmoothingmethodenum.html
    """ ## ksSmoothingMethodEnum - Метод сглаживания """
    ksNoisy        = 0
    """ Сглаживание зашумленных точек """
    ksNoisyMidline = 1
    """ Сглаживание по средней линии отклонений зашумленных точек """


class ksSnapTypeEnum:  # kssnaptypeenum.html
    """ ## ksSnapTypeEnum - Тип привязки к объектам """
    ksSTUnknown        = -1
    """ Информация отсутствует """
    ksSTUndefine       = 0
    """ Нет привязки """
    ksSTNearestPoint   = 1
    """ Ближайшая точка """
    ksSTNearestMiddle  = 2
    """ Ближайшая середина """
    ksSTObjectCentre   = 3
    """ Центр объекта """
    ksSTIntersect      = 4
    """ Пересечение """
    ksSTGrid           = 5
    """ Привязка по сетке """
    ksSTXYAlign        = 6
    """ Выравнивание по X Y """
    ksSTAngleSnap      = 7
    """ Угловая привязка """
    ksSTPointOnCurve   = 8
    """ Точка на кривой """
    ksSTNormalToCurve  = 9
    """ По нормали на кривую """
    ksSTTangentToCurve = 10
    """ По касательной на кривую """


class ksSortTypeEnum:  # kssorttypeenum.html
    """ ## ksSortTypeEnum - Типы сортировки """
    ksSortTypeNone          = 0
    """ Нет сортировки """
    ksSortTypeCompositeUp   = 1
    """ Составная сортировка по возрастанию колонок """
    ksSortTypeUp            = 3
    """ Сортировка по возрастанию колонок """
    ksSortTypeDocument      = 4
    """ Сортировка раздела документация """
    ksSortTypeDown          = 5
    """ Сортировка по убыванию колонок """
    ksSortTypeCompositeDown = 6
    """ Составная сортировка по убыванию колонок """


class ksSpecificationColumnTypeEnum:  # ksspecificationcolumntypeenum.html
    """ ## ksSpecificationColumnTypeEnum - Типы колонок спецификации """
    ksSColumnUnknown        = 0
    """ Неизвестный тип """
    ksSColumnFormat         = 1
    """ Формат """
    ksSColumnZone           = 2
    """ Зона """
    ksSColumnPosition       = 3
    """ Позиция """
    ksSColumnMark           = 4
    """ Обозначение """
    ksSColumnName           = 5
    """ Наименование """
    ksSColumnCount          = 6
    """ Количество """
    ksSColumnNote           = 7
    """ Примечание """
    ksSColumnMass           = 8
    """ Масса """
    ksSColumnMaterial       = 9
    """ Материал """
    ksSColumnUser           = 10
    """ Пользовательская """
    ksSColumnCode           = 11
    """ Код """
    ksSColumnFactory        = 12
    """ Завод изготовитель """
    ksSColumnDocumentNumber = 13
    """ Номер документа """
    ksSColumnDocumentName   = 14
    """ Наименование документа """
    ksSColumnDocumentCode   = 15
    """ Код документа """
    ksSColumnCodeOKP        = 16
    """ Код ОКП """


class ksSpecificationObjectStateEnum:  # ksspecificationobjectstateenum.html
    """ ## ksSpecificationObjectStateEnum - Состояние объекта спецификации """
    ksObjectStateIndependent    = 0
    """ Самостоятельный объект """
    ksObjectStateFromInsert     = 1
    """ Объект из вставки """
    ksObjectStateEdit           = 2
    """ Объект редактировался в документе """
    ksObjectStateUserSetNotEdit = 3
    """ Пользователь снял признак редактирования. """


class ksSpecificationObjectTypeEnum:  # ksspecificationobjecttypeenum.html
    """
    ## ksSpecificationObjectTypeEnum - Типы объектов для спецификации

    В API5 соответствует Типам объектов спецификации...
    """
    ksSpecificationUnknownObject = 0
    """ Неизвестный тип """
    ksSpecificationBaseObject    = 1
    """ Базовый объект """
    ksSpecificationComment       = 2
    """ Комментарий """
    ksSpecificationSectionName   = 3
    """ Имя раздела """
    ksSpecificationBlock         = 4
    """ Начало блока """
    ksSpecificationReserveString = 5
    """ Резервная строка """
    ksSpecificationEmptyString   = 6
    """ Пустая строка """
    ksSpecificationBilletObject  = 7
    """ Объект заготовка """


class ksSpecificationVariantEnum:  # ksspecificationvariantenum.html
    """ ## ksSpecificationVariantEnum - Варианты оформления спецификации """
    ksSpecificationSimple   = 0
    """ Простая """
    ksSpecificationVariantA = 1
    """ Вариант А """
    ksSpecificationVariantB = 2
    """ Вариант Б """
    ksSpecificationVariantV = 3
    """ Вариант В """
    ksSpecificationVariantG = 4
    """ Вариант Г """


class ksSpecRoughPlacementEnum:  # ksspecroughplacementenum.html
    """ ## ksSpecRoughPlacementEnum - Размещение неуказанной шероховатости """
    ksRPTopLeft     = 0
    """ Вверху слева """
    ksRPTopRight    = 1
    """ Вверху справа """
    ksRPBottomRight = 2
    """ Внизу справа """


class ksSpcUsedTypeEnum:  # ksspcusedtypeenum.html
    """ ## ksSpcUsedTypeEnum - Признаки использования в спецификации """
    ksSpcUsedInAllDescriptions    = 0
    """ Отображать во всех описаниях """
    ksSpcUsedInCurrentDescription = 1
    """ Отображать в текущем описании """


class ksSpiral3DHeightTypeEnum:  # ksspiral3dheighttypeenum.html
    """ ## ksSpiral3DHeightTypeEnum - Способ задания высоты спирали 3D """
    ksSHTByValue  = 0
    """ По заданному значению высоты """
    ksSHTByObject = 1
    """ По объекту """
    ksSHTByCurve  = 2
    """ По длине плоской кривой """


class ksSplineTransitionTypeEnum:  # kssplinetransitiontypeenum.html
    """ ## ksSplineTransitionTypeEnum - Способ создания сопряжения в заданной вершине сплайна """
    ksSTTNone       = 0
    """ Не задан """
    ksSTTByParam    = 1
    """ Параметрами """
    ksSTTConstraint = 2
    """ Сопряжением """


class ksSplineTangentEnum:  # kssplinetangentenum.html
    """ ## ksSplineTangentEnum - Тип направления касательной """
    ksSTNone         = 0
    """ Не задано """
    ksSTByDirection  = 1
    """ По направлению """
    ksSTCurveU       = 2
    """ К изопараметрической кривой по направлению U """
    ksSTCurveV       = 3
    """ К изопараметрической кривой по направлению V """
    ksSTSurfaceCurve = 4
    """ К кривой на поверхности """


class ksSpline3DBuildingTypeEnum:  # ksspline3dbuildingtypeenum.html
    """ ## ksSpline3DBuildingTypeEnum - Способ построения спирали 3D """
    ksSBTByStepAndTurnCount   = 0
    """ По шагу и количеству витков """
    ksSBTByStepAndHeight      = 1
    """ По шагу и высоте """
    ksSBTByTurnCountAndHeight = 2
    """ По количеству витков и высоте """


class ksSpline3DDiameterTypeEnum:  # ksspline3ddiametertypeenum.html
    """ ## ksSpline3DDiameterTypeEnum - Способ построения спирали 3D """
    ksSDTByValue               = 0
    """ По заданному значению диаметра """
    ksSDTByObject              = 1
    """ По объекту """
    ksSDTByGeneratrixTiltAngle = 2
    """ По углу наклона образующей """


class ksSplineBuildingTypeEnum:  # kssplinebuildingtypeenum.html
    """ ## ksSplineBuildingTypeEnum - Способ построения """
    ksSpline3DOnPoles    = 0
    """ Сплайн по полюсам """
    ksSpline3DOnPoints   = 1
    """ Сплайн по точкам """
    ksSpline3DMetaSpline = 2
    """ Метасплайн """


class ksStepTypeEnum:  # kssteptypeenum.html
    """ ## ksStepTypeEnum - Способы вычисления приращения параметра по объекту """
    ksSpaceStep     = 0x01
    """ Шаг по стрелке прогиба """
    ksDeviationStep = 0x02
    """ Шаг по углу отклонения """
    ksMetricStep    = 0x04
    """ Шаг по длине """
    ksParamStep     = 0x08
    """ Шаг для для привязки объектов к параметрам поверхности """
    ksCollisionStep = 0x10
    """ Шаг для определения столкновений элементов модели """
    ksMipStep       = 0x20
    """ Шаг для расчета инерционных характеристик """


class ksStylesLibraryTypeEnum:  # ksstyleslibrarytypeenum.html
    """ ## ksStylesLibraryTypeEnum - События функции поиска объектов """
    ksCurveStyleLibrary         = 1
    """ Библиотека стилей кривых (*.lcs) """
    ksHatchStyleLibrary         = 2
    """ Библиотека стилей штриховок (*.lhs) """
    ksTextStyleLibrary          = 3
    """ Библиотека стилей текстов (*.lts) """
    ksStampStyleLibrary         = 4
    """ Библиотека стилей описаний штампов (*.lyt) """
    ksGraphicLayoutStyleLibrary = 5
    """ Библиотека стилей оформлений графических документов и спецификаций (*.lyt) """
    ksTextLayoutStyleLibrary    = 6
    """ Библиотека стилей оформлений текстовых документов (*.lyt) """
    ksSpcLayoutStyleLibrary     = 7
    """ Библиотека стилей оформлений спецификаций (*.lyt) """


class ksSurfaceSalientTypeEnum:  # kssurfacesalienttypeenum.html
    """ ## ksSurfaceSalientTypeEnum - Признак выпуклой поверхности """
    ksSurfaceSalientNo      = -1
    """ Вогнутая поверхность """
    ksSurfaceSalientUnknown = 0
    """ Плоская или неоднородная или неизвестно """
    ksSurfaceSalientYes     = 1
    """ Выпуклая поверхность """


class ksSystemControlStartEnum:  # kssystemcontrolstartenum.html
    """ ## ksSystemControlStartEnum - Результаты передачи управления системе КОМПАС """
    ksSCStoppedByMenuCommand    = 1
    """ Выполнена команда меню Остановить работу библиотеки """
    ksSCCloseApplication        = 0
    """ Идет закрытие системы КОМПАС/Не запущен SystemControlStart. """
    ksSCStopItself              = -1
    """ Вызов функции SystemControlStop из-под библиотеки """
    ksSCAlreadyStarted          = -2
    """ Управление системе КОМПАС уже передано той же библиотекой """
    ksSCStartedByAnotherLibrary = -3
    """ Управление системе КОМПАС уже передано другой библиотекой """
    ksSCError                   = -4
    """ Ошибка """


class ksSystemPathTypeEnum:  # kssystempathtypeenum-----.html
    """ ## ksSystemPathTypeEnum - Тип системных каталогов """
    ksSystemFiles                  = 0
    """ Путь к каталогу системных файлов """
    ksApplications                 = 1
    """ Путь к каталогу файлов приложений """
    ksTemporaryFiles               = 2
    """ Путь к каталогу сохранения временных файлов """
    ksConfigurations               = 3
    """ Путь к каталогу сохранения конфигурации системы """
    ksIniFile                      = 4
    """ Полное имя INI-файла системы """
    ksBinaryFiles                  = 5
    """ Путь к каталогу исполняемых файлов системы """
    ksProjectFiles                 = 6
    """ Путь к каталогу сохранения kompas.prj """
    ksDesktopFiles                 = 7
    """ Путь к каталогу сохранения kompas.dsk """
    ksTemplates                    = 8
    """ Путь к каталогу шаблонов Компас-документов """
    ksProfiles                     = 9
    """ Путь к каталогу сохранения профилей пользователя """
    ksWorkFiles                    = 10
    """ Путь к каталогу Мои документы """
    ksSheetmetalTables             = 11
    """ Путь к каталогу таблиц сгибов """
    ksPartLib                      = 12
    """ Путь к каталогу PartLib """
    ksMultilineTemplates           = 13
    """ Путь к каталогу шаблонов мультилинии """
    ksPrintDeviceConfigurations    = 14
    """ Путь к каталогу конфигураций плоттеров/принтеров """
    ksCurrentWorkFiles             = 15
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения рабочих файлов """
    ksCurrentApplications          = 16
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения приложения """
    ksCurrentSystemFiles           = 17
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения системных файлов """
    ksCurrentProfiles              = 18
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения профиля пользователя """
    ksCurrentSheetmetalTables      = 19
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения таблиц сгибов """
    ksApplicationDirectories       = 20
    """ Список каталогов приложений """
    ksDocumentLibraries            = 21
    """ Путь к каталогу библиотек документов """
    ksDocumentLibrariesDirectories = 22
    """ Список каталогов библиотек документов """
    ksCurrentDocumentLibraries     = 23
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения библиотек документов """
    ksUnils                        = 24
    """ Путь к каталогу утилит """
    ksUnilsDirectories             = 25
    """ Список каталогов утилит """
    ksCurrentUnils                 = 26
    """ Последний выбранный путь в диалоге Open|Save для открытия/сохранения утилиты """
    ksProgramData                  = 27
    """ Путь к каталогу данных приложения """


class ksTablePointEnum:  # kstablepointenum.html
    """ ## ksTablePointEnum - Тип расположения точки на таблице """
    ksTPLeftBottom   = 1
    """ Левый нижний угол """
    ksTPLeftCenter   = 2
    """ Середина левой стороны """
    ksTPLeftUp       = 3
    """ Левый верхний угол """
    ksTPUpCenter     = 4
    """ Середина верхней стороны """
    ksTPRightUp      = 5
    """ Правый верхний угол """
    ksTPRightCenter  = 6
    """ Середина правой стороны """
    ksTPRightBottom  = 7
    """ Правый нижний угол """
    ksTPBottomCenter = 8
    """ Середина нижней стороны """
    ksTPCenter       = 9
    """ Середина точка для контрола Базовая точка """
    ksTPUndefined    = 0
    """ Не задано """


class ksTableTileLayoutEnum:  # kstabletilelayoutenum.html
    """ ## ksTableTileLayoutEnum - Расположение заголовка таблицы """
    ksTTLFirstRow    = 0
    """ В первой строке """
    ksTTLFirstColumn = 1
    """ В первом столбце """
    ksTTLNotCreate   = 2
    """ Не создавать """


class ksTabulatorFillingEnum:  # kstabulatorfillingenum.html
    """ ## ksTabulatorFillingEnum - Заполнение табулятора """
    ksTabulatorFillingNone       = 0
    """ Без заполнения """
    ksTabulatorFillingNone       = 1
    """ Базовая линия """
    ksTabulatorFillingCenterLine = 2
    """ Средняя линия """
    ksTabulatorFillingBaseDot    = 3
    """ Базовые точки """
    ksTabulatorFillingCenterDot  = 4
    """ Средние точки """
    ksTabulatorFillingBaseDash   = 5
    """ Базовый пунктир """
    ksTabulatorFillingCenterDash = 6
    """ Средний пунктир """


class ksTechnicalDemand3DPlacementEnum:  # kstechnicaldemand3dplacementenum.html
    """ ## ksTechnicalDemand3DPlacementEnum - Размещение технических требований """
    ksTdPTopRight    = 0
    """ Верху справа """
    ksTdPBottomRight = 1
    """ Внизу справа """


class ksTextureTypeEnum:  # kstexturetypeenum.html
    """ ## ksTextureTypeEnum - Тип текстуры """
    ksBaseProperties = -1
    """ Все """
    ksTexture        = 0
    """ Текстура """
    ksRelief         = 1
    """ Рельеф """
    ksCutting        = 2
    """ Вырезы """


class ksTransitionVectorIndexEnum:  # kstransitionvectorindexenum.html
    """ ## ksTransitionVectorIndexEnum - Индекс вектора в точке сопряжения """
    ksTVTangent = 0
    """ Касательный """
    ksTVNormal  = 1
    """ Нормальный """
    ksTVBNormal = 2
    """ Бинормальный """


class ksTextAlignEnum:  # kstextalignenum.html
    """ ## ksTextAlignEnum - Выравнивание текста для внешнего объекта GDI """
    ksTALeft     = 0
    """ Cлева """
    ksTARight    = 2
    """ Справа """
    ksTAHCenter  = 6
    """ Центр горизонтали """
    ksTATop      = 0
    """ Вверху """
    ksTABottom   = 8
    """ Внизу """
    ksTABaseline = 24
    """ Базовая линия """
    ksTAVCenter  = 56
    """ Центр вертикали """


class ksTextHorizontalFormatEnum:  # kstexthorizontalformatenum.html
    """ ## ksTextHorizontalFormatEnum – Признак горизонтального форматирования текста на чертеже """
    ksHFormatNot          = 0
    """ Перенос правой границы (нет форматирования) """
    ksHFormatStrNarrowing = 1
    """ Сужение текста """
    ksHFormatDivision     = 2
    """ Перенос на другую строку """


class ksTextExportFormEnum:  # kstextexportformenum.html
    """ ## ksTextExportFormEnum - Представление текста при экспорте """
    ksTEFTextOnly     = 1
    """ Только текст """
    ksTEFGeometryOnly = 2
    """ Геометрическое представление текста """


class ksTextItemEnum:  # kstextitemenum.html
    """ ## ksTextItemEnum – Тип компонента текста """
    ksTItString             = 0
    """ Строка. """
    ksTItNumerator          = 0x1
    """ Числитель. """
    ksTItDenominator        = 0x2
    """ Знаменатель. """
    ksTItFractionEnd        = 0x3
    """ Конец дроби. """
    ksTItUpperDeviation     = 0x4
    """ Верхнее отклонение. """
    ksTItLowerDeviation     = 0x5
    """ Нижнее отклонение. """
    ksTItDeviationEnd       = 0x6
    """ Конец отклонений. """
    ksTItSBase              = 0x7
    """ Основание выражения типа суммы. """
    ksTItSUpperIndex        = 0x8
    """ Верхний индекс выражения типа суммы. """
    ksTItSLowerIndex        = 0x9
    """ Нижний индекс выражения типа суммы. """
    ksTItSEnd               = 0x10
    """ Конец выражения типа суммы. """
    ksTItSpecialSymbol      = 0x11
    """ Спецзнак. """
    ksTItSpecialSymbolEnd   = 0x12
    """ Конец спецзнаков с текстом. """
    ksTItSpecialSymbolNext  = 0x13
    """ Начало для ввода следующих строк в спецзнаке с текстом. """
    ksTItSpecialSymbolDown  = 0x14
    """ Для ввода строк снизу в спецзнаке с текстом. """
    ksTItSpecialSymbolRight = 0x15
    """ Для ввода строк справа в спецзнаке с текстом. """
    ksTItTab                = 0x16
    """ Табуляция по текущему стилю. """
    ksTItFontSymbol         = 0x17
    """ Символ шрифта. """
    ksTItHyperText          = 0x2000
    """ Cсылка на текст или положение объекта """
    ksTItFontSymbolW        = 0x2017
    """ Символ шрифта Unicode """


class ksTextNumberingEnum:  # kstextnumberingenum.html
    """ ## ksTextNumberingEnum – Тип нумерации абзаца """
    ksTNumbUnknown       = -1
    """ Тип не определенный. """
    ksTNumbNoNumber      = 0
    """ Cрока без нумерации. """
    ksTNumbNumber        = 1
    """ Cтрока с нумерацией уровня level. """
    ksTNumbNewNumber     = 2
    """ На строке начинается новая нумерация пунктов. """
    ksTNumbDisableNumber = 3
    """ Cтрока не должна нумероваться никогда. """


class ksTextSizeEnum:  # kstextsizeenum.html
    """ ## ksTextSizeEnum – Размерный коэффициент текста """
    ksTextDefault = 0
    """ Умолчательной высоты. """
    ksTextNormal  = 1
    """ Нормальной высоты. """
    ksTextMiddle  = 2
    """ Средней высоты. """
    ksTextSmall   = 3
    """ Малой высоты. """
    ksTextBig     = 2
    """ Большой высоты. """


class ksTextStyleEnum:  # kstextstyleenum.html
    """ ## ksTextStyleEnum – Системные стили текста """
    ksTSDefault                  = 0
    """ Умолчательный стиль для данного типа объекта. """
    ksTSDrawingAnnotation        = 1
    """ Текст на чертеже. """
    ksTSSpecifications           = 2
    """ Текст для технических требований. """
    ksTSDimensionText            = 3
    """ Текст для размерной надписи. """
    ksTSSurfaceFinish            = 4
    """ Текст для шероховатости. """
    ksTSLeader1                  = 5
    """ Текст для линии выноски (позиционной . """
    ksTSLeader2                  = 6
    """ Текст для линии выноски (над/под полкой ). """
    ksTSLeader3                  = 7
    """ Текст для линии выноски (сбоку). """
    ksTSShapeDeviations          = 8
    """ Текст для отклонений формы и базы. """
    ksTSTableHeader              = 9
    """ Текст для таблицы (заголовок). """
    ksTSTableCell                = 10
    """ Текст для таблицы (ячейка). """
    ksTSSectionLine              = 11
    """ Текст для линии разреза/сечения. """
    ksTSDirectionArrow           = 12
    """ Текст для стрелки вида. """
    ksTSUnspecifiedSurfaceFinish = 13
    """ Текст для неуказанной шероховатости. """
    ksTSModificationSymbol       = 14
    """ Текст для обозначения изменения. """
    ksTSBrace                    = 15
    """ Текст для фигурной скобки. """
    ksTSUnitNumber               = 16
    """ Текст для номера узла. """
    ksTSMultiTextLeader          = 17
    """ Текст для выносной надписи. """
    ksTSUnitMarking              = 18
    """ Текст для обозначения узла. """
    ksTSAxisMark                 = 19
    """ Текст для марки координационной оси. """
    ksTSMarkOnLeader             = 20
    """ Текст для МПО (марка/позиционное обозначение с линией-выноской). """
    ksTSMarkOnLine               = 21
    """ Текст для МПО (марка/позиционное обозначение) на линии. """
    ksTSMarkInsideForm           = 22
    """ Текст для МПО (марка/позиционное обозначение) без линии выноски. """
    ksTSBOMTableName             = 23
    """ Текст для заголовков спецификации. """
    ksTSBuildingCutLine          = 24
    """ Текст для линия разреза/сечения для СПДС. """
    ksTSRprtTableHeader          = 25
    """ Текст для таблицы отчета (заголовок). """
    ksTSRprtTableCell            = 26
    """ Текст для таблицы отчета (ячейка). """
    ksTSRprtTableName            = 27
    """ Текст для таблицы отчета (наименование ) """
    ksTSTableName                = 28
    """ Текст для таблицы ( наименование ) """
    ksTSTextMark                 = 29
    """ Текст текстовой метки """


class ksThemeEnum:  # ksthemeenum.html
    """ ## ksThemeEnum - Темы Компас """
    ksThemeLight = 0
    """ Светлая """
    ksThemeDark  = 2
    """ Темная """


class ksTolerancePrefixSignEnum:  # kstoleranceprefixsignenum.html
    """ ## ksTolerancePrefixSignEnum - Знак в обозначении допуска """
    ksTPSNone        = 0
    """ Нет """
    ksTPSRadius      = 1
    """ Радиус """
    ksTPSDiametr     = 2
    """ Диаметр """
    ksTPSToleranseT  = 3
    """ Допуск в диаметральном выражении """
    ksTPSToleranseT2 = 4
    """ Допуск в радиусном выражении """


class ksToleranceRecalcsEnum:  # kstolerancerecalcsenum.html
    """ ## ksToleranceRecalcsEnum - Способ пересчета размера """
    ksTRUnknown     = 0
    """ Неопределенное состояние """
    ksTRLowerLimit  = 1
    """ По нижнему пределу """
    ksTRTopLimit    = 2
    """ По верхнему пределу """
    ksTRMiddle      = 3
    """ В середину поля допуска """
    ksTRCoefficient = 4
    """ С коэффициентом """
    ksTRUser        = 5
    """ Пользовательский вариант пересчета (Для вставки) """


class ksToleranceSuffixSignEnum:  # kstolerancesuffixsignenum.html
    """ ## ksToleranceSuffixSignEnum - Знак в обозначении базы допуска """
    ksTSNone       = 0
    """ Нет """
    ksTSToleranseM = 1
    """ Зависимый допуск """
    ksTSToleranseS = 2
    """ Независимый допуск """
    ksTSToleranseP = 3
    """ Выступающее поле допуска """


class ksUndercutDistanceTypeEnum:  # ksundercutdistancetypeenum.html
    """ ## ksUndercutDistanceTypeEnum - Способ задания размера """
    ksUCDictanceOut = 0
    """ Снаружи """
    ksUCDictanceIn  = 1
    """ Внутри """
    ksUCDictanceAll = 2
    """ Полный """


class ksUnfoldTypeEnum:  # ksunfoldtypeenum.html
    """ ## ksUnfoldTypeEnum - Способы определения длины развертки """
    ksCoefficient  = 0
    """ Коэффициент нейтрального слоя """
    ksValueBend    = 1
    """ Величина сгиба """
    ksDecreaseBend = 2
    """ Уменьшение сгиба """
    ksTableBends   = 3
    """ Таблица сгибов """


class ksValueTypeEnum:  # ksvaluetypeenum.html
    """ ## ksValueTypeEnum - Типы значения атрибута, его колонок и колонок спецификации """
    ksValueTypeUnknown = 0
    """ Неизвестный """
    ksValueTypeInteger = 1
    """ Целое со знаком """
    ksValueTypeFloat   = 2
    """ Вещественное """
    ksValueTypeString  = 3
    """ Строка """
    ksValueTypeRecord  = 4
    """ Запись """


class ksVariableRadiusBuildingTypeEnum:  # ksvariableradiusbuildingtypeenum.html
    """ ## ksVariableRadiusBuildingTypeEnum - Способ построения при скруглении с переменным радиусом """
    ksVariableRadiusOff      = 0
    """ Построение с переменным радиусом отключено """
    ksVariableRadiusByPoints = 1
    """ Построение с переменным радиусом по точкам """
    ksVariableRadiusByCurve  = 2
    """ Построение с переменным радиусом по граничной кривой """


class ksVariableTypeEnum:  # ksvariabletypeenum.html
    """ ## ksVariableTypeEnum - Тип переменной """
    ksVariableUnknown  = 0
    """ По касательной """
    ksVariableBool     = 1
    """ Логический """
    ksVariableInt      = 2
    """ Целый """
    ksVariableDouble   = 3
    """ Вещественный """
    ksVariableAngle    = 4
    """ Угловой """
    ksVariableInterval = 5
    """ Интервал """
    ksVariableFunction = 6
    """ Функция """


class ksVector3DParametersTypeEnum:  # ksvector3dparameterstypeenum.html
    """ ## ksVector3DParametersTypeEnum - Типы параметров вектора """
    ksVector3DUnknown      = 0
    """ Не определен """
    ksVector3D2Vertex      = 1
    """ По двум вершинам """
    ksVector3DCSAngle      = 2
    """ Угол в плоскости СК (Плоскости XY YZ XZ) """
    ksVector3DAxis         = 3
    """ По оси СК """
    ksVector3DCoefficients = 4
    """ По коэффициентам """
    ksVector3D2Angles      = 5
    """ По двум углам """
    ksVector3DEdge         = 6
    """ По прямолинейному ребру, оси или перпендикулярно плоскости кривой """
    ksVector3DPlane        = 7
    """ По оси цилиндра или перпендикулярно плоской грани, плоскости """
    ksVector3DSurface      = 8
    """ Перпендикулярно грани в указанной точке """
    ksVector3DCurve        = 9
    """ По базисному вектору в точке кривой (кроме прямолинейных объектов) """
    ksVector3DScreen       = 10
    """ Перпендикулярно плоскости экрана """


class ksViewProjectionType:  # ksviewprojectiontype.html
    """ ## ksViewProjectionType - Тип проекции """
    ksVPNone      = -1
    """ Не определена """
    ksVPNormalTo  = 0
    """ Нормально к """
    ksVPFront     = 1
    """ Спереди - Фронтальная плоскость """
    ksVPRear      = 2
    """ Сзади """
    ksVPUp        = 3
    """ Сверху - Горизонтальная плоскость """
    ksVPDown      = 4
    """ Снизу """
    ksVPLeft      = 5
    """ Слева - Профильная плоскость """
    ksVPRight     = 6
    """ Справа """
    ksVPIsometric = 7
    """ Изометрия """
    ksVPDimetric  = 8
    """ Диметрия """
    ksVPUnfold    = 9
    """ Развертка """
    ksVPUser      = 10
    """ Пользовательская проекция """


class ksVisibleStateEnum:  # ksvisiblestateenum.html
    """ ## ksVisibleStateEnum - Состояние видимости объекта """
    ksVSUndefined = -1
    """ Неопределенное состояние """
    ksVSVisible   = 0
    """ Видимый """
    ksVSHidden    = 1
    """ Невидимый """
    ksVSByLayer   = 2
    """ По слою """


class ksZoneDivisionTypeEnum:  # kszonedivisiontypeenum.html
    """ ## ksZoneDivisionTypeEnum - Способ разбиения зоны """
    ksZoneDivisionRegular  = 0
    """ Равномерно по осям """
    ksZoneDivisionByPlanes = 1
    """ По набору плоскостей """


class ksZoneTypeEnum:  # kszonetypeenum.html
    """ ## ksZoneTypeEnum - Способ создания зоны """
    ksZoneFree      = 0
    """ Зона без параметров (Результат операции разбиение зон). """
    ksZoneByPoints  = 1
    """ По координатам габаритного прямоугольника """
    ksZoneByObjects = 2
    """ По суммарному габариту объектов """


class ks3DLineStyle:  # ks3dlinestyle.html
    """ ## ks3DLineStyle - Стили 3D линий для отрисовки с помощью OpenGL """
    ksCS3DNoDrawing         = 0
    """ Линия не отрисовывается. """
    ksCS3DSolid             = 1
    """ Сплошная линия. """
    ksCS3DDashed            = 2
    """ Штриховая линия. """
    ksCS3DDotted            = 3
    """ Пунктирная линия. """
    ksCS3DDashDot           = 4
    """ Штрихпунктирная линия. """
    ksCS3DDashDotLDash2Dots = 5
    """ Штрихпунктирная линия (штрих и 2 точки). """


class LayersGroupWayEnum:  # layersgroupwayenum.html
    """ ## LayersGroupWayEnum - Способ группировки слоев """
    wgLayers                = 0
    """ Группировать слои """
    wgLayersCharacteristics = 1
    """ Группировать свойства слоев """


class paramType:  # paramtype.html
    """ ## paramType - Тип редактирования макроэлемента """
    MP_DBL_CLICK_OFF   = 0x01
    """ - редактирование по двойному нажатию выключено, """
    MP_HOTPOINTS       = 0x02
    """ - интерфейс hot точек включен, """
    MP_EXTERN_EDIT     = 0x04
    """ - интерфейс внешнего управления, """
    MP_PROPERTY_OBJECT = 0x08
    """ - интерфейс внешних свойств объекта. """


class ProcessTypeEnum:  # processtypeenum.html
    """ ## ProcessTypeEnum - Типы процессов КОМПАС API """
    prUnknown                             = 0
    """ Неизвестный процесс """
    prPoint                               = 10000
    """ Точка """
    prPointAlong                          = 10001
    """ Точки по кривой """
    prIntersectPoint                      = 10002
    """ Точки пересечения 2-х кривых """
    prAllIntersectPoint                   = 10003
    """ Все точки пересечения кривой """
    prPointOnDistance                     = 10004
    """ Точка на кривой на заданном расстоянии от другой точки """
    prLineSeg                             = 10005
    """ Отрезок """
    prParallelLineSeg                     = 10006
    """ Параллельный отрезок """
    prPerpendLineSeg                      = 10007
    """ Перпендикулярный отрезок """
    prTanLineSegByOutsidePnt              = 10008
    """ Касательный отрезок через внешнюю точку """
    prTanLineSegByPntOn                   = 10009
    """ Касательный отрезок через точку кривой """
    prTangent2LineSeg                     = 10010
    """ Отрезок, касательный к 2 кривым """
    prContourLineSeg                      = 10011
    """ Отрезок в контуре """
    prContourParallelLineSeg              = 10012
    """ Параллельный отрезок в контуре """
    prContourPerpendLineSeg               = 10013
    """ Перпендикулярный отрезок в контуре """
    prContourTanLineSegByOutsidePnt       = 10014
    """ Касательный отрезок через внешнюю точку в контуре """
    prLine                                = 10015
    """ Вспомогательная прямая """
    prVerticalLine                        = 10016
    """ Вертикальная прямая """
    prHorizontalLine                      = 10017
    """ Горизонтальная прямая """
    prPerpendLine                         = 10018
    """ Перпендикулярная прямая """
    prParallelLine                        = 10019
    """ Параллельная прямая """
    prTangent2Line                        = 10020
    """ Прямая, касательная к 2 кривым """
    prTanLineByPntOn                      = 10021
    """ Касательная прямая через точку кривой """
    prTanLineByOutsidePnt                 = 10022
    """ Касательная прямая через внешнюю точку """
    prBisectorLine                        = 10023
    """ Биссектриса """
    prCircle                              = 10024
    """ Окружность """
    prCircle3Points                       = 10025
    """ Окружность по 3 точкам """
    prCircleCentreOnEl                    = 10026
    """ Окружность с центром на объекте """
    prCircleTangent                       = 10027
    """ Окружность, касательная к 1 кривой """
    prCircleTangent2                      = 10028
    """ Окружность, касательная к 2 кривым """
    prCircleTangent3                      = 10029
    """ Окружность, касательная к 3 кривым """
    prCircle2Points                       = 10030
    """ Окружность по 2 точкам """
    prCircleArc                           = 10031
    """ Дуга """
    prArc3Points                          = 10032
    """ Дуга по 3 точкам """
    prArc2PointsAngle                     = 10033
    """ Дуга по 2 точкам и углу раствора """
    prArc2Points                          = 10034
    """ Дуга по 2 точкам """
    prArcTangent                          = 10035
    """ Дуга, касательная к кривой """
    prContourArc                          = 10036
    """ Дуга по трем точкам в контуре """
    prContourConArc                       = 10037
    """ Сопряженная дуга в контуре """
    prEllipse                             = 10038
    """ Эллипс """
    prEllipseGabDiagonal                  = 10039
    """ Эллипс по диагонали прямоугольника """
    prEllipseTangent2                     = 10040
    """ Эллипс, касательный к 2 кривым """
    prEllipseCentre3Points                = 10041
    """ Эллипс по центру и 3 точкам """
    prEllipseParallel3Points              = 10042
    """ Эллипс по 3 вершинам параллелограмма """
    prEllipseParallelCentre2Points        = 10043
    """ Эллипс по центру, середине стороны и вершине параллелограмма """
    prEllipseGabCentrePoint               = 10044
    """ Эллипс по центру и вершине прямоугольника """
    prBezier                              = 10045
    """ Кривая Безье """
    prContourBezier                       = 10046
    """ Сплайн в контуре """
    prPolyline                            = 10047
    """ Ломаная """
    prNurbs                               = 10048
    """ NURBS-кривая """
    prContourNurbs                        = 10049
    """ NURBS-кривая в контуре """
    prRectangle                           = 10050
    """ Прямоугольник """
    prRectangleCentrePoint                = 10051
    """ Прямоугольник по центру и вершине """
    prPolygon                             = 10052
    """ Многоугольник """
    prEquidToObj                          = 10053
    """ Эквидистанта кривой """
    prAssemblyEquid                       = 10054
    """ Эквидистанта по стрелке """
    prLineDimension                       = 10055
    """ Линейный размер """
    prCommonBaseLineDim                   = 10056
    """ Линейный размер от общей базы """
    prChainLineDim                        = 10057
    """ Линейный цепной размер """
    prCommonLineLineDim                   = 10058
    """ Линейный размер с общей размерной линией """
    pr2ObjectsLineDim                     = 10059
    """ Линейный размер от отрезка до точки """
    prCutLineDimension                    = 10060
    """ Линейный размер с обрывом """
    prAngleDimension                      = 10061
    """ Угловой размер """
    prCommonBaseAngleDim                  = 10062
    """ Угловой размер от общей базы """
    prChainAngleDim                       = 10063
    """ Угловой цепной размер """
    prCommonLineAngleDim                  = 10064
    """ Угловой размер с общей размерной линией """
    prCutAngleDimension                   = 10065
    """ Угловой размер с обрывом """
    prRadialDimension                     = 10066
    """ Радиальный размер """
    prDiametralDimension                  = 10068
    """ Диаметральный размер """
    prArcDimension                        = 10069
    """ Размер дуги окружности """
    prOrdinateDimension                   = 10070
    """ Размер высоты """
    prLeader                              = 10071
    """ Линия-выноска """
    prBrandLeader                         = 10072
    """ Знак клеймения """
    prMarkLeader                          = 10073
    """ Знак маркировки """
    prPositionLeader                      = 10074
    """ Обозначение позиций """
    prChangeLeader                        = 10075
    """ Знак изменения """
    prHatch                               = 10076
    """ Штриховка """
    prText                                = 10077
    """ Ввод текста """
    prTable                               = 10078
    """ Ввод таблицы """
    prRough                               = 10079
    """ Шероховатость """
    prBase                                = 10080
    """ База """
    prCutLine                             = 10081
    """ Линия разреза """
    prViewPointer                         = 10082
    """ Стрелка взгляда """
    prRemoteElement                       = 10083
    """ Выносной элемент """
    prAxedLineSegment                     = 10084
    """ Осевая линия по двум точкам """
    prCentreMarker                        = 10085
    """ Обозначение центра """
    prAssemblyContour                     = 10086
    """ Собрать контур """
    prFormTolerance                       = 10087
    """ Допуск формы """
    prInsertRaster                        = 10088
    """ Вставить растровый объект """
    prMakeMacro                           = 10089
    """ Объединить в макроэлемент """
    prInsertFragment                      = 10090
    """ Вставить внешний фрагмент """
    prCreateSheetView                     = 10091
    """ Создать вид """
    prInsertOLEObject                     = 10092
    """ Вставить OLE-объект """
    prCreateStandartSheetView             = 10093
    """ Создать стандартные виды """
    prCreateSectionSheetView              = 10094
    """ Создать вид разрез/сечение """
    prCreateArbitrarySheetView            = 10095
    """ Создать произвольный вид """
    prCreateProjectionSheetView           = 10096
    """ Создать проекционный вид """
    prCreateArrowSheetView                = 10097
    """ Создать вид по стрелке """
    prCreateRemoteSheetView               = 10098
    """ Создать вид - выносной элемент """
    prCreateLocalSheetView                = 10099
    """ Создать местный вид """
    prCreateLocalSectionSheetView         = 10100
    """ Создать местный вид-разрез """
    prCreateBrokenSheetView               = 10101
    """ Создать вид с разрывом """
    prContour                             = 10102
    """ Непрерывный ввод объектов """
    prChamfer                             = 10103
    """ Фаска между пересекающимися объектами """
    prChamferPolyContour                  = 10104
    """ Фаска на углах объекта """
    prFillet                              = 10105
    """ Скругление между пересекающимися объектами """
    prFilletPolyContour                   = 10106
    """ Скругление на углах объекта """
    prProjectionObject                    = 10107
    """ Спроецировать объект на плоскость эскиза """
    prSmartDimension                      = 10108
    """ Авторазмер """
    prSmartAxedLineSegment                = 10109
    """ Автоосевая """
    prMeasurePointProperties              = 10110
    """ Измерить координаты точки в локальной системе координат """
    prMeasureDistance2Points              = 10111
    """ Измерить расстояние между двумя точками """
    prMeasureDistance2PointsByCurve       = 10112
    """ Измерить расстояние между двумя точками на кривой """
    prMeasureDistancePointObject          = 10113
    """ Измерить расстояние от кривой до точки """
    prMeasureDistance2Curves              = 10114
    """ Измерить расстояние между двумя кривыми """
    prMeasureAngle2Lines                  = 10115
    """ Измерить угол между двумя прямыми/отрезками """
    prMeasureAngle3Points                 = 10116
    """ Измерить угол, заданный 3 точками """
    prPerimeter                           = 10117
    """ Измерить длину кривой и суммарную длину """
    prMeasureArea                         = 10118
    """ Измерить площадь """
    prMix                                 = 10119
    """ Расчет массово-центровочных характеристик плоских фигур """
    prMix3DRevolution                     = 10120
    """ Расчет массово-центровочных характеристик тел вращения """
    prMix3DExtrision                      = 10121
    """ Расчет массово-центровочных характеристик тел выдавливания """
    prObjectShift                         = 10122
    """ Сдвиг выделенных объектов """
    prObjectShiftAngleLen                 = 10123
    """ Сдвиг с заданием угла и расстояния """
    prObjectRotate                        = 10124
    """ Поворот выделенных объектов """
    prObjectScale                         = 10125
    """ Масштабирование выделенных объектов """
    prObjectSymmetry                      = 10126
    """ Симметричное отображение выделенных объектов """
    prObjectMultiply                      = 10127
    """ Копирование выделенных объектов """
    prObjectMultiplyByCurve               = 10128
    """ Копирование выделенных объектов по кривой """
    prObjectMultiplyByCircle              = 10129
    """ Копирование выделенных объектов по окружности """
    prObjectMultiplyByRing                = 10130
    """ Копирование выделенных объектов по концентрической сетке """
    prObjectMultiplyByMesh                = 10131
    """ Копирование выделенных объектов по сетке """
    prMoveDeformation                     = 10132
    """ Деформация сдвигом """
    prRotateDeformation                   = 10133
    """ Деформация поворотом """
    prScaleDeformation                    = 10134
    """ Деформация масштабированием """
    prCutObjectPart                       = 10135
    """ Усечь кривую """
    prCutObjectPartBy2Points              = 10136
    """ Усечь кривую двумя точками """
    prJustify                             = 10137
    """ Выровнять кривую по границе """
    prRemoveChamfer                       = 10138
    """ Удалить фаску или скругление """
    prBreakCurve                          = 10139
    """ Разбить кривую на две части """
    prBreakCurveNParts                    = 10140
    """ Разбить кривую на N равных частей """
    prBlackBox                            = 10141
    """ Очистить заданную область """
    prConvertToNurbs                      = 10142
    """ Преобразовать геометрический объект или текст в NURBS-кривые """
    prParametricHorizontal                = 10143
    """ Установить горизонтальность отрезка или прямой """
    prParametricVertical                  = 10144
    """ Установить вертикальность отрезка или прямой """
    prParametricXAlign                    = 10145
    """ Выровнять по горизонтали две характерные точки объектов """
    prParametricYAlign                    = 10146
    """ Выровнять по вертикали две характерные точки объектов """
    prParametricMergePoints               = 10147
    """ Объединить две точки """
    prParametricPointOnCurve              = 10148
    """ Задать размещение точки на кривой """
    prParametricPointSymmetry             = 10149
    """ Симметрия 2 точек относительно оси """
    prParametricParallel                  = 10150
    """ Установить параллельность двух прямых и/или отрезков """
    prParametricNormal                    = 10151
    """ Установить перпендикулярность двух прямых и/или отрезков """
    prParametricColinear                  = 10152
    """ Установить коллинеарность двух прямых и/или отрезков """
    prParametricTangent                   = 10153
    """ Установить касание двух кривых """
    prParametricFixPoint                  = 10154
    """ Зафиксировать координаты точки """
    prParametricEqualRadiuses             = 10155
    """ Установить равенство радиусов двух дуг и/или окружностей """
    prParametricEqualLength               = 10156
    """ Установить равенство длин двух отрезков """
    prParametricFixDimension              = 10157
    """ Зафиксировать значение размера """
    prParametricChangeDimension           = 10158
    """ Установить значение размера """
    prParametricSelected                  = 10159
    """ Параметризовать выделенные объекты """
    prParametricDeleteObjConstraints      = 10160
    """ Показать/удалить ограничения """
    prParametricDeleteAllConstraints      = 10161
    """ Удалить все ограничения """
    prSelectObject                        = 10162
    """ Выделить отдельный объект """
    prSelectLayer                         = 10163
    """ Выделить слой указанием лежащего на этом слое объекта """
    prSelectSheetView                     = 10164
    """ Выделить вид указанием точки внутри этого вида """
    prSelectWithRect                      = 10165
    """ Выделить объекты внутри прямоугольной рамки """
    prSelectOutSideRect                   = 10166
    """ Выделить объекты снаружи от прямоугольной рамки """
    prSelectWithCutRect                   = 10167
    """ Выделить объекты, пересекающиеся с прямоугольной рамкой """
    prSelectWithCutPolyline               = 10168
    """ Выделить объекты, пересекающиеся с ломаной """
    prExcludeObject                       = 10169
    """ Исключить отдельный объект """
    prExcludeLayer                        = 10170
    """ Исключить слой указанием лежащего на этом слое объекта """
    prExcludeSheetView                    = 10171
    """ Исключить вид указанием точки внутри этого вида """
    prExcludeWithRect                     = 10172
    """ Исключить объекты внутри прямоугольной рамки """
    prExcludeOutSideRect                  = 10173
    """ Исключить объекты снаружи от прямоугольной рамки """
    prExcludeWithCutRect                  = 10174
    """ Исключить объекты, пересекающиеся с прямоугольной рамкой """
    prExcludeWithCutPolyline              = 10175
    """ Исключить объекты, пересекающиеся с ломаной """
    prSmartLine                           = 10176
    """ Автолиния """
    prBrace                               = 10177
    """ Фигурная скобка """
    prAutoDimL                            = 10178
    """ Авторазмер - ввод линейного размера """
    prAutoDimA                            = 10179
    """ Авторазмер - ввод углового размера """
    prAutoDimD                            = 10180
    """ Авторазмер - ввод диаметрального размера """
    prAutoDimR                            = 10181
    """ Авторазмер - ввод радиального размера """
    prAutoDimLToPoint                     = 10182
    """ Авторазмер - ввод линейного размера от отрезка до точки """
    prAutoDimLBreak                       = 10183
    """ Авторазмер - ввод линейного размера с обрывом от отрезка до отрезка осевой линией """
    prAutoDimABreak                       = 10184
    """ Авторазмер - ввод углового размера с обрывом от отрезка до отрезка осевой линией """
    prTechnicalDemandPlacement            = 10185
    """ Технические требования-размещение """
    prDirectAxis                          = 10186
    """ Прямая координационная ось """
    prArcAxis                             = 10187
    """ Дуговая координационная ось """
    prCircleAxis                          = 10188
    """ Круговая координационная ось """
    prWaveLine                            = 10189
    """ Волнистая линия """
    prMarkOnLDRPosNum                     = 10190
    """ Марка/Позиционное обозначение на линии выноске """
    prMarkWoLDRPosNum                     = 10191
    """ Марка/Позиционное обозначение без линии выноски """
    prKnotNumber                          = 10192
    """ Номер узла """
    prUnitMarking                         = 10193
    """ Обозначение узла """
    prCutUnitMarking                      = 10194
    """ Обозначение узла в сечении """
    prMultiTextLeader                     = 10195
    """ Выносная надпись к многослойным конструкциям """
    prColouring                           = 10196
    """ Заливка """
    prMultiLine                           = 10197
    """ Мультилиния """
    prBuildingCutLine                     = 10198
    """ Линия разреза/сечения для СПДС """
    prBrokenLine                          = 10199
    """ Линия обрыва с изломами """
    prCreateReport                        = 10200
    """ Создать отчет """
    prCreateAttachedLeaders               = 10201
    """ Редактировать оформление составного объекта """
    prEditProperties                      = 10202
    """ Процесс редактирования свойств объекта или документа """
    prParametricBisector                  = 10203
    """ Создание ограничения биссектриса """
    prParametricFixedLenght               = 10204
    """ Фиксировать длину """
    prParametricFixedAngle                = 10205
    """ Фиксировать угол """
    prParametricPointOnCurveMiddle        = 10206
    """ Точка на середине кривой """
    prTechnicalDemand                     = 10207
    """ Ввод\\Редактирование технических требований """
    prSpecRough                           = 10208
    """ Ввод\\Редактирование неуказанной шероховатости """
    prMoveSpecRough                       = 10209
    """ Ручное размещение неуказанной шероховатости """
    prDeleteHistory                       = 10210
    """ Удаление истории построения """
    prUndo                                = 10211
    """ Undo """
    prRedo                                = 10212
    """ Redo """
    prEmbodimentsReport                   = 10213
    """ Создать таблицу исполнений """
    prArrayParamReport                    = 10214
    """ Создать таблицу параметров массива """
    prConicCurve                          = 10215
    """ Коническая кривая """
    prConicCurve4Or5Point                 = 10216
    """ Коническая кривая по 4 или 5 точкам """
    prMarkOnLeader                        = 10217
    """ Марка/позиционное обозначение с линией-выноской """
    prCutLineMultiple                     = 10218
    """ Линия сложного разреза/сечения """
    prBuildingCutLineMultiple             = 10219
    """ Линия сложного разреза/сечения для СПДС """
    prCircularCentres                     = 10220
    """ Круговая сетка центров """
    prLinearCentres                       = 10221
    """ Линейная сетка центров """
    prSelectWithPolyline                  = 10222
    """ Выделить объекты замкнутой ломаной """
    prBaseExtrusion                       = 20000
    """ Базовая операция выдавливания """
    prBossExtrusion                       = 20001
    """ Приклеивание выдавливанием """
    prCutExtrusion                        = 20002
    """ Вырезать выдавливанием """
    prExtrusionSurface                    = 20003
    """ Поверхность выдавливания """
    prBaseRotated                         = 20004
    """ Базовая операция вращения """
    prBossRotated                         = 20005
    """ Приклеивание вращением """
    prCutRotated                          = 20006
    """ Вырезать вращением """
    prRotatedSurface                      = 20007
    """ Поверхность вращения """
    prBaseEvolution                       = 20008
    """ Кинематическая операция """
    prBossEvolution                       = 20009
    """ Приклеить кинематически """
    prCutEvolution                        = 20010
    """ Вырезать кинематически """
    prEvolutionSurface                    = 20011
    """ Кинематическая поверхность """
    prBaseLoft                            = 20012
    """ Базовая операция по сечениям """
    prBossLoft                            = 20013
    """ Приклеивание по сечениям """
    prCutLoft                             = 20014
    """ Вырезать по сечениям """
    prLoftSurface                         = 20015
    """ Поверхность по сечениям """
    prFillet3D                            = 20016
    """ Операция "фаска" """
    prChamfer3D                           = 20017
    """ Операция "скругление" """
    prCutByPlane                          = 20018
    """ Операция "сечение поверхностью" """
    prCutBySketch                         = 20019
    """ Операция "сечение эскизом" """
    prMeshCopy                            = 20020
    """ Операция копирования по сетке """
    prCircularCopy                        = 20021
    """ Операция копирования по концентрической сетке """
    prCurveCopy                           = 20022
    """ Операция копирования по кривой """
    prMirrorCopy                          = 20023
    """ Операция "зеркальный массив" """
    prMirrorAllCopy                       = 20024
    """ Операция "зеркально отразить все" """
    prDerivativePartArray                 = 20025
    """ Операция массив по образцу для сборки """
    prMeshPartArray                       = 20026
    """ Операция массив по сетке для сборки """
    prCircularPartArray                   = 20027
    """ Операция массив по концентрической сетке для сборки """
    prCurvePartArray                      = 20028
    """ Операция массив по кривой для сборки """
    prIncline                             = 20029
    """ Операция "уклон" """
    prShell                               = 20030
    """ Операция "оболочка" """
    prRib                                 = 20031
    """ Операция "ребро жесткости" """
    prHole                                = 20032
    """ Отверстие """
    prThread                              = 20033
    """ Условное изображение резьбы """
    prCPlaneOffset                        = 20034
    """ Смещенная плоскость """
    prCPlane3Points                       = 20035
    """ Плоскость по 3-м точкам """
    prCPlaneAngle                         = 20036
    """ Плоскость под углом """
    prCPlaneEdgePoint                     = 20037
    """ Плоскость через ребро и вершину """
    prCPlaneParallel                      = 20038
    """ Плоскость через вершину параллельно другой плоскости """
    prCPlanePerpendicular                 = 20039
    """ Плоскость через вершину перпендикулярно ребру """
    prCPlaneNormalToSurface               = 20040
    """ Нормальная плоскость """
    prCPlaneTangentToSurface              = 20041
    """ Касательная плоскость """
    prCPlaneLineToEdge                    = 20042
    """ Плоскость через ребро параллельно/перпендикулярно другому ребру """
    prCPlaneLineToFlat                    = 20042
    """ Плоскость через ребро параллельно/перпендикулярно грани """
    prCAxis2Points                        = 20043
    """ Ось по двум точкам """
    prCAxis2Planes                        = 20044
    """ Ось по двум плоскостям """
    prCAxisConeface                       = 20045
    """ Ось конической грани """
    prCAxisEdge                           = 20046
    """ Ось, проходящая через ребро """
    prCAxisOperation                      = 20047
    """ Ось операции """
    prPolyline3D                          = 20048
    """ Ломаная """
    prSpline3D                            = 20049
    """ Сплайн """
    prCylindricSpiral                     = 20050
    """ Цилиндрическая спираль """
    prConicSpiral                         = 20051
    """ Коническая спираль """
    prImportedSurface                     = 20052
    """ Импортированная поверхность """
    prInsertScetch                        = 20053
    """ Эскиз из библиотеки """
    prEditScetch                          = 20054
    """ Редактировать эскиз """
    prOrientationScetch                   = 20055
    """ Разместить эскиз на плоскости """
    prInPlacePartEdit                     = 20056
    """ Редактировать компонент на месте """
    prOutPlacePartEdit                    = 20057
    """ Редактировать компонент в своем окне """
    prAddDetail                           = 20058
    """ Вставить деталь в сборку """
    prAddAssembly                         = 20059
    """ Вставить сборку в сборку """
    prMateCoincident                      = 20060
    """ Сопряжения компонентов - Совпадение """
    prMateConcentric                      = 20061
    """ Сопряжения компонентов - Соосность """
    prMateParallel                        = 20062
    """ Сопряжения компонентов - Параллельность """
    prMatePerpendicular                   = 20063
    """ Сопряжения компонентов - Перпендикулярность """
    prMateOnDistance                      = 20064
    """ Сопряжения компонентов - На расстоянии """
    prMateOnAngle                         = 20065
    """ Сопряжения компонентов - Под углом """
    prMateTangent                         = 20066
    """ Сопряжения компонентов - Касание """
    prPartVariables                       = 20067
    """ Просмотр и редактирование переменных """
    prCopyBilletPart                      = 20068
    """ Создание детали путем копирования детали из другого файла """
    prMakeMoldCavity                      = 20069
    """ Вычесть компоненты """
    prMakeUnionComps                      = 20070
    """ Объединить компоненты """
    prAddPartFromFile                     = 20071
    """ Добавить компонент из файла """
    prMovePart                            = 20072
    """ Переместить компонент """
    prRotatePartWC                        = 20073
    """ Повернуть компонент вокруг центральной точки """
    prRotatePartAxis                      = 20074
    """ Повернуть компонент вокруг оси """
    prRotatePartPoint                     = 20075
    """ Повернуть компонент вокруг точки """
    prMakeSplitLine                       = 20076
    """ Построение линии разъема """
    prMeasureDistance3D                   = 20077
    """ Измерить расстояние и угол """
    prMeasurePerimeter3D                  = 20078
    """ Измерить длину ребра """
    prMeasureArea3D                       = 20079
    """ Измерить площадь """
    prMeasureMix3D                        = 20080
    """ Вычисление массово-центровочных характеристик """
    prMeasureInterferenceVolumes          = 20081
    """ Проверка коллизий """
    prBaseShMtSolid                       = 20082
    """ Листовое тело """
    prShMtBend                            = 20083
    """ Построение сгиба вдоль ребра листового тела """
    prShMtCombinedBend                    = 20084
    """ Построение сгибов вдоль ребер листового тела по эскизу """
    prShMtBendLine                        = 20085
    """ Создание сгиба в листовом теле по прямолинейному объекту """
    prShMtBendHook                        = 20086
    """ Создание подсечки в листовом теле по прямолинейному объекту """
    prShMtHole                            = 20087
    """ Построение круглого отверстия на грани листового тела """
    prShMtCut                             = 20088
    """ Построение выреза на грани листового тела """
    prBaseShMtPlate                       = 20089
    """ Добавление пластины к листовому телу """
    prShMtClosedCorner                    = 20090
    """ Замыкание углов двух смежных элементов листового тела """
    prShMtBendStraighten                  = 20091
    """ Разгибание элементов листового тела """
    prShMtBendBended                      = 20092
    """ Сгибание элементов листового тела """
    prShMtBendParamUnfold                 = 20093
    """ Настроить параметры развертки листового тела """
    prPatchSurface                        = 20094
    """ Создание поверхности по замкнутому контуру """
    prSewSurface                          = 20095
    """ Сшивка поверхностей """
    prMakeFaceRemover                     = 20096
    """ Удалить грани """
    prCPlaneMiddle                        = 20097
    """ Средняя плоскость """
    prCPointControl                       = 20098
    """ Контрольная точка """
    prCPointConjunctive                   = 20099
    """ Присоединительная точка """
    prCAggregateOper                      = 20100
    """ Булева операция """
    prCPlaneLineToFlat                    = 20101
    """ Плоскость через ребро параллельно/перпендикулярно грани """
    prPoint3D                             = 20103
    """ Конструктивная 3D точка """
    prLocalCoordinateSystem               = 20104
    """ Локальная система координат """
    prLineDimention3DPlane                = 20105
    """ Размер по двум объектам и планару. """
    prLineDimention3D                     = 20106
    """ Размер по ребру и точке """
    prAngleDimention3D                    = 20107
    """ Угловой размер """
    prRough3D                             = 20108
    """ Шероховатость """
    prTolerance3D                         = 20109
    """ Допуск формы и расположения поверхностей """
    prBrandLeader3D                       = 20110
    """ Клеймение """
    prMarkerLeader3D                      = 20111
    """ Маркировка """
    prPositionLeader3D                    = 20112
    """ Обозначение позиции """
    prBase3D                              = 20113
    """ База """
    prLeader3D                            = 20114
    """ Линия-выноска """
    prSaveBody                            = 20115
    """ Процесс сохранения тела в деталь """
    prCreateSketch                        = 20116
    """ Процесс создания\\редактирования эскиза """
    prMeasureInformation                  = 20117
    """ Информация об объекте """
    prEquidistant3D                       = 20118
    """ Эквидистанта 3D """
    prChoiceOperationResult               = 20119
    """ Выбор результата 3D операции """
    prChoiceBodyUnit                      = 20120
    """ Выбор частей тела """
    prSelectCurrentCS                     = 20121
    """ Выбрать текущую СК в модели """
    prShmtRuledOperation                  = 20122
    """ Обечайка """
    prArc3D                               = 20123
    """ Дуга в пространстве """
    prConnectCurve                        = 20124
    """ Cопряжения пространственных кривых – соединение """
    prTrimCurve                           = 20125
    """ Cопряжения пространственных кривых – обрезка """
    prFilletCurve                         = 20126
    """ Cопряжения пространственных кривых – скругление """
    prSwithOwnCS                          = 20127
    """ Перенести в СК модели """
    prScalingOperation                    = 20128
    """ Маштабирование тела или поверхности """
    prPointDrivenPattern                  = 20129
    """ Массив пространственных объектов по точкам """
    prNurbs3DByObjects                    = 20130
    """ 3D сплайн по объектам """
    prCurveOperationCrossing              = 20131
    """ Кривая пересечения пространственных объектов """
    prConvertToNurbsSurface3D             = 20133
    """ NURBS-поверхность по объектам """
    prNurbsSurface3DByPoints              = 20134
    """ NURBS-поверхность по точкам """
    prNurbsSurface3DByCurves              = 20135
    """ NURBS-поверхность по сети кривых """
    prArrayPointsFromFile                 = 20136
    """ Массив пространственных точек из файла """
    prArrayPointsOnCurve                  = 20137
    """ Массив пространственных точек вдоль кривой """
    prArrayPointsByCloud                  = 20138
    """ NURBS-поверхность по облаку точек """
    prOffsetSurface                       = 20139
    """ Эквидистанта поверхности """
    prAuxObjectMultiplyByMesh             = 20140
    """ Копирование вспомогательной геометрии в пространстве по плоской параллелограмной сетке """
    prAuxObjectMultiplyByRing             = 20141
    """ Копирование вспомогательной геометрии в пространстве по плоской концентрической сетке """
    prAuxObjectMultiplyByCurve            = 20142
    """ Копирование вспомогательной геометрии в пространстве вдоль кривой """
    prTrimmedSurface                      = 20143
    """ Усечение поверхности по объекту """
    prSurfaceToBody                       = 20144
    """ Создание тела из поверхности приданием ей толщины """
    prAxisByDirection                     = 20145
    """ Ось через вершину по объекту """
    prRuledSurface                        = 20146
    """ Линейчатая поверхность """
    prExtensionSurface                    = 20147
    """ Продление поверхности """
    prCPlaneTangentAtPoint                = 20148
    """ Плоскость, касательная к грани в точке """
    prCPlaneAtCurve                       = 20149
    """ Плоскость через плоскую кривую """
    prArrayPintsOnSyrface                 = 20150
    """ Группа точек по поверхности """
    prAuxObjectMultiplyMirror             = 20151
    """ Зеркальная копия вспомогательной геометрии в пространстве """
    prOutlineCurve                        = 20152
    """ Построение линии очерка поверхности """
    prSplineOnSurface                     = 20153
    """ Сплайн на поверхности """
    prPartsPointDrivenPattern             = 20154
    """ Массив компонентов по точкам """
    prChooseLinearPattern                 = 20155
    """ Процесс выбора трехмерных объектов для копирования По сетке """
    prChooseCircularPattern               = 20156
    """ Процесс выбора трехмерных объектов для копирования По концентрической сетке """
    prChooseCurvePattern                  = 20157
    """ Процесс выбора трехмерных объектов для копирования По кривой """
    prChoosePointDrivenPattern            = 20158
    """ Процесс выбора трехмерных объектов для копирования По точкам """
    prChooseTablePattern                  = 20159
    """ Процесс выбора трехмерных объектов для копирования По таблице """
    prChooseMirrorPattern                 = 20160
    """ Процесс выбора трехмерных объектов для построении симметричной копии """
    prTablePattern                        = 20161
    """ Массив операций по таблице """
    prAuxTablePattern                     = 20162
    """ Массив вспомогательной геометрии по таблице """
    prPartsTablePattern                   = 20163
    """ Массив компонентов по таблице """
    prAuxPointDrivenPattern               = 20164
    """ Массив вспомогательной геометрии по точкам """
    prBodiesLinearPattern                 = 20165
    """ Массив тел по сетке """
    prBodiesCircularPattern               = 20166
    """ Массив тел по концентрической сетке """
    prBodiesCurvePattern                  = 20167
    """ Массив тел по кривой """
    prBodiesPointDrivenPattern            = 20168
    """ Массив тел по точкам """
    prBodiesTablePattern                  = 20169
    """ Массив тел по таблице """
    prContour3D                           = 20170
    """ Контур 3D """
    prCurveOper2Projection                = 20171
    """ Пространственная кривая по 2 проекциям """
    prCurveByLaw                          = 20172
    """ Пространственная кривая по закону """
    prBodyReposition                      = 20173
    """ Изменить положение тела или поверхности """
    prIsoparamCurve                       = 20174
    """ Изопараметрическая пространственная кривая """
    prIsoparamCurveArr                    = 20175
    """ Группа изопараметрических кривых на поверхности """
    prBindingMesh                         = 20176
    """ Редактировать как сплайн по сетке """
    prSaveBodyAs                          = 20177
    """ Сохранение тела в деталь """
    prBlendSurface                        = 20178
    """ Поверхность соединения """
    prLineSegment3D                       = 20179
    """ Отрезок 3D """
    prEmbodiment                          = 20180
    """ Создание исполнения """
    prCreateSpecificationObjects          = 20181
    """ Создать объекты спецификации """
    prDeleteSpecificationObjects          = 20182
    """ Удалить объекты спецификации """
    prCreateSpecificationFromAssembly     = 20183
    """ Создать спецификацию по сборке """
    prSpecRough3D                         = 20184
    """ Ввод\\Редактирование неуказанной шероховатости 3D """
    prShmtRuledCowling                    = 20185
    """ Линейчатая обечайка """
    prAddLocalPartFromFile                = 20187
    """ Добавить локальную деталь из файла """
    prAddLayoutGeometryFromFile           = 20188
    """ Добавить компоновочную геометрию """
    prAddBilletPartFromFile               = 20189
    """ Добавить деталь заготовку """
    prMateSymmetry                        = 20190
    """ Сопряжения компонентов - Симметрия """
    prMateDependent                       = 20191
    """ Сопряжения компонентов - Зависимое положение """
    prMateCamGear                         = 20192
    """ Сопряжения компонентов - Кулачковый механизм. Кулачек-толкатель """
    prMateRotation                        = 20193
    """ Сопряжения компонентов - Вращение-Вращение """
    prMateRotationTransfer                = 20194
    """ Сопряжения компонентов - Вращение-Перемещение """
    prTechnicalDemand3D                   = 20195
    """ Ввод\\Редактирование технических требований 3D """
    prHoleSimple                          = 20196
    """ Отверстие простое """
    prHoleCounterbore                     = 20197
    """ Отверстие с цековкой """
    prHoleCountersinking                  = 20198
    """ Отверстие с зенковкой """
    prHoleCounterdrill                    = 20199
    """ Отверстие с зенковкой и цековкой """
    prHoleConic                           = 20200
    """ Отверстие коническое """
    prPoint3DCoord                        = 20201
    """ Конструктивная 3D точка. Точка по координатам """
    prPoint3DDisplace                     = 20202
    """ Конструктивная 3D точка. Точка переносом """
    prPoint3DIntersect                    = 20203
    """ Конструктивная 3D точка. Точка на пересечении """
    prPoint3DCurve                        = 20204
    """ Конструктивная 3D точка. Точка на кривой """
    prPoint3DSurface                      = 20205
    """ Конструктивная 3D точка. Точка на поверхности """
    prPoint3DCenter                       = 20206
    """ Конструктивная 3D точка.Точка в центре """
    prPoint3DProjection                   = 20207
    """ Конструктивная 3D точка. Точка в центре """
    prPoint3DCylindrCoord                 = 20208
    """ Конструктивная 3D точка. Цилиндрические координаты """
    prPoint3DSphericCoord                 = 20209
    """ Конструктивная 3D точка. Сферические координаты """
    prShMtBendObject                      = 20210
    """ Листовой металл, сгибы листовых операций """
    prShMtClocingPressForming             = 20211
    """ Листовой металл, закрытая штамповка """
    prShMtOpeningPressForming             = 20212
    """ Листовой металл, открытая штамповка """
    prShMtShoulder                        = 20213
    """ Листовой металл, буртик """
    prShMtJalousie                        = 20214
    """ Листовой металл, жалюзи """
    prShMtRib                             = 20215
    """ Ребро усиления """
    prAxis3D                              = 20216
    """ Осевая линия """
    prFullFillet                          = 20217
    """ Полное скругление """
    prRestoredSurface                     = 20218
    """ Восстановленная поверхность """
    prCurvatureGraph                      = 20219
    """ График кривизны """
    prContinuityCheck                     = 20220
    """ Проверка непрерывности """
    prSectionAnalysis                     = 20221
    """ Сетка графиков кривизны """
    prArcDimension3D                      = 20222
    """ Размер дуги окружности 3D """
    prSketchArcDimension3D                = 20223
    """ Управляющий размер дуги окружности эскиза 3D """
    prSheetMetalPunch                     = 20224
    """ Листовой металл, штамповка телом """
    prSheetMetalFlanging                  = 20225
    """ Листовой металл, отбортовка """
    prMakeFaceMover                       = 20226
    """ Переместить грани """
    prSplitSolid                          = 20227
    """ Операция “Разрезать” """
    prSheetMetalConvertFromBody           = 20228
    """ Операция “Преобразования в листовое тело” """
    prConicSectionSurface                 = 20229
    """ Поверхность конического сечения """
    prConicCurve3DVertexAndHeight         = 20230
    """ Коническая кривая по вершине и дискриминанту """
    prConicCurve3DVertexAndPointOnCurve   = 20231
    """ Коническая кривая по вершине и точке на кривой """
    prConicCurve3DTangentsAndHeight       = 20232
    """ Коническая кривая по касательным и дискриминанту """
    prConicCurve3DTangentsAndPointOnCurve = 20233
    """ Коническая кривая по касательным и точке на кривой """
    prAddDummyPartFromFile                = 20234
    """ Добавить макет компонента из файла """
    prExtensionCurve                      = 20235
    """ Продление кривой """
    prPoint3DBetweenPoints                = 20236
    """ Конструктивная 3D точка. Между точками """
    prZoomWindow                          = 32411
    """ Увеличить масштаб окном """
    prMoveView                            = 32418
    """ Сдвинуть изображение """
    prPanoramaView                        = 32419
    """ Приблизить/отдалить изображение """
    prRotateView                          = 32420
    """ Повернуть изображение (для 3D-окна) """
    prEditSelectedObject                  = 35736
    """ Редактировать выделенный объект """
    prEditSelectedObject3D                = 40707
    """ Редактировать выделенный 3D объект """
    prEditCopy                            = 0xE122
    """ Копировать в буфер обмена """
    prEditCut                             = 0xE123
    """ Вырезать в буфер обмена """
    prEditPaste                           = 0xE125
    """ Вставить из буфера обмена """


class PropertyControlNameVisibility:  # propertycontrolnamevisibility.html
    """ ## PropertyControlNameVisibility - Видимость имени элемента управления на Панели свойств """
    ksNameAlwaysVisible     = 0
    """ Всегда показывать имя элемента управления на Панели свойств. """
    ksNameHorizontalVisible = 1
    """ Показывать имя элемента управления на горизонтальной Панели. """
    ksNameVerticalVisible   = 2
    """ Показывать имя элемента управления на вертикальной Панели. """
    ksNameNoVisible         = 3
    """ Не показывать имя элемента управления. """


class PropertyManagerLayout:  # propertymanagerlayout.html
    """ ## PropertyManagerLayout - Положение панели свойств """
    pmAlignRight        = 3
    """ Панель прикреплена справа """
    pmAlignLeft         = 4
    """ Панель прикреплена слева """
    pmAlignRightInGroup = 5
    """ Панель прикреплена справа в группе """
    pmAlignLeftInGroup  = 6
    """ Панель прикреплена слева в группе """


class SaveDocumentVersion:  # savedocumentversion.html
    """ ## SaveDocumentVersion - Способ записи документа """
    sdv_Prev            = -1
    """ Предыдущую версию """
    sdv_Current         = 0
    """ Текущую версию (обычный режим) """
    sdv_Kompas_5_11_R03 = 1
    """ Версия KOMPAS_5_11_R03_VERSION """
    sdv_Last            = 1
    """ Последняя версия """
    sdv_Kompas_6_0      = 2
    """ Версия KOMPAS_6_0_VERSION """
    sdv_Kompas_6_Plus   = 3
    """ Версия KOMPAS_6_PLUS_VERSION """
    sdv_Kompas_7_0      = 4
    """ Версия KOMPAS_7_0_VERSION """
    sdv_Kompas_7_Plus   = 5
    """ Версия KOMPAS_7_PLUS_VERSION """
    sdv_Kompas_8_0      = 6
    """ Версия KOMPAS_8_0 """


class SeparatorTypeEnum:  # separatortypeenum.html
    """ ## SeparatorTypeEnum - Типы элемента управления Панели свойств - "разделитель" (сепаратор) """
    ksSeparatorDownName     = 0
    """ Вывод имени снизу под сепаратором. """
    ksSeparatorUpName       = 1
    """ Вывод имени сверху над сепаратором. """
    ksSeparatorWithoutLine  = 2
    """ Вывод только имени; сепаратор отсутствует. """
    ksSeparatorBMPLeftName  = 3
    """ Вывод значка с именем слева. """
    ksSeparatorBMPRightName = 4
    """ Вывод значка с именем справа. """


class SlideTypeEnum:  # slidetypeenum.html
    """ ## SlideTypeEnum - Тип отображения слайда в окне """
    ksSlide          = -1
    """ Отображение слайда """
    ksBitmap         = 1
    """ Отображение растрового изображения """
    ksGroup          = 2
    """ Отображение группы """
    ksKompasDocument = 3
    """ Отображение документа КОМПАС """
    ksKompasText     = 4
    """ Отображение текста в формате КОМПАС """


class SpecPropertyButtonEnum:  # specpropertybuttonenum.html
    """ ## SpecPropertyButtonEnum - Предопределенные кнопки панели свойств """
    pbEnter      = 1
    """ Ввод """
    pbEsc        = 2
    """ Отказ """
    pbAutoCreate = 3
    """ Автосоздание """
    pbSaveState  = 4
    """ Запомнить состояние """
    pbNewSearch  = 5
    """ Новый поиск """
    pbPrevObj    = 6
    """ Предыдущий объект """
    pbNextObj    = 7
    """ Следующий объект """
    pbHelp       = 8
    """ Справка """
    pbCopyProps  = 9
    """ Копировать свойства """


class SpecificationLinkTypeEnum:  # ksspecificationlinktypeenum.html
    """ ## SpecificationLinkTypeEnum - Режимы связи сборки или чертежа со спецификацией """
    ksLinkNone                  = 0
    """ Нет. """
    ksLinkOnlyObjects           = 1
    """ Только вставка объектов спецификации. """
    ksLinkWithPositionCalculate = 2
    """ Связь с расчетом позиций. """


class SpecPropertyToolBarEnum:  # specpropertytoolbarenum.html
    """ ## SpecPropertyToolBarEnum - Предопределенные спецпанели для Панели свойств """
    pnUnknown                        = 0
    """ Неизвестная панель """
    pnEmpty                          = 1
    """ Пустая панель """
    pnEscHelp                        = 2
    """ Панель (pbEsc pbHelp) """
    pnEnterEscHelp                   = 3
    """ Панель (pbEnter pbEsc pbHelp) """
    pnEnterEscCreateHelp             = 4
    """ Панель (pbEnter pbEsc pbAutoCreate pbHelp) """
    pnEnterEscCreateSaveHelp         = 5
    """ Панель (pbEnter pbEsc pbAutoCreate SaveState pbHelp) """
    pnEnterEscCreateSaveSearchHelp   = 6
    """ Панель (pbEnter pbEsc pbAutoCreate SaveState pbNewSearch pbHelp) """
    pnEnterEscSaveSearchPrevNextHelp = 7
    """ Панель (pbEnter pbEsc SaveState pbNewSearch pbPrevObj pbNextObj pbHelp) """
    pnEnterEscSearchHelp             = 8
    """ Панель (pbEnter pbEsc pbNewSearch pbHelp) """
    pnEscSaveSearchHelp              = 9
    """ Панель (pbEsc SaveState pbNewSearch pbHelp) """
    pnEnterEscCreateSearchHelp       = 10
    """ Панель (pbEnter pbEsc pbAutoCreate pbNewSearch pbHelp) """
    pnEnterEscSaveSearchHelp         = 11
    """ Панель (pbEnter pbEsc SaveState pbNewSearch pbHelp) """
    pnEscSaveStateHelp               = 12
    """ Панель (pbEsc SaveState pbHelp) """
    pnEnterEscSearchPrevNextHelp     = 13
    """ Панель (pbEnter pbEsc pbNewSearch pbPrevObj pbNextObj pbHelp) """


class ZoomTypeEnum:  # zoomtypeenum.html
    """ ## ZoomTypeEnum - Тип изменения масштаба отображения документа в окне """
    ksZoomNext     = 0
    """ Следующий масштаб """
    ksZoomPrevious = 1
    """ Предыдущий масштаб """
    ksZoomAll      = 2
    """ Показать весь документ """


class ksDocumentFrameNotifyEnum:  # ksdocumentframenotifyenum.html
    """ ## ksDocumentFrameNotifyEnum - События для окна документа: клавиатура, мышь, события по отрисовке документа """
    frBeginPaint           = 1
    """ Начало отрисовки документа """
    frClosePaint           = 2
    """ Конец отрисовки документа """
    frMouseDown            = 3
    """ Нажатие кнопки мыши """
    frMouseUp              = 4
    """ Отпускание кнопки мыши """
    frMouseDblClick        = 5
    """ Двойной щелчок мыши """
    frBeginPaintGL         = 6
    """ Начало создания листа в контексте OpenGL """
    frClosePaintGL         = 7
    """ Окончание создания листа в контексте OpenGL """
    frAddGabarit           = 8
    """ Определение габаритов документа """
    frActivate             = 9
    """ Окно активизировалось """
    frDeactivate           = 10
    """ Окно деактивизировалось """
    frCloseFrame           = 11
    """ Закрытие окна """
    frMouseMove            = 12
    """ Перемещение мыши """
    frShowOcxTree          = 13
    """ Активизация закладки дерева документа """
    frBeginPaintTmpObjects = 14
    """ Начало отрисовки временных объектов (фантомов) """
    frClosePaintTmpObjects = 15
    """ Конец отрисовки временных объектов (фантомов) """


class ksPropertyManagerNotifyEnum:  # kspropertymanagernotifyenum.html
    """ ## ksPropertyManagerNotifyEnum - События Панели свойств или процессных параметров """
    prButtonClick         = 1
    """ Нажата кнопка спецпанели """
    prChangeControlValue  = 2
    """ Изменено значение элемента управления """
    prControlCommand      = 3
    """ Нажата кнопка элемента управления """
    prButtonUpdate        = 4
    """ Задано состояние кнопки спецпанели """
    prProcessActivate     = 5
    """ Активизирован процесс """
    prProcessDeactivate   = 6
    """ Деактивирован процесс """
    prCommandHelp         = 7
    """ Вызвана справка """
    prSelectItem          = 8
    """ Выделен элемент списка """
    prCheckItem           = 9
    """ Выбран элемент списка """
    prEditFocus           = 11
    """ Установка/снятие фокуса на редакторе ввода """
    prUserMenuCommand     = 12
    """ Нажатие пункта пользовательского меню """
    prLayoutChanged       = 13
    """ Изменение размещения панели свойств """
    prGetContextMenuType  = 14
    """ CLLBACK для получения типа контекстного меню """
    prFillContextPanel    = 15
    """ CLLBACK для накачки контекстной панели """
    prFillContextIconMenu = 16
    """ CLLBACK для накачки меню с иконками """
    prEndEditItem         = 17
    """ Завершение редактирования элемента """
    prChangeTabExpanded   = 18
    """ Сворачивание/Разворачивание закладки панели свойств """
    prItemDblClick        = 19
    """ Двойной клик по элементу в списке """


class ksPropertyUserControlNotifyEnum:  # kspropertyusercontrolnotifyenum.html
    """ ## ksPropertyUserControlNotifyEnum - События пользовательского элемента управления """
    puCreateOCX  = 1
    """ Создан элемент управления OCX """
    puDestroyOCX = 2
    """ Удален элемент управления OCX """


class ksViewsAndLayersManagerNotifyEnum:  # ksviewsandlayersmanagernotifyenum.html
    """ ## ksViewsAndLayersManagerNotifyEnum - События для менеджера видов и слоев """
    vmBeginEdit = 1
    """ Начато редактирование """
    vmEndEdit   = 2
    """ Завершено редактирование """


class ksViewProjectionScheme:  # ksviewprojectionscheme.html
    """ ## ksViewProjectionScheme - Схема ориентаций модели """
    ksVPSUnknown           = -1
    """ Не определена """
    ksVPSUser              = 0
    """ Пользовательская """
    ksVPSZAxonometric      = 1
    """ Z-аксонометрия """
    ksVPSYAxonometric      = 2
    """ Y-аксонометрия """
    ksVPSXAxonometric      = 3
    """ X-аксонометрия """
    ksVPSZ90AxonometricISO = 4
    """ Z-аксонометрия (ISO 90) """
    ksVPSY90AxonometricISO = 5
    """ Y-аксонометрия (ISO 90) """
    ksVPSX90AxonometricISO = 6
    """ X-аксонометрия (ISO 90) """


class ksDocument2DNotifyEnum:  # ksdocument2dnotifyenum.html
    """ ## ksDocument2DNotifyEnum - События графического документа """
    d2BeginRebuild        = 1
    """ Начало перестроения модели """
    d2Rebuild             = 2
    """ Модель перестроена """
    d2BeginChoiceMaterial = 3
    """ Начало выбора материала """
    d2СhoiceMaterial      = 4
    """ Закончен выбор материала """
    d2BeginInsertFragment = 5
    """ Начало вставки фрагмента (до диалога выбора имени) """
    d2LocalFragmentEdit   = 6
    """ Редактирование локального фрагмента """
    d2BeginChoiceProperty = 7
    """ Начало выбора свойства """
    d2ChoiceProperty      = 8
    """ Закончен выбор свойства """


class ksDocument3DNotifyEnum:  # ksdocument3dnotifyenum.html
    """ ## ksDocument3DNotifyEnum - События документа-модели """
    d3BeginRebuild               = 1
    """ Начало перестроения модели """
    d3Rebuild                    = 2
    """ Модель перестроена """
    d3BeginChoiceMaterial        = 3
    """ Начало выбора материала """
    d3СhoiceMaterial             = 4
    """ Закончен выбор материала """
    d3BeginChoiceMarking         = 5
    """ Начало выбора обозначения """
    d3ChoiceMarking              = 6
    """ Закончен выбор обозначения """
    d3BeginSetPartFromFile       = 7
    """ Начало установки компонента в сборку (до диалога выбора имени) """
    d3BeginCreatePartFromFile    = 8
    """ Начало создания компонента в сборке (до диалога выбора имени) """
    d2BeginDeleteProperty        = 9
    """ Начало удаления значения свойства """
    d2DeleteProperty             = 10
    """ Завершение удаления свойства """
    d3BeginChoiceProperty        = 12
    """ Начало выбора свойства """
    d3ChoiceProperty             = 13
    """ Закончен выбор свойства """
    d3BeginRollbackFeatures      = 14
    """ Начало отката дерева модели """
    d3RollbackFeatures           = 15
    """ Завершение отката дерева модели """
    d3BedinLoadCombinationChange = 16
    """ Начало переключения типа загрузки """
    d3LoadCombinationChange      = 17
    """ Завершение переключения типа загрузки """
    d3BeginDeleteMaterial        = 18
    """ Начало удаления материала """
    d3DeleteMaterial             = 19
    """ Материал удален """
    d3BeginDeleteProperty        = 20
    """ Начало удаления значения свойства """
    d3DeleteProperty             = 21
    """ Завершение удаления свойства """


class ksDocumentFileNotifyEnum:  # ksdocumentfilenotifyenum.html
    """ ## ksDocumentFileNotifyEnum - События для документов; работа с файлом """
    kdBeginCloseDocument    = 1
    """ - начало закрытия документа """
    kdCloseDocument         = 2
    """ - документ закрыт """
    kdBeginSaveDocument     = 3
    """ - начало сохранения документа """
    kdSaveDocument          = 4
    """ - документ сохранен """
    kdActiveDocument        = 5
    """ - документ активизировался """
    kdDeactiveDocument      = 6
    """ - документ деактивизировался """
    kdBeginSaveAsDocument   = 7
    """ - начало сохранения документа c другим именем (до диалога выбора имени) """
    kdDocumentFrameOpen     = 8
    """ - окно документа открылось """
    kdProcessActivate       = 9
    """ - процесс активизирован """
    kdProcessDeactivate     = 10
    """ - процесс деактивизирован """
    kdBeginProcess          = 11
    """ - начало процесса """
    kdEndProcess            = 12
    """ - завершение процесса """
    kdBeginAutoSaveDocument = 13
    """ - начало автосохранения документа """
    kdAutoSaveDocument      = 14
    """ - Документ автосохранен """


class ksKompasObjectNotifyEnum:  # kskompasobjectnotifyenum.html
    """ ## ksKompasObjectNotifyEnum - События приложения """
    koCreateDocument              = 1
    """ - документ создан """
    koBeginOpenDocumen            = 2
    """ - начало открытия документа """
    koOpenDocumen                 = 3
    """ - документ открыт, """
    koChangeActiveDocument        = 4
    """ - переключение на другой активный документ """
    koApplicatinDestroy           = 5
    """ - закрытие приложения. """
    koBeginCreate                 = 6
    """ - начало создания документа (до диалога выбора типа) """
    koBeginOpenFile               = 7
    """ - начало открытия документа (до диалога выбора имени) """
    koBeginCloseAllDocument       = 8
    """ - начало закрытия всех открытых документов """
    koKeyDown                     = 9
    """ - событие нажатия клавиатуры. клавиша нажата. """
    koKeyUp                       = 10
    """ - событие нажатия клавиатуры. клавиша отпущена """
    koKeyPress                    = 11
    """ -событие нажатия клавиатуры. клавиша нажата """
    koIsNeedConvertToSavePrevious = 15
    """ -Начало сохранения документа в предыдущую верcию """
    koBeginConvertToSavePrevious  = 16
    """ -Начало конвертации документа перед записью в предыдущую верию """
    koEndConvertToSavePrevious    = 17
    """ -Завершение конвертации документа перед записью в предыдущую верcию """
    koChangeTheme                 = 18
    """ -Изменение темы """
    koBeginDragOpenFiles          = 19
    """ Открытие файлов перетаскиванием в окно Компас """


class ksLayoutSheetsNotifyEnum:  # kslayoutsheetsnotifyenum.html
    """ ## ksLayoutSheetsNotifyEnum - События для листов оформления """
    ksLayoutAdd    = 1
    """ Добавлен лист """
    ksLayoutDelete = 2
    """ Удален лист оформления """
    ksLayoutUpdate = 3
    """ Изменены параметры листа оформления """


class ksLibraryManagerNotifyEnum:  # kslibrarymanagernotifyenum.html
    """ ## ksLibraryManagerNotifyEnum - События для менеджера библиотек """
    ksLMBeginAttach              = 1
    """ Подключить библиотеку """
    ksLMAttach                   = 2
    """ Библиотека подключена """
    ksLMBeginDetach              = 3
    """ Отключить библиотеку """
    ksLMDetach                   = 4
    """ Библиотека отключена """
    ksLMBeginExecute             = 5
    """ Запуск выполнения команды библиотеки """
    ksLMEndExecute               = 6
    """ Завершение выполнения команды библиотеки """
    ksLMSystemControlStop        = 7
    """ Передача управления библиотеке """
    ksLMSystemControlStart       = 8
    """ Передача управления системе """
    ksLMAddLibraryDescription    = 9
    """ Добавлено описание библиотеки """
    ksLMDeleteLibraryDescription = 10
    """ Удалено описание библиотеки """
    ksLMAddInsert                = 11
    """ Добавлен документ в библиотеку документов """
    ksLMDeleteInsert             = 12
    """ Удален документ из библиотеки документов """
    ksLMEditInsert               = 13
    """ Редактирование документа из библиотеки документов """
    ksLMTryExecute               = 14
    """ Попытка вызвать команду библиотеки """
    ksLMBeginInsertDocument      = 15
    """ Запуск вставки документа из библиотеки """


class ksNotifyType:  # ksnotifytype.html
    """ ## ksNotifyType - Перечень интерфейсов событий """
    ntKompasObjectNotify            = 1
    """ События приложения """
    ntDocumentFileNotify            = 2
    """ События документа, работа с файлом """
    ntStampNotify                   = 3
    """ События основной надписи """
    ntObject2DNotify                = 4
    """ События объекта графического документа """
    ntSelectionMngNotify            = 5
    """ События менеджера выделенных объектов """
    ntSpcObjectNotify               = 6
    """ События объекта спецификации """
    ntSpcDocumentNotify             = 7
    """ События документа-спецификации """
    ntSpecificationNotify           = 8
    """ События спецификации """
    ntDocument3DNotify              = 9
    """ События документа-модели """
    ntObject3DNotify                = 10
    """ События объекта документа-модели """
    ntDocument2DNotify              = 11
    """ События графического документа """
    ntPropertyManagerNotify         = 12
    """ События для Панели свойств """
    ntPropertyUserControlNotifyEnum = 13
    """ События пользовательского элемента управления """
    ntDocumentFrameNotify           = 14
    """ События для окна документа """
    ntViewsAndLayersManagerNotify   = 15
    """ События для менеджера видов и слоев """
    ntLibraryManagerNotify          = 16
    """ События для менеджера библиотек """
    ntProcess2DNotify               = 18
    """ События процесса 2D """
    ntProcess3DNotify               = 19
    """ События процесса 3D """
    ntContentDialogNotify           = 20
    """ События диалога с внешним наполнением """
    ntFindObjectParametersNotify    = 21
    """ События функции поиска объектов под курсором """
    ntProcess3DManipulatorsNotify   = 22
    """ События манипуляторов процесса 3D """
    ntPLMObjectNotify               = 23
    """ События объектов версионирования """
    ntFindObject3DParametersNotify  = 24
    """ Параметры поиска объектов 3D """


class ksObject2DNotifyEnum:  # ksobject2dnotifyenum.html
    """ ## ksObject2DNotifyEnum - События объектов графических документов """
    koChangeActive         = 1
    """ переключение активности объекта( вид, слой) """
    koBeginDelete          = 2
    """ начало удаления объекта """
    koDelete               = 3
    """ объект удален """
    koBeginMove            = 4
    """ начало сдвига объекта """
    koMove                 = 5
    """ завершение сдвига объекта, """
    koBeginRotate          = 6
    """ начало поворота объекта """
    koRotate               = 7
    """ завершение поворота объекта """
    koBeginScale           = 8
    """ начало масштабирования объекта """
    koScale                = 9
    """ завершение масштабирования объекта """
    koBeginTransform       = 10
    """ начало трансформации объекта """
    koTransform            = 11
    """ завершение трансформации объекта """
    koBeginCopy            = 12
    """ начало копирования объекта, """
    koCopy                 = 13
    """ завершение копирования объекта """
    koBeginSymmetry        = 14
    """ начало симметричного преобразования объекта """
    koSymmetry             = 15
    """ завершение симметричного преобразования объекта """
    koBeginProcess         = 16
    """ начало редактирования\\создания объекта """
    koEndProcess           = 17
    """ завершение редактирования\\создания объекта """
    koCreateObject         = 18
    """ создание объекта """
    koUpdateObject         = 19
    """ редактирование объекта """
    koBeginDestroyObject   = 20
    """ начало разрушения объекта """
    koDestroyObject        = 21
    """ разрушение объекта """
    koBeginPropertyChanged = 22
    """ начало изменения свойств объекта """
    koPropertyChanged      = 23
    """ изменены свойства объекта """


class ksObject3DNotifyEnum:  # ksobject3dnotifyenum.html
    """ ## ksObject3DNotifyEnum - События объектов документа-модели """
    o3BeginDelete           = 1
    """ Начало удаления объектов """
    o3Delete                = 2
    """ Oбъекты удалены """
    o3Excluded              = 3
    """ Oбъект исключен/включен в расчет """
    o3Hidden                = 4
    """ Oбъект скрыт/показан """
    o3BeginPropertyChanged  = 5
    """ Начало изменения свойств объекта """
    o3PropertyChanged       = 6
    """ Изменены свойства объекта """
    o3BeginPlacementChanged = 7
    """ Начало изменения положения объекта """
    o3PlacementChanged      = 8
    """ Начало изменения положения объекта """
    o3BeginProcess          = 9
    """ Начало """
    o3EndProcess            = 10
    """ Конец редактирования\\создания объекта """
    o3CreateObject          = 11
    """ Создание объекта """
    o3UpdateObject          = 12
    """ Редактирование объекта """
    o3BeginLoadStateChange  = 13
    """ Начало изменения типа загрузки """
    o3LoadStateChange       = 14
    """ Завершение изменения типа загрузки """


class ksProcess2DTypeEnum:  # ksprocess2dtypeenum.html
    """ ## ksProcess2DTypeEnum - Типы процессов 2D """
    ksProcess2DCursor    = 1
    """ - запрос на получение точки """
    ksProcess2DPlacement = 2
    """ - запрос на получение точки и угла """


class ksProcess3DTypeEnum:  # ksprocess3dtypeenum.html
    """ ## ksProcess3DTypeEnum - Типы процессов 3D """
    ksProcess3DPlacementAndEntity = 1
    """ - запрос на указание местоположения и объекта """
    ksProcess3DSelectEntity       = 2
    """ - запрос на выбор объекта """


class ksProcess2DNotifyEnum:  # ksprocess2dnotifyenum.html
    """ ## ksProcess2DNotifyEnum - События процесса 2D """
    ksProcess2DPlacementChanged     = 1
    """ - изменение положения """
    ksProcess2DExecuteCommand       = 2
    """ - выполнить команду меню """
    ksProcess2DRun                  = 3
    """ - запуск процесса """
    ksProcess2DStop                 = 4
    """ - остановка процесса """
    ksProcess2DActivate             = 5
    """ - активизация процесса """
    ksProcess2DDeactivate           = 6
    """ - деактивизация процесса """
    ksProcess2DEndProcess           = 7
    """ - окончание процесса """
    ksProcess2DMouseEnterLeaveParam = 8
    """ - запрос параметров точек для визуального определения места применения параметра """
    ksProcess2DAbortProcess         = 9
    """ - прерывание процесса при запуске другого процесса или команды """


class ksProcess3DNotifyEnum:  # ksprocess3dnotifyenum.html
    """ ## ksProcess3DNotifyEnum - События процесса 3D """
    ksProcess3DPlacementChanged       = 1
    """ - изменение положения """
    ksProcess3DExecuteCommand         = 2
    """ - выполнить команду меню """
    ksProcess3DRun                    = 3
    """ - запуск процесса """
    ksProcess3DStop                   = 4
    """ - остановка процесса """
    ksProcess3DActivate               = 5
    """ - активизация процесса """
    ksProcess3DDeactivate             = 6
    """ - деактивизация процесса """
    ksProcess3DFilterObjects          = 7
    """ - фильтрация объектов """
    ksProcess3DCreateTakeObject       = 8
    """ - событие создания объекта в - - - подчиненном режиме """
    ksProcess3DEndProcess             = 9
    """ - окончание процесса """
    ksProcess3DProcessingGroupObjects = 10
    """ - обработать объекты, пришедшие при селектировании рамкой """
    ksProcess3DAbortProcess           = 11
    """ - прерывание процесса при запуске другого процесса или команды """


class ksTwinSwitcherValueEnum:  # kstwinswitchervalueenum.html
    """ ## ksTwinSwitcherValueEnum - Значения переключателя """
    ksTwinSwitcherPos1 = 1
    """ - положение 1 """
    ksTwinSwitcherPos2 = 2
    """ - положение 2 """


class ksToleranceArrowType:  # kstolerancearrowtype.html
    """ ## ksToleranceArrowType - Тип стрелки ответвления у допуска формы """
    ksTANone       = 0
    """ - нет """
    ksTAArrow      = 1
    """ - стрелка """
    ksksTATriangle = 2
    """ - треугольник """


class ksEnterButtonIconTypeEnum:  # ksenterbuttonicontypeenum.html
    """ ## ksEnterButtonIconTypeEnum - Тип иконки для кнопки Cоздать """
    ksEnterCheckIcon    = 0
    """ Обычная кнопка. Создать в виде галочки """
    ksEnterFloppyIcon   = 1
    """ Дискета """
    ksEnterNewInputIcon = 2
    """ Новый ввод """
    ksEnterApplyIcon    = 3
    """ Применить """


class ksShowHideTmpObjTypeEnum:  # ksshowhidetmpobjtypeenum.html
    """ ## ksShowHideTmpObjTypeEnum - Тип отображения временного объекта в документе """
    ksTmpObjHide        = 0
    """ - объект скрыт """
    ksTmpObjShow        = 1
    """ - объект отображается как обычный объект """
    ksTmpObjShowPhantom = 2
    """ - объект отображается как фантом """


class ksSelectionMngNotifyEnum:  # ksselectionmngnotifyenum.html
    """ ## ksSelectionMngNotifyEnum - События менеджера выделенных объектов """
    ksmSelect      = 1
    """ - объект выделен """
    ksmUnselect    = 2
    """ - снято выделение с объекта """
    ksmUnselectAll = 3
    """ - снято выделение со всех объектов """


class ksStampNotifyEnum:  # ksstampnotifyenum.html
    """ ## ksStampNotifyEnum - События основной надписи графических документов (штампа) """
    kdBeginEditStamp       = 1
    """ Начало работы со штампом """
    kdEndEditStamp         = 2
    """ Завершение работы со штампом """
    kdStampCellDblClick    = 3
    """ Двойной щелчок мышью в ячейке штампа """
    kdStampCellBeginEdit   = 4
    """ Начало редактирования в ячейке штампа """
    kdStampBeginClearCells = 5
    """ Начало очистки ячеек штампа """


class ksSpcDocumentNotifyEnum:  # ksspcdocumentnotifyenum.html
    """ ## ksSpcDocumentNotifyEnum - События документа-спецификации """
    sdDocumentBeginAdd    = 1
    """ Начало добавления документа сборочного чертежа """
    sdDocumentAdd         = 2
    """ Добавлен документ сборочного чертежа """
    sdDocumentBeginRemove = 3
    """ Начало удаления документа сборочного чертежа """
    sdDocumentRemove      = 4
    """ Удален документ сборочного чертеж """
    sdSpcStyleBeginChange = 5
    """ Начало изменения стиля спецификации """
    sdSpcStyleChange      = 6
    """ Стиль спецификации изменился """


class ksSpcObjectNotifyEnum:  # ksspcobjectnotifyenum.html
    """ ## ksSpcObjectNotifyEnum - События объекта спецификации """
    soBeginDelete      = 1
    """ Начало удаления объекта """
    soDelete           = 2
    """ Объект удален """
    soCellDblClick     = 3
    """ Двойной щелчок в ячейке """
    soCellBeginEdit    = 4
    """ Начало редактирования в ячейке """
    soChangeCurrent    = 5
    """ Текущий объект изменен """
    soDocumentBeginAdd = 6
    """ Начало добавления документа """
    soDocumentAdd      = 7
    """ Документ в объекте спецификации добавлен """
    soDocumentRemove   = 8
    """ Документ из объекта спецификации удален """
    soBeginGeomChange  = 9
    """ Начало изменения геометрии объекта спецификации """
    soGeomChange       = 10
    """ Геометрия объекта спецификации изменилась """
    soBeginProcess     = 11
    """ Начало редактирования\\создания объекта """
    soEndProcess       = 12
    """ Конец редактирования\\создания объекта """
    soCreateObject     = 13
    """ Объект создан """
    soUpdateObject     = 14
    """ Объект изменен """
    soBeginCopy        = 15
    """ Начало копирования объекта """
    soCopy             = 16
    """ Копирование объекта """


class ksSpecificationNotifyEnum:  # ksspecificationnotifyenum.html
    """ ## ksSpecificationNotifyEnum - События для спецификации """
    ssTuningSpcStyleBeginChange   = 1
    """ Начало изменения настроек спецификации """
    ssTuningSpcStyleChange        = 2
    """ Настройки спецификации изменились """
    ssChangeCurrentSpcDescription = 3
    """ Изменилось текущее описание спецификации """
    ssSpcDescriptionAdd           = 4
    """ Добавилось описание спецификации """
    ssSpcDescriptionRemove        = 5
    """ Удалилось описание спецификации """
    ssSpcDescriptionBeginEdit     = 6
    """ Начало редактирования описания спецификации """
    ssSpcDescriptionEdit          = 7
    """ Отредактировали описание спецификации """
    ssSynchronizationBegin        = 8
    """ Начало синхронизации """
    ssSynchronization             = 9
    """ Синхронизация проведена """
    ssBeginCalcPositions          = 10
    """ Начало расчета позиций """
    ssCalcPositions               = 11
    """ Проведен расчет позиций """
    ssBeginCreateObject           = 12
    """ Начало создания объекта спецификации (до диалога выбора раздела) """


# ctypes.html
SPC_CLM_FORMAT   = 1
""" - формат """
SPC_CLM_ZONE     = 2
""" - зона """
SPC_CLM_POS      = 3
""" - позиция """
SPC_CLM_MARK     = 4
""" - обозначение """
SPC_CLM_NAME     = 5
""" - наименование """
SPC_CLM_COUNT    = 6
""" - количество """
SPC_CLM_NOTE     = 7
""" - примечание """
SPC_CLM_MASSA    = 8
""" - масса """
SPC_CLM_MATERIAL = 9
""" - материал """
SPC_CLM_USER     = 10
""" - пользовательская """
SPC_CLM_KOD      = 11
""" - код """
SPC_CLM_FACTORY  = 12
""" - предприятие-изготовитель """


# spcstrtypes.html
SPC_BASE_OBJECT  = 1
""" - базовый объект """
SPC_COMMENT      = 2
""" - вспомогательный объект """
SPC_SECTION_NAME = 3
""" - заголовок раздела """
SPC_BLOCK_NAME   = 4
""" - заголовок блока исполнений """
SPC_RESERVE_STR  = 5
""" - резервная строка """
SPC_EMPTY_STR    = 6
""" - пустая строка в конце страницы """


# spcsorttypes.html
SPC_SORT_OFF      = 0
""" - нет сортировки """
SPC_SORT_COMPOS   = 1
""" - составная сортировка """
SPC_SORT_ALPHABET = 2
""" - сортировка по алфавиту """
SPC_SORT_UP       = 3
""" - сортировка по возрастанию числового значения """
SPC_SORT_DOCUMENT = 4
""" - сортировка раздела документация """
SPC_SORT_DOWN     = 5
""" - сортировка по убыванию числового значения """


# attypes.html
CHAR_ATTR_TYPE   = 1
""" - целое (от -128 до 127) """
UCHAR_ATTR_TYPE  = 2
""" - целое (от 0 до 255) """
INT_ATTR_TYPE    = 3
""" - целое (от -32768 до 32767) """
UINT_ATTR_TYPE   = 4
""" - целое (от 0 до 65535) """
LINT_ATTR_TYPE   = 5
""" - целое """
FLOAT_ATTR_TYPE  = 6
""" - действительное (от -1Е38 до 1Е38) """
DOUBLE_ATTR_TYPE = 7
""" - действительное (от -1Е308 до 1Е307) """
STRING_ATTR_TYPE = 8
""" - строка фиксированной длины MAX_TEXT_LENGTH """
RECORD_ATTR_TYPE = 9
""" - запись """


class ksSpecificationStyleDifferenceTypeEnum:  # ksspecificationstyledifferencetypeenum.html
    """ ## ksSpecificationStyleDifferenceTypeEnum - Отличие стиля спецификации от библиотечного """
    ksSpcStyleEqual       = 0
    """ Стиль спецификации не отличается от библиотечного """
    ksSpcStyleDistinguish = 1
    """ Стиль спецификации отличается от библиотечного """
    ksSpcStyleNotFound    = -1
    """ Стиль спецификации не найден в библиотеке стилей """


class ksSheetTypeEnum:  # kssheettypeenum.html
    """ ## ksSheetTypeEnum - Тип листа """
    ksDocumentSheet        = 0
    """ Лист документа """
    ksFrontAdditionalSheet = 1
    """ Дополнительный лист в начале документа """
    ksLastAdditionalSheet  = 2
    """ Дополнительный лист в конце документа """


# ordinateddimtypes.html
OD_FRONTVIEW     = 0x00
""" - для вида спереди, с полкой и стрелкой, возможна выносная линия """
OD_TOPVIEW       = 0x08
""" - для вида сверху без линии-выноски - только текст в рамке """
OD_TOPVIEWLEADER = 0x10
""" - для вида сверху с линией-выноской """


# stypes.html
SN_NEAREST_POINT  = 1
""" - Ближайшая точка """
SN_NEAREST_MIDDLE = 2
""" - Середина """
SN_CENTRE         = 3
""" - Центр """
SN_INTERSECT      = 4
""" - Пересечение """
SN_GRID           = 5
""" - По сетке """
SN_XY_ALIGN       = 6
""" - Выравнивание """
SN_ANGLE          = 7
""" - Угловая привязка """
SN_POINT_CURVE    = 8
""" - Точка на кривой """


# sstypes.html
SN_DYNAMICALLY      = 0x1
""" - динамически отслеживать привязки """
SN_ASSISTANT        = 0x2
""" - отображать название действующей привязки """
SN_BACKGROUND_LAYER = 0x4
""" - учитывать фоновые слои и виды """
SN_SUSPENDED        = 0x8
""" - подавить привязки """


# layertypes.html
stACTIVE    = 0
""" - активный (видимый фоновый) """
stREADONLY  = 1
""" - фоновый """
stINVISIBLE = 2
""" - невидимый (погашенный) """
stCURRENT   = 3
""" - текущий """


# l3dexportformats.html
FORMAT_SAT  = 1
""" формат SAT, для сохранения документов """
FORMAT_XT   = 2
""" формат XT, для сохранения документов """
FORMAT_STEP = 3
""" формат STEP, для сохранения документов """
FORMAT_IGES = 4
""" формат IGES, для сохранения документов """
FORMAT_VRML = 5
""" формат VRML, для сохранения документов """
FORMAT_STL  = 6
""" формат STL, для сохранения документов """
FORMAT_C3D  = 7
""" формат C3D, для сохранения документов """


# lrasterformats.html
FORMAT_BMP = 0
""" - BMP """
FORMAT_GIF = 1
""" - GIF """
FORMAT_JPG = 2
""" - JPEG """
FORMAT_PNG = 3
""" - PNG """
FORMAT_TIF = 4
""" - TIFF """
FORMAT_TGA = 5
""" - TGA """
FORMAT_PCX = 6
""" - PCX """
FORMAT_WMF = 16
""" - WMF (не поддерживается) """
FORMAT_EMF = 17
""" - EMF """


# lobjcolors.html
BLACKWHITE  = 0
""" - черный """
COLORVIEW   = 1
""" - цвет, установленный для вида """
COLORLAYER  = 2
""" - цвет, установленный для слоя """
COLOROBJECT = 3
""" - цвет, установленный для объекта """


# lpalettes.html
BPP_COLOR_01 = 1
""" - монохромный """
BPP_COLOR_02 = 2
""" - 4 цвета """
BPP_COLOR_04 = 4
""" - 16 цветов """
BPP_COLOR_08 = 8
""" - 256 цветов """
BPP_COLOR_16 = 16
""" - 16 разрядов """
BPP_COLOR_24 = 24
""" - 24 разряда """
BPP_COLOR_32 = 32
""" - 32 разряда """


# standartviewtypes.html
VIEW_FRONT = 0x1
""" Спереди """
VIEW_REAR  = 0x2
""" Сзади """
VIEW_UP    = 0x4
""" Сверху """
VIEW_DOWN  = 0x8
""" Снизу """
VIEW_LEFT  = 0x10
""" Слева """
VIEW_RIGHT = 0x20
""" Справа """
VIEW_ISO   = 0x40
""" Изометрия """


class ksDrawInScreenPlaneEnum:  # ksdrawinscreenplaneenum.html
    """ ## ksDrawInScreenPlaneEnum - Способ преобразования координат внешней триангуляции """
    ksDrawNone              = 0
    """ - Не преобразовывать координаты в плоскость экран """
    ksDrawInScreenPlane     = 1
    """ - Координаты Ox и Oy совпадают с экранными """
    ksDrawProjectToScreen   = 2
    """ - Координаты Oz Совпадает с экранными, Ox И Oy проецируются на экран """
    ksDrawProjectFromScreen = 3
    """ - Координаты Ox остаются неизменными, координаты Oz проецируются с экранными """


class ksBooleanType:  # ksbooleantype.html
    """
    ## ksBooleanType - Типы булевых операций над твердыми телами

    При типе направления dtMiddlePlane в методах SetSideParam и GetSideParam параметр depth интерпретируется как общая глубина выдавливания и задается следующим образом:

    SetSideParam(TRUE, etBlind, depth, ...)
    """
    ksBooleanUnknown = 0
    """ Неизвестность """
    ksIntersect      = 1
    """ Пересечение """
    ksDifference     = 2
    """ Вычитание """
    ksUnion          = 3
    """ Объединение """


class End_Type:  # end_type.html
    """
    ## End_Type - Типы операций выдавливания

    1. При типах выдавливания etUpToVertexTo, etUpToVertexFrom, etUpToSurfaceTo и etUpToSurfaceFrom в методах SetSideParam и GetSideParam параметр depth интерпретируется как глубина, вычитаемая или добавляемая к расстоянию до указанного объекта. Объект, определяющий глубину, задается с помощью метода SetDepthObject.

    2. В API7 соответствуют перечислению ksEndTypeEnum.
    """
    etBlind           = 0
    """ строго на глубину """
    etThroughAll      = 1
    """ через всю деталь """
    etUpToVertexTo    = 2
    """ на расстояние до вершины """
    etUpToVertexFrom  = 3
    """ на расстояние за вершину """
    etUpToSurfaceTo   = 4
    """ на расстояние до поверхности """
    etUpToSurfaceFrom = 5
    """ на расстояние за поверхность """
    etUpToNearSurface = 6
    """ до ближайшей поверхности """


class ksContourFormEnum:  # kscontourformenum.html
    """ ## ksContourFormEnum – форма контура обозначения узла """
    ksUFormCircle     = 0
    """ Окружность """
    ksUFormRectangle  = 1
    """ Прямоугольник """
    ksUFormCRectangle = 2
    """ Прямоугольник со скругленными вершинами """


class COM:  # interfaceparamtypeenum.html
    """ ## Константы типов интерфейсов параметров для COM в 2D """
    kо_ParametrizeParam = 9000
    """ ksParametrizationParam - параметры параметризации группы объектов. """


# thicknesstypes.html
LIKE_BASIC_LINE = 0x10
""" - параметры пера как у системной основной линии """
LIKE_THIN_LINE  = 0x20
""" - параметры пера как у системной тонкой линии """
LIKE_HEAVY_LINE = 0x30
""" - параметры пера как у системной утолщенной линии """


class ksDrawingObjectParamTypeEnum:  # ksdrawingobjectparamtypeenum.html
    """ ## ksDrawingObjectParamTypeEnum – тип параметров объекта """
    ksAllParam      = -1
    """ Все параметры """
    ksSheetAllParam = -2
    """ Все параметры объекта в СК листа """
    ksViewAllParam  = -7
    """ Все параметры объекта в СК вида """


class ksStampEnum:  # ksstampenum.html
    """ ## ksStampEnum - Идентификаторы ячеек штампа """
    ksStPartNumber           = 1
    """ Наименование изделия """
    ksStDescription          = 2
    """ Обозначение документа """
    ksStMaterial             = 3
    """ Обозначение материала """
    ksStMass                 = 5
    """ Масса изделия """
    ksStScale                = 6
    """ Масштаб """
    ksStSheetNumber          = 7
    """ Номер листа """
    ksStNumberOfSheets       = 8
    """ Количество листов """
    ksStCompany              = 9
    """ Индекс предприятия """
    ksStTypeOfWork           = 10
    """ Характер работы """
    ksStFormat               = 32
    """ Формат """
    ksStDocumentLetter1      = 40
    """ Литера документа (графа 1) """
    ksStDocumentLetter2      = 41
    """ Литера документа (графа 2) """
    ksStDocumentLetter3      = 42
    """ Литера документа (графа 3) """
    ksStFullFileName         = 43
    """ Имя файла (полное) """
    ksStShortFileName        = 44
    """ Имя файла (короткое) """
    ksStMarkingLine          = 45
    """ Строка обозначения и дефис """
    ksStDocumentName         = 51
    """ Наименование документа """
    ksStDocumentCode         = 52
    """ Код документа """
    ksStOKPCode              = 53
    """ Код ОКП """
    ksStAuthor               = 110
    """ Фамилия разработавшего """
    ksStCheckedBy            = 111
    """ Фамилия проверившего """
    ksStMfgApprovedBy        = 112
    """ Фамилия тех. контр """
    ksStDesigner             = 113
    """ Фамилия вып. работу """
    ksStRateOfInspection     = 114
    """ Фамилия норм. контр """
    ksStApprovedBy           = 115
    """ Фамилия утверждающего """
    ksStEndDesignDate        = 130
    """ Дата окончания разработки """
    ksStCheckedDate          = 131
    """ Дата проверки """
    ksStMfgApprovedDate      = 132
    """ Дата тех. контр """
    ksStExecutionDate        = 133
    """ Дата выполнения """
    ksStRateOfInspectionDate = 134
    """ Дата норм. контр """
    ksStApprovedDate         = 135
    """ Дата утверждения """


class ksReportTypeEnum:  # ksreporttypeenum.html
    """ ## ksReportTypeEnum - Тип отчета """
    ksRTPropertiesReport                = 0
    """ Отчет по свойствам """
    ksRTEmbodimentsReport               = 1
    """ Отчет по исполнениям """
    ksRTPatternWithVariablesTableReport = 2
    """ Отчет по таблице изменяемых переменных в массиве """
    ksRTAdditionNumbersReport           = 3
    """ Отчет по таблице дополнительных номеров """


class ksRowsNumberingTypeEnum:  # ksrowsnumberingtypeenum.html
    """ ## ksRowsNumberingTypeEnum - Формат нумерации строк отчета """
    ksRNTNone       = 0
    """ Нумерацию не использовать """
    ksRNTSimple     = 1
    """ Простая нумерация """
    ksRNTMultiLevel = 2
    """ Многоуровневая нумерация """


class ksNumberingTypeEnum:  # ksnumberingtypeenum.html
    """ ## ksNumberingTypeEnum - Формат нумерации """
    ksNTArabicNumerals  = 0
    """ 1,2,3,4,5... """
    ksNTRomanNumerals   = 1
    """ I, II, III, IV, V... """
    ksNTUpperRegEnglish = 2
    """ A,B,C,D... """
    ksNTLowerRegEnglish = 3
    """ a,b,c,d... """
    ksNTUpperRegRussian = 4
    """ А,Б,В,Г... """
    ksNTLowerRegRussian = 5
    """ а,б,в,г... """


class ksReportStyleInitEnum:  # ksreportstyleinitenum.html
    """ ## ksReportStyleInitEnum - Способ инициализации стиля отчета """
    ksRSIDefault = 0
    """ Стиль по умолчанию """


class ksGroupeTypeEnum:  # ksgroupetypeenum.html
    """ ## ksGroupeTypeEnum - Тип группировки колонки отчета """
    ksGTNone  = 0
    """ Нет группировки """
    ksGTMatch = 1
    """ Совпадение - группируются только строки с одинаковыми значениями """
    ksGTSum   = 2
    """ Сумма (Только для числовых колонок) """
    ksGTRange = 3
    """ Диапазон (Только для числовых колонок) """
    ksGTEnum  = 4
    """ Перечисление """


class ksReportBuildingTypeEnum:  # ksreportbuildingtypeenum.html
    """ ## ksReportBuildingTypeEnum - Способ выбора объектов для отчета """
    ksRBAllObjects    = 0
    """ По всем объектам """
    ksRBChooseObjects = 1
    """ По указанным объектам """
    ksRBCurrentView   = 2
    """ По текущему виду """
    ksRBChoiceToLevel = 3
    """ До указанного уровня """


class ksPageLayoutTypeEnum:  # kspagelayouttypeenum.html
    """ ## ksPageLayoutTypeEnum - Тип компоновки таблиц отчета """
    ksRPLayoutDefault = 0
    """ Вправо, затем вниз """
    ksRPLayout1       = 1
    """ Вниз, затем вправо """


# textflags.html
INVARIABLE         = 0
""" - не менять флаги текста """
NUMERATOR          = 0x1
""" - числитель """
DENOMINATOR        = 0x2
""" - знаменатель """
END_FRACTION       = 0x3
""" - конец дроби """
UPPER_DEVIAT       = 0x4
""" - верхнее отклонение """
LOWER_DEVIAT       = 0x5
""" - нижнее отклонение """
END_DEVIAT         = 0x6
""" - конец отклонений """
S_BASE             = 0x7
""" - основание выражения с под- или над- строкой """
S_UPPER_INDEX      = 0x8
""" - верхний индекс выражения с под- или надстрокой """
S_LOWER_INDEX      = 0x9
""" - нижний индекс выражения с под- или надстрокой """
S_END              = 0x10
""" - конец выражения с под- или над- строкой """
SPECIAL_SYMBOL     = 0x11
""" - спецзнак """
SPECIAL_SYMBOL_END = 0x12
""" - конец спецзнака для спецзнаков с текстом """
RETURN_BEGIN       = 0x13
""" - начало для ввода следующих строк в спецзнаке с текстом, дробях, отклонениях """
RETURN_DOWN        = 0x14
""" - для ввода следующих строк в спецзнаке с текстом, дробях, отклонениях """
RETURN_RIGHT       = 0x15
""" - для ввода строк справа в спецзнаке с текстом, дробях, отклонениях """
TAB                = 0x16
""" - табуляция по текущему стилю, """
FONT_SYMBOL        = 0x17
""" - символ шрифта, """
ITALIC_ON          = 0x40
""" - включить наклон """
ITALIC_OFF         = 0x80
""" - выключить наклон, """
BOLD_ON            = 0x100
""" - включить жирное начертание """
BOLD_OFF           = 0x200
""" - выключить жирное начертание """
UNDERLINE_ON       = 0x400
""" - включить подчеркивание """
UNDERLINE_OFF      = 0x800
""" - выключить подчеркивание """
NEW_LINE           = 0x1000
""" - новая строка в параграфе """
FONT_SYMBOL_W      = 0x2017
""" - символ шрифта Unicode """


# bk1823723.html
ksCMViewFullScreen           = 32403
""" Полный экран. """
ksCMSaveAll                  = 32404
""" Сохранить все """
ksCMSaveTechnicalDemand      = 32405
""" Cохранить технические требования """
ksCMSaveTechnicalDemandToTxt = 32406
""" Сохранить технические требования в текстовый документ """
ksCMCloseTechnicalDemand     = 32407
""" Закрыть технические требования """
ksCMCloseSpcSlave            = 32408
""" Закрыть окно объектов спецификаций """
ksCMDocumentSetup            = 32410
""" Настройки текущего документа """
ksCMViewVariables            = 32498
""" Скрыть/показать панель Переменные """
ksCMTutor3D                  = 32535
""" Азбука КОМПАС-3D """
ksCMTutor2D                  = 32540
""" Азбука КОМПАС-График """


# zooming.html
ksCMZoomWindow         = 32411
""" Увеличить масштаб окном """
ksCMZoomIn             = 32412
""" Увеличить масштаб """
ksCMZoomOut            = 32413
""" Уменьшить масштаб """
ksCMScaleView          = 32414
""" Текущий масштаб (Комбобокс с масштабом) """
ksCMZoomEntireDocument = 32415
""" Показать весь документ """
ksCMZoomSelected       = 32416
""" Показать полностью выделенные объекты """
ksCMRefresh            = 32417
""" Обновить изображение """
ksCMMoveView           = 32418
""" Сдвинуть изображение """
ksCMPanoramaView       = 32419
""" Приблизить/отдалить изображение """
ksCMRotateView         = 32420
""" Повернуть изображение (для 3Д-окна) """
ksCMZoom1              = 32545
""" Масштаб 1,0 """
ksCMZoomSketch         = 40872
""" Показать эскиз полностью """


# styles.html
ksCMSetAttributeTypes = 32421
""" Типы атрибутов """
ksCMSetCurveStyles    = 32422
""" Стили линий """
ksCMSetTextStyles     = 32423
""" Стили текстов """
ksCMSetStampStyles    = 32424
""" Редактирование изображения штампа """
ksCMSetTextShape      = 32425
""" Редактирование текстовых оформлений """
ksCMSetGraphicShape   = 32426
""" Редактирование графических оформлений """
ksCMSetHatchStyles    = 32427
""" Стили штриховок """
ksCMSetSpcStyles      = 32448
""" Стили спецификаций """
ksCMSummaryInfo       = 32440
""" Информация о документе """


# lists_navigation.html
ksCMMoveDocumentlists_navigationEX = 32522
""" Перейти к листу (со списком листов) """
ksCMMoveDocumentFirst              = 32523
""" Перейти к первому листу документа """
ksCMMoveDocumentLast               = 32524
""" Перейти к первому листу документа """
ksCMMoveDocumentPrev               = 32525
""" Перейти к предыдущему листу документа """
ksCMMoveDocumentNext               = 32526
""" Перейти к последующему листу документа """
ksCMRetryCommand                   = 32534
""" Повтор последней команды """
ksCMCloseAll                       = 32535
""" Закрыть все """
ksCMStop                           = 33206
""" Отмена текущей команды (Стоп) """
ksCMRepeatFind                     = 33207
""" Повторение поиска объекта """
ksCMCreateObject                   = 33700
""" Создать объект Создать """
ksCMCansel                         = 33701
""" Отказ от создания объекта (Стоп) """
ksCMEscape                         = 33211
""" Отмена текущей команды (По клавише Esc) """
ksPrintSpecialExecute              = 37289
""" Отправить документ на специальную полистную печать """


# specification.html
ksCMSpcObjectsSort         = 33796
""" Автоматическая сортировка объектов текущего раздела СП """
ksCMSpcRebuild             = 33797
""" Перестроить спецификацию """
ksCMFullPageHeight         = 33800
""" Изменить масштаб по высоте листа для спецификации """
ksCMFullPageWidth          = 33801
""" Изменить масштаб по ширине листа для спецификации """
ksCMSpcMakePosition        = 33891
""" Расставить позиции """
ksCMSpcObjectDelete        = 33892
""" Удалить элемент спецификации """
ksCMSpcObjectInsert        = 33893
""" Добавить элемент спецификации """
ksCMSpcSynchronize         = 33896
""" Cинхронизировать данные """
ksCMSpcInsertLine          = 33898
""" Добавить строку """
ksCMSpcShowAll             = 33900
""" Показать все объекты """
ksCMSpcTuningSetup         = 33901
""" Настройка спецификации """
ksCMSpcCopyObject          = 33902
""" Копировать текущий объект спецификации """
ksCMSpcObjectMoveUp        = 33903
""" Cдвинуть текущий объект спецификации вверх """
ksCMSpcObjectMoveDovn      = 33904
""" Cдвинуть текущий объект спецификации вниз """
ksCMSpcObjectEdit          = 33905
""" Редактировать текст текущего объекта спецификации """
ksCMSpcInsertIspoln        = 33906
""" Добавить объекты-исполнения для текущего объекта спецификации """
ksCMSpcOpenGeometryDocs    = 33907
""" Открыть документы с геометрией объекта """
ksCMCpcShowExcludedObjects = 33911
""" Показать исключенные объекты """


# frags.html
ksCMFragmentManager     = 35704
""" Управление фрагментами """
ksCMEditFragment        = 35705
""" Редактировать фрагмент """
ksCMCreateLocalFragment = 35706
""" Создать локальный фрагмент """


# objects_del.html
ksCMDelAuxCurves             = 35739
""" Удалить вспомогательные кривые во всех видах """
ksCMDelAuxCurvesInCurentView = 35740
""" Удалить вспомогательные кривые в текущем виде """
ksCMDelStamp                 = 35741
""" Удалить штамп """
ksCMDelTechnicalDemand       = 35742
""" Удалить технические требования """
ksCMDelSpecRough             = 35743
""" Удалить неуказанную шероховатость """
ksCMSheetViewStates          = 35744
""" Состояния видов """
ksCMViewLayerStates          = 35745
""" Слои """
ksCMGridOnOf                 = 35746
""" Включить/выключить отображение сетки """
ksCMSnapSuspend              = 35748
""" Включить/выключить действие глобальных привязок """
ksCMSnapSetup                = 35749
""" Настройка глобальных привязок """
ksCMOrthoModeOnOff           = 35750
""" Включить/выключить режим ортогонального черчения """
ksCMDiscreteModeOnOff        = 35747
""" Включить/выключить режим 'дискретирования' линейных величин по шагу курсора """


# layers_states.html
ksCMRebuildSheet                 = 35751
""" Перестроить чертеж """
ksCMSheetViewParams              = 35752
""" Параметры текущего вида """
ksCMTechnicalDemand              = 35753
""" Технические требования - ввод """
ksCMSpecRough                    = 35754
""" Неуказанная шероховатость """
ksCMSlaveSpc                     = 35755
""" Просмотр\\редактирование объектов спецификации """
ksCMAddEditSpcObject             = 35760
""" Добавить\\редактировать объект спецификации """
ksCMAddEditChangeListObject      = 35761
""" Добавить\\редактировать объект таблицы изменений """
ksCMSpcSinhronize                = 35763
""" Cинхронизировать данные """
ksCMSheetSpc                     = 35764
""" Таблица спецификации на листе """
ksCMLayoutManager                = 35765
""" Управление списком оформлений документа """
ksCMAddPage                      = 35766
""" Добавить лист в многолистовой документ """
ksCMGoto00                       = 36028
""" Поставить курсор в точку 0.0 """
ksCMToggleCursor                 = 36029
""" Переключить размер курсора """
ksCMRegulateLeaderLineX          = 36075
""" Выравнивать линии выноски по горизонтали """
ksCMRegulateLeaderLineY          = 36076
""" Выравнивать линии выноски по вертикали """
ksCMEditSpcObject                = 36077
""" Редактировать объект спецификации по линии-выноске """
ksCMEditSpcObjectForGeom         = 36086
""" Редактировать объект спецификации по геометрии """
ksCMGridSetup                    = 36090
""" Настроить параметры сетки """
ksCMSlaveSpcDelegate             = 36094
""" Просмотр\\редактирование объектов-делегатов спецификации """
ksCMAddSpcDelegate               = 36095
""" Добавить\\редактировать объект-делегат спецификации """
ksCMAutoCreateSpcObj             = 36097
""" Сформировать объекты спецификации для модели """
ksCMLibraryBarVisible            = 36104
""" Скрыть/показать панель Библиотеки """
ksRestoreStylesInAssociationView = 37002
""" Восстановить стили объектов ассоциативного вида """
ksCMBuildTreeView                = 37003
""" Скрыть/показать дерево построений """
ksSheetViewParams                = 37005
""" Параметры вида """
ksCMaximizeWorkArea              = 37079
""" Показать панели """
ksCMParameters                   = 37608
""" Настройки системы и новых документов """
ksCMZoomUndo                     = 38530
""" Предыдущий масштаб """
ksCMZoomRedo                     = 38531
""" Последующий масштаб """
ksViewShowBreakups               = 39344
""" Вид - Показать разрывы """


# cms_3d_doc.html
ksCM3DRebuild                           = 40356
""" Перестроить 3D документ """
ksCMHideCPlaces                         = 40360
""" Скрыть\\показать начала координат """
ksCMHideCPlanes                         = 40361
""" Скрыть\\показать конструктивные плоскости """
ksCMHideCAxies                          = 40362
""" Скрыть\\показать конструктивные оси """
ksCMHideSketches                        = 40363
""" Скрыть\\показать эскизы """
ksCMHideSurfaces                        = 40364
""" Скрыть\\показать поверхности """
ksCMHideThreads                         = 40365
""" Скрыть\\показать изображения резьбы """
ksCMHideCurves                          = 40366
""" Скрыть\\показать пространственные кривые """
ksCMHidePoints                          = 40367
""" Скрыть\\показать конструктивные точки """
ksCMHideAllObjects                      = 40368
""" Скрыть\\показать вспомогательные объекты """
ksCMHideDimensions                      = 40369
""" Скрыть\\показать размеры """
ksCMHideDesignations                    = 40370
""" Скрыть\\показать условные обозначения """
ksCMCreateSheetFromModel                = 40373
""" Создать новый чертеж из модели """
ksCMDeleteRollbackObjects               = 40375
""" Удалить все объекты под указателем """
ksCMSelectedObjectProperties            = 40461
""" Свойства объекта (оси, плоскости, эскиза, операции, грани) """
ksCMSelectedObjectOwnerProperties       = 40462
""" Свойства родителя (эскиза, операции) """
ksCMSelectedCompanentProperties         = 40463
""" Свойства детали или сборки """
ksCMSelectedCompanentInstanceProperties = 40464
""" Свойства вставленного компонента """
ksCMViewFeatureInTree                   = 40524
""" Показать в дереве """
ksCMLODOn                               = 40610
""" Упрощенное отображение """
ksCM3DArrayDestroy                      = 40615
""" Разрушить массив компонентов """
ksCMEditBilletPart                      = 40621
""" Редактировать источник для операции деталь-заготовка """
ksCMChangeBilletPart                    = 40622
""" Заменить источник для операции деталь-заготовка """
ksCMEditObject3D                        = 40707
""" Редактировать выделенный 3D объект """
ksCMEmbodimentManager                   = 40710
""" Редактор исполнений """
ksCMAdditionNumberberManager            = 40711
""" Редактор дополнительных номеров исполнений """
ksCMHideInCompCPlaces                   = 40728
""" Скрыть\\показать во вставках начала координат """
ksCMHideInCompCPlanes                   = 40729
""" Скрыть\\показать во вставках конструктивные плоскости """
ksCMHideInCompCAxies                    = 40730
""" Скрыть\\показать во вставках конструктивные оси """
ksCMHideInCompSketches                  = 40731
""" Скрыть\\показать во вставках эскизы """
ksCMHideInCompSurfaces                  = 40732
""" Скрыть\\показать во вставках поверхности """
ksCMHideInCompThreads                   = 40733
""" Скрыть\\показать во вставках изображения резьбы """
ksCMHideInCompCurves                    = 40734
""" Скрыть\\показать во вставках пространственные кривые """
ksCMHideInCompPoints                    = 40735
""" Скрыть\\показать во вставках конструктивные точки """
ksCMHideInCompAllObjects                = 40736
""" Скрыть\\показать во вставках вспомогательные объекты """
ksCMHideInCompDimensions                = 40737
""" Скрыть\\показать во вставках размеры """
ksCMHideInCompDesignations              = 40738
""" Скрыть\\показать во вставках условные обозначения """
ksCM3DSavePartAs                        = 40744
""" Преобразование Компонент деталь – компонент сборка и наоборот """
ksCM3DUnitParts                         = 40745
""" Разрушить массив компонентов """
ksCM3DAssemblyDestroy                   = 40746
""" Разрушить подсборку """
ksCMWireframeMode                       = 41882
""" Каркас """
ksCMHiddenRemovedMode                   = 41883
""" Удаление невидимых линий """
ksCMHiddenThinMode                      = 41884
""" Невидимые линии тонкие """
ksCMShadedMode                          = 41885
""" Полутоновое """
ksCMPerspective                         = 41886
""" Перспективное отображение """
ksCMShadedWireframeMode                 = 41893
""" Полутоновое с каркасом """
ksCMRotateCCW                           = 41887
""" Вращать изображение против часовой стрелки """
ksCMRotateCC                            = 41888
""" Вращать изображение по часовой стрелке """
ksCMRotate90CCW                         = 41889
""" Вращать изображение против часовой стрелки на 90гр """
ksCMRotate90CC                          = 41890
""" Вращать изображение по часовой стрелке на 90гр """
ksCMFastLines                           = 41891
""" Быстрое отображение линий """
ksCMTreeStructure                       = 41904
""" Вариант состава дерева построения """
ksCMPropertyEditor                      = 45171
""" Редактор свойств """
ksCMProcessBarVisible                   = 46541
""" Скрыть/показать панель параметров """


# properties.html
ksCMSetProperties                = 32541
""" Дополнительные свойства объектов """
ksCMSetReportStyles              = 32542
""" Поднять окно редактирования стиля отчёта """
ksEditDocumentProperties         = 37171
""" Процесс редактирования свойств документа """
ksEditInserionFragmentProperties = 37172
""" Процесс редактирования свойств вставки фрагмента """
ksEditInserionViewProperties     = 37173
""" Процесс редактирования свойств вставки вида """
ksEditMacroObjectProperties      = 37174
""" Процесс редактирования свойств макроэлемента """


class ksHideMessageEnum:  # kshidemessageenum.html
    """ ## ksHideMessageEnum - Режим скрытия сообщений и диалогов """
    ksShowMessage    = 0
    """ Показывать все сообщения и диалоги """
    ksHideMessageYes = 1
    """ Скрывать сообщения и диалоги с выбором ОК или Да, если сообщение или диалог предусматривают такой выбор, с перестроением документа. """
    ksHideMessageNo  = 2
    """ Скрывать сообщения с ОК, если имеется только кнопка ОК, сообщения и диалоги с выбором Нет, если сообщение или диалог предусматривают такой выбор, без перестроения документа """


# stoptypes.html
scsSTOPPED_FOR_MENU_COMMAND      = 1
""" - выполнена команда меню "Остановить работу библиотеки" """
scsSTOPPED_FOR_SYSTEM_STOP       = 0
""" - идет закрытие системы КОМПАС """
scsSTOPPED_FOR_ITSELF            = -1
""" - вызов функции SystemControlStop из-под библиотеки """
scsSTOPPED_FOR_START_THIS_LIB    = -2
""" - управление системе КОМПАС уже передано той же библиотекой, """
scsSTOPPED_FOR_START_ANOTHER_LIB = -3
""" - управление системе КОМПАС уже передано другой библиотекой. """


# foldertypes.html
sptSYSTEM_FILES          = 0
""" - папка системных файлов """
sptLIBS_FILES            = 1
""" - папка файлов библиотек """
sptAPPS_FILES            = 1
""" - выдать путь на каталог файлов приложений """
sptTEMP_FILES            = 2
""" - папка хранения временных файлов, """
sptCONFIG_FILE           = 3
""" - папка хранения файлов конфигурации системы """
sptINI_FILE              = 4
""" - папка хранения INI-файла системы. """
sptBIN_FILE              = 5
""" - папка исполняемых файлов системы """
sptPROJECT_FILES         = 6
""" - папка сохранения kompas.prj """
sptDESKTOP_FILES         = 7
""" - папка сохранения kompas.dsk """
sptTEMPLATES_FILES       = 8
""" - папка шаблонов КОМПАС-документов """
sptPROFILES_FILES        = 9
""" - папка сохранения профилей пользователя """
sptWORK_FILES            = 10
""" - рабочая папка """
sptSHEETMETAL_FILES      = 11
""" - папка таблиц сгибов """
sptPARTLIB_FILES         = 12
""" - папка PartLib """
sptMULTILINE_FILES       = 13
""" - папка шаблонов мультилинии """
sptPRINTDEVICE_FILES     = 14
""" - папка конфигураций плоттеров/принтеров """
sptCURR_WORK_FILES       = 15
""" - открытия/сохранения файлов документов """
sptCURR_LIBS_FILES       = 16
""" - подключения прикладных библиотек и библиотек документов """
sptCURR_APPS_FILES       = 16
""" - запоминание последних директорий, из которых выполнилось открытие/сохранение файла в диалоге Open|Save """
sptCURR_SYSTEM_FILES     = 17
""" - подключения библиотек стилей """
sptCURR_PROFILES_FILES   = 18
""" - загрузки/сохранения профиля """
sptCURR_SHEETMETAL_FILES = 19
""" - загрузки таблиц сгибов """
sptMULTY_APPS_FILES      = 20
""" - выдать список каталогов файлов приложений """
sptDOC_LIBS_FILES        = 21
""" - выдать путь на каталог файлов библиотек документов """
sptMULTY_DOC_LIBS_FILES  = 22
""" - выдать список каталогов файлов библиотек документов """
sptCUR_DOC_LIBS_FILES    = 23
""" - запоминание последних директорий, с которых выполнилось открытие/сохранение файла в диалоге Open|Save """
sptUTILS_FILES           = 24
""" - выдать путь на каталог утилит """
sptMULTY_UTILS_FILES     = 25
""" - выдать список каталогов утилит """
sptCURR_UTILS_FILES      = 26
""" - запоминание последних директорий, из которых выполнилось открытие/сохранение файла в диалоге Open|Save """
sptPROGRAMDATA_FILES     = 27
""" - Выдать путь на каталог данных приложения ( C:\\ProgramData\\ASCON\\KOMPAS-3D\\18 ) """


# sttypes.html
CURVE_STYLE    = 1
"""
- стиль кривых

ksCurveStyleParam
"""
HATCH_STYLE    = 2
"""
- стиль штриховок

ksHatchStyleParam
"""
TEXT_STYLE     = 3
"""
- стиль текста

ksTextStyleParam
"""
STAMP_STYLE    = 4
"""
- тип основной надписи

В настоящее время не реализовано
"""
CURVE_STYLE_EX = 5
"""
- расширенный стиль кривых

ksCurveStyleParam
"""


# settypes.html
DIMENTION_OPTIONS          = 1
""" Настройки размера """
SNAP_OPTIONS               = 1
""" Настройки привязок """
ARROWFILLING_OPTIONS       = 2
""" Настройки зачернения стрелок """
SHEET_OPTIONS              = 3
""" Настройка параметров оформления листа документа для новых документов """
SHEET_OPTIONS_EX           = 4
""" Настройка параметров листа документа """
LENGTHUNITS_OPTIONS        = 5
""" Настройки единиц измерений """
SNAP_OPTIONS_EX            = 6
""" Настройки привязок документа """
VIEWCOLOR_OPTIONS          = 7
""" Настройки цвета фона рабочего поля 2d - документов """
TEXTEDIT_VIEWCOLOR_OPTIONS = 8
""" Настройки цвета фона редактирования текста """
MODEL_VIEWCOLOR_OPTIONS    = 9
""" Настройки цвета фона для моделей """
OVERLAP_OBJECT_OPTIONS     = 10
""" Настройки перекрывающихся объектов """
DIMENTION_OPTIONS_EX       = 11
""" Настройки размера """


# ltypes.html
CURVE_STYLE_LIBRARY          = 1
""" - библиотека стилей кривых (*.lcs) """
HATCH_STYLE_LIBRARY          = 2
""" - библиотека стилей штриховок (*.lhs) """
TEXT_STYLE_LIBRARY           = 3
""" - библиотека стилей текстов (*.lts) """
STAMP_LAYOUT_STYLE_LIBRARY   = 4
""" - библиотека основных надписей (*.lyt) """
GRAPHIC_LAYOUT_STYLE_LIBRARY = 5
""" - библиотека оформлений графических документов (*.lyt) """
TEXT_LAYOUT_STYLE_LIBRARY    = 6
""" - библиотека оформлений текстовых документов (*.lyt) """
SPC_LAYOUT_STYLE_LIBRARY     = 7
""" - библиотека стилей спецификаций (*.lyt) """


# mtypes.html
ST_MIX_MM  = 0x1
""" - миллиметры """
ST_MIX_SM  = 0
""" - сантиметры """
ST_MIX_DM  = 0x2
""" - дециметры """
ST_MIX_M   = 0x3
""" - метры """
ST_MIX_GR  = 0
""" - граммы """
ST_MIX_KG  = 0x10
""" - килограммы """
ST_MIX_EXT = 0
""" - тело выдавливания """
ST_MIX_RV  = 0x20
""" - тело вращения """


# lentypes.html
ST_MIX_MM = 0x1
""" - миллиметры """
ST_MIX_SM = 0
""" - сантиметры """
ST_MIX_DM = 0x2
""" - дециметры """
ST_MIX_M  = 0x3
""" - метры """


# paramrestrictiontypes.html
CONSTRAINT_FIXED_POINT           = 1
""" - фиксация точки """
CONSTRAINT_POINT_ON_CURVE        = 2
""" - точка на кривой """
CONSTRAINT_HORIZONTAL            = 3
""" - горизонталь """
CONSTRAINT_VERTICAL              = 4
""" - вертикаль """
CONSTRAINT_PARALLEL              = 5
""" - параллельность двух прямых или отрезков """
CONSTRAINT_PERPENDICULAR         = 6
""" - перпендикулярность двух прямых или отрезков """
CONSTRAINT_EQUAL_LENGTH          = 7
""" - равенство длин двух отрезков """
CONSTRAINT_EQUAL_RADIUS          = 8
""" - равенство радиусов двух дуг или окружностей """
CONSTRAINT_HOR_ALIGN_POINTS      = 9
""" - выравнивание двух точек по горизонтали """
CONSTRAINT_VER_ALIGN_POINTS      = 10
""" - выравнивание двух точек по вертикали """
CONSTRAINT_MERGE_POINTS          = 11
""" - совпадение двух точек """
CONSTRAINT_TANGENT_TWO_CURVES    = 15
""" - коллинеарность отрезков """
CONSTRAINT_SYMMETRY_TWO_POINTS   = 16
""" - симметрия двух точек относительно отрезка """
CONSTRAINT_COLLINEAR             = 17
""" - коллинеарность двух отрезков """
CONSTRAINT_FIXED_ANGLE           = 18
""" - фиксированный угол """
CONSTRAINT_FIXED_LENGHT          = 19
""" - фиксированная длина """
CONSTRAINT_POINT_ON_CURVE_MIDDLE = 20
""" - точка на середине кривой """
CONSTRAINT_BISECTOR              = 21
""" - биссектриса """
CONSTRAINT_CONCENTRICITY         = 22
""" - совпадение центров окружностей, дуг, эллипсов и точек """


class LTVariant:  # datatypes.html
    """ ## Типы элементов массива LTVariant """
    ltv_Char   = 1
    """ - символ """
    ltv_Uchar  = 2
    """ - байт """
    ltv_Int    = 3
    """ - целое """
    ltv_Uint   = 4
    """ - беззнаковое целое """
    ltv_Long   = 5
    """ - длинное целое """
    ltv_Float  = 6
    """ - вещественное """
    ltv_Double = 7
    """ - двойное вещественное """
    ltv_Str    = 8
    """ - строка 255 символов """
    ltv_Short  = 10
    """ - короткое целое """


class ksHotPointEnum:  # kshotpointenum.html
    """ ## ksHotPointEnum -Типы горячих точек """
    ksHPDefault           = -1
    ksHPNormal            = 0
    """ - обычный """
    ksHPSmall             = 1
    """ - маленький """
    ksHPRing              = 2
    """ - изменение угла поворота """
    ksHPBiDirArrow        = 3
    """ - изменение длины """
    ksHPMiddlepoint       = 4
    """ - средняя точка """
    ksHPTriangleDisplaced = 5
    """ - смещенный треугольник """
    ksHPVisibilityOn      = 6
    """ - глаз - видимый объект """
    ksHPVisibilityOff     = 7
    """ - перечеркнутый глаз - скрытый объект """
    ksHPTilt              = 12
    """ - наклон """


class D3FormatConvType:  # d3formatconvtype.html
    """
    ## D3FormatConvType - Определения для конвертации в дополнительные форматы jgs, sat, xt, step, stl, VRML,C3D

    При использовании константы format_STEP сохранение выполняется в формат STEP AP203
    """
    format_SAT        = 1
    """ формат SAT """
    format_XT         = 2
    """ формат XT """
    format_STEP       = 3
    """ формат STEP """
    format_IGES       = 4
    """ формат IGES """
    format_VRML       = 5
    """ формат VRML """
    format_STL        = 6
    """ формат STL """
    format_JT         = 8
    """ формат JT """
    load_format_SAT   = -1
    """ формат SAT, для открытия документов """
    load_format_XT    = -2
    """ формат XT, для открытия документов """
    load_format_STEP  = -3
    """ формат STEP, для открытия документов """
    load_format_IGES  = -4
    """ формат IGES, для открытия документов """
    load_format_STL   = -6
    """ формат STL, для открытия документов """
    load_format_C3D   = -7
    """ формат C3D, для открытия документов математического ядра """
    load_format_JT    = -8
    """ формат JT, для открытия документов """
    load_format_OBJ   = -9
    """ формат OBJ, Для открытия документов """
    load_format_NX    = 100
    """ формат NX, для открытия документов """
    load_format_CREO  = 101
    """ формат CREO, для открытия документов """
    load_format_SW    = 102
    """ формат SolidWorks, для открытия документов """
    load_format_INV   = 103
    """ формат Inventor, для открытия документов """
    load_format_CATIA = 104
    """ формат Catia, для открытия документов """
    load_format_SE    = 105
    """ Формат SolidEdge. Для открытия документов """
    format_STEP_AP203 = 203
    """ формат STEP AP203. Прикладной протокол 203 (Проектирование с управляемой конфигурацией) """
    format_STEP_AP214 = 214
    """ формат STEP AP214. Прикладной протокол 214 (Проектирование автомобилей ) """
    format_STEP_AP242 = 242
    """ формат STEP AP242.Прикладной протокол 242 (Проектирование автомобилей ) """


class Positioner_Type:  # positioner_type.html
    """ ## Positioner_Type - Тип перемещения """
    pnMove   = 0
    """ сдвиг """
    pnRotate = 1
    """ вращение """


class MateConstraintType:  # mateconstrainttype.html
    """ ## MateConstraintType - Типы сопряжений """
    mc_Coincidence   = 0
    """ совпадение объектов """
    mc_Parallel      = 1
    """ параллельность """
    mc_Perpendicular = 2
    """ перпендикулярность """
    mc_Tangency      = 3
    """ касательность """
    mc_Concentric    = 4
    """ концентричность """
    mc_Distance      = 5
    """ постоянное расстояние между объектами """
    mc_Angle         = 6
    """ постоянный угол между объектами """
    mc_InPlace       = 7
    """ создание компонента "на месте" (эквивалентно совпадению системы координат плоскости, на которой создается компонент, и системы координат плоскости первого эскиза этого компонента) """
    mc_Transmission  = 9
    """ Механическая передача """
    mc_CamGear       = 10
    """ Кулачковый механизм. Кулачек-толкатель """
    mc_Symmetric     = 11
    """ Симметрия """
    mc_Dependent     = 14
    """ Зависимое положение """


class ksTypeLookStyle:  # kstypelookstyle.html
    """ ## ksTypeLookStyle - Тип отрисовки визуальной части """
    tls_VisualStudio_97           = 0
    """ Microsoft Visual Studio 97 """
    tls_VisualStudio_NET          = 1
    """ Microsoft Visual Studio.NET 2003 """
    tls_Office_2003               = 2
    """ Microsoft Office 2003 """
    tls_VisualStudio2005          = 3
    """ Microsoft Visual Studio 2005 """
    tls_WindowsXP                 = 4
    """ Microsoft Windows XP native look """
    tls_Office_2007               = 5
    """ Microsoft Office 2007 """
    tls_Office_2007_LunaBlue      = 5
    """ Microsoft Office 2007. Luna Blue """
    tls_Office_2007_ObsidianBlack = 6
    """ Microsoft Office 2007. Obsidian Black """
    tls_Office_2007_Aqua          = 7
    """ Microsoft Office 2007. Aqua """
    tls_Office_2007_Silver        = 8
    """ Microsoft Office 2007. Silver """
    tls_VisualStudio2008          = 9
    """ Microsoft Visual Studio 2008 """
    tls_VisualStudio2010          = 10
    """ Microsoft Visual Studio 2010 """
    tls_Office_2010_Blue          = 11
    """ Microsoft Office 2010 Blue """
    tls_Office_2010_Dark          = 12
    """ Microsoft Office 2010 Dark """
    tls_Office_2010_White         = 13
    """ Microsoft Office 2010 White """
    tls_Carbon                    = 14
    """ Carbon """


class ViewMode:  # viewmode.html
    """ ## ViewMode - Способы отображения моделей """
    vm_Wireframe     = 0
    """ каркас """
    vm_HiddenRemoved = 1
    """ без невидимых линий """
    vm_HiddenThin    = 2
    """ невидимые линии тонкие """
    vm_Shaded        = 3
    """ полутоновой """


class ksLineBuildingType:  # kslinebuildingtype.html
    """ ## ksLineBuildingType - Способ построения сегмента ломаной """
    ksLBTByPoint       = 0
    """ По точкам """
    ksLBTXDirection    = 1
    """ По оси X """
    ksLBTYDirection    = 2
    """ По оси Y """
    ksLBTZDirection    = 3
    """ По оси Z """
    ksLBTParallel      = 4
    """ Параллельно объекту """
    ksLBTPerpendicular = 5
    """ Перпендикулярно объекту """
    ksLineBuildingType = 6
    """ Через построение точки """


class Direction_Type:  # direction_type.html
    """
    ## Direction_Type - Типы направлений выдавливания

    1. При типе направления dtMiddlePlane в методах SetSideParam и GetSideParam параметр depth интерпретируется как общая глубина выдавливания и задается следующим образом:

    SetSideParam(TRUE, etBlind, depth,...)

    2. В API7 соответствует перечислению ksDirectionTypeEnum.
    """
    dtNormal      = 0
    """ прямое направление (для тонкой стенки - наружу) """
    dtReverse     = 1
    """ обратное направление (для тонкой стенки - внутрь) """
    dtBoth        = 2
    """ в обе стороны """
    dtMiddlePlane = 3
    """ от средней плоскости """


class ksContour3DBuildingTypeTypeEnum:  # kscontour3dbuildingtypetypeenum.html
    """ ## ksContour3DBuildingTypeTypeEnum - Способ построения Контура 3D """
    ksCBTUnknown     = 0
    """ Не определен """
    ksCBTEdges       = 1
    """ Ребрами """
    ksCBTEquidistant = 2
    """ Эквидистанта """


class ksObj3dTypeEnum:  # obj3dtype.html
    """
    ## Obj3dType (ksObj3dTypeEnum) - Типы объектов документа-модели; соответствие интерфейсов API 5 и API 7

    В таблице представлены идентификаторы объектов для интерфейсов API 5 и API 7.
    """
    o3d_unknown                       = 0
    """ Название объекта: неизвестный (включает все объекты) """
    o3d_planeXOY                      = 1
    """
    Название объекта: плоскость XOY

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IPlane3D
    """
    o3d_planeXOZ                      = 2
    """
    Название объекта: плоскость XOZ

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IPlane3D
    """
    o3d_planeYOZ                      = 3
    """
    Название объекта: плоскость YOZ

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IPlane3D
    """
    o3d_pointCS                       = 4
    """
    Название объекта: точка начала системы координат

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IModelObject
    """
    o3d_sketch                        = 5
    """
    Название объекта: эскиз

    Интерфейс параметров API 5: ksSketchDefinition

    Интерфейс параметров API 7: ISketch
    """
    o3d_face                          = 6
    """
    Название объекта: поверхность

    Интерфейс параметров API 5: ksFaceDefinition

    Интерфейс параметров API 7: IFace
    """
    o3d_edge                          = 7
    """
    Название объекта: ребро

    Интерфейс параметров API 5: ksEdgeDefinition

    Интерфейс параметров API 7: IEdge
    """
    o3d_vertex                        = 8
    """
    Название объекта: вершина

    Интерфейс параметров API 5: ksVertexDefinition

    Интерфейс параметров API 7: IVertex
    """
    o3d_axis2Planes                   = 9
    """
    Название объекта: ось по двум плоскостям

    Интерфейс параметров API 5: ksAxis2PlanesDefinition

    Интерфейс параметров API 7: IAxis3DBy2Planes
    """
    o3d_axis2Points                   = 10
    """
    Название объекта: ось по двум точкам

    Интерфейс параметров API 5: ksAxis2PointsDefinition

    Интерфейс параметров API 7: IAxis3DBy2Points
    """
    o3d_axisConeFace                  = 11
    """
    Название объекта: ось конической грани

    Интерфейс параметров API 5: ksAxisConefaceDefinition

    Интерфейс параметров API 7: IAxis3DByConeface
    """
    o3d_axisEdge                      = 12
    """
    Название объекта: ось, проходящая через ребро

    Интерфейс параметров API 5: ksAxisEdgeDefinition

    Интерфейс параметров API 7: IAxis3DByEdge
    """
    o3d_axisOperation                 = 13
    """
    Название объекта: ось операции

    Интерфейс параметров API 5: ksAxisOperationsDefinition

    Интерфейс параметров API 7: IAxis3DByOperation
    """
    o3d_planeOffset                   = 14
    """
    Название объекта: смещённая плоскость

    Интерфейс параметров API 5: ksPlaneOffsetDefinition

    Интерфейс параметров API 7: IPlane3DByOffset
    """
    o3d_planeAngle                    = 15
    """
    Название объекта: плоскость под углом

    Интерфейс параметров API 5: ksPlaneAngleDefinition

    Интерфейс параметров API 7: IPlane3DByAngle
    """
    o3d_plane3Points                  = 16
    """
    Название объекта: плоскость по 3-м точкам

    Интерфейс параметров API 5: ksPlane3PointsDefinition

    Интерфейс параметров API 7: IPlane3DBy3Points
    """
    o3d_planeNormal                   = 17
    """
    Название объекта: нормальная плоскость

    Интерфейс параметров API 5: ksPlaneNormalToSurfaceDefinition

    Интерфейс параметров API 7: IPlane3DNormalToSurface
    """
    o3d_planeTangent                  = 18
    """
    Название объекта: касательная плоскость

    Интерфейс параметров API 5: ksPlaneTangentToSurfaceDefinition

    Интерфейс параметров API 7: IPlane3DTangentToFace
    """
    o3d_planeEdgePoint                = 19
    """
    Название объекта: плоскость через ребро и вершину

    Интерфейс параметров API 5: ksPlaneEdgePointDefinition

    Интерфейс параметров API 7: IPlane3DByEdgeAndPoint
    """
    o3d_planeParallel                 = 20
    """
    Название объекта: плоскость через вершину параллельно другой плоскости

    Интерфейс параметров API 5: ksPlaneParallelDefinition

    Интерфейс параметров API 7: IPlane3DParallelByPoint
    """
    o3d_planePerpendicular            = 21
    """
    Название объекта: плоскость через вершину перпендикулярно ребру

    Интерфейс параметров API 5: ksPlanePerpendicularDefinition

    Интерфейс параметров API 7: IPlane3DPerpendicularByEdge
    """
    o3d_planeLineToEdge               = 22
    """
    Название объекта: плоскость через ребро параллельно /перпендикулярно другому ребру

    Интерфейс параметров API 5: ksPlaneLineToEdgeDefinition

    Интерфейс параметров API 7: IPlane3DBy2Edge
    """
    o3d_planeLineToPlane              = 23
    """
    Название объекта: плоскость через ребро параллельно /перпендикулярно грани

    Интерфейс параметров API 5: ksPlaneLineToPlaneDefinition

    Интерфейс параметров API 7: IPlane3DByEdgeAndPlane
    """
    o3d_baseExtrusion                 = 24
    """
    Название объекта: базовая операция выдавливания

    Интерфейс параметров API 5: ksBaseExtrusionDefinition

    Интерфейс параметров API 7: IExtrusion
    """
    o3d_bossExtrusion                 = 25
    """
    Название объекта: приклеивание выдавливанием

    Интерфейс параметров API 5: ksBossExtrusionDefinition

    Интерфейс параметров API 7: IExtrusion
    """
    o3d_cutExtrusion                  = 26
    """
    Название объекта: вырезать выдавливанием

    Интерфейс параметров API 5: ksCutExtrusionDefinition

    Интерфейс параметров API 7: ICutExtrusion
    """
    o3d_baseRotated                   = 27
    """
    Название объекта: базовая операция вращения

    Интерфейс параметров API 5: ksBaseRotatedDefinition

    Интерфейс параметров API 7: IRotated
    """
    o3d_bossRotated                   = 28
    """
    Название объекта: приклеивание вращением

    Интерфейс параметров API 5: ksBossRotatedDefinition

    Интерфейс параметров API 7: IRotated
    """
    o3d_cutRotated                    = 29
    """
    Название объекта: вырезать вращением

    Интерфейс параметров API 5: ksCutRotatedDefinition

    Интерфейс параметров API 7: ICutRotated
    """
    o3d_baseLoft                      = 30
    """
    Название объекта: базовая операция по сечениям

    Интерфейс параметров API 5: ksBaseLoftDefinition

    Интерфейс параметров API 7: ILoft
    """
    o3d_bossLoft                      = 31
    """
    Название объекта: приклеивание по сечениям

    Интерфейс параметров API 5: ksBossLoftDefinition

    Интерфейс параметров API 7: ILoft
    """
    o3d_cutLoft                       = 32
    """
    Название объекта: вырезать по сечениям

    Интерфейс параметров API 5: ksCutLoftDefinition

    Интерфейс параметров API 7: ILoft
    """
    o3d_chamfer                       = 33
    """
    Название объекта: операция "фаска"

    Интерфейс параметров API 5: ksChamferDefinition

    Интерфейс параметров API 7: IChamfer
    """
    o3d_fillet                        = 34
    """
    Название объекта: операция "скругление"

    Интерфейс параметров API 5: ksFilletDefinition

    Интерфейс параметров API 7: IFillet
    """
    o3d_meshCopy                      = 35
    """
    Название объекта: операция копирования по сетке

    Интерфейс параметров API 5: ksMeshCopyDefinition

    Интерфейс параметров API 7: ILinearPattern
    """
    o3d_circularCopy                  = 36
    """
    Название объекта: операция копирования по концентрической сетке

    Интерфейс параметров API 5: ksCircularCopyDefinition

    Интерфейс параметров API 7: ICircularPattern
    """
    o3d_curveCopy                     = 37
    """
    Название объекта: операция копирования по кривой

    Интерфейс параметров API 5: ksCurveCopyDefinition

    Интерфейс параметров API 7: IPathPattern
    """
    o3d_circPartArray                 = 38
    """
    Название объекта: операция массив по концентрической сетке для сборки

    Интерфейс параметров API 5: ksCircularPartArrayDefinition

    Интерфейс параметров API 7: ICircularPattern
    """
    o3d_meshPartArray                 = 39
    """
    Название объекта: операция массив по сетке для сборки

    Интерфейс параметров API 5: ksMeshPartArrayDefinition

    Интерфейс параметров API 7: ILinearPattern
    """
    o3d_curvePartArray                = 40
    """
    Название объекта: операция массив по кривой для сборки

    Интерфейс параметров API 5: ksCurvePartArrayDefinition

    Интерфейс параметров API 7: IPathPattern
    """
    o3d_derivPartArray                = 41
    """
    Название объекта: операция массив по образцу для сборки

    Интерфейс параметров API 5: ksDerivativePartArrayDefinition

    Интерфейс параметров API 7: IDerivedPattern
    """
    o3d_incline                       = 42
    """
    Название объекта: операция "уклон"

    Интерфейс параметров API 5: ksInclineDefinition

    Интерфейс параметров API 7: IIncline
    """
    o3d_shellOperation                = 43
    """
    Название объекта: операция "оболочка"

    Интерфейс параметров API 5: ksShellDefinition

    Интерфейс параметров API 7: IShell
    """
    o3d_ribOperation                  = 44
    """
    Название объекта: операция "ребро жесткости"

    Интерфейс параметров API 5: ksRibDefinition

    Интерфейс параметров API 7: IRib
    """
    o3d_baseEvolution                 = 45
    """
    Название объекта: кинематическая операция

    Интерфейс параметров API 5: ksBaseEvolutionDefinition

    Интерфейс параметров API 7: IEvolution
    """
    o3d_bossEvolution                 = 46
    """
    Название объекта: приклеить кинематически

    Интерфейс параметров API 5: ksBossEvolutionDefinition

    Интерфейс параметров API 7: IEvolution
    """
    o3d_cutEvolution                  = 47
    """
    Название объекта: вырезать кинематически

    Интерфейс параметров API 5: ksCutEvolutionDefinition

    Интерфейс параметров API 7: IEvolution
    """
    o3d_mirrorOperation               = 48
    """
    Название объекта: операция "зеркальный массив"

    Интерфейс параметров API 5: ksMirrorCopyDefinition

    Интерфейс параметров API 7: IMirrorPattern
    """
    o3d_mirrorAllOperation            = 49
    """
    Название объекта: операция "зеркально отразить все"

    Интерфейс параметров API 5: ksMirrorCopyAllDefinition

    Интерфейс параметров API 7: IMirrorPattern
    """
    o3d_cutByPlane                    = 50
    """
    Название объекта: операция "сечение поверхностью"

    Интерфейс параметров API 5: ksCutByPlaneDefinition

    Интерфейс параметров API 7: ICut
    """
    o3d_cutBySketch                   = 51
    """
    Название объекта: операция "сечение эскизом"

    Интерфейс параметров API 5: ksCutBySketchDefinition

    Интерфейс параметров API 7: ICut
    """
    o3d_holeOperation                 = 52
    """ Название объекта: отверстие """
    o3d_polyline                      = 53
    """
    Название объекта: ломаная

    Интерфейс параметров API 5: ksPolyLineDefinition

    Интерфейс параметров API 7: IPolyLine
    """
    o3d_conicSpiral                   = 54
    """
    Название объекта: коническая спираль

    Интерфейс параметров API 5: ksConicSpiralDefinition

    Интерфейс параметров API 7: IConicSpiral3D
    """
    o3d_spline                        = 55
    """
    Название объекта: сплайн

    Интерфейс параметров API 5: ksSplineDefinition

    Интерфейс параметров API 7: ISpline3D
    """
    o3d_cylindricSpiral               = 56
    """
    Название объекта: цилиндрическая спираль

    Интерфейс параметров API 5: ksCylindricSpiralDefinition

    Интерфейс параметров API 7: ICylindricSpiral3D
    """
    o3d_importedSurface               = 57
    """
    Название объекта: импортирванная поверхность

    Интерфейс параметров API 5: ksImportedSurfaceDefinition

    Интерфейс параметров API 7: IImportedSurface
    """
    o3d_thread                        = 58
    """
    Название объекта: условное изображение резьбы

    Интерфейс параметров API 5: ksThreadDefinition

    Интерфейс параметров API 7: IThread
    """
    o3d_EvolutionSurface              = 59
    """
    Название объекта: кинематическая поверхность

    Интерфейс параметров API 5: ksEvolutionSurfaceDefinition

    Интерфейс параметров API 7: IEvolution
    """
    o3d_ExtrusionSurface              = 60
    """
    Название объекта: поверхность выдавливания

    Интерфейс параметров API 5: ksExtrusionSurfaceDefinition

    Интерфейс параметров API 7: IExtrusionSurface
    """
    o3d_RotatedSurface                = 61
    """
    Название объекта: поверхность вращения

    Интерфейс параметров API 5: ksRotatedSurfaceDefinition

    Интерфейс параметров API 7: IRotatedSurface
    """
    o3d_LoftSurface                   = 62
    """
    Название объекта: поверхность по сечениям

    Интерфейс параметров API 5: ksLoftSurfaceDefinition

    Интерфейс параметров API 7: ILoft
    """
    o3d_MacroObject                   = 63
    """
    Название объекта: макроэлемент 3D

    Интерфейс параметров API 5: ksMacro3DDefinition

    Интерфейс параметров API 7: IMacroObject3D
    """
    o3d_UnionComponents               = 64
    """
    Название объекта: операция объединения компонентов

    Интерфейс параметров API 5: ksUnionComponentsDefinition

    Интерфейс параметров API 7: IUnionComponents
    """
    o3d_MoldCavity                    = 65
    """
    Название объекта: операция вычитания компонентов

    Интерфейс параметров API 5: ksMoldCavityDefinition

    Интерфейс параметров API 7: IMoldCavity
    """
    o3d_planeMiddle                   = 66
    """
    Название объекта: средняя плоскость

    Интерфейс параметров API 5: ksPlaneMiddleDefinition

    Интерфейс параметров API 7: IPlane3DMiddle
    """
    o3d_controlPoint                  = 67
    """
    Название объекта: контрольная точка

    Интерфейс параметров API 5: ksControlPointDefinition

    Интерфейс параметров API 7: IControlPoint
    """
    o3d_conjunctivePoint              = 68
    """
    Название объекта: присоединительная точка

    Интерфейс параметров API 5: ksConjunctivePointDefinition

    Интерфейс параметров API 7: IConjunctivePoint
    """
    o3d_aggregate                     = 69
    """
    Название объекта: Булева операция

    Интерфейс параметров API 5: ksAggregateDefinition

    Интерфейс параметров API 7: IBoolean
    """
    o3d_point3D                       = 70
    """
    Название объекта: Конструктивная 3D точка

    Интерфейс параметров API 7: IPoint3D
    """
    o3d_axisOX                        = 71
    """
    Название объекта: Ось OX

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IAxis3D
    """
    o3d_axisOY                        = 72
    """
    Название объекта: Ось OY

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IAxis3D
    """
    o3d_axisOZ                        = 73
    """
    Название объекта: Ось OZ

    Интерфейс параметров API 5: ksDefaultObject

    Интерфейс параметров API 7: IAxis3D
    """
    o3d_sheetMetalBody                = 74
    """
    Название объекта: Листовое тело

    Интерфейс параметров API 7: ISheetMetalBody
    """
    o3d_sheetMetalBend                = 75
    """
    Название объекта: Сгиб

    Интерфейс параметров API 7: ISheetMetalBend
    """
    o3d_sheetMetalLineBend            = 76
    """
    Название объекта: Сгиб по линии

    Интерфейс параметров API 7: ISheetMetalLineBend
    """
    o3d_sheetMetalHole                = 77
    """
    Название объекта: Элемент листового тела "отверстие"

    Интерфейс параметров API 7: ISheetMetalHole
    """
    o3d_sheetMetalCut                 = 78
    """
    Название объекта: Элемент листового тела "вырез"

    Интерфейс параметров API 7: ISheetMetalCut
    """
    o3d_UnHistoried                   = 79
    """ Название объекта: Операция без истории """
    o3d_baselineDimension3D           = 80
    """
    Название объекта: Линейный размер 3D (от отрезка до точки)

    Интерфейс параметров API 7: IBaseLineDimension3D
    """
    o3d_lineDimension3D               = 81
    """
    Название объекта: Линейный размер 3D (на плоскости)

    Интерфейс параметров API 7: ILineDimension3D
    """
    o3d_radialDimension3D             = 82
    """
    Название объекта: Радиальный размер 3D

    Интерфейс параметров API 7: IRadialDimension3D
    """
    o3d_diametralDimension3D          = 83
    """
    Название объекта: Диаметральный размер 3D

    Интерфейс параметров API 7: IDiametralDimension3D
    """
    o3d_angleDimension3D              = 84
    """
    Название объекта: Угловой размер 3D

    Интерфейс параметров API 7: IAngleDimension3D
    """
    o3d_localCoordinateSystem         = 85
    """
    Название объекта: Локальная система координат

    Интерфейс параметров API 7: ILocalCoordinateSystem
    """
    o3d_leader3D                      = 86
    """
    Название объекта: Линия-выноска 3D

    Интерфейс параметров API 7: ILeader
    """
    o3d_markLeader3D                  = 87
    """
    Название объекта: Знак маркировки 3D

    Интерфейс параметров API 7: IMarkLeader
    """
    o3d_rough3D                       = 88
    """
    Название объекта: Обозначение 3D шероховатости

    Интерфейс параметров API 7: IRough3D
    """
    o3d_positionLeader3D              = 89
    """
    Название объекта: Обозначение позиции 3D

    Интерфейс параметров API 7: IPositionLeader
    """
    o3d_brandLeader3D                 = 90
    """
    Название объекта: Знак клеймения 3D

    Интерфейс параметров API 7: IBrandLeader
    """
    o3d_base3D                        = 91
    """
    Название объекта: Обозначение 3D базы

    Интерфейс параметров API 7: IBase3D
    """
    o3d_tolerance3D                   = 92
    """
    Название объекта: Допуск формы 3D

    Интерфейс параметров API 7: ITolerance3D
    """
    o3d_SplitLine                     = 93
    """
    Название объекта: Линия разъема

    Интерфейс параметров API 7: ISplitLine
    """
    o3d_SurfacePatch                  = 94
    """
    Название объекта: Заплатка

    Интерфейс параметров API 7: ISurfacePatch
    """
    o3d_FaceRemover                   = 95
    """
    Название объекта: Операция удаления граней

    Интерфейс параметров API 7: IFaceRemover
    """
    o3d_SurfaceSewer                  = 96
    """
    Название объекта: Операция сшивки поверхностей

    Интерфейс параметров API 7: ISurfaceSewer
    """
    o3d_NurbsSurface                  = 97
    """
    Название объекта: NURBS-поверхность

    Интерфейс параметров API 7: INurbsSurface
    """
    o3d_SurfacesIntersectionCurve     = 98
    """
    Название объекта: Кривая пересечения поверхностей

    Интерфейс параметров API 7: ISurfacesIntersectionCurve
    """
    o3d_lastEntityElement             = 99
    """ Название объекта: Всегда последний из Entity!!! """
    o3d_variable                      = 100
    """
    Название объекта: параметрическая переменная

    Интерфейс параметров API 5: ksVariable

    Интерфейс параметров API 7: IVariable7
    """
    o3d_placement                     = 101
    """
    Название объекта: местоположение

    Интерфейс параметров API 5: ksPlacement

    Интерфейс параметров API 7: IPlacement3D
    """
    o3d_entityCollection              = 102
    """
    Название объекта: Массив трехмерных объектов

    Интерфейс параметров API 5: ksEntityCollection
    """
    o3d_document                      = 103
    """
    Название объекта: Документ-модель

    Интерфейс параметров API 5: ksDocument3D

    Интерфейс параметров API 7: IKompasDocument3D
    """
    o3d_part                          = 104
    """
    Название объекта: Деталь

    Интерфейс параметров API 5: ksPart

    Интерфейс параметров API 7: IPart7
    """
    o3d_entity                        = 105
    """
    Название объекта: Объект

    Интерфейс параметров API 5: ksEntity

    Интерфейс параметров API 7: IModelObject
    """
    o3d_mateConstraint                = 106
    """
    Название объекта: сопряжение

    Интерфейс параметров API 5: ksMateConstraint

    Интерфейс параметров API 7: IMateConstraint3D
    """
    o3d_mateConstraintCollection      = 107
    """
    Название объекта: Массив сопряжений

    Интерфейс параметров API 5: ksMateConstraintCollection

    Интерфейс параметров API 7: IMateConstraints3D
    """
    o3d_partCollection                = 108
    """
    Название объекта: Массив элементов сборки

    Интерфейс параметров API 5: ksPartCollection

    Интерфейс параметров API 7: IParts7
    """
    o3d_constrElement                 = 109
    """ Название объекта: конструктивные элементы-плоскости и оси (конструктивные от o3d_axis2Planes до o3d_plane3Points) """
    o3d_operationElement              = 110
    """ Название объекта: Операции (от o3d_baseExtrusion до o3d_cylindricSpiral) """
    o3d_curveElement                  = 111
    """ Название объекта: Кривые (пространственные и ребра) """
    o3d_rasterFormat                  = 112
    """
    Название объекта: интерфейс параметров для конвертации в растровый формат

    Интерфейс параметров API 5: ksRasterFormatParam
    """
    o3d_additionFormat                = 113
    """
    Название объекта: интерфейс параметров для конвертации в дополнительные форматы: jgs, sat, xt, x_b, step, stl, VRML

    Интерфейс параметров API 5: ksAdditionFormatParam
    """
    o3d_bodyCollection                = 114
    """
    Название объекта: интерфейс массива трехмерных тел

    Интерфейс параметров API 5: ksBodyCollection
    """
    o3d_body                          = 115
    """
    Название объекта: интерфейс трехмерного тела

    Интерфейс параметров API 5: ksBody

    Интерфейс параметров API 7: IBody7
    """
    o3d_faceCollection                = 116
    """
    Название объекта: интерфейс массива граней

    Интерфейс параметров API 5: ksFaceCollection
    """
    o3d_tessellation                  = 117
    """
    Название объекта: интерфейс триангуляции

    Интерфейс параметров API 5: ksTessellation

    Интерфейс параметров API 7: ITesselllation7
    """
    o3d_facet                         = 118
    """
    Название объекта: интерфейс триангуляционной пластины

    Интерфейс параметров API 5: ksFacet
    """
    o3d_featureCollection             = 119
    """
    Название объекта: интерфейс массива объектов дерева

    Интерфейс параметров API 5: ksFeatureCollection
    """
    o3d_feature                       = 120
    """
    Название объекта: интерфейс объекта дерева

    Интерфейс параметров API 5: ksFeature

    Интерфейс параметров API 7: IFeature7
    """
    o3d_edgeCollection                = 121
    """
    Название объекта: интерфейс массива ребер

    Интерфейс параметров API 5: ksEdgeCollection
    """
    o3d_orientedEdge                  = 122
    """
    Название объекта: интерфейс ориентированного ребра

    Интерфейс параметров API 5: ksOrientedEdge

    Интерфейс параметров API 7: IOrientedEdge7
    """
    o3d_orientedEdgeCollection        = 123
    """
    Название объекта: интерфейс массива ориентированных ребер

    Интерфейс параметров API 5: ksOrientedEdgeCollection
    """
    o3d_loop                          = 124
    """
    Название объекта: интерфейс цикла

    Интерфейс параметров API 5: ksLoop

    Интерфейс параметров API 7: ILoop7
    """
    o3d_loopCollection                = 125
    """
    Название объекта: интерфейс массива циклов

    Интерфейс параметров API 5: ksLoopCollection
    """
    o3d_curve3D                       = 126
    """
    Название объекта: интерфейс математической кривой в трехмерном пространстве

    Интерфейс параметров API 5: ksCurve3D

    Интерфейс параметров API 7: IMathCurve3D
    """
    o3d_surface                       = 127
    """
    Название объекта: интерфейс математической поверхности в трехмерном пространстве

    Интерфейс параметров API 5: ksSurface

    Интерфейс параметров API 7: IMathSurface3D
    """
    o3d_massInertiaParam              = 128
    """
    Название объекта: Интерфейс параметров для расчета массово-центровочных характеристик

    Интерфейс параметров API 5: ksMassInertiaParam

    Интерфейс параметров API 7: IMassInertiaParam7
    """
    o3d_line3dParam                   = 129
    """
    Название объекта: Интерфейс параметров 3dLine

    Интерфейс параметров API 5: ksLineSeg3dParam
    """
    o3d_circle3dParam                 = 130
    """
    Название объекта: Интерфейс параметров 3dCircle

    Интерфейс параметров API 5: ksCircle3dParam
    """
    o3d_ellipse3dParam                = 131
    """
    Название объекта: Интерфейс параметров 3dEllipce

    Интерфейс параметров API 5: ksEllipse3dParam
    """
    o3d_nurbsPoint3dParam             = 132
    """
    Название объекта: Интерфейс параметров точки для трехмерной NURBS

    Интерфейс параметров API 5: ksNurbsPoint3dParam
    """
    o3d_nurbsPoint3dCollection        = 133
    """
    Название объекта: Интерфейс массива точек для трехмерной NURBS

    Интерфейс параметров API 5: ksNurbsPoint3dCollection
    """
    o3d_nurbsPoint3dCollCollection    = 134
    """
    Название объекта: Интерфейс массива массивов точек для трехмерной NURBS поверхности

    Интерфейс параметров API 5: ksNurbsPoint3dCollCollection
    """
    o3d_nurbsKnotCollection           = 135
    """
    Название объекта: Интерфейс массива узлов для трехмерного NURBS

    Интерфейс параметров API 5: ksNurbsKnotCollection
    """
    o3d_nurbs3dParam                  = 136
    """
    Название объекта: Интерфейс параметров трехмерного NURBS

    Интерфейс параметров API 5: ksNurbs3dParam
    """
    o3d_planeParam                    = 137
    """
    Название объекта: Интерфейс параметров плоскости

    Интерфейс параметров API 5: ksPlaneParam
    """
    o3d_coneParam                     = 138
    """
    Название объекта: Интерфейс параметров конической поверхности

    Интерфейс параметров API 5: ksConeParam
    """
    o3d_cylinderParam                 = 139
    """
    Название объекта: Интерфейс параметров цилиндрической поверхности

    Интерфейс параметров API 5: ksCylinderParam
    """
    o3d_sphereParam                   = 140
    """
    Название объекта: Интерфейс параметров сферы

    Интерфейс параметров API 5: ksSphereParam
    """
    o3d_torusParam                    = 141
    """
    Название объекта: Интерфейс параметров тора

    Интерфейс параметров API 5: ksTorusParam
    """
    o3d_nurbsSurfaceParam             = 142
    """
    Название объекта: Интерфейс параметров NURBS-поверхности

    Интерфейс параметров API 5: ksNurbsSurfaceParam
    """
    o3d_mateConstraintGroup           = 143
    """
    Название объекта: Объект дерева: группа сопряжений

    Интерфейс параметров API 5: IModelObject

    Интерфейс параметров API 7: IFeature7
    """
    o3d_measurer                      = 144
    """
    Название объекта: Интерфейс для измерений расстояния и угла между двумя примитивами (гранями, ребрами, вершинами)

    Интерфейс параметров API 5: ksMeasurer
    """
    o3d_selectionMng                  = 145
    """
    Название объекта: Интерфейс менеджера выделенных объектов

    Интерфейс параметров API 5: ksSelectionMng

    Интерфейс параметров API 7: ISelectionManager
    """
    o3d_chooseMng                     = 146
    """
    Название объекта: Интерфейс менеджера выбора (подсветки) объектов

    Интерфейс параметров API 5: ksChooseMng

    Интерфейс параметров API 7: IChooseManager
    """
    o3d_arc3dParam                    = 147
    """
    Название объекта: Интерфейс параметров трехмерной дуги

    Интерфейс параметров API 5: ksArc3dParam
    """
    o3d_deletedCopyCollection         = 148
    """
    Название объекта: Интерфейс массива удаленных индексов для операций копирования и массивов компонент

    Интерфейс параметров API 5: ksDeletedCopyCollection
    """
    o3d_viewProjection                = 149
    """
    Название объекта: Интерфейс проекции отображения модели в окне

    Интерфейс параметров API 5: ksViewProjection
    """
    o3d_viewProjectionCollection      = 150
    """
    Название объекта: Интерфейс массива проекций отображения модели в окне

    Интерфейс параметров API 5: ksViewProjectionCollection
    """
    o3d_attribute                     = 151
    """
    Название объекта: Интерфейс атрибута объекта модели

    Интерфейс параметров API 5: ksAttribute3D

    Интерфейс параметров API 7: IAttribute
    """
    o3d_attributeCollection           = 152
    """
    Название объекта: Интерфейс массива атрибутов объекта модели

    Интерфейс параметров API 5: ksAttribute3DCollection
    """
    o3d_componentPositioner           = 153
    """
    Название объекта: Интерфейс управления положением компонентов в сборке

    Интерфейс параметров API 5: ksComponentPositioner
    """
    o3d_modelLibrary                  = 154
    """
    Название объекта: Интерфейс библиотеки моделей

    Интерфейс параметров API 5: ksModelLibrary

    Интерфейс параметров API 7: IInsertsLibrary
    """
    o3d_ObjectsFilter3D               = 155
    """ Название объекта: Не используется """
    o3d_coordinate3dCollection        = 156
    """
    Название объекта: Интерфейс коллекции координат

    Интерфейс параметров API 5: ksCoordinate3dCollection
    """
    o3d_intersectionResult            = 157
    """
    Название объекта: Интерфейс результатов пересечений двух тел

    Интерфейс параметров API 5: ksIntersectionResult
    """
    o3d_PolygonalLineVertexParam      = 158
    """
    Название объекта: Параметры вершины полилинии

    Интерфейс параметров API 5: ksPolyLineVertexParam

    Интерфейс параметров API 7: ICurveVertexParam
    """
    o3d_variableCollection            = 159
    """
    Название объекта: Массив параметрических переменных

    Интерфейс параметров API 5: ksvariableCollection
    """
    o3d_sTrackingPointsMeasurer       = 160
    """
    Название объекта: Интерфейс для расчета координат точек при S- образном соединении прямолинейных рёбер

    Интерфейс параметров API 5: IsTrackingPointsMeasurer
    """
    o3d_surfaceElement                = 161
    """ Название объекта: Поверхности """
    o3d_designationElemen             = 162
    """ Название объекта: Размеры и условные обозначения """
    o3d_copyleftObject                = 163
    """ Название объекта: Объекты доступные для копирования """
    o3d_Embodiment                    = 164
    """
    Название объекта: Исполнение

    Интерфейс параметров API 7: IEmbodiment
    """
    o3d_userMateConstraint            = 165
    """
    Название объекта: Пользовательское сопряжение

    Интерфейс параметров API 7: IMateConstraint + IUserObject3D
    """
    o3d_intervalVariable              = 166
    """ Название объекта: Интервальная переменная """
    o3d_userFunc                      = 167
    """ Название объекта: Функциональная переменная """
    o3d_firstEntityElement2           = 500
    """ Название объекта: Первый из Entity2!!! """
    o3d_Equidistant3D                 = 501
    """
    Название объекта: Эквидистанта 3D

    Интерфейс параметров API 7: IEquidistant3D
    """
    o3d_TrimmedCurve                  = 502
    """
    Название объекта: Операция усечения кривой

    Интерфейс параметров API 7: ITrimmedCurve
    """
    o3d_TrimmedCurveObject            = 503
    """
    Название объекта: Усеченная кривая

    Интерфейс параметров API 7: ITrimmedCurve
    """
    o3d_AuxMeshCopy                   = 504
    """
    Название объекта: Массив вспомогательной геометрии по сетке

    Интерфейс параметров API 7: ILinearPattern
    """
    o3d_AuxCircularCopy               = 505
    """
    Название объекта: Массив вспомогательной геометрии по концентрической сетке

    Интерфейс параметров API 7: ICircularPattern
    """
    o3d_AuxCurveCopy                  = 506
    """
    Название объекта: Массив вспомогательной геометрии вдоль кривой

    Интерфейс параметров API 7: IPathPattern
    """
    o3d_PointDrivenPattern            = 507
    """
    Название объекта: Массив операций по точкам

    Интерфейс параметров API 7: IPointDrivenPattern
    """
    o3d_PartsPointDrivenPattern       = 508
    """
    Название объекта: Массив компонентов по точкам

    Интерфейс параметров API 7: IPointDrivenPattern
    """
    o3d_AuxMirrorOperation            = 509
    """
    Название объекта: Зеркальный массив вспомогательной геометрии

    Интерфейс параметров API 7: IMirrorPattern
    """
    o3d_ConnectCurve                  = 510
    """
    Название объекта: Операция соединения кривых

    Интерфейс параметров API 7: IConnectCurve
    """
    o3d_ConnectCurveObject            = 511
    """
    Название объекта: Кривая соединения

    Интерфейс параметров API 7: IModelObject
    """
    o3d_FilletCurve                   = 512
    """
    Название объекта: Операция скругления кривых

    Интерфейс параметров API 7: IFilletCurve
    """
    o3d_FilletCurveObject             = 513
    """
    Название объекта: Скругленная кривая

    Интерфейс параметров API 7: IModelObject
    """
    o3d_EquidistantSurface            = 514
    """
    Название объекта: Операция построения эквидистанты поверхности

    Интерфейс параметров API 7: IEquidistantSurface
    """
    o3d_RuledSurface                  = 515
    """
    Название объекта: Линейчатая поверхность

    Интерфейс параметров API 7: IRuledSurface
    """
    o3d_TrimmedSurface                = 516
    """
    Название объекта: Операция усечения поверхности

    Интерфейс параметров API 7: ITrimmedSurface
    """
    o3d_ExtensionSurface              = 517
    """
    Название объекта: Операция продления поверхности

    Интерфейс параметров API 7: IExtensionSurface
    """
    o3d_SurfaceThickening             = 518
    """
    Название объекта: Операция придания толщины поверхности

    Интерфейс параметров API 7: ISurfaceThickening
    """
    o3d_Arc3D                         = 519
    """
    Название объекта: 3D дуга

    Интерфейс параметров API 7: IArc3D
    """
    o3d_AuxPointDrivenPattern         = 520
    """
    Название объекта: Массив вспомогательной геометрии по точкам

    Интерфейс параметров API 7: IPointDrivenPattern
    """
    o3d_BodiesPointDrivenPattern      = 521
    """
    Название объекта: Массив тел по точкам

    Интерфейс параметров API 7: IPointDrivenPattern
    """
    o3d_TablePattern                  = 522
    """
    Название объекта: Массив операций по таблице из файла

    Интерфейс параметров API 7: ITablePattern
    """
    o3d_PartsTablePattern             = 523
    """
    Название объекта: Массив компонентов по таблице из файла

    Интерфейс параметров API 7: ITablePattern
    """
    o3d_AuxTablePattern               = 524
    """
    Название объекта: Массив вспомогательной геометрии по таблице из файла

    Интерфейс параметров API 7: ITablePattern
    """
    o3d_BodiesTablePattern            = 525
    """
    Название объекта: Массив тел по таблице из файла

    Интерфейс параметров API 7: ITablePattern
    """
    o3d_MeshPointsSurface             = 526
    """
    Название объекта: Поверхность по сети точек

    Интерфейс параметров API 7: IMeshPointsSurface
    """
    o3d_CloudPointsSurface            = 527
    """
    Название объекта: Поверхность по пласту (облаку) точек

    Интерфейс параметров API 7: ICloudPointsSurface
    """
    o3d_BodiesMeshCopy                = 528
    """
    Название объекта: Массив тел по сетке

    Интерфейс параметров API 7: ILinearPattern
    """
    o3d_BodiesCircularCopy            = 529
    """
    Название объекта: Массив тел по концентрической сетке

    Интерфейс параметров API 7: ICircularPattern
    """
    o3d_BodiesCurveCopy               = 530
    """
    Название объекта: Массив тел вдоль кривой

    Интерфейс параметров API 7: IPathPattern
    """
    o3d_Scaling3D                     = 531
    """
    Название объекта: Масштабирование

    Интерфейс параметров API 7: IScaling3D
    """
    o3d_MirrorPart                    = 532
    """
    Название объекта: Зеркальная деталь, с внешней ссылкой на источник (зеркальная вставка детали заготовки)

    Интерфейс параметров API 7: IBilletObsolete
    """
    o3d_sheetMetalUndercut            = 533
    """
    Название объекта: Листовой металл, операция подсечка

    Интерфейс параметров API 7: ISheetMetalUndercut
    """
    o3d_sheetMetalPlate               = 534
    """
    Название объекта: Листовой металл, операция пластина

    Интерфейс параметров API 7: ISheetMetalPlate
    """
    o3d_sheetMetalCombinedBend        = 535
    """
    Название объекта: Листовой металл, операция комбинированный сгиб, - cгиб по эскизу

    Интерфейс параметров API 7: ISheetMetalSketchBend
    """
    o3d_sheetMetalBendStraighten      = 536
    """
    Название объекта: Листовой металл, операция разогнуть

    Интерфейс параметров API 7: ISheetMetalBendedStraighten
    """
    o3d_sheetMetalBendBended          = 537
    """
    Название объекта: Листовой металл, операция согнуть

    Интерфейс параметров API 7: ISheetMetalBendedStraighten
    """
    o3d_sheetMetalBendUnfold          = 538
    """
    Название объекта: Листовой металл, операция развертка

    Интерфейс параметров API 7: ISheetMetalBendUnfoldParameters
    """
    o3d_sheetMetalClosedCorner        = 539
    """
    Название объекта: Листовой металл, операция 'замыкание углов'

    Интерфейс параметров API 7: ISheetMetalClosedCorner
    """
    o3d_sheetMetalBendObject          = 540
    """
    Название объекта: Листовой металл, сгибы листовых операций

    Интерфейс параметров API 7: IModelObject
    """
    o3d_sheetMetalDimpleCutout        = 541
    """
    Название объекта: Листовой металл, закрытая штамповка

    Интерфейс параметров API 7: ISheetMetalPressForming
    """
    o3d_sheetMetalDrawnCutout         = 542
    """
    Название объекта: Листовой металл, открытая штамповка

    Интерфейс параметров API 7: ISheetMetalPressForming
    """
    o3d_sheetMetalBeat                = 543
    """
    Название объекта: Листовой металл, буртик

    Интерфейс параметров API 7: ISheetMetalShoulder
    """
    o3d_sheetMetalLouver              = 544
    """
    Название объекта: Листовой металл, жалюзи

    Интерфейс параметров API 7: ISheetMetalJalousie
    """
    o3d_sheetMetalCowling             = 545
    """
    Название объекта: Обечайка

    Интерфейс параметров API 7: ISheetMetalRuledShell
    """
    o3d_PointsArrOnCurve              = 546
    """
    Название объекта: Группа точек по кривой

    Интерфейс параметров API 7: IPointsArrOnCurve
    """
    o3d_PointsArrFromFile             = 547
    """
    Название объекта: Группа точек из файла

    Интерфейс параметров API 7: IPointsArrFromFile
    """
    o3d_PointsArrOnSurface            = 548
    """
    Название объекта: Группа точек на поверхности

    Интерфейс параметров API 7: IPointsArrOnSurface
    """
    o3d_ArrayExemplar                 = 549
    """
    Название объекта: Экземпляр массива

    Интерфейс параметров API 7: IModelObject
    """
    o3d_AuxGeomArrayExemplar          = 550
    """
    Название объекта: Экземпляр массива вспомогательной геометрии

    Интерфейс параметров API 7: IModelObject
    """
    o3d_BodyArrayExemplar             = 551
    """
    Название объекта: Экземпляр массива копирования тел

    Интерфейс параметров API 7: IModelObject
    """
    o3d_NurbsSurfaceByCurvesMesh      = 552
    """
    Название объекта: Сплайновая поверхность по сетке кривых

    Интерфейс параметров API 7: INurbsSurfacesByCurvesMeshs
    """
    o3d_PlaneByPointAndTangentToFace  = 553
    """
    Название объекта: Конструктивная касательная плоскость к грани в точке

    Интерфейс параметров API 7: IPlane3DTangentToFaceInPoint
    """
    o3d_PlaneByPlaneCurve             = 554
    """
    Название объекта: Конструктивная касательная плоскость через плоскую кривую

    Интерфейс параметров API 7: IPlane3DByPlaneCurve
    """
    o3d_JointSurface                  = 555
    """
    Название объекта: Поверхность соединения

    Интерфейс параметров API 7: IJointSurface
    """
    o3d_DistanceAngleMeasure          = 556
    """
    Название объекта: Объект 'Измерение расстояния и угла'

    Интерфейс параметров API 7: IDistanceAngleMeasurement3D
    """
    o3d_EdgeLengthMeasure             = 557
    """
    Название объекта: Объект 'Измерение длины ребра'

    Интерфейс параметров API 7: IEdgeLengthMeasurement3D
    """
    o3d_AreaMeasure                   = 558
    """
    Название объекта: Объект 'Измерение площади'

    Интерфейс параметров API 7: IAreaMeasurement3D
    """
    o3d_AxisFromPointByDirection      = 559
    """
    Название объекта: Ось через вершину по направлению

    Интерфейс параметров API 7: IAxis3DByPointAndObject
    """
    o3d_Curve3DWithoutHistory         = 560
    """
    Название объекта: Кривая без истории

    Интерфейс параметров API 7: IUnhistoredCurve3D
    """
    o3d_CurveBy2Projections           = 561
    """
    Название объекта: Кривая по двум проекциям

    Интерфейс параметров API 7: ICurveBy2Projections
    """
    o3d_CurveByLaw                    = 562
    """
    Название объекта: Кривая по закону

    Интерфейс параметров API 7: ICurveByLaw
    """
    o3d_IsoparametricCurve            = 563
    """
    Название объекта: Изопараметрическая кривая

    Интерфейс параметров API 7: IIsoparametricCurve
    """
    o3d_CurveOutLine                  = 564
    """
    Название объекта: Линия очерка

    Интерфейс параметров API 7: ICurveOutLine
    """
    o3d_SplineOnSurface               = 565
    """
    Название объекта: Сплайн на поверхности

    Интерфейс параметров API 7: ISplineOnSurface
    """
    o3d_IsoparametricCurvesSet        = 566
    """
    Название объекта: Группа изопараметрических кривых

    Интерфейс параметров API 7: IIsoparametricCurvesSet
    """
    o3d_ProjectionCurve               = 567
    """
    Название объекта: Проекционная кривая

    Интерфейс параметров API 7: IProjectionCurve
    """
    o3d_Contour3D                     = 568
    """
    Название объекта: Контур 3D

    Интерфейс параметров API 7: IContour3D
    """
    o3d_BodyReposition                = 569
    """
    Название объекта: Перепозиционирование тела, поверхности

    Интерфейс параметров API 7: IBodyReposition
    """
    o3d_LineSegment3D                 = 570
    """
    Название объекта: Отрезок 3D

    Интерфейс параметров API 7: ILineSegment3D
    """
    o3d_Billet                        = 571
    """
    Название объекта: Операция 'деталь заготовка'

    Интерфейс параметров API 7: IBilletObsolete
    """
    o3d_PolyLine3DPoint               = 572
    """
    Название объекта: Точка ломаной и сплайна

    Интерфейс параметров API 7: IModelObject
    """
    o3d_OperationLinearDimension      = 573
    """
    Название объекта: Управляющий линейный размер операции 3D

    Интерфейс параметров API 7: IBaseLineDimension3D
    """
    o3d_OperationAngularDimension     = 574
    """
    Название объекта: Управляющий угловой размер операции 3D

    Интерфейс параметров API 7: IAngleDimension3D
    """
    o3d_OperationRadialDimension      = 575
    """
    Название объекта: Управляющий радиальный размер операции 3D

    Интерфейс параметров API 7: IRadialDimension3D
    """
    o3d_OperationDiametralDimension   = 576
    """
    Название объекта: Управляющий диаметральный размер операции 3D

    Интерфейс параметров API 7: IDiametralDimension3D
    """
    o3d_SketchLinearDimension         = 577
    """
    Название объекта: Управляющий линейный размер эскиза 3D

    Интерфейс параметров API 7: IBaseLineDimension3D
    """
    o3d_SketchAngularDimension        = 578
    """
    Название объекта: Управляющий угловой размер эскиза 3D

    Интерфейс параметров API 7: IAngleDimension3D
    """
    o3d_SketchBreakAngularDimension   = 579
    """
    Название объекта: Управляющий угловой размер эскиза 3D с обрывом

    Интерфейс параметров API 7: IAngleDimension3D
    """
    o3d_SketchRadialDimension         = 580
    """
    Название объекта: Управляющий радиальный размер эскиза 3D

    Интерфейс параметров API 7: IRadialDimension3D
    """
    o3d_SketchBreakRadialDimension    = 581
    """
    Название объекта: Управляющий радиальный размер эскиза 3D с обрывом

    Интерфейс параметров API 7: IRadialDimension3D
    """
    o3d_SketchDiametralDimension      = 582
    """
    Название объекта: Управляющий диаметральный размер эскиза 3D

    Интерфейс параметров API 7: IDiametralDimension3D
    """
    o3d_Hole3D                        = 583
    """
    Название объекта: Отверстие 3D

    Интерфейс параметров API 7: IHole3D
    """
    o3d_UserObjectOperation           = 584
    """
    Название объекта: Пользовательская многотельная операция

    Интерфейс параметров API 7: IUserObject3D
    """
    o3d_Zone3D                        = 585
    """
    Название объекта: Зона 3D

    Интерфейс параметров API 7: IZone
    """
    o3d_Zone3DDivision                = 586
    """
    Название объекта: Разбиение зон

    Интерфейс параметров API 7: IZoneDivision
    """
    o3d_Zones3D                       = 587
    """
    Название объекта: Группа Зоны 3D

    Интерфейс параметров API 7: IZonesManager
    """
    o3d_WireFrame3D                   = 588
    """ Название объекта: Трехмерный каркас """
    o3d_CopyGeometry                  = 589
    """
    Название объекта: Копия геометрии

    Интерфейс параметров API 7: ICopyGeometry
    """
    o3d_CollectionGeometry            = 590
    """
    Название объекта: Коллекция геометрии

    Интерфейс параметров API 7: ICollectionGeometry
    """
    o3d_MeshPatternAnyCopy            = 591
    """
    Название объекта: Копирование произвольных объектов по сетке

    Интерфейс параметров API 7: ILinearPattern
    """
    o3d_CircularPatternAnyCopy        = 592
    """
    Название объекта: Копирование произвольных объектов по окружности

    Интерфейс параметров API 7: ICircularPattern
    """
    o3d_CurvePatternAnyCopy           = 593
    """
    Название объекта: Копирование произвольных объектов по кривой

    Интерфейс параметров API 7: IPathPattern
    """
    o3d_PointDrivenPatternAnyCopy     = 595
    """
    Название объекта: Копирование произвольных объектов по точкам

    Интерфейс параметров API 7: IPointDrivenPattern
    """
    o3d_TablePatternAnyCopy           = 596
    """
    Название объекта: Копирование произвольных объектов по таблице

    Интерфейс параметров API 7: ITablePattern
    """
    o3d_LinearUnhistoriedDimension    = 597
    """
    Название объекта: Импортированный линейный размер

    Интерфейс параметров API 7: IBaseLineDimension3D
    """
    o3d_AngularUnhistoriedDimension   = 598
    """
    Название объекта: Импортированный угловой размер

    Интерфейс параметров API 7: IAngleDimension3D
    """
    o3d_RadialUnhistoriedDimension    = 599
    """
    Название объекта: Импортированный радиальный размер

    Интерфейс параметров API 7: IRadialDimension3D
    """
    o3d_DiametralUnhistoriedDimension = 600
    """
    Название объекта: Импортированный диаметральный размер

    Интерфейс параметров API 7: IDiametralDimension3D
    """
    o3d_FaceLift                      = 601
    """
    Название объекта: Операция подтягивания граней

    Интерфейс параметров API 7: IModelObject
    """
    o3d_UserWireFrame3D               = 602
    """
    Название объекта: Трехмерный каркас - пользовательский объект

    Интерфейс параметров API 7: IUserObject3D
    """
    o3d_UndefPartObject               = 603
    """
    Название объекта: Модельный объект неопределенного типа

    Интерфейс параметров API 7: IModelObject
    """
    o3d_SpecRough3D                   = 604
    """
    Название объекта: Неуказанная шероховатость 3D

    Интерфейс параметров API 7: ISpecRough3D
    """
    o3d_SketchBreakLinearDimension    = 605
    """
    Название объекта: Управляющий линейный размер эскиза 3D с обрывом

    Интерфейс параметров API 7: IBaseLineDimension3D
    """
    o3d_sheetMetalRuledCowling        = 606
    """
    Название объекта: Линейчатая обечайка

    Интерфейс параметров API 7: ISheetMetalLinearRuledShell, ISheetMetalRuledShell
    """
    o3d_UserDesignationObject3D       = 607
    """
    Название объекта: Пользовательский объект обозначение 3D

    Интерфейс параметров API 7: IUserObject3D
    """
    o3d_SplineFormOperation           = 608
    """ Название объекта: Операция прямого редактирования """
    o3d_UnhistoriedBase3D             = 609
    """
    Название объекта: База без истории

    Интерфейс параметров API 7: IBase3D
    """
    o3d_UnhistoriedThread             = 610
    """
    Название объекта: Резьба без истории

    Интерфейс параметров API 7: IModelObject
    """
    o3d_UserDesignationCompObj        = 611
    """
    Название объекта: Составной объект для пользовательских объектов обозначений 3D

    Интерфейс параметров API 7: IUserObject3D
    """
    o3d_UserFolder                    = 612
    """
    Название объекта: Пользовательская директория 3D

    Интерфейс параметров API 7: IUserObject3D
    """
    o3d_MeshObject3D                  = 613
    """
    Название объекта: Полигональный объект 3D

    Интерфейс параметров API 7: IMeshObject3D
    """
    o3d_sheetMetalRib                 = 614
    """
    Название объекта: Ребро усиления

    Интерфейс параметров API 7: ISheetMetalRib
    """
    o3d_axis3D                        = 615
    """
    Название объекта: Ось 3D

    Интерфейс параметров API 7: IAxis3D
    """
    o3d_SubFoldLine                   = 616
    """
    Название объекта: Подобъект Линия сгиба

    Интерфейс параметров API 7: IModelObject
    """
    o3d_OperationLeaderDimension      = 617
    """
    Название объекта: Управляющий размер операции в виде линии выноски

    Интерфейс параметров API 7: IBaseLeader3D
    """
    o3d_FullFillet                    = 618
    """
    Название объекта: Полное скругление

    Интерфейс параметров API 7: IFullFillet
    """
    o3d_DynamicCrossSection           = 619
    """
    Название объекта: Динамическое сечение

    Интерфейс параметров API 7: IDynamicCrossSection
    """
    o3d_RestoredSurface               = 620
    """
    Название объекта: Восстановленная поверхность

    Интерфейс параметров API 7: IRestoredSurface
    """
    o3d_CurvatureGraph                = 621
    """ Название объекта: График кривизны """
    o3d_CollisionObject               = 622
    """ Название объекта: Информация о коллизии """
    o3d_CurvatureCheckObject          = 623
    """ Название объекта: Проверка кривизны """
    o3d_ContinuityCheck               = 624
    """ Название объекта: Проверка непрерывности """
    o3d_SketchFace                    = 625
    """ Название объекта: Контур эскиза """
    o3d_SectionAnalysis               = 626
    """ Название объекта: Сетка графиков кривизны """
    o3d_Text3D                        = 627
    """ Название объекта: Надпись 3D """
    o3d_SketchArcDimension            = 628
    """ Название объекта: Управляющий размер дуги окружности эскиза 3D """
    o3d_ArcDimension3D                = 629
    """ Название объекта: Размер дуги окружности 3D """
    o3d_sheetMetalPunch               = 630
    """ Название объекта: Листовой металл, штамповка телом """
    o3d_sheetMetalFlanging            = 631
    """ Название объекта: Листовой металл, отбортовка """
    o3d_FaceMover                     = 632
    """ Название объекта: Операция переместить грани """
    o3d_SplitSolid                    = 633
    """ Название объекта: Операция Разрезать """
    o3d_sheetMetalConvertFromBody     = 634
    """ Название объекта: Операция Преобразования в листовое тело """
    o3d_ConicSectionSurface           = 635
    """ Название объекта: Поверхность конического сечения """
    o3d_TechnicalDemand3D             = 636
    """
    Название объекта: Технические требования 3D

    Интерфейс параметров API 7: ITechnicalDemand3D
    """
    o3d_ModelText                     = 637
    """
    Название объекта: Текст в модели

    Интерфейс параметров API 7: IModelText
    """
    o3d_ModelTable                    = 638
    """
    Название объекта: Таблица в модели

    Интерфейс параметров API 7: IModelTable
    """
    o3d_ConicCurve3D                  = 639
    """ Название объекта: Коническая 3D кривая """
    o3d_ExtensionCurve                = 640
    """ Название объекта: Продление кривой """
    o3d_WrapCurve                     = 641
    """ Название объекта: Свернутая кривая """
    o3d_UnwrapCurve                   = 642
    """ Название объекта: Развернутая кривая. """
    o3d_PlaneUnhistoried              = 643
    """ Название объекта: Плоскость без истории """
    o3d_DraftFromEdges                = 644
    """ Название объекта: Операция "Уклон от базовой линии" """
    o3d_lastEntityElement2            = 1500
    """ Название объекта: Всегда последний из Entity2!!! """


class Intersection_Type:  # intersection_type.html
    """ ## Intersection_Type - Типы пересечений """
    itTangentPoint   = 1
    """ Пересечение точкой """
    itTangentCurve   = 2
    """ Пересечение вдоль касательной линии """
    itTangentSurface = 3
    """ Пересечение касательной областью поверхности """
    itBody           = 4
    """ Пересечение образует тело """


class ksMateType:  # ksmatetype.html
    """
    ## ksMateType - Типы математических объектов, участвующих в сопряжении

    Представление математических объектов, участвующих в сопряжении...
    """
    ksMateUnknown  = 0
    """ Неизвестный объект """
    ksMatePoint    = 1
    """ Точка """
    ksMateLine     = 2
    """ Линия """
    ksMatePlane    = 3
    """ Плоскость """
    ksMateCylinder = 4
    """ Цилиндр """
    ksMateCone     = 5
    """ Конус """
    ksMateSphere   = 6
    """ Сфера """
    ksMateTorus    = 7
    """ Тор """


class ksPatternOrientationTypeEnum:  # kspatternorientationtypeenum.html
    """ ## ksPatternOrientationTypeEnum - Способ ориентации экземпляров массива """
    ksOrientationSave     = 0
    """ Сохранять исходную ориентацию """
    ksOrientationByNormal = 1
    """ Доворачивать до нормали """
    ksOrientationByObject = 2
    """ Ориентировать по объекту """


class ksProductObjectTypeEnum:  # ksproductobjecttypeenum.html
    """ ## ksProductObjectTypeEnum - Тип объектов дерева СЧИ """
    ksPOTAllObjects        = -1
    """ Не задан. Выдавать все объекты """
    ksPOTDocumentObject    = 1
    """ Документ """
    ksPOTEmbodimentsObject = 2
    """ Исполнение """
    ksPOTPartObject        = 4
    """ Компонент. """
    ksPOTBodyObject        = 8
    """ Тело """
    ksPOTProductObject     = 16
    """ Изделие """
    ksPOTInformObject      = 32
    """ Информационный объект """
    ksPOTSurfaceObject     = 64
    """ Поверхность """
    ksPOTBillet            = 128
    """ Изделие-заготовка """
    ksPOTGroupObject       = 256
    """ Групповой объект """


class ksSaveDocumentVersionEnum:  # kssavedocumentversionenum.html
    """ ## ksSaveDocumentVersionEnum - Версия сохранения файла """
    ksSDV_Prev            = -1
    """ В предыдущую версию """
    ksSDV_Current         = 0
    """ В текущую версию """
    ksSDV_Kompas_5_11_R03 = 1
    """ В версию Компас 5.11.R03 """
    ksSDV_Kompas_6_0      = 2
    """ В версию Компас 6.0. """
    ksSDV_Kompas_6_Plus   = 3
    """ В версию Компас 6 Plus """
    ksSDV_Kompas_7_0      = 4
    """ В версию Компас 7.0. """
    ksSDV_Kompas_7_Plus   = 5
    """ В версию Компас 7 Plus """
    ksSDV_Kompas_8_0      = 6
    """ В версию Компас 8.0 """
    ksSDV_Kompas_8_Plus   = 7
    """ В версию Компас 8 Plus """
    ksSDV_Kompas_9_0      = 8
    """ В версию Компас 9.0 """
    ksSDV_Kompas_10_0     = 9
    """ В версию Компас 10.0 """
    ksSDV_Kompas_11_0     = 10
    """ В версию Компас 11.0 """
    ksSDV_Kompas_12_0     = 11
    """ В версию Компас 12.0 """
    ksSDV_Kompas_13_0     = 12
    """ В версию Компас 13.0 """
    ksSDV_Kompas_14_0     = 13
    """ В версию Компас 14.0 """
    ksSDV_Kompas_14_Sp1   = 14
    """ В версию Компас 14 Sp1 """
    ksSDV_Kompas_14_Sp2   = 15
    """ В версию Компас 14 Sp2 """
    ksSDV_Kompas_15_0     = 16
    """ В версию Компас 15.0 """
    ksSDV_Kompas_15_Sp1   = 17
    """ В версию Компас 15 Sp1 """
    ksSDV_Kompas_15_Sp2   = 18
    """ В версию Компас 15 Sp2 """
    ksSDV_Kompas_16       = 19
    """ В версию Компас 16 """
    ksSDV_Kompas_16_Sp1   = 20
    """ В версию Компас 16 Sp1 """
    ksSDV_Kompas_17       = 21
    """ В версию Компас 17 """
    ksSDV_Kompas_17_Sp1   = 22
    """ В версию Компас 17_Sp1 """
    ksSDV_Kompas_18       = 23
    """ В версию Компас 18 """
    ksSDV_Kompas_18_Sp1   = 24
    """ В версию Компас 18_Sp1 """
    ksSDV_Kompas_19       = 25
    """ В версию Компас 19 """
    ksSDV_Kompas_20       = 26
    """ В версию Компас 20 """
    ksSDV_Kompas_21       = 27
    """ В версию Компас 21 """
    ksSDV_Kompas_22       = 28
    """ В версию Компас 22 """


class UseColor:  # usecolor.html
    """ ## UseColor - Типы используемого цвета """
    useColorUnknown = -1
    """ тип не определен """
    useColorOur     = 0
    """ собственный цвет """
    useColorOwner   = 1
    """ цвет хозяина """
    useColorSource  = 2
    """ цвет источника """
    useColorLayer   = 3
    """ Цвет слоя """


class ksTreeTypeEnum:  # kstreetypeenum.html
    """ ## ksTreeTypeEnum - Типы Дерева построения 3D документа """
    ksOperTree  = 0
    """ Операционное дерево """
    ksMultiTree = 1
    """ Многотельное дерево """


class ksVariantMarkingTypeEnum:  # ksvariantmarkingtypeenum.html
    """ ## ksVariantMarkingTypeEnum - Параметры формирования обозначения """
    ksVMFullMarking      = -1
    """ Полное обозначение """
    ksVMBaseMarking      = 0x1
    """ Базовая часть обозначения """
    ksVMEmbodimentNumber = 0x2
    """ Исполнение """
    ksVMAdditionalNumber = 0x4
    """ Дополнительный номер """
    ksVMCode             = 0x8
    """ Код документа """


class ksPrinterTypeEnum:  # ksprintertypeenum.html
    """ ## ksPrinterTypeEnum - Параметры формирования обозначения """
    ksPTPrintPreviewPrinter = 0
    """ Принтер для печати через предварительный просмотр """
    ksPTSpecialPrinter      = 1
    """ Принтер для специальной печати """


class ProjectionType:  # projectiontype.html
    """ ## ProjectionType - Типы проекций """
    vp_None     = -1
    """ Не определена """
    vp_NormalTo = 0
    """ Нормально к текущему планару """
    vp_Front    = 1
    """ Спереди - Фронтальная плоскость """
    vp_Rear     = 2
    """ Сзади """
    vp_Up       = 3
    """ Сверху - Горизонтальная плоскость """
    vp_Down     = 4
    """ Снизу """
    vp_Left     = 5
    """ Слева - Профильная плоскость """
    vp_Right    = 6
    """ Справа """
    vp_IsoXYZ   = 7
    """ Изометрия XYZ """
    vp_IsoYZX   = 8
    """ Изометрия YZX """
    vp_IsoZXY   = 9
    """ Изометрия ZXY """
    vp_Dio      = 10
    """ Диметрия """


class LtQualSystem:  # ltqualsystem.html
    """ ## LtQualSystem - Система квалитета """
    lt_qsShaft = 1
    """ вала """
    lt_qsHole  = 2
    """ отверстия """


class LtQualDir:  # ltqualdir.html
    """ ## LtQualDir - Квалитеты """
    lt_qdPreferable = 1
    """ предпочтительные """
    lt_qdBasic      = 2
    """ основные """
    lt_qdAdditional = 3
    """ дополнительные """


class LtRemoteElmSignType:  # ltremoteelmsigntype.html
    """ ## LtRemoteElmSignType - Типы значка объекта "Выносной элемент" """
    re_Circle    = 0
    """ окружность """
    re_Rectangle = 1
    """ прямоугольник """
    re_Ballon    = 2
    """ скругленный прямоугольник """


class ChangeOrderType:  # changeordertype.html
    """ ## ChangeOrderType - Типы изменения порядка объектов """
    co_Top          = 1
    """ Выше всех """
    co_Bottom       = 2
    """ Ниже всех """
    co_BeforeObject = 3
    """ Перед объектом """
    co_AfterObject  = 4
    """ За объектом """
    co_UpLevel      = 5
    """ На уровень вперед """
    co_DownLevel    = 6
    """ На уровень назад """


class DocType:  # doctype.html
    """ ## DocType - Типы документов системы КОМПАС """
    lt_DocUnknown              = 0
    """ - нет активного документа """
    lt_DocSheetStandart        = 1
    """ - чертеж стандартного формата """
    lt_DocSheetUser            = 2
    """ - чертеж нестандартного формата """
    lt_DocFragment             = 3
    """ - фрагмент """
    lt_DocSpc                  = 4
    """ - спецификация """
    lt_DocPart3D               = 5
    """ - деталь """
    lt_DocAssemble3D           = 6
    """ - сборка """
    lt_DocTxtStandart          = 7
    """ - текстовый документ стандартный """
    lt_DocTxtUser              = 8
    """ - текстовый документ нестандартный """
    lt_DocSpcUser              = 9
    """ - спецификация - нестандартный формат """
    lt_DocTechnologyAssemble3D = 10
    """ - 3d-документ технологическая сборка """


class LtNodeType:  # ltnodetype.html
    """ ## LtNodeType - Типы узла дерева библиотеки документов """
    tn_root = 0
    """ - корень дерева """
    tn_dir  = 1
    """ - папка """
    tn_file = 2
    """ - документ (файл) """


class LtVariantType:  # ltvarianttype.html
    """ ## LtVariantType - Типы данных для LtVariant """
    ltv_Char   = 1
    """ символ """
    ltv_UChar  = 2
    """ байт """
    ltv_Int    = 3
    """ целое """
    ltv_UInt   = 4
    """ беззнаковое целое """
    ltv_Long   = 5
    """ длинное целое """
    ltv_Float  = 6
    """ вещественное """
    ltv_Double = 7
    """ двойное вещественное """
    ltv_Str    = 8
    """ строка 255 символов char[255] """
    ltv_NoUsed = 9
    """ пока не используется """
    ltv_Short  = 10
    """ короткое целое """
    ltv_WStr   = 11
    """ Строка 255 символов whar_t[255] """


class StructType2DEnum:  # structtype2denum.html
    """
    ## StructType2DEnum - Типы интерфейсов параметров объектов графического документа, получаемых методом KompasObject::GetParamStruct

    См. также метод KompasObject::GetParamStruct
    """
    ko_Type1                 = 1
    """ ksType1 """
    ko_Type2                 = 2
    """ ksType2 """
    ko_Type3                 = 3
    """ ksType3 """
    ko_Type5                 = 4
    """ ksType5 """
    ko_Type6                 = 5
    """ ksType6 """
    ko_Phantom               = 6
    """ ksPhantom """
    ko_PlacementParam        = 7
    """ ksPlacementParam """
    ko_ViewParam             = 8
    """ ksViewParam """
    ko_LayerParam            = 9
    """ ksLayerParam """
    ko_RequestInfo           = 10
    """ ksRequestInfo """
    ko_LineSegParam          = 11
    """ ksLineSegParam """
    ko_ArcByAngleParam       = 12
    """ ksArcByAngleParam """
    ko_ArcByPointParam       = 13
    """ ksArcByPointParam """
    ko_MathPointParam        = 14
    """ ksMathPointParam """
    ko_RectParam             = 15
    """ ksRectParam """
    ko_PointParam            = 16
    """ ksPointParam """
    ko_BezierPointParam      = 17
    """ ksBezierPointParam """
    ko_NurbsPointParam       = 18
    """ ksNurbsPointParam """
    ko_BezierParam           = 19
    """ ksBezierParam """
    ko_CircleParam           = 20
    """ ksCircleParam """
    ko_LineParam             = 21
    """ ksLineParam """
    ko_EllipseParam          = 22
    """ ksEllipseParam """
    ko_EllipsArcParam        = 23
    """ ksEllipseArcParam """
    ko_EllipsArcParam1       = 24
    """ ksEllipseArcParam1 """
    ko_EquidParam            = 25
    """ ksEquidistantParam """
    ko_HatchParam            = 26
    """ ksHatchParam """
    ko_ParagraphParam        = 27
    """ ksParagraphParam """
    ko_TextParam             = 28
    """ ksTextParam """
    ko_TextLineParam         = 29
    """ ksTextLineParam """
    ko_TextItemFont          = 30
    """ ksTextItemFont """
    ko_TextItemParam         = 31
    """ ksTextItemParam """
    ko_StandartSheet         = 32
    """ ksStandartSheet """
    ko_SheetSize             = 33
    """ ksSheetSize """
    ko_SheetPar              = 34
    """ ksSheetPar """
    ko_DocumentParam         = 35
    """ ksDocumentParam """
    ko_ColumnInfoParam       = 36
    """ ksColumnInfoParam """
    ko_AttributeType         = 37
    """ ksAttributeTypeParam """
    ko_Attribute             = 38
    """ ksAttributeParam """
    ko_LibraryAttrTypeParam  = 39
    """ ksLibraryAttrTypeParam """
    ko_TAN                   = 40
    """ ksTAN """
    ko_CON                   = 41
    """ ksCON """
    ko_DimText               = 42
    """ ksDimTextParam """
    ko_LDimSource            = 43
    """ ksLDimSourceParam """
    ko_DimDrawing            = 44
    """ ksDimDrawingParam """
    ko_LDimParam             = 45
    """ ksLDimParam """
    ko_LBreakDimSource       = 46
    """ ksLBreakDimSource """
    ko_BreakDimDrawing       = 47
    """ ksBreakDimDrawing """
    ko_LBreakDimParam        = 48
    """ ksLBreakDimParam """
    ko_ADimSourceParam       = 49
    """ ksADimSourceParam """
    ko_ADimParam             = 50
    """ ksADimParam """
    ko_ABreakDimParam        = 51
    """ ksABreakDimParam """
    ko_RDimSource            = 52
    """ ksRDimSourceParam """
    ko_RDimDrawing           = 53
    """ ksRDimDrawingParam """
    ko_RDimParam             = 54
    """ ksRDimParam """
    ko_RBreakDrawing         = 55
    """ ksRBreakDrawingParam """
    ko_RBreakDimParam        = 56
    """ ksRBreakDimParam """
    ko_RoughPar              = 57
    """ ksRoughPar """
    ko_ShelfPar              = 58
    """ ksShelfPar """
    ko_RoughParam            = 59
    """ ksRoughParam """
    ko_LeaderParam           = 60
    """ ksLeaderParam """
    ko_PosLeaderParam        = 61
    """ ksPosLeaderParam """
    ko_BrandLeaderParam      = 62
    """ ksBrandLeaderParam """
    ko_MarkerLeaderParam     = 63
    """ ksMarkerLeaderParam """
    ko_BaseParam             = 64
    """ ksBaseParam """
    ko_CutLineParam          = 65
    """ ksCutLineParam """
    ko_ViewPointerParam      = 66
    """ ksViewPointerParam """
    ko_ToleranceBranch       = 67
    """ ksToleranceBranch """
    ko_ToleranceParam        = 68
    """ ksToleranceParam """
    ko_CurvePattern          = 69
    """ ksCurvePattern """
    ko_CurvePicture          = 70
    """ ksCurvePicture """
    ko_CurvePatternEx        = 71
    """ ksCurvePatternEx """
    ko_CurveStyleParam       = 72
    """ ksCurveStyleParam """
    ko_DimensionPartsParam   = 73
    """ ksDimensionPartsParam """
    ko_TextStyleParam        = 74
    """ ksTextStyleParam """
    ko_ConicArcParam         = 75
    """ ksConicArcParam """
    ko_PolylineParam         = 76
    """ ksPolylineParam """
    ko_LibStyle              = 77
    """ ksLibStyle """
    ko_TechnicalDemandParam  = 78
    """ ksTechnicalDemandParam """
    ko_SpecRoughParam        = 79
    """ ksSpecRoughParam """
    ko_DimensionOptions      = 80
    """ ksDimensionsOptions """
    ko_SpcColumnParam        = 81
    """ ksSpcColumnParam """
    ko_LibraryStyleParam     = 82
    """ ksLibraryStyleParam """
    ko_InertiaParam          = 83
    """ ksInertiaParam """
    ko_MassInertiaParam      = 84
    """ ksMassInertiaParam """
    ko_VariableParam         = 85
    """ ksVariable """
    ko_SnapOptions           = 86
    """ ksSnapOptions """
    ko_NurbsParam            = 87
    """ ksNurbsParam """
    ko_InsertFragmentParam   = 88
    """ ksInsertFragmentParam """
    ko_ConstraintParam       = 89
    """ ksConstraintParam """
    ko_CornerParam           = 90
    """ ksCornerParam """
    ko_RectangleParam        = 91
    """ ksRectangleParam """
    ko_RegularPolygonParam   = 92
    """ ksRegularPolygonParam """
    ko_CentreParam           = 93
    """ ksCentreParam """
    ko_DocAttachSpcParam     = 94
    """ ksDocAttachedSpcParam """
    ko_SpcObjParam           = 95
    """ ksSpcObjParam """
    ko_RasterParam           = 96
    """ ksRasterParam """
    ko_RecordTypeAttrParam   = 97
    """ ksRecordTypeAttrParam """
    ko_NumberTypeAttrParam   = 98
    """ ksNumberTypeAttrParam """
    ko_SpcStyleColumnParam   = 99
    """ ksSpcStyleColumnParam """
    ko_SpcStyleSectionParam  = 100
    """ ksSpcStyleSectionParam """
    ko_SpcSubSectionParam    = 101
    """ ksSpcSubSectionParam """
    ko_SpcTuningSectionParam = 102
    """ ksSpcTuningSectionParam """
    ko_SpcTuningStyleParam   = 103
    """ ksSpcTuningStyleParam """
    ko_SpcStyleParam         = 104
    """ ksSpcStyleParam """
    ko_SpcDescrParam         = 105
    """ ksSpcDescrParam """
    ko_QualityItemParam      = 106
    """ ksQualityItemParam """
    ko_QualityContensParam   = 107
    """ ksQualityContensParam """
    ko_LtVariant             = 108
    """ ksLtVariant """
    ko_ContourParam          = 109
    """ ksContourParam """
    ko_DoubleValue           = 110
    """ ksDoubleValue """
    ko_Char255               = 111
    """ ksChar255 """
    ko_UserParam             = 112
    """ ksUserParam """
    ko_HatchLineParam        = 113
    """ ksHatchLineParam """
    ko_HatchStyleParam       = 114
    """ ksHatchStyleParam """
    ko_OrdinatedSourceParam  = 115
    """ ksOrdinatedSourceParam """
    ko_OrdinatedDrawingParam = 116
    """ ksOrdinatedDrawingParam """
    ko_OrdinatedDimParam     = 117
    """ ksOrdinatedDimParam """
    ko_SheetOptions          = 118
    """ ksSheetOptions """
    ko_InsertFragmentParamEx = 119
    """ ksInsertFragmentParamEx """
    ko_TreeNodeParam         = 120
    """ ksTreeNodeParam """
    ko_AssociationViewParam  = 121
    """ ksAssociationViewParam """
    ko_HatchLineParam        = 122
    """ ksHatchLineParam """
    ko_AxisLineParam         = 123
    """ ksAxisLineParam """
    ko_TextDocumentParam     = 124
    """ ksTextDocumentParam """
    ko_CopyObjectParam       = 126
    """ ksCopyObjectParam """
    ko_OverlapObjectOptions  = 127
    """ ksOverlapObjectOptions """
    ko_ChangeLeaderParam     = 128
    """ ksChangeLeaderParam """
    ko_ParametrizationParam  = 9000
    """ ksParametrizationParam """


class TextAlign:  # textalign.html
    """ ## TextAlign -Типы привязки текста """
    txta_Left   = 0
    """ - точка привязки слева """
    txta_Center = 1
    """ - точка привязки в центре """
    txta_Right  = 2
    """ - точка привязки справа """


class LtViewType:  # ltviewtype.html
    """ ## LtViewType - Типы видов чертежа """
    vtUnknown    = -1
    """ Неизвестный тип """
    vt_System    = 0
    """ Системный вид с номером 0; создается автоматически, существует всегда """
    vt_Normal    = 1
    """ Обычный вид """
    vt_Arbitrary = 2
    """ Произвольный вид """
    vt_Standart  = 3
    """ Стандартный вид """
    vt_Projected = 4
    """ Проекционный вид """
    vt_Arrow     = 5
    """ Вид по стрелке """
    vt_Remote    = 6
    """ Выносной вид """
    vt_Section   = 7
    """ Вид разрез\\сечение """
    vt_Remote2D  = 100
    """ Выносной вид не связанный с 3D моделью """


class ErrorType:  # errorcodes.html
    """ ## ErrorType - Коды ошибок графического документа """
    etNo3dDocument  = -7
    """ Документ не активизирован или не является трехмерной моделью """
    etNoAllDocument = -6
    """ Документ не активизирован """
    etNoSPCDocument = -5
    """ Документ не активизирован или не является спецификацией """
    etLibraryClose  = -4
    """ Принудительное завершение выполнения библиотеки """
    etNoPreView     = -3
    """ В режиме предварительного просмотра нельзя создавать или открывать выводимые документы """
    etNoDocument    = -2
    """ Документ не активизирован или не является листом/фрагментом """
    etAbort         = -1
    """ Аварийное завершение """
    etSuccess       = 0
    """ Успешное завершение """
    etError1        = 1
    """ Попытка выполнить EndObj при неоткрытом составном элементе """
    etError2        = 2
    """ Попытка поставить в сплайн недопустимый объект """
    etError3        = 3
    """ Попытка поставить в штриховку недопустимый объект """
    etError4        = 4
    """ Попытка выполнить delete_mtr при невведенной локальной системе координат """
    etError5        = 5
    """ Ошибка при введении локальной системы координат """
    etError6        = 6
    """ Группа должна быть постоянной """
    etError7        = 7
    """ Объект не существует """
    etError8        = 8
    """ В текущем документе объект не найден """
    etError9        = 9
    """ Нет памяти """
    etError10       = 10
    """ Вырожденный объект """
    etError11       = 11
    """ Неверный указатель группы """
    etError12       = 12
    """ Объект не принадлежит группе """
    etError13       = 13
    """ Объект нельзя поставить в группу """
    etError14       = 14
    """ Группа должна быть временной """
    etError15       = 15
    """ Первый объект не существует или не является кривой """
    etError16       = 16
    """ Второй объект не существует или не является кривой """
    etError17       = 17
    """ Кривые расположены в разных видах """
    etError18       = 18
    """ Один (или оба) из указанных объектов - не геометрический """
    etError19       = 19
    """ Первый объект не является кривой """
    etError20       = 20
    """ Второй объект не является кривой """
    etError21       = 21
    """ Объект уже находится в группе """
    etError22       = 22
    """ Временный объект не может быть в постоянной группе """
    etError23       = 23
    """ В документе не предусмотрена работа с видами """
    etError24       = 24
    """ Вид с заданным номером уже существует """
    etError25       = 25
    """ Недопустимое значение номера вида """
    etError26       = 26
    """ В текущем документе вид не найден """
    etError27       = 27
    """ Неверный указатель вида """
    etError28       = 28
    """ Вид не редактируется """
    etError29       = 29
    """ Состояние вида задано неверно """
    etError30       = 30
    """ Параметры текущего вида не меняются """
    etError31       = 31
    """ Неверный указатель макроэлемента """
    etError32       = 32
    """ Должен быть режим редактирования макроэлемента """
    etError33       = 33
    """ Неверный тип параметров редактирования макроэлемента """
    etError34       = 34
    """ В виде остались не закрытые составные элементы """
    etError35       = 35
    """ Неверный указатель слоя """
    etError36       = 36
    """ Недопустимое значение номера слоя """
    etError37       = 37
    """ В текущем виде слой не найден """
    etError38       = 38
    """ У объекта нет параметров """
    etError39       = 39
    """ Размер структуры параметров не соответствует указанному """
    etError40       = 40
    """ Состояние слоя задано неверно """
    etError41       = 41
    """ Параметры текущего слоя не меняются """
    etError42       = 42
    """ В указанном виде редактирование запрещено """
    etError43       = 43
    """ В указанном слое редактирование запрещено """
    etError44       = 44
    """ Параметры системного вида не меняется """
    etError45       = 45
    """ Попытка поставить в текст недопустимый объект """
    etError46       = 46
    """ Неверный ввод текста """
    etError47       = 47
    """ Неверный тип массива """
    etError48       = 48
    """ Неверный указатель массива """
    etError49       = 49
    """ Указатель на структуру параметров должен быть не NULL """
    etError50       = 50
    """ Неверный индекс массива """
    etError51       = 51
    """ Неверное редактирование текста """
    etError52       = 52
    """ Точка кривой Безье используется неверно """
    etError53       = 53
    """ Неправильный индекс """
    etError54       = 54
    """ Режим работы документа задан неверно """
    etError55       = 55
    """ Режим обработки документов задан неверно """
    etError56       = 56
    """ Неверный указатель на документ """
    etError57       = 57
    """ Попытка сохранить документ без имени """
    etError58       = 58
    """ Документ закрыт без сохранения """
    etError59       = 59
    """ Имя файла документа задано неверно """
    etError60       = 60
    """ Объект не соответствует типу поиска """
    etError61       = 61
    """ Невозможно создать документ. Документ с таким именем уже открыт """
    etError62       = 62
    """ Поиск объектов задан неверно """
    etError63       = 63
    """ В текущем документе итератор не найден """
    etError64       = 64
    """ Документ не найден или неверная структура файла """
    etError65       = 65
    """ Документ открыт в видимом режиме """
    etError66       = 66
    """ Документ открыт в невидимом режиме """
    etError67       = 67
    """ Нельзя менять тип документа """
    etError68       = 68
    """ Стиль спецификации не найден """
    etError69       = 69
    """ У фрагмента нет размеров листа """
    etError70       = 70
    """ Режим работы документа не меняется """
    etError71       = 71
    """ Вид должен быть активным или текущим """
    etError72       = 72
    """ Тип атрибута задан неверно """
    etError73       = 73
    """ Тип атрибута не найден """
    etError74       = 74
    """ Неверный пароль """
    etError75       = 75
    """ Не найдено определение локального фрагмента """
    etError76       = 76
    """ Атрибут в документе не найден """
    etError77       = 77
    """ Атрибут не принадлежит объекту """
    etError78       = 78
    """ Неправильный номер колонки атрибута """
    etError79       = 79
    """ Неправильный номер строки атрибута """
    etError80       = 80
    """ Родительское окно не найдено """
    etError81       = 81
    """ Библиотека атрибутов не найдена или ошибка в библиотеке """
    etError82       = 82
    """ Текст размера задан неверно """
    etError83       = 83
    """ Параметры привязки размера заданы неверно """
    etError84       = 84
    """ Текст шероховатости задан неверно """
    etError85       = 85
    """ Неверный указатель линейного размера """
    etError86       = 86
    """ Текст линии выноски задан неверно """
    etError87       = 87
    """ Параметры линии выноски заданы неверно """
    etError88       = 88
    """ Попытка поставить в контур недопустимый объект """
    etError89       = 89
    """ У звеньев контура не совпадают узлы """
    etError90       = 90
    """ В документе не предусмотрена работа с техническими требованиями """
    etError91       = 91
    """ В документе не предусмотрена работа с неуказанной шероховатостью """
    etError92       = 92
    """ Попытка поставить в таблицу недопустимый объект """
    etError93       = 93
    """ В составном объекте не предусмотрена работа с техническими требованиями """
    etError94       = 94
    """ В документе не предусмотрена работа с основной надписью """
    etError95       = 95
    """ В составном объекте не предусмотрена работа с основной надписью """
    etError96       = 96
    """ Попытка поставить в допуск формы недопустимый объект """
    etError97       = 97
    """ Точка кривой NURBS используется неверно """
    etError98       = 98
    """ Попытка поставить в ломаную линию недопустимый объект """
    etError99       = 99
    """ Объект должен быть геометрическим """
    etError100      = 100
    """ Эквидистанту в контур включать нельзя """
    etError101      = 101
    """ Неправильная работа с указателем на определение вставного фрагмента """
    etError102      = 102
    """ Рекурсивная вставка фрагмента """
    etError103      = 103
    """ Ошибка чтения файла фрагмента """
    etError104      = 104
    """ Аналогичное определение вставки фрагмента уже есть. Новый комментарий не принимается """
    etError105      = 105
    """ Неправильная работа с указателем на основную надпись """
    etError106      = 106
    """ Неправильная работа с указателем на неуказанную шероховатость """
    etError107      = 107
    """ Неправильная работа с указателем на технические требования """
    etError108      = 108
    """ Документ должен быть активным """
    etError109      = 109
    """ Стиль кривой не найден """
    etError110      = 110
    """ Объект должен быть кривой """
    etError111      = 111
    """ Стиль текста не найден """
    etError112      = 112
    """ Неверно заданы параметры для расчета длины текста """
    etError113      = 113
    """ Новый слой должен существовать и быть доступным для редактирования """
    etError114      = 114
    """ Номер раздела задан неверно """
    etError115      = 115
    """ Стиль спецификации не найден """
    etError116      = 116
    """ В текущем документе объект спецификации не найден """
    etError117      = 117
    """ Попытка подключить к объекту спецификации недопустимый объект """
    etError118      = 118
    """ Тип объекта задан неверно """
    etError119      = 119
    """ Объект заданного типа не редактируется """
    etError120      = 120
    """ Нужно завершить редактирование составного объекта """
    etError121      = 121
    """ Объект должен быть таблицей """
    etError122      = 122
    """ Объект должен быть допуском формы """
    etError123      = 123
    """ Не найден файл для отрисовки слайда """
    etError124      = 124
    """ Неверная структура файла """
    etError125      = 125
    """ Нужно завершить редактирование объекта спецификации """
    etError126      = 126
    """ Объект должен быть макроэлементом """
    etError127      = 127
    """ Попытка поставить в макроэлемент недопустимый объект """
    etError128      = 128
    """ Библиотека фрагментов уже закрыта или не открывалась """
    etError129      = 129
    """ Библиотека фрагментов уже открыта """
    etError130      = 130
    """ Файл библиотеки фрагментов не найден """
    etError131      = 131
    """ Ошибка в структуре файла библиотеки фрагментов """
    etError132      = 132
    """ Ошибка в имени файла библиотеки фрагментов """
    etError133      = 133
    """ Ошибка в имени фрагмента для библиотеки фрагментов """
    etError134      = 134
    """ Доступ к фрагменту в библиотеке фрагментов невозможен" """
    etError135      = 135
    """ В документе не предусмотрена работа со спецификацией на листе """
    etError136      = 136
    """ Некорректный вид типа атрибута """
    etError137      = 137
    """ Номер листа спецификации задан неверно """
    etError138      = 138
    """ Документ должен быть открыт в видимом режиме """
    etError139      = 139
    """ Ошибка при обработке картинки для стиля кривой """
    etError140      = 140
    """ Объект должен быть штриховкой """
    etError141      = 141
    """ Объект должен быть текстом """
    etError142      = 142
    """ В документе не предусмотрена работа со спецификацией на листе """
    etError143      = 143
    """ В документе не предусмотрена работа с зонами """
    etError144      = 144
    """ Объект спецификации не редактируется """
    etError145      = 145
    """ Файл c растровым объектом не найден """
    etError146      = 146
    """ Ошибка в определении параметров описания спецификации """
    etError147      = 147
    """ Описание спецификации не найдено """
    etError148      = 148
    """ Имя файла спецификации уже используется в листе """
    etError149      = 149
    """ Описание спецификации данного типа уже есть в листе """
    etError150      = 150
    """ Необходимо завершить текущую операцию """
    etError151      = 151
    """ Редактируемый макроэлемент удалять нельзя """
    etError152      = 152
    """ Служебный файл допусков graphic.tol не найден """
    etError153      = 153
    """ Попытка поставить в макроэлемент собственный объект """
    etError154      = 154
    """ Неправильно задано оформление первого листа спецификации: не указана таблица, предназначенная для спецификации """
    etError155      = 155
    """ Не найдено оформление первого листа спецификации """
    etError156      = 156
    """ Неправильно задано оформление первого листа спецификации: не найдены ячейки типа "Для спецификации". """
    etError157      = 157
    """ Неправильно задано оформление второго и последующих листов спецификации: не указана таблица, предназначенная для спецификации """
    etError158      = 158
    """ Не найдено оформление второго и последующих листов спецификации. """
    etError159      = 159
    """ Неправильно задано оформление второго и последующих листов спецификации: не найдены ячейки типа "Для спецификации". """
    etError160      = 160
    """ Попытка изменить параметры объекта только для чтения. """
    etError161      = 161
    """ Попытка изменить параметры объекта только для чтения. """
    etError162      = 162
    """ Ошибка создания файла библиотекаря фрагментов. """
    etError163      = 163
    """ Текущий документ пустой. Сохранение в выбранном формате производиться не будет. """
    etError164      = 164
    """ Не найдена библиотека стилей спецификаций. """
    etError165      = 165
    """ Размер растра превышает допустимый максимальный размер (65536 x 65536). """
    etError166      = 166
    """ Не хватает памяти для создания растра указанного размера. """
    etError167      = 167
    """ Выбранный диапазон страниц в документе не существует. """
    etError168      = 168
    """ Неверный указатель линии выноски. """
    etError169      = 169
    """ Имя документа изменить нельзя. Документ с таким именем уже открыт. """
    etError170      = 170
    """ Базовый вид должен быть ассоциативным. """
    etError171      = 171
    """ Базовый объект должен быть стрелкой вида. """
    etError172      = 172
    """ Базовый объект должен быть выносным элементом. """
    etError173      = 173
    """ Неправильно задан цвет. """
    etError174      = 174
    """ Неправильно заданы единицы измерения. """
