from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDir

import sys
import os


class Application:
    def get_date(self):
        qdate = self.form.MyCalendar.selectedDate()
        return f'{qdate.day()}.{qdate.month()}.{qdate.year()}'

    def get_note(self):
        return self.form.NewNote.toPlainText()

    def create_file_note(self):
        date = self.get_date()
        note = self.get_note()
        path = os.path.join(self.notes_dir, f'{date}.txt')

        file = open(path, 'w')
        file.write(note)
        file.close()

    def __init__(self, notes_dir):
        Form, Window = uic.loadUiType(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'mainwindow.ui'))
        self.app = QApplication(sys.argv)
        self.notes_dir = notes_dir
        self.form = Form()
        window = Window()
        
        if not os.path.exists(self.notes_dir):
    	    os.makedirs(self.notes_dir)

        self.form.setupUi(window)
        window.show()

        self.form.AddNote.clicked.connect(self.create_file_note)

        sys.exit(self.app.exec_())


def help():
    print('Run my_notes providing notes directory path:\n', 'run(<your_path>)\n',
          'or with the default value: <directory that contains main.py>/"My Notes"\n', sep='')


def run(notes_dir=os.path.join(f'{QDir.currentPath()}', 'My Notes')):
    Application(notes_dir)
