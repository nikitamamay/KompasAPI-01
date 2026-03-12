"""
Реализация функций `issubclass_for_KompasAPI()`, `isinstance_for_KompasAPI()`
для корректной работой с иерархией классов Компас API.
"""
import typing

from . import classes_hierarchy
from .classes_hierarchy import CLASS_NAME_IDISPATCH






def get_KompasAPI_base_classes(kompas_api_class_name: str) -> tuple[bool, list[str]]:
    """
    Возвращает рекурсивно имена всех родительских классов до `IDispatch` включительно
    у класса `kompas_api_class_name`.

    Пример:
    ```
    >>> get_KompasAPI_base_classes("IAxis3DBy2Points")
    ['IAxis3D', 'IModelObject', 'IKompasAPIObject', 'IDispatch']
    ```
    """
    if not kompas_api_class_name in classes_hierarchy.KompasAPIclassesHierarchy:
        return (False, [])
        # raise LookupError(f"KompasAPI_01.classes_hierarchy has no hierarchy for class {repr(kompas_api_class_name)}")

    base_classes = []

    for cls_ in classes_hierarchy.KompasAPIclassesHierarchy[kompas_api_class_name]:
        base_classes.append(cls_)
        base_classes.extend(get_KompasAPI_base_classes(cls_))

    # не надо добавлять отсутствующий в списке "IDispatch",
    # потому что некоторые классы (например, событий) от него не_наследуются.
    # if not CLASS_NAME_IDISPATCH in base_classes:
    #     base_classes.append(CLASS_NAME_IDISPATCH)

    return (True, base_classes)


def _is_str_subclass_for_KompasAPI_by_str(
        class_name: str,
        target_class_names: typing.Container[str],
        ) -> bool:
    """
    Реализация функции `issubclass()` для классов Компас API с учетом их иерархии.

    См. также `get_KompasAPI_base_classes()`.
    """
    if class_name in target_class_names:
        return True

    if not class_name in classes_hierarchy.KompasAPIclassesHierarchy:
        raise LookupError(f"KompasAPI_01.classes_hierarchy has no hierarchy for class {repr(class_name)}")

    base_classes = classes_hierarchy.KompasAPIclassesHierarchy[class_name]
    for bc in base_classes:
        if _is_str_subclass_for_KompasAPI_by_str(bc, target_class_names):
            return True
    return False


def issubclass_for_KompasAPI_by_str(
        cls: type,
        target_class_names: typing.Container[str],
        ) -> bool:
    """
    Так же, как и `issubclass_for_KompasAPI()`, только принимает вторым аргументов
    массив строк - названий классов (`object.__class__.__name__`).
    """
    return _is_str_subclass_for_KompasAPI_by_str(cls.__name__, target_class_names)


def issubclass_for_KompasAPI(
        cls: type,
        class_or_tuple: type | tuple[type],
        ) -> bool:
    """
    Аналог `issubclass()`, но второй аргумент предназначен **только** для классов Компас API.

    Проверяет, если `cls` является классом `class_or_tuple` или его дочерним классом.

    Так же, как и в `issubclass()`, второй аргумент `class_or_tuple` может быть
    неизменяемым массивом (`tuple`) нескольких классов, тогда функция вернет `True`,
    если выполнится проверка хотя бы для одного из них.

    Самый низший уровень иерархии `class_or_tuple` - это `IDispatch`.
    """
    class_or_tuple = (class_or_tuple, ) if not isinstance(class_or_tuple, tuple) else class_or_tuple
    return _is_str_subclass_for_KompasAPI_by_str(
        cls.__name__,
        [c.__name__ for c in class_or_tuple]
    )


def isinstance_for_KompasAPI_by_str(
        obj: object,
        target_class_names: typing.Container[str],
        ) -> bool:
    """
    Так же, как и `isinstance_for_KompasAPI()`, только принимает вторым аргументов
    массив строк - названий классов (`object.__class__.__name__`).
    """
    return _is_str_subclass_for_KompasAPI_by_str(obj.__class__.__name__, target_class_names)


def isinstance_for_KompasAPI(
        obj: object,
        class_or_tuple: type | tuple[type],
        ) -> bool:
    """
    Аналог `isinstance()`, но второй аргумент предназначен **только** для классов Компас API.

    Проверяет, если `obj` является объектом класса `class_or_tuple` или его дочернего класса.

    Так же, как и в `isinstance()`, второй аргумент `class_or_tuple` может быть
    неизменяемым массивом (`tuple`) нескольких классов, тогда функция вернет `True`,
    если выполнится проверка хотя бы для одного из них.

    Самый низший уровень иерархии `class_or_tuple` - это `IDispatch`.
    """
    class_or_tuple = (class_or_tuple, ) if not isinstance(class_or_tuple, tuple) else class_or_tuple
    return _is_str_subclass_for_KompasAPI_by_str(
        obj.__class__.__name__,
        [c.__name__ for c in class_or_tuple]
    )
