import os
from setuptools import setup

os.environ["QT_PREFERRED_BINDING"] = "None"
version = __import__("Qt5").__version__


classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]


setup(
    name="Qt5.py",
    version=version,
    description="Python 2 & 3 compatibility wrapper around PyQt5 and PySide2",
    author="Marcus Ottosson",
    author_email="konstruktion@gmail.com",
    url="https://github.com/mottosso/Qt5",
    license="MIT",
    zip_safe=False,
    data_files=["LICENSE"],
    py_modules=["Qt5"],
    classifiers=classifiers
)
