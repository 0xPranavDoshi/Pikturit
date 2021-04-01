from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, uic
import sys
import subprocess
from PIL import Image
import math


def main():
    if len(sys.argv) == 2:
        image_file = sys.argv[1]
        print(f"Image file is {image_file}")
        image = Image.open(image_file)
        width, height = image.size
        print(width, height)

        # Do stuff

        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window, width, height, image, image_file)
        window.show()
        sys.exit(app.exec())
    else:
        print('Usage pikturit.py <image_file_path>')


class Ui_MainWindow(object):
    width = 0
    height = 0
    aspect_ratio = 0
    hasChanged = False
    isAspectRatio = True
    pixels = True

    def setupUi(self, MainWindow, _width, _height, image, image_file):
        self.width = _width
        self.height = _height
        self.aspect_ratio = _width / _height

        MainWindow.setObjectName("Pikturit")
        MainWindow.resize(350, 225)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 225))
        MainWindow.setMaximumSize(QtCore.QSize(350, 225))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.grpBox = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBox.setGeometry(QtCore.QRect(15, 15, 295, 151))
        self.grpBox.setObjectName("grpBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.grpBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 10, 275, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(9, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 15, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setEnabled(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(
            lambda: self.changedRadio(self.radioButton_2.isChecked(), _width, _height))
        self.horizontalLayout.addWidget(self.radioButton)
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, -1, 10, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(QtGui.QIntValidator(0, 100000000))
        self.lineEdit_2.textChanged.connect(
            lambda: self.changedWidth(self.lineEdit_2.text()))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(QtGui.QIntValidator(0, 100000000))
        self.lineEdit_3.textChanged.connect(
            lambda: self.changedHeight(self.lineEdit_3.text()))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(
            lambda: self.aspectRatioChanged(self.checkBox.isChecked()))
        self.verticalLayout.addWidget(self.checkBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(147, 180, 156, 23))
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(
            lambda: self.accept(self.width, self.height, image, image_file))
        self.buttonBox.rejected.connect(self.reject)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, _width, _height)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def accept(self, width, height, image, image_file):
        print(f"New dimensions {width}x{height}")
        newSize = (int(width), int(height))
        newImage = image.resize(newSize, Image.ANTIALIAS)
        print(f"Before splitting is {image_file}")
        image_file = image_file.split('\\')
        name = image_file.pop()
        name = name.split('.')
        end = name.pop()
        name = name[0]
        name = name + "_pikturit." + end
        print(f"Name is {name}")
        end = end.upper()
        if end == 'JPG':
            end = 'JPEG'
        image_file.append(name)
        image_file = '\\'.join(image_file)
        print(f"image_file is {image_file}")
        newImage.save(image_file, end)
        exit()

    def reject(self):
        print("Clicked cancel")
        exit()

    def changedRadio(self, pixel, ogwidth, ogheight):
        print(f"Radio pixels is {pixel}")
        self.pixels = pixel
        if pixel == True:
            print("Changing units to pixels")
            newWidth = int(int(ogwidth) * (int(self.width) / 100))
            newHeight = int(int(ogheight) * (int(self.height) / 100))
            self.hasChanged = True
            self.lineEdit_2.setText(f"{newWidth}")
            self.hasChanged = True
            self.lineEdit_3.setText(f"{newHeight}")
        else:
            print("Changing unit to percentage")
            newWidth = int((int(self.width) / int(ogwidth))*100)
            newHeight = int((int(self.height) / int(ogheight))*100)
            self.hasChanged = True
            self.lineEdit_2.setText(f"{newWidth}")
            self.hasChanged = True
            self.lineEdit_3.setText(f"{newHeight}")

    def aspectRatioChanged(self, isChecked):
        print(f"Aspect ratio checked is {isChecked}")

        if self.pixels == True:
            if self.width == '':
                self.lineEdit_3.setText("0")
            else:
                newHeight = int(self.width) / self.aspect_ratio
                self.lineEdit_3.setText(f"{int(newHeight)}")
        else:
            if self.width == '':
                self.lineEdit_3.setText("0")
            else:
                newHeight = int(self.width)
                self.lineEdit_3.setText(f"{newHeight}")

        self.isAspectRatio = isChecked

    def changedWidth(self, width):
        print(f"Width has changed: {width}")
        print(f"Has changed is {self.hasChanged}")
        self.width = width

        if self.pixels == True:
            if self.isAspectRatio == True:
                if self.hasChanged == False:
                    if width == '':
                        print("New height is 0")
                        self.hasChanged = True
                        self.lineEdit_3.setText("0")
                    else:
                        newHeight = int(width) / self.aspect_ratio
                        print(f"new height is {int(newHeight)}")
                        self.hasChanged = True
                        self.lineEdit_3.setText(f"{int(newHeight)}")
                else:
                    print("Changing hasChanged to False")
                    self.hasChanged = False
        else:
            if self.isAspectRatio == True:
                if self.hasChanged == False:
                    if width == '':
                        print("New height is 0")
                        self.hasChanged = True
                        self.lineEdit_3.setText("0")
                    else:
                        newHeight = int(width)
                        print(f"new height is {newHeight}")
                        self.hasChanged = True
                        self.lineEdit_3.setText(f"{newHeight}")
                else:
                    print("Changing hasChanged to False")
                    self.hasChanged = False

    def changedHeight(self, height):
        print(f"Height has changed: {height}")
        print(f"Has changed is {self.hasChanged}")
        self.height = height
        if self.isAspectRatio == True:
            if self.hasChanged == False:
                if height == '':
                    print("New width is 0")
                    self.hasChanged = True
                    self.lineEdit_2.setText("0")
                else:
                    newWidth = self.aspect_ratio * int(height)
                    print(f"new width is {int(newWidth)}")
                    self.hasChanged = True
                    self.lineEdit_2.setText(f"{int(newWidth)}")
            else:
                print("Changing hasChanged to False")
                self.hasChanged = False

    def retranslateUi(self, MainWindow, width, height):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grpBox.setTitle(_translate("MainWindow", "Resize"))
        self.label_3.setText(_translate("MainWindow", "By:"))
        self.radioButton.setText(_translate("MainWindow", "Percentage"))
        self.radioButton_2.setText(_translate("MainWindow", "Pixels"))
        self.label.setText(_translate("MainWindow", "Horizontal: "))
        self.label_2.setText(_translate("MainWindow", "Vertical: "))
        self.lineEdit_2.setText(_translate("MainWindow", f"{width}"))
        self.lineEdit_3.setText(_translate("MainWindow", f"{height}"))
        self.checkBox.setText(_translate(
            "MainWindow", "Maintain aspect ratio"))


if __name__ == '__main__':
    main()
