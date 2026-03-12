"""
Дополнительные функции для упрощения работы с Компас API.
"""

from . import KompasAPI7, constants


def is_3d_document(obj: KompasAPI7.IKompasAPIObject) -> bool:
    """
    Возвращает `True`, если текущий объект является 3D-документом
    (моделью детали или сборки).
    """
    return obj.Type in (
        constants.KompasAPIObjectTypeEnum.ksObjectAssemblyDocument,
        constants.KompasAPIObjectTypeEnum.ksObjectPartDocument,
    )

