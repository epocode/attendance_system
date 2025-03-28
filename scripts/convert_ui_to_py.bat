@echo off
cd /d "%~dp0"
pyside6-uic ../ui_creator/form.ui -o ../src/ui/ui_files/ui_main_window.py
pyside6-uic ../ui_creator/login.ui -o ../src/ui/ui_files/ui_login.py
pyside6-rcc ../ui_creator/resources.qrc -o ../src/ui/ui_files/resources_rc.py
pyside6-uic ../ui_creator/admin_window.ui -o ../src/ui/ui_files/ui_admin_window.py

powershell -Command "(Get-Content ../src/ui/ui_files/ui_admin_window.py) -replace 'import resources_rc', 'from src.ui.ui_files import resources_rc' | Set-Content ../src/ui/ui_files/ui_admin_window.py"