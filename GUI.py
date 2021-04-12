import funciones_final
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Reconocimiento Facial")
        MainWindow.resize(506, 556)
        MainWindow.setMinimumSize(QtCore.QSize(506, 556))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ia.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)    
        MainWindow.setStyleSheet("QMainWindow {background-color:rgb(4,59,90)}")
        MainWindow.setWindowOpacity(0.93)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 110, 491, 421))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 70, 491, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.listWidget.setStyleSheet("QListWidget{color:white;background-color:rgb(1,1,1);font-size: 14px;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
        )
        
        self.pushButton.setStyleSheet("QPushButton {background:blue;padding: 2px;text-align:center;background-color: rgb(38,176,150);font-size: 10pt;color:white;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
            "QPushButton:hover {background-color:rgb(0, 255, 212);font-size: 10pt;font-weight: bold;color:white}"
            "QPushButton:pressed {background-color:black;font-size: 10pt;font-weight: bold;color:white}"
            )
        self.pushButton_2.setStyleSheet("QPushButton {background:blue;padding: 2px;text-align:center;background-color: rgb(38,176,150);font-size: 10pt;color:white;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
            "QPushButton:hover {background-color:rgb(0, 255, 212);font-size: 10pt;font-weight: bold;color:white}"
            "QPushButton:pressed {background-color:black;font-size: 10pt;font-weight: bold;color:white}"
            )
        self.pushButton_3.setStyleSheet("QPushButton {background:blue;padding: 2px;text-align:center;background-color: rgb(38,176,150);font-size: 10pt;color:white;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
            "QPushButton:hover {background-color:rgb(0, 255, 212);font-size: 10pt;font-weight: bold;color:white}"
            "QPushButton:pressed {background-color:black;font-size: 10pt;font-weight: bold;color:white}"
            )
        self.pushButton_4.setStyleSheet("QPushButton {background:blue;padding: 2px;text-align:center;background-color: rgb(38,176,150);font-size: 10pt;color:white;font-weight: bold;border-style: outset;border-width: .5px;border-radius: 4px;border-color: black;}"
            "QPushButton:hover {background-color:rgb(0, 255, 212);font-size: 10pt;font-weight: bold;color:white}"
            "QPushButton:pressed {background-color:black;font-size: 10pt;font-weight: bold;color:white}"
            )
        self.label.setStyleSheet("QLabel{color:white}")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.entrenar)        
        self.pushButton_2.clicked.connect(self.listar)
        self.pushButton_4.clicked.connect(self.video_)        
        self.pushButton_3.clicked.connect(self.imagen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema ReconocimientoFacial"))
        self.pushButton.setText(_translate("MainWindow", "Agregar persona"))
        self.pushButton_2.setText(_translate("MainWindow", "Personas registradas"))
        self.pushButton_4.setText(_translate("MainWindow", "Reconocimiento en Video"))
        self.pushButton_3.setText(_translate("MainWindow", "Reconocimiento en Imagen"))
        self.label.setText(_translate("MainWindow", "Sistema de Reconocimiento Facial"))
    
    def entrenar(self):
        funciones_final.model_creator()
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Entrenmiento completado')
        mb.setText('Se han agregado a todas las personas en la base de datos: ')
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_() 
    
    def listar(self):
        nombres=funciones_final.print_names()        
        for x in range (len(nombres)):
            self.listWidget.addItem(str(x+1)+") "+nombres[x])
    
    def video_(self):
        try:
            funciones_final.detfvid(0)
        except e:
            print("rayos")
    
    def imagen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog        
        fileName, _ = QFileDialog.getOpenFileName(None,"Buscar Imagen", "","Imagenes (*.jpg *.png *.jpeg)",options=options)
        if fileName:
            funciones_final.image(fileName)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
