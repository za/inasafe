# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_dialog_base.ui'
#
# Created: Tue Oct 21 11:51:15 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OptionsDialogBase(object):
    def setupUi(self, OptionsDialogBase):
        OptionsDialogBase.setObjectName(_fromUtf8("OptionsDialogBase"))
        OptionsDialogBase.resize(699, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        OptionsDialogBase.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(OptionsDialogBase)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(OptionsDialogBase)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_basic = QtGui.QWidget()
        self.tab_basic.setObjectName(_fromUtf8("tab_basic"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_basic)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.tab_basic)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 677, 517))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cbxVisibleLayersOnly = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxVisibleLayersOnly.setObjectName(_fromUtf8("cbxVisibleLayersOnly"))
        self.gridLayout.addWidget(self.cbxVisibleLayersOnly, 0, 0, 1, 1)
        self.cbxSetLayerNameFromTitle = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxSetLayerNameFromTitle.setEnabled(True)
        self.cbxSetLayerNameFromTitle.setObjectName(_fromUtf8("cbxSetLayerNameFromTitle"))
        self.gridLayout.addWidget(self.cbxSetLayerNameFromTitle, 1, 0, 1, 1)
        self.cbxZoomToImpact = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxZoomToImpact.setEnabled(True)
        self.cbxZoomToImpact.setObjectName(_fromUtf8("cbxZoomToImpact"))
        self.gridLayout.addWidget(self.cbxZoomToImpact, 2, 0, 1, 1)
        self.cbxHideExposure = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxHideExposure.setEnabled(True)
        self.cbxHideExposure.setObjectName(_fromUtf8("cbxHideExposure"))
        self.gridLayout.addWidget(self.cbxHideExposure, 3, 0, 1, 1)
        self.cbxClipToViewport = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxClipToViewport.setChecked(False)
        self.cbxClipToViewport.setObjectName(_fromUtf8("cbxClipToViewport"))
        self.gridLayout.addWidget(self.cbxClipToViewport, 4, 0, 1, 1)
        self.cbxClipHard = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxClipHard.setObjectName(_fromUtf8("cbxClipHard"))
        self.gridLayout.addWidget(self.cbxClipHard, 5, 0, 1, 1)
        self.cbxShowPostprocessingLayers = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.cbxShowPostprocessingLayers.setObjectName(_fromUtf8("cbxShowPostprocessingLayers"))
        self.gridLayout.addWidget(self.cbxShowPostprocessingLayers, 6, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.dsbFemaleRatioDefault = QtGui.QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.dsbFemaleRatioDefault.setAccelerated(True)
        self.dsbFemaleRatioDefault.setMaximum(1.0)
        self.dsbFemaleRatioDefault.setSingleStep(0.01)
        self.dsbFemaleRatioDefault.setObjectName(_fromUtf8("dsbFemaleRatioDefault"))
        self.horizontalLayout.addWidget(self.dsbFemaleRatioDefault)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.grpNotImplemented = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.grpNotImplemented.setObjectName(_fromUtf8("grpNotImplemented"))
        self.gridLayout_3 = QtGui.QGridLayout(self.grpNotImplemented)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.grpNotImplemented)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.toolButton_4 = QtGui.QToolButton(self.grpNotImplemented)
        self.toolButton_4.setEnabled(True)
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.horizontalLayout_4.addWidget(self.toolButton_4)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.grpNotImplemented)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.cbxBubbleLayersUp = QtGui.QCheckBox(self.grpNotImplemented)
        self.cbxBubbleLayersUp.setEnabled(True)
        self.cbxBubbleLayersUp.setObjectName(_fromUtf8("cbxBubbleLayersUp"))
        self.gridLayout_3.addWidget(self.cbxBubbleLayersUp, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.grpNotImplemented)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.spinBox = QtGui.QSpinBox(self.grpNotImplemented)
        self.spinBox.setEnabled(True)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_5.addWidget(self.spinBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.grpNotImplemented)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.toolButton = QtGui.QToolButton(self.grpNotImplemented)
        self.toolButton.setEnabled(True)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.grpNotImplemented)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.cbxUseThread = QtGui.QCheckBox(self.grpNotImplemented)
        self.cbxUseThread.setObjectName(_fromUtf8("cbxUseThread"))
        self.gridLayout_3.addWidget(self.cbxUseThread, 10, 0, 1, 1)
        self.gridLayout.addWidget(self.grpNotImplemented, 8, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_basic, _fromUtf8(""))
        self.tab_templates = QtGui.QWidget()
        self.tab_templates.setObjectName(_fromUtf8("tab_templates"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_templates)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.template_warning_checkbox = QtGui.QCheckBox(self.tab_templates)
        self.template_warning_checkbox.setChecked(True)
        self.template_warning_checkbox.setObjectName(_fromUtf8("template_warning_checkbox"))
        self.verticalLayout_2.addWidget(self.template_warning_checkbox)
        self.custom_org_logo_checkbox = QtGui.QCheckBox(self.tab_templates)
        self.custom_org_logo_checkbox.setObjectName(_fromUtf8("custom_org_logo_checkbox"))
        self.verticalLayout_2.addWidget(self.custom_org_logo_checkbox)
        self.splitter_org_logo = QtGui.QSplitter(self.tab_templates)
        self.splitter_org_logo.setEnabled(False)
        self.splitter_org_logo.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_org_logo.setObjectName(_fromUtf8("splitter_org_logo"))
        self.leOrganisationLogoPath = QtGui.QLineEdit(self.splitter_org_logo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leOrganisationLogoPath.sizePolicy().hasHeightForWidth())
        self.leOrganisationLogoPath.setSizePolicy(sizePolicy)
        self.leOrganisationLogoPath.setObjectName(_fromUtf8("leOrganisationLogoPath"))
        self.toolOrganisationLogoPath = QtGui.QToolButton(self.splitter_org_logo)
        self.toolOrganisationLogoPath.setObjectName(_fromUtf8("toolOrganisationLogoPath"))
        self.verticalLayout_2.addWidget(self.splitter_org_logo)
        self.organisation_on_dock_checkbox = QtGui.QCheckBox(self.tab_templates)
        self.organisation_on_dock_checkbox.setChecked(True)
        self.organisation_on_dock_checkbox.setObjectName(_fromUtf8("organisation_on_dock_checkbox"))
        self.verticalLayout_2.addWidget(self.organisation_on_dock_checkbox)
        self.custom_north_arrow_checkbox = QtGui.QCheckBox(self.tab_templates)
        self.custom_north_arrow_checkbox.setChecked(False)
        self.custom_north_arrow_checkbox.setObjectName(_fromUtf8("custom_north_arrow_checkbox"))
        self.verticalLayout_2.addWidget(self.custom_north_arrow_checkbox)
        self.splitter_north_arrow = QtGui.QSplitter(self.tab_templates)
        self.splitter_north_arrow.setEnabled(False)
        self.splitter_north_arrow.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_north_arrow.setObjectName(_fromUtf8("splitter_north_arrow"))
        self.leNorthArrowPath = QtGui.QLineEdit(self.splitter_north_arrow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leNorthArrowPath.sizePolicy().hasHeightForWidth())
        self.leNorthArrowPath.setSizePolicy(sizePolicy)
        self.leNorthArrowPath.setObjectName(_fromUtf8("leNorthArrowPath"))
        self.toolNorthArrowPath = QtGui.QToolButton(self.splitter_north_arrow)
        self.toolNorthArrowPath.setObjectName(_fromUtf8("toolNorthArrowPath"))
        self.verticalLayout_2.addWidget(self.splitter_north_arrow)
        self.custom_templates_dir_checkbox = QtGui.QCheckBox(self.tab_templates)
        self.custom_templates_dir_checkbox.setChecked(False)
        self.custom_templates_dir_checkbox.setObjectName(_fromUtf8("custom_templates_dir_checkbox"))
        self.verticalLayout_2.addWidget(self.custom_templates_dir_checkbox)
        self.splitter_custom_report = QtGui.QSplitter(self.tab_templates)
        self.splitter_custom_report.setEnabled(False)
        self.splitter_custom_report.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_custom_report.setObjectName(_fromUtf8("splitter_custom_report"))
        self.leReportTemplatePath = QtGui.QLineEdit(self.splitter_custom_report)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leReportTemplatePath.sizePolicy().hasHeightForWidth())
        self.leReportTemplatePath.setSizePolicy(sizePolicy)
        self.leReportTemplatePath.setObjectName(_fromUtf8("leReportTemplatePath"))
        self.toolReportTemplatePath = QtGui.QToolButton(self.splitter_custom_report)
        self.toolReportTemplatePath.setObjectName(_fromUtf8("toolReportTemplatePath"))
        self.verticalLayout_2.addWidget(self.splitter_custom_report)
        self.custom_org_disclaimer_checkbox = QtGui.QCheckBox(self.tab_templates)
        self.custom_org_disclaimer_checkbox.setChecked(False)
        self.custom_org_disclaimer_checkbox.setObjectName(_fromUtf8("custom_org_disclaimer_checkbox"))
        self.verticalLayout_2.addWidget(self.custom_org_disclaimer_checkbox)
        self.txtDisclaimer = QtGui.QPlainTextEdit(self.tab_templates)
        self.txtDisclaimer.setEnabled(False)
        self.txtDisclaimer.setObjectName(_fromUtf8("txtDisclaimer"))
        self.verticalLayout_2.addWidget(self.txtDisclaimer)
        self.tabWidget.addTab(self.tab_templates, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.import_button = QtGui.QPushButton(self.tab)
        self.import_button.setObjectName(_fromUtf8("import_button"))
        self.gridLayout_2.addWidget(self.import_button, 0, 0, 1, 1)
        self.export_button = QtGui.QPushButton(self.tab)
        self.export_button.setObjectName(_fromUtf8("export_button"))
        self.gridLayout_2.addWidget(self.export_button, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.remove_button = QtGui.QToolButton(self.tab)
        self.remove_button.setObjectName(_fromUtf8("remove_button"))
        self.gridLayout_2.addWidget(self.remove_button, 0, 3, 1, 1)
        self.add_button = QtGui.QToolButton(self.tab)
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.gridLayout_2.addWidget(self.add_button, 0, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.minimum_needs_table = QtGui.QTableWidget(self.tab)
        self.minimum_needs_table.setObjectName(_fromUtf8("minimum_needs_table"))
        self.minimum_needs_table.setColumnCount(0)
        self.minimum_needs_table.setRowCount(0)
        self.gridLayout_5.addWidget(self.minimum_needs_table, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_advanced = QtGui.QWidget()
        self.tab_advanced.setObjectName(_fromUtf8("tab_advanced"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_advanced)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.lblKeywordCache = QtGui.QLabel(self.tab_advanced)
        self.lblKeywordCache.setEnabled(True)
        self.lblKeywordCache.setObjectName(_fromUtf8("lblKeywordCache"))
        self.gridLayout_6.addWidget(self.lblKeywordCache, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.leKeywordCachePath = QtGui.QLineEdit(self.tab_advanced)
        self.leKeywordCachePath.setEnabled(True)
        self.leKeywordCachePath.setObjectName(_fromUtf8("leKeywordCachePath"))
        self.horizontalLayout_6.addWidget(self.leKeywordCachePath)
        self.toolKeywordCachePath = QtGui.QToolButton(self.tab_advanced)
        self.toolKeywordCachePath.setEnabled(True)
        self.toolKeywordCachePath.setObjectName(_fromUtf8("toolKeywordCachePath"))
        self.horizontalLayout_6.addWidget(self.toolKeywordCachePath)
        self.gridLayout_6.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.cbxUseSentry = QtGui.QCheckBox(self.tab_advanced)
        self.cbxUseSentry.setObjectName(_fromUtf8("cbxUseSentry"))
        self.gridLayout_6.addWidget(self.cbxUseSentry, 2, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.tab_advanced)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_6.addWidget(self.textBrowser, 3, 0, 1, 1)
        self.cbxDevMode = QtGui.QCheckBox(self.tab_advanced)
        self.cbxDevMode.setObjectName(_fromUtf8("cbxDevMode"))
        self.gridLayout_6.addWidget(self.cbxDevMode, 4, 0, 1, 1)
        self.cbxNativeZonalStats = QtGui.QCheckBox(self.tab_advanced)
        self.cbxNativeZonalStats.setObjectName(_fromUtf8("cbxNativeZonalStats"))
        self.gridLayout_6.addWidget(self.cbxNativeZonalStats, 5, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 6, 0, 1, 1)
        self.tabWidget.addTab(self.tab_advanced, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(OptionsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OptionsDialogBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), OptionsDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), OptionsDialogBase.reject)
        QtCore.QObject.connect(self.custom_org_disclaimer_checkbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.txtDisclaimer.setEnabled)
        QtCore.QObject.connect(self.custom_org_logo_checkbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.splitter_org_logo.setEnabled)
        QtCore.QObject.connect(self.custom_north_arrow_checkbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.splitter_north_arrow.setEnabled)
        QtCore.QObject.connect(self.custom_templates_dir_checkbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.splitter_custom_report.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialogBase)
        OptionsDialogBase.setTabOrder(self.lineEdit_4, self.cbxVisibleLayersOnly)
        OptionsDialogBase.setTabOrder(self.cbxVisibleLayersOnly, self.cbxSetLayerNameFromTitle)
        OptionsDialogBase.setTabOrder(self.cbxSetLayerNameFromTitle, self.cbxZoomToImpact)
        OptionsDialogBase.setTabOrder(self.cbxZoomToImpact, self.cbxHideExposure)
        OptionsDialogBase.setTabOrder(self.cbxHideExposure, self.cbxClipToViewport)
        OptionsDialogBase.setTabOrder(self.cbxClipToViewport, self.cbxClipHard)
        OptionsDialogBase.setTabOrder(self.cbxClipHard, self.cbxShowPostprocessingLayers)
        OptionsDialogBase.setTabOrder(self.cbxShowPostprocessingLayers, self.dsbFemaleRatioDefault)
        OptionsDialogBase.setTabOrder(self.dsbFemaleRatioDefault, self.cbxBubbleLayersUp)
        OptionsDialogBase.setTabOrder(self.cbxBubbleLayersUp, self.organisation_on_dock_checkbox)
        OptionsDialogBase.setTabOrder(self.organisation_on_dock_checkbox, self.txtDisclaimer)
        OptionsDialogBase.setTabOrder(self.txtDisclaimer, self.leKeywordCachePath)
        OptionsDialogBase.setTabOrder(self.leKeywordCachePath, self.toolKeywordCachePath)
        OptionsDialogBase.setTabOrder(self.toolKeywordCachePath, self.cbxUseSentry)
        OptionsDialogBase.setTabOrder(self.cbxUseSentry, self.textBrowser)
        OptionsDialogBase.setTabOrder(self.textBrowser, self.cbxDevMode)
        OptionsDialogBase.setTabOrder(self.cbxDevMode, self.cbxNativeZonalStats)
        OptionsDialogBase.setTabOrder(self.cbxNativeZonalStats, self.cbxUseThread)
        OptionsDialogBase.setTabOrder(self.cbxUseThread, self.toolButton)
        OptionsDialogBase.setTabOrder(self.toolButton, self.toolButton_4)
        OptionsDialogBase.setTabOrder(self.toolButton_4, self.scrollArea)
        OptionsDialogBase.setTabOrder(self.scrollArea, self.spinBox)
        OptionsDialogBase.setTabOrder(self.spinBox, self.lineEdit)

    def retranslateUi(self, OptionsDialogBase):
        OptionsDialogBase.setWindowTitle(_translate("OptionsDialogBase", "InaSAFE - Options", None))
        self.cbxVisibleLayersOnly.setText(_translate("OptionsDialogBase", "Only show visible layers in InaSAFE dock", None))
        self.cbxSetLayerNameFromTitle.setText(_translate("OptionsDialogBase", "Set QGIS layer name from \'title\' in keywords", None))
        self.cbxZoomToImpact.setText(_translate("OptionsDialogBase", "Zoom to impact layer on scenario estimate completion", None))
        self.cbxHideExposure.setText(_translate("OptionsDialogBase", "Hide exposure layer on scenario estimate completion", None))
        self.cbxClipToViewport.setToolTip(_translate("OptionsDialogBase", "Turn on to clip hazard and exposure layers to the currently  visible extent on the map canvas", None))
        self.cbxClipToViewport.setText(_translate("OptionsDialogBase", "Clip datasets to visible extent before analysis", None))
        self.cbxClipHard.setText(_translate("OptionsDialogBase", "When clipping, also clip features (i.e. will clip polygon smaller)", None))
        self.cbxShowPostprocessingLayers.setToolTip(_translate("OptionsDialogBase", "Turn on to see the intermediate files generated by the postprocessing steps in the map canvas", None))
        self.cbxShowPostprocessingLayers.setText(_translate("OptionsDialogBase", "Show intermediate layers generated by postprocessing", None))
        self.label_6.setText(_translate("OptionsDialogBase", "Female ratio default value", None))
        self.grpNotImplemented.setTitle(_translate("OptionsDialogBase", "Not yet implemented", None))
        self.toolButton_4.setText(_translate("OptionsDialogBase", "...", None))
        self.label_4.setText(_translate("OptionsDialogBase", "Organisation name (for maps, reports etc.)", None))
        self.cbxBubbleLayersUp.setText(_translate("OptionsDialogBase", "Bubble exposure and hazard layers to top when selected", None))
        self.label_5.setText(_translate("OptionsDialogBase", "DPI (Maps and reports)", None))
        self.toolButton.setText(_translate("OptionsDialogBase", "...", None))
        self.label.setText(_translate("OptionsDialogBase", "Location for results", None))
        self.cbxUseThread.setText(_translate("OptionsDialogBase", "Run analysis in a separate thread (experimental)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_basic), _translate("OptionsDialogBase", "Basic Options", None))
        self.template_warning_checkbox.setText(_translate("OptionsDialogBase", "Prompt me in cases when a template has missing elements", None))
        self.custom_org_logo_checkbox.setText(_translate("OptionsDialogBase", "Use custom organisation logo", None))
        self.toolOrganisationLogoPath.setText(_translate("OptionsDialogBase", "...", None))
        self.organisation_on_dock_checkbox.setText(_translate("OptionsDialogBase", "Show organisation logo on main panel too", None))
        self.custom_north_arrow_checkbox.setText(_translate("OptionsDialogBase", "Use custom north arrow image", None))
        self.toolNorthArrowPath.setText(_translate("OptionsDialogBase", "...", None))
        self.custom_templates_dir_checkbox.setText(_translate("OptionsDialogBase", "Additional report templates directory", None))
        self.toolReportTemplatePath.setText(_translate("OptionsDialogBase", "...", None))
        self.custom_org_disclaimer_checkbox.setText(_translate("OptionsDialogBase", "Use custom organisation disclaimer text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_templates), _translate("OptionsDialogBase", "Template Options", None))
        self.import_button.setText(_translate("OptionsDialogBase", "Import ...", None))
        self.export_button.setText(_translate("OptionsDialogBase", "Export ...", None))
        self.remove_button.setText(_translate("OptionsDialogBase", "-", None))
        self.add_button.setText(_translate("OptionsDialogBase", "+", None))
        self.label_2.setText(_translate("OptionsDialogBase", "Note: Changes only take effect after closing and reopening QGIS.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("OptionsDialogBase", "Minimum Needs", None))
        self.lblKeywordCache.setText(_translate("OptionsDialogBase", "Keyword cache for remote datasources", None))
        self.toolKeywordCachePath.setText(_translate("OptionsDialogBase", "...", None))
        self.cbxUseSentry.setText(_translate("OptionsDialogBase", "Help to improve InaSAFE by submitting errors to a remote server", None))
        self.textBrowser.setHtml(_translate("OptionsDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:12pt; font-weight:600; color:#f50000;\">Note:</span><span style=\" font-family:\'Cantarell\'; font-size:12pt;\"> The above setting requires a QGIS restart to disable / enable. Error messages and diagnostic information will be posted to http://sentry.linfiniti.com/inasafe-desktop/. Some institutions may not allow you to enable this feature - check with your network administrator if unsure. Although the data is submitted anonymously, the information contained in tracebacks may contain file system paths which reveal your identity or other information from your system.</span></p></body></html>", None))
        self.cbxDevMode.setText(_translate("OptionsDialogBase", "Enable developer mode for dock webkit (needs restart)", None))
        self.cbxNativeZonalStats.setText(_translate("OptionsDialogBase", "Use QGIS zonal statistics (leave unchecked to use InaSAFE\'s zonal statistics)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_advanced), _translate("OptionsDialogBase", "Advanced", None))

import resources_rc
