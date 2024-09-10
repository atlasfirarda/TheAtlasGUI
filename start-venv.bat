@echo off
title atlasata-code // .venv // 

@rem call to set env variables.
call %~dp0setenv.bat

@rem start .venv ^^
call "%PYTHON_DIR%\Scripts\activate"
cmd /k