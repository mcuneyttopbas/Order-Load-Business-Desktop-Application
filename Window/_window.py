# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Asus\Desktop\order_load\Window\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 757)
        MainWindow.setMinimumSize(QtCore.QSize(1180, 757))
        MainWindow.setMaximumSize(QtCore.QSize(1180, 757))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grBox_newOrders = QtWidgets.QGroupBox(self.centralwidget)
        self.grBox_newOrders.setGeometry(QtCore.QRect(30, 10, 1131, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grBox_newOrders.setFont(font)
        self.grBox_newOrders.setObjectName("grBox_newOrders")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.grBox_newOrders)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 30, 1091, 171))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table_new_order = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_new_order.sizePolicy().hasHeightForWidth())
        self.table_new_order.setSizePolicy(sizePolicy)
        self.table_new_order.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_new_order.setAutoFillBackground(False)
        self.table_new_order.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_new_order.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_new_order.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.table_new_order.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.table_new_order.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_new_order.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_new_order.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_new_order.setShowGrid(True)
        self.table_new_order.setGridStyle(QtCore.Qt.SolidLine)
        self.table_new_order.setCornerButtonEnabled(True)
        self.table_new_order.setObjectName("table_new_order")
        self.table_new_order.setColumnCount(0)
        self.table_new_order.setRowCount(0)
        self.table_new_order.horizontalHeader().setVisible(True)
        self.table_new_order.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_2.addWidget(self.table_new_order)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_nw_prepare = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_nw_prepare.sizePolicy().hasHeightForWidth())
        self.btn_nw_prepare.setSizePolicy(sizePolicy)
        self.btn_nw_prepare.setObjectName("btn_nw_prepare")
        self.verticalLayout_2.addWidget(self.btn_nw_prepare)
        self.btn_nw_note = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_nw_note.setObjectName("btn_nw_note")
        self.verticalLayout_2.addWidget(self.btn_nw_note)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_nw_wait = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_nw_wait.setObjectName("btn_nw_wait")
        self.verticalLayout_2.addWidget(self.btn_nw_wait)
        self.btn_nw_remove = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_nw_remove.setObjectName("btn_nw_remove")
        self.verticalLayout_2.addWidget(self.btn_nw_remove)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.grBox_preparing = QtWidgets.QGroupBox(self.centralwidget)
        self.grBox_preparing.setGeometry(QtCore.QRect(30, 250, 551, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grBox_preparing.setFont(font)
        self.grBox_preparing.setObjectName("grBox_preparing")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.grBox_preparing)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 511, 171))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.table_preparing = QtWidgets.QTableWidget(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_preparing.sizePolicy().hasHeightForWidth())
        self.table_preparing.setSizePolicy(sizePolicy)
        self.table_preparing.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_preparing.setAutoFillBackground(False)
        self.table_preparing.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_preparing.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_preparing.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.table_preparing.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.table_preparing.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_preparing.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_preparing.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_preparing.setShowGrid(True)
        self.table_preparing.setGridStyle(QtCore.Qt.SolidLine)
        self.table_preparing.setCornerButtonEnabled(True)
        self.table_preparing.setObjectName("table_preparing")
        self.table_preparing.setColumnCount(0)
        self.table_preparing.setRowCount(0)
        self.table_preparing.horizontalHeader().setVisible(True)
        self.table_preparing.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_4.addWidget(self.table_preparing)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_pr_complete = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pr_complete.sizePolicy().hasHeightForWidth())
        self.btn_pr_complete.setSizePolicy(sizePolicy)
        self.btn_pr_complete.setObjectName("btn_pr_complete")
        self.verticalLayout_4.addWidget(self.btn_pr_complete)
        self.btn_pr_split = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_pr_split.setObjectName("btn_pr_split")
        self.verticalLayout_4.addWidget(self.btn_pr_split)
        self.btn_pr_wait = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_pr_wait.setObjectName("btn_pr_wait")
        self.verticalLayout_4.addWidget(self.btn_pr_wait)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.btn_pr_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.btn_pr_cancel.setObjectName("btn_pr_cancel")
        self.verticalLayout_4.addWidget(self.btn_pr_cancel)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.grBox_waiting = QtWidgets.QGroupBox(self.centralwidget)
        self.grBox_waiting.setGeometry(QtCore.QRect(610, 250, 551, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grBox_waiting.setFont(font)
        self.grBox_waiting.setObjectName("grBox_waiting")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.grBox_waiting)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 511, 171))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.table_waiting = QtWidgets.QTableWidget(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_waiting.sizePolicy().hasHeightForWidth())
        self.table_waiting.setSizePolicy(sizePolicy)
        self.table_waiting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_waiting.setAutoFillBackground(False)
        self.table_waiting.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_waiting.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_waiting.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.table_waiting.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.table_waiting.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_waiting.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_waiting.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_waiting.setShowGrid(True)
        self.table_waiting.setGridStyle(QtCore.Qt.SolidLine)
        self.table_waiting.setCornerButtonEnabled(True)
        self.table_waiting.setObjectName("table_waiting")
        self.table_waiting.setColumnCount(0)
        self.table_waiting.setRowCount(0)
        self.table_waiting.horizontalHeader().setVisible(True)
        self.table_waiting.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_5.addWidget(self.table_waiting)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_wt_prepare = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_wt_prepare.sizePolicy().hasHeightForWidth())
        self.btn_wt_prepare.setSizePolicy(sizePolicy)
        self.btn_wt_prepare.setObjectName("btn_wt_prepare")
        self.verticalLayout_5.addWidget(self.btn_wt_prepare)
        self.btn_wt_info = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_wt_info.setObjectName("btn_wt_info")
        self.verticalLayout_5.addWidget(self.btn_wt_info)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.btn_wt_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.btn_wt_cancel.setObjectName("btn_wt_cancel")
        self.verticalLayout_5.addWidget(self.btn_wt_cancel)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.grBox_ready = QtWidgets.QGroupBox(self.centralwidget)
        self.grBox_ready.setGeometry(QtCore.QRect(30, 480, 1131, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.grBox_ready.setFont(font)
        self.grBox_ready.setObjectName("grBox_ready")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.grBox_ready)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 30, 1101, 171))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.table_ready = QtWidgets.QTableWidget(self.horizontalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_ready.sizePolicy().hasHeightForWidth())
        self.table_ready.setSizePolicy(sizePolicy)
        self.table_ready.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_ready.setAutoFillBackground(False)
        self.table_ready.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_ready.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_ready.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.table_ready.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.table_ready.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_ready.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_ready.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_ready.setShowGrid(True)
        self.table_ready.setGridStyle(QtCore.Qt.SolidLine)
        self.table_ready.setCornerButtonEnabled(True)
        self.table_ready.setObjectName("table_ready")
        self.table_ready.setColumnCount(0)
        self.table_ready.setRowCount(0)
        self.table_ready.horizontalHeader().setVisible(True)
        self.table_ready.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout_6.addWidget(self.table_ready)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.btn_rdy_ship = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_rdy_ship.setObjectName("btn_rdy_ship")
        self.verticalLayout_6.addWidget(self.btn_rdy_ship)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.btn_rdy_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.btn_rdy_cancel.setObjectName("btn_rdy_cancel")
        self.verticalLayout_6.addWidget(self.btn_rdy_cancel)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(840, 710, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txt_lastUpdate = QtWidgets.QLabel(self.centralwidget)
        self.txt_lastUpdate.setGeometry(QtCore.QRect(1000, 710, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_lastUpdate.setFont(font)
        self.txt_lastUpdate.setText("")
        self.txt_lastUpdate.setObjectName("txt_lastUpdate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 710, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lbl_user = QtWidgets.QLabel(self.centralwidget)
        self.lbl_user.setGeometry(QtCore.QRect(140, 710, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_user.setFont(font)
        self.lbl_user.setText("")
        self.lbl_user.setObjectName("lbl_user")
        self.check_close = QtWidgets.QCheckBox(self.centralwidget)
        self.check_close.setGeometry(QtCore.QRect(280, 750, 98, 25))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.check_close.setFont(font)
        self.check_close.setObjectName("check_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 26))
        self.menubar.setObjectName("menubar")
        self.menu_main = QtWidgets.QMenu(self.menubar)
        self.menu_main.setObjectName("menu_main")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.action_order = QtWidgets.QAction(MainWindow)
        self.action_order.setObjectName("action_order")
        self.action_update = QtWidgets.QAction(MainWindow)
        self.action_update.setObjectName("action_update")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setObjectName("action_version")
        self.action_developer = QtWidgets.QAction(MainWindow)
        self.action_developer.setObjectName("action_developer")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_settings = QtWidgets.QAction(MainWindow)
        self.action_settings.setObjectName("action_settings")
        self.action_report = QtWidgets.QAction(MainWindow)
        self.action_report.setObjectName("action_report")
        self.menu_main.addAction(self.action_order)
        self.menu_main.addAction(self.action_update)
        self.menu_main.addAction(self.action_report)
        self.menu_main.addSeparator()
        self.menu_main.addAction(self.action_settings)
        self.menu_main.addAction(self.action_exit)
        self.menu_about.addAction(self.action_version)
        self.menu_about.addAction(self.action_developer)
        self.menubar.addAction(self.menu_main.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Order & Load Business Intelligence v1"))
        self.grBox_newOrders.setTitle(_translate("MainWindow", "YENİ SİPARİŞLER"))
        self.table_new_order.setSortingEnabled(False)
        self.btn_nw_prepare.setText(_translate("MainWindow", "Hazırla"))
        self.btn_nw_note.setText(_translate("MainWindow", "Not Ekle"))
        self.btn_nw_wait.setText(_translate("MainWindow", "Bekleyene Al"))
        self.btn_nw_remove.setText(_translate("MainWindow", "Sil"))
        self.grBox_preparing.setTitle(_translate("MainWindow", "HAZIRLANAN SİPARİŞLER"))
        self.table_preparing.setSortingEnabled(False)
        self.btn_pr_complete.setText(_translate("MainWindow", "Tamamla"))
        self.btn_pr_split.setText(_translate("MainWindow", "Parçala"))
        self.btn_pr_wait.setText(_translate("MainWindow", "Bekleyene Al"))
        self.btn_pr_cancel.setText(_translate("MainWindow", "İptal Et"))
        self.grBox_waiting.setTitle(_translate("MainWindow", "BEKLEYEN SİPARİŞLER"))
        self.table_waiting.setSortingEnabled(False)
        self.btn_wt_prepare.setText(_translate("MainWindow", "Hazırla"))
        self.btn_wt_info.setText(_translate("MainWindow", "Bilgi Ekle"))
        self.btn_wt_cancel.setText(_translate("MainWindow", "İptal Et"))
        self.grBox_ready.setTitle(_translate("MainWindow", "TAMAMLANAN SİPARİŞLER"))
        self.table_ready.setSortingEnabled(False)
        self.btn_rdy_ship.setText(_translate("MainWindow", "Sevk-Et"))
        self.btn_rdy_cancel.setText(_translate("MainWindow", "İptal Et"))
        self.label.setText(_translate("MainWindow", "SON GÜNCELLEME :"))
        self.label_2.setText(_translate("MainWindow", "KULLANICI :"))
        self.check_close.setText(_translate("MainWindow", "CheckBox"))
        self.menu_main.setTitle(_translate("MainWindow", "Menü"))
        self.menu_about.setTitle(_translate("MainWindow", "Hakkında"))
        self.action_order.setText(_translate("MainWindow", "Sipariş Ekle"))
        self.action_order.setToolTip(_translate("MainWindow", "Sipariş Ver "))
        self.action_order.setShortcut(_translate("MainWindow", "Shift+S"))
        self.action_update.setText(_translate("MainWindow", "Tabloları Güncelle "))
        self.action_update.setShortcut(_translate("MainWindow", "Shift+G"))
        self.action_version.setText(_translate("MainWindow", "Sürüm"))
        self.action_developer.setText(_translate("MainWindow", "Geliştirici"))
        self.action_exit.setText(_translate("MainWindow", "Çıkış"))
        self.action_settings.setText(_translate("MainWindow", "Ayarlar"))
        self.action_report.setText(_translate("MainWindow", "Rapora Gözat"))
        self.action_report.setShortcut(_translate("MainWindow", "Shift+R"))