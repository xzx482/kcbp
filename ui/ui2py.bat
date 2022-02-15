@echo off
..\Python39\python.exe -m PyQt5.uic.pyuic  %1 -o %1o.py
if not %errorlevel%==0 pause