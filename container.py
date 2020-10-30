import inject

from cafe.object_service import CafeRepository


def di_configure(binder):
    binder.bind(CafeRepository())


inject.configure(di_configure)

