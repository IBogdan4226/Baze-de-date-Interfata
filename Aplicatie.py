from PyQt5 import QtCore, QtGui, QtWidgets

from threading import Thread
import cx_Oracle


con = cx_Oracle.connect("bd027", "bd027", "bd-dc.cs.tuiasi.ro:1539/orcl")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 593)
        MainWindow.setMinimumSize(QtCore.QSize(569, 593))
        MainWindow.setMaximumSize(QtCore.QSize(569, 593))
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(-140, -60, 1661, 991))
        self.MainFrame.setMinimumSize(QtCore.QSize(1661, 0))
        self.MainFrame.setMaximumSize(QtCore.QSize(1661, 16777215))
        self.MainFrame.setStyleSheet("background-color: rgb(216, 230, 242);")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.MainFrame)
        self.stackedWidget.setGeometry(QtCore.QRect(-40, 0, 1561, 1001))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_PersoaneShow = QtWidgets.QWidget()
        self.page_PersoaneShow.setObjectName("page_PersoaneShow")
        self.tablePersoane = QtWidgets.QTableWidget(self.page_PersoaneShow)
        self.tablePersoane.setGeometry(QtCore.QRect(200, 70, 531, 341))
        self.tablePersoane.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tablePersoane.setRowCount(0)
        self.tablePersoane.setObjectName("tablePersoane")
        self.tablePersoane.setColumnCount(3)
        self.tablePersoane.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tablePersoane.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePersoane.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablePersoane.setHorizontalHeaderItem(2, item)
        self.tablePersoane.horizontalHeader().setDefaultSectionSize(168)
        self.PersinsertNume = QtWidgets.QTextEdit(self.page_PersoaneShow)
        self.PersinsertNume.setGeometry(QtCore.QRect(200, 450, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PersinsertNume.setFont(font)
        self.PersinsertNume.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PersinsertNume.setObjectName("PersinsertNume")
        self.PersAddButton = QtWidgets.QPushButton(self.page_PersoaneShow)
        self.PersAddButton.setGeometry(QtCore.QRect(650, 450, 81, 31))
        self.PersAddButton.setObjectName("PersAddButton")
        self.PersDeleteButton = QtWidgets.QPushButton(self.page_PersoaneShow)
        self.PersDeleteButton.setGeometry(QtCore.QRect(650, 510, 81, 31))
        self.PersDeleteButton.setObjectName("PersDeleteButton")
        self.PerscomboChooseUpdate = QtWidgets.QComboBox(self.page_PersoaneShow)
        self.PerscomboChooseUpdate.setGeometry(QtCore.QRect(310, 570, 81, 31))
        self.PerscomboChooseUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PerscomboChooseUpdate.setObjectName("PerscomboChooseUpdate")
        self.PerscomboChooseUpdate.addItem("Nume")
        self.PerscomboChooseUpdate.addItem("Prenume")
        self.PersUpdateButton = QtWidgets.QPushButton(self.page_PersoaneShow)
        self.PersUpdateButton.setGeometry(QtCore.QRect(650, 570, 81, 31))
        self.PersUpdateButton.setObjectName("PersUpdateButton")
        self.PersInsertPrenume = QtWidgets.QTextEdit(self.page_PersoaneShow)
        self.PersInsertPrenume.setGeometry(QtCore.QRect(430, 450, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PersInsertPrenume.setFont(font)
        self.PersInsertPrenume.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PersInsertPrenume.setObjectName("PersInsertPrenume")
        self.PersinsertUpdate = QtWidgets.QTextEdit(self.page_PersoaneShow)
        self.PersinsertUpdate.setGeometry(QtCore.QRect(430, 570, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PersinsertUpdate.setFont(font)
        self.PersinsertUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PersinsertUpdate.setPlaceholderText("")
        self.PersinsertUpdate.setObjectName("PersinsertUpdate")
        self.PersIDcomboBox = QtWidgets.QComboBox(self.page_PersoaneShow)
        self.PersIDcomboBox.setGeometry(QtCore.QRect(560, 510, 61, 31))
        self.PersIDcomboBox.setEditable(False)
        self.PersIDcomboBox.setDuplicatesEnabled(True)
        self.PersIDcomboBox.setObjectName("PersIDcomboBox")
        self.stackedWidget.addWidget(self.page_PersoaneShow)
        self.page_DetaliiShow = QtWidgets.QWidget()
        self.page_DetaliiShow.setObjectName("page_DetaliiShow")
        self.tableDetalii = QtWidgets.QTableWidget(self.page_DetaliiShow)
        self.tableDetalii.setGeometry(QtCore.QRect(200, 70, 531, 341))
        self.tableDetalii.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableDetalii.setRowCount(0)
        self.tableDetalii.setObjectName("tableDetalii")
        self.tableDetalii.setColumnCount(4)
        self.tableDetalii.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetalii.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetalii.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetalii.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableDetalii.setHorizontalHeaderItem(3, item)
        self.tableDetalii.horizontalHeader().setDefaultSectionSize(132)
        self.DetAddButton = QtWidgets.QPushButton(self.page_DetaliiShow)
        self.DetAddButton.setGeometry(QtCore.QRect(650, 450, 81, 31))
        self.DetAddButton.setObjectName("DetAddButton")
        self.DetInsertOras = QtWidgets.QTextEdit(self.page_DetaliiShow)
        self.DetInsertOras.setGeometry(QtCore.QRect(450, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DetInsertOras.setFont(font)
        self.DetInsertOras.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DetInsertOras.setObjectName("DetInsertOras")
        self.DetInsertCNP = QtWidgets.QTextEdit(self.page_DetaliiShow)
        self.DetInsertCNP.setGeometry(QtCore.QRect(260, 450, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DetInsertCNP.setFont(font)
        self.DetInsertCNP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DetInsertCNP.setObjectName("DetInsertCNP")
        self.DetcomboSange = QtWidgets.QComboBox(self.page_DetaliiShow)
        self.DetcomboSange.setGeometry(QtCore.QRect(570, 450, 61, 31))
        self.DetcomboSange.setObjectName("DetcomboSange")
        self.DetcomboSange.addItem("")
        self.DetcomboSange.addItem("")
        self.DetcomboSange.addItem("")
        self.DetcomboSange.addItem("")
        self.DetDeleteButton = QtWidgets.QPushButton(self.page_DetaliiShow)
        self.DetDeleteButton.setGeometry(QtCore.QRect(650, 510, 81, 31))
        self.DetDeleteButton.setObjectName("DetDeleteButton")
        self.DetUpdateButton = QtWidgets.QPushButton(self.page_DetaliiShow)
        self.DetUpdateButton.setGeometry(QtCore.QRect(650, 570, 81, 31))
        self.DetUpdateButton.setObjectName("DetUpdateButton")
        self.DetsinsertUpdate = QtWidgets.QTextEdit(self.page_DetaliiShow)
        self.DetsinsertUpdate.setGeometry(QtCore.QRect(450, 570, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.DetsinsertUpdate.setFont(font)
        self.DetsinsertUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DetsinsertUpdate.setPlaceholderText("")
        self.DetsinsertUpdate.setObjectName("DetsinsertUpdate")
        self.DetcomboChooseUpdate = QtWidgets.QComboBox(self.page_DetaliiShow)
        self.DetcomboChooseUpdate.setGeometry(QtCore.QRect(370, 570, 61, 31))
        self.DetcomboChooseUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DetcomboChooseUpdate.setObjectName("DetcomboChooseUpdate")
        self.DetcomboChooseUpdate.addItem("")
        self.DetcomboChooseUpdate.addItem("")
        self.DetcomboChooseUpdate.addItem("")
        self.DetIDcomboBox = QtWidgets.QComboBox(self.page_DetaliiShow)
        self.DetIDcomboBox.setGeometry(QtCore.QRect(200, 450, 51, 31))
        self.DetIDcomboBox.setEditable(False)
        self.DetIDcomboBox.setDuplicatesEnabled(True)
        self.DetIDcomboBox.setObjectName("DetIDcomboBox")
        self.stackedWidget.addWidget(self.page_DetaliiShow)
        self.page_IstoricShow = QtWidgets.QWidget()
        self.page_IstoricShow.setObjectName("page_IstoricShow")
        self.tableIstoric = QtWidgets.QTableWidget(self.page_IstoricShow)
        self.tableIstoric.setGeometry(QtCore.QRect(200, 70, 531, 341))
        self.tableIstoric.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableIstoric.setRowCount(0)
        self.tableIstoric.setObjectName("tableIstoric")
        self.tableIstoric.setColumnCount(4)
        self.tableIstoric.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tableIstoric.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIstoric.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIstoric.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableIstoric.setHorizontalHeaderItem(3, item)
        self.tableIstoric.horizontalHeader().setDefaultSectionSize(132)
        self.IstoricInsertMedicatie = QtWidgets.QTextEdit(self.page_IstoricShow)
        self.IstoricInsertMedicatie.setGeometry(QtCore.QRect(450, 450, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.IstoricInsertMedicatie.setFont(font)
        self.IstoricInsertMedicatie.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IstoricInsertMedicatie.setObjectName("IstoricInsertMedicatie")
        self.IstoricInsertAfectiune = QtWidgets.QTextEdit(self.page_IstoricShow)
        self.IstoricInsertAfectiune.setGeometry(QtCore.QRect(260, 450, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.IstoricInsertAfectiune.setFont(font)
        self.IstoricInsertAfectiune.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IstoricInsertAfectiune.setObjectName("IstoricInsertAfectiune")
        self.IstoricAddButton = QtWidgets.QPushButton(self.page_IstoricShow)
        self.IstoricAddButton.setGeometry(QtCore.QRect(650, 470, 81, 31))
        self.IstoricAddButton.setObjectName("IstoricAddButton")
        self.IstoricInsertData = QtWidgets.QTextEdit(self.page_IstoricShow)
        self.IstoricInsertData.setGeometry(QtCore.QRect(450, 490, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.IstoricInsertData.setFont(font)
        self.IstoricInsertData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IstoricInsertData.setObjectName("IstoricInsertData")
        self.IstoricIDcomboBox = QtWidgets.QComboBox(self.page_IstoricShow)
        self.IstoricIDcomboBox.setGeometry(QtCore.QRect(200, 450, 51, 31))
        self.IstoricIDcomboBox.setEditable(False)
        self.IstoricIDcomboBox.setDuplicatesEnabled(True)
        self.IstoricIDcomboBox.setObjectName("IstoricIDcomboBox")
        self.stackedWidget.addWidget(self.page_IstoricShow)
        self.page_CazareShow = QtWidgets.QWidget()
        self.page_CazareShow.setObjectName("page_CazareShow")
        self.tableCazare = QtWidgets.QTableWidget(self.page_CazareShow)
        self.tableCazare.setGeometry(QtCore.QRect(200, 70, 531, 341))
        self.tableCazare.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableCazare.setRowCount(0)
        self.tableCazare.setObjectName("tableCazare")
        self.tableCazare.setColumnCount(3)
        self.tableCazare.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tableCazare.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCazare.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableCazare.setHorizontalHeaderItem(2, item)
        self.tableCazare.horizontalHeader().setDefaultSectionSize(176)
        self.CazareIDcomboBox = QtWidgets.QComboBox(self.page_CazareShow)
        self.CazareIDcomboBox.setGeometry(QtCore.QRect(200, 450, 51, 31))
        self.CazareIDcomboBox.setEditable(False)
        self.CazareIDcomboBox.setDuplicatesEnabled(True)
        self.CazareIDcomboBox.setObjectName("CazareIDcomboBox")
        self.CazareAddButton = QtWidgets.QPushButton(self.page_CazareShow)
        self.CazareAddButton.setGeometry(QtCore.QRect(650, 450, 81, 31))
        self.CazareAddButton.setObjectName("CazareAddButton")
        self.CazareInsertNumarPat = QtWidgets.QTextEdit(self.page_CazareShow)
        self.CazareInsertNumarPat.setGeometry(QtCore.QRect(260, 450, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CazareInsertNumarPat.setFont(font)
        self.CazareInsertNumarPat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CazareInsertNumarPat.setObjectName("CazareInsertNumarPat")
        self.CazareInsertData = QtWidgets.QTextEdit(self.page_CazareShow)
        self.CazareInsertData.setGeometry(QtCore.QRect(450, 450, 181, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CazareInsertData.setFont(font)
        self.CazareInsertData.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CazareInsertData.setObjectName("CazareInsertData")

        self.CazareUpdateButton = QtWidgets.QPushButton(self.page_CazareShow)
        self.CazareUpdateButton.setGeometry(QtCore.QRect(650, 570, 81, 31))
        self.CazareUpdateButton.setObjectName("CazareUpdateButton")
        self.CazarecomboChooseUpdate = QtWidgets.QComboBox(self.page_CazareShow)
        self.CazarecomboChooseUpdate.setGeometry(QtCore.QRect(360, 570, 81, 31))
        self.CazarecomboChooseUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CazarecomboChooseUpdate.setObjectName("CazarecomboChooseUpdate")
        self.CazarecomboChooseUpdate.addItem("")
        self.CazarecomboChooseUpdate.addItem("")
        self.CazareInsertUpdate = QtWidgets.QTextEdit(self.page_CazareShow)
        self.CazareInsertUpdate.setGeometry(QtCore.QRect(450, 570, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CazareDatacomboBox = QtWidgets.QComboBox(self.page_CazareShow)
        self.CazareDatacomboBox.setGeometry(QtCore.QRect(450, 510, 181, 31))
        self.CazareDatacomboBox.setEditable(False)
        self.CazareDatacomboBox.setDuplicatesEnabled(True)
        self.CazareDatacomboBox.setObjectName("CazareDatacomboBox")
        self.CazareInsertUpdate.setFont(font)
        self.CazareInsertUpdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CazareInsertUpdate.setPlaceholderText("")
        self.CazareInsertUpdate.setObjectName("CazareInsertUpdate")
        self.CazareDeleteButton = QtWidgets.QPushButton(self.page_CazareShow)
        self.CazareDeleteButton.setGeometry(QtCore.QRect(650, 510, 81, 31))
        self.CazareDeleteButton.setObjectName("CazareDeleteButton")
        self.CazareIDcomboBox.currentIndexChanged.connect(lambda: IDChanged2(self))
        self.stackedWidget.addWidget(self.page_CazareShow)
        self.page_ObservatiiShow = QtWidgets.QWidget()
        self.page_ObservatiiShow.setObjectName("page_ObservatiiShow")
        self.tableObservatii = QtWidgets.QTableWidget(self.page_ObservatiiShow)
        self.tableObservatii.setGeometry(QtCore.QRect(200, 70, 531, 341))
        self.tableObservatii.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableObservatii.setRowCount(0)
        self.tableObservatii.setObjectName("tableObservatii")
        self.tableObservatii.setColumnCount(4)
        self.tableObservatii.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.tableObservatii.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableObservatii.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableObservatii.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableObservatii.setHorizontalHeaderItem(3, item)
        self.tableObservatii.horizontalHeader().setDefaultSectionSize(132)
        self.ObservatiiIDcomboBox = QtWidgets.QComboBox(self.page_ObservatiiShow)
        self.ObservatiiIDcomboBox.setGeometry(QtCore.QRect(200, 450, 51, 31))
        self.ObservatiiIDcomboBox.setEditable(False)
        self.ObservatiiIDcomboBox.setDuplicatesEnabled(True)
        self.ObservatiiIDcomboBox.setObjectName("ObservatiiIDcomboBox")
        self.ObservatiiIDcomboBox.currentIndexChanged.connect(lambda: IDChanged1(self))
        self.ObservatiiDatacomboBox = QtWidgets.QComboBox(self.page_ObservatiiShow)
        self.ObservatiiDatacomboBox.setGeometry(QtCore.QRect(270, 450, 131, 31))
        self.ObservatiiDatacomboBox.setEditable(False)
        self.ObservatiiDatacomboBox.setDuplicatesEnabled(True)
        self.ObservatiiDatacomboBox.setObjectName("ObservatiiDatacomboBox")
        self.ObservatiiInsertFapta = QtWidgets.QTextEdit(self.page_ObservatiiShow)
        self.ObservatiiInsertFapta.setGeometry(QtCore.QRect(420, 450, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ObservatiiInsertFapta.setFont(font)
        self.ObservatiiInsertFapta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ObservatiiInsertFapta.setObjectName("ObservatiiInsertFapta")
        self.ObservatiiGravitatecomboBox = QtWidgets.QComboBox(self.page_ObservatiiShow)
        self.ObservatiiGravitatecomboBox.setGeometry(QtCore.QRect(590, 450, 51, 31))
        self.ObservatiiGravitatecomboBox.setEditable(False)
        self.ObservatiiGravitatecomboBox.setDuplicatesEnabled(True)
        self.ObservatiiGravitatecomboBox.setObjectName("ObservatiiGravitatecomboBox")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiGravitatecomboBox.addItem("")
        self.ObservatiiAddButton = QtWidgets.QPushButton(self.page_ObservatiiShow)
        self.ObservatiiAddButton.setGeometry(QtCore.QRect(650, 450, 81, 31))
        self.ObservatiiAddButton.setObjectName("ObservatiiAddButton")
        self.ObservatiiDeleteButton = QtWidgets.QPushButton(self.page_ObservatiiShow)
        self.ObservatiiDeleteButton.setGeometry(QtCore.QRect(650, 510, 81, 31))
        self.ObservatiiDeleteButton.setObjectName("ObservatiiDeleteButton")
        self.stackedWidget.addWidget(self.page_ObservatiiShow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        self.menuPersoane = QtWidgets.QMenu(self.menubar)
        self.menuPersoane.setObjectName("menuPersoane")
        self.menuDetalii = QtWidgets.QMenu(self.menubar)
        self.menuDetalii.setObjectName("menuDetalii")
        self.menuIstoricM = QtWidgets.QMenu(self.menubar)
        self.menuIstoricM.setObjectName("menuIstoricM")
        self.menuCazare = QtWidgets.QMenu(self.menubar)
        self.menuCazare.setObjectName("menuCazare")
        self.menuObservatii = QtWidgets.QMenu(self.menubar)
        self.menuObservatii.setObjectName("menuObservatii")
        MainWindow.setMenuBar(self.menubar)
        self.ShowPersoane = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowPersoane.setFont(font)
        self.ShowPersoane.setObjectName("ShowPersoane")
        self.ShowDetalii = QtWidgets.QAction(MainWindow)
        self.ShowDetalii.setObjectName("ShowDetalii")
        self.ShowIstoricM = QtWidgets.QAction(MainWindow)
        self.ShowIstoricM.setObjectName("ShowIstoricM")
        self.ShowCazare = QtWidgets.QAction(MainWindow)
        self.ShowCazare.setObjectName("showCazare")
        self.ShowObservatii = QtWidgets.QAction(MainWindow)
        self.ShowObservatii.setObjectName("showObservatii")
        self.menuPersoane.addAction(self.ShowPersoane)
        self.menuDetalii.addAction(self.ShowDetalii)
        self.menuIstoricM.addAction(self.ShowIstoricM)
        self.menuCazare.addAction(self.ShowCazare)
        self.menuObservatii.addAction(self.ShowObservatii)
        self.menubar.addAction(self.menuPersoane.menuAction())
        self.menubar.addAction(self.menuDetalii.menuAction())
        self.menubar.addAction(self.menuIstoricM.menuAction())
        self.menubar.addAction(self.menuCazare.menuAction())
        self.menubar.addAction(self.menuObservatii.menuAction())
        self.retranslateUi(MainWindow)

        #######################CONECTARE FERESTRE DE TAB-UL MENIU SI AFISARE #########################
        self.ShowPersoane.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_PersoaneShow))
        self.ShowDetalii.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_DetaliiShow))
        self.ShowIstoricM.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_IstoricShow))
        self.ShowCazare.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_CazareShow))
        self.ShowObservatii.triggered.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ObservatiiShow))
        showAllValues(self)
        ##############################################################################################
        #######################Functiile de callback ale butoanelor###################################
        self.PersAddButton.clicked.connect(lambda: addEntryPersoana(self))
        self.DetAddButton.clicked.connect(lambda: addEntryDetaliiP(self))
        self.IstoricAddButton.clicked.connect(lambda: addEntryIstoricM(self))
        self.CazareAddButton.clicked.connect(lambda: addEntryCazare(self))
        self.ObservatiiAddButton.clicked.connect(lambda: addEntryObservatii(self))
        self.PersDeleteButton.clicked.connect(lambda:deleteEntryPersoana(self))
        self.DetDeleteButton.clicked.connect(lambda: deleteEntryDetalii(self))
        self.CazareDeleteButton.clicked.connect(lambda:deleteEntryCazare(self))
        self.ObservatiiDeleteButton.clicked.connect(lambda: deleteEntryObservatii(self))
        self.PersUpdateButton.clicked.connect(lambda: updatePersoane(self))
        self.DetUpdateButton.clicked.connect(lambda: updateDetaliiP(self))
        self.CazareUpdateButton.clicked.connect(lambda: updateCazare(self))
        ###############################################################################################
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        app.aboutToQuit.connect(self.closeEvent)

    def closeEvent(self):
        # Your desired functionality here
        print('Close button pressed')
        con.close()
        print('Conexiune inchisa')
        import sys
        sys.exit(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Baze de Date---Tema"))
        item = self.tablePersoane.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Persoana"))
        item = self.tablePersoane.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nume"))
        item = self.tablePersoane.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prenume"))
        self.PersinsertNume.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.PersinsertNume.setPlaceholderText(_translate("MainWindow", "Nume"))
        self.PersAddButton.setText(_translate("MainWindow", "Add"))
        self.PersDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.PerscomboChooseUpdate.setItemText(0, _translate("MainWindow", "Nume"))
        self.PerscomboChooseUpdate.setItemText(1, _translate("MainWindow", "Prenume"))
        self.PersUpdateButton.setText(_translate("MainWindow", "Update"))
        self.PersInsertPrenume.setHtml(_translate("MainWindow",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.PersInsertPrenume.setPlaceholderText(_translate("MainWindow", "Prenume"))
        self.PersinsertUpdate.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        item = self.tableDetalii.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Persoana"))
        item = self.tableDetalii.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CNP"))
        item = self.tableDetalii.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Oras natal"))
        item = self.tableDetalii.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tip de sange"))
        self.DetAddButton.setText(_translate("MainWindow", "Add"))
        self.DetInsertOras.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.DetInsertOras.setPlaceholderText(_translate("MainWindow", "Oras"))
        self.DetInsertCNP.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.DetInsertCNP.setPlaceholderText(_translate("MainWindow", "CNP"))
        self.DetcomboSange.setItemText(0, _translate("MainWindow", "O"))
        self.DetcomboSange.setItemText(1, _translate("MainWindow", "A"))
        self.DetcomboSange.setItemText(2, _translate("MainWindow", "B"))
        self.DetcomboSange.setItemText(3, _translate("MainWindow", "AB"))
        self.DetDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.DetUpdateButton.setText(_translate("MainWindow", "Update"))
        self.DetsinsertUpdate.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.DetcomboChooseUpdate.setItemText(0, _translate("MainWindow", "CNP"))
        self.DetcomboChooseUpdate.setItemText(1, _translate("MainWindow", "Oras"))
        self.DetcomboChooseUpdate.setItemText(2, _translate("MainWindow", "Tip de Sange"))
        item = self.tableIstoric.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Persoana"))
        item = self.tableIstoric.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Afectiune"))
        item = self.tableIstoric.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Medicatie"))
        item = self.tableIstoric.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data tratament"))
        self.IstoricInsertMedicatie.setHtml(_translate("MainWindow",
                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.IstoricInsertMedicatie.setPlaceholderText(_translate("MainWindow", "Medicatie"))
        self.IstoricInsertAfectiune.setHtml(_translate("MainWindow",
                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.IstoricInsertAfectiune.setPlaceholderText(_translate("MainWindow", "Afectiune"))
        self.IstoricAddButton.setText(_translate("MainWindow", "Add"))
        self.IstoricInsertData.setHtml(_translate("MainWindow",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.IstoricInsertData.setPlaceholderText(_translate("MainWindow", "Data: dd.mm.yyyy"))
        item = self.tableCazare.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Persoana"))
        item = self.tableCazare.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Numar Pat"))
        item = self.tableCazare.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data Cazarii"))
        self.CazareAddButton.setText(_translate("MainWindow", "Add"))
        self.CazareInsertNumarPat.setHtml(_translate("MainWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.CazareInsertNumarPat.setPlaceholderText(_translate("MainWindow", "Numar Pat"))
        self.CazareInsertData.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.CazareInsertData.setPlaceholderText(_translate("MainWindow", "Data: dd.mm.yyyy"))

        self.CazareUpdateButton.setText(_translate("MainWindow", "Update"))
        self.CazarecomboChooseUpdate.setItemText(0, _translate("MainWindow", "Numar Pat"))
        self.CazarecomboChooseUpdate.setItemText(1, _translate("MainWindow", "Data Cazarii"))
        self.CazareInsertUpdate.setHtml(_translate("MainWindow",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.CazareDeleteButton.setText(_translate("MainWindow", "Delete"))
        item = self.tableObservatii.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID Persoana"))
        item = self.tableObservatii.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fapta Savarsita"))
        item = self.tableObservatii.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gravitate"))
        item = self.tableObservatii.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data cazarii"))
        self.ObservatiiInsertFapta.setHtml(_translate("MainWindow",
                                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.ObservatiiInsertFapta.setPlaceholderText(_translate("MainWindow", "Fapta savarsita"))
        self.ObservatiiGravitatecomboBox.setItemText(0, _translate("MainWindow", "1"))
        self.ObservatiiGravitatecomboBox.setItemText(1, _translate("MainWindow", "2"))
        self.ObservatiiGravitatecomboBox.setItemText(2, _translate("MainWindow", "3"))
        self.ObservatiiGravitatecomboBox.setItemText(3, _translate("MainWindow", "4"))
        self.ObservatiiGravitatecomboBox.setItemText(4, _translate("MainWindow", "5"))
        self.ObservatiiGravitatecomboBox.setItemText(5, _translate("MainWindow", "6"))
        self.ObservatiiGravitatecomboBox.setItemText(6, _translate("MainWindow", "7"))
        self.ObservatiiGravitatecomboBox.setItemText(7, _translate("MainWindow", "8"))
        self.ObservatiiGravitatecomboBox.setItemText(8, _translate("MainWindow", "9"))
        self.ObservatiiGravitatecomboBox.setItemText(9, _translate("MainWindow", "10"))
        self.ObservatiiAddButton.setText(_translate("MainWindow", "Add"))
        self.ObservatiiDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.menuPersoane.setTitle(_translate("MainWindow", "Persoane"))
        self.menuDetalii.setTitle(_translate("MainWindow", "Detalii Persoane"))
        self.menuIstoricM.setTitle(_translate("MainWindow", "Istoric_Medical"))
        self.menuCazare.setTitle(_translate("MainWindow", "Cazare"))
        self.menuObservatii.setTitle(_translate("MainWindow", "Observatii"))
        self.ShowPersoane.setText(_translate("MainWindow", "Show"))
        self.ShowDetalii.setText(_translate("MainWindow", "Show"))
        self.ShowIstoricM.setText(_translate("MainWindow", "Show"))
        self.ShowCazare.setText(_translate("MainWindow", "Show"))
        self.ShowObservatii.setText(_translate("MainWindow", "Show"))




def showPersoane(self):
    persoane = []
    cur = con.cursor()
    cur.execute('select * from persoane order by ID_Primit')
    for result in cur:
        persoana = {}
        persoana['ID'] = result[0]
        persoana['Nume'] = result[1]
        persoana['Prenume'] = result[2]
        persoane.append(persoana)
    cur.close()
    row = 0
    self.tablePersoane.setRowCount(0)
    self.tablePersoane.setRowCount(len(persoane))
    for person in persoane:
        self.tablePersoane.setItem(row, 0, QtWidgets.QTableWidgetItem(str(person["ID"])))
        self.tablePersoane.setItem(row, 1, QtWidgets.QTableWidgetItem(person["Nume"]))
        self.tablePersoane.setItem(row, 2, QtWidgets.QTableWidgetItem(person["Prenume"]))
        row = row + 1

def showDetaliiP(self):
    Dpersoane = []
    cur = con.cursor()
    cur.execute('select * from detalii_persoane order by Persoane_ID_Primit')
    for result in cur:
        persoana = {}
        persoana['ID'] = result[0]
        persoana['CNP'] = result[1]
        persoana['Oras'] = result[2]
        persoana['Sange'] = result[3]
        Dpersoane.append(persoana)
    cur.close()
    row = 0
    self.tableDetalii.setRowCount(0)
    self.tableDetalii.setRowCount(len(Dpersoane))
    for person in Dpersoane:
        self.tableDetalii.setItem(row, 0, QtWidgets.QTableWidgetItem(str(person["ID"])))
        self.tableDetalii.setItem(row, 1, QtWidgets.QTableWidgetItem(str(person["CNP"])))
        self.tableDetalii.setItem(row, 2, QtWidgets.QTableWidgetItem(str(person["Oras"])))
        self.tableDetalii.setItem(row, 3, QtWidgets.QTableWidgetItem(str(person["Sange"])))
        row = row + 1

def showIstoric(self):
    IstoricM = []
    cur = con.cursor()
    cur.execute('select * from Istoric_medical order by Persoane_ID_Primit')
    for result in cur:
        entry = {}
        entry['ID'] = result[0]
        entry['Afectiune'] = result[1]
        entry['Medicatie'] = result[2]
        entry['Data'] = result[3]
        IstoricM.append(entry)
    cur.close()
    row = 0
    self.tableIstoric.setRowCount(0)
    self.tableIstoric.setRowCount(len(IstoricM))
    for entry in IstoricM:
        self.tableIstoric.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry["ID"])))
        self.tableIstoric.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry["Afectiune"])))
        self.tableIstoric.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry["Medicatie"])))
        try:
            self.tableIstoric.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry["Data"].strftime("%d.%m.%Y"))))
        except:
            pass
        row = row + 1

def showCazare(self):
    Cazare = []
    cur = con.cursor()
    cur.execute('select * from Cazare order by Data_Cazarii')
    for result in cur:
        entry = {}
        entry['ID'] = result[0]
        entry['Pat'] = result[1]
        entry['Data'] = result[2]

        Cazare.append(entry)
    cur.close()
    row = 0
    self.tableCazare.setRowCount(0)
    self.tableCazare.setRowCount(len(Cazare))
    for entry in Cazare:
        self.tableCazare.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry["ID"])))
        self.tableCazare.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry["Pat"])))
        self.tableCazare.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry["Data"].strftime("%d.%m.%Y"))))
        row = row + 1

def showObservatii(self):
    Observatii = []
    cur = con.cursor()
    cur.execute('select * from Observatii order by Cazare_Data_Cazarii')
    for result in cur:
        entry = {}
        entry['ID'] = result[4]
        entry['Fapta'] = result[0]
        entry['Gravitate'] = result[1]
        entry['Data'] = result[3]
        Observatii.append(entry)
    cur.close()
    row = 0
    self.tableObservatii.setRowCount(0)
    self.tableObservatii.setRowCount(len(Observatii))
    for entry in Observatii:
        self.tableObservatii.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry["ID"])))
        self.tableObservatii.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry["Fapta"])))
        self.tableObservatii.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry["Gravitate"])))
        self.tableObservatii.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry["Data"].strftime("%d.%m.%Y"))))
        row = row + 1

def showAllValues(self):
    showPersoane(self)
    showDetaliiP(self)
    showIstoric(self)
    showCazare(self)
    showObservatii(self)
    getAllID(self)
    IDChanged1(self)
    IDChanged2(self)

def getAllID(self):
    ID = []
    cur = con.cursor()
    cur.execute('select * from Persoane order by ID_Primit')
    for result in cur:
        entry = result[0]
        ID.append(entry)
    cur.close()
    self.PersIDcomboBox.clear()
    self.DetIDcomboBox.clear()
    self.IstoricIDcomboBox.clear()
    self.CazareIDcomboBox.clear()
    self.ObservatiiIDcomboBox.clear()
    for id in ID:
        self.PersIDcomboBox.addItem(str(id))
        self.DetIDcomboBox.addItem(str(id))
        self.IstoricIDcomboBox.addItem(str(id))
        self.CazareIDcomboBox.addItem(str(id))
        self.ObservatiiIDcomboBox.addItem(str(id))

def IDChanged1(self):
    Data = []
    try:
        cur = con.cursor()
        cur.execute('select Data_Cazarii from Cazare where Persoane_ID_Primit={} order by Data_Cazarii'.format(str(self.ObservatiiIDcomboBox.currentText())))
        for result in cur:
            entry = result[0]
            Data.append(entry)
    except:
        return
    finally:
        cur.close()
    self.ObservatiiDatacomboBox.clear()
    for date in Data:
        self.ObservatiiDatacomboBox.addItem(date.strftime("%d.%m.%Y"))

def IDChanged2(self):
    Data = []
    try:
        cur = con.cursor()
        cur.execute('select Data_Cazarii from Cazare where Persoane_ID_Primit={} order by Data_Cazarii'.format(str(self.CazareIDcomboBox.currentText())))
        for result in cur:
            entry = result[0]
            Data.append(entry)
    except:
        return
    finally:
        cur.close()
    self.CazareDatacomboBox.clear()
    for date in Data:
        self.CazareDatacomboBox.addItem(date.strftime("%d.%m.%Y"))

def addEntryPersoana(self):
    nume = self.PersinsertNume.toPlainText()
    nume = nume.capitalize().strip()
    prenume = self.PersInsertPrenume.toPlainText()
    prenume = prenume.capitalize().strip()
    if (len(nume) < 3 or len(prenume) < 3):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Nume/Prenume introdus incorect!')
        error_dialog.exec_()
        return
    try:
        cur = con.cursor()
        sql = """ INSERT INTO Persoane
                               (Nume,Prenume) VALUES ('{}','{}')""".format(nume,prenume)
        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def addEntryDetaliiP(self):
    ID = str(self.DetIDcomboBox.currentText())
    CNP= str(self.DetInsertCNP.toPlainText()).strip()
    Oras=str(self.DetInsertOras.toPlainText()).capitalize().strip()
    BloodType=str(self.DetcomboSange.currentText())
    if (len(CNP)!=13 or len(Oras)<3):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Date introduse incorect!')
        error_dialog.exec_()
        return
    try:
        cur = con.cursor()
        sql = """ INSERT INTO Detalii_Persoane
                                VALUES ('{}','{}','{}','{}')""".format(ID,CNP,Oras,BloodType)
        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def addEntryIstoricM(self):
    ID = str(self.IstoricIDcomboBox.currentText())
    Afectiune= str(self.IstoricInsertAfectiune.toPlainText()).strip().capitalize()
    Medicatie=str(self.IstoricInsertMedicatie.toPlainText()).capitalize().strip().capitalize()
    Data=str(self.IstoricInsertData.toPlainText()).capitalize().strip()

    if (len(Afectiune)<4 or len(Medicatie)<3 or len(Data)!=10):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Date introduse incorect!')
        error_dialog.exec_()
        return
    try:
        cur = con.cursor()
        sql = """ INSERT INTO Istoric_medical 
                                VALUES ('{}','{}','{}',to_date('{}','dd.mm.yyyy'))""".format(ID,Afectiune,Medicatie,Data)
        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def addEntryCazare(self):
    ID = str(self.CazareIDcomboBox.currentText())
    Pat= str(self.CazareInsertNumarPat.toPlainText()).strip().capitalize()
    Data=str(self.CazareInsertData.toPlainText()).capitalize().strip()

    try:
        cur = con.cursor()
        sql = """ INSERT INTO Cazare 
                                VALUES ('{}','{}',to_date('{}','dd.mm.yyyy'))""".format(ID,Pat,Data)
        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def addEntryObservatii(self):
    ID = str(self.ObservatiiIDcomboBox.currentText())
    Data=str(self.ObservatiiDatacomboBox.currentText())
    Gravitate=str(self.ObservatiiGravitatecomboBox.currentText())
    Fapta=str(self.ObservatiiInsertFapta.toPlainText()).strip().capitalize()

    try:
        cur = con.cursor()
        cur.execute(""" select Nr_Pat from Cazare where Persoane_ID_Primit={} and Data_Cazarii=to_date('{}','dd.mm.yyyy')""".format(ID,Data))
        for value in cur:
            Pat=value[0]
    except:
        return
    finally:
        cur.close()

    try:
        cur = con.cursor()
        sql = """ INSERT INTO Observatii 
                                VALUES ('{}','{}','{}',to_date('{}','dd.mm.yyyy'),'{}')""".format(Fapta,Gravitate,Pat,Data,ID)
        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def deleteEntryPersoana(self):
    ID=str(self.PersIDcomboBox.currentText())
    try:
        cur = con.cursor()
        cur.execute('Delete from Persoane where ID_Primit={}'.format(ID))
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def deleteEntryDetalii(self):
    ID=str(self.DetIDcomboBox.currentText())
    try:
        cur = con.cursor()
        cur.execute('Delete from Detalii_Persoane where Persoane_ID_Primit={}'.format(ID))
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def deleteEntryCazare(self):
    ID=str(self.CazareIDcomboBox.currentText())
    Data = str(self.CazareDatacomboBox.currentText())
    try:
        cur = con.cursor()


        cur.execute(
                """ Delete from Cazare where Persoane_ID_Primit={} and Data_Cazarii=to_date('{}','dd.mm.yyyy')""".format(
                    ID, Data))
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def deleteEntryObservatii(self):
    ID = str(self.ObservatiiIDcomboBox.currentText())
    Data = str(self.ObservatiiDatacomboBox.currentText())
    try:
        cur = con.cursor()
        cur.execute(
             """ Delete from Observatii where Cazare_ID_Primit={} and Cazare_Data_Cazarii=to_date('{}','dd.mm.yyyy')""".format(
                 ID, Data))
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def updatePersoane(self):
    camp=str(self.PerscomboChooseUpdate.currentText())
    campIntrodus = str(self.PersinsertUpdate.toPlainText()).strip().capitalize()
    ID = str(self.PersIDcomboBox.currentText())
    if (len(campIntrodus)<3):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Nume/Prenume introdus incorect!')
        error_dialog.exec_()
        return
    try:
        cur = con.cursor()
        if(camp=="Nume"):
            sql = """ Update Persoane set Nume='{}' where ID_Primit={}""".format(campIntrodus, ID)
        else:
            sql = """ Update Persoane set Prenume='{}' where ID_Primit={}""".format(campIntrodus, ID)

        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def updateDetaliiP(self):
    camp=str(self.DetcomboChooseUpdate.currentText())
    campIntrodus = str(self.DetsinsertUpdate.toPlainText()).strip().upper()
    ID = str(self.DetIDcomboBox.currentText())
    if ((camp=="CNP" and len(campIntrodus)!=13) or (camp=="Oras" and len(campIntrodus)<3) or (camp=="Tip de Sange" and len(campIntrodus)>2)):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Valoare noua gresita!')
        error_dialog.exec_()
        return
    try:
        cur = con.cursor()
        if(camp=="CNP"):
            sql = """ Update Detalii_Persoane set CNP='{}' where Persoane_ID_Primit={}""".format(campIntrodus, ID)
        elif(camp=="Oras"):
            sql = """ Update Detalii_Persoane set Orasul_natal='{}' where Persoane_ID_Primit={}""".format(campIntrodus, ID)
        else:
            sql = """ Update Detalii_Persoane set Tip_de_sange='{}' where Persoane_ID_Primit={}""".format(campIntrodus, ID)

        cur.execute(sql)
        con.commit()
        showAllValues(self)

    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()

def updateCazare(self):
    camp=str(self.CazarecomboChooseUpdate.currentText())
    Data = str(self.CazareDatacomboBox.currentText())
    campIntrodus = str(self.CazareInsertUpdate.toPlainText()).strip().capitalize()
    ID = str(self.CazareIDcomboBox.currentText())
    if (camp=="Data Cazarii" and len(campIntrodus)!=10):
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Valoare noua gresita!')
        error_dialog.exec_()
        return
    try:
        cur = con.cursor()
        if(camp=="Numar Pat"):
            sql = """ Update Cazare set Nr_Pat='{}' where Persoane_ID_Primit={} and Data_Cazarii=to_date('{}','dd.mm.yyyy')""".format(campIntrodus, ID,Data)
        else:
            sql = """ Update Cazare set Data_Cazarii=to_date('{}','dd.mm.yyyy') where Persoane_ID_Primit={} and Data_Cazarii=to_date('{}','dd.mm.yyyy')""".format(campIntrodus, ID,Data)

        cur.execute(sql)
        con.commit()
        showAllValues(self)


    except cx_Oracle.Error as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(str(e))
        error_dialog.exec_()
    finally:
        cur.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    thread = Thread(target=MainWindow.show())
    thread.start()
    thread.join()
    sys.exit(app.exec_())
