# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(900, 620))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(16)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 22, 24, 22)
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")

        self.headerLayout.addWidget(self.logoLabel)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.headerSpacer)

        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.headerLayout.addWidget(self.addButton)


        self.mainLayout.addLayout(self.headerLayout)

        self.subtitleLabel = QLabel(self.centralwidget)
        self.subtitleLabel.setObjectName(u"subtitleLabel")

        self.mainLayout.addWidget(self.subtitleLabel)

        self.filtersLayout = QHBoxLayout()
        self.filtersLayout.setObjectName(u"filtersLayout")
        self.searchInput = QLineEdit(self.centralwidget)
        self.searchInput.setObjectName(u"searchInput")

        self.filtersLayout.addWidget(self.searchInput)

        self.genreFilter = QComboBox(self.centralwidget)
        self.genreFilter.setObjectName(u"genreFilter")
        self.genreFilter.setMinimumSize(QSize(150, 0))

        self.filtersLayout.addWidget(self.genreFilter)

        self.platformFilter = QComboBox(self.centralwidget)
        self.platformFilter.setObjectName(u"platformFilter")
        self.platformFilter.setMinimumSize(QSize(170, 0))

        self.filtersLayout.addWidget(self.platformFilter)


        self.mainLayout.addLayout(self.filtersLayout)

        self.countLabel = QLabel(self.centralwidget)
        self.countLabel.setObjectName(u"countLabel")

        self.mainLayout.addWidget(self.countLabel)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollContent = QWidget()
        self.scrollContent.setObjectName(u"scrollContent")
        self.cardsLayout = QGridLayout(self.scrollContent)
        self.cardsLayout.setObjectName(u"cardsLayout")
        self.cardsLayout.setAlignment(Qt.AlignTop)
        self.cardsLayout.setHorizontalSpacing(16)
        self.cardsLayout.setVerticalSpacing(16)
        self.scrollArea.setWidget(self.scrollContent)

        self.mainLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GameDex | Biblioteca de videojuegos", None))
        self.logoLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f3ae GameDex", None))
        self.logoLabel.setObjectName(QCoreApplication.translate("MainWindow", u"logoLabel", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\uff0b A\u00f1adir videojuego", None))
        self.addButton.setObjectName(QCoreApplication.translate("MainWindow", u"addButton", None))
        self.subtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Tu colecci\u00f3n, organizada en un solo lugar.", None))
        self.subtitleLabel.setObjectName(QCoreApplication.translate("MainWindow", u"subtitleLabel", None))
        self.searchInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar por t\u00edtulo...", None))
        self.countLabel.setText(QCoreApplication.translate("MainWindow", u"0 videojuegos", None))
        self.countLabel.setObjectName(QCoreApplication.translate("MainWindow", u"countLabel", None))
    # retranslateUi

