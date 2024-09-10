@echo off
title atlasata-code // GUI // 

@rem call to set env variables.
call %~dp0setenv.bat

@rem start code ^^
call "%PYTHON_DIR%\Scripts\activate"
call "%ATLASGUI_DIR%\src\main.py"