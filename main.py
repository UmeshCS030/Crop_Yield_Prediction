import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).parent
PYTHON = ROOT / "venv" / "Scripts" / "python.exe"

backend = subprocess.Popen(
    [
        str(PYTHON),
        "-m",
        "uvicorn",
        "app:app",
        "--reload",
    ],
    cwd=ROOT / "backend",
)

time.sleep(2)

frontend = subprocess.Popen(
    [
        str(PYTHON),
        "-m",
        "streamlit",
        "run",
        "Home.py",
    ],
    cwd=ROOT / "frontend",
)

backend.wait()
frontend.wait()