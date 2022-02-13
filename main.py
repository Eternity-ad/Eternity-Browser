import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

import os
import sys

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
        file_menu = self.menuBar().addMenu("&File")

        save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

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
# ========================================================================================================================
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
# =========================================================================================================================
        new_btn1 = QAction('TicTacToe', self)
        new_btn1.triggered.connect(self.navigate_tab1)
        navbar2.addAction(new_btn1)
        aboutproject1 = QAction('AboutOurProject', self)
        aboutproject1.triggered.connect(self.aboutproject)
        navbar2.addAction(aboutproject1)
        ninjagame = QAction('Knife Master', self)
        ninjagame.triggered.connect(self.ninjagamebtn)
        navbar2.addAction(ninjagame)
        bullseye = QAction('Bow Master', self)
        bullseye.triggered.connect(self.bullseyef)
        navbar2.addAction(bullseye)
        flipgame = QAction('Flip Game', self)
        flipgame.triggered.connect(self.flipgamef)
        navbar2.addAction(flipgame)
        rimage = QAction('RandomImage', self)
        rimage.triggered.connect(self.randomimagef)
        navbar2.addAction(rimage)
# =========================================================================================================================
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
    def ninjagamebtn(self):
        self.browser.setUrl(QUrl('https://bit.ly/ninjagamebtn'))
    def bullseyef(self):
        self.browser.setUrl(QUrl('https://bit.ly/bullseyegameop'))
    def flipgamef(self):
        self.browser.setUrl(QUrl('https://bit.ly/flipgameop'))
    def randomimagef(self):
        self.browser.setUrl(QUrl('https://bit.ly/randomimagebyyash'))

# ====================================================================================================================

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.tabs.currentWidget().setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            html = self.tabs.currentWidget().page().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))
# =================================================================================================================
app = QApplication(sys.argv)
QApplication.setApplicationName('Intergrity Browser')
window = MainWindow()
app.exec_()
