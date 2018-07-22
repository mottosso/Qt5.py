<img width=260 src=logo.svg>

Qt5.py enables you to write software that runs the same on both PySide2 and PyQt5.

**See also**

- [Qt.py](https://github.com/mottosso/Qt.py) - Like Qt5.py, with added support for PySide and PyQt4.

<br>

### Goals

Write once, run in any binding.

Qt5.py is the younger brother to [Qt.py](https://github.com/mottosso/Qt.py) and provides extended support for features unique to Qt 5, such as QtQml, QtMultimedia and QtWebAssembly.

| Goal | Description
|:-----|:---------
| *Support co-existence* | Qt5.py should not affect other bindings, not even Qt.py, running in the same interpreter session
| *Build for one, run with all* | Code written with Qt5.py should run identically on both PySide2 and PyQt5
| *Explicit is better than implicit* | Differences between bindings should be visible to you.

<br>
<br>
<br>

### Install

Qt5.py is a single file and can be either [copy/pasted](https://raw.githubusercontent.com/mottosso/Qt5.py/master/Qt5.py) into your project, [downloaded](https://github.com/mottosso/Qt5.py/archive/master.zip) as-is, cloned as-is or installed via `pip`.

```bash
# From PyPI
$ pip install Qt5.py
```

- Pro tip: The direct download and clone options refer to the latest commit of this project, which is typically beta. For the latest **stable** release, refer to any of the official [releases](https://github.com/mottosso/Qt5.py/releases)
- Pro top: Qt5.py supports [vendoring](https://fredrikaverpil.github.io/2017/05/04/vendoring-qt-py/)

<br>
<br>
<br>

### Usage

Use Qt5.py as you would use PySide2.

<img width=242 src=https://user-images.githubusercontent.com/2152766/43045221-659284c8-8dac-11e8-8e96-693471050a66.png>

```python
import os
import sys
import tempfile

from Qt5 import QtGui, QtQml

f = tempfile.NamedTemporaryFile("w", delete=False)
f.write("""\
import QtQuick 2.4
import QtQuick.Controls 1.4

ApplicationWindow {
    title: "My App"
    width: 240
    height: 180
    visible: true

    Button {
        text: "Hello World"
        anchors.centerIn: parent
    }
}
""")
f.close()

app = QtGui.QGuiApplication(sys.argv)
engine = QtQml.QQmlApplicationEngine()
engine.load(f.name)
engine.quit.connect(app.quit)
app.exec_()
os.remove(f.name)
```
