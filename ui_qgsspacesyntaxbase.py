
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\iletisim.ui'
#
# Created: Tue Sep 27 11:36:35 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QgsSpaceSyntaxBase(object):
    def setupUi(self, QgsSpaceSyntaxBase):
        QgsSpaceSyntaxBase.setObjectName(_fromUtf8("QgsSpaceSyntaxBase"))
        QgsSpaceSyntaxBase.resize(261, 300)
        QgsSpaceSyntaxBase.setWindowTitle(QtGui.QApplication.translate("Dialog", "Space Syntax Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(QgsSpaceSyntaxBase)
        self.buttonBox.setGeometry(QtCore.QRect(10, 265, 200, 23))
        self.buttonBox.setMinimumSize(QtCore.QSize(200, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.groupBox_1 = QtGui.QGroupBox(QgsSpaceSyntaxBase)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 170, 240, 80))
        self.groupBox_1.setTitle(QtGui.QApplication.translate("Dialog", "Options for headings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_1.setObjectName(_fromUtf8("groupBox_1"))

        self.radioButton = QtGui.QRadioButton(self.groupBox_1)
        self.radioButton.setGeometry(QtCore.QRect(10, 52, 117, 17))
        self.radioButton.setText(QtGui.QApplication.translate("Dialog", "Use a field.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setEnabled(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_1)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 20, 153, 22))
        self.radioButton_2.setText(QtGui.QApplication.translate("Dialog", "Use internal index.", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

        self.checkBox_2 = QtGui.QCheckBox(QgsSpaceSyntaxBase)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 50, 226, 17))
        self.checkBox_2.setText(QtGui.QApplication.translate("Dialog", "Calculate intellegibility value.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.checkBox_3 = QtGui.QCheckBox(QgsSpaceSyntaxBase)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 80, 170, 17))
        self.checkBox_3.setText(QtGui.QApplication.translate("Dialog", "Create network data:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))

        self.comboBox_1 = QtGui.QComboBox(QgsSpaceSyntaxBase)
        self.comboBox_1.setGeometry(QtCore.QRect(180, 78, 50, 22))
        self.comboBox_1.setEnabled(False)
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.comboBox_1.addItem(unicode("dl"))
        self.comboBox_1.addItem(unicode("net"))

        self.checkBox_4 = QtGui.QCheckBox(QgsSpaceSyntaxBase)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 110, 180, 17))
        self.checkBox_4.setText(QtGui.QApplication.translate("Dialog", "Create geodesic matrix.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))

        self.checkBox_5 = QtGui.QCheckBox(QgsSpaceSyntaxBase)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 140, 226, 17))
        self.checkBox_5.setText(QtGui.QApplication.translate("Dialog", "Save file(s) in a different location.", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))

        self.comboBox = QtGui.QComboBox(QgsSpaceSyntaxBase)
        self.comboBox.setGeometry(QtCore.QRect(140, 218, 101, 22))
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.label = QtGui.QLabel(QgsSpaceSyntaxBase)
        self.label.setGeometry(QtCore.QRect(10, 20, 125, 20))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Radius for local:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))

        self.param = QtGui.QLineEdit(QgsSpaceSyntaxBase)
        self.param.setGeometry(QtCore.QRect(140, 20, 81, 20))
        self.param.setEnabled(True)
        self.param.setText("3")
        self.param.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.param.setCursorPosition(0)
        self.param.setObjectName(_fromUtf8("param"))

        self.retranslateUi(QgsSpaceSyntaxBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QgsSpaceSyntaxBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QgsSpaceSyntaxBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QgsSpaceSyntaxBase)

    def retranslateUi(self, QgsSpaceSyntaxBase):
        pass

