import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import fpdf
except ImportError:
    install("fpdf")

try:
    import streamlit
except ImportError:
    install("streamlit")

