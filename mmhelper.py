#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Medical Manuscript Helper
~~~~~~~~~~~~~~~~~~~~~

An application that can help to create medical manuscript fast and rationally.

:mmhelper.py: Main Program
:copyright: (c) 2018 by Dearfad
:Email: dearfad@sina.com
:license: GPL-v3
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QPushButton, QTextEdit, QVBoxLayout, QGroupBox


class MainWindow(QMainWindow):
    """Main GUI of MmHelper"""

    def __init__(self):
        super().__init__()
        self.menuBar()
        self.groupbox = QGroupBox()
        self.setCentralWidget(self.groupbox)
        self.bt_load = QPushButton('LOAD')
        self.bt_load.clicked.connect(self.loadcsv)
        self.textedit = QTextEdit()
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.textedit)
        self.vlayout.addWidget(self.bt_load)
        self.groupbox.setLayout(self.vlayout)
        # self.statusBar()

    def loadcsv(self):
        """Load .csv File."""
        filepath = QFileDialog.getOpenFileName(
            caption='Load .csv File...',
            filter='CSV File (*.csv)',
        )[0]
        self.textedit.append(filepath)


def main():
    """Main Function."""
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
