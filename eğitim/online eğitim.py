import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QMessageBox, QFileDialog, QInputDialog

class Kurs:
    def __init__(self, ad, egitmen):
        self.ad = ad
        self.egitmen = egitmen
        self.ogrenciler = []

    def kurs_olustur(self):
        QMessageBox.information(None, "Bilgi", f"'{self.ad}' kursu oluşturuldu.")

    def kaydol(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        QMessageBox.information(None, "Bilgi", f"{ogrenci.isim}, '{self.ad}' kursuna kaydoldu.")

    def icerik_yukle(self, dosya_yolu):
        try:
            with open(dosya_yolu, 'r') as dosya:
                icerik = dosya.read()
            QMessageBox.information(None, "Bilgi", f"'{self.ad}' kursunun içeriği yüklendi.")
            return icerik
        except FileNotFoundError:
            QMessageBox.warning(None, "Uyarı", "Dosya bulunamadı.")

class Egitmen:
    def __init__(self, isim, uzmanlik_alani):
        self.isim = isim
        self.uzmanlik_alani = uzmanlik_alani

class Ogrenci:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.kurslar = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Kurs Oluştur
        layout_kurs_olustur = QVBoxLayout()
        lbl_kurs_ad = QLabel("Kurs Adı:")
        self.input_kurs_ad = QLineEdit()
        self.input_kurs_ad.setPlaceholderText("Kurs adını giriniz")
        layout_kurs_olustur.addWidget(lbl_kurs_ad)
        layout_kurs_olustur.addWidget(self.input_kurs_ad)

        lbl_egitmen_isim = QLabel("Eğitmen Adı:")
        self.input_egitmen_isim = QLineEdit()
        self.input_egitmen_isim.setPlaceholderText("Eğitmen adını giriniz")
        layout_kurs_olustur.addWidget(lbl_egitmen_isim)
        layout_kurs_olustur.addWidget(self.input_egitmen_isim)

        lbl_egitmen_uzmanlik = QLabel("Eğitmen Uzmanlık Alanı:")
        self.input_egitmen_uzmanlik = QLineEdit()
        self.input_egitmen_uzmanlik.setPlaceholderText("Eğitmen uzmanlık alanını giriniz")
        layout_kurs_olustur.addWidget(lbl_egitmen_uzmanlik)
        layout_kurs_olustur.addWidget(self.input_egitmen_uzmanlik)

        btn_kurs_olustur = QPushButton("Kurs Oluştur")
        btn_kurs_olustur.clicked.connect(self.kurs_olustur)
        layout_kurs_olustur.addWidget(btn_kurs_olustur)
        layout.addLayout(layout_kurs_olustur)

        # Öğrenci Kaydet
        layout_ogrenci_kaydet = QHBoxLayout()
        lbl_ogrenci_ad = QLabel("Öğrenci Adı:")
        self.input_ogrenci_ad = QLineEdit()
        self.input_ogrenci_ad.setPlaceholderText("Öğrenci adını giriniz")
        layout_ogrenci_kaydet.addWidget(lbl_ogrenci_ad)
        layout_ogrenci_kaydet.addWidget(self.input_ogrenci_ad)

        lbl_ogrenci_email = QLabel("Öğrenci E-posta:")
        self.input_ogrenci_email = QLineEdit()
        self.input_ogrenci_email.setPlaceholderText("Öğrenci e-postasını giriniz")
        layout_ogrenci_kaydet.addWidget(lbl_ogrenci_email)
        layout_ogrenci_kaydet.addWidget(self.input_ogrenci_email)

        btn_ogrenci_kaydet = QPushButton("Öğrenci Kaydet")
        btn_ogrenci_kaydet.clicked.connect(self.ogrenci_kaydet)
        layout_ogrenci_kaydet.addWidget(btn_ogrenci_kaydet)
        layout.addLayout(layout_ogrenci_kaydet)

        # Kurs İçeriği Yükle
        layout_kurs_icerik = QHBoxLayout()
        lbl_kurs_icerik = QLabel("İçeriğini yüklemek istediğiniz kurs numarası:")
        self.input_kurs_icerik = QLineEdit()
        self.input_kurs_icerik.setPlaceholderText("Kurs numarasını giriniz")
        layout_kurs_icerik.addWidget(lbl_kurs_icerik)
        layout_kurs_icerik.addWidget(self.input_kurs_icerik)

        btn_kurs_icerik_yukle = QPushButton("Kurs İçeriği Yükle")
        btn_kurs_icerik_yukle.clicked.connect(self.kurs_icerik_yukle)
        layout_kurs_icerik.addWidget(btn_kurs_icerik_yukle)
        layout.addLayout(layout_kurs_icerik)

        # İçerik Göster
        layout_icerik_goster = QVBoxLayout()
        lbl_icerik_goster = QLabel("Kurs İçeriği:")
        self.text_icerik = QTextEdit()
        layout_icerik_goster.addWidget(lbl_icerik_goster)
        layout_icerik_goster.addWidget(self.text_icerik)
        layout.addLayout(layout_icerik_goster)

        # Kurs Listesi
        self.list_kurslar = QListWidget()
        layout.addWidget(self.list_kurslar)

        self.setLayout(layout)

    def kurs_olustur(self):
        ad = self.input_kurs_ad.text()
        egitmen_isim = self.input_egitmen_isim.text()
        egitmen_uzmanlik = self.input_egitmen_uzmanlik.text()
        egitmen = Egitmen(egitmen_isim, egitmen_uzmanlik)
        kurs = Kurs(ad, egitmen)
        self.kurslar.append(kurs)
        kurs.kurs_olustur()
        self.guncelle_kurs_listesi()

    def ogrenci_kaydet(self):
        ad = self.input_ogrenci_ad.text()
        email = self.input_ogrenci_email.text()
        kurs_numarasi, ok = QInputDialog.getInt(self, "Kurs Seç", "Kaydolmak istediğiniz kurs numarasını giriniz:")
        if ok:
            kurs_numarasi -= 1
            if kurs_numarasi >= 0 and kurs_numarasi < len(self.kurslar):
                ogrenci = Ogrenci(ad, email)
                self.kurslar[kurs_numarasi].kaydol(ogrenci)
            else:
                QMessageBox.warning(self, "Uyarı", "Geçersiz kurs numarası!")

    def kurs_icerik_yukle(self):
        # Mevcut olarak seçili kursu al
        secili_item = self.list_kurslar.currentItem()
        if secili_item:
            index = self.list_kurslar.row(secili_item)
            kurs = self.kurslar[index]

            # Dosya seçme iletişim kutusunu aç ve içerik dosyasını seç
            dosya_yolu, _ = QFileDialog.getOpenFileName(self, "Kurs İçeriği Yükle", "", "Text Files (*.txt)")
            if dosya_yolu:
                with open(dosya_yolu, 'r') as dosya:
                    icerik = dosya.read()
                self.text_icerik.setPlainText(icerik)
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kurs seçin!")

    def guncelle_kurs_listesi(self):
        self.list_kurslar.clear()
        for index, kurs in enumerate(self.kurslar):
            item = QListWidgetItem(f"{index+1}. {kurs.ad}")
            self.list_kurslar.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Arayuz()
    window.setWindowTitle("Kurs Yönetim Sistemi")
    window.show()
    sys.exit(app.exec_())