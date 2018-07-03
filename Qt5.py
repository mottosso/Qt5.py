import types

QtCompat = types.ModuleType("QtCompat")

try:
    from PySide2 import (
        QtWidgets,
        QtCore,
        QtGui,
        QtQml,
        QtQuick,
    )

    from shiboken2 import wrapInstance
    QtCompat.wrapInstance = wrapInstance


except ImportError:
    from PyQt5 import (
        QtWidgets,
        QtCore,
        QtGui,
        QtQml,
        QtQuick,
    )

    QtCore.Signal = QtCore.pyqtSignal
    QtCore.Slot = QtCore.pyqtSlot
    QtCore.Property = QtCore.pyqtProperty

    from sip import wrapinstance as wrapInstance
    QtCompat.wrapInstance = wrapInstance


__all__ = [
    "QtWidgets",
    "QtCore",
    "QtGui",
    "QtQml",
    "QtQuick",
    "QtCompat",
]
