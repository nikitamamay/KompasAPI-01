"""
Основные функции для работы с Компас API.
"""

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

