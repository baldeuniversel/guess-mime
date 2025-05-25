# -*- mode: python ; coding: utf-8 -*-

import os





#
array_data = []
for dirpath, dirnames, filenames in os.walk('assets'):
    # Exclude 'media' dir
    if 'media' not in dirpath:
        for file in filenames:
            datas.append((os.path.join(dirpath, file), os.path.relpath(dirpath, 'assets')))


a = Analysis(
    ['guess_mime/main.py'],
    pathex=[],
    binaries=[],
    datas=array_data,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='guess-mime',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
