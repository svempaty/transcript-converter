import os
import subprocess
import sys

# Determine the path to the directory containing the script
if getattr(sys, 'frozen', False):
    # If running from a PyInstaller bundle
    script_dir = sys._MEIPASS
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    test_script_path = os.path.join(script_dir, './src/converter.py')

    try:
        subprocess.run(['streamlit', 'run', test_script_path])
    except Exception as e:
        print(f"Exception occurred: {e}")