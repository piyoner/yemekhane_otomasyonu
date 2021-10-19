from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        self.sayac = 0.00
        self.sayacYardim = 9.50
        self.fark = 0

    def setUI(self):
        self.setWindowTitle("Yemekhane Otomasyonu")
        self.sonuc = QLabel()
        self.sonucBaslik = QLabel("TOPLAM MİKTAR:")
        self.sonuc2 = QLabel()
        self.sonuc2Baslik = QLabel("ÖDENMESİ GEREKEN FARK:")
        self.sonuc.setFont(QFont("Helvetica",32,QFont.Bold))
        self.sonuc2.setFont(QFont("Helvetica",32,QFont.Bold))
        self.sonucBaslik.setFont(QFont("Helvetica",24))
        self.sonuc2Baslik.setFont(QFont("Helvetica",24))
        #self.sonuc.setAlignment(Qt.AlignCenter)
        #self.sonuc2.setAlignment(Qt.AlignCenter)

        self.setGeometry(0, 0, 1920, 1080)
        #self.setAutoFillBackground(True)

        self.girisetiket = QLabel("Verilen Parayı giriniz: ")
        self.giris = QLineEdit()
        self.paraüstüHesap = QPushButton("Hesapla")
        self.paraüstülabel = QLabel("Para üstü:")
        self.paraüstüsonuc = QLabel()
        self.girisetiket.setFont(QFont("Helvetica",24))
        self.giris.setFont(QFont("Helvetica",24))
        self.paraüstüHesap.setFont(QFont("Helvetica",24))
        self.paraüstülabel.setFont(QFont("Helvetica",24))
        self.paraüstüsonuc.setFont(QFont("Helvetica",24))

        self.temizle = QPushButton("Temizle")
        self.hesapla = QPushButton("Yemek Yardımı Uygula")

        self.corba = QPushButton("Çorba")
        self.pilav = QPushButton("Pilav")
        self.salata = QPushButton("Salata")
        self.makarna = QPushButton("Makarna")
        self.ekmek = QPushButton("Ekmek")
        self.SuBüyük =  QPushButton("Büyük Su ")
        self.SuKücük =  QPushButton("Küçük Su")
        self.MeyveSuyu =    QPushButton("Meyve Suyu")
        self.tavukyemegi =  QPushButton("Tavuk Yemeği")
        self.etyemegi =     QPushButton("Et Yemeği")

        self.corba.setFont(QFont("Helvetica", 32))
        self.pilav.setFont(QFont("Helvetica", 32))
        self.SuBüyük.setFont(QFont("Helvetica", 32))
        self.SuKücük.setFont(QFont("Helvetica", 32))
        self.MeyveSuyu.setFont(QFont("Helvetica", 32))
        self.etyemegi.setFont(QFont("Helvetica", 32))
        self.tavukyemegi.setFont(QFont("Helvetica", 32))
        self.salata.setFont(QFont("Helvetica", 32))
        self.makarna.setFont(QFont("Helvetica", 32))
        self.ekmek.setFont(QFont("Helvetica", 32))
        self.temizle.setFont(QFont("Helvetica",24))
        self.hesapla.setFont(QFont("Helvetica",24))

        h_box_1 = QHBoxLayout()
        h_box_2 = QHBoxLayout()
        h_box_3 = QHBoxLayout()
        h_box_4 = QHBoxLayout()
        h_box_5 = QHBoxLayout()
        h_box_6 = QHBoxLayout()

        h_box_1.addWidget(self.corba)
        h_box_1.addWidget(self.pilav)
        h_box_1.addWidget(self.salata)
        h_box_1.addWidget(self.makarna)
        h_box_1.addWidget(self.ekmek)
        h_box_2.addWidget(self.SuBüyük)
        h_box_2.addWidget(self.SuKücük)
        h_box_2.addWidget(self.MeyveSuyu)
        h_box_2.addWidget(self.tavukyemegi)
        h_box_2.addWidget(self.etyemegi)
        h_box_3.addWidget(self.temizle)
        h_box_3.addWidget(self.hesapla)
        h_box_4.addWidget(self.sonucBaslik)
        h_box_4.addWidget(self.sonuc)
        h_box_5.addWidget(self.sonuc2Baslik)
        h_box_5.addWidget(self.sonuc2)
        h_box_6.addWidget(self.girisetiket)
        h_box_6.addWidget(self.giris)
        h_box_6.addWidget(self.paraüstüHesap)
        h_box_6.addWidget(self.paraüstülabel)
        h_box_6.addWidget(self.paraüstüsonuc)

        v_box = QVBoxLayout()

        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addLayout(h_box_3)
        v_box.addLayout(h_box_4)
        v_box.addLayout(h_box_5)
        v_box.addLayout(h_box_6)

        self.corba.clicked.connect(self.uygula1)
        self.pilav.clicked.connect(self.uygula1)
        self.salata.clicked.connect(self.uygula9)
        self.makarna.clicked.connect(self.uygula2)
        self.ekmek.clicked.connect(self.uygula3)
        self.SuKücük.clicked.connect(self.uygula6)
        self.SuBüyük.clicked.connect(self.uygula4)
        self.MeyveSuyu.clicked.connect(self.uygula5)
        self.tavukyemegi.clicked.connect(self.uygula7)
        self.etyemegi.clicked.connect(self.uygula8)
        self.paraüstüHesap.clicked.connect(self.uygula11)

        self.hesapla.clicked.connect(self.uygula10)
        self.temizle.clicked.connect(self.tz)

        self.setLayout(v_box)

        self.show()

    def tz(self):
        self.sonuc.clear()
        self.sayac = 0.00
        self.sonuc2.clear()
        self.Paraüstü = 0.00
        self.paraüstüsonuc.clear()
        self.giris.clear()
        self.fark = 0.00
    def uygula1(self):
        self.sayac+=3.00
        self.sonuc.setNum(self.sayac)
    def uygula2(self):
        self.sayac+=3.25
        self.sonuc.setNum(self.sayac)
    def uygula3(self):
        self.sayac+=0.35
        self.sonuc.setNum(self.sayac)
    def uygula4(self):
        self.sayac+=1.15
        self.sonuc.setNum(self.sayac)
    def uygula5(self):
        self.sayac+=1.50
        self.sonuc.setNum(self.sayac)
    def uygula6(self):
        self.sayac+=0.60
        self.sonuc.setNum(self.sayac)
    def uygula7(self):
        self.sayac+=6.50
        self.sonuc.setNum(self.sayac)
    def uygula8(self):
        self.sayac+=8.00
        self.sonuc.setNum(self.sayac)
    def uygula9(self):
        self.sayac+=2.50
        self.sonuc.setNum(self.sayac)

    def uygula10(self):
        self.fark = self.sayac - self.sayacYardim
        self.sonuc2.setNum(self.fark)

    def uygula11(self):
        if self.giris.text() == "" or self.fark == 0 or self.giris.text() == str:
            pass
        else:
            try:
                self.Paraüstü = float(self.giris.text()) - self.fark
                self.paraüstüsonuc.setNum(self.Paraüstü)
            except ValueError:
                mesaj = QMessageBox()
                mesaj.setText("Lütfen virgül yerine nokta kullanın.")
                self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())
