"""
Пример, демонстрирующий работу функции `core.isinstance_for_KompasAPI()`.

Для работы следует открыть 3D-модель, в которой должны быть плоскости, построенные
произвольным образом (командами "Смещенная плоскость", "Плоскость через 3 точки",
"Плоскость под углом" и/или др.).
При запуске скрипта будут найдены объекты всех плоскостей, так как классы этих объектов
наследуются от класса `KompasAPI7.IPlane3D` и тем самым проходят проверку
функцией `core.isinstance_for_KompasAPI(obj, KompasAPI7.IPlane3D)`.

"""

import typing

from KompasAPI_01 import KompasAPI7, Kompas6API5, constants, core, extras



def main():
    app7 = core.get_KompasAPI7_IApplication()

    doc = app7.ActiveDocument
    if doc is None or not extras.is_3d_document(doc):
        print("Ошибка: не 3d-документ")
        return

    doc = KompasAPI7.IKompasDocument3D(doc)

    part: KompasAPI7.IPart7 = doc.TopPart

    feature = KompasAPI7.IFeature7(part)

    mos: list[KompasAPI7.IModelObject] = core.ensure_list(feature.ModelObjects(constants.ksObj3dTypeEnum.o3d_unknown))

    planes = list(filter(lambda mo: core.isinstance_for_KompasAPI(mo, KompasAPI7.IPlane3D), mos))

    print(f"Найдено плоскостей: {len(planes)}")
    for plane in planes:
        print(f"class_name={plane.__class__.__name__}, name='{plane.Name}'")



if __name__ == "__main__":
    main()
