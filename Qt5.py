import os
import types
import sys

QT_VERBOSE = bool(os.getenv("QT_VERBOSE"))
QtCompat = types.ModuleType("QtCompat")


def _log(text):
    if QT_VERBOSE:
        sys.stdout.write(text + "\n")


try:
    from PySide2 import (
        QtWidgets,
        QtCore,
        QtGui,
        QtQml,
        QtQuick,
    )

    from shiboken2 import wrapInstance, getCppPointer
    QtCompat.wrapInstance = wrapInstance
    QtCompat.getCppPointer = getCppPointer
    try:
        from PySide2 import QtUiTools

        QtCompat.loadUi = QtUiTools.QUiLoader
    except ImportError:
        _log("QtUiTools not provided.")


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

    from sip import wrapinstance, unwrapinstance
    QtCompat.wrapInstance = wrapinstance
    QtCompat.getCppPointer = unwrapinstance

    try:
        from PyQt5 import uic
        QtCompat.loadUi = uic.loadUi
    except ImportError:
        _log("uic not provided.")


__all__ = [
    "QtWidgets",
    "QtCore",
    "QtGui",
    "QtQml",
    "QtQuick",
    "QtCompat",
]
