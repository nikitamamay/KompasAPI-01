
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

    # bodies: list[KompasAPI7.IBody7] = core.ensure_list(feature.ResultBodies)

    # if len(bodies) < 1:
    #     print("Ошибка: нет тел в модели")
    #     return

    # body = bodies[0]

    mos: list[KompasAPI7.IModelObject] = core.ensure_list(feature.ModelObjects(constants.ksObj3dTypeEnum.o3d_unknown))

    for mo in mos:
        print(mo, mo.__class__.__name__, end=" ")
        print(core.isinstance_for_KompasAPI(mo, KompasAPI7.IPlane3D))



if __name__ == "__main__":
    main()
