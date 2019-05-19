# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
#
# Created: Sat Aug 20 00:38:16 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(380, 260)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/images/logo.png")))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About QuickRecon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AboutDialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("AboutDialog", "License", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
