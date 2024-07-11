import os
import subprocess

if __name__ == "__main__":
    try:
        subprocess.run(['streamlit', 'run', './src/converter.py'])
    except Exception as e:
        print(f"Exception occurred: {e}")