call .env/Scripts/activate.bat
pyinstaller -F --icon=icon.ico --paths=algorithms/ --paths=.env\Lib\site-packages main.py