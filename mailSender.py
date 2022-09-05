import os
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QVBoxLayout,QRadioButton,QTextEdit,QFileDialog,QHBoxLayout,QApplication,QAction,qApp,QMainWindow
from PyQt5 import QtWidgets
import smtplib 
from email.mime.multipart import MIMEMultipart ## Mesaj gövdemizi oluşturcak.
from email.mime.text import MIMEText ##Mailimizde ne yazcak bununla yapıcaz.



class Pencere(QWidget):
    
    def __init__(self):
                
        super().__init__()
        self.init_ui()
        
        
    
    def init_ui(self):
        self.ustMail=QLabel("Kimden:")
        self.mail =  QtWidgets.QLineEdit()
        self.ustSifre=QLabel("Şifre:")
        self.sifre=QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ustGonderilenMail=QLabel("Kime:")
        self.gonderilenMail=QtWidgets.QLineEdit()
        self.ustBaslik=QLabel("Konu:")
        self.baslik=QtWidgets.QLineEdit()
        self.ustMailText=QLabel("İçerik:")
        self.mailText=QtWidgets.QTextEdit()
        self.temizle=QtWidgets.QPushButton("Temizle")
        self.gonder=QtWidgets.QPushButton("Gönder")
        
        
        
        #v_box = QVBoxLayout()        
        #v_box.addWidget(self.ustMail)
        #v_box.addWidget(self.mail)
        #v_box.addWidget(self.ustSifre)
        #v_box.addWidget(self.sifre)
        #v_box.addWidget(self.ustGonderilenMail)
        #v_box.addWidget(self.gonderilenMail)
        #v_box.addWidget(self.ustBaslik)
        #v_box.addWidget(self.baslik)
        #v_box.addWidget(self.ustMailText)
        #v_box.addWidget(self.mailText)
        #v_box.addWidget(self.temizle)
        #v_box.addWidget(self.gonder)
        #self.setLayout(v_box)
        
        
        
        h1_box=QHBoxLayout()
        h1_box.addWidget(self.ustMail)
        h1_box.addWidget(self.mail)
        
        h2_box=QHBoxLayout()
        h2_box.addWidget(self.ustSifre)
        h2_box.addWidget(self.sifre)
        
        h3_box=QHBoxLayout()
        h3_box.addWidget(self.ustGonderilenMail)
        h3_box.addWidget(self.gonderilenMail)
        
        h4_box=QHBoxLayout()
        h4_box.addWidget(self.ustBaslik)
        h4_box.addWidget(self.baslik)
        
        h5_box=QHBoxLayout()
        h5_box.addWidget(self.ustMailText)
        h5_box.addWidget(self.mailText)
        
        h6_box=QHBoxLayout()
        h6_box.addWidget(self.temizle)
        h6_box.addWidget(self.gonder)
        
        v_box = QtWidgets.QVBoxLayout()

        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addLayout(h4_box)
        v_box.addLayout(h5_box)
        v_box.addLayout(h6_box)
        
        self.setLayout(v_box)
        
        


        
        
        
        
        self.setWindowTitle("Mail App")
        self.setStyleSheet("background-color:lightblue")
        
        
        
        self.gonder.clicked.connect(self.mailGonder)
        self.temizle.clicked.connect(self.mailTemizle)
        
        self.show()
        
        
    def mailTemizle(self):
        self.mailText.clear()
    
        


    def mailGonder(self):
        mesaj=MIMEMultipart()
        
        
        mesaj["from"]=self.mail.text() ## 'from' yani kimden
        mesaj["to"]=self.gonderilenMail.text() ## 'to' yani kime göndereceğimiz.
        mesaj["Subject"]=self.baslik.text() ##Mail konusu
        
        


        
        




##Üstteki yazımızın bizim mesaj yapımıza gitmesi için gövde yapımıza geçiyoruz: 
        mesajGovdesi=MIMEText(self.mailText.toPlainText(),"plain") ## -!- Mail içeriğimizin yer aldıgı nokta

        mesaj.attach(mesajGovdesi) ##MesajGovdesi'ni mesaj yapısının içine atıyoruz.



        try:
            mail=smtplib.SMTP("smtp.gmail.com",587) ##Tırnak içinde hangi smtp serverına bağlandıgımızı veriyoruz. 2. değerde de hangi porta bağlacagımızın sayısı.
            mail.ehlo() ##Ben sana bağlancam diyoruz.
    
            mail.starttls() ## Kullanıcı adı ve şifremizin şifrelenmesi için.
    
            mail.login(self.mail.text(),self.sifre.text()) ##İlk boşluga kendi mailimizi, 2. boşluga mailimizin şifresini giriyoruz.
    
            mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string()) ##Mesaj yazpımızı stringe çevirmemiz gerekiyordu ondan as.string
    
            print("Mail başarıyla gönderildi.")
    
            mail.close()
    
        except:
            sys.stderr.write("Bir hata oluştu...")
            sys.stderr.flush()






app=QApplication(sys.argv) ## import kısmında QtWidgets'ı yazdıgımız için burada gerek yok.
pencere=Pencere()
sys.exit(app.exec_())
