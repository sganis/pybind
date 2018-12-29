@echo off
setlocal

:: this script directory
set DIR=%~dp0
set DIR=%DIR:~0,-1%
set CWD=%CD%
set BUILD=%1

copy %BUILD%\example.dll %DIR%\..\pack\example\_example.pyd
cd %DIR%\..\pack
C:\Python37\python.exe setup.py sdist bdist_wheel
cd %CWD%
