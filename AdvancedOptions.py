# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdvancedOptions.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdvancedWindow(object):
    def setupUi(self, AdvancedWindow):
        AdvancedWindow.setObjectName("AdvancedWindow")
        AdvancedWindow.resize(929, 739)
        AdvancedWindow.setStyleSheet("QWidget#AdvancedWindow{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(204, 255, 203, 255), stop:1 rgba(152, 255, 233, 255))}")
        self.centralwidget = QtWidgets.QWidget(AdvancedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 80, 691, 451))
        self.label.setStatusTip("")
        self.label.setStyleSheet("border: 1px solid gray;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.databaseInput = QtWidgets.QLineEdit(self.centralwidget)
        self.databaseInput.setGeometry(QtCore.QRect(180, 361, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.databaseInput.setPalette(palette)
        self.databaseInput.setText("")
        self.databaseInput.setObjectName("databaseInput")
        self.versionCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.versionCheckBox.setGeometry(QtCore.QRect(290, 140, 85, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.versionCheckBox.setPalette(palette)
        self.versionCheckBox.setObjectName("versionCheckBox")
        self.keepCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.keepCheckBox.setGeometry(QtCore.QRect(180, 140, 85, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.keepCheckBox.setPalette(palette)
        self.keepCheckBox.setStatusTip("By default, intermediate files are deleted. Activate\n"
"this flag to keep intermediate files.\n"
" ")
        self.keepCheckBox.setObjectName("keepCheckBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 360, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(282, 250, 81, 21))
        self.label_4.setObjectName("label_4")
        self.verbosityDropdownMenu = QtWidgets.QComboBox(self.centralwidget)
        self.verbosityDropdownMenu.setGeometry(QtCore.QRect(180, 250, 91, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(245, 223, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 223, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(245, 223, 253))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.verbosityDropdownMenu.setPalette(palette)
        self.verbosityDropdownMenu.setObjectName("verbosityDropdownMenu")
        self.verbosityDropdownMenu.addItem("")
        self.verbosityDropdownMenu.addItem("")
        self.verbosityDropdownMenu.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 111, 41))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(160, 120, 91, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(150, 110, 31, 21))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(150, 220, 31, 21))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 210, 111, 41))
        self.label_7.setObjectName("label_7")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(160, 230, 91, 20))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(150, 330, 31, 21))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 320, 111, 41))
        self.label_5.setObjectName("label_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(160, 340, 91, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.threadsInput = QtWidgets.QLineEdit(self.centralwidget)
        self.threadsInput.setGeometry(QtCore.QRect(180, 401, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.threadsInput.setPalette(palette)
        self.threadsInput.setText("")
        self.threadsInput.setObjectName("threadsInput")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 400, 61, 21))
        self.label_6.setObjectName("label_6")
        self.TMPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.TMPInput.setGeometry(QtCore.QRect(370, 361, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.TMPInput.setPalette(palette)
        self.TMPInput.setText("")
        self.TMPInput.setObjectName("TMPInput")
        self.qualityInput = QtWidgets.QLineEdit(self.centralwidget)
        self.qualityInput.setGeometry(QtCore.QRect(370, 401, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.qualityInput.setPalette(palette)
        self.qualityInput.setText("")
        self.qualityInput.setObjectName("qualityInput")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 360, 31, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 400, 111, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(630, 399, 61, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(630, 359, 31, 21))
        self.label_11.setObjectName("label_11")
        self.baseFractionInput = QtWidgets.QLineEdit(self.centralwidget)
        self.baseFractionInput.setGeometry(QtCore.QRect(570, 360, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.baseFractionInput.setPalette(palette)
        self.baseFractionInput.setText("")
        self.baseFractionInput.setObjectName("baseFractionInput")
        self.cgmlstInput = QtWidgets.QLineEdit(self.centralwidget)
        self.cgmlstInput.setGeometry(QtCore.QRect(570, 400, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.cgmlstInput.setPalette(palette)
        self.cgmlstInput.setText("")
        self.cgmlstInput.setObjectName("cgmlstInput")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(430, 439, 81, 21))
        self.label_12.setObjectName("label_12")
        self.forwardInput = QtWidgets.QLineEdit(self.centralwidget)
        self.forwardInput.setGeometry(QtCore.QRect(180, 440, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.forwardInput.setPalette(palette)
        self.forwardInput.setText("")
        self.forwardInput.setObjectName("forwardInput")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(630, 438, 41, 21))
        self.label_13.setObjectName("label_13")
        self.MMHInput = QtWidgets.QLineEdit(self.centralwidget)
        self.MMHInput.setGeometry(QtCore.QRect(570, 439, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.MMHInput.setPalette(palette)
        self.MMHInput.setText("")
        self.MMHInput.setObjectName("MMHInput")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(240, 439, 81, 21))
        self.label_14.setObjectName("label_14")
        self.reverseInput = QtWidgets.QLineEdit(self.centralwidget)
        self.reverseInput.setGeometry(QtCore.QRect(370, 440, 51, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.reverseInput.setPalette(palette)
        self.reverseInput.setText("")
        self.reverseInput.setObjectName("reverseInput")
        self.crossDetailsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.crossDetailsCheckBox.setGeometry(QtCore.QRect(400, 140, 131, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 225, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 239))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.crossDetailsCheckBox.setPalette(palette)
        self.crossDetailsCheckBox.setObjectName("crossDetailsCheckBox")
        AdvancedWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdvancedWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 19))
        self.menubar.setObjectName("menubar")
        AdvancedWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdvancedWindow)
        self.statusbar.setObjectName("statusbar")
        AdvancedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdvancedWindow)
        QtCore.QMetaObject.connectSlotsByName(AdvancedWindow)

    def retranslateUi(self, AdvancedWindow):
        _translate = QtCore.QCoreApplication.translate
        AdvancedWindow.setWindowTitle(_translate("AdvancedWindow", "MainWindow"))
        self.versionCheckBox.setStatusTip(_translate("AdvancedWindow", "Show program\'s version number and exit"))
        self.versionCheckBox.setText(_translate("AdvancedWindow", "V"))
        self.keepCheckBox.setText(_translate("AdvancedWindow", "K"))
        self.label_2.setStatusTip(_translate("AdvancedWindow", "Databases folder. To download these, you will need to get access to the rMLST databases. For complete instructions on how to do this, please see https://olc-bioinformatics.github.io/ConFindr/install/#downloading-confindr-databases\n"
" "))
        self.label_2.setText(_translate("AdvancedWindow", "DATABASES"))
        self.label_4.setStatusTip(_translate("AdvancedWindow", "Amount of output you want printed to the screen. Defaults to info, which should be good for most users.\n"
" "))
        self.label_4.setText(_translate("AdvancedWindow", "VERBOSITY"))
        self.verbosityDropdownMenu.setItemText(0, _translate("AdvancedWindow", "INFO"))
        self.verbosityDropdownMenu.setItemText(1, _translate("AdvancedWindow", "DEBUG"))
        self.verbosityDropdownMenu.setItemText(2, _translate("AdvancedWindow", "WARNING"))
        self.label_3.setText(_translate("AdvancedWindow", "Checkboxes"))
        self.label_7.setText(_translate("AdvancedWindow", "Dropdowns"))
        self.label_5.setText(_translate("AdvancedWindow", "Inputs"))
        self.label_6.setStatusTip(_translate("AdvancedWindow", "Number of threads to run analysis with.\n"
" "))
        self.label_6.setText(_translate("AdvancedWindow", "THREADS"))
        self.label_8.setStatusTip(_translate("AdvancedWindow", "If your ConFindr databases are in a location you don\'t have write access to, you can enter this option to specify a temporary directory to put genus-specific databases to."))
        self.label_8.setText(_translate("AdvancedWindow", "TMP"))
        self.label_9.setStatusTip(_translate("AdvancedWindow", "Base quality needed to support a multiple allele call. Defaults to 20."))
        self.label_9.setText(_translate("AdvancedWindow", "QUALITY CUTOFF"))
        self.label_10.setStatusTip(_translate("AdvancedWindow", "Path to a cgMLST database to use for contamination\n"
"detection instead of using the default rMLST database.\n"
"Sequences in this file should have headers in format\n"
">genename_allelenumber. To speed up ConFindr runs, clustering the cgMLST database with CD-HIT before running ConFindr is recommended. This is highly experimental, results should be interpreted with great\n"
"care."))
        self.label_10.setText(_translate("AdvancedWindow", "CGMLST"))
        self.label_11.setStatusTip(_translate("AdvancedWindow", "(Base Fraction Cutoff) Fraction of bases necessary to support a multiple allele call. Particularly useful when dealing with\n"
"very high coverage samples. Default is 0.05."))
        self.label_11.setText(_translate("AdvancedWindow", "BFC"))
        self.label_12.setStatusTip(_translate("AdvancedWindow", "Identifier for reverse reads."))
        self.label_12.setText(_translate("AdvancedWindow", "REVERSE ID"))
        self.label_13.setStatusTip(_translate("AdvancedWindow", "(Min Matching Hashes) Minimum number of matching hashes in a MASH screen in order for a genus to be considered present in a\n"
"sample. Default is 150.\n"
" "))
        self.label_13.setText(_translate("AdvancedWindow", "MMH"))
        self.label_14.setStatusTip(_translate("AdvancedWindow", "Identifier for forward reads."))
        self.label_14.setText(_translate("AdvancedWindow", "FORWARD ID"))
        self.crossDetailsCheckBox.setStatusTip(_translate("AdvancedWindow", "Continue ConFindr analyses on samples with two or more\n"
"genera identified. Default is False.\n"
" "))
        self.crossDetailsCheckBox.setText(_translate("AdvancedWindow", "CROSS DETAILS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdvancedWindow = QtWidgets.QMainWindow()
    ui = Ui_AdvancedWindow()
    ui.setupUi(AdvancedWindow)
    AdvancedWindow.show()
    sys.exit(app.exec_())
