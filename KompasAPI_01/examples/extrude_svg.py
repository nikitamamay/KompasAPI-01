"""
Макрос, демонстрирующий работу с эскизами и создание операции вытягивания
на примере рисования логотипа Компас-3D из SVG-файла.

Для работы скрипта требуется библиотека `svg.path`. Установите её с помощью команды:
```
pip install svg.path
```

"""

import typing

import os
try:
    import svg.path
except:
    print("Ошибка: для работы скрипта требуется библиотека 'svg.path'.")
    exit(1)

from KompasAPI_01 import KompasAPI7, Kompas6API5, constants, core, extras

import re


Point2d: typing.TypeAlias = tuple[float, float]|list[float]


re_path_d = re.compile(r"<path[^>]*\bd=['\"](.*?)['\"]", re.DOTALL | re.IGNORECASE)
""" Регулярное выражение для поиска svg path definition """

re_viewbox = re.compile(r"<svg[^>]*\bviewBox=['\"](-?[\d\.]+)\s+(-?[\d\.]+)\s+(-?[\d\.]+)\s+(-?[\d\.]+)['\"]", re.DOTALL | re.IGNORECASE)
""" Регулярное выражение для поиска svg viewBox """

height: float = 8
""" Высота выдавливания """

body_color: int = 0x4fa8eb
""" Цвет тела выдавливания в традиционном формате 0xRRGGBB """

DEFAULT_SVG_FILEPATH = os.path.join(os.path.dirname(__file__), "img/kompas-logo.svg")
""" Путь к SVG-файлу логотипа Компас """

DEFAULT_KOMPAS_FILEPATH = "./kompas_logo.m3d"
""" Путь к файлу модели """


def read_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        svg_xml = f.read()
    return svg_xml


def iterate_paths(svg_xml: str):
    for m in re_path_d.finditer(svg_xml):
        svg_path_def = m.group(1)
        path: svg.path.Path = svg.path.parse_path(svg_path_def)
        yield path


def get_svg_viewBox(svg_xml: str) -> tuple[Point2d, Point2d] | None:
    m = re_viewbox.search(svg_xml)
    if m is None:
        print(f"get_svg_viewBox(): не найден svg[viewBox]")
        return None
    try:
        x = float(m.group(1))
        y = float(m.group(2))
        w = float(m.group(3))
        h = float(m.group(4))
    except Exception as e:
        print(f"get_svg_viewBox(): {e}")
        return None
    return ((x, y), (w, h))


def get_point(point_complex: complex, do_reverse_y: bool = False) -> Point2d:
    """
    Возвращает точку в виде `tuple[float, float]`.

    `do_reverse_y` может быть актуален, потому что что в svg ось Y сверху вниз, а в Компас наоборот.
    """
    point = (point_complex.real, point_complex.imag)
    if do_reverse_y:
        return reverse_point_y(point)
    return point


def add_points(point: Point2d, delta: Point2d) -> Point2d:
    return (point[0] + delta[0], point[1] + delta[1])


def multiply_point(point: Point2d, x: float) -> Point2d:
    return (point[0] * x, point[1] * x)

def reverse_point_y(point: Point2d) -> Point2d:
    return (point[0], point[1] * -1)


def main(svg_filepath: str, kompas_filepath: str):
    global height

    kompas_filepath = os.path.abspath(kompas_filepath)
    svg_filepath = os.path.abspath(svg_filepath)

    svg_xml = read_file(svg_filepath)

    paths = list(iterate_paths(svg_xml))

    delta: Point2d = (0, 0)
    viewbox = get_svg_viewBox(svg_xml)
    if viewbox is not None:
        delta = reverse_point_y(multiply_point(add_points(viewbox[0], multiply_point(viewbox[1], 1/2)), -1))
        size = viewbox[1]
        height = min(size) / 10
        print(f"Размеры изображения: {size}")

    app7 = core.get_KompasAPI7_IApplication()
    app7.Visible = True

    docs = app7.Documents

    # поиск документа с указанным путем к файлу среди открытых документов.
    # если найден, то этот документ закрывается без сохранения,
    # чтобы в конце построений можно было перезаписать файл документа.
    for i in range(docs.Count):
        d = docs.Item(i)
        try:
            if os.path.samefile(d.PathName, kompas_filepath):
                d.Close(constants.DocumentCloseOptions.kdDoNotSaveChanges)
        except:
            pass

    doc = KompasAPI7.IKompasDocument3D(app7.Documents.Add(constants.DocumentTypeEnum.ksDocumentPart, True))
    part: KompasAPI7.IPart7 = doc.TopPart

    doc.HideAllPlanes = True
    doc.HideAllAxis = True

    plane = part.DefaultObject(constants.ksObj3dTypeEnum.o3d_planeXOY)

    mc = KompasAPI7.IModelContainer(part)
    sketches = mc.Sketchs

    if viewbox is not None:
        sketch = sketches.Add()
        sketch.Name = "Габарит рисунка"
        sketch.Plane = plane
        sketch.Update()

        fragment_doc = sketch.BeginEdit()

        vlm = fragment_doc.ViewsAndLayersManager

        view = vlm.Views.View(0)  # системный вид фрагмента (= эскиза) под индексом 0

        dc = KompasAPI7.IDrawingContainer(view)
        line_segments = dc.LineSegments

        top_left = viewbox[0]
        bottom_right = add_points(viewbox[0], viewbox[1])
        for start, end in [
                ((top_left[0], top_left[1]), (top_left[0], bottom_right[1])),
                ((top_left[0], bottom_right[1]), (bottom_right[0], bottom_right[1])),
                ((bottom_right[0], bottom_right[1]), (bottom_right[0], top_left[1])),
                ((bottom_right[0], top_left[1]), (top_left[0], top_left[1])),
                ]:
            line_segment = line_segments.Add()
            x1, y1 = add_points(reverse_point_y(start), delta)
            x2, y2 = add_points(reverse_point_y(end), delta)

            line_segment.X1 = x1
            line_segment.Y1 = y1
            line_segment.X2 = x2
            line_segment.Y2 = y2

            line_segment.Update()

        sketch.EndEdit()

    for path in paths:
        sketch = sketches.Add()
        sketch.Plane = plane
        sketch.Update()

        fragment_doc = sketch.BeginEdit()

        vlm = fragment_doc.ViewsAndLayersManager

        view = vlm.Views.View(0)  # системный вид фрагмента (= эскиза) под индексом 0

        dc = KompasAPI7.IDrawingContainer(view)
        line_segments = dc.LineSegments
        bezier_splines = dc.Beziers

        for segment in path:
            if isinstance(segment, (svg.path.Line, svg.path.Close)):
                line_segment = line_segments.Add()
                x1, y1 = add_points(get_point(segment.start, True), delta)
                x2, y2 = add_points(get_point(segment.end, True), delta)

                line_segment.X1 = x1
                line_segment.Y1 = y1
                line_segment.X2 = x2
                line_segment.Y2 = y2

                line_segment.Update()

            elif isinstance(segment, svg.path.CubicBezier):
                bezier_spline: KompasAPI7.IBezier = bezier_splines.Add()
                x1,  y1  = add_points(get_point(segment.start, True), delta)
                c1x, c1y = add_points(get_point(segment.control1, True), delta)
                c2x, c2y = add_points(get_point(segment.control2, True), delta)
                x2,  y2  = add_points(get_point(segment.end, True), delta)

                bezier_spline.AddPoint(0, x1, y1, x1, y1, c1x, c1y)
                bezier_spline.AddPoint(1, x2, y2, c2x, c2y, x2, y2)

                bezier_spline.Update()

            elif isinstance(segment, svg.path.Move):
                pass

            else:
                print(f"Unsupported type={type(segment)} for: {segment}")

        # view.Update()

        sketch.EndEdit()

        extrusions = mc.Extrusions
        extrusion: KompasAPI7.IExtrusion = extrusions.Add(constants.ksObj3dTypeEnum.o3d_bossExtrusion)
        extrusion.SetDepth(True, height)
        extrusion.Sketch = sketch
        extrusion.Update()

        bodies = core.ensure_list(extrusion.Owner.ResultBodies)
        if len(bodies) > 0:
            body = bodies[0]

            part_color_param = KompasAPI7.IColorParam7(body)
            part_color_param.Color = core.color_traditional_to_kompas(body_color)

            body.Update()

        app7.ExecuteKompasCommand(constants.ksCMZoomEntireDocument, True)

    doc.SaveAs(kompas_filepath)
    print(f"Деталь сохранена в файл '{kompas_filepath}'")




if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Для рисунка из SVG-файла создать эскиз и выдавить его в 3D-модели.')

    parser.add_argument(
        '-s', '--svg',
        default=DEFAULT_SVG_FILEPATH, type=str,
        help=f'путь к svg-файлу изображения. По умолчанию {DEFAULT_SVG_FILEPATH}')
    parser.add_argument(
        '-o', '--output',
        default=DEFAULT_KOMPAS_FILEPATH, type=str,
        help=f'путь к файлу модели Компас-3D.\nЕсли файл не существует, будет создан; если существует, будет перезаписан. По умолчанию {DEFAULT_KOMPAS_FILEPATH}')

    args = parser.parse_args()
    if len(sys.argv) < 2:
        print("Используются настройки по умолчанию. Используйте --help, чтобы узнать, какие опции можно задать.\n")

    svg_filepath: str = args.svg
    kompas_filepath: str = args.output

    main(svg_filepath, kompas_filepath)
