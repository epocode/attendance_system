@echo off
cd /d "%~dp0"
pyside6-uic ../ui_creator/form.ui -o ../src/ui/ui_files/ui_main_window.py
pyside6-uic ../ui_creator/login.ui -o ../src/ui/ui_files/ui_login.py
pyside6-rcc ../ui_creator/resources.qrc -o ../src/ui/ui_files/resources.py
