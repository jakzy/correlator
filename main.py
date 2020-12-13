import design
import sys
import filetype
from correlator import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap


class correlatorWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        # Доступ к переменным, методам и т.д. в файле design.py
        super().__init__()
        # Инициализация дизайна
        self.setupUi(self)

        # Связь нажатия кнопок загрузки
        self.btnLoad_Full.clicked.connect(self.openFileFull)
        self.btnLoad_Part.clicked.connect(self.openFilePart)

        # Связь опций цвета
        self.btn_white.triggered.connect(self.setColor)
        self.btn_black.triggered.connect(self.setColor)
        self.btn_red.triggered.connect(self.setColor)
        self.btn_orange.triggered.connect(self.setColor)
        self.btn_yellow.triggered.connect(self.setColor)
        self.btn_green.triggered.connect(self.setColor)
        self.btn_blue.triggered.connect(self.setColor)
        self.btn_purple.triggered.connect(self.setColor)

        # Связь опций метода
        self.btn_SQDIFF.triggered.connect(self.setMethod)
        self.btn_SQDIFF_NORMED.triggered.connect(self.setMethod)
        self.btn_CCOEFF.triggered.connect(self.setMethod)
        self.btn_CCOEFF_NORMED.triggered.connect(self.setMethod)
        self.btn_CCORR.triggered.connect(self.setMethod)
        self.btn_CCORR_NORMED.triggered.connect(self.setMethod)

        # Связь опции печати карты
        self.cbtnMAP.stateChanged.connect(self.checkMap)

        # Связь нажатия кнопки выполнения программы
        self.btnMain.clicked.connect(self.runCorr)

        # Функционирующий класс
        self.correlator = Correlator()

    def openFileFull(self):
        """
        Открытие файла полного изображения
        """
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")[0]
        if fileName:
            self.image_full = cv2.imread(fileName)
            if filetype.is_image(fileName):
                self.correlator.set_full(fileName)
                pix = QPixmap(fileName)
                self.label_full.setPixmap(pix)
                self.checkLoads()

    def openFilePart(self):
        """
        Открытие файла искомого изображения
        """
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")[0]
        if fileName:
            self.image_part = cv2.imread(fileName)
            if filetype.is_image(fileName):
                self.correlator.set_part(fileName)
                pix = QPixmap(fileName)
                self.label_part.setPixmap(pix)
                self.checkLoads()

    def checkLoads(self):
        """
        Проверка на то, загруженны ли целевое изображение и шаблон
        """
        if self.correlator.is_full and self.correlator.is_part:
            self.btnMain.setEnabled(True)

    def setColor(self):
        """
        Изменение цвета прямоугольника вокруг найденного изображения
        """
        if self.btn_white.isChecked():
            self.correlator.set_color('white')

            self.btn_black.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_blue.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_black.isChecked():
            self.correlator.set_color('black')

            self.btn_white.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_blue.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_red.isChecked():
            self.correlator.set_color('red')

            self.btn_white.setEnabled(False)
            self.btn_black.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_blue.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_orange.isChecked():
            self.correlator.set_color('orange')

            self.btn_white.setEnabled(False)
            self.btn_black.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_blue.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_yellow.isChecked():
            self.correlator.set_color('yellow')

            self.btn_white.setEnabled(False)
            self.btn_black.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_blue.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_green.isChecked():
            self.correlator.set_color('green')

            self.btn_white.setEnabled(False)
            self.btn_black.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_blue.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_blue.isChecked():
            self.correlator.set_color('blue')

            self.btn_white.setEnabled(False)
            self.btn_black.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_purple.setEnabled(False)
        elif self.btn_purple.isChecked():
            self.correlator.set_color('purple')

            self.btn_white.setEnabled(False)
            self.btn_black.setEnabled(False)
            self.btn_red.setEnabled(False)
            self.btn_orange.setEnabled(False)
            self.btn_yellow.setEnabled(False)
            self.btn_green.setEnabled(False)
            self.btn_blue.setEnabled(False)
        else:
            self.btn_white.setEnabled(True)
            self.btn_black.setEnabled(True)
            self.btn_red.setEnabled(True)
            self.btn_orange.setEnabled(True)
            self.btn_yellow.setEnabled(True)
            self.btn_green.setEnabled(True)
            self.btn_blue.setEnabled(True)
            self.btn_purple.setEnabled(True)

    def setMethod(self):
        """
        Изменение статистического метода обработки изображения
        """
        if self.btn_SQDIFF.isChecked():
            self.correlator.set_method('SQDIFF')
            self.btn_SQDIFF_NORMED.setEnabled(False)
            self.btn_CCOEFF.setEnabled(False)
            self.btn_CCOEFF_NORMED.setEnabled(False)
            self.btn_CCORR.setEnabled(False)
            self.btn_CCORR_NORMED.setEnabled(False)
        elif self.btn_SQDIFF_NORMED.isChecked():
            self.correlator.set_method('SQDIFF_NORMED')
            self.btn_SQDIFF.setEnabled(False)
            self.btn_CCOEFF.setEnabled(False)
            self.btn_CCOEFF_NORMED.setEnabled(False)
            self.btn_CCORR.setEnabled(False)
            self.btn_CCORR_NORMED.setEnabled(False)
        elif self.btn_CCOEFF.isChecked():
            self.correlator.set_method('CCOEFF')
            self.btn_SQDIFF.setEnabled(False)
            self.btn_SQDIFF_NORMED.setEnabled(False)
            self.btn_CCOEFF_NORMED.setEnabled(False)
            self.btn_CCORR.setEnabled(False)
            self.btn_CCORR_NORMED.setEnabled(False)
        elif self.btn_CCOEFF_NORMED.isChecked():
            self.correlator.set_method('CCOEFF_NORMED')
            self.btn_SQDIFF.setEnabled(False)
            self.btn_SQDIFF_NORMED.setEnabled(False)
            self.btn_CCOEFF.setEnabled(False)
            self.btn_CCORR.setEnabled(False)
            self.btn_CCORR_NORMED.setEnabled(False)
        elif self.btn_CCORR.isChecked():
            self.correlator.set_method('CCORR')
            self.btn_SQDIFF.setEnabled(False)
            self.btn_SQDIFF_NORMED.setEnabled(False)
            self.btn_CCOEFF.setEnabled(False)
            self.btn_CCOEFF_NORMED.setEnabled(False)
            self.btn_CCORR_NORMED.setEnabled(False)
        elif self.btn_CCORR_NORMED .isChecked():
            self.correlator.set_method('CCORR_NORMED')
            self.btn_SQDIFF.setEnabled(False)
            self.btn_SQDIFF_NORMED.setEnabled(False)
            self.btn_CCOEFF.setEnabled(False)
            self.btn_CCOEFF_NORMED.setEnabled(False)
            self.btn_CCORR.setEnabled(False)
        else:
            self.btn_SQDIFF.setEnabled(True)
            self.btn_SQDIFF_NORMED.setEnabled(True)
            self.btn_CCOEFF.setEnabled(True)
            self.btn_CCOEFF_NORMED.setEnabled(True)
            self.btn_CCORR.setEnabled(True)
            self.btn_CCORR_NORMED.setEnabled(True)

    def checkMap(self):
        """
        Проверка неоюходимости сохранения тепловой карты
        """
        if self.cbtnMAP.isChecked():
            self.correlator.mp_fl = True
        else:
            self.correlator.mp_fl = False

    def runCorr(self):
        self.correlator.match_img()
        self.correlator.repr_res()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = correlatorWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
