@echo off
setlocal

:: this script directory
set DIR=%~dp0
set DIR=%DIR:~0,-1%
set CWD=%CD%

rd /s /q %DIR%\..\build
md %DIR%\..\build
cd %DIR%\..\build
cmake .. -G "Visual Studio 14" -A x64
cmake --build .
cd %CWD%
echo done.
