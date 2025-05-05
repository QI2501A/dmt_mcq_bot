@echo off
REM run_quiz.bat — launcher for the DMT MCQ Quiz GUI on Windows

REM Determine the directory containing this script
set "SCRIPT_DIR=%~dp0"

REM Launch the Python script with any arguments passed to this batch file
python "%SCRIPT_DIR%dmt_mcq_quiz_gui.py" %*
