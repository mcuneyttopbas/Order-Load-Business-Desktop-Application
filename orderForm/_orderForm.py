# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Asus\Desktop\order_load\orderForm\_orderForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 713)
        MainWindow.setMinimumSize(QtCore.QSize(713, 713))
        MainWindow.setMaximumSize(QtCore.QSize(713, 713))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 569, 281, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.txt_ship_adress = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ship_adress.sizePolicy().hasHeightForWidth())
        self.txt_ship_adress.setSizePolicy(sizePolicy)
        self.txt_ship_adress.setObjectName("txt_ship_adress")
        self.horizontalLayout_2.addWidget(self.txt_ship_adress)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 140, 281, 20))
        self.label_8.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 419, 281, 141))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.txt_ship_type = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txt_ship_type.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_ship_type.setObjectName("txt_ship_type")
        self.gridLayout_2.addWidget(self.txt_ship_type, 2, 1, 1, 1)
        self.txt_ship_tel = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txt_ship_tel.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_ship_tel.setObjectName("txt_ship_tel")
        self.gridLayout_2.addWidget(self.txt_ship_tel, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.txt_customer_code = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.txt_customer_code.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_customer_code.setObjectName("txt_customer_code")
        self.gridLayout_2.addWidget(self.txt_customer_code, 1, 1, 1, 1)
        self.cb_cargos = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.cb_cargos.setObjectName("cb_cargos")
        self.gridLayout_2.addWidget(self.cb_cargos, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 299, 281, 89))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.txt_cust_adress = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_cust_adress.sizePolicy().hasHeightForWidth())
        self.txt_cust_adress.setSizePolicy(sizePolicy)
        self.txt_cust_adress.setObjectName("txt_cust_adress")
        self.horizontalLayout.addWidget(self.txt_cust_adress)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 159, 281, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_receiver_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_receiver_name.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_receiver_name.setObjectName("txt_receiver_name")
        self.gridLayout.addWidget(self.txt_receiver_name, 0, 1, 1, 1)
        self.txt_gsm_tel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_gsm_tel.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_gsm_tel.setObjectName("txt_gsm_tel")
        self.gridLayout.addWidget(self.txt_gsm_tel, 3, 1, 1, 1)
        self.txt_cust_tel = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_cust_tel.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_cust_tel.setObjectName("txt_cust_tel")
        self.gridLayout.addWidget(self.txt_cust_tel, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.txt_author = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_author.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_author.setObjectName("txt_author")
        self.gridLayout.addWidget(self.txt_author, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 400, 281, 20))
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.table_details = QtWidgets.QTableWidget(self.centralwidget)
        self.table_details.setGeometry(QtCore.QRect(360, 60, 321, 541))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_details.sizePolicy().hasHeightForWidth())
        self.table_details.setSizePolicy(sizePolicy)
        self.table_details.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_details.setLineWidth(1)
        self.table_details.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_details.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_details.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_details.setProperty("showDropIndicator", True)
        self.table_details.setDragEnabled(False)
        self.table_details.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.table_details.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.table_details.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_details.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_details.setRowCount(2)
        self.table_details.setColumnCount(3)
        self.table_details.setObjectName("table_details")
        self.table_details.horizontalHeader().setCascadingSectionResizes(False)
        self.table_details.horizontalHeader().setDefaultSectionSize(100)
        self.table_details.horizontalHeader().setHighlightSections(False)
        self.table_details.verticalHeader().setDefaultSectionSize(30)
        self.table_details.verticalHeader().setSortIndicatorShown(False)
        self.table_details.verticalHeader().setStretchLastSection(False)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 49, 137, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_15.setObjectName("label_15")
        self.cb_customers = QtWidgets.QComboBox(self.centralwidget)
        self.cb_customers.setGeometry(QtCore.QRect(182, 50, 131, 31))
        self.cb_customers.setObjectName("cb_customers")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(40, 10, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_16.setObjectName("label_16")
        self.lbl_order_code = QtWidgets.QLabel(self.centralwidget)
        self.lbl_order_code.setGeometry(QtCore.QRect(150, 10, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_order_code.sizePolicy().hasHeightForWidth())
        self.lbl_order_code.setSizePolicy(sizePolicy)
        self.lbl_order_code.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_order_code.setText("")
        self.lbl_order_code.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_order_code.setObjectName("lbl_order_code")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(590, 610, 91, 41))
        self.btn_save.setObjectName("btn_save")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(360, 10, 151, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_18.setObjectName("label_18")
        self.lbl_date = QtWidgets.QLabel(self.centralwidget)
        self.lbl_date.setGeometry(QtCore.QRect(520, 10, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_date.sizePolicy().hasHeightForWidth())
        self.lbl_date.setSizePolicy(sizePolicy)
        self.lbl_date.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_date.setText("")
        self.lbl_date.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_date.setObjectName("lbl_date")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 90, 137, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_17.setObjectName("label_17")
        self.order_date = QtWidgets.QDateEdit(self.centralwidget)
        self.order_date.setGeometry(QtCore.QRect(180, 90, 131, 31))
        self.order_date.setAlignment(QtCore.Qt.AlignCenter)
        self.order_date.setDate(QtCore.QDate(2021, 1, 1))
        self.order_date.setObjectName("order_date")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(360, 610, 91, 41))
        self.btn_refresh.setObjectName("btn_refresh")
        self.check_close = QtWidgets.QCheckBox(self.centralwidget)
        self.check_close.setGeometry(QtCore.QRect(500, 740, 81, 20))
        self.check_close.setObjectName("check_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cb_customers, self.order_date)
        MainWindow.setTabOrder(self.order_date, self.txt_receiver_name)
        MainWindow.setTabOrder(self.txt_receiver_name, self.txt_author)
        MainWindow.setTabOrder(self.txt_author, self.txt_cust_tel)
        MainWindow.setTabOrder(self.txt_cust_tel, self.txt_gsm_tel)
        MainWindow.setTabOrder(self.txt_gsm_tel, self.txt_cust_adress)
        MainWindow.setTabOrder(self.txt_cust_adress, self.cb_cargos)
        MainWindow.setTabOrder(self.cb_cargos, self.txt_customer_code)
        MainWindow.setTabOrder(self.txt_customer_code, self.txt_ship_type)
        MainWindow.setTabOrder(self.txt_ship_type, self.txt_ship_tel)
        MainWindow.setTabOrder(self.txt_ship_tel, self.txt_ship_adress)
        MainWindow.setTabOrder(self.txt_ship_adress, self.table_details)
        MainWindow.setTabOrder(self.table_details, self.btn_refresh)
        MainWindow.setTabOrder(self.btn_refresh, self.btn_save)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sipariş Formu"))
        self.label_6.setText(_translate("MainWindow", "ADRES"))
        self.label_8.setText(_translate("MainWindow", "ALICI BİLGİLERİ"))
        self.label_13.setText(_translate("MainWindow", "MÜŞTERİ NO"))
        self.label_4.setText(_translate("MainWindow", "TAŞIMA TİPİ"))
        self.label_3.setText(_translate("MainWindow", "TEL NO."))
        self.label_14.setText(_translate("MainWindow", "NAKLİYE ADI"))
        self.label_5.setText(_translate("MainWindow", "ADRES"))
        self.label_2.setText(_translate("MainWindow", "GSM"))
        self.label.setText(_translate("MainWindow", "TEL NO."))
        self.label_12.setText(_translate("MainWindow", "YETKİLİ KİŞİ"))
        self.label_11.setText(_translate("MainWindow", "ALICI ADI"))
        self.label_7.setText(_translate("MainWindow", "TESLİMAT BİLGİLERİ"))
        self.label_15.setText(_translate("MainWindow", "FİRMA ADI"))
        self.label_16.setText(_translate("MainWindow", "SİPARİŞ NO."))
        self.btn_save.setText(_translate("MainWindow", "KAYDET"))
        self.label_18.setText(_translate("MainWindow", "DÜZENLENME TARİHİ"))
        self.label_17.setText(_translate("MainWindow", "SİPARİŞ TARİHİ"))
        self.btn_refresh.setText(_translate("MainWindow", "SIFIRLA"))
        self.check_close.setText(_translate("MainWindow", "CheckBox"))
