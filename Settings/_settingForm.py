# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Asus\Desktop\order_load\Settings\settingForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settingForm(object):
    def setupUi(self, settingForm):
        settingForm.setObjectName("settingForm")
        settingForm.resize(359, 328)
        self.stackedWidget = QtWidgets.QStackedWidget(settingForm)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 20, 301, 281))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_customer = QtWidgets.QWidget()
        self.page_customer.setObjectName("page_customer")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_customer)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 241, 206))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.txt_company = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txt_company.setObjectName("txt_company")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_company)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_mail1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txt_mail1.setObjectName("txt_mail1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_mail1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txt_mail3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txt_mail3.setObjectName("txt_mail3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txt_mail3)
        self.cb_extra_code = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_extra_code.setText("")
        self.cb_extra_code.setObjectName("cb_extra_code")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.cb_extra_code)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lbl = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl.setFont(font)
        self.lbl.setObjectName("lbl")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lbl)
        self.cb_notification = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cb_notification.setText("")
        self.cb_notification.setObjectName("cb_notification")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cb_notification)
        self.txt_mail2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.txt_mail2.setObjectName("txt_mail2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_mail2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.btn_save_customer = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_customer.setFont(font)
        self.btn_save_customer.setObjectName("btn_save_customer")
        self.verticalLayout_2.addWidget(self.btn_save_customer)
        self.stackedWidget.addWidget(self.page_customer)
        self.page_cargo = QtWidgets.QWidget()
        self.page_cargo.setObjectName("page_cargo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_cargo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 241, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.txt_cargo_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_cargo_name.setObjectName("txt_cargo_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_cargo_name)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txt_cargo_authority = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_cargo_authority.setObjectName("txt_cargo_authority")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_cargo_authority)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txt_cargo_phone = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_cargo_phone.setObjectName("txt_cargo_phone")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_cargo_phone)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.txt_cargo_adress = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.txt_cargo_adress.setObjectName("txt_cargo_adress")
        self.verticalLayout.addWidget(self.txt_cargo_adress)
        self.btn_save_cargo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_save_cargo.setFont(font)
        self.btn_save_cargo.setObjectName("btn_save_cargo")
        self.verticalLayout.addWidget(self.btn_save_cargo)
        self.stackedWidget.addWidget(self.page_cargo)

        self.retranslateUi(settingForm)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(settingForm)

    def retranslateUi(self, settingForm):
        _translate = QtCore.QCoreApplication.translate
        settingForm.setWindowTitle(_translate("settingForm", "Ayarlar"))
        self.label.setText(_translate("settingForm", "Firma Adı"))
        self.label_2.setText(_translate("settingForm", "Mail-1"))
        self.label_3.setText(_translate("settingForm", "Mail-2"))
        self.label_4.setText(_translate("settingForm", "Mail-3"))
        self.label_5.setText(_translate("settingForm", "Ek Sipariş Kodu"))
        self.lbl.setText(_translate("settingForm", "Bildirimler"))
        self.btn_save_customer.setText(_translate("settingForm", "Kaydet"))
        self.label_7.setText(_translate("settingForm", "Kargo Adı"))
        self.label_8.setText(_translate("settingForm", "Yekili Kişi"))
        self.label_9.setText(_translate("settingForm", "Telefon"))
        self.label_10.setText(_translate("settingForm", "Adres"))
        self.btn_save_cargo.setText(_translate("settingForm", "Kaydet"))