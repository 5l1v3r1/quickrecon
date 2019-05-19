# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xfndialog.ui'
#
# Created: Sat Aug 20 00:39:05 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_XFNDialog(object):
    def setupUi(self, XFNDialog):
        XFNDialog.setObjectName(_fromUtf8("XFNDialog"))
        XFNDialog.resize(466, 279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        XFNDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(XFNDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(XFNDialog)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/images/xfn.png")))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(XFNDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(XFNDialog)
        QtCore.QMetaObject.connectSlotsByName(XFNDialog)

    def retranslateUi(self, XFNDialog):
        XFNDialog.setWindowTitle(QtGui.QApplication.translate("XFNDialog", "XFN quick reference", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
