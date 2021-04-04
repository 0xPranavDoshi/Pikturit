from tkinter import *
import sys
from PIL import Image
import glob
import os

root = Tk()

aspect_ratio = 1
hasChanged = False
isFolder = False
image = None
images = []

width = StringVar(value="1")
height = StringVar(value="1")
isAspectRatio = IntVar(value=1)
pixels = IntVar()

widthEntry = Entry()
heightEntry = Entry()
checkbox = Checkbutton()

def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

def main():
    global aspect_ratio, checkbox, width, height, widthEntry, heightEntry, isFolder, image, images

    if len(sys.argv) == 2:
        ogwidth, ogheight = (0, 0)
        image_path = sys.argv[1]
        print(f"Image file is {image_path}")
        pathName = image_path.split('.')
        print(pathName)
        if len(pathName) == 1:
            print("It is a folder")
            isFolder = True
            pngImages = glob.glob(f"{image_path}/*.png")
            jpgImages = glob.glob(f"{image_path}/*.jpg")
            jpegImages = glob.glob(f"{image_path}/*.jpeg")
            bmpImages = glob.glob(f"{image_path}/*.bmp")
            images = pngImages + jpgImages + jpegImages + bmpImages
            print(images)
        else: 
            print("It is a file")
            isFolder = False
            image = Image.open(image_path)
            ogwidth, ogheight = image.size
            print(ogwidth, ogheight)         
            width = StringVar(value=ogwidth)
            height = StringVar(value=ogheight)
            aspect_ratio = ogwidth / ogheight

        root.title("Pikturit")
        root.resizable(False, False)

        vcmd = (root.register(callback))

        Label(root, text="By:").grid(row=0, column=0, pady=(7, 3))
        Radiobutton(root, text="Percentage", variable=pixels, value=1, command=lambda: changedRadio(ogwidth, ogheight)).grid(row=0, column=1)
        Radiobutton(root, text="Pixels", variable=pixels, value=0, command=lambda: changedRadio(ogwidth, ogheight)).grid(row=0, column=2)
        Label(root, text="Horizontal:").grid(row=1, column=0, pady=3)
        widthEntry = Entry(root, textvariable=width, validate='all', validatecommand=(vcmd, '%P'))
        widthEntry.grid(row=1, column=1)
        Label(root, text="Vertical:").grid(row=2, column=0, pady=3)
        heightEntry = Entry(root, textvariable=height, validate='all', validatecommand=(vcmd, '%P'))
        heightEntry.grid(row=2, column=1)   
        checkbox = Checkbutton(root, variable=isAspectRatio, command=aspectRatioChanged, text="Maintain aspect ratio").grid(row=3, column=0, pady=3)
        image_path = sys.argv[1]
        Button(root, text="Ok", command=lambda: accept(image, image_path, ogwidth, ogheight), width=10).grid(row=4, column=1,pady=(0, 10))
        Button(root, text="Cancel", command=reject, width=10).grid(row=4, column=2, pady=(0, 10), padx=(0, 10))

        width.trace("w", lambda name, index, mode, width=width: widthChanged(width))
        height.trace("w", lambda name, index, mode, height=height: heightChanged(height))

        root.mainloop()
    else:
        print('Usage pikturit.py <image_file_path>')

def accept(image, image_path, ogwidth, ogheight):
    if isFolder:
        image_path = image_path.split('\\')
        folderName = image_path.pop()
        newFolderName = folderName + "_pikturit"
        image_path.append(newFolderName)
        image_path = '\\'.join(image_path)
        print(f"New path for folder is {image_path}")
        os.mkdir(image_path)
        for path in images:
            print(f"New dimensions {width.get()}x{height.get()}")
            newSize = (int(width.get()), int(height.get()))
            file = Image.open(path)
            newImage = file.resize(newSize, Image.ANTIALIAS)
            print(f"Before splitting is {path}")
            path = path.split('\\')
            fileName = path.pop()
            name = fileName.split('.')
            end = name.pop()
            name = name[0]
            name = name + "_pikturit." + end
            print(f"Name is {name}")
            end = end.upper()
            if end == 'JPG':
                end = 'JPEG'
            path.append(name)
            path = '\\'.join(path)
            print(f"image_file is {path}")
            savePath = image_path + '\\' + fileName
            print(f"Saving image in path: {savePath}")
            newImage.save(savePath, end)
        sys.exit()
    else: 
        print("It is a file")         
        if pixels.get() == 0:
            _width = width.get()
            _height = height.get()
        else:
            _width = int(int(ogwidth) * (int(width.get()) / 100))
            _height = int(int(ogheight) * (int(height.get()) / 100))
        print(f"New dimensions {_width}x{_height}")
        newSize = (int(_width), int(_height))
        newImage = image.resize(newSize, Image.ANTIALIAS)
        print(f"Before splitting is {image_path}")
        image_path = image_path.split('\\')
        name = image_path.pop()
        name = name.split('.')
        end = name.pop()
        name = name[0]
        name = name + "_pikturit." + end
        print(f"Name is {name}")
        end = end.upper()
        if end == 'JPG':
            end = 'JPEG'
        image_path.append(name)
        image_path = '\\'.join(image_path)
        print(f"image_file is {image_path}")
        newImage.save(image_path, end)
        sys.exit()


def reject():
    print("Decline changes")
    sys.exit()

def widthChanged(newWidth):
    global hasChanged, height

    newWidth = newWidth.get()
    print("Width changed: ", newWidth)
    print("HasChanged is ", hasChanged)
    
    if isAspectRatio.get() == 1:
        if pixels.get() == 0:
            if hasChanged == False:
                if width.get() == '':
                    print("Width is blank")
                    hasChanged = True
                    height.set("0")    
                else:
                    print("Width is not blank")
                    hasChanged = True
                    newHeight = int(width.get()) / aspect_ratio
                    height.set(str(int(newHeight)))
            else: 
                hasChanged = False
        else:
            if hasChanged == False:
                if width.get() == '':
                    print("Width is blank")
                    hasChanged = True
                    height.set("0")
                else:
                    print("Width is not blank")
                    hasChanged = True
                    newHeight = int(width.get())
                    height.set(str(int(newHeight)))
            else: 
                hasChanged = False

def heightChanged(newHeight):
    global hasChanged, width

    newHeight = newHeight.get()
    print("Height changed: ", newHeight)
    print("HasChanged is ", hasChanged)
    if isAspectRatio.get() == 1:
        if pixels.get() == 0:
            if hasChanged == False:
                if height.get() == '':
                    print("Height is blank")
                    hasChanged = True
                    width.set("0")
                else:
                    print("Height is not blank")
                    hasChanged = True
                    newWidth = aspect_ratio * int(height.get())
                    width.set(str(int(newWidth)))
            else: 
                hasChanged = False
        else:
            if hasChanged == False:
                if height.get() == '':
                    hasChanged = True
                    width.set("0")
                else:
                    hasChanged = True
                    newWidth = int(height.get())
                    width.set(str(int(newWidth)))
            else: 
                hasChanged = False

def changedRadio(ogwidth, ogheight):
    type = pixels.get()
    print(f"Radio pixels is {type}")   
    if type == 0:
        print("Changing units to pixels: ", width.get())
        newWidth = int(int(ogwidth) * (int(width.get()) / 100))
        newHeight = int(int(ogheight) * (int(height.get()) / 100))
        widthEntry.delete(0, END)
        widthEntry.insert(END, newWidth)
        heightEntry.delete(0, END)
        heightEntry.insert(0, newHeight)
    else:
        print("Changing unit to percentage")
        newWidth = int((int(width.get()) / int(ogwidth))*100)
        newHeight = int((int(height.get()) / int(ogheight))*100)
        widthEntry.delete(0, END)
        widthEntry.insert(END, newWidth)
        heightEntry.delete(0, END)
        heightEntry.insert(0, newHeight)

def aspectRatioChanged():
    global isAspectRatio, aspect_ratio, pixels, width

    print("aspect ratio: ", aspect_ratio, "width: ", width.get(), "pixels: ", pixels.get())

    if isAspectRatio.get() == 1:
        print("Aspect ratio enabled")
        if pixels.get() == 0:
            if width.get() == '':
                heightEntry.delete(0, END)
                heightEntry.insert(END, 0)
            else:
                newHeight = int(width.get()) / aspect_ratio
                heightEntry.delete(0, END)
                heightEntry.insert(0, int(newHeight))
        else:
            if width.get() == '':
                heightEntry.delete(0, END)
                heightEntry.insert(END, 0)
            else:
                newHeight = int(width.get())
                heightEntry.delete(0, END)
                heightEntry.insert(0, int(newHeight))
    else:
        print("Aspect ratio disabled")

if __name__ == '__main__':
    main()


# class Ui_MainWindow(object):
#     width = 0
#     height = 0
#     aspect_ratio = 0
#     hasChanged = False
#     isAspectRatio = True
#     pixels = True

#     def setupUi(self, MainWindow, _width, _height, image, image_file):
#         self.width = _width
#         self.height = _height
#         self.aspect_ratio = _width / _height

#         MainWindow.setObjectName("Pikturit")
#         MainWindow.resize(350, 225)
#         sizePolicy = QtWidgets.QSizePolicy(
#             QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
#         sizePolicy.setHorizontalStretch(0)
#         sizePolicy.setVerticalStretch(0)
#         sizePolicy.setHeightForWidth(
#             MainWindow.sizePolicy().hasHeightForWidth())
#         MainWindow.setSizePolicy(sizePolicy)
#         MainWindow.setMinimumSize(QtCore.QSize(350, 225))
#         MainWindow.setMaximumSize(QtCore.QSize(350, 225))
#         MainWindow.setAutoFillBackground(False)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.grpBox = QtWidgets.QGroupBox(self.centralwidget)
#         self.grpBox.setGeometry(QtCore.QRect(15, 15, 295, 151))
#         self.grpBox.setObjectName("grpBox")
#         self.verticalLayoutWidget = QtWidgets.QWidget(self.grpBox)
#         self.verticalLayoutWidget.setGeometry(QtCore.QRect(14, 10, 275, 141))
#         self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
#         self.verticalLayout.setContentsMargins(9, 10, 10, 10)
#         self.verticalLayout.setSpacing(10)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.horizontalLayout.setContentsMargins(5, -1, 15, -1)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
#         self.label_3.setObjectName("label_3")
#         self.horizontalLayout.addWidget(self.label_3)
#         self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
#         self.radioButton.setEnabled(True)
#         self.radioButton.setChecked(False)
#         self.radioButton.setObjectName("radioButton")
#         self.radioButton.toggled.connect(
#             lambda: self.changedRadio(self.radioButton_2.isChecked(), _width, _height))
#         self.horizontalLayout.addWidget(self.radioButton)
#         self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
#         self.widget.setObjectName("widget")
#         self.horizontalLayout.addWidget(self.widget)
#         self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
#         self.radioButton_2.setChecked(True)
#         self.radioButton_2.setObjectName("radioButton_2")
#         self.horizontalLayout.addWidget(self.radioButton_2)
#         self.verticalLayout.addLayout(self.horizontalLayout)
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_2.setContentsMargins(5, -1, 10, -1)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
#         self.label.setObjectName("label")
#         self.horizontalLayout_2.addWidget(self.label)
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.lineEdit_2.setValidator(QtGui.QIntValidator(0, 100000000))
#         self.lineEdit_2.textChanged.connect(
#             lambda: self.changedWidth(self.lineEdit_2.text()))
#         self.horizontalLayout_2.addWidget(self.lineEdit_2)
#         self.verticalLayout.addLayout(self.horizontalLayout_2)
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_3.setContentsMargins(5, -1, 10, -1)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
#         self.label_2.setObjectName("label_2")
#         self.horizontalLayout_3.addWidget(self.label_2)
#         self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
#         self.lineEdit_3.setObjectName("lineEdit_3")
#         self.lineEdit_3.setValidator(QtGui.QIntValidator(0, 100000000))
#         self.lineEdit_3.textChanged.connect(
#             lambda: self.changedHeight(self.lineEdit_3.text()))
#         self.horizontalLayout_3.addWidget(self.lineEdit_3)
#         self.verticalLayout.addLayout(self.horizontalLayout_3)
#         self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
#         self.checkBox.setChecked(True)
#         self.checkBox.setObjectName("checkBox")
#         self.checkBox.stateChanged.connect(
#             lambda: self.aspectRatioChanged(self.checkBox.isChecked()))
#         self.verticalLayout.addWidget(self.checkBox)
#         self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
#         self.buttonBox.setGeometry(QtCore.QRect(147, 180, 156, 23))
#         self.buttonBox.setStandardButtons(
#             QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#         self.buttonBox.accepted.connect(
#             lambda: self.accept(self.width, self.height, image, image_file))
#         self.buttonBox.rejected.connect(self.reject)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow, _width, _height)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def accept(self, width, height, image, image_file):
#         print(f"New dimensions {width}x{height}")
#         newSize = (int(width), int(height))
#         newImage = image.resize(newSize, Image.ANTIALIAS)
#         print(f"Before splitting is {image_file}")
#         image_file = image_file.split('\\')
#         name = image_file.pop()
#         name = name.split('.')
#         end = name.pop()
#         name = name[0]
#         name = name + "_pikturit." + end
#         print(f"Name is {name}")
#         end = end.upper()
#         if end == 'JPG':
#             end = 'JPEG'
#         image_file.append(name)
#         image_file = '\\'.join(image_file)
#         print(f"image_file is {image_file}")
#         newImage.save(image_file, end)
#         sys.exit()

#     def reject(self):
#         print("Clicked cancel")
#         sys.exit()

#     def changedRadio(self, pixel, ogwidth, ogheight):
#         print(f"Radio pixels is {pixel}")
#         self.pixels = pixel
#         if pixel == True:
#             print("Changing units to pixels")
#             newWidth = int(int(ogwidth) * (int(self.width) / 100))
#             newHeight = int(int(ogheight) * (int(self.height) / 100))
#             self.hasChanged = True
#             self.lineEdit_2.setText(f"{newWidth}")
#             self.hasChanged = True
#             self.lineEdit_3.setText(f"{newHeight}")
#         else:
#             print("Changing unit to percentage")
#             newWidth = int((int(self.width) / int(ogwidth))*100)
#             newHeight = int((int(self.height) / int(ogheight))*100)
#             self.hasChanged = True
#             self.lineEdit_2.setText(f"{newWidth}")
#             self.hasChanged = True
#             self.lineEdit_3.setText(f"{newHeight}")

#     def aspectRatioChanged(self, isChecked):
#         print(f"Aspect ratio checked is {isChecked}")

#         if self.pixels == True:
#             if self.width == '':
#                 self.lineEdit_3.setText("0")
#             else:
#                 newHeight = int(self.width) / self.aspect_ratio
#                 self.lineEdit_3.setText(f"{int(newHeight)}")
#         else:
#             if self.width == '':
#                 self.lineEdit_3.setText("0")
#             else:
#                 newHeight = int(self.width)
#                 self.lineEdit_3.setText(f"{newHeight}")

#         self.isAspectRatio = isChecked

#     def changedWidth(self, width):
#         print(f"Width has changed: {width}")
#         print(f"Has changed is {self.hasChanged}")
#         self.width = width

#         if self.pixels == True:
#             if self.isAspectRatio == True:
#                 if self.hasChanged == False:
#                     if width == '':
#                         print("New height is 0")
#                         self.hasChanged = True
#                         self.lineEdit_3.setText("0")
#                     else:
#                         newHeight = int(width) / self.aspect_ratio
#                         print(f"new height is {int(newHeight)}")
#                         self.hasChanged = True
#                         self.lineEdit_3.setText(f"{int(newHeight)}")
#                 else:
#                     print("Changing hasChanged to False")
#                     self.hasChanged = False
#         else:
#             if self.isAspectRatio == True:
#                 if self.hasChanged == False:
#                     if width == '':
#                         print("New height is 0")
#                         self.hasChanged = True
#                         self.lineEdit_3.setText("0")
#                     else:
#                         newHeight = int(width)
#                         print(f"new height is {newHeight}")
#                         self.hasChanged = True
#                         self.lineEdit_3.setText(f"{newHeight}")
#                 else:
#                     print("Changing hasChanged to False")
#                     self.hasChanged = False

#     def changedHeight(self, height):
#         print(f"Height has changed: {height}")
#         print(f"Has changed is {self.hasChanged}")
#         self.height = height
#         if self.isAspectRatio == True:
#             if self.hasChanged == False:
#                 if height == '':
#                     print("New width is 0")
#                     self.hasChanged = True
#                     self.lineEdit_2.setText("0")
#                 else:
#                     newWidth = self.aspect_ratio * int(height)
#                     print(f"new width is {int(newWidth)}")
#                     self.hasChanged = True
#                     self.lineEdit_2.setText(f"{int(newWidth)}")
#             else:
#                 print("Changing hasChanged to False")
#                 self.hasChanged = False

#     def retranslateUi(self, MainWindow, width, height):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.grpBox.setTitle(_translate("MainWindow", "Resize"))
#         self.label_3.setText(_translate("MainWindow", "By:"))
#         self.radioButton.setText(_translate("MainWindow", "Percentage"))
#         self.radioButton_2.setText(_translate("MainWindow", "Pixels"))
#         self.label.setText(_translate("MainWindow", "Horizontal: "))
#         self.label_2.setText(_translate("MainWindow", "Vertical: "))
#         self.lineEdit_2.setText(_translate("MainWindow", f"{width}"))
#         self.lineEdit_3.setText(_translate("MainWindow", f"{height}"))
#         self.checkBox.setText(_translate(
#             "MainWindow", "Maintain aspect ratio"))

