from typing import Sequence

from PySide6 import QtCore, QtQml

from .consts import QML_IMPORT_MAJOR_VERSION, QML_IMPORT_MINOR_VERSION, QML_IMPORT_NAME

try:
    import contourpy
except ModuleNotFoundError:
    CONTOURPY_AVAILABLE = False
else:
    CONTOURPY_AVAILABLE = True


def contour_line(
    x: Sequence[Sequence[float]],
    y: Sequence[Sequence[float]],
    z: Sequence[Sequence[float]],
    height: float,
) -> Sequence[Sequence[QtCore.QPointF]]:
    gen = contourpy.contour_generator(
        x=x, y=y, z=z, line_type=contourpy.LineType.Separate
    )
    result = []
    for loop in gen.lines(height):
        points = [QtCore.QPointF(x, y) for x, y in loop]
        result.append(points)
    return result


def contour_fill(
    x: Sequence[Sequence[float]],
    y: Sequence[Sequence[float]],
    z: Sequence[Sequence[float]],
    heights: tuple[float, float],
) -> Sequence[Sequence[QtCore.QPointF]]:
    gen = contourpy.contour_generator(
        x=x, y=y, z=z, fill_type=contourpy.FillType.OuterOffset
    )
    result = []
    for loop, offsets in zip(*gen.filled(*heights)):
        for start, end in zip(offsets, offsets[1:]):
            points = [QtCore.QPointF(x, y) for x, y in loop[start:end]]
            result.append(points)
    return result


@QtQml.QmlElement
@QtQml.QmlSingleton
class ContourHelper(QtCore.QObject):
    @QtCore.Slot(list, list, list, float, result=list)
    def contourLine(
        self,
        x: Sequence[Sequence[float]],
        y: Sequence[Sequence[float]],
        z: Sequence[Sequence[float]],
        height: float,
    ) -> Sequence[Sequence[QtCore.QPointF]]:
        return contour_line(x, y, z, height)

    @QtCore.Slot(list, list, list, float, float, result=list)
    def contourFill(
        self,
        x: Sequence[Sequence[float]],
        y: Sequence[Sequence[float]],
        z: Sequence[Sequence[float]],
        h_min: float,
        h_max: float,
    ) -> Sequence[Sequence[QtCore.QPointF]]:
        return contour_fill(x, y, z, (h_min, h_max))
