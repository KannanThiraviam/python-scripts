# Python Scripts Repository

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-scripts.git
cd python-scripts
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:

On Windows (PowerShell):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

On Windows (Command Prompt):
```cmd
.\venv\Scripts\activate.bat
```

On Unix or MacOS:
```bash
source venv/bin/activate
```

4. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

5. Run Python scripts:
```bash
python your_script.py
```

## Note
- Always activate the virtual environment before running scripts
- To deactivate the virtual environment when done, simply run:
```bash
deactivate
```
