# DMT MCQ Quiz GUI

This README explains how to set up and run the DMT MCQ Quiz GUI on both macOS/Linux and Windows.

---

## Prerequisites

1. **Python 3.6+**  
   Install from [python.org](https://python.org) if you don’t already have it.

2. **Quiz files**  
   - `dmt_mcq_quiz_gui.py` (your main script)  
   - `run_quiz.sh` (for macOS/Linux)  
   - `run_quiz.bat` (for Windows)

---

## Setup on macOS / Linux

1. **Create a directory**  
   ```bash
   mkdir ~/dmt_quiz
   cd ~/dmt_quiz

	2.	Copy files into the directory
Place dmt_mcq_quiz_gui.py and run_quiz.sh inside ~/dmt_quiz.
	3.	Make the shell script executable

chmod +x run_quiz.sh


	4.	(Optional) Create a virtual environment

python3 -m venv venv
source venv/bin/activate


	5.	Install dependencies
If your GUI needs external packages (e.g. PySimpleGUI), install them now:

pip install PySimpleGUI


	6.	Run the quiz

./run_quiz.sh

Or, to pass arguments:

./run_quiz.sh --some-option



⸻

Setup on Windows
	1.	Create a folder

mkdir C:\dmt_quiz
cd C:\dmt_quiz


	2.	Copy files into the folder
Place dmt_mcq_quiz_gui.py and run_quiz.bat inside C:\dmt_quiz.
	3.	(Optional) Create and activate a virtual environment

python -m venv venv
venv\Scripts\activate


	4.	Install dependencies

pip install PySimpleGUI


	5.	Run the quiz
	•	Double‑click run_quiz.bat in Explorer
	•	Or from Command Prompt:

cd C:\dmt_quiz
run_quiz.bat


	•	To pass arguments:

run_quiz.bat --some-option value



⸻

Troubleshooting
	•	“command not found” / “python not recognized”
	•	Ensure Python is on your PATH.
	•	On Windows, during install, check “Add Python to PATH.”
	•	Missing modules

pip install <module-name>


	•	Permissions
If run_quiz.sh won’t execute, re‑run:

chmod +x run_quiz.sh


	•	Virtual environment won’t activate
	•	macOS/Linux: source venv/bin/activate
	•	Windows: venv\Scripts\activate

⸻

You’re all set! Enjoy running your DMT MCQ Quiz GUI.
