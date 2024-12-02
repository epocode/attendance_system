@echo off
cd /d "%~dp0"
pyside6-uic ../ui_creator/form.ui -o ../src/ui_main_window.py
pyside6-rcc ../ui_creator/resources.qrc -o ../src/resources.py