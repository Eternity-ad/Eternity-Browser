import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
# Please Install This Packages pip install PyQtWebEngine
# pip install PyQt5
# Uttkarsh
# Yash_OP
# Integrity
# AlwaysBees


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.bing.com/?toWww=1&redig=375257EAD25C4BF5AA82551D2405763A'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        navbar2 = QToolBar()
        self.addToolBar(navbar2)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
    # navbar2
        tab1 = QAction('Main', self)
        tab1.triggered.connect(self.main_tab1)
        navbar2.addAction(tab1)
        tab2 = QAction('Incognito', self)
        tab2.triggered.connect(self.main_tab2)
        navbar2.addAction(tab2)
        main3 = QAction('Google', self)
        main3.triggered.connect(self.main_tab3)
        navbar2.addAction(main3)
        main4 = QAction('Yandex', self)
        main4.triggered.connect(self.main_tab4)
        navbar2.addAction(main4)
        main5 = QAction('Yahoo', self)
        main5.triggered.connect(self.main_tab5)
        navbar2.addAction(main5)
        new_btn = QAction('Brave', self)
        new_btn.triggered.connect(self.navigate_tab)
        navbar2.addAction(new_btn)

        new_btn1 = QAction('TicTacToe', self)
        new_btn1.triggered.connect(self.navigate_tab1)
        navbar2.addAction(new_btn1)
        aboutproject1 = QAction('AboutOurProject', self)
        aboutproject1.triggered.connect(self.aboutproject)
        navbar2.addAction(aboutproject1)
#functions
    def navigate_home(self):
        self.browser.setUrl(QUrl('http://yash.brizy.site'))
    def navigate_tab(self):
        self.browser.setUrl(QUrl('https://seach.brave.com'))
    def navigate_tab1(self):
        self.browser.setUrl(QUrl('https://bit.ly/tictactoeop'))
    def main_tab1(self):
        self.browser.setUrl(QUrl('https://www.bing.com/?toWww=1&redig=94F4AABD4CB34B349328F5A428C42C5E'))
    def main_tab2(self):
        self.browser.setUrl(QUrl('https://duckduckgo.com'))
    def main_tab3(self):
        self.browser.setUrl(QUrl('https://google.com'))
    def main_tab4(self):
        self.browser.setUrl(QUrl('https://yandex.com/'))
    def main_tab5(self):
        self.browser.setUrl(QUrl('https://in.search.yahoo.com/?fr2=inr'))
    def aboutproject(self):
        self.browser.setUrl(QUrl('https://bit.ly/aboutinegrity'))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Intergrity Browser')
window = MainWindow()
app.exec_()
