# -*- mode: python ; coding: utf-8 -*-
import os
import sys

# onefile 실행 시 python3xx.dll 누락 방지: base/venv/Scripts 등에서 DLL 명시 포함
binaries_extra = []
_search_dirs = [
    getattr(sys, 'base_prefix', sys.prefix),
    sys.prefix,
    os.path.dirname(sys.executable),
    os.path.join(getattr(sys, 'base_prefix', sys.prefix), 'Scripts'),
    os.path.join(sys.prefix, 'Scripts'),
]
_dll_names = ['python312.dll', 'python311.dll', 'python310.dll', 'python3.dll']
_seen = set()
for d in _search_dirs:
    if not d or not os.path.isdir(d):
        continue
    for name in _dll_names:
        dll = os.path.normpath(os.path.join(d, name))
        if dll in _seen:
            continue
        if os.path.isfile(dll):
            binaries_extra.append((dll, '.'))
            _seen.add(dll)

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries_extra,
    datas=[('index.html', '.')],
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
    name='Heartowiki',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
