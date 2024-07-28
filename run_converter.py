import os
import streamlit
import streamlit.web.cli as stcli
import sys

def resolve_script_path():
    if getattr(sys, 'frozen', False):
        print('Running in a bundle')
        script_dir = sys._MEIPASS
    else:
        print('Running in normal Python environment')
        script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, 'src/converter.py')
    print(f'Script path: {script_path}')
    return script_path

if __name__ == '__main__':
    print('In run.py')
    script_path = resolve_script_path()
    sys.argv = [
        'streamlit',
        'run',
        script_path,
        '--global.developmentMode=false'
    ]
    sys.exit(stcli.main())