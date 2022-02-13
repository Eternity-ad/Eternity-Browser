import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
# Please Install This Packages pip install PyQtWebEngine
# pip install PyQt5
# Yash_OP
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

        new_btn = QAction('Google', self)
        new_btn.triggered.connect(self.navigate_tab)
        navbar.addAction(new_btn)

        new_btn1 = QAction('Brave', self)
        new_btn1.triggered.connect(self.navigate_tab1)
        navbar.addAction(new_btn1)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://yash.brizy.site'))
    def navigate_tab(self):
        self.browser.setUrl(QUrl('https://google.com'))
    def navigate_tab1(self):
        self.browser.setUrl(QUrl('https://search.brave.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Fastest Browser')
window = MainWindow()
app.exec_()
