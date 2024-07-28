from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

# Path to streamlit runtime in your Python site-packages
# Example: ...Python/Python312/Lib/site-packages/streamlit-packages/streamlit/runtime
datas = [
    ('/Library/Frameworks/Python.framework/Versions/3.11//lib/python3.11/site-packages/streamlit/runtime', './streamlit/runtime')
]
datas += collect_data_files('streamlit')
datas += copy_metadata('streamlit')

a = Analysis(
    ['run_converter.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('src/converter.py', 'src'),
        ('src/transcript_formatter.py', 'src')
    ],
    hiddenimports=['pypandoc'],
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run_converter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run_converter',
)