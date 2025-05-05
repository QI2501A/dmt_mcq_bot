# DMT MCQ Quiz GUI

This README explains how to set up and run the DMT MCQ Quiz GUI on both macOS/Linux and Windows.

---

## Prerequisites

1. **Python 3.6+**  
   Install from https://python.org if you don’t already have it.

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
   ```

2. **Copy files into the directory**  
   Place `dmt_mcq_quiz_gui.py` and `run_quiz.sh` inside `~/dmt_quiz`.

3. **Make the shell script executable**  
   ```bash
   chmod +x run_quiz.sh
   ```

4. **(Optional) Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install dependencies**  
   If your GUI needs external packages (e.g. `PySimpleGUI`), install them now:
   ```bash
   pip install PySimpleGUI
   ```

6. **Run the quiz**  
   ```bash
   ./run_quiz.sh
   ```
   Or with arguments:
   ```bash
   ./run_quiz.sh --some-option
   ```

---

## Setup on Windows

1. **Create a folder**  
   ```bat
   mkdir C:\dmt_quiz
   cd C:\dmt_quiz
   ```

2. **Copy files into the folder**  
   Place `dmt_mcq_quiz_gui.py` and `run_quiz.bat` inside `C:\dmt_quiz`.

3. **(Optional) Create and activate a virtual environment**  
   ```bat
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install dependencies**  
   ```bat
   pip install PySimpleGUI
   ```

5. **Run the quiz**  
   - Double‑click `run_quiz.bat` in Explorer  
   - Or from Command Prompt:
     ```bat
     cd C:\dmt_quiz
     run_quiz.bat
     ```
   - To pass arguments:
     ```bat
     run_quiz.bat --some-option value
     ```

---

## Troubleshooting

- **“command not found” / “python not recognized”**  
  - Ensure Python is on your `PATH`.  
  - On Windows, during install, check “Add Python to PATH.”

- **Missing modules**  
  ```bash
  pip install <module-name>
  ```

- **Permissions**  
  If `run_quiz.sh` won’t execute, re‑run:
  ```bash
  chmod +x run_quiz.sh
  ```

- **Virtual environment won’t activate**  
  - macOS/Linux: `source venv/bin/activate`  
  - Windows: `venv\Scripts\activate`

---

You’re all set! Enjoy running your DMT MCQ Quiz GUI.
