# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '欢迎.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(s, Form):
        Form.setObjectName("Form")
        Form.resize(569, 449)
        s.verticalLayoutWidget = QtWidgets.QWidget(Form)
        s.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 571, 451))
        s.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        s.verticalLayout = QtWidgets.QVBoxLayout(s.verticalLayoutWidget)
        s.verticalLayout.setContentsMargins(0, 0, 0, 0)
        s.verticalLayout.setObjectName("verticalLayout")
        s.label = QtWidgets.QLabel(s.verticalLayoutWidget)
        s.label.setAlignment(QtCore.Qt.AlignCenter)
        s.label.setObjectName("label")
        s.verticalLayout.addWidget(s.label)
        s.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        s.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        s.horizontalLayout_4.addItem(spacerItem)
        s.pushButton = QtWidgets.QPushButton(s.verticalLayoutWidget)
        s.pushButton.setObjectName("pushButton")
        s.horizontalLayout_4.addWidget(s.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        s.horizontalLayout_4.addItem(spacerItem1)
        s.verticalLayout.addLayout(s.horizontalLayout_4)

        s.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(s, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        s.label.setText(_translate("Form", "<h1>欢迎</h1>"))
        s.pushButton.setText(_translate("Form", "开始"))

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())