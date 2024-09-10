@rem set environment variables

set ROOT_DIR=%~dp0
set ATLASGUI_DIR=%ROOT_DIR%master
set PYTHON_DIR=%ROOT_DIR%master\.venv
set MINGIT_DIR=%ROOT_DIR%git
set FFMPEG_DIR=%ROOT_DIR%master\src\ffmpeg
set NCNN_DIR=%ROOT_DIR%master\src\ncnn
set WINRAR_DIR=C:\Program Files\WinRAR
set PATH=C:\Windows\system32;C:\Windows;C:\WINDOWS\System32\WindowsPowerShell\v1.0;%PYTHON_DIR%;%PYTHON_DIR%\Scripts;%MINGIT_DIR%\cmd;%FFMPEG_DIR%;%NCNN_DIR%;%WINRAR_DIR%;%ATLASGUI_DIR%;

@rem clear python related variables
set PYTHONHOME=
set PYTHONPATH=
set PYTHONSTARTUP=
set PYTHONUSERBASE=
set PYTHONEXECUTABLE=
set PIP_TARGET=

@rem git env
set GIT_CONFIG_NOSYSTEM=1
