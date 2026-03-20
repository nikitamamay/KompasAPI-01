"""
Макрос для обновления положения точки, которая должна быть расположена в центре масс модели.

Такую точку можно создать с помощью команды "МЦХ модели > Создать точку в центре масс", но перестроить при изменении ЦМ модели встроенными средствами невозможно

"""


import typing

from KompasAPI_01 import KompasAPI7, Kompas6API5, constants, core, extras


DEFAULT_POINT_NAME = "Точка в ЦМ:1"


def main(point_name):
    app7 = core.get_KompasAPI7_IApplication()

    doc = app7.ActiveDocument
    if doc is None or not extras.is_3d_document(doc):
        print("Ошибка: не 3d-документ")
        return

    doc = KompasAPI7.IKompasDocument3D(doc)

    part: KompasAPI7.IPart7 = doc.TopPart

    mc = KompasAPI7.IModelContainer(part)
    points = mc.Points3D

    point: KompasAPI7.IPoint3D|None = None

    for i in range(points.Count):
        p = points.Point3D(i)
        if p.Name == point_name:
            feature = p.Owner
            if feature is not None and not feature.Excluded:
                point = p
                break

    if point is None:
        print(f"Точка с именем {repr(point_name)} не найдена. Будет создана новая.")
        point = points.Add()
        point.Symbol = constants.ksAnnotationSymbolEnum.ksStrikeSquarePoint
        point.Name = point_name
        point.Update()

    mip = KompasAPI7.IMassInertiaParam7(part)

    # Внимание! Ошибка в Справке Компас: нужно указывать `ksLengthUnitsEnum`, а не `ksLengthUnitEnum`!
    # Более того, значения в перечислениях `ksLengthUnitsEnum` и `ksLengthUnitEnum` не одни и те же, а совершенно разные!
    mip.LengthUnits = constants.ksLengthUnitsEnum.ksLUnMM
    part.Update()

    mip.Calculate()

    # # переводной коэффициент из единиц Компас в миллиметры
    # multiple = {
    #     constants.ksLengthUnitsEnum.ksLUnMM: 1,
    #     constants.ksLengthUnitsEnum.ksLUnSM: 10,
    #     constants.ksLengthUnitsEnum.ksLUnDM: 100,
    #     constants.ksLengthUnitsEnum.ksLUnM    : 1000,
    #     constants.ksLengthUnitsEnum.ksLUnDocument : 1,
    # }[mip.LengthUnits]  # По умолчанию там сантиметры...
    multiple = 1

    cX = mip.Xc * multiple
    cY = mip.Yc * multiple
    cZ = mip.Zc * multiple

    point.X = cX
    point.Y = cY
    point.Z = cZ

    point.Update()
    part.Update()

    print(f"Центр масс: X={cX}, Y={cY}, Z={cZ}")
    print(f"Обновлена точка '{point_name}'.")



if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Перестроить существующую точку в центре масс (или создать новую) в текущей 3D-модели.')

    parser.add_argument(
        '-p', '--point',
        default=DEFAULT_POINT_NAME, type=str,
        help='имя точки, которая должна быть построена в центре масс модели.')

    args = parser.parse_args()
    if len(sys.argv) < 2:
        print("Используются настройки по умолчанию. Используйте --help, чтобы узнать, какие опции можно задать.\n")

    point_name: str = args.point

    main(point_name)
