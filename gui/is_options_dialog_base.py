# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'is_options_dialog_base.ui'
#
# Created: Wed Mar 28 17:03:54 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ISOptionsDialogBase(object):
    def setupUi(self, ISOptionsDialogBase):
        ISOptionsDialogBase.setObjectName(_fromUtf8("ISOptionsDialogBase"))
        ISOptionsDialogBase.resize(507, 478)
        ISOptionsDialogBase.setWindowTitle(QtGui.QApplication.translate("ISOptionsDialogBase", "InaSAFE - Options", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ISOptionsDialogBase.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(ISOptionsDialogBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(ISOptionsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(ISOptionsDialogBase)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 487, 425))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbxSetLayerNameFromTitle = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxSetLayerNameFromTitle.setEnabled(True)
        self.cbxSetLayerNameFromTitle.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Set QGIS layer name from \'title\' in keywords", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSetLayerNameFromTitle.setObjectName(_fromUtf8("cbxSetLayerNameFromTitle"))
        self.gridLayout_2.addWidget(self.cbxSetLayerNameFromTitle, 2, 0, 1, 1)
        self.checkBox_3 = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Bubble exposure and hazard layers to top when selected", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout_2.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setEnabled(False)
        self.label.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Location for results", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setEnabled(False)
        self.label_2.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Report template", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_2 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.toolButton_2 = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_2.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.horizontalLayout.addWidget(self.toolButton_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setEnabled(False)
        self.label_3.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Logo for maps (must be x x y) ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 8, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.toolButton_3 = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_3.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.horizontalLayout_3.addWidget(self.toolButton_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 9, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setEnabled(False)
        self.label_4.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Organisation name (for maps, reports etc.)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 10, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.toolButton_4 = QtGui.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_4.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout_4.addWidget(self.toolButton_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 11, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setEnabled(False)
        self.label_5.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "DPI (Maps and reports)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox = QtGui.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setEnabled(False)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 12, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 14, 0, 1, 1)
        self.cbxVisibleLayersOnly = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxVisibleLayersOnly.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Only show visible layers in InaSAFE dock", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxVisibleLayersOnly.setObjectName(_fromUtf8("cbxVisibleLayersOnly"))
        self.gridLayout_2.addWidget(self.cbxVisibleLayersOnly, 1, 0, 1, 1)
        self.cbxUseThread = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxUseThread.setText(QtGui.QApplication.translate("ISOptionsDialogBase", "Run analysis in a separate thread (experimental)", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxUseThread.setObjectName(_fromUtf8("cbxUseThread"))
        self.gridLayout_2.addWidget(self.cbxUseThread, 13, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(ISOptionsDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ISOptionsDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ISOptionsDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ISOptionsDialogBase)
        ISOptionsDialogBase.setTabOrder(self.cbxVisibleLayersOnly, self.cbxSetLayerNameFromTitle)
        ISOptionsDialogBase.setTabOrder(self.cbxSetLayerNameFromTitle, self.checkBox_3)
        ISOptionsDialogBase.setTabOrder(self.checkBox_3, self.lineEdit)
        ISOptionsDialogBase.setTabOrder(self.lineEdit, self.toolButton)
        ISOptionsDialogBase.setTabOrder(self.toolButton, self.lineEdit_2)
        ISOptionsDialogBase.setTabOrder(self.lineEdit_2, self.toolButton_2)
        ISOptionsDialogBase.setTabOrder(self.toolButton_2, self.lineEdit_3)
        ISOptionsDialogBase.setTabOrder(self.lineEdit_3, self.toolButton_3)
        ISOptionsDialogBase.setTabOrder(self.toolButton_3, self.lineEdit_4)
        ISOptionsDialogBase.setTabOrder(self.lineEdit_4, self.toolButton_4)
        ISOptionsDialogBase.setTabOrder(self.toolButton_4, self.spinBox)
        ISOptionsDialogBase.setTabOrder(self.spinBox, self.cbxUseThread)
        ISOptionsDialogBase.setTabOrder(self.cbxUseThread, self.buttonBox)
        ISOptionsDialogBase.setTabOrder(self.buttonBox, self.scrollArea)

    def retranslateUi(self, ISOptionsDialogBase):
        pass

import resources_rc
