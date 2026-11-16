# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_GameForm(object):
    def setupUi(self, GameForm):
        if not GameForm.objectName():
            GameForm.setObjectName(u"GameForm")
        GameForm.resize(560, 750)
        self.rootLayout = QVBoxLayout(GameForm)
        self.rootLayout.setSpacing(14)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(24, 24, 24, 24)
        self.formTitle = QLabel(GameForm)
        self.formTitle.setObjectName(u"formTitle")

        self.rootLayout.addWidget(self.formTitle)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(12)
        self.titleLabel = QLabel(GameForm)
        self.titleLabel.setObjectName(u"titleLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.titleLabel)

        self.titleInput = QLineEdit(GameForm)
        self.titleInput.setObjectName(u"titleInput")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.titleInput)

        self.genreLabel = QLabel(GameForm)
        self.genreLabel.setObjectName(u"genreLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.genreLabel)

        self.genreInput = QComboBox(GameForm)
        self.genreInput.setObjectName(u"genreInput")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.genreInput)

        self.platformLabel = QLabel(GameForm)
        self.platformLabel.setObjectName(u"platformLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.platformLabel)

        self.platformInput = QComboBox(GameForm)
        self.platformInput.setObjectName(u"platformInput")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.platformInput)

        self.yearLabel = QLabel(GameForm)
        self.yearLabel.setObjectName(u"yearLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.yearLabel)

        self.yearInput = QSpinBox(GameForm)
        self.yearInput.setObjectName(u"yearInput")
        self.yearInput.setMinimum(1958)
        self.yearInput.setMaximum(2100)
        self.yearInput.setValue(2024)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.yearInput)

        self.ratingLabel = QLabel(GameForm)
        self.ratingLabel.setObjectName(u"ratingLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ratingLabel)

        self.ratingInput = QDoubleSpinBox(GameForm)
        self.ratingInput.setObjectName(u"ratingInput")
        self.ratingInput.setMaximum(5.000000000000000)
        self.ratingInput.setSingleStep(0.500000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.ratingInput)

        self.coverLabel = QLabel(GameForm)
        self.coverLabel.setObjectName(u"coverLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.coverLabel)

        self.coverLayout = QHBoxLayout()
        self.coverLayout.setObjectName(u"coverLayout")
        self.coverInput = QLineEdit(GameForm)
        self.coverInput.setObjectName(u"coverInput")
        self.coverInput.setReadOnly(True)

        self.coverLayout.addWidget(self.coverInput)

        self.browseCoverButton = QPushButton(GameForm)
        self.browseCoverButton.setObjectName(u"browseCoverButton")

        self.coverLayout.addWidget(self.browseCoverButton)


        self.formLayout.setLayout(5, QFormLayout.ItemRole.FieldRole, self.coverLayout)


        self.rootLayout.addLayout(self.formLayout)

        self.coverPreview = QLabel(GameForm)
        self.coverPreview.setObjectName(u"coverPreview")
        self.coverPreview.setMinimumSize(QSize(120, 160))
        self.coverPreview.setMaximumSize(QSize(120, 160))
        self.coverPreview.setAlignment(Qt.AlignCenter)

        self.rootLayout.addWidget(self.coverPreview)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.rootLayout.addItem(self.verticalSpacer)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(GameForm)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(GameForm)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonLayout.addWidget(self.saveButton)


        self.rootLayout.addLayout(self.buttonLayout)


        self.retranslateUi(GameForm)

        QMetaObject.connectSlotsByName(GameForm)
    # setupUi

    def retranslateUi(self, GameForm):
        GameForm.setWindowTitle(QCoreApplication.translate("GameForm", u"A\u00f1adir / Editar Videojuego", None))
        self.formTitle.setText(QCoreApplication.translate("GameForm", u"A\u00f1adir videojuego", None))
        self.titleLabel.setText(QCoreApplication.translate("GameForm", u"T\u00edtulo *", None))
        self.titleInput.setPlaceholderText(QCoreApplication.translate("GameForm", u"Ej: Elden Ring", None))
        self.genreLabel.setText(QCoreApplication.translate("GameForm", u"G\u00e9nero", None))
        self.platformLabel.setText(QCoreApplication.translate("GameForm", u"Plataforma", None))
        self.yearLabel.setText(QCoreApplication.translate("GameForm", u"A\u00f1o", None))
        self.ratingLabel.setText(QCoreApplication.translate("GameForm", u"Puntuaci\u00f3n (0-5)", None))
        self.coverLabel.setText(QCoreApplication.translate("GameForm", u"Car\u00e1tula", None))
        self.browseCoverButton.setText(QCoreApplication.translate("GameForm", u"Examinar\u2026", None))
        self.coverPreview.setText(QCoreApplication.translate("GameForm", u"Sin car\u00e1tula", None))
        self.cancelButton.setText(QCoreApplication.translate("GameForm", u"Cancelar", None))
        self.saveButton.setText(QCoreApplication.translate("GameForm", u"Guardar", None))
    # retranslateUi

