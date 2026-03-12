"""
Основные функции для работы с Компас API.
"""

import typing

from . import KompasAPI7
from . import Kompas6API5
from . import constants
from .is_instance import \
    issubclass_for_KompasAPI, issubclass_for_KompasAPI_by_str,\
    isinstance_for_KompasAPI, isinstance_for_KompasAPI_by_str

import pythoncom
from win32com.client import Dispatch


def ensure_list(obj) -> list:
    """
    Вспомогательная функция, которая гарантированно возвращает список объектов
    (тип возвращаемого значения `list`).

    Актуально для функций Компас-API, которые непредсказуемо возвращают
    или один объект, или массив объектов, или `None`.
    Тип возврата у таких функций задан как `VT_ARRAY | VT_DISPATCH`.
    Например, `IFeature7.ModelObjects()`.

    Пример использования:
    ```python
    edges: list[KAPI7.IEdge] = ensure_list(feature.ModelObjects(LDefin3D.o3d_edge))
    if len(edges) == 0:
        print("Ребра не найдены")
    ```
    """
    if obj is None:
        return []
    if isinstance(obj, (tuple,)):
        return list(obj)
    if isinstance(obj, (list,)):
        return obj
    return [obj]


def get_Kompas6API5_KompasObject() -> Kompas6API5.KompasObject:
    """
    Возвращает объект интерфейса API Компас `KompasObject` (Компас API 5).
    """
    return Kompas6API5.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(
        Kompas6API5.KompasObject.CLSID, pythoncom.IID_IDispatch)) # type: ignore


def get_KompasAPI7_IApplication() -> KompasAPI7.IApplication:
    """
    Возвращает объект интерфейса приложения Компас-3D `IApplication` (Компас API 7).
    """
    return KompasAPI7.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(
        KompasAPI7.IApplication.CLSID, pythoncom.IID_IDispatch)) # type: ignore





def transfer_to_K5(obj: object, o3d_type: int = 0, kompas_object_5: Kompas6API5.KompasObject|None = None) -> typing.Any:
    """
    Преобразует объект интерфейса Компас-API 5 `obj`
    в объект интерфейса Компас-API 7.

    См. также `transfer_to_7()`.
    """
    if kompas_object_5 is None:
        kompas_object_5 = get_Kompas6API5_KompasObject()
    return kompas_object_5.TransferInterface(obj, 1, o3d_type)


def transfer_to_7(obj: object, o3d_type: int = 0, kompas_object_5: Kompas6API5.KompasObject|None = None) -> typing.Any:
    """
    Преобразует объект интерфейса Компас-API 7 `obj`
    в объект интерфейса Компас-API 5.

    См. также `transfer_to_K5()`.
    """
    if kompas_object_5 is None:
        kompas_object_5 = get_Kompas6API5_KompasObject()
    return kompas_object_5.TransferInterface(obj, 2, o3d_type)




def color_traditional_to_kompas(color_traditional: int) -> int:
    """
    Преобразование цвета из традиционного формата `0xRRGGBB` в формат Компаса `0xBBGGRR`.
    """
    r = (color_traditional & 0xff0000) >> 16
    g = (color_traditional & 0x00ff00) >> 8
    b = color_traditional & 0x0000ff
    return (b << 16) | (g << 8) | r

def color_kompas_to_traditional(color_kompas: int) -> int:
    """
    Преобразование цвета из формата Компаса `0xBBGGRR` в традиционный формат `0xRRGGBB`.
    """
    r = color_kompas & 0x0000ff
    g = (color_kompas & 0x00ff00) >> 8
    b = (color_kompas & 0xff0000) >> 16
    return (r << 16) | (g << 8) | b

def pretty_print_color(color: int) -> str:
    """
    Возвращает строковое представление цвета в html-нотациии: `#RRGGBB`.

    Значение `color` уже должно быть в традиционном формате `0xRRGGBB`.
    """
    return "#" + hex(color)[2:].rjust(6, "0")
